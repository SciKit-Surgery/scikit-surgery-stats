"""Functions to write html"""
import os.path
import json


def load_cache_file(filename):
    """Loads lines of code data from filename, stripping
    var_name from the front
    """
    ret_dict = {}
    try:
        with open(filename, "r") as filein:
            file_content = filein.read()
            # If there is a file but there are no hash entries inside i.e. the first time this functionality is run
            if len(file_content) == 0:
                return ret_dict
            try:
                jsontext = file_content.split("=")[1]
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
