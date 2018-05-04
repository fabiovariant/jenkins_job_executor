from src.server import handler

def main():
    handler.app.run(port=8076)

if __name__ == '__main__':
    main()