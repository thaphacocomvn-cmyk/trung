# Hướng dẫn cho Codex – Landing page Webcake (Thảo Dược Thaphaco)

Trả lời và ghi chú bằng **tiếng Việt**. Người giao việc là nhân viên, không phải lập trình viên. Hãy giải thích ngắn gọn, dễ hiểu.

## 1. Cấu trúc repo
- `pke-goc/`: file .pke gốc xuất từ Webcake. **Không sửa trực tiếp.**
- `pke-moi/`: file .pke đã chỉnh, để nhân viên tải về và import lại vào Webcake.
- `tools/pke_tool.py`: công cụ chuyển .pke ↔ JSON (cần `pip install msgpack`).
- `.agents/skills/`: các skill. Skill nội dung bán hàng: cro, copywriting, copy-editing, offers, popups, marketing-psychology, product-marketing. Skill giao diện: ui-ux-pro-max.
- `mockup/`: bản mẫu HTML khi cần thiết kế lại hẳn.

## 2. Quy trình sửa file .pke
1. `python tools/pke_tool.py kiem-tra pke-goc/<ten>.pke` để kiểm tra file gốc.
2. `python tools/pke_tool.py liet-ke pke-goc/<ten>.pke` để xem toàn bộ chữ trên trang.
3. `python tools/pke_tool.py giai-nen pke-goc/<ten>.pke` để tạo file JSON. Chỉ sửa trong file JSON này bằng script Python, không sửa tay hàng loạt.
4. `python tools/pke_tool.py dong-goi pke-goc/<ten>.json`, rồi chuyển file `.moi.pke` vào `pke-moi/`.
5. Xoá file JSON trung gian. Cuối task, liệt kê **từng thay đổi** (trước → sau, section nào).

### Cấu trúc dữ liệu
- `source.page` là danh sách section, `source.popup` là danh sách popup. Mỗi phần tử có `children` lồng nhau.
- Chữ nằm ở `specials.text`.
- Kiểu dáng nằm ở `responsive.mobile.styles` và `responsive.desktop.styles`. **Phải sửa cả hai** khi đổi màu hoặc font.
- Màu ghi dạng `rgba(r, g, b, a)`. Font ghi dạng `"Playfair Display", serif`. Font chung của trang nằm ở `source.settings.fontGeneral`.
- Chiều rộng trang: mobile 420px, desktop 960px.

### Được phép sửa
Chữ, giá, % ưu đãi, màu (`color`, `background` dạng màu, `borderColor`), font (`fontFamily`, `fontSize`, `fontWeight`, `lineHeight`), bo góc, đổ bóng, link và các lựa chọn trong form.

### Không tự ý sửa (chỉ sửa khi được yêu cầu rõ ràng)
- Toạ độ và kích thước: `top`, `left`, `width`, `height`. Nếu chữ dài hơn, giữ khung cũ và báo lại để người dùng chỉnh vị trí trong Webcake.
- Link ảnh, vì ảnh phải là link CDN của Webcake (`content.pancake.vn`).
- `extra_script` và mã tracking (Facebook, TikTok).
- Các trường `id`.

## 3. Nội dung bán hàng: ưu tiên số 1
Bạn **không nhìn thấy** trang khi sửa file .pke. Vì vậy hãy tập trung vào chữ, ưu đãi và luồng mua hàng, là phần sửa an toàn và tăng chuyển đổi nhiều nhất.
- Hồ sơ sản phẩm và khách hàng nằm ở `.agents/product-marketing.md`. Đọc file này trước mọi việc. Nếu chưa có file, dùng skill `product-marketing` để soạn từ nội dung file .pke, rồi hỏi người dùng bổ sung.
- Đánh giá trang, tìm điểm làm khách bỏ đi: dùng skill `cro`.
- Viết lại tiêu đề, lợi ích, CTA: dùng skill `copywriting`. Rà và sửa câu chữ: dùng skill `copy-editing`.
- Thiết kế ưu đãi, combo, quà tặng, khan hiếm: dùng skill `offers`. Popup: dùng skill `popups`. Tâm lý mua hàng: dùng skill `marketing-psychology`.
- Viết tiếng Việt tự nhiên, giọng gần gũi với khách nữ Việt Nam. Không dịch máy từ tiếng Anh. Giữ độ dài chữ gần bằng bản cũ (±20%) để không tràn khung.
- Khi người dùng yêu cầu, đưa ra 2–3 phương án chữ để chọn trước khi sửa file.

## 4. Giao diện: thận trọng, dùng skill ui-ux-pro-max
Trang gốc được thiết kế cùng với ảnh (ảnh sản phẩm, banner có sẵn chữ và màu). Đổi cả bảng màu hay đổi font toàn trang **sẽ làm trang lệch tông với ảnh và vỡ khung chữ**. Do đó:
- **Không** đổi bảng màu hay font toàn trang, trừ khi người dùng yêu cầu rõ ràng bằng chữ "đổi toàn bộ".
- Mặc định chỉ sửa có mục tiêu: làm nút mua nổi bật hơn, tăng tương phản chữ khó đọc, tăng cỡ chữ quá nhỏ, thống nhất các màu lệch nhau. Màu mới phải lấy từ màu đang có trên trang hoặc màu thương hiệu.
- Nếu người dùng gửi ảnh chụp màn hình trang, hãy xem ảnh trước khi đề xuất.
- Muốn thiết kế lại hẳn, **không sửa file .pke**. Làm một bản mẫu `mockup/<ten>.html` (khổ mobile 420px) để nhân viên xem, rồi dựng lại trong Webcake.

Các bước khi dùng ui-ux-pro-max:
1. Chạy design system trước, ví dụ:
   `python3 .agents/skills/ui-ux-pro-max/scripts/search.py "beauty herbal skincare natural wellness" --design-system -p "Thaphaco"`
2. Tra thêm khi cần: `--domain landing` (cấu trúc trang bán hàng, CTA), `--domain color`, `--domain typography`, `--domain google-fonts`, `--domain ux` (ví dụ `"form mobile cta"`).
3. Áp dụng kết quả vào file .pke theo mục 2, chỉ ở phần được phép sửa.
4. Lưu ý riêng cho tiếng Việt và Webcake:
   - Font **bắt buộc hỗ trợ tiếng Việt có dấu** (Google Fonts có subset Vietnamese, ví dụ Be Vietnam Pro, Montserrat, Roboto, Playfair Display, Lora, Nunito). Nếu skill gợi ý font không có tiếng Việt, hãy đổi sang font tương đương có tiếng Việt.
   - Ưu tiên mobile (đa số khách xem bằng điện thoại). Chữ nội dung tối thiểu 14px, nút bấm tối thiểu 44px chiều cao, độ tương phản chữ/nền tối thiểu 4.5:1.
   - Tối đa 2 font và một bảng màu thống nhất cho cả trang và popup.
5. Ghi rõ bảng màu và font đã chọn, kèm lý do ngắn, trong phần tóm tắt.

## 5. Quy định nội dung quảng cáo (bắt buộc)
Sản phẩm là thực phẩm bảo vệ sức khoẻ / mỹ phẩm, **không phải thuốc**:
- Không dùng: "chữa bệnh", "điều trị", "trị dứt điểm", "khỏi hẳn", "thay thế thuốc", "cam kết 100%", "tốt nhất".
- Dùng: "hỗ trợ", "giúp", "góp phần".
- Thực phẩm bảo vệ sức khoẻ phải giữ câu: "Sản phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh."
- Nếu nội dung gốc vi phạm, đề xuất câu thay thế và báo lại, không tự xoá.
