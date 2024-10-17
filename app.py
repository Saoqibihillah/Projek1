from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Buat list kosong untuk menyimpan bucket list
bucket_list = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form["bucket_give"]
    num = len(bucket_list) + 1  # Nomor urut item
    doc = {
        'num': num,
        'bucket': bucket_receive,
        'done': 0
    }
    bucket_list.append(doc)  # Tambahkan item ke list
    return jsonify({'msg': 'Item saved successfully!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['bucket_done']
    # Cari item berdasarkan nomor dan tandai sebagai selesai
    for bucket in bucket_list:
        if bucket['num'] == int(num_receive):
            bucket['done'] = 1
            break
    return jsonify({'msg': 'Item marked as done!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    # Kirim bucket list sebagai respon JSON
    return jsonify({'buckets': bucket_list})

@app.route("/bucket/delete", methods=["POST"])
def bucket_delete():
    num_receive = request.form['num_give']
    # Cari item berdasarkan nomor dan hapus dari bucket_list
    global bucket_list  # Untuk memastikan kita menggunakan bucket_list global
    bucket_list = [bucket for bucket in bucket_list if bucket['num'] != int(num_receive)]
    return jsonify({'msg': 'Item deleted successfully!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
