document.addEventListener('DOMContentLoaded', function() {
    const fruitDisplay = document.getElementById('fruit-display');
    const button = document.getElementById('get-fruit-button');
    fetch('/proxy/5000/get_fruit')
        .then(response => response.json())
        .then(data => {
            data.fruits.forEach(fruit => {
                const imgElement = document.createElement('img');
                imgElement.src = fruit;
                imgElement.alt = 'Fruit Image';
                imgElement.style.width = '100px'; // Adjust as needed
                imgElement.style.height = 'auto'; // Maintain aspect ratio
                fruitDisplay.appendChild(imgElement);
            });
        });
   
    button.addEventListener('click', function() {
        fetch('/proxy/5000/get_fruit')
            .then(response => response.json())
            .then(data => {
                while (fruitDisplay.firstChild) {
                    fruitDisplay.removeChild(fruitDisplay.firstChild);
                }
                data.fruits.forEach(fruit => {
                    const imgElement = document.createElement('img');
                    imgElement.src = fruit;
                    imgElement.alt = 'Fruit Image';
                    imgElement.style.width = '100px'; // Adjust as needed
                    imgElement.style.height = 'auto'; // Maintain aspect ratio
                    fruitDisplay.appendChild(imgElement);
                });
            });
        });
    });


