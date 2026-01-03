async function KirimData() {
    const urlInput = document.getElementById("url").value;
    const statusP  = document.getElementById('status');
    
    if(!urlInput) {
        alert("masukkan link yang benar dulu bos!");
        return;
    }

    statusP.innerText = "Mendownload...";

    try{
        const response = await fetch('/download', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'url=' + encodeURIComponent(urlInput)
        });

        const hasil = await response.text();
        statusP.innerText = hasil;
    } catch(error){
        statusP.innerText = 'terjadi kesalahan...';
    }
}