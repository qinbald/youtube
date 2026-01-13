async function KirimData() {
    const urlInput = document.getElementById("url").value;
    const statusP  = document.getElementById('status');
    const lirikBox = document.getElementById('lirik-box');
    
    if(!urlInput) {
        alert("masukkan link yang benar dulu bos!");
        return;
    }

    statusP.innerText = "Mendownload & Mencari Lirik...";

    try{
        const response = await fetch('/download', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'url=' + encodeURIComponent(urlInput)
        });

        const hasil = await response.json();
        
        if(hasil.error) {
            statusP.innerText = "Error: " + hasil.error;
        } else {
            statusP.innerText = "Selesai: " + hasil.judul;
            lirikBox.innerText = hasil.lirik;
        }
    } catch(error){
        statusP.innerText = 'Terjadi kesalahan sistem...';
    }
}