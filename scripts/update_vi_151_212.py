import json
import os

def update_questions():
    file_path = r'c:\Development\Antigravity\Salesforce-PD1\src\data\questions.json'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    translations = {
        151: "Một tổ chức có một Visual Workflow hiện có dùng để tạo Opportunity với một thành phần update records. Developer phải cập nhật Visual Workflow này để đồng thời tạo một Contact và lưu trữ ID của Contact vừa được tạo vào Opportunity. Developer nên thực hiện cập nhật nào trong Visual Workflow?",
        152: "Ursa Major Solar (UMS) sử dụng một đối tượng tùy chỉnh có tên là Vendor. Đối tượng tùy chỉnh Vendor có quan hệ Master-Detail với đối tượng Account tiêu chuẩn. Dựa trên một số cuộc thảo luận nội bộ, quản trị viên UC đã cố gắng thay đổi quan hệ Master-Detail thành quan hệ Lookup nhưng không thể thực hiện được. Nguyên nhân khả thi nào khiến thay đổi này không được cho phép?",
        153: "Universal Containers gần đây đã chuyển đổi từ Classic sang Lightning Experience. Một trong các quy trình nghiệp vụ của họ yêu cầu một số giá trị từ đối tượng Opportunity phải được gửi qua một callout HTTP REST đến hệ thống quản lý đơn hàng bên ngoài dựa trên hành động do người dùng khởi xướng trên trang chi tiết Opportunity. Các giá trị ví dụ là: Name, Amount, Account. Hai phương pháp nào developer nên triển khai để đáp ứng yêu cầu nghiệp vụ? (Chọn 2)",
        154: "Đối tượng tùy chỉnh Job_Application__c có một trường là quan hệ Master-Detail với đối tượng Contact, trong đó đối tượng Contact là Master. Như một phần của việc triển khai tính năng, một developer cần lấy một danh sách chứa tất cả các bản ghi Contact có Industry của Account liên quan là 'Technology', đồng thời lấy các bản ghi Job_Application__c liên quan của Contact đó. Dựa trên các mối quan hệ của đối tượng, câu lệnh nào là hiệu quả nhất để lấy danh sách các Contact?",
        155: "Loại ngoại lệ (exception) nào không thể bị bắt (catch)?",
        156: "Một developer đã hoàn thành các sửa đổi cho một tính năng tùy chỉnh bao gồm hai thành phần: Trigger Apex và class Trigger Handler. Hai yếu tố nào developer phải tính đến để triển khai sửa đổi lên môi trường production một cách chính xác? (Chọn 2)",
        157: "Một developer cần có các bản ghi với các giá trị trường cụ thể để kiểm tra một class Apex mới. Developer nên làm gì để đảm bảo dữ liệu có sẵn cho bài kiểm tra?",
        158: "Một developer phải tạo một component Lightning cho phép người dùng nhập thông tin bản ghi Contact để tạo một bản ghi Contact mới, bao gồm một trường tùy chỉnh Salary__c. Developer nên sử dụng thành phần nào cùng với lightning-record-edit-form để trường Salary__c hoạt động như một đầu vào tiền tệ (currency input) và chỉ hiển thị cũng như có thể chỉnh sửa bởi những người dùng có quyền cấp trường (field level permissions) chính xác trên trường Salary__c?",
        159: "Universal Containers có một số lượng lớn các ứng dụng tùy chỉnh được xây dựng bằng framework JavaScript của bên thứ ba và được hiển thị bằng các trang Visualforce. Công ty muốn cập nhật các ứng dụng này để áp dụng kiểu dáng (styling) giống với giao diện của Lightning Experience. Developer nên làm gì để đáp ứng yêu cầu nghiệp vụ một cách nhanh nhất và hiệu quả nhất?",
        160: "Trong giao diện Lightning UI, developer nên tìm thông tin về một Paused Flow Interview ở đâu?",
        161: "Ba lợi ích của việc sử dụng các tùy chỉnh khai báo (declarative) so với code là gì? (Chọn 3)",
        162: "Universal Containers sử dụng Service Cloud với một trường tùy chỉnh, Stage__c, trên đối tượng Case. Ban quản lý muốn gửi một email nhắc nhở theo dõi 6 giờ sau khi trường Stage__c được đặt thành \"Waiting on Customer\". Quản trị viên bán hàng muốn đảm bảo giải pháp được sử dụng là an toàn khi xử lý hàng loạt (bulk safe). Hai công cụ tự động hóa nào developer nên khuyến nghị để đáp ứng các yêu cầu nghiệp vụ này? (Chọn 2)",
        163: "Một developer đã tạo một ứng dụng quản lý đơn hàng tùy chỉnh sử dụng một class Apex. Đơn hàng được đại diện bởi đối tượng Order và đối tượng OrderItem có quan hệ Master-Detail với Order. Trong quá trình xử lý đơn hàng, một đơn hàng có thể được chia thành nhiều đơn hàng. Developer nên làm gì để cho phép mã của họ chuyển một số bản ghi OrderItem hiện có sang một bản ghi Order mới?",
        164: "Hai cách nào mà một controller và extension có thể được chỉ định trên một trang Visualforce? (Chọn 2)",
        165: "Class Apex nào chứa các phương thức trả về lượng tài nguyên đã được sử dụng cho một giới hạn (governor) cụ thể, chẳng hạn như số lượng câu lệnh DML?",
        166: "Hành động nào mặc định gây ra việc kích hoạt Before Trigger cho đối tượng Account?",
        167: "Một quản trị viên Salesforce đang tạo một record-triggered flow. Khi một số tiêu chí nhất định được đáp ứng, flow phải gọi một phương thức Apex để thực hiện kiểm tra tính hợp lệ phức tạp liên quan đến một số loại đối tượng. Khi tạo phương thức Apex, developer nên sử dụng annotation nào để đảm bảo phương thức có thể được sử dụng bên trong flow?",
        168: "Universal Containers thuê một developer để xây dựng một trang tìm kiếm tùy chỉnh giúp người dùng tìm thấy các Account mà họ muốn. Người dùng sẽ có thể tìm kiếm theo Name, Description và một trường nhận xét tùy chỉnh. Developer nên lưu ý hai cân nhắc nào khi quyết định giữa SOQL và SOSL? (Chọn 2)",
        169: "Một developer đã tạo trigger Apex này gọi MyClass.myStaticMethod: Trigger myTrigger on Contact (before insert) { MyClass.myStaticMethod(trigger.new, trigger.oldMap); }. Developer tạo một class test với một phương thức test gọi MyClass.myStaticMethod, dẫn đến tổng độ bao phủ mã (code coverage) là 81%. Điều gì xảy ra khi developer cố gắng triển khai trigger và hai class lên production, giả sử không có mã nào khác tồn tại?",
        170: "Hai lệnh sfdx nào có thể được sử dụng để thêm dữ liệu kiểm tra vào một sandbox Developer? (Chọn 2)",
        171: "Một chiến lược Next Best Action sử dụng thành phần Enhance Element gọi một phương thức Apex để xác định mức chiết khấu cho một Contact, dựa trên một số yếu tố. Định nghĩa chính xác của phương thức Apex là gì?",
        172: "Một developer đã tạo một Lightning Web Component có tên là statusComponent để chèn vào trang record Account. Hai điều nào developer nên làm để component này có sẵn? (Chọn 2)",
        173: "Hai cách nào developer có thể lấy trạng thái của một job đã được đưa vào hàng đợi (enqueued) cho một class triển khai interface Queueable? (Chọn 2)",
        174: "Cho đoạn mã sau đây, là một phần của custom controller cho một trang Visualforce: public void updateContact(Contact thisContact) { thisContact.Is_Active__c = false; try { update thisContact; } catch(Exception e) { String errorMessage = 'An error occurred while updating the Contact, ' + e.getMessage(); ApexPages.addMessage(new ApexPages.Message(ApexPages.Severity.FATAL, errorMessage)); } }. Có hai cách nào để khối try/catch có thể được bao bọc để thực thi các quyền cấp đối tượng và cấp trường, đồng thời ngăn chặn câu lệnh DML thực thi nếu người dùng hiện tại không có mức độ truy cập phù hợp? (Chọn 2)",
        175: "Làm thế nào để cung cấp một giao diện người dùng tùy chỉnh khi người dùng chỉnh sửa một Account trong Lightning Experience?",
        176: "Một component Lightning có một thuộc tính wired, searchResults, lưu trữ một danh sách các Opportunity. Định nghĩa nào về phương thức Apex, mà thuộc tính searchResults được wired tới, nên được sử dụng?",
        177: "Tham khảo đoạn mã sau chạy trong một khối execute anonymous: for(List<Lead> theseLeads : [SELECT LastName, Company, Email FROM Lead LIMIT 2000]) { for(Lead thisLead : theseLeads) { if (thisLead.Email == null) thisLead.Email = assignGenericEmail(thisLead.LastName, thisLead.Company); } Database.update(theseLeads, false); }. Trong một môi trường mà toàn bộ tập kết quả được trả về, kết quả khả thi của đoạn mã này là gì?",
        178: "Hai cách thực hành tốt nhất (best practices) nào liên quan đến việc xử lý sự kiện Aura component và application? (Chọn 2)",
        179: "Tính năng nào của Salesforce cho phép developer xem người dùng đăng nhập vào Salesforce lần cuối khi nào nếu không yêu cầu thông báo thời gian thực?",
        180: "Một developer phải sửa đổi đoạn mã sau để ngăn chặn số lượng truy vấn SOQL vượt quá giới hạn governor của nền tảng. public without sharing class OpportunityService { public static List<OpportunityLineItem> getOpportunityProducts(Set<Id> opportunityIds) { List<OpportunityLineItem> oppLineItems = new List<OpportunityLineItem>(); for (Id thisOppId : opportunityIds) { oppLineItems.addAll([SELECT Id FROM OpportunityLineItem WHERE OpportunityId = :thisOppId]); } return oppLineItems; } }. Phương thức trên có thể được gọi trong quá trình thực thi trigger thông qua một component Lightning. Kỹ thuật nào nên được triển khai để tránh đạt đến giới hạn governor?",
        181: "Một developer có các yêu cầu sau: Tính tổng số tiền trên một đơn hàng; Tính số tiền của từng dòng dựa trên số lượng được chọn và giá; Di chuyển các dòng đơn hàng sang một Order khác nếu dòng đó không còn hàng. Triển khai mối quan hệ nào hỗ trợ các yêu cầu này?",
        182: "Phân đoạn mã Lightning nào nên được viết để khai báo các dependency trên một component Lightning, c:accountList, được sử dụng trong một trang Visualforce?",
        183: "Câu lệnh nào tạo ra một danh sách các Lead và Contact có một trường chứa cụm từ 'ACME'?",
        184: "Hai thiết lập nào phải được xác định để cập nhật một bản ghi của một đối tượng liên kết (junction object)? (Chọn 2)",
        185: "Ba phát biểu nào đúng về các ngoại lệ tùy chỉnh (custom exceptions) trong Apex? (Chọn 3)",
        186: "Một Opportunity cần có một số tiền được tổng hợp (roll up) từ một đối tượng tùy chỉnh không nằm trong quan hệ Master/Detail. Làm thế nào để đạt được điều này?",
        187: "Khía cạnh nào của lập trình Apex bị giới hạn do cơ chế đa thuê bao (multitenancy)?",
        188: "Tham khảo đoạn mã sau cho một môi trường có hơn 200 Account thuộc ngành 'Technology': for (Account thisAccount : [SELECT Id, Industry FROM Account LIMIT 250]) { if (thisAccount.Industry == 'Technology') { thisAccount.Is_Tech__c = true; } update thisAccount; }. Khi đoạn mã thực thi, điều gì sẽ xảy ra như một kết quả của transaction Apex?",
        189: "Ba cách nào để developer thực thi các bài kiểm tra (tests) trong một tổ chức? (Chọn 3)",
        190: "Developer nên sử dụng gì để lấy Id và Name của tất cả các Lead, Account và Contact có tên công ty là \"Universal Containers\"?",
        191: "Universal Containers đang xây dựng một ứng dụng tuyển dụng với đối tượng Applicant lưu trữ thông tin về một cá nhân đại diện cho một công việc. Mỗi ứng viên có thể ứng tuyển vào nhiều công việc. Developer nên triển khai gì để đại diện cho việc một ứng viên đã ứng tuyển vào một công việc?",
        192: "Một developer phải viết một phương thức Apex sẽ được gọi từ một Lightning Component. Phương thức này có thể xóa một account được lưu trữ trong biến accountRec. Developer sử dụng phương thức nào để đảm bảo chỉ những người dùng có quyền xóa Account mới có thể thực hiện việc xóa thành công?",
        193: "Một custom Visualforce controller gọi phương thức ApexPages.addMessage(), nhưng không có thông báo nào được hiển thị trên trang. Thành phần nào nên được thêm vào trang Visualforce để hiển thị thông báo?",
        194: "Get Cloudy Consulting (GCC) có rất nhiều server lưu trữ các website của khách hàng. GCC muốn cung cấp một trang trạng thái server luôn được hiển thị trong trung tâm cuộc gọi của mình. Nó nên cập nhật theo thời gian thực với bất kỳ thay đổi nào được thực hiện đối với bất kỳ server nào. Để đáp ứng điều này ở phía server, một developer đã tạo một platform event có tên là Server Update. Developer đang làm việc trên một Lightning Web Component để hiển thị thông tin. Những gì nên được thêm vào Lightning Web Component để cho phép developer tương tác với platform event Server Update?",
        195: "Một quản trị viên Salesforce đã sử dụng Flow Builder để tạo một flow có tên là \"accountOnboarding\". Flow này phải được sử dụng bên trong một component Aura. Developer nên sử dụng thẻ nào để hiển thị flow trong component?",
        196: "Universal Containers quyết định chỉ sử dụng phát triển khai báo (declarative development) để xây dựng một ứng dụng Salesforce mới. Ba tùy chọn nào nên được sử dụng để xây dựng tầng database cho ứng dụng? (Chọn 3)",
        197: "Cloud Kicks (CK) muốn sao lưu tất cả dữ liệu và file đính kèm trong tổ chức Salesforce mỗi tháng một lần. Developer nên sử dụng cách tiếp cận nào để đáp ứng yêu cầu này?",
        198: "Một developer đang tạo một ứng dụng chứa nhiều Lightning Web Components. Một trong các component con được sử dụng cho mục đích điều hướng. Khi người dùng nhấp vào một nút có tên là Next, component cha phải được thông báo để có thể điều hướng sang trang tiếp theo. Làm thế nào để thực hiện việc này?",
        199: "AW Computing (AWC) xử lý các đơn hàng trong Salesforce và lưu trữ tồn kho sản phẩm trong một trường, Inventory__c, trên một đối tượng tùy chỉnh, Product__c. Khi một đơn hàng cho Product__c được đặt, trường Inventory__c sẽ được giảm đi theo số lượng của đơn hàng bằng một trigger Apex. AWC muốn việc giảm tồn kho theo thời gian thực cho một sản phẩm được gửi đến nhiều hệ thống bên ngoài, bao gồm cả một số hệ thống trong tương lai mà công ty đang lên kế hoạch. Developer nên thêm gì vào mã tại vị trí giữ chỗ để đáp ứng các yêu cầu này?",
        200: "Universal Containers sử dụng một ứng dụng Order Management đơn giản. Trên các Order Line, tổng số dòng đơn hàng được tính bằng cách nhân giá sản phẩm với số lượng đặt hàng. Có một mối quan hệ Master-Detail giữa đối tượng Order và đối tượng Order Line. Cách tốt nhất để tính tổng của tất cả các tổng số dòng đơn hàng trên tiêu đề đơn hàng là gì?",
        201: "Hai phát biểu nào đúng về việc sử dụng annotation @testSetup trong một class test Apex? (Chọn 2)",
        202: "Lợi ích của việc phát triển ứng dụng trong môi trường đa thuê bao (multi-tenant) là gì?",
        203: "Tham khảo đoạn mã Apex sau: Integer x = 0; do { x = 1; x++; } while (x < 1); System.debug(x); Giá trị của x khi được ghi vào debug log là bao nhiêu?",
        204: "Một developer cần triển khai một SOAP Web Service tùy chỉnh được sử dụng bởi một ứng dụng Web bên ngoài. Developer chọn bao gồm các phương thức trợ giúp không được ứng dụng Web sử dụng trong việc triển khai class Web Service. Phân đoạn mã nào cho thấy khai báo chính xác của class và các phương thức?",
        205: "Ba tài nguyên Salesforce nào có thể được truy cập từ một Lightning Web Component? (Chọn 3)",
        206: "Về mô hình MVC, hai lợi thế của việc triển khai tầng view của ứng dụng Salesforce bằng cách phát triển dựa trên Lightning Web Component so với Visualforce là gì? (Chọn 2)",
        207: "Một developer cần tạo một nút tùy chỉnh cho đối tượng Account mà khi nhấp vào, sẽ thực hiện một loạt các tính toán và chuyển hướng người dùng đến một trang Visualforce tùy chỉnh. Ba thuộc tính nào cần được định nghĩa với các giá trị trong thẻ <apex:page> để hoàn thành việc này? (Chọn 3)",
        208: "Một developer cần tạo một interface tùy chỉnh trong Apex. Ba cân nhắc nào developer phải lưu ý khi phát triển Apex Interface? (Chọn 3)",
        209: "Những gì có thể được phát triển bằng cách sử dụng framework Lightning Component?",
        210: "Mã nào hiển thị nội dung của một trang Visualforce dưới dạng PDF?",
        211: "Universal Containers sử dụng mối quan hệ Master-Detail và lưu trữ ngày có hàng (availability date) trên mỗi Line Item của một Order và các Order chỉ được giao khi tất cả các Line Item đều có hàng. Phương pháp nào nên được sử dụng để tính ngày giao hàng dự kiến cho một Order?",
        212: "Một developer có một class custom controller duy nhất hoạt động với một Visualforce Wizard để hỗ trợ tạo và chỉnh sửa nhiều sObject. Wizard chấp nhận dữ liệu từ các đầu vào của người dùng trên nhiều trang Visualforce và từ một tham số trên URL ban đầu. Ba câu lệnh nào hữu ích bên trong unit test để kiểm tra custom controller một cách hiệu quả? (Chọn 3)"
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
