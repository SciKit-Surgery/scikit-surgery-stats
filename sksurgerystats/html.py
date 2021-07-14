"""Functions to write html"""

def WriteCellWithLinkedImage(fileout, image = None, link = None, 
                             alt_text = None):
    """
    Write a cell to fileout with image and link
    if image is none it writes an empty cell
    """
    fileout.write('    <td>\n')
    if image is not None:
        fileout.write(str('      <a href="' + str(link) + '">\n'))
        fileout.write(str('        <img src="' + str(image) + '" alt="' +
                          alt_text + '">\n'))
        fileout.write(str('      </a>\n'))
    fileout.write('    </td>\n')


