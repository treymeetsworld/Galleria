const fileInput = document.getElementById('file-input1')
const fileName = document.getElementById('file-name1')

fileInput.addEventListener('change', evt => {
  const fileToUpload = evt.target.files[0].name
  if(fileToUpload) {
    fileName.innerText = fileToUpload
  } else {
    fileName.innerText = ""
  }
})