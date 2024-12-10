import logging
import time
import data_fetcher  # Import the data fetcher module

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

def generate_html(animals_data):
    """Generates HTML for animal cards"""
    logging.debug("Generating HTML content for animals...")
    html = ""
    for animal in animals_data:
        html += '<li class="cards__item">'
        html += f'<div class="card__title">{animal.get("name", "Unknown Animal")}</div>'
        html += '<p class="card__text">'
        characteristics = animal.get("characteristics", {})
        
        # Add the diet
        html += f'<strong>Diet:</strong> {characteristics.get("diet", "Unknown")}<br>'
        
        # Add the locations
        locations = animal.get("locations", ["Unknown"])
        html += f'<strong>Location:</strong> {", ".join(locations)}<br>'
        
        # Add the type (from characteristics or direct field)
        animal_type = animal.get("type") or characteristics.get("type", "Unknown")
        html += f'<strong>Type:</strong> {animal_type}<br>'
        
        html += '</p></li>'
    
    logging.debug(f"Generated HTML for {len(animals_data)} animals.")
    return html

def write_html(html_content):
    """Inserts animal HTML into a template"""
    logging.debug("Reading template HTML...")
    with open('animals_template.html', 'r') as template_file:
        template = template_file.read()
    
    # Replace placeholder with generated HTML content
    logging.debug("Replacing placeholder with generated animal HTML...")
    html_output = template.replace('__REPLACE_ANIMALS_INFO__', html_content)
    
    logging.debug("Writing to animals.html...")
    with open('animals.html', 'w') as output_file:
        output_file.write(html_output)
    logging.debug("HTML file written to animals.html.")

def main():
    # Ask the user for an animal name
    animal_name = input("Please enter an animal: ")
    
    # Fetch data from the API using the data_fetcher
    animals_data = data_fetcher.fetch_data(animal_name)
    
    if animals_data:
        # Generate the HTML content for the animal cards
        html_content = generate_html(animals_data)
        
        # Write the generated HTML into a new file
        write_html(html_content)
    else:
        print(f"The animal '{animal_name}' doesn't exist or there was an error fetching the data.")

if __name__ == "__main__":
    logging.debug("Script is starting...")
    main()
