# KD Sales ERP V2.1

알루미늄 방범창 계산방식이 2가지로 구분됩니다.

## 소비자용 · 스마트스토어
- 기본 상품가격: 14,000원
- 가로 옵션 추가금
- 세로 옵션 추가금
- 조립 요청: 20,000원
- 수량 자동 합산

## 업체용
- 계산칸수 = 가로(mm) × 세로(mm) ÷ 90,000 후 올림
- 업체 단가 = 계산칸수 × 4,000원
- 수량 자동 합산

GitHub `kd-sales` 저장소에 압축파일의 모든 파일과 폴더를 덮어쓰세요.

필수 구조:
- index.html
- pipe-price.json
- data/aluminum-window-options.json
- tools/convert_aluminum_options.py
