import json
import os

def update_questions():
    file_path = r'c:\Development\Antigravity\Salesforce-PD1\src\data\questions.json'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    translations = {
        101: "Một developer làm việc trong một tổ chức có hàng triệu bản ghi Account. Câu query SOQL nào sẽ tránh được các vấn đề về hiệu suất và Governor Limits?",
        102: "Những câu lệnh nào có thể được sử dụng để lấy thông tin về các giới hạn (limits) hiện tại và các giới hạn tối đa cho một tổ chức? (Chọn 2)",
        103: "Một developer muốn lấy toàn bộ metadata của tổ chức và chuyển nó sang một tổ chức khác. Công cụ nào nên được sử dụng?",
        104: "Một developer nhận thấy các bài kiểm tra (test) trong một tổ chức tốn nhiều thời gian để chạy và thường xuyên gây ra các vấn đề về giới hạn (limit). Developer nên thực hiện hành động nào để tối ưu hóa việc thực thi test?",
        105: "Một developer viết một trigger trên đối tượng Contact. Trigger này cần truy cập vào một trường trên đối tượng Account cha. Cách tốt nhất để thực hiện việc này là gì?",
        106: "Một công ty muốn triển khai một giải pháp tự động hóa để gửi email thông báo cho khách hàng khi một Case được đóng. Giải pháp này nên được triển khai như thế nào?",
        107: "Một developer cần tạo một trang Visualforce hiển thị danh sách các bản ghi Account và cho phép người dùng lọc danh sách theo Industry. Cách tốt nhất để thực hiện việc này là gì?",
        108: "Một developer đang viết một class Apex và muốn đảm bảo rằng một biến nhất định không thể bị thay đổi sau khi đã được gán giá trị lần đầu tiên. Từ khóa nào nên được sử dụng?",
        109: "Một developer cần thực hiện một callout HTTP từ một trigger Apex. Điều gì là bắt buộc để thực hiện việc này?",
        110: "Một developer muốn hiển thị một thông báo lỗi tùy chỉnh trên một trang Visualforce khi một ngoại lệ (exception) xảy ra trong controller. Developer nên sử dụng thành phần nào?",
        111: "Một developer đang viết một bài kiểm tra (test) cho một trigger trên đối tượng Opportunity. Developer nên sử dụng phương thức nào để đảm bảo rằng các giới hạn (governor limits) được reset cho đoạn mã đang được kiểm tra?",
        112: "Một developer cần truy vấn tất cả các bản ghi Contact có liên quan đến một danh sách các Account. Câu query nào là hiệu quả nhất?",
        113: "Một developer muốn sử dụng một Lightning Web Component (LWC) để hiển thị thông tin từ một đối tượng tùy chỉnh. Decorator nào nên được sử dụng để cho phép component nhận dữ liệu từ một component cha?",
        114: "Một developer đang triển khai một giải pháp sử dụng Platform Events. Phương thức nào được sử dụng để bắn (publish) một sự kiện từ mã Apex?",
        115: "Một developer cần tạo một quan hệ giữa hai đối tượng sao cho khi bản ghi cha bị xóa, các bản ghi con cũng bị xóa theo. Loại quan hệ nào nên được sử dụng?",
        116: "Một developer muốn đảm bảo rằng mã Apex của họ tuân thủ các quy tắc bảo mật về quyền truy cập bản ghi (sharing rules). Từ khóa nào nên được sử dụng trong khai báo class?",
        117: "Một developer đang viết một bài kiểm tra (test) và muốn tạo dữ liệu giả mà không làm ảnh hưởng đến dữ liệu thật trong tổ chức. Developer nên sử dụng annotation nào để thiết lập dữ liệu dùng chung cho tất cả các phương thức kiểm tra trong class?",
        118: "Một developer muốn hiển thị một danh sách các bản ghi trong một Lightning Web Component (LWC). Phương thức nào là tốt nhất để lấy dữ liệu từ Salesforce một cách hiệu quả?",
        119: "Một developer cần triển khai một logic phức tạp để kiểm tra tính hợp lệ của dữ liệu trước khi bản ghi được lưu vào database. Loại trigger nào nên được sử dụng?",
        120: "Một developer muốn sử dụng một component Aura bên trong một trang Visualforce. Công cụ nào cho phép thực hiện việc này?",
        121: "Một developer cần lấy ID của bản ghi hiện tại trong một Lightning Web Component (LWC) được đặt trên một trang record. Developer nên sử dụng decorator nào cho biến recordId?",
        122: "Một developer đang viết một câu query SOSL để tìm kiếm một từ khóa trên nhiều đối tượng. Kết quả trả về của một câu query SOSL trong Apex là gì?",
        123: "Một developer muốn thực thi một đoạn mã Apex hàng ngày vào một thời điểm cụ thể. Interface nào cần được triển khai?",
        124: "Hai ví dụ nào hiển thị đúng kết quả của một câu truy vấn Aggregate (ví dụ: AVG, SUM)? (Chọn 2)",
        125: "Một developer đã tạo ba trường Rollup Summary trên đối tượng tùy chỉnh Project__c: Total_Timesheets__c, Total_Approved_Timesheets__c, Total_Rejected_Timesheets__c. Developer được yêu cầu tạo một trường mới hiển thị tỷ lệ giữa bảng chấm công bị từ chối và bảng chấm công được phê duyệt cho một dự án cụ thể. Hai lợi ích của việc chọn trường công thức (formula field) thay vì trigger Apex để đáp ứng yêu cầu này là gì? (Chọn 2)",
        126: "Một developer được giao nhiệm vụ thực hiện một kiểm tra logic phức tạp bằng Apex như một phần của logic nghiệp vụ nâng cao. Khi gặp class PurchaseOrder, developer phải ném ra một ngoại lệ tùy chỉnh (custom exception). Cách chính xác để developer khai báo một class có thể được sử dụng như một ngoại lệ là gì?",
        127: "Quản trị viên Salesforce đã tạo một trường picklist tùy chỉnh Account_Status__c trên đối tượng Account. Picklist này có các giá trị có thể là \"Inactive\" và \"Active\". Như một phần của quy trình nghiệp vụ mới, ban quản lý muốn đảm bảo một bản ghi Opportunity chỉ được tạo cho các Account được đánh dấu là \"Active\". Một developer được yêu cầu triển khai yêu cầu nghiệp vụ này. Hai công cụ tự động hóa nào nên được sử dụng để đáp ứng nhu cầu nghiệp vụ? (Chọn 2)",
        128: "Một developer muốn truy cập vào bảng giá tiêu chuẩn (standard pricebook) trong tổ chức khi đang viết một class test để kiểm tra một trigger OpportunityLineItem. Phương thức nào cho phép truy cập vào bảng giá?",
        129: "Đoạn mã sau đây được thực thi bởi một Lightning Web Component trong môi trường có hơn 2000 bản ghi Lead:\\n@AuraEnabled\\npublic static void updateLeads() {\\nfor (Lead thisLead : [SELECT Origin__c FROM Lead]) {\\nthisLead.LeadSource = thisLead.Origin__c;\\nupdate thisLead;\\n}\\n}\\nGiới hạn (governor limit) nào có khả năng sẽ bị vượt quá trong transaction Apex này?",
        130: "Một developer phải triển khai một class CheckPaymentProcessor cung cấp các khả năng xử lý thanh toán bằng séc tuân theo những gì được định nghĩa cho thanh toán trong interface PaymentProcessor.\\npublic interface PaymentProcessor {\\nvoid pay(Decimal amount);\\n}\\nCách triển khai nào là chính xác để sử dụng class interface PaymentProcessor?",
        131: "Trong khi làm việc trong một sandbox, một bài kiểm tra Apex bị thất bại khi chạy trong Test Framework, nhưng logic của bài kiểm tra đó lại thành công mà không có ngoại lệ hoặc lỗi nào khi chạy trong Developer Console. Tại sao phương thức này lại thất bại trong sandbox Test Framework nhưng lại thành công trong Developer Console?",
        132: "Khi sử dụng Salesforce DX, developer cần bật tính năng gì để tạo và quản lý các Scratch Org?",
        133: "Thay vì gửi email trực tiếp cho nhân viên hỗ trợ từ Salesforce, Universal Containers muốn thông báo cho một hệ thống bên ngoài khi có một ngoại lệ không được xử lý (unhandled exception) xảy ra. Logic publish/subscribe nào là phù hợp để đáp ứng yêu cầu này?",
        134: "Một developer phải tạo một class CreditCardPayment cung cấp bản triển khai (implementation) của một class Payment hiện có.\\npublic virtual class Payment {\\npublic virtual void makePayment(Decimal amount) { /*implementation*/ }\\n}\\nCách triển khai nào sau đây là chính xác?",
        135: "Universal Containers muốn một nút danh sách (list button) hiển thị một trang Visualforce cho phép người dùng chỉnh sửa nhiều bản ghi. Tính năng Visualforce nào hỗ trợ yêu cầu này?",
        136: "Một developer xem xét đoạn mã sau:\\nBoolean isOK;\\nInteger x;\\nString theString = \"Hello\";\\nif (isOK == false && theString == \"Hello\") {\\nx = 1;\\n} else if (isOK == true && theString == \"Hello\") {\\nx = 2;\\n} else if (isOK != null && theString == \"Hello\") {\\nx = 3;\\n} else {\\nx = 4;\\n}\\nDựa trên mã này, giá trị của x là bao nhiêu?",
        137: "Một developer đã tạo một ứng dụng thời tiết chứa nhiều Lightning Web Components. Một trong các component, có tên là Toggle, có nút chuyển đổi cho đơn vị độ F (Fahrenheit) hoặc độ C (Celsius). Một component khác, có tên là Temperature, hiển thị nhiệt độ hiện tại theo đơn vị được chọn trong component Toggle. Khi người dùng chuyển đổi đơn vị trong component Toggle, thông tin phải được gửi đến Temperature để nhiệt độ có thể được chuyển đổi và hiển thị. Cách được khuyến nghị để thực hiện việc này là gì?",
        138: "Một đối tượng tùy chỉnh Licensed_Professional__c tồn tại trong hệ thống với hai trường Master-Detail cho các đối tượng sau: Certification__c và Contact. Người dùng với vai trò \"Certification Representative\" có thể truy cập các bản ghi Certification mà họ sở hữu và xem các bản ghi Licensed Professional liên quan, tuy nhiên người dùng với vai trò \"Sales Representative\" báo cáo rằng họ không thể xem bất kỳ bản ghi Licensed Professional nào mặc dù họ sở hữu bản ghi Contact liên quan. Hai nguyên nhân có khả năng nhất khiến người dùng trong vai trò \"Sales Representative\" không thể truy cập các bản ghi Licensed Professional là gì? (Chọn 2)",
        139: "Universal Containers có một quy trình hỗ trợ cho phép người dùng yêu cầu hỗ trợ từ đội ngũ kỹ thuật bằng cách sử dụng một đối tượng tùy chỉnh, Engineering_Support__c. Người dùng có thể liên kết nhiều bản ghi Engineering_Support__c với một bản ghi Opportunity duy nhất. Ngoài ra, thông tin tổng hợp về các bản ghi Engineering_Support__c phải được hiển thị trên bản ghi Opportunity. Developer nên triển khai gì để đáp ứng các yêu cầu này?",
        140: "Như một phần của chiến lược làm sạch dữ liệu, AW Computing muốn chủ động xóa các bản ghi Opportunity liên quan khi Account liên quan bị xóa. Công cụ tự động hóa nào nên được sử dụng để đáp ứng yêu cầu nghiệp vụ này?",
        141: "Ba tài nguyên nào trong một Aura Component có thể chứa các hàm JavaScript? (Chọn 3)",
        142: "Một trường tùy chỉnh PrimaryId__c tồn tại trên đối tượng tùy chỉnh Candidate__c. Trường này được sử dụng để lưu trữ số ID của mỗi ứng viên và được đánh dấu là Unique trong định nghĩa schema. Như một phần của quy trình làm giàu dữ liệu, Universal Containers có một tệp CSV chứa dữ liệu cập nhật cho tất cả các ứng viên trong hệ thống. Tệp này chứa Primary Id của mỗi ứng viên dưới dạng một điểm dữ liệu. Universal Containers muốn tải thông tin này lên Salesforce, đồng thời đảm bảo tất cả các hàng dữ liệu được ánh xạ chính xác đến một ứng viên trong hệ thống. Kỹ thuật nào developer nên triển khai để hợp lý hóa việc tải dữ liệu?",
        143: "Ba khả năng của thẻ <ltng:require> khi tải các tài nguyên JavaScript trong các Aura component là gì? (Chọn 3)",
        144: "Trong ví dụ sau, ngữ cảnh chia sẻ (sharing context) nào mà myMethod sẽ thực thi khi được gọi?\\npublic class myClass {\\npublic void myMethod() { /* implementation */ }\\n}",
        145: "Một developer đang triển khai một class Apex cho một hệ thống tài chính. Trong class đó, các biến 'creditAmount' và 'debitAmount' không được phép thay đổi một khi giá trị đã được gán. Hai cách nào developer có thể khai báo các biến để đảm bảo giá trị của chúng chỉ có thể được gán một lần? (Chọn 2)",
        146: "Cloud Kicks Fitness, một đối tác ISV của Salesforce, đang phát triển một ứng dụng managed package. Một trong các module của ứng dụng cho phép người dùng tính toán lượng mỡ cơ thể bằng cách sử dụng class Apex, BodyFat, và phương thức calculateBodyFat() của nó. Chủ sở hữu sản phẩm muốn đảm bảo phương thức này có thể truy cập được bởi người dùng ứng dụng khi phát triển các tùy chỉnh bên ngoài namespace của package ISV. Developer nên thực hiện cách tiếp cận nào để đảm bảo calculateBodyFat() có thể truy cập được bên ngoài namespace của package?",
        147: "Cloud Kicks (CK) muốn đánh giá các ưu điểm của phát triển khai báo (declarative) so với tùy chỉnh lập trình (programmatic) cho các trường hợp sử dụng cụ thể trong việc triển khai Salesforce. Hai đặc điểm của phát triển khai báo so với tùy chỉnh lập trình là gì? (Chọn 2)",
        148: "Cho đoạn mã Anonymous Block sau:\\nList<Case> casesToUpdate = new List<Case>();\\nfor (Case thisCase : [SELECT Id, Status FROM Case LIMIT 50000]) {\\nthisCase.Status = 'Working';\\ncasesToUpdate.add(thisCase);\\n}\\ntry {\\nDatabase.update(casesToUpdate, false);\\n} catch (Exception e) {\\nSystem.debug(e.getMessage());\\n}\\nDeveloper nên cân nhắc điều gì cho một môi trường có hơn 10,000 bản ghi Case?",
        149: "Kết quả đầu ra trong debug log trong trường hợp xảy ra QueryException trong khi gọi phương thức aQuery trong ví dụ sau sẽ là gì?",
        150: "Một developer cần xác nhận rằng một trigger Contact hoạt động chính xác mà không làm thay đổi dữ liệu của tổ chức. Developer nên làm gì để kiểm tra trigger Contact?"
    }

    updated_count = 0
    for q in questions:
        q_id = q.get('id')
        if q_id in translations:
            q['explanation']['vi_question'] = translations[q_id]
            updated_count += 1

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully updated {updated_count} questions.")

if __name__ == "__main__":
    update_questions()
