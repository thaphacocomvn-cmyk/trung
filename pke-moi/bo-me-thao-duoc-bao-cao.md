# Bồ Mễ: màu sắc, font và nội dung mới

## Phạm vi
Bản gốc không thay đổi. Bản xuất: `bo-me-thao-duoc.moi.pke`. Áp dụng màu/font cho mobile và desktop, viết lại tiêu đề và CTA. Giữ ưu đãi 35% theo yêu cầu trước đó. Không sửa giá, kích thước, vị trí, ảnh, ID, sự kiện, form, mã tracking hoặc script. Đánh giá mobile dưới đây chỉ là đề xuất, không áp dụng sửa bố cục/cỡ chữ.

## Thiết kế đề xuất và đã áp dụng
- Xanh lá trầm #234B37: tiêu đề, mảng nhấn, footer; gợi thảo dược.
- Kem #F8F6EF, xanh nhạt #E8EEE0, trắng #FFFFFF: nền dịu và phân cấp nội dung.
- Vàng đồng đậm #8B5E20: nút mua và tư vấn; chữ trắng.
- Chữ nội dung #2D3A2F, chữ phụ #51604E; viền #C9D2C0.
- Lora cho tiêu đề từng dùng Playfair Display; Be Vietnam Pro cho nội dung/nút và font chung. Cả hai có subset Vietnamese trong dữ liệu Google Fonts của skill.

Đã chạy design-system và tra typography/google-fonts/UX bằng ui-ux-pro-max. Gợi ý tự động Liquid Glass không phù hợp Webcake/thảo dược nên không áp dụng. Bảng màu này là điều chỉnh thiết kế theo yêu cầu, không phải nguyên xi kết quả tìm kiếm. Không áp dụng hiệu ứng hay đổi bố cục. Ảnh nền có sẵn giữ nguyên nên các sắc hồng nằm trong ảnh vẫn còn.

## Đánh giá mobile của file gốc — chỉ vấn đề và đề xuất
Đánh giá từ dữ liệu .pke, chưa xem trang được render trong Webcake hoặc thiết bị thật; không kết luận về chồng lấn/hiển thị thực tế.

| Vấn đề từ dữ liệu gốc | Đề xuất chưa áp dụng |
|---|---|
| Section 3: đoạn giải thích dài cỡ 14px; Section 5 cũng có nội dung 14px. | Cân nhắc 16px cho nhóm khách 30–45; kiểm tra khung sau khi tăng. |
| Section 6: chú thích video 12px; Section 7 và Popup 2: điều kiện thanh toán 12px. Section 9: tuổi khách hàng 12px; footer 12px. | Tăng tối thiểu 14px; điều kiện ưu đãi nên đọc rõ trước khi đặt mua. |
| CTA đầu trang 213×52px, Section 5 194×52px, đặt hàng 304×57px; nút footer chỉ 165×43px, nút xem cách dùng 231×40px, nút đóng 130×40px. | Giữ các nút lớn; tăng các nút dưới 44px lên tối thiểu 44px theo quy ước repo, kiểm tra khoảng cách. |
| CTA đầu trang dùng chữ trắng trên gradient hồng–đỏ; tương phản thay đổi dọc nền. | Dùng nền đặc, đo tương phản ít nhất 4.5:1. |
| Nút đặt hàng gốc chữ hồng #E3496C trên nền #FFECEC khá nhẹ so với vai trò mua hàng. | Dùng một màu CTA đủ đậm, nhất quán toàn trang/popup. |
| Nhiều sắc hồng, đỏ, cam và gradient cùng xuất hiện; nền ảnh vẫn có màu riêng. | Dùng ít màu vai trò; chuẩn bị ảnh cùng tông trong một công việc riêng nếu cần. |
| Nhiều phần tử chữ có height 0 hoặc 1 trong dữ liệu. | Kiểm tra render Webcake; đây có thể là quy ước tự giãn, chưa đủ bằng chứng kết luận lỗi. |
| Đổi font và tiêu đề có thể thay đổi xuống dòng trong bố cục tuyệt đối. | Import rồi xem ở 360/390/420px; chỉnh khung trong Webcake nếu cần. |

## Nội dung quảng cáo cần xác minh — không tự sửa
- Section 3: con số “90%” chưa có nguồn trong phần chữ; cần chứng cứ hoặc đề xuất thay bằng “Một số yếu tố thường gặp” và viết lại cụm liên quan cho liền nghĩa.
- Section 1: “CHỈ TRONG HÔM NAY” cần thời hạn thực; đề xuất “Khám phá ưu đãi hiện có” nếu không có chiến dịch theo ngày.
- Section 5: công dụng dưỡng ẩm, tổng hợp collagen, làm chậm lão hoá cần đối chiếu phân loại và hồ sơ sản phẩm. Dùng “hỗ trợ” không tự động bảo đảm quảng cáo hợp lệ. Khi chưa có chứng cứ, có thể chuyển sang thông tin cách dùng đã xác minh.
- Chưa thấy câu “Sản phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh.” trong các text node. Nếu sản phẩm được phân loại là thực phẩm bảo vệ sức khoẻ, cần bổ sung trước khi đăng. Chưa tự thêm vì chưa có phân loại/hồ sơ và vị trí được duyệt. Chữ nằm trong ảnh chưa được kiểm tra.
- Giá/ưu đãi, quà tặng, miễn phí vận chuyển và nhận xét khách hàng phải đúng thực tế; không tạo mới chứng thực hay cam kết hiệu quả.

