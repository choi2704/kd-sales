"""
네이버 스마트스토어 추가상품 엑셀(.xls)을
data/aluminum-window-options.json으로 변환합니다.

사용:
python tools/convert_aluminum_options.py supplementProduct.xls
"""
from pathlib import Path
import xlrd, json, re, sys

src = Path(sys.argv[1])
out = Path(__file__).resolve().parents[1] / "data" / "aluminum-window-options.json"

book = xlrd.open_workbook(str(src))
sheet = book.sheet_by_index(0)

widths, heights = {}, {}
assembly = 0

for row in range(1, sheet.nrows):
    name = str(sheet.cell_value(row, 0)).strip()
    value = str(sheet.cell_value(row, 1)).strip()
    price = int(float(sheet.cell_value(row, 2) or 0))
    enabled = str(sheet.cell_value(row, 4)).strip().upper()
    if enabled != "Y":
        continue
    if name.startswith("가로"):
        widths[str(int(re.sub(r"\D", "", value)))] = price
    elif name.startswith("세로"):
        heights[str(int(re.sub(r"\D", "", value)))] = price
    elif name == "조립요청":
        assembly = price

data = {
    "productName": "알루미늄 방범창",
    "productUrl": "https://smartstore.naver.com/kangdongjavara/products/13590585371",
    "baseSizeCm": {"width": 60, "height": 60},
    "basePrice": 14000,
    "businessUnitPrice": 4000,
    "assemblyPrice": assembly,
    "currency": "KRW",
    "widthOptions": widths,
    "heightOptions": heights,
    "sourceFile": src.name
}
out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(out)
