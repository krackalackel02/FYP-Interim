from pybtex.database import parse_file

def generate_ieee_refs(bib_file_path, output_path):
    # Parse the BibTeX file
    bib_data = parse_file(bib_file_path)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, (entry_key, entry) in enumerate(bib_data.entries.items(), start=1):
            try:
                # 1. Format Authors (Firstname Lastname)
                authors = entry.persons.get('author', [])
                author_list = []
                for person in authors:
                    first_names = " ".join(person.first_names)
                    last_names = " ".join(person.last_names)
                    author_list.append(f"{first_names} {last_names}".strip())
                
                author_str = ", ".join(author_list)
                if author_str and not author_str.endswith('.'):
                    author_str += "."

                # 2. Extract Title and strip BibTeX brackets
                title = entry.fields.get('title', '').replace('{', '').replace('}', '')
                if title and not title.endswith('.'):
                    title += "."

                # 3. Extract Source (Checks journal, institution, school, publisher, etc.)
                source = entry.fields.get('journal', 
                         entry.fields.get('institution',
                         entry.fields.get('school',
                         entry.fields.get('publisher', 
                         entry.fields.get('howpublished', '')))))
                
                # 4. Extract Year
                year = entry.fields.get('year', '')
                
                # 5. Format the Source and Year with a comma (e.g., "Imperial College London, 2024.")
                source_year = ""
                if source and year:
                    source_year = f"{source}, {year}."
                elif source:
                    source_year = f"{source}."
                elif year:
                    source_year = f"{year}."

                # Assemble the final string
                components = [author_str, title, source_year]
                final_text = " ".join([c for c in components if c])
                
                # Write to file with a TAB (\t) for clean indentation in PowerPoint
                f.write(f"[{i}]\t{final_text}\n")
                
            except Exception as e:
                print(f"Skipped {entry_key} due to missing fields: {e}")

# Run the function (Make sure your .bib file name matches here)
generate_ieee_refs('my_references.bib', 'formatted_refs.txt')