// Function to create a dropdown
function createDropdown(labelText, id, name, options) {
  const group = document.createElement("div");
  group.className = "input-group mb-3";

  const label = document.createElement("label");
  label.className = "input-group-text";
  label.htmlFor = id;
  label.textContent = labelText;

  const select = document.createElement("select");
  select.className = "form-select";
  select.id = id;
  select.name = name;

  // Add placeholder option
  const placeholderOption = document.createElement("option");
  placeholderOption.value = "";
  placeholderOption.selected = true;
  placeholderOption.disabled = true;
  placeholderOption.textContent = "Choose...";
  select.appendChild(placeholderOption);

  // Add cities options
  options.forEach(city => {
    const option = document.createElement("option");
    option.value = city;
    option.textContent = city;
    select.appendChild(option);
  });

  group.appendChild(label);
  group.appendChild(select);
  return group;
}

// Function to create a date picker
function createDatePicker(labelText, id, name) {
  const group = document.createElement("div");
  group.className = "mb-3";

  const label = document.createElement("label");
  label.htmlFor = id;
  label.textContent = labelText;
  label.style.marginRight = '10px';

  const input = document.createElement("input");
  input.type = "date";
  input.id = id;
  input.name = name;

  // Date restrictions - between 14 and 300 days from today
  const today = new Date();
  const formatDateString = (date) => date.toISOString().slice(0, 10);

  const minDate = new Date(today);
  minDate.setDate(today.getDate() + 14);
  const maxDate = new Date(today);
  maxDate.setDate(today.getDate() + 300);

  const minDateStr = formatDateString(minDate);
  const maxDateStr = formatDateString(maxDate);

  input.min = minDateStr;
  input.max = maxDateStr;

  group.appendChild(label);
  group.appendChild(input);
  return group;
}

export function chooseCitiesAndDatesForm(containerId) {
  const container = document.getElementById(containerId);

  if (!container) {
    console.error(`Container with ID "${containerId}" not found.`);
    return;
  }

  // Create form
  const form = document.createElement("form");
  form.action = "/info";
  form.method = "POST";

  // Cities list
  const cities = ["New York City", "Mumbai", "London", "Barcelona", "Tel Aviv"];

  // Add dropdowns
  form.appendChild(createDropdown("I'm leaving from", "sourceCities", "sourceCities", cities));
  form.appendChild(createDropdown("I'm arriving at", "destinationCities", "destinationCities", cities));

  // Add date pickers
  const arrivalGroup = createDatePicker("Arrival date:", "arrivalDatePicker", "arrivalDatePicker");
  const departureGroup = createDatePicker("Departure date:", "departureDatePicker", "departureDatePicker");

  form.appendChild(arrivalGroup);
  form.appendChild(departureGroup);

  // Add submit button
  const buttonGroup = document.createElement("div");
  buttonGroup.className = "input-group mb-5";

  const submitButton = document.createElement("button");
  submitButton.type = "submit";
  submitButton.style.marginTop = '20px';
  submitButton.className = "btn btn-primary";
  submitButton.textContent = "Get Travel Info";

  buttonGroup.appendChild(submitButton);
  form.appendChild(buttonGroup);

  // Append form to container
  container.appendChild(form);
}
