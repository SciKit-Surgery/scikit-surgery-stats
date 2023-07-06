"""Functions to write html"""
import os.path
import json


def adjustHeaders(head, available_badges):
    # Define the opening and closing tags for table head
    opening_tag = '<table id="highscoretable">'
    closing_tag = "</thead>"

    # Find the start and end indexes of the table head section
    start_index = head.find(opening_tag) + len(opening_tag)
    end_index = head.find(closing_tag, start_index)

    # Extract the table head section
    table_head = head[start_index:end_index]

    # Split the table head into individual table headers
    table_headers = table_head.split("<th")

    # Adjust the width and filter out unwanted table headers
    updated_table_headers = []
    for header in table_headers:
        if (
            any(keyword in header for keyword in available_badges)
            and header != "Library"
        ):
            # Adjust the width by dividing it by the number of available badges
            width_index = header.find('style="width:') + len('style="width:')
            width_end_index = header.find('">', width_index)
            width = float(header[width_index:width_end_index])
            width /= len(available_badges)
            header = header[:width_index] + str(width) + header[width_end_index:]

            updated_table_headers.append(header)

    # Combine the updated table headers back into a single string
    updated_table_head = "<th".join(updated_table_headers)

    # Replace the original table head with the updated version
    updated_head = head[:start_index] + updated_table_head + head[end_index:]

    return updated_head


def load_cache_file(filename):
    """Loads lines of code data from filename, stripping
    var_name from the front
    """
    ret_dict = {}
    try:
        with open(filename, "r") as filein:
            try:
                jsontext = filein.read().split("=")[1]
                ret_dict = json.loads(jsontext)
            except json.JSONDecodeError:
                raise json.JSONDecodeError
            except IndexError:
                raise IndexError
    except FileNotFoundError:
        pass

    return ret_dict


def make_html_file(package, jsfile, template_file="templates/loc_plot.html"):
    """Write Lines of Code information to html files of each library stored under /libraries/"""
    # create dir if not existing
    try:
        os.mkdir("loc/")
    except FileExistsError:
        pass

    with open(template_file, "r") as filein:
        template = filein.read()

    with_title = template.replace("PAGE_TITLE", str(package + " Lines of Code"))
    with_heading = with_title.replace(
        "CHART_HEADING", str(package + " Lines of Code vs Date")
    )
    with_data = with_heading.replace("PATH_TO_DATA", str("../" + jsfile))

    with open(str("loc/" + package + ".html"), "w") as fileout:
        fileout.write(with_data)


def write_to_js_file(data, fileout):
    """Write git hashes and date information to js files of each library stored under /libraries/"""
    outstring = str("var loc_data = " + json.dumps(data))
    with open(fileout, "w") as fileout:
        fileout.write(outstring)


def WriteCellWithLinkedImage(fileout, image=None, link=None, alt_text=None):
    """
    Write a cell to fileout with image and link
    if image is none it writes an empty cell
    """
    fileout.write("    <td>\n")
    if image is not None:
        fileout.write(str('      <a href="' + str(link) + '">\n'))
        fileout.write(
            str('        <img src="' + str(image) + '" alt="' + alt_text + '">\n')
        )
        fileout.write(str("      </a>\n"))
    fileout.write("    </td>\n")
