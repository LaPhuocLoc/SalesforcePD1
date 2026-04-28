import json
import os

def update_translations():
    target_file = r'c:\Development\Antigravity\Salesforce-PD1\src\data\questions.json'
    if not os.path.exists(target_file):
        print(f"File {target_file} not found.")
        return

    with open(target_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Mapping of ID to full vi_question translation
    translations = {
        1: "Application Events tuân theo mô hình publish-subscribe truyền thống. Phương thức nào được sử dụng để kích hoạt (fire) một event?",
        2: "Một workflow cập nhật giá trị của một trường tùy chỉnh (custom field) cho một Account đã tồn tại. Làm thế nào để một lập trình viên có thể truy cập giá trị trường tùy chỉnh đã được cập nhật từ một trigger?",
        3: "Một lập trình viên muốn lấy thông tin các Contact và User có địa chỉ email là 'dev@uc.com'. Câu lệnh SOSL nào lập trình viên nên sử dụng?",
        4: "Cho đoạn code trigger Lead sau: [leadTrigger]. Lập trình viên nhận được lỗi triển khai (deployment errors) mỗi khi cố gắng triển khai từ Sandbox lên Production. Lập trình viên nên làm gì để đảm bảo triển khai thành công?",
        5: "Nếu mã Apex thực thi bên trong phương thức execute() của một Apex class khi triển khai interface Batchable, hai phát biểu nào sau đây là đúng về governor limits? (Chọn 2)",
        6: "Một lập trình viên tạo một Lightning Web Component (LWC) để import một phương thức bên trong một Apex class. Khi nhấn nút Validation, phương thức đó sẽ thực thi các kiểm tra (validations) phức tạp. Trong kịch bản triển khai này, thành phần (artifact) nào là một phần của Controller theo kiến trúc MVC?",
        7: "Quy trình tự động hóa nào nên được sử dụng để gửi một outbound message mà không cần sử dụng mã Apex?",
        8: "Giả sử 'name' là một String nhận được từ thẻ <apex:inputText> trên một trang Visualforce, hai câu truy vấn SOQL nào sau đây là an toàn trước lỗi SOQL injection? (Chọn 2)",
        9: "Một phương thức Apex, getAccounts, trả về một List các Account dựa trên một search Term, có sẵn để Lightning Web Components sử dụng. Định nghĩa đúng của một thuộc tính (property) Lightning Web Component sử dụng phương thức getAccounts là gì?",
        10: "Một lập trình viên muốn nhập 500 bản ghi Opportunity vào một sandbox. Vì lý do gì lập trình viên chọn Data Loader thay vì Data Import Wizard?",
        11: "Khi nhập (import) và xuất (export) dữ liệu vào Salesforce, hai phát biểu nào sau đây là đúng? (Chọn 2)",
        12: "Ba cân nhắc nào là đúng khi sử dụng annotation @InvocableMethod trong Apex? (Chọn 3)",
        13: "Hai loại tự động hóa quy trình nào có thể được sử dụng để tính toán chi phí vận chuyển cho một Đơn hàng (Order) khi Đơn hàng được tạo và áp dụng một tỷ lệ phần trăm của chi phí vận chuyển cho một số Sản phẩm của Đơn hàng (Order Products) liên quan? (Chọn 2)",
        14: "Ba phát biểu nào sau đây là chính xác về debug logs? (Chọn 3)",
        15: "Một transaction đệ quy được khởi tạo bởi một câu lệnh DML tạo các bản ghi cho hai đối tượng này: Accounts và Contacts. Trigger của Account đạt đến độ sâu stack là 16. Phát biểu nào sau đây là đúng về kết quả của transaction này?",
        16: "Khung làm việc (framework) Lightning component giúp lập trình viên triển khai các giải pháp nhanh hơn như thế nào?",
        17: "Một lập trình viên tạo một ngoại lệ tùy chỉnh (custom exception) như sau: public class ParityException extends Exception { }. Có hai cách nào để lập trình viên có thể kích hoạt (fire) ngoại lệ trong Apex? (Chọn 2)",
        18: "Cloud Kicks (CK) muốn giảm chi phí vận chuyển đồng thời làm cho quy trình vận chuyển hiệu quả hơn. Nhân viên phân phối khuyên CK triển khai địa chỉ toàn cầu (global addresses) để cho phép nhiều Account chia sẻ một địa chỉ lấy hàng mặc định. Lập trình viên được giao nhiệm vụ tạo đối tượng và mối quan hệ hỗ trợ cho yêu cầu kinh doanh này và sử dụng Menu Setup để tạo một đối tượng tùy chỉnh tên là 'Global Address'. Lập trình viên nên thêm trường nào để tạo ra mô hình hiệu quả nhất hỗ trợ nhu cầu kinh doanh?",
        19: "Một tổ chức theo dõi các đơn hàng của khách hàng trên đối tượng Order và các dòng sản phẩm của Order trên đối tượng Line Item. Đối tượng Line Item có mối quan hệ Master-Detail với đối tượng Order. Một lập trình viên có yêu cầu tính toán số tiền đơn hàng trên Order và số tiền trên mỗi Line Item dựa trên số lượng và giá cả. Triển khai nào sau đây là đúng?",
        20: "Lập trình viên nên làm gì để kiểm tra độ bao phủ mã (code coverage) của một class sau khi chạy tất cả các test?",
        21: "Nên sử dụng công cụ nào để tạo các scratch org?",
        22: "Một lập trình viên muốn đánh dấu mỗi Account trong một List<Account> là Active hoặc Inactive dựa trên giá trị trường Last Modified Date đã quá 90 ngày. Kỹ thuật Apex nào lập trình viên nên sử dụng?",
        23: "Trong một Lightning Web Component, cách đúng để tham chiếu một tài sản hình ảnh (image asset) được lưu trữ dưới dạng một Static Resource tên là 'CompanyLogo' là gì?",
        24: "Trong hai trường hợp nào lập trình viên nên sử dụng Apex triggers thay vì Process Builder? (Chọn 2)",
        25: "Làm thế nào để một lập trình viên có thể lấy danh sách các bản ghi Account mà người dùng hiện tại đã xem gần đây? (Chọn 1)",
        26: "Một lập trình viên cần triển khai một giải pháp cho phép người dùng nhập thông tin và sau đó tạo ra một bản ghi. Công cụ nào nên được sử dụng?",
        27: "Ba tính năng nào có sẵn trong Salesforce DX? (Chọn 3)",
        28: "Một lập trình viên có một phương thức Apex chấp nhận một tham số là một List các ID bản ghi. Phương thức này thực hiện một câu truy vấn SOQL để lấy các bản ghi đó. Làm thế nào để đảm bảo phương thức này an toàn trước lỗi SOQL injection?",
        29: "Ba loại collection nào được hỗ trợ trong Apex? (Chọn 3)",
        30: "Một lập trình viên cần tạo một trigger để đảm bảo rằng khi một Case được tạo, một bản ghi tùy chỉnh liên quan sẽ được tạo tự động. Nên sử dụng loại trigger nào?",
        31: "Sự khác biệt giữa insert và database.insert() trong Apex là gì?",
        32: "Hai câu lệnh nào là đúng về việc sử dụng External ID trong Salesforce? (Chọn 2)",
        33: "Làm thế nào để chỉ định thứ tự thực thi của nhiều trigger trên cùng một đối tượng?",
        34: "Ba kiểu dữ liệu nào có thể được trả về bởi một câu truy vấn SOQL? (Chọn 3)",
        35: "Làm thế nào để một lập trình viên có thể ngăn chặn việc xóa một bản ghi Account nếu nó có các bản ghi Case liên quan?",
        36: "Ba loại mối quan hệ nào được hỗ trợ trong Salesforce? (Chọn 3)",
        37: "Sự khác biệt giữa Public và Global access modifiers trong Apex là gì?",
        38: "Làm thế nào để một lập trình viên có thể chạy một đoạn mã Apex một lần duy nhất?",
        39: "Ba đặc điểm của một Master-Detail relationship là gì? (Chọn 3)",
        40: "Làm thế nào để kích hoạt (enable) debug logs cho một người dùng cụ thể?",
        41: "Ba loại action nào có thể được thực hiện bởi một Workflow Rule? (Chọn 3)",
        42: "Một lập trình viên cần viết một đoạn mã để cập nhật hàng loạt 10,000 bản ghi. Kỹ thuật nào nên được sử dụng để tránh lỗi governor limits?",
        43: "Sự khác biệt giữa List và Set trong Apex là gì?",
        44: "Làm thế nào để tham chiếu một trường của một đối tượng liên quan trong một câu truy vấn SOQL (Relationship Query)?",
        45: "Ba cách để thực thi mã Apex là gì? (Chọn 3)",
        46: "Làm thế nào để xử lý các ngoại lệ (exceptions) trong Apex?",
        47: "Sự khác biệt giữa Before và After triggers là gì?",
        48: "Làm thế nào để thực hiện một câu truy vấn SOQL trong một trigger một cách hiệu quả (Bulkified)?",
        49: "Ba loại giới hạn (governor limits) nào phổ biến trong Salesforce? (Chọn 3)",
        50: "Làm thế nào để một lập trình viên có thể xem kết quả của System.debug()?"
    }

    for item in data:
        q_id = item.get('id')
        if q_id in translations:
            if 'explanation' not in item:
                item['explanation'] = {}
            item['explanation']['vi_question'] = translations[q_id]

    with open(target_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Updated {len(translations)} questions (1-50).")

if __name__ == '__main__':
    update_translations()
