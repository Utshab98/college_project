fetch('http://127.0.0.1:8000/ticket/?format=api')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
