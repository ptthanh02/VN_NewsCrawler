# VN_NewsCrawler (2023)

[VietNamNet](https://vietnamnet.vn/) news crawler that extracts article titles and content for various categories.


## Installation

Requires Python 3.11 or higher.

- Clone this repository: 
```bash
$ git clone https://github.com/ptthanh02/VN_NewsCrawler.git
```

- Navigate to the project directory:
```bash
$ cd VN_NewsCrawler
```
- Create and active virtual environment:
```bash
$ python -m venv venv
$ venv\Scripts\activate 
```
- Install the required packages:
```bash
$ pip install -r requirements.txt
```

## Configuration
Modifying your crawler configuration file `config.py` to customize your crawling progress.

```python
# Supported categories: 'thoi-su', 'kinh-doanh', 'van-hoa', 'giao-duc', 'the-gioi'
categories = ['thoi-su', 'kinh-doanh', 'van-hoa', 'giao-duc', 'the-gioi'] 
number_of_articles = 10  # Number of articles to crawl for each category
```
By default, the configuration will crawl 10 articles for each category listed in the `categories` variable, resulting in a total of 50 crawled articles. You can adjust `number_of_articles` to crawl more articles or modify the `categories` variable to crawl specific categories.


## Usage
- Run the crawler:
```bash
$ python crawler.py
```

## Example Results
The crawler will create a `result` folder and store the crawled articles in the `baibao.txt` file. The following is an example of the crawled articles:
```txt. 
------------------------ Thể loại: Thời Sự --------------------------
Bài báo thứ 1: 
Tiêu đề: Bắt tạm giam cựu Phó Chủ tịch phường ở Khánh Hòa vì lạm quyền
Nội dung: 
Ngày 28/9, Công an thị xã Ninh Hòa (Khánh Hòa) khởi tố, bắt tạm giam ông Trần Thanh Tùng, cựu Phó Chủ tịch UBND phường Ninh Hải, để điều tra hành vi Lạm quyền khi thi hành công vụ.
Theo kết luận thanh tra của UBND thị xã Ninh Hòa, ông Tùng khi còn giữ chức Phó Chủ tịch UBND phường Ninh Hải, không được phân công nhiệm vụ chứng thực. Tuy nhiên, ông Tùng đã tự ý ký chứng thực hợp đồng chuyển nhượng đất cho con trai và một người phụ nữ ở địa phương. Việc ký này bị xác định có dấu hiệu lạm dụng quyền trong khi thi hành công vụ.

UBND phường Ninh Hải, thị xã Ninh Hòa Ảnh: N.X. 

Công chức tư pháp phường Ninh Hải khẳng định không tiếp nhận hồ sơ đề nghị chứng thực hợp đồng chuyển nhượng nói trên, hồ sơ chứng thực không được lưu giữ tại UBND phường Ninh Hải. Bên cạnh đó, số chứng thực, ngày chứng thực không có trong sổ chứng thực hợp đồng của phường.
Sau kết luận thanh tra, ông Tùng bị kỷ luật cảnh cáo, miễn nhiệm chức Phó chủ tịch UBND phường Ninh Hải.
Ông Trịnh Thanh Bình (cựu công chức địa chính phường Ninh Hải) cũng bị khởi tố tội Lợi dụng chức vụ quyền hạn trong khi thi hành công vụ, do sai phạm về đất đai.
Ngoài ra, ông Trần Hải, Chủ tịch UBND phường Ninh Hải bị kỷ luật, miễn nhiệm chức vụ. Ông Hải để xảy ra các vi phạm trong việc xét đề nghị cấp giấy chứng nhận quyền sử dụng đất, vi phạm trong tiếp nhận, giải quyết các đơn phát sinh liên quan đến diện tích đất ở trên núi của địa phương.

Kỷ luật cảnh cáo với một chủ tịch thị xã ở Khánh HòaÔng Nguyễn Vĩnh Thạnh, Chủ tịch UBND thị xã Ninh Hòa (Khánh Hòa) bị kỷ luật cảnh cáo do thiếu trách nhiệm kiểm tra, giám sát, đôn đốc các cơ quan chuyên môn thực hiện việc thu hồi, quản lý nhà, đất...

 
--------------------------------------------------
Bài báo thứ 2: 
Tiêu đề: Tạm giữ đối tượng lái xe vi phạm nồng độ cồn, chống người thi hành công vụ
Nội dung: 
Ngày 28/9, Công an tỉnh Bắc Giang cho biết, đơn vị này đang tạm giữ đối tượng vi phạm nồng độ cồn, chống người thi hành công vụ.
Trước đó, vào tối ngày 25/9, tổ công tác của Bộ Công an phối hợp với lực lượng cảnh sát giao thông (CSGT) tỉnh Bắc Giang tuần tra, kiểm soát, xử lý vi phạm nồng độ cồn trên đường Xương Giang, TP Bắc Giang (khu vực cạnh đền Xương Giang).
Tại đây, tổ công tác ra hiệu lệnh dừng ô tô biển kiểm soát 30T-31xx do ông Đinh Công Bình (SN 1974, phường Ngô Quyền, TP Bắc Giang) điều khiển. Tuy nhiên lái xe không chấp hành mà tiếp tục di chuyển về phía trước.
Ngay sau đó, cán bộ Trung đoàn Cảnh sát cơ động Thủ đô Tạ Văn Nam đến hỗ trợ, sử dụng đèn pin, gậy điều khiển giao thông ra hiệu lệnh dừng xe nhưng ông Bình vẫn lái xe tiến sát vị trí anh Nam đang đứng.
Thấy nguy hiểm nên anh Nam nhảy lên nắp ca pô, bám tay trái vào cần gạt nước của xe ô tô, dùng đèn pin ra hiệu lệnh dừng lại nhưng ông Bình tiếp tục đi.
Được khoảng 10m, bị các thành viên trong tổ công tác áp sát, tài xế mới dừng lại. Qua kiểm tra, xác định ông Bình có nồng độ cồn là 0,203mg/lít khí thở. Cơ quan Cảnh sát điều tra Công an TP Bắc Giang đã ra Quyết định tạm giữ ông Bình về hành vi “Chống người thi hành công vụ”.

Lực lượng chức năng đang tạm giữ đối tượng Đinh Công Bình vi phạm nồng độ cồn, chống người thi hành công vụ. Ảnh: CACC.

Được biết, ông Bình làm nghề kinh doanh mua bán ô tô cũ, chưa có tiền án tiền sự. Tối 25/9, ông đi liên hoan cùng bạn bè ở huyện Lạng Giang và có uống rượu.
Đến khoảng 21 giờ, ông điều khiển xe ô tô về nhà, đến đoạn đường trước cổng đền Xương Giang thì phát hiện có chốt kiểm tra của lực lượng CSGT.
Lo sợ bị thổi nồng độ cồn, ông Bình điều khiển xe sang làn đường ngược chiều với ý định bỏ chạy. Các thành viên tổ công tác nhiều lần yêu cầu dừng xe nhưng ông Bình không chấp hành, cố tình lái xe gây nguy hiểm cho người thực thi công vụ. 
--------------------------------------------------
Bài báo thứ 3: 
Tiêu đề: Hơn 1.500 chung cư mini, nhà trọ tại TP.HCM vi phạm cháy nổ
Nội dung: 
Tại buổi họp báo về tình hình kinh tế - xã hội của TP.HCM chiều 28/9, Thượng tá Lê Mạnh Hà, Phó phòng Tham mưu Công an TP cho biết, thời gian qua, Giám đốc Công an TPHCM đã chỉ đạo Phòng Cảnh sát Phòng cháy chữa cháy và Cứu nạn cứu hộ, công an các quận, huyện, TP Thủ Đức nhanh chóng tham mưu ban hành kế hoạch, đồng loạt ra quân tổng rà soát, kiểm tra địa bàn.

Một  khu chung cư mini trên đường Lê Đình Cẩn , TP.HCM bít kín bằng lưới rào, song sắt

Bước đầu, các lực lượng đã kiểm tra 10.000 cơ sở, phát hiện, xử lý 1.541 cơ sở vi phạm với tổng số tiền phạt hơn 2,4 tỷ đồng, đình chỉ và tạm đình chỉ hoạt động 6 cơ sở.
Ngoài ra, có 4 cơ sở bị xử lý trong lĩnh vực xây dựng, 41 cơ sở bị xử lý về đăng ký kinh doanh, 161 cơ sở bị xử lý trong đăng ký thường trú, tạm trú.
Không sạc pin xe máy, xe đạp điện qua đêm
Cũng tại buổi họp báo, Thượng tá Hà thông tin thêm về nguy cơ cháy nổ của xe đạp điện, xe máy điện tại các chung cư.
Theo ông Hà, xe đạp điện, xe máy điện đang là loại hình phương tiện lưu thông phổ biến. Thời gian qua, nhiều vụ cháy nổ liên quan đến xe điện đã xảy ra.

Thượng tá Lê Mạnh Hà trả lời tại buổi họp báo

"Khi các phương tiện sử dụng năng lượng điện tăng thì theo quy luật, nguy cơ cháy xe đạp điện, xe máy điện cũng tăng”, ông Hà cho biết.
Cũng theo ông Hà, có ba nguyên nhân gây cháy, nổ, gồm: Tâm lý chủ quan và thói quen sạc xe qua đêm không có người trông coi; sạc xe ngay sau khi sử dụng lúc pin còn nóng; mua sắm phương tiện giá rẻ không đảm bảo chất lượng,
Ông Lê Mạnh Hà chia sẻ thêm, xe điện sử dụng nhiều loại ắc quy, pin nhưng phổ biến nhất là loại pin lithium ion. Loại pin này khi cháy, nổ sẽ khó dập tắt bằng bình cứu hỏa thông thường do các phản ứng hóa học.
Công an TPHCM cũng đưa ra khuyến cáo, trong quá trình sạc cho xe máy, xe đạp điện, các tủ điện, thiết bị điều khiển và cấp nguồn cho trạm sạc cần đặt ở nơi khô ráo, ngăn cách với khu vực có nguồn lửa, nguồn nhiệt.
Vị trí sạc xe điện cũng cần ngăn cách với khu vực để xe động cơ khác. Khi sạc điện, người dân không để xe bên trên hoặc gần vật dụng, hàng hóa dễ cháy nổ, gần nguồn lửa, nguồn nhiệt, thiết bị sinh lửa, sinh nhiệt.
Đồng thời, người dân cần thường xuyên kiểm tra xe khi sạc để kịp thời phát hiện, xử lý ngày sự cố, không sạc xe qua đêm. 
--------------------------------------------------
...

```
Check the `result` folder for the full example.
