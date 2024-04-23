from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/')
def home():
    dump_me = request.args.get("dump_me")
    if not dump_me:
        return "(╯°□°）╯", 400

    try:
        with open(dump_me, "r") as file:
            content = file.read().strip()
            return content, 200
    except Exception as e:
        return f"Nah.\n{e}", 500

if __name__ == "__main__":
    app.run(debug=False)