Các tiêu đề/CTA mới tránh hứa hẹn điều trị hoặc bảo đảm hiệu quả; chưa thể xác nhận toàn trang tuân thủ khi còn các nội dung nêu trên.

## Từng thay đổi câu chữ
| Vị trí | Trước | Sau |
|---|---|---|
| Section 1 | Dưỡng da căng mướt, mềm mịn từ bên trong nhờ lớp gel tự nhiên của Bồ Mễ  | Bồ Mễ – chút dịu lành cho ngày thêm thư thái  |
| Section 1 | <span><span>Nhận Ưu Đãi Ngay</span></span> | <span><span>Xem ưu đãi Bồ Mễ</span></span> |
| Section 1 | Chăm da không chỉ là chuyện của mỹ phẩm  | Chăm mình từ những điều giản dị  |
| Section 2 | Đắp Bao Nhiêu Thứ Lên Mặt Mà Da Vẫn Cứ... | Bạn có đang gặp những thay đổi này ở da? |
| Section 3 | Bạn Đã Thực Sự Hiểu Nguyên Nhân Do Đâu Chưa? | Điều gì khiến làn da thiếu sức sống? |
| Section 4 | GIẢI ĐÁP THẮC MẮC VỀ CÁCH NẤU CHÈ DƯỠNG NHAN | CÙNG KHÁM PHÁ CÁCH NẤU CHÈ BỒ MỄ |
| Section 4 | <span><span>Nhận Tư Vấn</span></span> | <span><span>Tư vấn cách dùng</span></span> |
| Section 4 | Nuôi dưỡng làn da căng mướt cùng Bồ Mễ | Bồ Mễ cho phút chăm mình mỗi ngày |
| Section 5 | Bạn Sẽ Nhận Được Gì Từ Bồ Mễ | Tìm hiểu thêm về Bồ Mễ |
| Section 5 | <span><span>Nhận Ưu Đãi Ngay</span></span> | <span><span>Xem ưu đãi Bồ Mễ</span></span> |
| Section 6 | Gợi Ý Các Cách Dùng Bồ Mễ | Thưởng thức Bồ Mễ theo cách của bạn |
| Section 6 | Cách lười cho dân văn phòng  | Pha tiện lợi cho ngày bận rộn  |
| Section 6 | Đừng bỏ qua bước này | Bắt đầu từ bước ngâm nở |
| Section 6 | Bồ Mễ phải ngâm nở trước nhé! | Ngâm nở Bồ Mễ trước khi dùng |
| Section 6 | <span><span>XEM CÁCH DÙNG KHÁC</span></span> | <span><span>KHÁM PHÁ CÁCH DÙNG</span></span> |
| Section 7 | Đặt Mua Bồ Mễ Chính Hãng Ngay Hôm Nay | Chọn Bồ Mễ cho góc bếp của bạn |
| Section 7 | Ưu Đãi 30% | Ưu Đãi 35% |
| Section 7 | <span><span>ĐẶT HÀNG NGAY</span></span> | <span><span>Đặt mua Bồ Mễ</span></span> |
| Section 9 | Cảm Nhận Của Khách Hàng | Khách hàng chia sẻ về Bồ Mễ |
| Section 10 | <span><span>Nhận Ưu Đãi Ngay</span></span> | <span><span>Xem ưu đãi Bồ Mễ</span></span> |
| Popup 2 | Đặt Mua Bồ Mễ Chính Hãng Ngay Hôm Nay | Chọn Bồ Mễ cho góc bếp của bạn |
| Popup 2 | Ưu Đãi 30% | Ưu Đãi 35% |
| Popup 2 | <span><span>ĐẶT HÀNG NGAY</span></span> | <span><span>Đặt mua Bồ Mễ</span></span> |

## Chi tiết mọi thay đổi
Tệp `bo-me-thao-duoc-thay-doi.csv` liệt kê từng trường trước → sau, kèm Section/Popup và đường dẫn mobile/desktop.

## Kiểm tra bản xuất
Đóng gói/đọc lại khớp dữ liệu; đối chiếu đệ quy đúng 1.158 trường thay đổi cho phép, gồm 23 node chữ. File gốc khớp byte với file tải lên. Hình học, ID, sự kiện, link ảnh, tracking/script không đổi. Cặp chữ trắng/nút vàng đồng mới đạt 5,65:1; xanh đậm/nền kem đạt 9,10:1. Nút đặt hàng gốc hồng/nền hồng nhạt khoảng 3,40:1. Đây là số đo các cặp màu xác định, không bảo đảm toàn bộ chữ trên ảnh/gradient hoặc hình chồng lớp. Chưa xác minh tải font, xuống dòng hay import/render bằng Webcake.
