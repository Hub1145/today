
import asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')
    await sio.emit('start_bot', {})
    print('start_bot event sent')
    await sio.disconnect()

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('http://localhost:5000')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())
