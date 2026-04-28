import json
import os

def update_questions():
    file_path = r'c:\Development\Antigravity\Salesforce-PD1\src\data\questions.json'
    
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    # Translation dictionary for IDs 51-100
    translations = {
        51: "Một lập trình viên phải tạo một lớp ShippingCalculator không thể được khởi tạo trực tiếp và phải bao gồm một triển khai mặc định hoạt động của phương thức calculate mà các lớp con có thể ghi đè. Cách triển khai lớp ShippingCalculator nào sau đây là đúng?",
        52: "Ursa Major Solar (UMS) đã triển khai mô hình chia sẻ riêng tư cho đối tượng Account. Một công cụ tìm kiếm Account tùy chỉnh đã được phát triển bằng Apex để giúp các đại diện bán hàng tìm kiếm các tài khoản khớp với nhiều tiêu chí họ chỉ định. Kể từ khi phát hành, người dùng báo cáo rằng họ có thể thấy các Account mà họ không sở hữu. Lập trình viên nên sử dụng gì để thực thi quyền chia sẻ cho người dùng hiện đang đăng nhập khi sử dụng công cụ tìm kiếm tùy chỉnh?",
        53: "Ba đặc điểm nào của việc triển khai bằng Change Sets là đúng? (Chọn 3)",
        54: "Phương thức Apex sau đây là một phần của lớp ContactService được gọi từ một trigger. Lập trình viên nên sửa đổi mã như thế nào để đảm bảo đáp ứng các tiêu chuẩn thực hành tốt nhất (best practices)?",
        55: "Một lập trình viên đã tạo một trang Visualforce và bộ điều khiển tùy chỉnh (custom controller) để hiển thị trường loại tài khoản (Account Type) như bên dưới. Giá trị của trường loại tài khoản không được hiển thị chính xác trên trang. Giả sử bộ điều khiển tùy chỉnh được tham chiếu đúng trên trang Visualforce, lập trình viên nên làm gì để khắc phục vấn đề này?",
        56: "Một Visual Flow sử dụng một hành động Apex (Apex Action) để cung cấp thông tin bổ sung về nhiều Contact, được lưu trữ trong một lớp tùy chỉnh, contactInfo. Định nghĩa đúng của phương thức Apex lấy thông tin bổ sung là gì?",
        57: "Kịch bản nào sau đây là hợp lệ để thực thi bởi các unit test?",
        58: "Một lập trình viên có một bộ điều khiển Apex (Apex controller) cho một trang Visualforce nhận một ID dưới dạng tham số URL. Lập trình viên nên làm gì để ngăn chặn lỗ hổng bảo mật tấn công chéo trang (XSS - cross-site scripting)?",
        59: "Một lập trình viên viết một trigger trên đối tượng Account cho sự kiện before update để tăng giá trị của một trường đếm. Một quy tắc quy trình làm việc (workflow rule) cũng tăng trường đếm mỗi khi Account được tạo hoặc cập nhật. Cập nhật trường trong quy tắc quy trình làm việc được cấu hình để không đánh giá lại các quy tắc quy trình làm việc. Giá trị của trường đếm là bao nhiêu nếu một Account được chèn với giá trị ban đầu là 0, giả sử không có logic tự động nào khác được triển khai trên Account?",
        60: "Một lập trình viên phải tạo một lớp Apex, ContactController, mà một Lightning component có thể sử dụng để tìm kiếm các bản ghi Contact. Người dùng của Lightning component chỉ có thể tìm kiếm các bản ghi Contact mà họ có quyền truy cập. Hai cách nào sau đây sẽ giới hạn các bản ghi một cách chính xác? (Chọn 2)",
        61: "Hai phát biểu nào sau đây là chính xác liên quan đến các lớp (classes) và giao diện (interfaces) trong Apex? (Chọn 2)",
        62: "Lớp OrderHelper là một lớp tiện ích chứa logic nghiệp vụ để xử lý các đơn hàng. Hãy xem xét đoạn mã sau: Một lập trình viên cần tạo một hằng số tên là DELIVERY_MULTIPLIER với giá trị là 4.15. Giá trị của hằng số này không được thay đổi bất kỳ lúc nào trong mã. Lập trình viên nên khai báo hằng số DELIVERY_MULTIPLIER như thế nào để đáp ứng các mục tiêu nghiệp vụ?",
        63: "Hai phát biểu nào sau đây đại diện chính xác cho việc triển khai khung làm việc MVC trong Salesforce? (Chọn 2)",
        64: "Cloud Kicks lưu trữ các Đơn hàng (Orders) và Các mục trong đơn hàng (Line Items) trong Salesforce. Vì lý do bảo mật, các đại diện tài chính được phép xem thông tin trên Đơn hàng như số tiền đơn hàng, nhưng họ không được phép xem Các mục trong đơn hàng đó. Loại quan hệ nào nên được sử dụng?",
        65: "Cho đoạn mã bên dưới. Làm thế nào để cải thiện đoạn mã này để tuân thủ các thực hành tốt nhất về hiệu suất?",
        66: "Một doanh nghiệp đã triển khai kế hoạch game hóa để khuyến khích khách hàng xem các video giáo dục. Khách hàng có thể xem video trong nhiều ngày và tiến trình của họ được ghi lại. Điểm thưởng được trao cho khách hàng cho tất cả các video đã hoàn thành. Khi video được đánh dấu là hoàn thành trong Salesforce, một dịch vụ web bên ngoài phải được gọi để điểm thưởng có thể được trao cho người dùng. Một lập trình viên đã triển khai các yêu cầu này trong trigger after update bằng cách gọi đến một dịch vụ web bên ngoài. Tuy nhiên, một lỗi System.CalloutException đang xảy ra. Lập trình viên nên làm gì để khắc phục lỗi này?",
        67: "Ba bước nào cho phép một file SVG tùy chỉnh được bao gồm trong một Lightning Web Component? (Chọn 3)",
        68: "Một lập trình viên đang di chuyển một trang Visualforce sang một Lightning Web Component. Trang Visualforce hiển thị thông tin về một bản ghi duy nhất. Lập trình viên quyết định sử dụng Lightning Data Service để truy cập dữ liệu bản ghi. Cân nhắc bảo mật nào mà lập trình viên nên lưu ý?",
        69: "Annotation (chú thích) nào hiển thị một lớp Apex dưới dạng một dịch vụ web RESTful?",
        70: "Hai đặc điểm nào là đúng đối với các sự kiện của Aura component (Aura component events)? (Chọn 2)",
        71: "Ban quản lý yêu cầu các cơ hội (opportunities) phải được tự động tạo cho các tài khoản (accounts) có doanh thu hàng năm lớn hơn $ 1,000,000. Một lập trình viên đã tạo trigger sau trên đối tượng Account để đáp ứng yêu cầu. Người dùng có thể cập nhật các bản ghi tài khoản qua giao diện người dùng và có thể thấy một cơ hội được tạo cho các tài khoản có doanh thu cao. Tuy nhiên, khi quản trị viên cố gắng tải lên một danh sách 179 tài khoản bằng Data Loader, nó thất bại với các lỗi System.Exception. Hai hành động nào mà lập trình viên nên thực hiện để khắc phục đoạn mã trên? (Chọn 2)",
        72: "Universal Containers có một trang Visualforce hiển thị bảng của mọi Container_c đang được thuê bởi một Account cụ thể. Gần đây, trang này đang thất bại với lỗi giới hạn view state vì một số khách hàng thuê hơn 10,000 container. Lập trình viên nên thay đổi điều gì về trang Visualforce để giúp khắc phục các lỗi tải trang?",
        73: "Nhóm quản lý bán hàng tại Universal Containers yêu cầu trường Lead Source của bản ghi Lead phải được điền khi Lead được chuyển đổi. Nên sử dụng gì để đảm bảo rằng người dùng điền trường Lead Source trước khi chuyển đổi Lead?",
        74: "Hai sự kiện nào cần xảy ra khi triển khai (deploy) lên một tổ chức production? (Chọn 2)",
        75: "Một lập trình viên nhận được lỗi khi cố gắng gọi một phương thức global phía máy chủ bằng cách sử dụng trình trang trí (decorator) @RemoteAction. Làm thế nào lập trình viên có thể giải quyết lỗi này?",
        76: "Một công ty phần mềm sử dụng các đối tượng và mối quan hệ sau: Case: để xử lý các vấn đề hỗ trợ khách hàng; Defect_c: một đối tượng tùy chỉnh để đại diện cho các lỗi đã biết với phần mềm của công ty; Case_Defect_c: một đối tượng Junction giữa Case và Defect_c để thể hiện rằng một lỗi là nguyên nhân của một vấn đề của khách hàng. Case và Defect_c có các giá trị mặc định toàn tổ chức (OWD) là Riêng tư (Private). Cần làm gì để chia sẻ một bản ghi Case_Defect_c cụ thể với người dùng?",
        77: "Một lập trình viên được yêu cầu tạo một trang Visualforce liệt kê các liên hệ do người dùng hiện tại sở hữu. Component này sẽ được nhúng trong một trang Lightning. Mà không cần viết mã không cần thiết, bộ điều khiển (controller) nào nên được sử dụng cho mục đích này?",
        78: "Một lập trình viên cần tạo một bộ dữ liệu cơ sở (Accounts, Contacts, Products, Assets) cho toàn bộ bộ thử nghiệm (test suite) cho phép họ kiểm tra các yêu cầu độc lập của các loại Salesforce Case khác nhau. Cách tiếp cận nào có thể tạo dữ liệu cần thiết một cách hiệu quả cho mỗi unit test?",
        79: "Tham khảo đoạn mã dưới đây: Const p1 = 3.1415926; Kiểu dữ liệu của p1 là gì?",
        80: "AW Computing theo dõi thông tin đơn hàng trong các đối tượng tùy chỉnh có tên là Order_c và Order_Line_c. Hiện tại, tất cả thông tin vận chuyển được lưu trữ trong đối tượng Order_c. Công ty muốn mở rộng ứng dụng đơn hàng của mình để hỗ trợ giao hàng chia nhỏ (split shipments) sao cho bất kỳ số lượng bản ghi Order_Line_c nào trên một Order_c duy nhất đều có thể được chuyển đến các địa điểm khác nhau. Lập trình viên nên thêm gì để thực hiện yêu cầu này?",
        81: "Một lập trình viên đã viết mã Apex thực hiện lệnh gọi (callout) ra hệ thống bên ngoài. Lập trình viên nên viết thử nghiệm (test) như thế nào để cung cấp độ bao phủ thử nghiệm (test coverage)?",
        82: "Một lập trình viên cần một phương thức Apex có thể xử lý các bản ghi Account hoặc Contact. Chữ ký phương thức (method signature) nào lập trình viên nên sử dụng?",
        83: "Một lập trình viên xác định các trigger sau trên đối tượng Expense__c: deleteExpense, applyDefaultsToExpense, validateExpenseUpdate; Các trigger này xử lý lần lượt các sự kiện before delete, before insert và before update. Hai kỹ thuật nào lập trình viên nên triển khai để đảm bảo tuân thủ các thực hành tốt nhất cho trigger? (Chọn 2)",
        84: "Hai giai đoạn nào nằm trong khung lan truyền Aura Application Event của Salesforce? (Chọn 2)",
        85: "Đoạn mã dưới đây giải tuần tự hóa (deserialized) đầu vào thành một danh sách Account. Việc sửa đổi mã nào nên được thực hiện để chèn các Account sao cho quyền bảo mật cấp độ trường (field-level security) được tôn trọng?",
        86: "Hai vị trí nào mà lập trình viên có thể tìm thấy thông tin về trạng thái của các phương thức batch hoặc future?",
        87: "Hai đặc điểm nào liên quan đến các công thức (formulas)? (Chọn 2)",
        88: "Giá trị ban đầu cho một trường số trên một bản ghi là 1. Người dùng đã cập nhật giá trị của trường số thành 10. Hành động này kích hoạt một cập nhật trường của quy trình làm việc (workflow field update), thay đổi giá trị của trường số thành 11. Sau khi cập nhật trường của quy trình làm việc, một trigger update được kích hoạt. Giá trị của trường số của đối tượng được lấy từ Trigger.old là bao nhiêu?",
        89: "Một lập trình viên đã tạo một trigger trên đối tượng Account và muốn kiểm tra xem trigger đó đã được tối ưu hóa cho xử lý hàng loạt (bulkified) đúng cách chưa. Nhóm lập trình viên quyết định trigger nên được thử nghiệm với 200 bản ghi tài khoản với tên duy nhất. Hai điều nào nên được thực hiện để tạo dữ liệu thử nghiệm trong unit test với lượng mã ít nhất? (Chọn 2)",
        90: "Các giá trị 'HIGH', 'MEDIUM' và 'LOW' được xác định là các giá trị phổ biến cho nhiều picklist trên các đối tượng khác nhau. Cách tiếp cận nào mà lập trình viên có thể thực hiện để hợp lý hóa việc bảo trì các picklist và giá trị của chúng, đồng thời giới hạn các giá trị ở những giá trị được đề cập ở trên?",
        91: "Hành động nào sau đây có thể khiến các trigger được kích hoạt?",
        92: "Mã nào trong trang Visualforce và/hoặc bộ điều khiển (controller) có thể gây ra lỗ hổng bảo mật?",
        93: "Một lập trình viên đang xây dựng chức năng tìm kiếm tùy chỉnh sử dụng SOSL để tìm kiếm các bản ghi account và contact khớp với thuật ngữ tìm kiếm của người dùng cuối. Tính năng này được hiển thị thông qua một Lightning Web Component và người dùng cuối có thể cung cấp một danh sách các thuật ngữ để tìm kiếm. Xem xét đoạn mã dưới đây: Số lượng thuật ngữ tìm kiếm tối đa mà người dùng cuối có thể cung cấp để thực hiện tìm kiếm thành công mà không gặp giới hạn hệ thống (governor limit) là bao nhiêu?",
        94: "Một lập trình viên có yêu cầu viết mã Apex để cập nhật một số lượng lớn các bản ghi account hàng đêm. Quản trị viên hệ thống cần có thể lập lịch để lớp này chạy sau giờ làm việc trên cơ sở khi cần thiết. Định nghĩa lớp nào nên được sử dụng để triển khai thành công yêu cầu này?",
        95: "Cloud Kicks có một quy trình nhiều màn hình (multi-screen flow) mà các đại lý trung tâm cuộc gọi của họ sử dụng khi xử lý các cuộc gọi dịch vụ khách hàng đến. Tại một trong các bước trong quy trình, các đại lý nên được trình bày một danh sách các số đơn hàng và ngày được truy xuất từ hệ thống quản lý đơn hàng bên ngoài theo thời gian thực và hiển thị trên màn hình. Lập trình viên nên sử dụng gì để đáp ứng yêu cầu này?",
        96: "Một lập trình viên phải cung cấp các giao diện người dùng tùy chỉnh khi người dùng chỉnh sửa một Contact trong Salesforce Classic hoặc Lightning Experience. Lập trình viên nên sử dụng gì để ghi đè (override) nút Edit của Contact và cung cấp chức năng này?",
        97: "Một lập trình viên cần triển khai chức năng cho một đại lý dịch vụ để thu thập nhiều thông tin từ khách hàng nhằm gửi thẻ tín dụng thay thế. Công cụ tự động hóa nào đáp ứng các yêu cầu này?",
        98: "Một lập trình viên đang tạo một lightning web component để hiển thị danh sách các bản ghi bán hàng. Người dùng Đại diện bán hàng sẽ có thể thấy trường hoa hồng (commission) trên mỗi bản ghi. Trợ lý bán hàng sẽ có thể thấy tất cả các trường trên bản ghi ngoại trừ trường hoa hồng. Điều này nên được thực thi như thế nào để component hoạt động cho cả hai người dùng mà không hiển thị bất kỳ lỗi nào?",
        99: "Một nhóm gồm nhiều lập trình viên làm việc trong các tổ chức (orgs) riêng lẻ của họ có cùng cấu hình với tổ chức production. Loại tổ chức nào phù hợp nhất cho kịch bản này?",
        100: "Một lập trình viên được giao nhiệm vụ thực hiện đánh giá bảo mật của lớp Apex ContactSearch tồn tại trong hệ thống. Trong lớp này, lập trình viên xác định phương thức sau đây là một mối đe dọa bảo mật: Hai cách nào lập trình viên có thể cập nhật phương thức để ngăn chặn cuộc tấn công SOQL Injection? (Chọn 2)"
    }

    updated_count = 0
    for q in questions:
        q_id = q.get('id')
        if q_id in translations:
            q['explanation']['vi_question'] = translations[q_id]
            updated_count += 1

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print(f"Updated {updated_count} questions (51-100).")

if __name__ == "__main__":
    update_questions()
