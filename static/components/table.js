export function populateCityTable(cityDetails) {
  const imageNames = ['currency', 'time', 'plug', 'emergency', 'language']

  const imageRow = document.getElementById('image-row');
  const descriptionRow = document.getElementById('description-row');

  // Loop through city details and append them to the table
  cityDetails.forEach((value, index) => {
    // Create image cell
    const imageCell = document.createElement('td');
    imageCell.classList.add('image-cell', 'align-top');
    const img = document.createElement('img');
    img.src = `../static/icons/${imageNames[index]}.png`;
    img.width = 100;
    imageCell.appendChild(img);
    imageRow.appendChild(imageCell);

    // Create description cell
    const descriptionCell = document.createElement('td');
    descriptionCell.classList.add('image-cell', 'align-top');
    descriptionCell.style.marginLeft = '25px';
    descriptionCell.style.marginRight = '25px';    
    descriptionCell.innerHTML = value.replace(/\n/g, '<br />');
    descriptionRow.appendChild(descriptionCell);
  });
}
