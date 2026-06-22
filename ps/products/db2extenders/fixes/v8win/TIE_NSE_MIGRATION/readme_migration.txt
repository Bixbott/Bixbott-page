IBM (R) DB2 (R) Net Search Extender
Ghi chú di cư

Phiên bản 8.1.0 (Cập nhật)

(C) Bản quyền thuộc về Tập đoàn International Business Machines 2001, 2002. Tất cả
Bản quyền đã được bảo lưu.
Quyền sử dụng, sao chép hoặc tiết lộ của người dùng thuộc Chính phủ Hoa Kỳ bị hạn chế.
Bị hạn chế bởi Hợp đồng Lịch trình GSA ADP với Tập đoàn IBM.


Nâng cấp Text Information Extender V7.2 lên Net Search Extender V8.1
==================================================================

- Các điều kiện tiên quyết của DB2 Net Search Extender
- Di chuyển DB2
- Di chuyển DB2 Extender


Các điều kiện tiên quyết của DB2 Net Search Extender
-------------------------------------
Hãy cài đặt DB2 Net Search Extender V8.1 trước khi di chuyển cơ sở dữ liệu DB2.
ví dụ.

Sau khi cài đặt DB2 Net Search Extender V8.1, bạn cần cập nhật
các tệp sau:

Trên Windows:

     - cteerror.dll
     - cteutil.dll
     - cteadmci.dll
     - db2extmdb.exe

Trên Windows, hãy sao chép các tệp đó vào thư mục '<db2install>/bin' của bạn.
với tư cách là người dùng quản trị.

Trên AIX và Solaris:

     - libcteerror.a / libcteerror.so
     - libcteutil.a / libcteutil.so
     - libcteadmci.a / libcteadmci.so
     - db2extmdb / db2extmdb

Trên hệ điều hành UNIX, hãy sử dụng tập lệnh install.sh với quyền người dùng root.

Lưu ý rằng với gói sửa lỗi Fix pack 2, các tệp mới nhất đã có sẵn và hoạt động tốt.
Không cần cập nhật.


Di chuyển DB2
-------------
Để biết thông tin về các bước di chuyển sang DB2, hãy sử dụng liên kết sau:

http://www-3.ibm.com/cgi-bin/db2www/data/db2/udb/winos2unix/support/techlib_v8.d2w/report

Sau đó tìm kiếm từ khóa 'migration' và thực hiện quy trình được mô tả.
   
Sau đó, bạn có thể di chuyển phiên bản DB2 và cơ sở dữ liệu DB2 của mình từ Phiên bản trước.
Từ phiên bản 7.2 đến phiên bản 8.1.

- Trên hệ điều hành Windows, phiên bản DB2 được tự động cập nhật trong quá trình này.
quá trình cài đặt.

- Trên hệ điều hành UNIX, nếu bạn đã di chuyển phiên bản DB2 của mình trước khi khởi động DB2 Net.
Cài đặt Search Extender V8.1, bắt đầu cập nhật phiên bản bằng cách sử dụng
'db2iupdt'.
    
Lưu ý rằng sau khi di chuyển phiên bản DB2, thư viện 'sqllib' trước đó sẽ được giữ nguyên.
Thư mục được đổi tên thành 'sqllib_v71'. Nếu bạn có chỉ mục văn bản
được lưu trữ trong thư mục chỉ mục mặc định, hãy di chuyển
Chuyển thư mục 'sqllib_v71/db2ext/indexes' sang thư mục sqllib mới.
'sqllib/db2ext/indexes'.


Di chuyển DB2 Extender
----------------------   
Sau đó, chủ sở hữu phiên bản có thể di chuyển tất cả các cơ sở dữ liệu đã được kích hoạt.
Ví dụ này sử dụng công cụ db2extmdb mới. Cú pháp như sau:

db2extmdb <tên cơ sở dữ liệu>

Lưu ý rằng chương trình chỉ cung cấp thông báo bằng tiếng Anh. Nếu một
Lỗi xảy ra, hãy sửa lỗi và gọi lại lệnh 'db2extmdb'.

Chương trình thu thập tất cả thông tin quản trị db2ext.
Thông tin này có liên quan đến quá trình di chuyển dữ liệu trong một bảng mới có tên là DB2EXT.TMIGRATION.
Trong đó, mỗi chỉ mục văn bản được biểu thị bằng một hàng duy nhất trong bảng.

Bảng thông tin di chuyển sẽ được lưu giữ cho đến khi cơ sở dữ liệu được hoàn tất.
Quá trình chuyển đổi đã thành công và người dùng không nên bỏ qua bước này.

Trong quá trình di chuyển chỉ mục văn bản, các quy trình xử lý khác nhau sẽ diễn ra. Điều này phụ thuộc vào...
về trạng thái của bảng nhật ký và tính khả dụng của các tệp chỉ mục.

- Nếu bảng nhật ký trống và các tệp chỉ mục có thể truy cập được, thì
Chỉ mục đã được di chuyển. Đây là phương án nhanh nhất.
- Nếu bảng nhật ký không trống hoặc không tìm thấy các tệp chỉ mục,
Không thể đảm bảo trạng thái nhất quán với cơ sở dữ liệu và chỉ mục.
Cần phải tạo lại.

Xin lưu ý rằng quá trình này có thể mất một khoảng thời gian đáng kể. Trong khi đó,
Quá trình chuyển đổi đang diễn ra, sẽ không có thay đổi nào đối với người dùng.
bảng.


Sự giới thiệu:
Trước khi gọi chương trình db2extmdb, người dùng cần sao lưu toàn bộ dữ liệu.
lập chỉ mục các thư mục và cơ sở dữ liệu, đồng thời xác minh rằng tất cả tài liệu đều chính xác.
Các tệp mô hình được sử dụng để tạo chỉ mục văn bản V7.2 vẫn còn tồn tại và
Có thể truy cập để đọc.
