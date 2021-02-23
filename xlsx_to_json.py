import xlrd

IN_FILE_PATH = './statics/test.xlsx'
OUT_FILE_PATH = './statics/test.json'
START_POSITION = 4
END_POSITION = 33
REFERENCE_INDEX = 0
DESCRIPTION_INDEX = 1
UNITY_INDEX = 2
QUANTITY_INDEX = 3
LEVEL_INDICATION = '.'
SECTION_TYPE = "SECTION"
CELL_TYPE = "CELL"


def extract_section(rows, row_idx):
    """
    extract section type data.
    :param rows: object in the given row and column
    :param row_idx: row index
    :return: dict: data of section
    """
    reference = rows(row_idx, 0).value
    description = rows(row_idx, 1).value
    level = reference.count(LEVEL_INDICATION)
    return dict(
        reference=reference,
        description=description,
        level=level
    )


def extract_cell(rows, row_idx):
    """
    extract cell type data.
    :param rows: object in the given row and column
    :param row_idx: row index
    :return: dict: data of cell
    """
    description = rows(row_idx, DESCRIPTION_INDEX).value
    unity = rows(row_idx, UNITY_INDEX).value
    quantity = rows(row_idx, QUANTITY_INDEX).value
    return dict(
        description=description,
        unity=unity,
        quantity=quantity,
    )


def xlsx_to_dict(path):
    """
    convert xlsx data to list data.
    :param path: object in the given row and column
    :return: list: list of data
    """
    items = []
    try:
        book = xlrd.open_workbook(path)
        sh = book.sheet_by_index(0)
    except xlrd.XLRDError:
        raise Exception('Invalid file type!')

    for row_idx in range(START_POSITION, END_POSITION):
        # extract order and work item
        reference = sh.cell(row_idx, 0).value
        work = sh.cell(row_idx, 1).value

        # check if empty row
        if not reference and not work:
            continue

        row_type = SECTION_TYPE
        extraction_func = extract_section
        # check if row type is cell
        if not reference:
            row_type = CELL_TYPE
            extraction_func = extract_cell

        extract_data = extraction_func(sh.cell, row_idx)
        extract_data.update(type=row_type, order=len(items))
        items.append(extract_data)
    return items


def save_data(file_path, data):
    import json
    with open(file_path, 'w') as fp:
        json.dump(data, fp)


if __name__ == '__main__':
    items = xlsx_to_dict(IN_FILE_PATH)
    save_data(OUT_FILE_PATH, items)
