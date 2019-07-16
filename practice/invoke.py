import json
import uuid
import asyncio
from aio_pika import connect, IncomingMessage, Message, ExchangeType


class SSFRpcClient:
    def __init__(self, loop):
        self.connection = None
        self.channel = None
        self.callback_queue = None
        self.futures = {}
        self.loop = loop

    async def connect(self):
        self.connection = await connect(
            "amqp://island:devenv@localhost:5672", loop=loop
        )
        self.channel = await self.connection.channel()
        self.callback_queue = await self.channel.declare_queue(
            exclusive=True
        )
        await self.callback_queue.consume(self.on_response)

        return self

    def on_response(self, message: IncomingMessage):
        future = self.futures.pop(message.correlation_id)
        future.set_result(message.body)

    async def call(self):
        correlation_id = str(uuid.uuid4())
        future = loop.create_future()

        self.futures[correlation_id] = future

        exchange = await self.channel.declare_exchange(
            'disconnectSSFUser', ExchangeType.DIRECT, auto_delete=True
        )
        await exchange.publish(
            Message(
                json.dumps({'accountId': 'a1'}).encode('utf8'),
                content_type='application/json',
                correlation_id=correlation_id,
                reply_to=self.callback_queue.name,
            ),
            routing_key='0',
        )

        return str(await future)


async def main(loop):
    rpc = await SSFRpcClient(loop).connect()
    print(" [x] Requesting ssf fetch relay servers")
    response = await rpc.call()
    print(" [.] Got %r" % response)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))