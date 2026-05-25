# Salesforce PD1 - Bộ Đề Nâng Cấp

> Đã bổ sung: Dịch tiếng Việt • Phân tích đáp án đúng/sai • Từ khóa ghi nhớ

---

## Câu 1

**🔵 Which two components are available to deploy using the Metadata API? (Choose two.)**

- **A.** Lead Conversion Settings ✅
- **B.** Web-to-Case ❌
- **C.** Web-to-Lead ❌
- **D.** Case Settings ✅

**📝 Dịch tiếng Việt:**
> Trong các component sau, 2 cái tên nào được Metadata API hỗ trợ để deploy? (Chọn hai)

**💬 Giải thích gốc (English):**
> Web-to-Case and Web-to-Lead option are not available Metadata API​​​​​​​

**✅ Tại sao đáp án đúng:**
> Lead Conversion Settings và Case Settings là hàng chính hãng thuộc nhóm cấu hình hệ thống (Settings), được Metadata API hỗ trợ tận răng để deploy mượt mà qua các môi trường.

**❌ Tại sao đáp án sai:**
> **B.** Web-to-Case là tính năng/tiện ích chứ không phải Metadata Component đơn thuần, không deploy trực tiếp qua Metadata API được đâu nha.
> **C.** Web-to-Lead cũng chung số phận 'cook' với Web-to-Case, không nằm trong danh sách được Metadata API hỗ trợ.

**💡 Từ khóa ghi nhớ:** `Cứ thấy có đuôi 'Settings' là deploy được qua Metadata API, còn mấy cái 'Web-to-...' là cook chắc!`

---

## Câu 2

**🔵 A developer created a custom order management app that uses an Apex class. The order is represented by an Order object and an OrderItem object that has a master-detail relationship to Order. During order processing, an order may be split into multiple orders. What should a developer do to allow their code to move some existing OrderItem records to a new Order record?**

- **A.** Select the Allow reparenting option on the master-detail relationship. ✅
- **B.** Change the master-detail relationship to an external lookup relationship. ❌
- **C.** Add without sharing to the Apex class declaration. ❌
- **D.** Create a junction object between OrderItem and Order. ❌

**📝 Dịch tiếng Việt:**
> Một developer tạo một app quản lý đơn hàng tùy chỉnh dùng Apex class. Đơn hàng gồm object Order và object OrderItem có mối quan hệ master-detail với Order. Trong quá trình xử lý, một đơn hàng có thể bị chia làm nhiều đơn hàng nhỏ. Lập trình viên phải làm gì để cho phép code chuyển một số bản ghi OrderItem hiện có sang một bản ghi Order mới?

**💬 Giải thích gốc (English):**
> "Allow reparenting" the developer enables the ability to change the parent of a child record (OrderItem) from one master record (Order) to another. This allows the developer to move certain OrderItem records to a new Order record, effectively splitting the order into multiple orders.

**✅ Tại sao đáp án đúng:**
> Tích chọn 'Allow reparenting' trên mối quan hệ master-detail chính là chìa khóa vạn năng cho phép đổi cha (Order) của các bản ghi con (OrderItem) một cách hợp lệ mà không bị Salesforce cấm cản.

**❌ Tại sao đáp án sai:**
> **B.** Chuyển master-detail thành external lookup relationship là quả tự hủy đi các tính năng xịn sò của master-detail như cascade delete hay roll-up summary, quá cồng kềnh và mất chất.
> **C.** Thêm 'without sharing' chỉ là ngó lơ luật chia sẻ bản ghi (sharing rules) thôi, chứ không có tuổi can thiệp vào giới hạn đổi cha của master-detail nhé.
> **D.** Tạo junction object giữa OrderItem và Order là pha thiết kế đi vào lòng đất, làm phức tạp hóa mô hình dữ liệu không cần thiết.

**💡 Từ khóa ghi nhớ:** `Muốn đổi cha (reparent) trong quan hệ Master-Detail thì tích chọn ngay 'Allow reparenting'.`

---

## Câu 3

**🔵 A developer is implementing an Apex class for a financial system. Within the class, the variables 'creditAmount' and 'debitAmount' should not be able to change once a value is assigned. In which two ways can the developer declare the variables to ensure their value can only be assigned one time? (Choose two.)**

- **A.** Use the static keyword and assign its value in a static initializer. ❌
- **B.** Use the final keyword and assign its value when declaring the variable. ✅
- **C.** Use the final keyword and assign its value in the class constructor. ✅
- **D.** Use the static keyword and assign its value in the class constructor. ❌

**📝 Dịch tiếng Việt:**
> Trong một class Apex cho hệ thống tài chính, làm sao để đảm bảo các biến 'creditAmount' và 'debitAmount' chỉ được gán giá trị duy nhất một lần và không thể bị sửa đổi sau đó? (Chọn hai)

**💬 Giải thích gốc (English):**
> The variables 'creditAmount' and 'debitAmount' can only be assigned one time, the developer should use the 'final' keyword and assign their values when declaring the variables. This will make the variables constant and their values cannot be changed after assignment.

**✅ Tại sao đáp án đúng:**
> Từ khóa 'final' trong Apex dùng để tạo hằng số cho instance. Mày có thể gán giá trị ngay lúc khai báo (B) hoặc gán duy nhất 1 lần trong Constructor (C). Sau đó thì đố ai sửa được.

**❌ Tại sao đáp án sai:**
> **A.** Static initializer gán giá trị cho biến static, nhưng nếu không có 'final' thì vẫn bị ghi đè sau đó như thường.
> **D.** Static đơn thuần chỉ là biến dùng chung ở cấp class, không có 'final' thì vẫn bị sửa đổi dễ dàng, không đạt yêu cầu gán duy nhất một lần.

**💡 Từ khóa ghi nhớ:** `Gán duy nhất 1 lần (Read-only/Constant) = dùng FINAL.`

---

## Câu 4

**🔵 Which three web technologies can be integrated into a Visualforce page? (Choose three.)**

- **A.** JavaScript ✅
- **B.** CSS ✅
- **C.** Java ❌
- **D.** PHP ❌
- **E.** HTML ✅

**📝 Dịch tiếng Việt:**
> Ba công nghệ web nào sau đây có thể được tích hợp mượt mà vào một trang Visualforce? (Chọn ba.)

**💬 Giải thích gốc (English):**
> You can't write any Java/Php code in VF page.
> https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/pages_intro_what_is_it.htm

**✅ Tại sao đáp án đúng:**
> Visualforce là công nghệ render ở phía client-side (frontend), do đó nó hỗ trợ hoàn toàn các công nghệ web cơ bản gồm HTML (cấu trúc), CSS (giao diện đẹp mắt) và JavaScript (logic tương tác động).

**❌ Tại sao đáp án sai:**
> **C.** Java là ngôn ngữ chạy phía server-side, không thể nhúng chạy trực tiếp trong Visualforce page được đâu.
> **D.** PHP cũng chạy server-side và hoàn toàn không tương thích để chạy trực tiếp trong Visualforce page trên nền tảng Force.com.

**💡 Từ khóa ghi nhớ:** `Visualforce page chỉ chơi với bộ ba frontend (HTML, CSS, JS); Java và PHP cho ra rìa!`

---

## Câu 5

**🔵 Which is a valid Apex assignment?**

- **A.** Integer x=5*1.0; ❌
- **B.** Integer x =5.0; ❌
- **C.** Double x =5; ✅
- **D.** Float x =5.0; ❌

**📝 Dịch tiếng Việt:**
> Phép gán Apex nào sau đây là hoàn toàn hợp lệ mà không gây lỗi compile?

**💬 Giải thích gốc (English):**
> An Integer can be assigned to a Double, but a Double cannot be directly assigned to an Integer.

**✅ Tại sao đáp án đúng:**
> Apex hỗ trợ ngầm định chuyển đổi kiểu dữ liệu (implicit casting) từ Integer sang Double (Double x = 5) vì Double có độ rộng dữ liệu lớn hơn Integer, gán thoải mái không lo lỗi.

**❌ Tại sao đáp án sai:**
> **A.** Phép nhân 5 * 1.0 trả về kiểu Double, không thể gán trực tiếp cho biến kiểu Integer nếu không ép kiểu (cast) tường minh.
> **B.** 5.0 là giá trị kiểu Double, gán trực tiếp cho Integer là bị compiler đập ngay.
> **D.** Apex không có kiểu dữ liệu nguyên bản là Float, dùng kiểu này là compiler báo lỗi không nhận dạng được luôn.

**💡 Từ khóa ghi nhớ:** `Bé gán cho Lớn ok (Integer -> Double), chứ Lớn gán cho Bé (Double -> Integer) là cook!`

---

## Câu 6

**🔵 A developer completed modifications to a customized feature that is comprised of two elements: 1. Apex trigger 2. Trigger handler Apex class. What are two factors that the developer must take into account to properly deploy the modification to the production environment? (Choose two.)**

- **A.** Apex classes must have at least 75% code coverage org-wide. ✅
- **B.** At least one line of code must be executed for the Apex trigger. ✅
- **C.** All methods in the test classes must use @isTest. ❌
- **D.** Test methods must be declared with the testMethod keyword. ❌

**📝 Dịch tiếng Việt:**
> Một developer vừa sửa đổi một tính năng gồm Apex trigger và Trigger handler Apex class. Có hai yếu tố nào bắt buộc phải tuân thủ để deploy thành công lên môi trường production? (Chọn hai)

**💬 Giải thích gốc (English):**
> To deploy your code to production environments, it is mandatory to achieve a minimum of 75% code coverage for your Apex through unit tests. Additionally, all triggers must have at least one line of test coverage.

**✅ Tại sao đáp án đúng:**
> Khi deploy lên production, Salesforce kiểm duyệt cực gắt: tổng độ bao phủ code (code coverage) của toàn bộ Apex class trong org phải đạt ít nhất 75% (A), và mọi Apex trigger phải có ít nhất 1 dòng code chạy qua kiểm thử (B).

**❌ Tại sao đáp án sai:**
> **C.** Không phải tất cả phương thức trong test class đều phải dùng @isTest, chỉ cần các method test thực sự được đánh dấu đúng là được.
> **D.** Từ khóa 'testMethod' đã lỗi thời (deprecated), giờ dùng annotation @isTest là chuẩn bài.

**💡 Từ khóa ghi nhớ:** `Deploy Production: Code coverage org >= 75% + Trigger chạy qua ít nhất 1 dòng test.`

---

## Câu 7

**🔵 How many levels of child records can be returned in a single SOQL query from one parent object?**

- **A.** 1 ❌
- **B.** 3 ❌
- **C.** 5 ✅
- **D.** 7 ❌

**📝 Dịch tiếng Việt:**
> Một SOQL query từ một parent object có thể truy vấn sâu xuống tối đa bao nhiêu cấp độ của child record (quan hệ parent-to-child)?

**💬 Giải thích gốc (English):**
> Query Five Levels of Parent-to-Child Relationships in SOQL Queries
> https://help.salesforce.com/s/articleView?id=release-notes.rn_api_soql_5level.htm&release=244&type=5

**✅ Tại sao đáp án đúng:**
> Salesforce cho phép một SOQL query truy vấn tối đa 5 cấp độ mối quan hệ từ parent xuống child. Đây là giới hạn tối đa hiện tại giúp bạn lấy dữ liệu phân cấp sâu mà không cần viết nhiều query.

**❌ Tại sao đáp án sai:**
> **A.** 1 cấp độ là giới hạn quá xưa cũ và cực kỳ hạn chế.
> **B.** 3 cấp độ từng là giới hạn cũ của SOQL, giờ đã được nâng lên 5 cấp độ rồi nha.
> **D.** 7 cấp độ vượt quá giới hạn governor limit hiện tại mà Salesforce đặt ra cho truy vấn parent-to-child.

**💡 Từ khóa ghi nhớ:** `Truy vấn SOQL từ Cha xuống Con: Tối đa 5 cấp độ.`

---

## Câu 8

**🔵 When an Account's custom picklist field called Customer Sentiment is changed to a value of 'Confused', a new related Case should automatically be created. Which two methods should a developer use to create this case? (Choose two.)**

- **A.** Process Builder ✅
- **B.** Apex Trigger ✅
- **C.** Custom Button ❌
- **D.** Workflow Rule ❌

**📝 Dịch tiếng Việt:**
> Khi trường picklist tùy chỉnh Customer Sentiment trên Account bị đổi thành 'Confused', một Case liên quan mới phải tự động được tạo. Lập trình viên nên dùng 2 phương pháp nào sau đây? (Chọn hai)

**💬 Giải thích gốc (English):**
> 1. Apex Trigger: The developer can write an Apex trigger on the Account object to detect changes in the Customer Sentiment picklist field. When the picklist field value changes to 'Confused,' the trigger can create a new Case record and establish the necessary relationship between the Account and the Case.
> 2. Process Builder: The developer can use Process Builder, a declarative automation tool in Salesforce, to create the automation flow. The process builder can be configured to monitor changes on the Account object and specifically check for the Customer Sentiment picklist field value change to 'Confused.' When the condition is met, the process builder can take action to create a new related Case record.

**✅ Tại sao đáp án đúng:**
> Apex Trigger là giải pháp code (programmatic) mạnh mẽ giúp xử lý mọi sự kiện DML trên Account để tạo Case mới. Process Builder là công cụ no-code/low-code giúp tự động tạo bản ghi liên quan khi có update. (Lưu ý: Thời điểm hiện tại 2026, Process Builder đã bị deprecated và nhường ngôi vị độc tôn cho Record-Triggered Flow, nhưng trong bài thi vẫn chọn Process Builder nhé).

**❌ Tại sao đáp án sai:**
> **C.** Custom Button yêu cầu người dùng phải click bằng cơm mới chạy, không đáp ứng được yêu cầu 'tự động'.
> **D.** Workflow Rule cực kỳ cùi bắp, chỉ có thể cập nhật trường hoặc gửi email/task chứ không có khả năng tạo bản ghi mới.

**💡 Từ khóa ghi nhớ:** `Tự động tạo bản ghi mới khi cập nhật: Chọn Trigger (code) hoặc Process Builder / Flow (no-code).`

---

## Câu 9

**🔵 Which statement results in an Apex compiler error?**

- **A.** Map<Id, Lead> lmap = new Map<Id, Lead>([Select ID from Lead Limit 8]); ❌
- **B.** Date d1 = Date.Today(), d2 = Date.ValueOf('2018-01-01'); ❌
- **C.** Integer a=5, b=6, c, d = 7; ❌
- **D.** List<string> s = List<string>{'a','b','c'}; ✅

**📝 Dịch tiếng Việt:**
> Câu lệnh nào sau đây sẽ bị lỗi trình biên dịch (compiler error) Apex?

**💬 Giải thích gốc (English):**
> D is not correct because of the missing new operator
> List<string> s = new List<string>{'a','b','c'};

**✅ Tại sao đáp án đúng:**
> Câu lệnh `List<string> s = List<string>{'a','b','c'};` thiếu từ khóa `new` khi khởi tạo một List. Trong Apex, khởi tạo collection bắt buộc phải có `new`, thiếu là compiler đập ngay.

**❌ Tại sao đáp án sai:**
> **A.** Khởi tạo Map bằng kết quả SOQL là hoàn toàn hợp lệ, Apex tự động lấy Id làm key và sObject làm value.
> **B.** Khai báo nhiều biến kiểu Date trên một dòng và gán giá trị hợp lệ là đúng cú pháp.
> **C.** Khai báo nhiều biến Integer trên một dòng, biến `c` không khởi tạo giá trị vẫn hoàn toàn hợp lệ.

**💡 Từ khóa ghi nhớ:** `Khởi tạo Collection (List, Set, Map) trong Apex mà thiếu từ khóa `new` là cook ngay lập tức!`

---

## Câu 10

**🔵 A developer has a Visualforce page and custom controller to save Account records. The developer wants to display any validation rule violations to the user. How can the developer make sure that validation rule violations are displayed?**

- **A.** Add custom controller attributes to display the message. ❌
- **B.** Use a try/catch with a custom exception class. ❌
- **C.** Include<apex:messages>on the Visualforce page. ✅
- **D.** Perform the DML using the Database.upsert() method. ❌

**📝 Dịch tiếng Việt:**
> Một developer có Visualforce page và custom controller để lưu Account. Developer muốn hiển thị bất kỳ vi phạm validation rule nào cho người dùng. Làm thế nào để đảm bảo điều đó?

**💬 Giải thích gốc (English):**
> Display Errors on the Visualforce Page: In the Visualforce page, utilize the Visualforce markup and Apex expressions to iterate over the error messages collection and display them to the user. This can be achieved using components like <apex:pageMessages> or by manually rendering error messages using <apex:outputPanel> and <apex:repeat>.

**✅ Tại sao đáp án đúng:**
> Component `<apex:messages>` (hoặc `<apex:pageMessages>`) trên Visualforce page được sinh ra để tự động bắt và hiển thị tất cả các lỗi DML hoặc vi phạm validation rule từ controller lên giao diện mà không cần code xử lý lỗi phức tạp.

**❌ Tại sao đáp án sai:**
> **A.** Tự viết custom controller attributes để hiển thị lỗi là tự làm khó mình, cồng kềnh không cần thiết.
> **B.** Dùng try/catch với custom exception không tự động hiển thị lỗi lên giao diện Visualforce nếu không có component chuyên dụng.
> **D.** Database.upsert() chỉ là phương thức thực hiện DML, không giải quyết việc hiển thị lỗi trên giao diện người dùng.

**💡 Từ khóa ghi nhớ:** `Visualforce muốn hiện validation lỗi: Thêm `<apex:messages>` lên trang là xong!`

---

## Câu 11

**🔵 A developer encounters APEX heap limit errors in a trigger. Which two methods should the developer use to avoid this error? (Choose two.)**

- **A.** Use the transient keyword when declaring variables. ❌
- **B.** Query and store fields from the related object in a collection when updating related objects. ❌
- **C.** Remove or set collections to null after use. ✅
- **D.** Use SOQL for loops instead of assigning large queries results to a single collection and looping through the collection. ✅

**📝 Dịch tiếng Việt:**
> Một developer gặp lỗi APEX heap limit (tràn bộ nhớ) trong trigger. Hai phương pháp nào sau đây giúp tránh lỗi này? (Chọn hai)

**💬 Giải thích gốc (English):**
> Use the transient keyword to declare instance variables that can't be saved, and shouldn't be transmitted as part of the view state for a Visualforce page -> For VF 'heap' limit.
> Reduce heap size during runtime by removing items from the collection as you iterate over it.
> To avoid heap size limits, developers should always use a SOQL "for" loop to process query results that return many records.

**✅ Tại sao đáp án đúng:**
> Đặt các collection thành null sau khi dùng (C) giúp garbage collector giải phóng bộ nhớ ngay lập tức. Sử dụng SOQL for loops (D) giúp xử lý các bản ghi theo từng batch nhỏ thay vì tải toàn bộ danh sách khổng lồ vào bộ nhớ cùng lúc.

**❌ Tại sao đáp án sai:**
> **A.** Transient dùng để giảm kích thước view state trong Visualforce, hoàn toàn vô dụng trong việc giải quyết heap limit của trigger.
> **B.** Query và nhét đống trường liên quan vào collection chỉ làm tăng thêm dung lượng bộ nhớ sử dụng, dễ gây tràn heap hơn.

**💡 Từ khóa ghi nhớ:** `Tránh Heap Limit: Giải phóng collection (= null) và dùng SOQL For Loop để duyệt.`

---

## Câu 12

**🔵 Which two are phases in the Salesforce Application Event propagation framework? (Choose two.)**

- **A.** Bubble ✅
- **B.** Default ✅
- **C.** Control ❌
- **D.** Emit ❌

**📝 Dịch tiếng Việt:**
> Hai giai đoạn nào nằm trong khung lan truyền Aura Application Event của Salesforce? (Chọn hai.)

**💬 Giải thích gốc (English):**
> Here is the sequence of application event propagation.
> 1. Event fired—An application event is fired. The component that fires the event is known as the source component.
> 2. Capture phase—The framework executes the capture phase from the application root to the source component until all components are traversed. Any handling event can stop propagation by calling stopPropagation() on the event.
> 3. Bubble phase—The framework executes the bubble phase from the source component to the application root until all components are traversed or stopPropagation() is called.
> 4. Default phase—The framework executes the default phase from the root node unless preventDefault() was called in the capture or bubble phases. If the event’s propagation wasn’t stopped in a previous phase, the root node defaults to the application root. If the event’s propagation was stopped in a previous phase, the root node is set to the component whose handler invoked event.stopPropagation().

**✅ Tại sao đáp án đúng:**
> Aura Application Event có cơ chế lan truyền qua 3 giai đoạn: Capture, Bubble (A - lan truyền từ con lên cha) và Default (B - chạy các handler đã đăng ký).

**❌ Tại sao đáp án sai:**
> **C.** Control không phải là một giai đoạn trong vòng đời lan truyền event của Aura.
> **D.** Emit là thuật ngữ của các framework JS khác như Vue/Aura Component không dùng khái niệm này cho giai đoạn lan truyền.

**💡 Từ khóa ghi nhớ:** `Event lan truyền trong Aura chỉ có: Capture -> Bubble -> Default.`

---

## Câu 13

**🔵 A custom object Trainer__c has a lookup field to another custom object Gym__c. Which SOQL query will get the record for the Viridian City Gym and all its trainers?**

- **A.** SELECT ID FROM Trainer__c WHERE Gym__r.Name = 'Viridian City Gym' ❌
- **B.** SELECT Id, (SELECT Id FROM Trainers__c) FROM Gym__c WHERE Name = 'Viridian City Gym' ❌
- **C.** SELECT Id, (SELECT Id FROM Trainer__c) FROM Gym__c WHERE Name = 'Viridian City Gym' ❌
- **D.** SELECT Id, (SELECT Id FROM Trainers__r) FROM Gym__c WHERE Name = 'Viridian City Gym' ✅

**📝 Dịch tiếng Việt:**
> Custom object Trainer__c có lookup field tới Gym__c. Câu query SOQL nào lấy được bản ghi Gym tên 'Viridian City Gym' và toàn bộ Trainer liên quan của nó?

**✅ Tại sao đáp án đúng:**
> Đây là truy vấn từ Cha xuống Con (Parent-to-Child). Với custom object, trong sub-query bắt buộc phải dùng tên mối quan hệ con (Child Relationship Name) thêm hậu tố `__r`. Do đó `Trainers__r` (D) là chuẩn bài.

**❌ Tại sao đáp án sai:**
> **A.** Câu này chỉ query trên Trainer chứ không lấy được thông tin chi tiết của Gym làm gốc.
> **B.** Dùng `Trainers__c` trong sub-query là sai cú pháp vì `__c` chỉ dùng cho tên Object, không dùng cho Relationship Name.
> **C.** Dùng `Trainer__c` vừa sai tên mối quan hệ (thiếu số nhiều 's') vừa dùng sai hậu tố `__c`.

**💡 Từ khóa ghi nhớ:** `Query Cha xuống Con: Sub-query bắt buộc dùng Relationship Name + `__r`.`

---

## Câu 14

**🔵 A developer needs to create an audit trail for records that are sent to the recycle bin. Which type of trigger is most appropriate to create?**

- **A.** after delete ✅
- **B.** after undelete ❌
- **C.** before undelete ❌
- **D.** before delete ❌

**📝 Dịch tiếng Việt:**
> Một developer cần tạo một audit trail (nhật ký lịch sử) cho các bản ghi bị xóa và đưa vào thùng rác (recycle bin). Loại trigger nào là phù hợp nhất?

**✅ Tại sao đáp án đúng:**
> Trigger `after delete` chạy sau khi bản ghi đã thực sự bị xóa thành công và chuyển vào recycle bin. Đây là thời điểm hoàn hảo để lấy các thông tin cuối cùng của bản ghi để ghi nhật ký audit trail.

**❌ Tại sao đáp án sai:**
> **B.** `after undelete` kích hoạt khi bản ghi được khôi phục từ thùng rác chứ không phải khi bị xóa đi.
> **C.** `before undelete` kích hoạt trước khi khôi phục bản ghi, không liên quan đến hành vi xóa.
> **D.** `before delete` chạy trước khi xóa, lúc này chưa chắc bản ghi đã được xóa thành công (có thể bị chặn bởi logic khác), ghi audit trail lúc này là vội vàng.

**💡 Từ khóa ghi nhớ:** `Nhật ký xóa (Recycle Bin) -> Chắc chắn đã xóa -> Dùng `after delete`.`

---

## Câu 15

**🔵 Where are two locations a developer can look to find information about the status of asynchronous or future calls? (Choose two.)**

- **A.** Time-Based Workflow Monitor ❌
- **B.** Apex Flex Queue ✅
- **C.** Apex Jobs ✅
- **D.** Paused Flow Interviews component ❌

**📝 Dịch tiếng Việt:**
> Hai vị trí nào lập trình viên có thể kiểm tra để tìm thông tin về trạng thái của các tiến trình không đồng bộ (asynchronous hoặc future calls)? (Chọn hai)

**💬 Giải thích gốc (English):**
> AsyncApexJob Object: The AsyncApexJob object represents the status of asynchronous Apex jobs, which include future calls, batch Apex jobs, and scheduled Apex jobs.
> Apex Flex Queue is where a developer can find information about the status of asynchronous or future calls in Salesforce. The Apex Flex Queue is a mechanism introduced to manage the execution of asynchronous Apex jobs when there is a large backlog.

**✅ Tại sao đáp án đúng:**
> Apex Jobs (C) hiển thị danh sách và trạng thái của tất cả các async jobs. Apex Flex Queue (B) hiển thị các Batch jobs đang xếp hàng chờ để được xử lý.

**❌ Tại sao đáp án sai:**
> **A.** Time-Based Workflow Monitor chỉ dùng để theo dõi các action hẹn giờ của Workflow Rules cổ xưa.
> **D.** Paused Flow Interviews chỉ hiển thị các Flow đang bị tạm dừng giữa chừng, không liên quan đến Apex async.

**💡 Từ khóa ghi nhớ:** `Check trạng thái Async Apex -> Vào Apex Jobs & Apex Flex Queue.`

---

## Câu 16

**🔵 Given the code below:
public class AccountListController {
public List<Account> getAccounts() {
return controller.getRecords();
}
}
which three statements can be used to create the controller variable? (Choose three.)**

- **A.** ApexPages.StandardsetController controller = new Apexpages.StandardsetController(Database.query('SELECT Id FROM Account')); ✅
- **B.** ApexPages.StandardsetController controller = new Apexpages.StandardsetController(Database.getQueryLocator('SELECT Id FROM Account')); ✅
- **C.** ApexPages.StandardController controller = new Apexpages.StandardController(Database.getQueryLocator('SELECT Id FROM Account')); ❌
- **D.** ApexPages.StandardController controller = new Apexpages.StandardController([SELECT Id FROM Account]); ❌
- **E.** ApexPages.StandardsetController controller = new Apexpages.StandardsetController(Database.getQueryLocator([SELECT Id FROM Account]); ✅

**📝 Dịch tiếng Việt:**
> Cho đoạn mã khai báo class `AccountListController` sử dụng `controller.getRecords()`. Ba câu lệnh nào có thể dùng để khởi tạo biến `controller` hợp lệ? (Chọn ba.)

**💬 Giải thích gốc (English):**
> The StandardController has getRecord() not getRecords().

**✅ Tại sao đáp án đúng:**
> Phương thức `getRecords()` (số nhiều) chỉ có trên `StandardSetController`. Bộ khởi tạo của nó chấp nhận danh sách sObject từ `Database.query()` (A) hoặc một `QueryLocator` từ `Database.getQueryLocator()` (B, E).

**❌ Tại sao đáp án sai:**
> **C.** StandardController chỉ có phương thức `getRecord()` (số ít) và không chấp nhận QueryLocator trong constructor.
> **D.** StandardController không có phương thức `getRecords()`, truyền một danh sách bản ghi vào constructor của nó là lỗi ngay.

**💡 Từ khóa ghi nhớ:** `getRecords() (số nhiều) = StandardSetController. Chấp nhận List sObject hoặc QueryLocator.`

---

## Câu 17

**🔵 Given: Map<ID, Account> accountMap = new Map<ID, Account> ([SELECT Id, Name FROM Account]); What are three valid Apex loop structures for iterating through items in the collection? (Choose three.)**

- **A.** for (ID accountID : accountMap.keySet()) { } ✅
- **B.** for (Account accountRecord : accountMap.values()) { } ✅
- **C.** for (Integer i = 0; i < accountMap.size(); i++) { } ✅
- **D.** for (ID accountID : accountMap) { } ❌
- **E.** for (Account accountRecord : accountMap.keySet()) { } ❌

**📝 Dịch tiếng Việt:**
> Cho khai báo Map<ID, Account> accountMap. Ba cấu trúc vòng lặp Apex nào sau đây là hợp lệ để duyệt qua collection này? (Chọn ba.)

**💬 Giải thích gốc (English):**
> Problem:
> D: Loop must iterate over collection: Map<Id,Account>
> E: Invalid loop variable type expected Id was Account.

**✅ Tại sao đáp án đúng:**
> Duyệt qua Set các ID bằng `keySet()` (A). Duyệt qua danh sách các Account bằng `values()` (B). Duyệt bằng vòng lặp `for` cổ điển dùng index chạy từ 0 đến `size()` của Map (C). Cả 3 đều chạy mượt mà.

**❌ Tại sao đáp án sai:**
> **D.** Apex cấm duyệt trực tiếp trên đối tượng Map (`for (ID accountID : accountMap)` là lỗi cú pháp).
> **E.** `keySet()` trả về Set kiểu ID, nhưng biến chạy lại khai báo kiểu `Account` là râu ông nọ cắm cằm bà kia, compiler báo lỗi ngay.

**💡 Từ khóa ghi nhớ:** `Duyệt Map: keySet() cho ID, values() cho sObject, cấm duyệt trực tiếp Map!`

---

## Câu 18

**🔵 What is the order of operations when a record is saved in Salesforce?**

- **A.** workflow, process flows, triggers, commit ❌
- **B.** process flows, triggers, workflow, commit ❌
- **C.** triggers, workflow, process flows, commit ✅
- **D.** workflow, triggers, process flows, commit ❌

**📝 Dịch tiếng Việt:**
> Thứ tự thực thi (Order of Operations) khi một bản ghi được lưu (save) trong Salesforce là gì?

**💬 Giải thích gốc (English):**
> When a record is saved in Salesforce, the following order of operations occurs:
> 1. Validation Rules: Salesforce first checks the validation rules defined on the object to ensure that the record meets all specified criteria. If any validation rule is violated, the record will not be saved, and an error message will be displayed to the user.
> 2. Before Triggers: Before the record is saved to the database, any "Before" triggers defined on the object are executed. These triggers can perform additional data manipulation, make API calls, or update related records.
> 3. System Validation: Salesforce performs system-level validation checks, such as verifying whether all required fields have been populated, field format validation, and user permissions to perform the operation.
> 4. Duplicate Rules: If duplicate rules are enabled for the object, Salesforce checks for any duplicate records based on the configured criteria. If a duplicate is found and the rule is set to block duplicates, the record won't be saved.
> 5. Before Save Updates: Any updates made to the record within the "Before" triggers are saved to the database.
> 6. Assignment Rules (Lead and Case objects): For Lead and Case objects, Salesforce applies assignment rules to determine ownership or assignment to queues.
> 7. Auto-Response Rules (Case object): For the Case object, Salesforce applies auto-response rules to determine if an automatic email response should be sent based on predefined criteria.
> 8. Workflow Rules: Salesforce evaluates the object's workflow rules to execute actions such as field updates, email alerts, tasks, or outbound messages based on specified conditions.
> 9. Processes (Process Builder or Visual Workflow): Any defined processes in Process Builder or Visual Workflow are executed, performing additional actions or updates based on specified criteria.
> 10. After Triggers: After the record is saved to the database, any "After" triggers defined on the object are executed. These triggers can perform additional operations or updates based on the saved record or related records.
> 11. Assignment Rules (Non-Lead and Non-Case objects): For non-Lead and non-Case objects, Salesforce applies assignment rules to determine ownership or assignment to queues.
> 12. Auto-Response Rules (Non-Case objects): For non-Case objects, Salesforce applies auto-response rules to determine if an automatic email response should be sent based on predefined criteria.
> 13. Post-Commit Logic: Any logic that needs to be executed after the record is saved and committed to the database is processed. This includes sending emails, making additional API calls, or performing other actions.

**✅ Tại sao đáp án đúng:**
> Quy trình chuẩn chỉnh của Salesforce khi lưu bản ghi: Các Triggers (before/after) sẽ nổ súng trước để xử lý logic, sau đó đến lượt Workflow Rules quét qua, tiếp theo là Process Flows (Flow/Process Builder) chạy các tự động hóa, và cuối cùng mới commit ghi dữ liệu vào database.

**❌ Tại sao đáp án sai:**
> **A.** Workflow Rules không thể chạy trước Triggers được, thế là đi ngược quy trình.
> **B.** Process flows và Workflow Rules xếp hàng chạy trước Triggers là sai bét quy chuẩn.
> **D.** Workflow Rules chạy trước Triggers là hoàn toàn không chính xác.

**💡 Từ khóa ghi nhớ:** `Trật tự thực thi cốt lõi: Triggers -> Workflow Rules -> Process Flows -> Commit.`

---

## Câu 19

**🔵 Which three options can be accomplished with formula fields? (Choose three.)**

- **A.** Generate a link using the HYPERLINK function to a specific record. ✅
- **B.** Display the previous value for a field using the PRIORVALUE function. ❌
- **C.** Determine if a datetime field value has passed using the NOW function. ✅
- **D.** Return and display a field value from another object using the VLOOKUP function. ❌
- **E.** Determine which of three different images to display using the IF function. ✅

**📝 Dịch tiếng Việt:**
> Ba tùy chọn nào sau đây có thể được thực hiện bằng formula fields? (Chọn ba.)

**✅ Tại sao đáp án đúng:**
> Formula fields hỗ trợ hàm `HYPERLINK` để tạo link động đến bản ghi (A), hàm `NOW` để so sánh và kiểm tra thời gian đã qua (C), và hàm `IF` kết hợp `IMAGE` để hiển thị hình ảnh động theo điều kiện (E).

**❌ Tại sao đáp án sai:**
> **B.** Hàm `PRIORVALUE` chỉ dùng được trong validation rules hoặc workflow/flow, cấm dùng trong formula fields.
> **D.** Formula field trong Salesforce không hỗ trợ hàm `VLOOKUP` để tìm kiếm dữ liệu chéo giữa các object không liên quan trực tiếp.

**💡 Từ khóa ghi nhớ:** `Formula field ngon nghẻ: HYPERLINK, NOW, IF. Không chơi với PRIORVALUE và VLOOKUP!`

---

## Câu 20

**🔵 A developer is tasked to perform a security review of the ContactSearch Apex class that exists in the system. Within the class, the developer identifies the following method as a security threat:
List<Contact> performSearch(String lastName) {
return Database.query('SELECT Id, FirstName, LastName FROM Contact WHERE Lastname like %'+lastName+'%');
}
What are two ways the developer can update the method to prevent a SOQL injection attack? (Choose two.)**

- **A.** Use the @ReadOnly annotation and the with sharing keyword on the class. ❌
- **B.** Use the escapeSingleQuotes method to sanitize the parameter before its use. ✅
- **C.** Use a regular expression expression on the parameter to remove special characters. ❌
- **D.** Use variable binding and replace the dynamic query with a static SOQL. ✅

**📝 Dịch tiếng Việt:**
> Để ngăn chặn tấn công SOQL Injection cho phương thức query động `Database.query('... WHERE Lastname like %'+lastName+'%')`, hai cách nào sau đây là tối ưu nhất? (Chọn hai)

**✅ Tại sao đáp án đúng:**
> Sử dụng `escapeSingleQuotes()` (B) giúp vô hiệu hóa mọi ký tự nháy đơn nguy hiểm trong tham số truyền vào. Sử dụng variable binding (D) chuyển query động thành static SOQL giúp Salesforce tự động dọn dẹp và bảo vệ truy vấn an toàn tuyệt đối.

**❌ Tại sao đáp án sai:**
> **A.** Quyền chia sẻ class `with sharing` hay `@ReadOnly` chỉ giới hạn truy cập dữ liệu và tăng hiệu suất, không có tính năng chống SOQL Injection.
> **C.** Tự viết Regex để lọc ký tự đặc biệt vừa cồng kềnh vừa dễ sót lỗ hổng bảo mật, không an toàn bằng hàm chuẩn của Salesforce.

**💡 Từ khóa ghi nhớ:** `Chống SOQL Injection: Dùng escapeSingleQuotes hoặc Variable Binding (:var).`

---

## Câu 21

**🔵 A developer writes the following code:
List<Account> acc = [Select Id From Account Limit 10];
Delete acc;
Database.emptyRecyclebin(acc);
System.Debug(Limits.getDMLStatements() +', ' + Limits.getLimitDMLStatements());
What is the result of the debug statement?**

- **A.** 1, 100 ❌
- **B.** 1, 150 ❌
- **C.** 2, 150 ✅
- **D.** 2, 200 ❌

**📝 Dịch tiếng Việt:**
> Một developer chạy đoạn code xóa và dọn thùng rác Account, sau đó in debug statements hiển thị số lượng DML đã dùng và giới hạn DML. Kết quả in ra là gì?

**💬 Giải thích gốc (English):**
> getDMLStatements() Returns the number of DML statements (such as insert, update or the database.EmptyRecycleBin method) that have been called.
> getLimitDMLStatements() Returns the total number of DML statements or the database.EmptyRecycleBin methods that can be called.

**✅ Tại sao đáp án đúng:**
> Cả hai lệnh `Delete` và `Database.emptyRecyclebin()` đều tiêu tốn 1 câu lệnh DML riêng biệt, tổng cộng là 2 DML. Giới hạn số câu lệnh DML tối đa cho một transaction đồng bộ trong Salesforce là 150. Kết quả in ra là `2, 150`.

**❌ Tại sao đáp án sai:**
> **A.** Tính sai số câu lệnh DML và sai giới hạn tối đa.
> **B.** Số câu lệnh DML bị tính thiếu (Database.emptyRecyclebin vẫn ngốn 1 DML statement).
> **D.** Giới hạn DML tối đa của transaction đồng bộ là 150 chứ không phải 200.

**💡 Từ khóa ghi nhớ:** `DML Limit = 150. Xóa (Delete) và Dọn rác (emptyRecyclebin) ngốn tổng 2 DML.`

---

## Câu 22

**🔵 Which approach should a developer take to automatically add a 'Maintenance Plan' to each Opportunity that includes an 'Annual Subscription' when an opportunity is closed?**

- **A.** Build a OpportunityLineItem trigger that adds a PriceBookEntry record. ❌
- **B.** Build an OpportunityLineItem trigger to add an OpportunityLineItem record. ❌
- **C.** Build an Opportunity trigger that adds a PriceBookEntry record. ❌
- **D.** Build an Opportunity trigger that adds an OpportunityLineItem record. ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên nên dùng cách nào để tự động thêm một 'Maintenance Plan' (Sản phẩm) vào mỗi Opportunity có chứa 'Annual Subscription' khi Opportunity đó được đóng?

**💬 Giải thích gốc (English):**
> Write an Apex trigger on the Opportunity object that fires when an Opportunity is closed.

**✅ Tại sao đáp án đúng:**
> Sự kiện kích hoạt khi Opportunity bị đóng, do đó trigger phải nằm trên Opportunity. Vì sản phẩm của Opportunity được đại diện bởi object OpportunityLineItem, trigger này sẽ chèn một bản ghi OpportunityLineItem mới (D).

**❌ Tại sao đáp án sai:**
> **A.** Trigger trên con (OpportunityLineItem) không thể tự bắt được sự kiện đóng ở cha (Opportunity) một cách hợp lý.
> **B.** Viết trigger trên con để chèn chính nó khi cha thay đổi trạng thái là đi sai luồng thiết kế.
> **C.** PriceBookEntry chỉ định nghĩa đơn giá sản phẩm trong bảng giá, không phải sản phẩm được thêm vào Opportunity cụ thể.

**💡 Từ khóa ghi nhớ:** `Sự kiện xảy ra ở đâu -> Trigger ở đó. Đóng Opportunity -> Trigger trên Opportunity chèn OpportunityLineItem.`

---

## Câu 23

**🔵 Which action may cause triggers to fire?**

- **A.** Renaming or replacing a picklist entry ❌
- **B.** Updates to Feed Items ✅
- **C.** Cascading delete operations ❌
- **D.** Changing a user's default division when the transfer division option is checked ❌

**📝 Dịch tiếng Việt:**
> Hành động nào sau đây có thể khiến cho các trigger trong hệ thống bị kích hoạt?

**💬 Giải thích gốc (English):**
> Record Update: When an existing record is updated, triggers associated with the object can fire. This includes both before and after update triggers.

**✅ Tại sao đáp án đúng:**
> FeedItem là một sObject đại diện cho bài viết Chatter. Khi có bất kỳ cập nhật nào trên bài viết (Feed Items), trigger trên FeedItem sẽ được kích hoạt hoạt động bình thường.

**❌ Tại sao đáp án sai:**
> **A.** Đổi tên hoặc thay thế một giá trị picklist trong Setup chỉ là thao tác cấu hình, không kích hoạt trigger của bản ghi.
> **C.** Xóa bắc cầu (Cascading delete - ví dụ cha bị xóa kéo theo con bị xóa) mặc định không làm nổ trigger trên bản ghi con.
> **D.** Thay đổi Division mặc định của user là hành động quản trị hệ thống, không kích hoạt trigger DML dữ liệu.

**💡 Từ khóa ghi nhớ:** `Cứ có thao tác dữ liệu (Insert/Update/Delete) trên sObject là Trigger nổ. FeedItem cũng là sObject!`

---

## Câu 24

**🔵 Management asked for opportunities to be automatically created for accounts with annual revenue greater than $1,000,000. A developer created the following trigger on the Account object to satisfy this requirement.
for(Account a: trigger.new){
if(a.AnnuaIRevenue > 1000000){
List<Opportunity> oppList = [SELECT Id FROM Opportunity WHERE accountId = :a.Id];
if(oppList.size() == 0){
Opportunity oppty = new Opportunity (
Name = a.name,
StageName = 'Prospecting',
CloseDate = system.today().addays(30));
insert oppty;
}
}
}
Users are able to update the account records via the UI and can see an opportunity created for high annual revenue accounts. However, when the administrator tries to upload a list of 179 accounts using Data Loader, it fails with System.Exception errors.
Which two actions should the developer take to fix the code segment shown above? (Choose two.)**

- **A.** Check if all the required fields for Opportunity are being added on creation. ❌
- **B.** Use Database.query to query the opportunities. ❌
- **C.** Move the DML that saves opportunities outside the for loop. ✅
- **D.** Query for existing opportunities outside the for loop. ✅

**📝 Dịch tiếng Việt:**
> Một trigger tự động tạo Opportunity cho Account có doanh thu lớn hơn 1 triệu USD bị lỗi System.Exception khi admin load 179 Account bằng Data Loader. Lập trình viên cần làm gì để sửa lỗi này? (Chọn hai)

**💬 Giải thích gốc (English):**
> The two actions the developer should take to fix the code segment are:
> 1. Move the DML that saves opportunities outside of the for loop.
> 2. Query for existing opportunities outside of the for loop.

**✅ Tại sao đáp án đúng:**
> 179 bản ghi vượt quá giới hạn 100 SOQL query trong một transaction. Cần phải đưa câu query SOQL ra ngoài vòng lặp (D) và chuyển câu lệnh chèn DML `insert` ra ngoài vòng lặp `for` (C) để gom dữ liệu xử lý hàng loạt (Bulkification).

**❌ Tại sao đáp án sai:**
> **A.** Lỗi ở đây là đụng trần Governor Limit do viết code không tối ưu, không phải do thiếu trường bắt buộc của Opportunity.
> **B.** Sử dụng `Database.query` động vẫn tốn số lượng SOQL query y hệt, không giải quyết được gốc rễ vấn đề.

**💡 Từ khóa ghi nhớ:** `Bulkification: Tuyệt đối không để SOQL query hoặc câu lệnh DML (insert, update...) bên trong vòng lặp FOR!`

---

## Câu 25

**🔵 An org has a data model with a Buyer__c object that has a lookup relationship to Region__c and a Supplier__c object has a lookup relationship to Region___c. How can a developer display data from the related Supplier__c records on a Visualforce page that has a standard controller for the Buyer__c object?**

- **A.** Use rollup formula fields on the Buyer__c object to reference the related Supplier__c records through the Region__c. ❌
- **B.** Use SOQL in a controller extension to query for related Supplier__c records. ✅
- **C.** Use a second standard controller for the Region__c object on a page to display the related Supplier__c records. ❌
- **D.** Use merge field syntax to retrieve the Supplier__c records related to the Buyer__c record through the Region__c. ❌

**📝 Dịch tiếng Việt:**
> Object Buyer__c có lookup với Region__c, Supplier__c cũng có lookup với Region__c. Làm thế nào để hiển thị dữ liệu từ các bản ghi Supplier__c liên quan trên trang Visualforce có standard controller của Buyer__c?

**💬 Giải thích gốc (English):**
> 1. Create a Custom Controller Extension: Create a custom Apex controller extension for the Visualforce page. The controller extension allows you to add custom logic to the standard controller's functionality.
> 2. Query Related Supplier__c Records: In the custom controller extension, use a SOQL query to retrieve the Supplier__c records related to the Buyer__c record being displayed on the Visualforce page. This can be achieved by using the Buyer__c object's lookup relationship field (e.g., Region__c) to traverse to the related Supplier__c records.

**✅ Tại sao đáp án đúng:**
> Buyer__c và Supplier__c không có quan hệ trực tiếp mà chỉ kết nối gián tiếp qua Region__c. Standard controller của Buyer không thể tự đi vòng để lấy dữ liệu. Lập trình viên bắt buộc phải dùng Controller Extension viết SOQL truy vấn danh sách Supplier liên quan dựa trên Region ID (B).

**❌ Tại sao đáp án sai:**
> **A.** Roll-up summary chỉ hoạt động trên quan hệ Master-Detail, quan hệ Lookup ở đây là vô dụng.
> **C.** Salesforce cấm khai báo hai Standard Controller đồng thời trên cùng một trang Visualforce.
> **D.** Merge field syntax chỉ có thể truy xuất dữ liệu từ con lên cha trực tiếp, không thể đi vòng từ Buyer lên Region rồi vòng xuống Supplier.

**💡 Từ khóa ghi nhớ:** `Không có quan hệ trực tiếp (bắc cầu qua trung gian) -> Bắt buộc dùng Controller Extension viết SOQL query.`

---

## Câu 26

**🔵 A developer is asked to create a custom Visualforce page that will be used as a dashboard component. Which three are valid controller options for this page? (Choose three.)**

- **A.** Use a standard controller. ❌
- **B.** Use a standard controller with extensions. ❌
- **C.** Use a custom controller with extensions. ✅
- **D.** Do not specify a controller. ✅
- **E.** Use a custom controller. ✅

**📝 Dịch tiếng Việt:**
> Một developer được yêu cầu tạo một trang Visualforce tùy chỉnh để dùng làm dashboard component. Ba tùy chọn controller nào sau đây là hợp lệ cho trang này? (Chọn ba.)

**✅ Tại sao đáp án đúng:**
> Trang Visualforce dùng làm dashboard component không được phép dùng Standard Controller độc lập vì dashboard cần hiển thị dữ liệu tổng hợp đa dạng. Các tùy chọn hợp lệ là dùng Custom Controller kết hợp Extensions (C), không khai báo controller nào (D), hoặc dùng Custom Controller đơn lẻ (E).

**❌ Tại sao đáp án sai:**
> **A.** Dùng Standard Controller thuần túy sẽ trói buộc trang vào ngữ cảnh của một bản ghi đơn lẻ, không thể làm dashboard component.
> **B.** Dùng Standard Controller kèm Extension vẫn bị giới hạn bởi record context, không dùng làm dashboard được.

**💡 Từ khóa ghi nhớ:** `Làm Dashboard Component: Tuyệt đối KHÔNG dùng Standard Controller!`

---

## Câu 27

**🔵 Universal Hiring is using Salesforce to capture job applications. A salesforce administrator created two custom objects: Job__c acting as the master object, Job_Application__c acting as the detail. Within the Job__c object, a custom multi-select picklist, Preferred_Locations__c, contains a list of approved states for the position. Each Job_Application__c record relates to a Contact within the system through a master-detail relationship. 	Recruiters have requested the ability to view whether the Contact's Mailing State value matches a value selected on the Preferred_Locations__c field, within the Job_Application__c record. Recruiters would like this value to be kept in sync, if changes occur to the Contact's Mailing State or if the Job's Preferred_Locations__c field is updated. What is the recommended tool a developer should use to meet the business requirement?**

- **A.** Apex Trigger ❌
- **B.** Process Builder ❌
- **C.** Record-triggered flow ✅
- **D.** Formula field ❌

**📝 Dịch tiếng Việt:**
> Quy trình tuyển dụng yêu cầu xem bang Mailing State của Contact có khớp với Preferred_Locations__c trên Job__c hay không và giữ đồng bộ tự động khi một trong hai thay đổi. Công cụ khai báo (declarative) nào được khuyến nghị sử dụng?

**✅ Tại sao đáp án đúng:**
> Để theo dõi thay đổi ở cả hai đối tượng đầu vào (Contact hoặc Job) và cập nhật đồng bộ bản ghi trung gian Job_Application__c, Record-triggered flow (C) là công cụ low-code mạnh mẽ, trực quan và tối ưu nhất của Salesforce hiện nay.

**❌ Tại sao đáp án sai:**
> **A.** Apex Trigger viết bằng code phức tạp, khó bảo trì hơn và không được ưu tiên khi có thể giải quyết bằng công cụ declarative (low-code).
> **B.** Process Builder là công nghệ cũ đã bị khai tử (deprecated), hiệu năng và tính năng kém xa so với Flow.
> **D.** Formula field chỉ hiển thị dữ liệu một chiều từ cha lên con, không thể tự động đồng bộ hai chiều phức tạp giữa các object.

**💡 Từ khóa ghi nhớ:** `Đồng bộ dữ liệu đa chiều + Low-code chuẩn chỉnh 2026 -> Chọn ngay Record-triggered flow!`

---

## Câu 28

**🔵 A developer declared a class as follows.
public class wysiwyg {
//properties and methods including DML
}
Which invocation of a class method will obey the organization-wide defaults and sharing settings for the running user in the Salesforce organization?**

- **A.** An Apex trigger that invokes a helper method in this class ❌
- **B.** A developer using the Developer Console that invokes a method in this class from the execute anonymous window ✅
- **C.** A Visualforce page with an Apex controller that invokes a method in this class ❌
- **D.** A user on an external system that has an API call into Salesforce that invokes a method in this class ❌

**📝 Dịch tiếng Việt:**
> Một class khai báo đơn giản `public class wysiwyg` chứa các phương thức DML. Cách gọi phương thức nào của class này sẽ tuân thủ OWD và sharing settings của user đang chạy?

**✅ Tại sao đáp án đúng:**
> Mặc định class không khai báo từ khóa sharing sẽ chạy ở chế độ hệ thống (system mode - bỏ qua sharing). Tuy nhiên, khi gọi code từ cửa sổ Anonymous Block (B) trong Developer Console, Salesforce luôn ép buộc tuân thủ tuyệt đối phân quyền và sharing settings của user đang thao tác.

**❌ Tại sao đáp án sai:**
> **A.** Trigger luôn chạy ở chế độ hệ thống (system mode), nên gọi helper class này cũng sẽ bỏ qua sharing rules của user.
> **C.** Visualforce controller chạy ở system mode mặc định, bỏ qua sharing rules trừ khi class được khai báo rõ ràng là 'with sharing'.
> **D.** API call từ hệ thống bên ngoài chạy dưới ngữ cảnh tài khoản tích hợp, cũng bỏ qua sharing rules nếu class không chỉ định.

**💡 Từ khóa ghi nhớ:** `Execute Anonymous = Luôn tuân thủ quyền hạn và sharing rules của user đang chạy.`

---

## Câu 29

**🔵 Universal Containers uses a simple Order Management app. On the Order Lines, the order line total is calculated by multiplying the item price with the quantity ordered. There is a Master-Detail relationship between the Order and the Order Lines object. What is the best practice to get the sum of all order line totals on the order header?**

- **A.** Declarative Roll-Up Summaries App ❌
- **B.** Roll-Up Summary field ✅
- **C.** Process Builder ❌
- **D.** Apex Trigger ❌

**📝 Dịch tiếng Việt:**
> Có mối quan hệ Master-Detail giữa Order (Master) và Order Line (Detail). Cách tốt nhất để tính tổng giá trị của tất cả các dòng Order Lines lên bản ghi Order cha là gì?

**💬 Giải thích gốc (English):**
> Roll-Up Summary Fields are a powerful feature in Salesforce that allow you to calculate and display aggregate values (such as sum, count, max, min, etc.) from child records on a parent record. In this case, you can create a Roll-Up Summary Field on the Order object to calculate the total order amount by summing up the order line totals from all related Order Line records.

**✅ Tại sao đáp án đúng:**
> Vì mối quan hệ ở đây là Master-Detail, sử dụng Roll-Up Summary field (B) là giải pháp hoàn hảo nhất: không tốn một dòng code, tự động tính toán chính xác real-time và đúng chuẩn Salesforce Best Practice.

**❌ Tại sao đáp án sai:**
> **A.** Hệ thống đã hỗ trợ sẵn Roll-Up Summary field, cài đặt thêm App ngoài (Declarative Roll-Up Summaries) là thừa thãi và cồng kềnh.
> **C.** Process Builder không hỗ trợ tính toán tổng hợp (SUM, COUNT) danh sách con một cách trực tiếp.
> **D.** Apex Trigger hoạt động tốt nhưng viết code cho một tính năng đã có sẵn no-code là vi phạm nguyên tắc tối ưu hóa hệ thống.

**💡 Từ khóa ghi nhớ:** `Quan hệ Master-Detail + Tính tổng/Đếm lên Cha = dùng ngay Roll-Up Summary Field!`

---

## Câu 30

**🔵 Given the following Apex statement: Account myAccount = [SELECT Id, Name FROM Account]; What occurs when more than one Account is returned by the SOQL query?**

- **A.** The variable, myAccount, is automatically cast to the List data type. ❌
- **B.** The first Account returned is assigned to myAccount. ❌
- **C.** The query fails and an error is written to the debug log. ❌
- **D.** An unhandled exception is thrown and the code terminates. ✅

**📝 Dịch tiếng Việt:**
> Điều gì xảy ra khi câu query SOQL `Account myAccount = [SELECT Id, Name FROM Account];` trả về nhiều hơn một bản ghi Account trong hệ thống?

**💬 Giải thích gốc (English):**
> When the query returns multiple records (multiple Accounts in this case), Salesforce will raise a QueryException because you cannot assign a list of records to a single record variable.

**✅ Tại sao đáp án đúng:**
> Apex sẽ ném ra một ngoại lệ không được xử lý (unhandled exception) là `QueryException: List has more than 1 row for assignment` và dừng ngay lập tức việc thực thi code (D).

**❌ Tại sao đáp án sai:**
> **A.** Apex cực kỳ nghiêm khắc, không bao giờ tự động ép kiểu từ sObject sang List cho bạn.
> **B.** Hệ thống không tự ý lấy bản ghi đầu tiên, muốn lấy bản ghi đầu tiên bạn phải thêm từ khóa `LIMIT 1` vào câu truy vấn.
> **C.** Nó không chỉ ghi lỗi vào debug log mà còn chặn đứng tiến trình và rollback toàn bộ transaction.

**💡 Từ khóa ghi nhớ:** `Query gán cho biến đơn mà trả về nhiều bản ghi -> Báo lỗi vỡ trận (QueryException) ngay lập tức!`

---

## Câu 31

**🔵 Which two statements are true about Apex code executed in Anonymous Blocks? (Choose two.)**

- **A.** The code runs with the permissions of the user specified in the runAs() statement. ❌
- **B.** The code runs with the permissions of the logged in user. ✅
- **C.** The code runs in system mode having access to all objects and fields. ❌
- **D.** All DML operations are automatically rolled back. ❌
- **E.** Successful DML operations are automatically committed. ✅

**📝 Dịch tiếng Việt:**
> Hai phát biểu nào sau đây là đúng về mã Apex được thực thi trong Anonymous Block? (Chọn 2)

**💬 Giải thích gốc (English):**
> Limited Access to Data: Anonymous Blocks have access only to data that the running user has permission to view. They don't have access to data that requires higher permissions, such as records with "View All" or "Modify All" permission.
> Data Changes are Committed: Any data changes made within an Anonymous Block are committed to the database and cannot be rolled back. Unlike unit tests, which perform a full rollback after execution, data changes made in Anonymous Blocks are permanent. This means that if you modify records or data in the Anonymous Block, those changes will be saved to the database.

**✅ Tại sao đáp án đúng:**
> B: Code chạy hoàn toàn dưới quyền hạn và phân quyền (Sharing/FLS/CRUD) của user đang đăng nhập. E: Mọi thao tác DML thành công trong Anonymous Block sẽ được commit vĩnh viễn vào database (không tự rollback như unit test).

**❌ Tại sao đáp án sai:**
> **A.** System.runAs() chỉ dùng được trong unit test class, cấm dùng trong Anonymous Block.
> **C.** Ngược lại, Anonymous Block chạy ở User mode chứ không phải System mode.
> **D.** Thao tác DML thành công sẽ được lưu thật, không hề tự động rollback.

**💡 Từ khóa ghi nhớ:** `Anonymous Block = Chạy dưới quyền User đang chạy + Lưu thật vào database.`

---

## Câu 32

**🔵 Using DescribeSObjectResult, which Apex method can a developer use to determine if the current user can edit records for an object?**

- **A.** canUpdate() ❌
- **B.** canEdit() ❌
- **C.** isUpdateable() ✅
- **D.** isEditable() ❌

**📝 Dịch tiếng Việt:**
> Sử dụng DescribeSObjectResult, phương thức Apex nào giúp lập trình viên xác định xem user hiện tại có quyền chỉnh sửa các bản ghi của một object hay không?

**💬 Giải thích gốc (English):**
> Developer can use the isUpdateable() method. This method allows you to check if the current user has the necessary permissions to edit records of a specific object.

**✅ Tại sao đáp án đúng:**
> isUpdateable() (C) là hàm chuẩn của lớp DescribeSObjectResult để kiểm tra xem user hiện tại có quyền Edit (Update) đối với sObject đó hay không.

**❌ Tại sao đáp án sai:**
> **A.** Hàm canUpdate() không tồn tại trong lớp DescribeSObjectResult.
> **B.** Hàm canEdit() cũng là hàng giả tưởng.
> **D.** isEditable() nghe rất xuôi tai nhưng thực tế Salesforce dùng thuật ngữ 'Updateable' cho quyền Edit.

**💡 Từ khóa ghi nhớ:** `Quyền Sửa (Edit/Update) trong Apex Describe = isUpdateable().`

---

## Câu 33

**🔵 Given the code below:
Public class Mycontroller {
private Integer recordCount;
}
what can be done so that recordCount can be accessed by a test class, but not by a non-test class?**

- **A.** Change recordCount from private to public. ❌
- **B.** Add the SeeAllData annotation to the test class. ❌
- **C.** Add the TestVisible annotation to recordCount. ✅
- **D.** Add the TestVisible annotation to the MyController class. ❌

**📝 Dịch tiếng Việt:**
> Cho đoạn code sau:
public class MyController {
private Integer recordCount;
}
Cần làm gì để recordCount có thể được truy cập bởi một class test, nhưng cấm truy cập từ các class thông thường khác?

**💬 Giải thích gốc (English):**
> The TestVisible annotation allows test classes to access private or protected members of a class.

**✅ Tại sao đáp án đúng:**
> Annotation @TestVisible (C) cho phép các class test nhìn thấy và thao tác được với các biến/phương thức private hoặc protected mà vẫn giữ nguyên tính đóng gói bảo mật đối với bên ngoài.

**❌ Tại sao đáp án sai:**
> **A.** Chuyển sang public sẽ làm lộ biến ra ngoài toàn hệ thống, phá vỡ tính đóng gói.
> **B.** SeeAllData liên quan đến việc truy cập dữ liệu bản ghi thật trong Org, không liên quan đến biến private.
> **D.** @TestVisible phải gắn trực tiếp lên biến recordCount, gắn lên cấp class MyController là sai cú pháp.

**💡 Từ khóa ghi nhớ:** `Test muốn soi đồ Private -> Gắn @TestVisible.`

---

## Câu 34

**🔵 Which two number expressions evaluate correctly? (Choose two.)**

- **A.** Double d = 3.14159; ✅
- **B.** Integer I = 3.14159; ❌
- **C.** Decimal d = 3.14159; ✅
- **D.** Long l = 3.14159; ❌

**📝 Dịch tiếng Việt:**
> Hai biểu thức khai báo số nào sau đây được biên dịch thành công? (Chọn 2)

**💬 Giải thích gốc (English):**
> A. Double d = 3.14159;: This expression is correct because 3.14159 is a floating-point literal, and it can be assigned to a variable of type Double
> C. Decimal d = 3.14159;: This expression is correct because 3.14159 is a floating-point literal, and it can be assigned to a variable of type Decimal

**✅ Tại sao đáp án đúng:**
> A: Số thập phân literal mặc định được gán rất mượt cho kiểu Double. C: Kiểu Decimal trong Apex cũng chấp nhận gán trực tiếp số thập phân.

**❌ Tại sao đáp án sai:**
> **B.** Integer chỉ chứa số nguyên, nhét số thập phân 3.14159 vào compiler sẽ báo lỗi.
> **D.** Long cũng chỉ chứa số nguyên lớn, không chấp nhận số thập phân literal trực tiếp.

**💡 Từ khóa ghi nhớ:** `Số thập phân -> Gán cho Double hoặc Decimal. Cấm gán cho Integer / Long.`

---

## Câu 35

**🔵 Assuming that name is a String obtained by an a Visualforce page.
which two SOQL Queries performed are safe from SOQL injection? (Choose two.)**

- **A.** List<Account> results = [SELECT Id FROM Account WHERE Name LIKE :query]; ✅
- **B.** String query = 'SELECT Id FROM Account WHERE Name LIKE \'%' + name.noQuotes()+ '%\''; List<Account> results = Database.query(query); ❌
- **C.** String query = 'SELECT Id FROM Account WHERE Name LIKE \'%' + string.escapeSingleQuotes(name) + '%\'';  List<Account> results = Database.query(query); ✅
- **D.** String query = 'SELECT Id FROM Account WHERE Name LIKE \'% + name + '%\'';  List<Account> results = Database.query(query); ❌

**📝 Dịch tiếng Việt:**
> Giả sử 'name' là một String nhận được từ thẻ <apex:inputText> trên một trang Visualforce, hai câu truy vấn SOQL nào sau đây là an toàn trước lỗi SOQL injection? (Chọn 2)

**💬 Giải thích gốc (English):**
> A: Uses Apex binding to dynamically insert the value of the 'name' variable into the SOQL query. This approach ensures that the input is properly sanitized and prevents any malicious injection of SOQL queries.
> C: Uses the 'string.escapeSingleQuotes()' method to properly escape any single quotes in the 'name' variable before inserting it into the query. This prevents the injection of malicious queries and ensures the query's integrity.

**✅ Tại sao đáp án đúng:**
> B: Sử dụng hàm escapeSingleQuotes() để vô hiệu hóa các ký tự điều khiển trong chuỗi. C: Sử dụng Static SOQL với Variable Binding (dấu hai chấm ':') là cách an toàn nhất vì Salesforce tự xử lý việc sanitize.

**❌ Tại sao đáp án sai:**
> **B.** Cộng chuỗi trực tiếp từ user input là con đường nhanh nhất để bị hack.
> **D.** Database.query() với chuỗi được cộng trực tiếp mà không qua sanitize cực kỳ nguy hiểm và dễ bị injection.

**💡 Từ khóa ghi nhớ:** `Chống SOQL Injection: 1. Static SOQL (:bind), 2. escapeSingleQuotes().`

---

## Câu 36

**🔵 A developer must create a ShippingCalculator class that cannot be instantiated and must include a working default implementation of a calculate method, that sub-classes can override. What is the correct implementation of the ShippingCalculator class?**

- **A.** public abstract class ShippingCalculator {
  public abstract calculate() {/* implementation */ }
} ❌
- **B.** public abstract class ShippingCalculator {
  public void calculate() {/* implementation */ }
} ❌
- **C.** public abstract class ShippingCalculator {
  public virtual void calculate() {/* implementation */ }
} ✅
- **D.** public abstract class ShippingCalculator {
  public override calculate() {/* implementation */ }
} ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên cần tạo class ShippingCalculator không được phép khởi tạo trực tiếp (cannot be instantiated) nhưng phải chứa một phương thức calculate có sẵn mã xử lý mặc định để các class con có thể ghi đè (override). Khai báo nào sau đây là đúng?

**💬 Giải thích gốc (English):**
> To create a ShippingCalculator class that cannot be instantiated and includes a default implementation of a calculate method that sub-classes can override, you can use the abstract keyword for the class and the virtual keyword for the calculate method.

**✅ Tại sao đáp án đúng:**
> Để class không được khởi tạo trực tiếp, ta dùng từ khóa 'abstract class'. Để phương thức có code mặc định và cho phép class con ghi đè, ta dùng từ khóa 'public virtual void calculate() ...' (tương ứng với đáp án C).

**❌ Tại sao đáp án sai:**
> **A.** Phương thức calculate() khai báo abstract thì không được phép định nghĩa body (phần thân hàm có chứa code mặc định) trong Apex.
> **B.** Thiếu từ khóa 'virtual' ở phương thức calculate() khiến lớp con không thể sử dụng từ khóa 'override' để ghi đè.
> **D.** Từ khóa 'override' chỉ dùng khi lớp con muốn ghi đè phương thức từ lớp cha, không thể dùng ở lớp cha để khai báo ban đầu.

**💡 Từ khóa ghi nhớ:** `Không cho new trực tiếp -> abstract class. Cho phép ghi đè + có code mặc định -> virtual method.`

---

## Câu 37

**🔵 Given the following Anonymous block:
List<Case> casesToUpdate = new List<Case>();
for(Case thisCase : [SELECT Id, Status FROM Case LIMIT 50000]){
thisCase.Status = 'Working';
CasesToUpdate.add(thisCase);
}
try{
Database.update(casesToUpdate, false);
}catch(Exception e){
System.debug(e.getMessage());
}
What should a developer consider for an environment that has over 10,000 Case records?**

- **A.** The try-catch block will handle exceptions thrown by governor limits. ❌
- **B.** The transaction will fall due to exceeding the governor limit. ✅
- **C.** The transaction will succeed and changes will be committed. ❌
- **D.** The try-catch block will handle any DML exceptions thrown. ❌

**📝 Dịch tiếng Việt:**
> Đoạn mã Anonymous Block trên xử lý cập nhật 50,000 Case. Với môi trường có hơn 10,000 bản ghi, điều gì sẽ xảy ra?

**💬 Giải thích gốc (English):**
> If there are more than 10,000 Case records in the environment, the code may hit the DML row limit and result in a "Too many DML rows: 10001" exception.

**✅ Tại sao đáp án đúng:**
> Giới hạn DML Row trong một transaction là 10,000. Đoạn code này cố gắng update tới 50,000 bản ghi trong 1 nốt nhạc, chắc chắn sẽ 'ăn' LimitException và oẳng luôn cả transaction.

**❌ Tại sao đáp án sai:**
> **A.** Governor Limit Exception (như LimitException) là loại 'bất trị', Try/Catch KHÔNG BAO GIỜ bắt được nó.
> **C.** Dù bắt được DML Exception thì transaction vẫn tạch vì dính limit 10k bản ghi trước khi kịp chạy Database.update thành công.
> **D.** Không bao giờ thành công nổi với cái LIMIT 50,000 to đùng kia.

**💡 Từ khóa ghi nhớ:** `Governor Limits = Cảnh sát giao thông. Mày vi phạm là nó 'cẩu xe' (Exception), không có Try/Catch nào xin xỏ được đâu.`

---

## Câu 38

**🔵 Which process automation should be used to send an outbound message without using Apex code?**

- **A.** Flow Builder ❌
- **B.** Process Builder ❌
- **C.** Workflow Rule ✅
- **D.** Approval Process ❌

**📝 Dịch tiếng Việt:**
> Quy trình tự động hóa nào nên được sử dụng để gửi một outbound message mà không cần sử dụng mã Apex?

**💬 Giải thích gốc (English):**
> You can use the Workflow Outbound Message process automation in Salesforce to send an outbound message without using Apex code.

**✅ Tại sao đáp án đúng:**
> Dù đã cũ, nhưng Workflow Rule vẫn là công cụ duy nhất trong danh sách này có tính năng gửi Outbound Message trực tiếp từ giao diện Setup mà không cần code bổ sung.

**❌ Tại sao đáp án sai:**
> **B.** Process Builder không hỗ trợ gửi Outbound Message trực tiếp.
> **A.** Strategy Builder dùng để đề xuất ưu đãi/hành động trong Next Best Action, không hỗ trợ gửi Outbound Message.
> **D.** Flow Builder muốn gửi Outbound Message phải gọi Apex hoặc dùng External Service (cần cấu hình thêm).

**💡 Từ khóa ghi nhớ:** `Outbound Message = Workflow Rule. (Mẹo thi: Flow giờ là vua, nhưng câu hỏi về OM thì cứ nhớ Workflow).`

---

## Câu 39

**🔵 A developer has an Apex controller for a Visualforce page that takes an ID as a URL parameter. How should the developer prevent a cross site scripting vulnerability?**

- **A.** ApexPages.currentPage().getParameters().get('url_param') ❌
- **B.** String.escapeSingleQuotes(ApexPages.currentPage().getParameters().get('url_param')) ✅
- **C.** String.ValueOf(ApexPages.currentPage().getParameters().get('url_param')) ❌
- **D.** ApexPages.currentPage().getParameters().get('url_param').escapeHtml4() ❌

**📝 Dịch tiếng Việt:**
> Làm thế nào để ngăn chặn lỗ hổng bảo mật XSS khi nhận tham số từ URL trong Visualforce?

**💬 Giải thích gốc (English):**
> This option is the correct approach to prevent XSS vulnerabilities. The String.escapeSingleQuotes() method escapes any single quotes (') in the parameter value, making it safe for further use in Apex code and preventing potential script injection.

**✅ Tại sao đáp án đúng:**
> Sử dụng `.escapeHtml()` giúp biến các ký tự nguy hiểm thành văn bản thuần, ngăn trình duyệt thực thi mã độc.

**❌ Tại sao đáp án sai:**
> **A.** String.valueOf() chỉ ép kiểu, không có tác dụng khử khuẩn mã độc.
> **C.** escapeSingleQuotes() dùng cho SOQL Injection (SQL), không phải XSS (HTML).
> **D.** Lấy trực tiếp mà không xử lý là dâng "tận miệng" cho hacker hack XSS.

**💡 Từ khóa ghi nhớ:** `XSS = Hacker nhồi script vào UI. Cách chống: .escapeHtml() hoặc dùng <apex:outputText> mặc định.`

---

## Câu 40

**🔵 A Visual Flow uses an Apex Action to provide additional information about multiple Contacts, stored in a custom class, ContactInfo. Which is the correct definition of the Apex method that gets the additional information?**

- **A.** @InvocableMethod(label='Additional Info')
public ContactInfo getInfo(Id contactId) { /*implementation*/ } ❌
- **B.** @InvocableMethod(label='Additional Info')
public List<ContactInfo> getInfo(List<Contact> contactIds) { /*implementation*/ } ❌
- **C.** @InvocableMethod(label='Additional Info')
public static ContactInfo getInfo(Id contactId) { /*implementation*/ } ❌
- **D.** @InvocableMethod(label='Additional Info')
public static List<ContactInfo> getInfo(List<Contact> contactIds) { /*implementation*/ } ✅

**📝 Dịch tiếng Việt:**
> Một Screen Flow gọi một Apex Action để lấy thông tin chi tiết cho nhiều bản ghi Contact, kết quả lưu trong một custom class ContactInfo. Định nghĩa phương thức Apex nào sau đây là đúng tiêu chuẩn?

**💬 Giải thích gốc (English):**
> This is an example.
> public class ContactInfo {
> @InvocableVariable(label='Contacts' description='List of Contacts to get additional information' required=true)
> public List<Contact> contactsList;
> @InvocableVariable(label='Additional Information' description='Additional information about the Contacts' required=true)
> public String additionalInfo;
> }
> public class ContactInfoApexAction {
> @InvocableMethod(label='Get Additional Information for Contacts')
> public static List<ContactInfo> getInfo(List<ContactInfo> contactInfoList) {
> // Perform the logic to get additional information about the Contacts
> // Update the 'additionalInfo' field of each ContactInfo in the input list
> // Example:
> for (ContactInfo info : contactInfoList) {
> List<Contact> contactsToUpdate = info.contactsList;
> String additionalInfo = 'Additional information for these Contacts.';
> info.additionalInfo = additionalInfo;
> }
> return contactInfoList;
> }
> }
> public class ContactInfoApexAction {
> @InvocableMethod(label='Get Additional Information for Contacts')
> public static List<ContactInfo> getAdditionalInformation(List<ContactInfo> contactInfoList) {
> // Perform the logic to get additional information about the Contacts
> // Update the 'additionalInfo' field of each ContactInfo in the input list
> // Example:
> for (ContactInfo info : contactInfoList) {
> List<Contact> contactsToUpdate = info.contactsList;
> String additionalInfo = 'Additional information for these Contacts.';
> info.additionalInfo = additionalInfo;
> }
> return contactInfoList;
> }
> }

**✅ Tại sao đáp án đúng:**
> D đúng vì: 1. Phương thức đính kèm `@InvocableMethod` phải là `static`. 2. Để hỗ trợ xử lý hàng loạt (bulkification), cả tham số đầu vào và giá trị trả về của phương thức `@InvocableMethod` phải ở dạng `List` (ví dụ: `List<Contact>` hoặc `List<Id>`).

**❌ Tại sao đáp án sai:**
> **A.** Thiếu từ khóa `static` (bắt buộc phải có để Flow gọi) và không sử dụng danh sách `List` cho input/output.
> **B.** Thiếu từ khóa `static` (bắt buộc phải có) mặc dù đã sử dụng danh sách `List` cho input/output.
> **C.** Đã sử dụng từ khóa `static` nhưng không sử dụng danh sách `List` cho input/output để hỗ trợ bulkification.

**💡 Từ khóa ghi nhớ:** `@InvocableMethod: Luôn đính kèm STATIC, input và output bắt buộc phải ở dạng LIST.`

---

## Câu 41

**🔵 Which aspect of Apex programming is limited due to multitenancy?**

- **A.** The number of methods in an Apex class ❌
- **B.** The number of records returned from database queries ✅
- **C.** The number of active Apex classes ❌
- **D.** The number of records processed in a loop ❌

**📝 Dịch tiếng Việt:**
> Khía cạnh nào bị giới hạn bởi cơ chế đa thuê bao (Multitenancy) trong Salesforce?

**💬 Giải thích gốc (English):**
> The number of records returned from database queries is limited due to multitenancy in Salesforce. Salesforce enforces governor limits to prevent queries from returning an excessive number of records, which could impact the performance and stability of the platform for other users.

**✅ Tại sao đáp án đúng:**
> Salesforce giới hạn số bản ghi trả về mỗi query (50,000 rows) để đảm bảo một khách hàng không 'chiếm dụng' hết tài nguyên database của server dùng chung.

**❌ Tại sao đáp án sai:**
> **A.** Số lượng method trong class không phải là một Governor Limit chính yếu bị ảnh hưởng trực tiếp bởi multitenancy.
> **D.** Org giới hạn tổng dung lượng code (6MB cho Apex), chứ không giới hạn cứng số lượng class theo kiểu transaction limit.
> **C.** Vòng lặp không bị giới hạn số lần, mà bị giới hạn bởi thời gian CPU thực thi (CPU Time).

**💡 Từ khóa ghi nhớ:** `Multitenancy = Governor Limits. Nhớ mốc 50,000 query rows.`

---

## Câu 42

**🔵 A developer is migrating a Visualforce page into a Lightning web component. The Visualforce page shows information about a single record. The developer decides to use Lightning Data Service to access record data. Which security consideration should the developer be aware of?**

- **A.** The with sharing keyword must be used to enforce sharing rules. ❌
- **B.** Lightning Data Service handles sharing rules and field-level security. ✅
- **C.** The isAccessible() method must be used for field-level access checks. ❌
- **D.** Lightning Data Service ignores field-level security. ❌

**📝 Dịch tiếng Việt:**
> Cân nhắc bảo mật nào khi dùng Lightning Data Service (LDS)?

**💬 Giải thích gốc (English):**
> Check CRUD and FLS: Before accessing the record data through LDS, check whether the current user has the necessary CRUD permissions for the object and whether they have FLS permissions for the specific fields you are accessing. You can use Apex's Schema classes to check FLS for fields.

**✅ Tại sao đáp án đúng:**
> LDS tự động xử lý Sharing và FLS cực kỳ an toàn.

**❌ Tại sao đáp án sai:**
> **A.** Ngược lại, LDS rất tôn trọng FLS.
> **C.** with sharing dùng cho Apex, không liên quan LDS.
> **D.** isAccessible() là kiểm tra thủ công trong Apex, LDS tự làm rồi.

**💡 Từ khóa ghi nhớ:** `LDS = Security Built-in. Không cần lo check quyền thủ công.`

---

## Câu 43

**🔵 Which approach should a developer use to add pagination to a Visualforce page?**

- **A.** A StandardController ❌
- **B.** The Action attribute for a page ❌
- **C.** The extensions attribute for a page ❌
- **D.** A StandardSetController ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên nên sử dụng phương pháp nào để thêm tính năng phân trang (pagination) vào một trang Visualforce?

**💬 Giải thích gốc (English):**
> Use StandardSetController: The StandardSetController is a built-in Apex class that provides pagination functionality for displaying sets of records in Visualforce pages. It allows developers to easily implement pagination with minimal code.

**✅ Tại sao đáp án đúng:**
> StandardSetController (D) là lớp có sẵn cực xịn của Salesforce, cung cấp toàn bộ các hàm phân trang như next(), previous(), setPageSize() giúp lập trình viên code cực nhàn.

**❌ Tại sao đáp án sai:**
> **A.** StandardController chỉ quản lý duy nhất 1 bản ghi cụ thể, không hỗ trợ danh sách và phân trang.
> **B.** Action attribute dùng để gọi method khi trang load, không liên quan phân trang.
> **C.** Extensions dùng để mở rộng tính năng chung, không phải class chuyên dụng cho phân trang như StandardSetController.

**💡 Từ khóa ghi nhớ:** `Phân trang (Pagination) trên Visualforce -> StandardSetController.`

---

## Câu 44

**🔵 Which message is logged by the code below?**

- **A.** Generic Exception ❌
- **B.** List Exception ❌
- **C.** NullPointer Exception ✅
- **D.** No message is logged. ❌

**📝 Dịch tiếng Việt:**
> Thông báo lỗi (exception) nào sẽ được ghi lại trong log bởi đoạn mã dưới đây? (Giả định đoạn code cố tình thực hiện thao tác trên một đối tượng chưa được khởi tạo - null)

**✅ Tại sao đáp án đúng:**
> Trong Salesforce, khi mày cố gắng truy cập thuộc tính hoặc gọi phương thức từ một biến đối tượng đang có giá trị null (chưa được khởi tạo bằng từ khóa 'new'), hệ thống sẽ ném ra lỗi 'NullPointerException' (C). Đây là lỗi kinh điển của mọi lập trình viên.

**❌ Tại sao đáp án sai:**
> **A.** Generic Exception là lớp cha chung (Exception), hệ thống sẽ ghi nhận lỗi cụ thể nhất là NullPointerException.
> **B.** List Exception chỉ xảy ra khi mày thao tác sai với List (ví dụ truy cập chỉ số vượt quá độ dài danh sách).
> **D.** Chắc chắn có lỗi và log sẽ được ghi lại khi code chạy dính null.

**💡 Từ khóa ghi nhớ:** `Đụng vào biến null mà đòi gọi method/field -> Ăn ngay NullPointerException.`

---

## Câu 45

**🔵 Universal Containers implemented a private sharing model for the Account object. A custom Account search tool was developed with Apex to help sales representatives find accounts that match multiple criteria they specify. Since its release, users of the tool report they can see Accounts they do not own. What should the developer use to enforce sharing permissions for the currently logged-in user while using the custom search tool?**

- **A.** Use the schema describe calls to determine if the logged-in user has access to the Account object. ❌
- **B.** Use the UserInfo Apex class to filter all SOQL queries to returned records owned by the logged-in user. ❌
- **C.** Use the with sharing keyword on the class declaration. ✅
- **D.** Use the without sharing keyword on the class declaration. ❌

**📝 Dịch tiếng Việt:**
> Làm sao để class Apex tuân thủ luật Sharing của User?

**💬 Giải thích gốc (English):**
> To enforce sharing permissions for the currently logged-in user while using the custom search tool, the developer should use the with sharing keyword in the Apex class that backs the search tool.

**✅ Tại sao đáp án đúng:**
> Từ khóa `with sharing` ép Apex phải kiểm tra quyền xem bản ghi của User đó.

**❌ Tại sao đáp án sai:**
> **B.** Schema describe chỉ check quyền Object (CRUD), không check được quyền trên từng bản ghi (Sharing).
> **A.** Without sharing là 'mở toang' hết, ai cũng thấy hết mọi thứ.
> **D.** Filter theo Owner chỉ là một phần nhỏ của Sharing, không bao quát hết các luật Sharing phức tạp.

**💡 Từ khóa ghi nhớ:** `Security: Always start with 'with sharing'.`

---

## Câu 46

**🔵 What are two ways that a controller and extension can be specified for a custom object named “Notice” on a Visualforce page? (Choose two.)**

- **A.** apex:page standardController=”Notice__c” extensions=”myControllerExtension” ✅
- **B.** apex:page=Notice extends=”myControllerExtension” ❌
- **C.** apex:page controller=”Notice__c” extensions=”myControllerExtension” ✅
- **D.** apex:page controllers=”Notice__c, myControllerExtension” ❌

**📝 Dịch tiếng Việt:**
> Có hai cách nào để khai báo Controller và Extension cho một custom object tên là 'Notice__c' trên trang Visualforce? (Chọn 2)

**💬 Giải thích gốc (English):**
> Controller Attribute: You can specify the controller for the Visualforce page using the controller attribute in the <apex:page> tag.
> Extension Attribute: You can specify an extension for the Visualforce page using the extensions attribute in the <apex:page> tag.

**✅ Tại sao đáp án đúng:**
> A: Khai báo sử dụng standardController cho custom object Notice__c kèm theo extensions là cách làm chuẩn mực nhất khi muốn mở rộng tính năng mặc định. C: Khai báo custom controller cho Notice__c (nếu Notice__c trùng tên với 1 class Apex custom controller) kèm extensions cũng là cú pháp hợp lệ của thẻ <apex:page>.

**❌ Tại sao đáp án sai:**
> **B.** Cú pháp sai hoàn toàn, thẻ <apex:page> không có thuộc tính 'extends' viết kiểu gán trực tiếp như thế.
> **D.** Không có thuộc tính 'controllers' (dạng số nhiều) trong thẻ <apex:page>.

**💡 Từ khóa ghi nhớ:** `Visualforce Page: standardController hoặc controller kết hợp với extensions (dạng số nhiều).`

---

## Câu 47

**🔵 A developer creates a custom controller and custom Visualforce page by using the code block below.
public class MyController{
public String myString{
get {
if(myString == null){myString = 'a';}
return myString;
}
private set;
}
public String getMyString(){
return 'getMyString';
}
public String getStringMethod(){
if(myString == null){
myString = 'b';
}
return myString;
}
}
<apex:page> controller='MyController'{!StringMethod}, {!myString}, {!myString}</apex:page>
What can the user expect to see when accessing the custom page?**

- **A.** a, b, b ❌
- **B.** a, b, getMyString ❌
- **C.** a, a, a ✅
- **D.** b, a, getMyString ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên tạo một custom controller và trang Visualforce bằng đoạn code dưới đây: [Controller & Page]. Người dùng sẽ thấy gì khi truy cập vào trang tùy chỉnh này?

**💬 Giải thích gốc (English):**
> The code block initializes myString as 'a' if it is null, so all three occurrences of {!myString} will display 'a' when accessed on the custom page.

**✅ Tại sao đáp án đúng:**
> Đáp án là 'a, a, a' (C). Do cơ chế render của Visualforce, hệ thống sẽ giải quyết và nạp giá trị cho các biến được bind (myString) trước để dựng View State. Khi myString được gọi lần đầu, getter chạy và gán myString = 'a'. Đến khi {!StringMethod} được gọi, myString đã có giá trị 'a' (không còn null nữa) nên lệnh gán 'b' bị bỏ qua, kết quả cả 3 chỗ đều hiển thị 'a'.

**❌ Tại sao đáp án sai:**
> **A.** Nếu {!StringMethod} chạy trước và gán 'b' thì kết quả sẽ là b, b, b chứ không nửa nọ nửa kia.
> **B.** Biến myString được gán trực tiếp chữ chứ không trỏ đến tên phương thức getMyString().
> **D.** Sai thứ tự giải quyết biến và cơ chế chạy của getter.

**💡 Từ khóa ghi nhớ:** `Visualforce Lifecycle: Getter chạy trước để dựng View State -> Gán 'a' từ đầu nên mãi là 'a'.`

---

## Câu 48

**🔵 Given the following trigger implementation:
trigger leadTrigger on Lead (before update) {
final ID BUSINESS_RECORDTYPEID = '012500000009Qad';
for (Lead thisLead : Trigger.new) {
if (thisLead.Company != null thisLead.RecordTypeld != BUSINESS_RECORDTYPEID) {
thisLead.RecordTypeld = BUSINESS_RECORDTYPEID;
}
}
}
The developer receives deployment errors every time a deployment is attempted from a sandbox to Production.
What should the developer do to ensure a successful deployment?**

- **A.** Ensure a record type with an ID of BUSINESS_RECORDTYPEID exists on Production prior to deployment. ✅
- **B.** Ensure BUSINESS_RECORDTYPEID is pushed as part of the deployment components. ❌
- **C.** Ensure BUSINESS_RECORDTYPEID is retrieved using Schema.Describe calls. ❌
- **D.** Ensure the deployment is validated by a System Admin user on Production. ❌

**📝 Dịch tiếng Việt:**
> Cho đoạn code trigger Lead sau: [leadTrigger]. Lập trình viên nhận được lỗi triển khai (deployment errors) mỗi khi cố gắng triển khai từ Sandbox lên Production. Lập trình viên nên làm gì để đảm bảo triển khai thành công?

**💬 Giải thích gốc (English):**
> The ID of a record type can vary between different environments (e.g., sandbox and production).
> -> Ensure a record type with an ID of BUSINESS_RECORDTYPEID exists on Production prior to deployment.

**✅ Tại sao đáp án đúng:**
> Lỗi cực kỳ cơ bản của lính mới là Hardcode ID. RecordType ID ở Sandbox và Production thường khác nhau. Dùng Schema.Describe (ví dụ: SObjectType.Lead.getRecordTypeInfosByDeveloperName()) giúp lấy ID động dựa trên tên, đảm bảo chạy đúng ở mọi môi trường.

**❌ Tại sao đáp án sai:**
> **B.** Admin validate không giải quyết được lỗi logic code.
> **C.** RecordType ID không phải là thứ có thể 'push' để giữ nguyên giá trị ID giữa các Org.
> **D.** Dù có tạo tay trên Pro cũng không ai dám chắc ID nó sẽ giống hệt Sandbox.

**💡 Từ khóa ghi nhớ:** `Keywords: Hardcoded IDs -> Bad practice. Thay bằng: Schema Describe hoặc Query theo DeveloperName.`

---

## Câu 49

**🔵 Which two settings must be defined in order to update a record of a junction object? (Choose two.)**

- **A.** Read/Write access on the junction object ❌
- **B.** Read access on the primary relationship ❌
- **C.** Read/Write access on the primary relationship ✅
- **D.** Read/Write access on the secondary relationship ✅

**📝 Dịch tiếng Việt:**
> Cần quyền gì ở các bản ghi cha để có thể cập nhật bản ghi Junction (Master-Detail)?

**💬 Giải thích gốc (English):**
> Junction Object is child and will get access settings from Primary Object.

**✅ Tại sao đáp án đúng:**
> Trong Salesforce, bản ghi Junction (con của 2 Master) bị kiểm soát quyền bởi các cha. Mày phải có quyền Read/Write ở cả Cha sơ cấp (Primary) và Cha thứ cấp (Secondary) thì mới sửa được con.

**❌ Tại sao đáp án sai:**
> **B.** Chỉ có quyền Read ở cha là không đủ để thực hiện lệnh Update trên bản ghi con.
> **A.** Bản ghi Junction kiểu MD không có quyền Sharing độc lập để mày set riêng.

**💡 Từ khóa ghi nhớ:** `Junction Security: Sửa con = R/W cả 2 Cha.`

---

## Câu 50

**🔵 Which tag should a developer include when styling from external CSS is required in a Visualforce page?**

- **A.** apex:includeStyles ❌
- **B.** apex:includeScript ❌
- **C.** apex:require ❌
- **D.** apex:stylesheet ✅

**📝 Dịch tiếng Việt:**
> Thẻ nào mà lập trình viên nên sử dụng khi cần nhúng CSS từ file bên ngoài (external CSS) vào một trang Visualforce?

**💬 Giải thích gốc (English):**
> To include external CSS styling in a Visualforce page, a developer should use the <apex:stylesheet> tag. The <apex:stylesheet> tag is used to reference an external CSS file and apply the specified styles to the Visualforce page.

**✅ Tại sao đáp án đúng:**
> Thẻ <apex:stylesheet> (D) sinh ra là để nhúng các file CSS (từ Static Resource hoặc URL ngoài) vào trang Visualforce, giúp định dạng giao diện một cách chuyên nghiệp.

**❌ Tại sao đáp án sai:**
> **A.** Thẻ <apex:includeStyles> là thẻ không tồn tại trong thư viện Visualforce của Salesforce.
> **B.** Thẻ <apex:includeScript> dùng để nhúng file JavaScript chứ không dùng cho CSS.
> **C.** Thẻ <apex:require> dùng để tải các thư viện JS ngoài theo dạng RequireJS, không dùng để nạp stylesheet.

**💡 Từ khóa ghi nhớ:** `Visualforce: Nhúng CSS -> Dùng <apex:stylesheet>. Nhúng JS -> Dùng <apex:includeScript>.`

---

## Câu 51

**🔵 Which declarative process automation feature supports iterating over multiple records?**

- **A.** Workflow rules ❌
- **B.** Flows ✅
- **C.** Validation rules ❌
- **D.** Approval processes ❌

**📝 Dịch tiếng Việt:**
> Tính năng tự động hóa dạng khai báo (declarative) nào hỗ trợ duyệt (lặp) qua nhiều bản ghi cùng lúc?

**💬 Giải thích gốc (English):**
> Flows is a powerful tool in Salesforce that allows administrators and developers to create automated processes with a point-and-click interface. One of its key functionalities is the ability to define actions that iterate over multiple records at once.

**✅ Tại sao đáp án đúng:**
> Flows (B) - cụ thể là Flow Builder - cung cấp phần tử 'Loop' cực kỳ mạnh mẽ, cho phép admin và dev duyệt qua danh sách nhiều bản ghi để xử lý logic hoàn toàn không cần code.

**❌ Tại sao đáp án sai:**
> **A.** Workflow rules chỉ chạy trên từng bản ghi đơn lẻ khi nó được save, không thể duyệt danh sách.
> **C.** Validation rules chỉ kiểm tra điều kiện trên bản ghi hiện tại để chặn lưu, không có khả năng lặp.
> **D.** Approval processes dùng để gửi duyệt bản ghi hiện tại theo từng bước, không hỗ trợ duyệt danh sách con.

**💡 Từ khóa ghi nhớ:** `Low-code duyệt qua danh sách bản ghi = LOOP trong FLOW.`

---

## Câu 52

**🔵 The Account object in an organization has a master detail relationship to a child object called Branch. The following automations exist: Rollup summary fields Custom validation rules Duplicate rules A developer created a trigger on the Account object. What two things should the developer consider while testing the trigger code? (Choose two.)**

- **A.** The trigger may fire multiple times during a transaction. ✅
- **B.** Rollup summary fields can cause the parent record to go through Save. ✅
- **C.** Duplicate rules are executed once all DML operations commit to the database. ❌
- **D.** The validation rules will cause the trigger to fire again. ❌

**📝 Dịch tiếng Việt:**
> Object Account có quan hệ Master-Detail với con là Branch. Khi viết trigger trên Account, hai điều nào lập trình viên bắt buộc phải lưu ý khi viết code test? (Chọn 2)

**💬 Giải thích gốc (English):**
> The trigger may fire multiple times during a transaction: Triggers in Salesforce can fire multiple times during a single transaction. This can happen due to workflow updates, record updates in triggers, or any other recursive actions.
> Rollup summary fields can cause the parent record to go through Save: Rollup summary fields on the Account object can trigger a recalculation of the parent record when child records (Branches) are inserted, updated, or deleted. This recalculation of the parent record may cause the trigger to fire again if the trigger logic is dependent on specific field changes or data conditions.

**✅ Tại sao đáp án đúng:**
> A: Một transaction trong Salesforce rất dễ bị chạy đè/chạy lại do workflow update hoặc trigger đệ quy, nên trigger có thể chạy nhiều lần. B: Trường Roll-up Summary trên Account (tính tổng từ con Branch) khi có thay đổi ở con sẽ tự động kích hoạt tiến trình Save và chạy trigger của Account cha.

**❌ Tại sao đáp án sai:**
> **C.** Duplicate rules chạy ngay trong tiến trình save trước khi DML commit chứ không phải sau khi commit xong.
> **D.** Validation rules chạy trước trigger after và sau trigger before, nó chỉ chặn lưu chứ không tự làm nổ trigger lại từ đầu.

**💡 Từ khóa ghi nhớ:** `Rollup Summary ở Cha = Chạm vào Con là nổ Trigger Cha. Trigger có thể nổ nhiều lần.`

---

## Câu 53

**🔵 How can a developer set up a debug log on a specific user?**

- **A.** It is not possible to setup debug logs for users other than yourself. ❌
- **B.** Ask the user for access to their account credentials, log in as the user and debug the issue. ❌
- **C.** Create Apex code that logs code actions into a custom object. ❌
- **D.** Set up a trace flag for the user, and define a logging level and time period for the trace. ✅

**📝 Dịch tiếng Việt:**
> Làm thế nào để một lập trình viên có thể thiết lập debug log cho một user cụ thể trong hệ thống?

**💬 Giải thích gốc (English):**
> To set up a debug log on a specific user in Salesforce, a developer needs to set up a TraceFlag for that user. A TraceFlag defines the logging level and time period for the trace.

**✅ Tại sao đáp án đúng:**
> Lập trình viên chỉ cần vào Setup -> Debug Logs, tạo một 'Trace Flag' cho user đó (D), chọn mức độ chi tiết (Logging Level) và khoảng thời gian theo dõi. Mọi thao tác của user đó sẽ được ghi log lại.

**❌ Tại sao đáp án sai:**
> **A.** Admin/Dev hoàn toàn có quyền setup debug log cho bất kỳ user nào trong Org.
> **B.** Đòi mật khẩu của user khác là vi phạm nghiêm trọng chính sách bảo mật thông tin.
> **C.** Viết code log vào custom object quá cồng kềnh, tốn tài nguyên DML và hoàn toàn không cần thiết khi đã có tool hệ thống.

**💡 Từ khóa ghi nhớ:** `Debug log cho User = Tạo Trace Flag trong Setup -> Debug Logs.`

---

## Câu 54

**🔵 A developer has an integer variable called maxAttempts. The developer needs to ensure that once maxAttempts is initialized, it preserves its value for the length of the Apex transaction; while being able to share the variable's state between trigger executions. How should the developer declare maxAttempts to meet these requirements?**

- **A.** Declare maxAttempts as a private static variable on a helper class. ❌
- **B.** Declare maxAttempts as a variable on a helper class. ❌
- **C.** Declare maxAttempts as a member variable on the trigger definition. ❌
- **D.** Declare maxAttempts as a constant using the static and final keywords. ✅

**📝 Dịch tiếng Việt:**
> Khai báo biến maxAttempts thế nào để giữ giá trị suốt transaction và dùng chung giữa các lần gọi trigger?

**💬 Giải thích gốc (English):**
> Apex constants are variables whose values don’t change after being initialized once. Constants can be defined using the final keyword.
> The final keyword means that the variable can be assigned at most once, either in the declaration itself, or with a static initializer method if the constant is defined in a class. This example declares two constants. The first is initialized in the declaration statement. The second is assigned a value in a static block by calling a static method.

**✅ Tại sao đáp án đúng:**
> Static giúp biến tồn tại suốt Transaction. Final giúp giá trị không bị đổi sau khi khởi tạo (hằng số).

**❌ Tại sao đáp án sai:**
> **A.** Private static thì trigger bên ngoài không 'với' tới được.
> **C.** Biến trong trigger sẽ chết ngắc khi trigger chạy xong lần đó.
> **B.** Thiếu static thì mỗi lần gọi class nó lại tạo ra instance mới, không giữ được state.

**💡 Từ khóa ghi nhớ:** `Static = Sống trọn transaction.`

---

## Câu 55

**🔵 Universal Containers (UC) decided it will not send emails to support personnel directly from Salesforce in the event that an unhandled exception occurs. Instead, UC wants an external system be notified of the error. What is the appropriate publish/subscribe logic to meet these requirements?**

- **A.** Publish the error event using the addError() method and write a trigger to subscribe to the event and notify the external system. ❌
- **B.** Publish the error event using the Eventbus.publish() method and have the external system subscribe to the event using CometD. ✅
- **C.** Have the external system subscribe to the BatchApexError event, no publishing is necessary. ❌
- **D.** Publish the error event using the addError() method and have the external system subscribe to the event using CometD. ❌

**📝 Dịch tiếng Việt:**
> Universal Containers quyết định KHÔNG gửi email báo lỗi trực tiếp từ Salesforce khi có ngoại lệ chưa được xử lý (unhandled exception). Thay vào đó, họ muốn báo lỗi sang hệ thống ngoài. Logic publish/subscribe nào là phù hợp?

**💬 Giải thích gốc (English):**
> By using the Eventbus.publish() method in the trigger to publish the Platform Event and having the external system subscribe to the event using CometD, UC can achieve the goal of notifying the external system of unhandled exceptions without directly sending emails from Salesforce. This approach provides real-time, scalable, and robust communication between Salesforce and the external system for exception notifications.

**✅ Tại sao đáp án đúng:**
> Giải pháp chuẩn hiện đại là dùng Platform Event. Lập trình viên gọi 'EventBus.publish()' để đẩy event lỗi lên bus, hệ thống ngoài sẽ subscribe (đăng ký nhận tin) thời gian thực thông qua giao thức CometD (B).

**❌ Tại sao đáp án sai:**
> **A.** Phương thức addError() chỉ dùng để hiển thị lỗi chặn lưu trên UI chứ không phải để publish Platform Event.
> **C.** BatchApexError chỉ dành riêng cho Batch Apex, không bao quát được mọi unhandled exception trong toàn hệ thống.
> **D.** addError() không đẩy được tin nhắn đi và CometD không thể nghe trực tiếp từ hàm addError().

**💡 Từ khóa ghi nhớ:** `Bắn lỗi ra hệ thống ngoài real-time -> Publish Platform Event + CometD.`

---

## Câu 56

**🔵 A developer has JavaScript code that needs to be called by controller functions in multiple Aura components by extending a new abstract component. Which resource in the abstract Aura component bundle allows the developer to achieve this?**

- **A.** helper.js ✅
- **B.** controller.js ❌
- **C.** superRender.js ❌
- **D.** renderer.js ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên có đoạn mã JavaScript dùng chung cần được gọi bởi các hàm controller trong nhiều Aura Component khác nhau thông qua việc kế thừa một abstract component mới. Tài nguyên nào trong abstract Aura component bundle hỗ trợ việc này?

**💬 Giải thích gốc (English):**
> To achieve the goal of calling JavaScript code by controller functions in multiple Aura components by extending a new abstract component, the developer can use the Helper resource in the abstract Aura component bundle.

**✅ Tại sao đáp án đúng:**
> Trong Aura Component, file helper.js (A) là nơi lý tưởng để viết các hàm JavaScript dùng chung. Khi các component con kế thừa (extends) abstract component cha, chúng có thể gọi trực tiếp các hàm helper của cha.

**❌ Tại sao đáp án sai:**
> **B.** controller.js chỉ xử lý trực tiếp các action của riêng component đó, không kế thừa tốt như helper.
> **C.** superRender.js là một cái tên tự chế, không tồn tại trong Aura bundle.
> **D.** renderer.js dùng để can thiệp vào quá trình render HTML/DOM, không dùng để chứa business logic dùng chung.

**💡 Từ khóa ghi nhớ:** `Aura Kế thừa / Dùng chung code JS -> Đút hết vào helper.js.`

---

## Câu 57

**🔵 A developer must create a Lightning component that allows users to input Contact record information to create a Contact record, including a Salary__c custom field. What should the developer use, along with a lightning-record-edit-form, so that Salary__c field functions as a currency input and is only viewable and editable by users that have the correct field level permissions on Salary__c?**

- **A.** <lightning-input type="number" value="Salary__c" formatter="currency"></lightning-input> ❌
- **B.** <lightning-formatted-number value="Salary__c" format-style="currency"></lightning-formatted-number> ❌
- **C.** <ligthning-input-field field-name="Salary__c"></lightning-input-field> ✅
- **D.** <lightning-input-currency value="Salary__c"></lightning-input-currency> ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên cần tạo LWC cho phép nhập thông tin Contact bao gồm trường lương Salary__c. Cần dùng thẻ nào đi kèm lightning-record-edit-form để trường Salary__c tự động hiển thị dạng tiền tệ và chỉ cho phép xem/sửa đối với user có quyền FLS phù hợp?

**💬 Giải thích gốc (English):**
> Using the lightning-record-edit-form along with lightning-input-field and setting the disabled attribute appropriately based on field-level permissions, the developer can ensure that the Salary__c field functions as a currency input and is only viewable and editable by users with the correct permissions.

**✅ Tại sao đáp án đúng:**
> Thẻ <lightning-input-field> (C) là 'vũ khí hạng nặng' của LWC. Khi đặt trong lightning-record-edit-form, nó tự động đọc metadata của trường để render đúng UI (tiền tệ) và tự động ẩn/hiển thị/khóa dựa trên quyền FLS của user đó mà không cần viết 1 dòng code logic nào.

**❌ Tại sao đáp án sai:**
> **A.** lightning-input bắt buộc phải tự code kiểm tra quyền FLS, không tự động bảo mật theo metadata được.
> **B.** lightning-formatted-number chỉ để hiển thị dạng read-only, không cho phép người dùng nhập liệu.
> **D.** Thẻ <lightning-input-currency> là thẻ không tồn tại trong bộ component chuẩn của Salesforce LWC.

**💡 Từ khóa ghi nhớ:** `LWC Form tự động FLS + Tự động định dạng -> Cứ lightning-input-field mà vã!`

---

## Câu 58

**🔵 Which two statements are acceptable for a developer to use inside procedural loops? (Choose two.)**

- **A.** delete contactList; ❌
- **B.** contactList.remove(i); ✅
- **C.** Contact con = new Contact(); ✅
- **D.** Account a = [SELECT Id, Name FROM Account WHERE Id = :con.AccountId LIMIT 1]; ❌

**📝 Dịch tiếng Việt:**
> Hai câu lệnh nào sau đây là hoàn toàn chấp nhận được khi viết bên trong vòng lặp (loop) trong Apex? (Chọn 2)

**💬 Giải thích gốc (English):**
> Options B and C are acceptable inside procedural loops, while options A and D are not recommended due to potential issues and governor limit concerns.

**✅ Tại sao đáp án đúng:**
> B: Phương thức remove() trên List chỉ thao tác trên bộ nhớ RAM nên chạy cực nhanh trong vòng lặp. C: Khởi tạo instance mới của sObject bằng từ khóa 'new' trong RAM cũng hoàn toàn vô hại và thường xuyên được sử dụng.

**❌ Tại sao đáp án sai:**
> **A.** delete contactList thực hiện lệnh DML xóa dữ liệu, cấm nhét vào vòng lặp vì sẽ nhanh chóng làm sập giới hạn 150 DML.
> **D.** Viết câu truy vấn SOQL [SELECT...] trong vòng lặp là tội ác lớn nhất vì sẽ chạm giới hạn 100 SOQL cực nhanh.

**💡 Từ khóa ghi nhớ:** `Governor Limit: Cấm tuyệt đối SOQL Query và DML Statement nằm trong vòng lặp (For/While).`

---

## Câu 59

**🔵 A developer needs to display all of the available fields for an object. In which two ways can the developer retrieve the available fields if the variable myObject represents the name of the object? (Choose two.)**

- **A.** Use myObject.sObjectType.getDescribe().fieldSet() to return a set of fields. ❌
- **B.** Use mySObject.myObject.fields.getMap() to return a map of fields. ❌
- **C.** Use Schema.describeSObjects(new String[]{myObject})[0].fields.getMap() to return a map of fields. ✅
- **D.** Use getGlobalDescribe().get(myObject).getDescribe().fields.getMap() to return a map of fields. ✅

**📝 Dịch tiếng Việt:**
> Để lấy danh sách tất cả các trường khả dụng của một đối tượng có tên nằm trong biến chuỗi myObject, hai cách nào sau đây giúp lập trình viên lấy được Map các trường? (Chọn 2)

**💬 Giải thích gốc (English):**
> Options C and D are the correct ways to retrieve the available fields for an object using the variable myObject.

**✅ Tại sao đáp án đúng:**
> C: Schema.describeSObjects() nhận vào mảng tên object và trả về mô tả chi tiết, từ đó gọi fields.getMap() để lấy map các trường. D: Schema.getGlobalDescribe() trả về map toàn bộ object trong Org, lấy theo tên biến myObject, describe nó rồi lấy map các trường.

**❌ Tại sao đáp án sai:**
> **A.** Biến chuỗi String (myObject) không có thuộc tính con '.sObjectType' để gọi trực tiếp như vậy.
> **B.** Cú pháp mySObject.myObject.fields... là hoàn toàn sai và không biên dịch được.

**💡 Từ khóa ghi nhớ:** `Lấy Map trường động bằng String tên Object: GlobalDescribe hoặc describeSObjects.`

---

## Câu 60

**🔵 A newly hired developer discovers that there are multiple triggers on the case object. What should the developer consider when working with triggers?**

- **A.** Developers must dictate the order of trigger execution. ❌
- **B.** Trigger execution order is based on creation date and time. ❌
- **C.** Unit tests must specify the trigger being tested. ❌
- **D.** Trigger execution order is not guaranteed for the same sObject. ✅

**📝 Dịch tiếng Việt:**
> Một lập trình viên mới phát hiện ra có rất nhiều trigger cùng tồn tại trên đối tượng Case. Lập trình viên nên lưu ý điều gì về các trigger này?

**💬 Giải thích gốc (English):**
> When working with triggers, it's essential to be aware that the order of execution of multiple triggers on the same sObject is not guaranteed. Salesforce executes triggers for the same sObject in an undetermined order. This means that if there are multiple triggers on the Case object, the developer cannot rely on a specific sequence of trigger execution.

**✅ Tại sao đáp án đúng:**
> Quy tắc vàng của Salesforce: Thứ tự thực thi của các trigger cùng viết trên một đối tượng (sObject) là KHÔNG ĐƯỢC ĐẢM BẢO (D). Hệ thống thích chạy thằng nào trước là quyền của nó.

**❌ Tại sao đáp án sai:**
> **A.** Lập trình viên không thể tự định đoạt thứ tự chạy nếu viết nhiều file trigger riêng lẻ.
> **B.** Thứ tự chạy không hề phụ thuộc vào ngày giờ tạo của trigger.
> **C.** Unit test chạy tất cả các trigger nổ khi có DML, không cần và không thể chỉ định đích danh trigger nào chạy.

**💡 Từ khóa ghi nhớ:** `One Trigger Per Object: Viết nhiều trigger trên 1 Object -> Thứ tự chạy ngẫu nhiên, dễ lỗi logic!`

---

## Câu 61

**🔵 Universal Containers has a support process that allows users to request support from its engineering team using a custom object, Engineering_Support__c. Users should be able to associate multiple Engineering_Support__c records to a single Opportunity record. Additionally, aggregate information about the Engineering_Support__c records should be shown on the Opportunity record. What should a developer implement to support these requirements?**

- **A.** Master-detail field from Opportunity to Engineering_Support__c ❌
- **B.** Lookup field from Engineering_Support__c to Opportunity ❌
- **C.** Lookup field from Opportunity to Engineering_Support__c ❌
- **D.** Master-detail field from Engineering_Support__c to Opportunity ✅

**📝 Dịch tiếng Việt:**
> Universal Containers có một quy trình hỗ trợ cho phép người dùng yêu cầu sự giúp đỡ từ đội kỹ thuật thông qua một custom object tên là Engineering_Support__c. Người dùng phải có khả năng liên kết nhiều bản ghi Engineering_Support__c với một bản ghi Opportunity duy nhất. Đồng thời, thông tin tổng hợp (aggregate information) của các bản ghi Engineering_Support__c phải được hiển thị trên Opportunity. Developer nên hiện thực hóa yêu cầu này như thế nào?

**💬 Giải thích gốc (English):**
> Implementing a Master-detail relationship from the Engineering_Support__c custom object to the Opportunity standard object ensures that the support records are tightly associated with specific Opportunities. This relationship allows for automatic aggregation of information and cascading behavior, which is essential for displaying aggregate data on the Opportunity record.

**✅ Tại sao đáp án đúng:**
> Để hiển thị thông tin tổng hợp (như Sum, Count, Min, Max) của các bản ghi con lên bản ghi cha mà không cần viết một dòng code nào, giải pháp tối ưu và duy nhất là dùng trường Roll-up Summary. Mà điều kiện tiên quyết để tạo được Roll-up Summary field trên Opportunity là Opportunity phải đóng vai trò là Master trong mối quan hệ Master-Detail. Do đó, ta phải tạo một trường Master-Detail trên đối tượng con Engineering_Support__c trỏ về đối tượng cha Opportunity (D).

**❌ Tại sao đáp án sai:**
> **A.** Tạo trường Master-Detail từ Opportunity sang Engineering_Support__c sẽ biến Opportunity thành con và Engineering_Support__c thành cha. Lúc này, thông tin tổng hợp sẽ hiển thị ở con chứ cha chẳng được xơ múi gì, sai logic nghiêm trọng!
> **B.** Mối quan hệ Lookup không hỗ trợ tính năng Roll-up Summary. Muốn tính tổng hợp qua Lookup là phải viết Apex Trigger cồng kềnh, mệt người.
> **C.** Vừa sai chiều quan hệ (trỏ từ cha sang con), vừa dùng Lookup không hỗ trợ Roll-up Summary, cook gấp!

**💡 Từ khóa ghi nhớ:** `Thấy 'aggregate information' (thông tin tổng hợp) trên Cha -> Cần dùng Roll-up Summary -> Auto chọn Master-Detail từ Con trỏ về Cha!`

---

## Câu 62

**🔵 When a user edits the Postal Code on an Account, a custom Account text field named 'Timezone' must be updated based on the values in another custom object called PostalCodeToTimezone__c. What is the optimal way to implement this feature?**

- **A.** Build an account assignment rule. ❌
- **B.** Build a flow with Flow Builder. ✅
- **C.** Create an account approval process. ❌
- **D.** Create a formula field. ❌

**📝 Dịch tiếng Việt:**
> Khi một người dùng chỉnh sửa trường Postal Code trên Account, một trường text tùy chỉnh tên 'Timezone' trên Account phải được cập nhật tự động dựa trên giá trị trong một custom object khác tên là PostalCodeToTimezone__c. Cách tối ưu nhất để hiện thực hóa tính năng này là gì?

**💬 Giải thích gốc (English):**
> The flow can then perform actions such as querying the PostalCodeToTimezone__c custom object, retrieving the relevant timezone value, and updating the ‘Timezone’ field on the Account.
> Formula fields are used to calculate values based on other fields on the same object or related objects, but they cannot perform lookups to other custom objects.

**✅ Tại sao đáp án đúng:**
> Flow Builder (B) là 'ông trùm' tự động hóa low-code của Salesforce hiện tại! Khi Postal Code trên Account thay đổi, Record-Triggered Flow sẽ tự động kích hoạt, dùng phần tử Get Records để tra cứu (lookup) sang bảng độc lập PostalCodeToTimezone__c rồi lấy giá trị Timezone cập nhật lại cho Account. Vừa mượt mà, vừa an toàn lại không tốn một dòng code.

**❌ Tại sao đáp án sai:**
> **A.** Account Assignment Rule chỉ dùng để tự động gán chủ sở hữu (Owner) hoặc phân vùng Territory cho Account dựa trên các tiêu chí địa lý, hoàn toàn không có cửa đi tra cứu bảng khác để update text field.
> **C.** Approval Process là quy trình phê duyệt (duyệt lương, duyệt nghỉ phép...), đem đi áp dụng cho một vụ tự động cập nhật ngầm thế này là cồng kềnh quá mức cần thiết.
> **D.** Formula field (trường công thức) chỉ có thể tham chiếu trực tiếp đến các Object cha có mối quan hệ trực tiếp (Lookup/Master-Detail). Bảng PostalCodeToTimezone__c là một object độc lập, không có quan hệ trực tiếp nên Formula field hoàn toàn bất lực, cook!

**💡 Từ khóa ghi nhớ:** `Cập nhật field cần tra cứu (Get Records) từ một Object độc lập không có quan hệ trực tiếp -> Flow Builder là chân ái!`

---

## Câu 63

**🔵 A team of many developers work in their own individual orgs that have the same configuration as the production org. Which type of org is best suited for this scenario?**

- **A.** Developer Sandbox ✅
- **B.** Developer Edition ❌
- **C.** Full Sandbox ❌
- **D.** Partner Developer Edition ❌

**📝 Dịch tiếng Việt:**
> Một đội ngũ gồm nhiều lập trình viên làm việc trên các org cá nhân của riêng họ nhưng phải có cấu hình (metadata) giống hệt với production org. Loại org nào phù hợp nhất cho kịch bản này?

**💬 Giải thích gốc (English):**
> A Developer Sandbox is a copy of the production org with the same configuration and data. Each developer can have their own Developer Sandbox, which allows them to work independently without interfering with each other's work.

**✅ Tại sao đáp án đúng:**
> Developer Sandbox (A) sinh ra là để dành cho các cá nhân dev 'quậy phá'. Nó sao chép toàn bộ cấu hình (metadata) từ Production, hoàn toàn miễn phí, khởi tạo cực nhanh và cô lập hoàn toàn giúp dev tha hồ viết code, thử nghiệm mà không sợ đụng chạm hay ảnh hưởng đến tiến độ của các dev khác.

**❌ Tại sao đáp án sai:**
> **B.** Developer Edition là một org cá nhân trống rỗng hoàn toàn độc lập, không được liên kết hay tự động sao chép cấu hình từ Production org của khách hàng. Dùng cái này là dev phải tự tay import metadata bằng cơm, siêu gà!
> **C.** Full Sandbox copy toàn bộ dữ liệu thật lẫn cấu hình của Production. Nó cực kỳ đắt đỏ và thời gian refresh rất lâu (thường là 29 ngày). Không ai đi cấp Full Sandbox cho từng dev để code lẻ tẻ cả, quá lãng phí tài nguyên!
> **D.** Partner Developer Edition dành cho các đối tác ISV để build package thương mại, tuy có giới hạn tài nguyên lớn hơn Developer Edition thông thường nhưng nó vẫn không tự động đồng bộ cấu hình từ Production org của khách hàng, cook!

**💡 Từ khóa ghi nhớ:** `Org cá nhân cho Dev + Cấu hình giống Prod = Developer Sandbox. Chạy nhanh, miễn phí, an toàn!`

---

## Câu 64

**🔵 Universal Containers uses Service Cloud with a custom field, Stage__c, on the Case object. Management wants to send a follow-up email reminder 6 hours after the Stage__c field is set to 'Waiting on Customer'. The Salesforce Administrator wants to ensure the solution used is bulk safe. Which automation tool should a developer recommend to meet these business requirements? (Choose two)**

- **A.** Record-Triggered Flow ✅
- **B.** Entitlement Process ❌
- **C.** Einstein Next Best Action ❌
- **D.** Scheduled Flow ✅

**📝 Dịch tiếng Việt:**
> Universal Containers sử dụng Service Cloud với một custom field tên là Stage__c trên Case object. Ban quản lý muốn tự động gửi một email nhắc nhở sau 6 giờ kể từ khi trường Stage__c chuyển sang giá trị 'Waiting on Customer'. Salesforce Administrator muốn đảm bảo giải pháp này phải an toàn khi xử lý hàng loạt (bulk safe). Công cụ tự động hóa nào lập trình viên nên khuyến nghị? (Chọn hai)

**💬 Giải thích gốc (English):**
> A Record-Triggered Flow can be used to detect when the Stage__c field is updated to ‘Waiting on Customer’. Then, a Scheduled Flow can be set to execute 6 hours later to send the follow-up email.

**✅ Tại sao đáp án đúng:**
> Record-Triggered Flow (A) hỗ trợ tính năng Scheduled Paths cực kỳ mạnh mẽ, cho phép lên lịch thực hiện hành động gửi email sau đúng 6 giờ kể từ khi bản ghi thỏa mãn điều kiện, cơ chế này cực kỳ tối ưu và an toàn khi xử lý hàng loạt (bulk safe). Đồng thời, Scheduled Flow (D) chạy theo lịch định kỳ cũng là một giải pháp bulk-safe cực tốt, nó có thể được lên lịch quét định kỳ hàng ngày để tìm các Case có trạng thái 'Waiting on Customer' quá 6 giờ và gửi email hàng loạt.

**❌ Tại sao đáp án sai:**
> **B.** Entitlement Process dùng để quản lý SLA và Milestone của Case. Dù nó có thể gửi mail nhưng cấu hình của nó rất phức tạp, nặng nề và không chuyên dụng cho một yêu cầu gửi mail nhắc nhở đơn giản thế này.
> **C.** Einstein Next Best Action chỉ dùng để hiển thị các gợi ý/hành động tiếp theo cho nhân viên hỗ trợ xem trực tiếp trên màn hình, hoàn toàn không phải công cụ tự động gửi email chạy ngầm.

**💡 Từ khóa ghi nhớ:** `Tự động hóa theo thời gian (Time-dependent) + Không code + An toàn hàng loạt = Scheduled Path trong Flow hoặc Scheduled Flow!`

---

## Câu 65

**🔵 A developer observes that an Apex test method fails in the Sandbox. To identify the issue, the developer copies the code inside the test method and executes it via the Execute Anonymous tool in the Developer Console. The code then executes with no exceptions or errors. Why did the test method fail in the sandbox and pass in the Developer Console?**

- **A.** The test method has a syntax error in the code. ❌
- **B.** The test method does not use System.runAs to execute as a specific user. ❌
- **C.** The test method is calling an @future method. ❌
- **D.** The test method relies on existing data in the sandbox. ✅

**📝 Dịch tiếng Việt:**
> Developer phát hiện một Apex test method bị FAIL trong Sandbox. Để tìm lỗi, anh ta copy toàn bộ code bên trong test method đó rồi chạy bằng công cụ Execute Anonymous trong Developer Console. Kỳ lạ thay, code chạy mượt mà, không hề xảy ra lỗi hay exception nào. Tại sao test method thì FAIL mà Execute Anonymous lại chạy thành công?

**💬 Giải thích gốc (English):**
> When running the same code in the Execute Anonymous tool in the Developer Console, it executes within the current user's context and can access the existing data, which might result in successful execution.

**✅ Tại sao đáp án đúng:**
> Khi chạy Unit Test, Salesforce áp dụng cơ chế cô lập dữ liệu cực kỳ nghiêm ngặt (mặc định SeeAllData=false). Class test sẽ không nhìn thấy bất kỳ bản ghi thật nào trong Sandbox mà bắt buộc phải tự tạo dữ liệu giả lập (test data). Trong khi đó, Execute Anonymous lại có quyền truy cập trực tiếp vào toàn bộ dữ liệu thật của Org. Sự khác biệt này chứng tỏ code test đã lười tạo dữ liệu giả lập mà lại đi phụ thuộc vào dữ liệu thật có sẵn trong Sandbox (D). Khi chạy test thật, hệ thống không tìm thấy dữ liệu nên bị FAIL!

**❌ Tại sao đáp án sai:**
> **A.** If there's a syntax error, the compiler stops it at the door. Cả Test Class và Execute Anonymous đều không thể compile hay chạy được chứ đừng nói là pass.
> **B.** System.runAs dùng để giả lập quyền hạn của một User cụ thể trong unit test, việc thiếu nó chỉ làm sai lệch logic phân quyền chứ không tạo ra sự khác biệt về khả năng truy cập dữ liệu giữa Test và Anonymous.
> **C.** Gọi phương thức @future trong unit test chỉ cần bọc trong Test.startTest() và Test.stopTest(). Nếu viết sai quy tắc này thì chạy ở Execute Anonymous hay Test Class cũng đều oẳng như nhau.

**💡 Từ khóa ghi nhớ:** `Test FAIL nhưng Execute Anonymous PASS -> Chắc chắn do lười tạo dữ liệu test, code bị phụ thuộc vào dữ liệu thật trong Org (Data Isolation)!`

---

## Câu 66

**🔵 A developer is writing tests for a class and needs to insert records to validate functionality. Which annotation method should be used to create records for every method in the test class?**

- **A.** @StartTest ❌
- **B.** @PreTest ❌
- **C.** @TestSetup ✅
- **D.** @isTest(SeeAllData=true) ❌

**📝 Dịch tiếng Việt:**
> Developer đang viết test cho một class và cần insert các bản ghi để kiểm tra tính năng. Annotation nào nên được sử dụng để tạo dữ liệu dùng chung cho tất cả các test method trong class test đó?

**💬 Giải thích gốc (English):**
> @TestSetup annotation
> Can create common test data once, which will be available for all test methods in the test class. This helps reduce duplicate code and ensures that the test data is consistent across all test methods.

**✅ Tại sao đáp án đúng:**
> @TestSetup (C) is the gold standard annotation to create common test data. Nó sẽ chạy duy nhất một lần trước khi bất kỳ test method nào trong class được thực thi. Sau mỗi test method, trạng thái dữ liệu sẽ tự động rollback về ban đầu, giúp tiết kiệm thời gian chạy test cực kỳ nhiều so với việc tạo dữ liệu thủ công ở từng method.

**❌ Tại sao đáp án sai:**
> **A.** @StartTest là cái tên tự chế, không hề tồn tại trong Salesforce Apex. Cú pháp chuẩn chỉ là Test.startTest() (phương thức chứ không phải annotation).
> **B.** @PreTest cũng là một annotation 'pha kè', gà mờ mới chọn.
> **D.** @isTest(SeeAllData=true) cho phép test class nhìn thấy dữ liệu thật của hệ thống. Đây là một 'bad practice' cực kỳ nguy hiểm, làm test class dễ bị tạch khi dữ liệu thật thay đổi, và nó cũng không phải là phương pháp tự tay tạo dữ liệu test mẫu.

**💡 Từ khóa ghi nhớ:** `Dữ liệu test dùng chung cho toàn bộ Class -> Khắc cốt ghi tâm `@TestSetup`!`

---

## Câu 67

**🔵 In the following example, which sharing context myMethod execute when it is invoked?
public Class myClass {
public void myMethod() { /* implementation */ }
}**

- **A.** Sharing rules will not be enforced for the running user. ✅
- **B.** Sharing rules will be inherited from the calling context. ❌
- **C.** Sharing rules will be enforced for the running user. ❌
- **D.** Sharing rules will be enforced by the instantiating class. ❌

**📝 Dịch tiếng Việt:**
> Trong ví dụ trên, phương thức myMethod sẽ thực thi trong ngữ cảnh chia sẻ (sharing context) nào khi nó được gọi?

**💬 Giải thích gốc (English):**
> Since the class myClass does not explicitly specify a sharing context (using with sharing or without sharing), it defaults to “without sharing”. This means that the method myMethod will execute without enforcing the sharing rules of the running user.

**✅ Tại sao đáp án đúng:**
> Ủa alo? Lại một pha ra đề hại não của Salesforce! Định nghĩa một class không có từ khóa 'with sharing' hay 'without sharing' thì về mặt kỹ thuật, nó sẽ kế thừa ngữ cảnh từ lớp gọi nó (calling context). Tuy nhiên, Salesforce lại thích chấm đáp án A (Sharing rules sẽ không được áp dụng cho running user) là ĐÚNG! Tại sao? Vì mặc định nếu class này là điểm xuất phát (entry point) chạy độc lập (như khi gọi từ trigger hoặc Anonymous Block) mà không qua class nào khác gọi, nó sẽ chạy ở System Mode (tức là không áp dụng Sharing Rules). Đi thi thì cứ nhắm mắt chọn A để có điểm tuyệt đối nhé các homie!

**❌ Tại sao đáp án sai:**
> **B.** Mặc dù về mặt lý thuyết Apex, omit từ khóa sẽ kế thừa ngữ cảnh của calling class, nhưng trong hệ thống đề thi PD1 câu này, Salesforce lại coi phát biểu kế thừa này không phải đáp án đúng chính thức, ra rìa!
> **C.** Phát biểu này chỉ đúng khi class được khai báo tường minh bằng từ khóa 'with sharing'.
> **D.** Quyền sharing không bị kiểm soát bởi class thực hiện new (instantiating class) nếu nó không trực tiếp gọi phương thức.

**💡 Từ khóa ghi nhớ:** `Đề thi hỏi Class mặc định không ghi từ khóa chạy ở chế độ nào -> Chọn ngay: 'Sharing rules will not be enforced' (Không áp dụng Sharing Rules)!`

---

## Câu 68

**🔵 A developer created a new after insert trigger on the Lead object that creates Task records for each Lead. After deploying to production, an existing outside integration that inserts Lead records in batches to Salesforce is occasionally reporting total batch failures being caused by the Task insert statement. This causes the integration process in the outside system to stop, requiring a manual restart. 	Which change should the developer make to allow the integration to continue when some records in a batch cause failures due to the Task insert statement, so that manual restarts are not needed?**

- **A.** Deactivate the trigger before the integration runs. ❌
- **B.** Use a try-catch block after the insert statement. ❌
- **C.** Use the Database method with allOrNone set to false. ✅
- **D.** Remove the Apex class from the integration user’s profile. ❌

**📝 Dịch tiếng Việt:**
> Developer viết một after insert trigger trên Lead để tự động tạo Task cho mỗi Lead. Khi deploy lên Production, một hệ thống tích hợp bên ngoài nạp Lead theo lô (batch) thỉnh thoảng báo lỗi hỏng cả lô do câu lệnh insert Task thất bại. Việc này làm dừng tiến trình của hệ thống ngoài và yêu cầu khởi động lại thủ công. Thay đổi nào giúp tiến trình tiếp tục chạy mượt mà khi một vài bản ghi trong lô bị lỗi do insert Task mà không cần restart thủ công?

**💬 Giải thích gốc (English):**
> When using the Database.insert() method with allOrNone set to false, if there are any errors during the insert operation (such as validation rule failures or triggers that cause an exception), the successful records will be committed, and the failed records will generate errors but won't cause the entire batch to fail. This way, the integration process will continue without requiring a manual restart.

**✅ Tại sao đáp án đúng:**
> Khi dùng DML thông thường (như insert tasks;), chỉ cần 1 bản ghi trong lô bị lỗi là Salesforce sẽ kích hoạt cơ chế rollback, làm sập cả lô (all-or-none = true mặc định) và ném ra unhandled exception làm dừng hệ thống tích hợp ngoài. Giải pháp tối ưu là dùng phương thức Database.insert(tasks, false) (C) với tham số allOrNone = false. Khi đó, các bản ghi hợp lệ vẫn được insert bình thường, bản ghi lỗi sẽ bị bỏ qua và ghi nhận kết quả vào danh sách SaveResult để hệ thống ngoài tự xử lý sau mà không làm sập cả transaction.

**❌ Tại sao đáp án sai:**
> **A.** Deactivate trigger là giải pháp trốn tránh trách nhiệm, làm mất luôn tính năng tạo Task tự động vô cùng quan trọng của hệ thống.
> **B.** Dùng khối try-catch bọc quanh câu lệnh insert thông thường chỉ giúp bắt lỗi chứ không cứu vãn được các bản ghi khác trong lô, vì DML chuẩn đã rollback là rollback sạch sành sanh cả lô rồi.
> **D.** Xóa class Apex khỏi profile của user tích hợp sẽ khiến 100% các cuộc gọi tích hợp bị lỗi phân quyền, tự hủy cực mạnh!

**💡 Từ khóa ghi nhớ:** `Muốn cứu những thằng đúng, bỏ qua những thằng sai trong lô -> Dùng ngay Database.insert(records, false) (allOrNone = false)!`

---

## Câu 69

**🔵 A developer needs to join data received from an integration with an external system with parent records in Salesforce. The data set does not contain the Salesforce IDs of the parent records, but it does have a foreign key attribute that can be used to identify the parent. Which action will allow the developer to relate records in the data model without knowing the Salesforce ID?**

- **A.** Create and populate a custom field on the parent object marked as Unique. ❌
- **B.** Create a custom field on the child object of type External Relationship. ❌
- **C.** Create and populate a custom field on the parent object marked as an External ID. ✅
- **D.** Create a custom field on the child object of type Foreign Key. ❌

**📝 Dịch tiếng Việt:**
> Developer cần liên kết dữ liệu nhận được từ hệ thống bên ngoài với các bản ghi cha (parent records) trong Salesforce. Dữ liệu nhận về không hề có Salesforce ID của bản ghi cha, nhưng lại có một trường khóa ngoại (foreign key) từ hệ thống ngoài để định danh. Hành động nào giúp liên kết các bản ghi này mà không cần biết Salesforce ID?

**💬 Giải thích gốc (English):**
> An External ID field is used to store unique identifiers from an external system and allows the developer to use this external identifier to match records in Salesforce with records in the external system.

**✅ Tại sao đáp án đúng:**
> Trường External ID (C) sinh ra chính là để giải quyết kiếp nạn này! Bằng cách tạo một custom field trên object cha, đánh dấu nó là External ID và lưu mã định danh từ hệ thống ngoài vào đó. Khi thực hiện nạp dữ liệu cho con, Salesforce cho phép chúng ta tham chiếu trực tiếp đến bản ghi cha thông qua External ID này mà không cần biết Salesforce ID 18 ký tự là gì. Quá xịn sò và đúng chuẩn tích hợp!

**❌ Tại sao đáp án sai:**
> **A.** Đánh dấu Unique chỉ giúp chống trùng lặp dữ liệu trên Object cha chứ không có tính năng giúp Salesforce hiểu để tự động mapping mối quan hệ khi thực hiện nạp dữ liệu (Upsert/Insert), cook!
> **B.** Tạo trường kiểu External Relationship trên object con chỉ dùng cho External Objects (khi kết nối qua Salesforce Connect), không áp dụng cho các custom/standard object thông thường của Salesforce.
> **D.** Trong Salesforce không có kiểu dữ liệu nào tên là 'Foreign Key' để tạo trực tiếp cả, chỉ có Lookup hoặc Master-Detail thôi.

**💡 Từ khóa ghi nhớ:** `Liên kết dữ liệu hệ thống ngoài + Không có Salesforce ID -> Auto gọi tên External ID!`

---

## Câu 70

**🔵 A developer creates a new Apex trigger with a helper class, and writes a test class that only exercises 95% coverage of the new Apex helper class. Change Set deployment to production fails with the test coverage warning: Test coverage of selected Apex Trigger is 0%, at least 1% test coverage is required. What should the developer do to successfully deploy the new Apex trigger and helper class?**

- **A.** Increase the test class coverage on the helper class. ❌
- **B.** Remove the failing test methods from the test class. ❌
- **C.** Run the tests using the 'Run All Tests' method. ❌
- **D.** Create a test class and methods to cover the Apex trigger. ✅

**📝 Dịch tiếng Việt:**
> Developer tạo một Apex trigger mới cùng với một helper class đi kèm, sau đó viết test class giúp phủ sóng (coverage) 95% dòng code của helper class. Tuy nhiên, khi deploy bằng Change Set lên Production thì bị từ chối thẳng thừng với cảnh báo: 'Test coverage của Apex Trigger là 0%, yêu cầu tối thiểu phải đạt 1%'. Developer phải làm gì để deploy thành công?

**💬 Giải thích gốc (English):**
> To successfully deploy the new Apex trigger and helper class, the developer needs to create a test class that provides test coverage for both the trigger and the helper class.

**✅ Tại sao đáp án đúng:**
> Luật thép của Salesforce khi deploy lên Production: Tổng test coverage toàn hệ thống phải đạt tối thiểu 75%, helper class đạt 95% là quá ngon, NHƯNG riêng đối với Apex Trigger, mỗi trigger bắt buộc phải có test coverage lớn hơn 0% (tức là tối thiểu 1% - phải chạy qua trigger ít nhất 1 dòng) (D). Trigger của bạn đang bị 0% vì trong test class bạn chỉ trực tiếp gọi hàm của helper class mà quên thực hiện lệnh DML (như Insert, Update, Delete) trên sObject để kích hoạt trigger nổ. Bạn phải sửa test class để thực hiện hành động DML kích hoạt trigger.

**❌ Tại sao đáp án sai:**
> **A.** Tăng test coverage của helper class lên 100% cũng vô ích vì trigger vẫn đang nằm im thin thít với con số 0% tròn trĩnh.
> **B.** Xóa các test method bị lỗi không hề giúp tăng coverage cho trigger, chỉ tổ làm mất công test logic.
> **C.** Chạy 'Run All Tests' chỉ là bấm nút chạy lại đống test cũ trong hệ thống, nếu bạn chưa viết dòng code nào kích hoạt trigger chạy trong môi trường test thì kết quả vẫn là 0% thôi.

**💡 Từ khóa ghi nhớ:** `Điều kiện deploy Production: Tổng local tests >= 75% + Mọi Trigger bắt buộc coverage > 0% (phải gọi DML trong test để trigger nổ)!`

---

## Câu 71

**🔵 How many Accounts will be inserted by the following block of code?
for(Integer i = 0; i 500; i++){
Account a = new Account(Name = 'New Account ' + i);
insert a;
}**

- **A.** 100 ❌
- **B.** 150 ❌
- **C.** 0 ✅
- **D.** 500 ❌

**📝 Dịch tiếng Việt:**
> Có bao nhiêu bản ghi Account sẽ được insert thành công vào cơ sở dữ liệu sau khi chạy đoạn code trên?

**💬 Giải thích gốc (English):**
> DML Exception

**✅ Tại sao đáp án đúng:**
> Đáp án chắc chắn là 0 (C)! Tại sao? Bởi vì Salesforce giới hạn nghiêm ngặt tối đa 150 lệnh DML (DML statements) trong một transaction đồng bộ. Đoạn code này cố tình ném lệnh 'insert a;' vào bên trong vòng lặp For chạy tới 500 lần. Khi vòng lặp chạy đến lần thứ 151, Salesforce sẽ ngay lập tức 'tuýt còi' ném ra lỗi LimitException: Too many DML statements: 151 và dừng cuộc chơi lập tức. Vì tính chất nguyên tử (Atomicity) của transaction, toàn bộ 150 bản ghi đã insert thành công trước đó cũng sẽ bị rollback sạch sẽ như chưa từng tồn tại!

**❌ Tại sao đáp án sai:**
> **A.** Vượt giới hạn DML 150 sẽ gây ra rollback toàn bộ dữ liệu, không có chuyện insert thành công 100 bản ghi.
> **B.** Mặc dù 150 là giới hạn DML, nhưng do transaction mang tính nguyên tử, lỗi ở lần 151 làm toàn bộ 150 bản ghi trước bị xóa sạch.
> **D.** Không bao giờ đạt được con số 500 khi viết DML trong vòng lặp như thế này.

**💡 Từ khóa ghi nhớ:** `Nhét SOQL hoặc DML vào trong vòng lặp For -> 100% dính Limit Exception -> Kết quả rollback về 0 bản ghi!`

---

## Câu 72

**🔵 A developer needs to implement a custom SOAP Web Service that is used by an external Web Application. The developer chooses to Include helper methods that are not used by the Web Application in the implementation of the Web Service Class. Which code segment shows the correct declaration of the class and methods?**

- **A.** webservice class WebServiceClass {
  private Boolean helperMethod() { /*implementation ...*/ }
  global static String updateRecords() { /*implementation ...*/ }
} ❌
- **B.** global class WebServiceClass {
  private Boolean helperMethod() { /*implementation ...*/ }
  webservice static String updateRecords() { /*implementation ...*/ }
} ✅
- **C.** webservice class WebServiceClass {
  private Boolean helperMethod() { /*implementation ...*/ }
  webservice static String updateRecords() { /*implementation ...*/ }
} ❌
- **D.** global class WebServiceClass {
  private Boolean helperMethod() { /*implementation ...*/ }
  global String updateRecords() { /*implementation ...*/ }
} ❌

**📝 Dịch tiếng Việt:**
> Developer cần tạo một custom SOAP Web Service để ứng dụng web bên ngoài gọi vào. Lập trình viên muốn viết thêm các phương thức helper nội bộ không dùng cho bên ngoài. Khai báo class và method nào sau đây là đúng chuẩn?

**💬 Giải thích gốc (English):**
> The class must be declared as global to be accessible by external applications.
> The method that is exposed as a web service must be declared with the webservice keyword.

**✅ Tại sao đáp án đúng:**
> Bất kỳ class nào chứa phương thức khai báo từ khóa 'webservice' đều BẮT BUỘC phải là global class (để bên ngoài có thể truy cập). Phương thức API phơi ra cho bên ngoài gọi qua SOAP bắt buộc phải dùng từ khóa 'webservice static'. Các phương thức helper nội bộ không muốn lộ ra ngoài thì cứ khai báo 'private' bình thường. Do đó khai báo B là chuẩn nhất.

**❌ Tại sao đáp án sai:**
> **A.** Cú pháp 'webservice class' là sai bét, Apex không cho phép dùng từ khóa webservice cho phần định nghĩa class.
> **C.** Tương tự A, sai cú pháp khai báo class với 'webservice class'.
> **D.** Thiếu từ khóa 'webservice' và 'static' trên phương thức updateRecords(), làm cho hệ thống bên ngoài không thể nhận diện và gọi qua SOAP.

**💡 Từ khóa ghi nhớ:** `Quy tắc vàng SOAP trong Apex: Class bắt buộc GLOBAL, Method bắt buộc WEBSERVICE STATIC.`

---

## Câu 73

**🔵 A developer is asked to prevent anyone other than a user with Sales Manager profile from changing the Opportunity Status to Closed Lost if the lost reason is blank. Which automation allows the developer to satisfy this requirement in the most efficient manner?**

- **A.** An error condition formula on a validation rule on Opportunity ✅
- **B.** An Apex trigger on the Opportunity object ❌
- **C.** A record trigger flow on the Opportunity object ❌
- **D.** An approval process on the Opportunity object ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên được yêu cầu ngăn chặn bất kỳ ai (ngoại trừ user có Profile là Sales Manager) chuyển Opportunity Status sang 'Closed Lost' nếu trường lý do thất bại (Lost Reason) bị để trống. Công cụ tự động hóa nào giúp giải quyết yêu cầu này một cách hiệu quả nhất?

**💬 Giải thích gốc (English):**
> Using a validation rule is the most efficient way to enforce this requirement. The validation rule can be set up to check if the Opportunity Status is being changed to “Closed Lost” and if the “Lost Reason” field is blank.
> Here’s an example of how the validation rule might look:
> AND(
> ISPICKVAL(StageName, "Closed Lost"),
> ISBLANK(Lost_Reason__c),
> $Profile.Name <> "Sales Manager"
> )

**✅ Tại sao đáp án đúng:**
> Để thực hiện các nghiệp vụ ngăn chặn (prevent/block) lưu dữ liệu sai logic hoặc thiếu thông tin, Validation Rule (A) là giải pháp nhanh gọn lẹ, hiệu quả nhất! Viết một công thức kiểm tra điều kiện lỗi (error condition formula) trên Opportunity cực kỳ trực quan, hoàn toàn không cần code, dễ bảo trì và chạy cực nhanh ở tầng database trước khi lưu bản ghi.

**❌ Tại sao đáp án sai:**
> **B.** Apex Trigger làm được nhưng viết code chỉ để check trống một field thì quá phí phạm, tốn thời gian viết test class và deploy phức tạp, 'gà' vô cùng.
> **C.** Record-Triggered Flow cũng làm được (bằng Custom Error element) nhưng giống như cầm dao mổ trâu để giết gà, cồng kềnh hơn Validation Rule rất nhiều.
> **D.** Approval Process dùng để chạy quy trình phê duyệt nhiều bước, không liên quan gì đến việc tự động check dữ liệu khi lưu.

**💡 Từ khóa ghi nhớ:** `Thấy chữ 'Prevent' (Ngăn chặn) hoặc 'Validation' (Xác thực dữ liệu) -> Nghĩ ngay đến Validation Rule trước tiên!`

---

## Câu 74

**🔵 A developer needs to prevent the creation of Request records when certain conditions exist in the system. A RequestLogic class exists that checks the conditions. What is the correct implementation?**

- **A.** trigger RequestTrigger on Request(before insert){
if(RequestLogic.isValid(Request))
Request.addError('Your request cannot be created at this time.');
} ❌
- **B.** trigger RequestTrigger on Request(after insert){
if(RequestLogic.isValid(Request))
Request.addError('Your request cannot be created at this time.');
} ❌
- **C.** trigger RequestTrigger on Request(after insert){
RequestLogic.validateRecords(trigger.new)
} ❌
- **D.** trigger RequestTrigger on Request(before insert){
RequestLogic.validateRecords(trigger.new)
} ✅

**📝 Dịch tiếng Việt:**
> Developer cần ngăn chặn việc tạo bản ghi Request khi có một số điều kiện nhất định xảy ra trong hệ thống. Một class RequestLogic đã có sẵn hàm kiểm tra điều kiện. Khai báo nào sau đây là đúng chuẩn?

**💬 Giải thích gốc (English):**
> This implementation ensures that the validation logic is applied before the records are inserted into the database, allowing the trigger to prevent the creation of invalid records.

**✅ Tại sao đáp án đúng:**
> D đúng vì: 1. Để ngăn chặn việc tạo bản ghi (prevent creation), ta phải viết trigger sự kiện `before insert` để chặn trước khi dữ liệu được ghi xuống database. 2. Ta sử dụng `Trigger.new` truyền vào hàm xử lý của `RequestLogic` để kiểm tra và gọi hàm `addError()` trên từng bản ghi cụ thể có lỗi.

**❌ Tại sao đáp án sai:**
> **A.** Sai cú pháp vì dùng tên Object `Request` trực tiếp để gọi hàm và phương thức `addError()`. Phải gọi trên đối tượng cụ thể trong Trigger Context (ví dụ duyệt `Trigger.new`).
> **B.** Sai cả sự kiện `after insert` (bản ghi đã lưu tạm vào DB, không dùng để chặn insert được nữa) lẫn sai cú pháp khi gọi trên tên Object `Request`.
> **C.** Sai sự kiện vì dùng `after insert` để thực hiện việc ngăn chặn tạo bản ghi mới.

**💡 Từ khóa ghi nhớ:** `Ngăn chặn tạo bản ghi = Dùng BEFORE INSERT + Gọi handler truyền TRIGGER.NEW.`

---

## Câu 75

**🔵 Which annotation exposes an Apex class as a RESTful web service?**

- **A.** @RemoteAction ❌
- **B.** @RestResource ✅
- **C.** @HttpInvocable ❌
- **D.** @AuraEnabled ❌

**📝 Dịch tiếng Việt:**
> Annotation nào dùng để phơi (expose) một class Apex thành một RESTful web service?

**✅ Tại sao đáp án đúng:**
> @RestResource(urlMapping='/yourUrl/*') (B) là annotation chính chủ của Salesforce dùng để khai báo một class là REST API. Khi sử dụng annotation này, ta có thể định nghĩa các phương thức xử lý HTTP tương ứng như @HttpGet, @HttpPost, @HttpDelete cực kỳ đơn giản và mạnh mẽ.

**❌ Tại sao đáp án sai:**
> **A.** @RemoteAction dùng trong Visualforce để hỗ trợ cơ chế JavaScript Remoting (gọi hàm Apex từ JS trên trang VF), hoàn toàn không phải để tạo REST API cho hệ thống ngoài gọi vào.
> **C.** @HttpInvocable là một từ khóa hoàn toàn bịa đặt, không tồn tại trong vũ trụ Salesforce.
> **D.** @AuraEnabled dùng để phơi các phương thức Apex cho Lightning Component (Aura hoặc LWC) gọi từ phía client-side, chứ không có tuổi tạo RESTful web service cho hệ thống ngoài kết nối.

**💡 Từ khóa ghi nhớ:** `Tạo RESTful Web Service -> Nhắm mắt chọn @RestResource!`

---

## Câu 76

**🔵 A developer must troubleshoot to pinpoint the causes of performance issues when a custom page loads in their org. Which tool should the developer use to troubleshoot?**

- **A.** Visual Studio Code IDE ❌
- **B.** AppExchange ❌
- **C.** Developer Console ✅
- **D.** Setup Menu ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên phải tiến hành kiểm tra để xác định chính xác nguyên nhân gây ra các vấn đề về hiệu suất (performance issues) khi tải một custom page trong Org. Công cụ nào nên được sử dụng?

**💬 Giải thích gốc (English):**
> The Developer Console allows developers to set up debug logs for specific users or classes. These logs capture detailed information about the execution of Apex code, including any SOQL queries, DML operations, and method calls.

**✅ Tại sao đáp án đúng:**
> Developer Console (C) là 'vũ khí tối thượng' tích hợp sẵn trong Salesforce để phân tích hiệu năng. Với tính năng xem Log chi tiết và đặc biệt là tab Timeline / Performance Profiling, nó sẽ hiển thị trực quan dưới dạng biểu đồ xem câu query SOQL nào tốn bao nhiêu mili-giây, code Apex nào ngốn tài nguyên CPU nhất để bạn biết chính xác chỗ nào cần tối ưu hóa.

**❌ Tại sao đáp án sai:**
> **A.** Visual Studio Code IDE là môi trường viết code cực xịn, mặc dù có thể tải log về đọc nhưng không có giao diện phân tích Timeline đồ họa trực quan và tương tác thời gian thực tốt bằng Developer Console.
> **B.** AppExchange là cái 'chợ' ứng dụng để cài thêm app, chả liên quan gì đến việc debug hiệu năng của page tự viết cả.
> **D.** Setup Menu là nơi cấu hình hệ thống, không hỗ trợ công cụ phân tích sâu tiến trình thực thi của code, cook!

**💡 Từ khóa ghi nhớ:** `Gặp bài toán tìm nguyên nhân lỗi hiệu năng, soi log chạy ngầm -> Chọn ngay Developer Console!`

---

## Câu 77

**🔵 What should a developer use to implement an automatic Approval Process submission for Cases?**

- **A.** An Assignment Rule ❌
- **B.** Scheduled Apex ❌
- **C.** Process Builder ✅
- **D.** A Workflow Rule ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên nên sử dụng công cụ nào để tự động gửi yêu cầu phê duyệt (Approval Process submission) cho Case?

**💬 Giải thích gốc (English):**
> Process Builder is a declarative automation tool that allows you to create automated processes by defining a set of criteria and actions to be executed when those criteria are met.

**✅ Tại sao đáp án đúng:**
> Process Builder (C) (và hiện nay là Flow Builder) hỗ trợ hành động chuẩn 'Submit for Approval' cực kỳ trực quan. Chỉ cần định nghĩa điều kiện của Case, khi thỏa mãn là hệ thống tự động đẩy bản ghi vào quy trình phê duyệt mà không cần viết một dòng code nào. (Lưu ý: Mặc dù Process Builder đã bị Salesforce hạn chế phát triển để nhường sân chơi cho Flow, nhưng trong hệ thống đề thi PD1 hiện tại, nó vẫn được tính là đáp án đúng chính thức).

**❌ Tại sao đáp án sai:**
> **A.** Assignment Rule chỉ dùng để tự động phân chia Owner hoặc Queue cho Case/Lead dựa trên các tiêu chí lọc, hoàn toàn không có tính năng gửi phê duyệt.
> **B.** Scheduled Apex dùng để lên lịch chạy định kỳ một tác vụ, không mang tính tức thời khi Case thỏa mãn điều kiện như Process Builder.
> **D.** Workflow Rule đời cũ cực kỳ thô sơ, hoàn toàn không hỗ trợ hành động gửi bản ghi vào Approval Process.

**💡 Từ khóa ghi nhớ:** `Tự động gửi phê duyệt (Submit for Approval) không code -> Chọn Process Builder!`

---

## Câu 78

**🔵 What are two ways a developer can get the status of an enqueued job for a class that implements the queueable interface? (Choose two.)**

- **A.** View the Apex Jobs Page ✅
- **B.** View the Apex Status Page ❌
- **C.** Query the AsyncApexJob object ✅
- **D.** View the Apex Flex Queue ❌

**📝 Dịch tiếng Việt:**
> Hai cách nào giúp lập trình viên kiểm tra trạng thái của một job chạy ngầm (Queueable job) đã được đẩy vào hàng đợi? (Chọn hai)

**💬 Giải thích gốc (English):**
> The two correct ways for a developer to get the status of an enqueued job for a class that implements the Queueable interface are:
> A. View the Apex Jobs Page
> This page provides a list of all queued, in-progress, and completed jobs, including those that implement the Queueable interface.
> C. Query the AsyncApexJob object
> Developers can query the AsyncApexJob object to retrieve detailed information about the status of queued jobs. For example:
> AsyncApexJob job = [SELECT Id, Status, NumberOfErrors, JobItemsProcessed, TotalJobItems, CreatedBy.Email
> FROM AsyncApexJob
> WHERE Id = :jobId];

**✅ Tại sao đáp án đúng:**
> 1. Vào Setup -> tìm trang Apex Jobs (A). Đây là giao diện trực quan hiển thị toàn bộ trạng thái (Queued, Processing, Completed, Failed) của các tác vụ async. 
2. Thực hiện truy vấn SOQL trên đối tượng hệ thống AsyncApexJob (C) (ví dụ: SELECT Status FROM AsyncApexJob WHERE Id = :jobId) để lấy trạng thái động ngay trong code Apex.

**❌ Tại sao đáp án sai:**
> **B.** Giao diện quản lý hàng đợi Apex Flex Queue chỉ dùng để theo dõi và sắp xếp lại thứ tự ưu tiên của các Batch job đang ở trạng thái 'Holding', không dùng để xem trạng thái tổng quát của Queueable job.
> **D.** Salesforce làm gì có trang nào tên là 'Apex Status Page', đây hoàn toàn là một cái tên bịa đặt để đánh lừa kẻ lười học!

**💡 Từ khóa ghi nhớ:** `Kiểm tra trạng thái Async Job -> 1. Xem trang Apex Jobs trong Setup; 2. SOQL bảng AsyncApexJob.`

---

## Câu 79

**🔵 The Review_c object has a lookup relationship up to the Job_Application_c object. The Job_Application_c object has a master-detail relationship up to the Position_c object. The relationship field names are based on the auto-populated defaults. What is the recommended way to display field data from the related Position_c record on a Visualforce page for a single Review_c record?**

- **A.** Use the Standard Controller for Review_c and cross-object Formula Fields on the Position_c object to display Position_c data. ❌
- **B.** Use the Standard Controller for Job_Application_c and a Controller Extension to query for Position_c data. ✅
- **C.** Use the Standard Controller for Job_Application_c and cross-object Formula Fields on the Review_c object to display Position_c data. ❌
- **D.** Use the Standard Controller for Review_c and expression syntax in the Page to display related Position_c data through the Job_Application_c object. ❌

**📝 Dịch tiếng Việt:**
> Object Review__c có quan hệ lookup với Job_Application__c. Object Job_Application__c lại có quan hệ Master-Detail với Position__c. Tên các trường quan hệ được để mặc định. Phương pháp khuyến nghị để hiển thị dữ liệu từ bản ghi Position__c liên quan trên một trang Visualforce hiển thị một bản ghi Review__c là gì? (Ủa khoan, lại một pha 'bug game' từ hệ thống đáp án của Salesforce! Để thầy phân tích cái sự ảo ma này cho nghe.)

**✅ Tại sao đáp án đúng:**
> 1. Về mặt kỹ thuật thực tế (Best Practice): Cách tốt nhất và nhanh nhất là dùng Standard Controller cho Review__c và sử dụng cú pháp merge field đi xuyên mối quan hệ cha (cross-object) trực tiếp trên trang Visualforce: {!Review__c.Job_Application__r.Position__r.Name}. Không cần code, không cần extension! (Đáng lẽ đáp án D mới là chuẩn nhất).
2. Nhưng đi thi Salesforce PD1: Hệ thống lại chấm đáp án B là ĐÚNG! Đáp án này bắt chúng ta dùng Standard Controller của Job_Application__c và viết thêm một Controller Extension bằng Apex để truy vấn dữ liệu của Position__c. Mặc dù cồng kềnh và tốn code vô lý, nhưng đi thi thì cứ chọn B để được điểm tối đa nhé!

**❌ Tại sao đáp án sai:**
> **A.** Viết cross-object formula field trên Position__c là sai hướng hoàn toàn vì ta cần hiển thị dữ liệu lên trang của Review__c chứ không phải ngược lại.
> **C.** Dùng Standard Controller cho Job_Application__c kết hợp viết formula trên Review__c là một cách giải quyết chắp vá, đi đường vòng cực kỳ mệt mỏi.
> **D.** Mặc dù đây là cách làm tối ưu nhất thực tế bằng merge field trên Visualforce, nhưng Salesforce lại không đánh dấu nó là đáp án đúng chính thức trong kỳ thi, thế mới tài!

**💡 Từ khóa ghi nhớ:** `Đi thi gặp bài toán mối quan hệ Review__c -> Job_Application__c -> Position__c trên Visualforce -> Chọn đáp án dùng Standard Controller cho Job_Application__c + Controller Extension (Chọn B)!`

---

## Câu 80

**🔵 Refer to the following code snippet for an environment has more than 200 Accounts belonging to the ‘Technology’ industry:
for(Account thisAccount : [SELECT Id, Industry FROM Account LIMIT 150]){
if(thisAccount.Industry == 'Technology'){
thisAccount.Is_Tech__c = true;
}
update thisAccount;
}
When the code executes, what happens as a result of the Apex transaction?**

- **A.** The Apex transaction succeeds regardless of any uncaught exception and all processed accounts are updated. ✅
- **B.** If executed in a synchronous context, the Apex transaction is likely to fail by exceeding the DML governor limit. ❌
- **C.** The Apex transaction fails with the following message: SObject row was retrieved via SOQL without querying the requested field: Account.Is_Tech__c. ❌
- **D.** If executed in an asynchronous context, the Apex transaction is likely to fail by exceeding the DML governor limit. ❌

**📝 Dịch tiếng Việt:**
> Cho đoạn code thực thi trong môi trường có hơn 200 Account thuộc ngành 'Technology': [Đoạn code vòng lặp For]. Khi đoạn code này chạy, điều gì sẽ xảy ra với transaction Apex này?

**✅ Tại sao đáp án đúng:**
> 1. Về mặt lý thuyết đi thi: Đáp án đúng chính thức của Salesforce là A (The Apex transaction succeeds...). Đề bài muốn lập luận rằng vòng lặp chỉ lấy tối đa 150 bản ghi (LIMIT 150), nên transaction có thể thành công trọn vẹn.
2. Về mặt kỹ thuật thực tế (Sự thật trần trụi): Đoạn code này viết lệnh DML 'update thisAccount;' ngay bên TRONG vòng lặp For! Vòng lặp chạy 150 lần nghĩa là sẽ thực hiện tới 150 lệnh DML. Giới hạn DML tối đa của Salesforce trong một transaction đồng bộ là đúng 150 DML statements. Nếu trong hệ thống có bất kỳ một Automation nào khác (như Flow, Trigger) chạy kèm khi Account được update, nó sẽ kích hoạt thêm các lệnh DML phụ và làm transaction 'oẳng' lập tức vì vượt quá giới hạn 150 DML. Do đó, việc nhét DML vào For là một Bad Practice kinh điển! Nhưng đi thi thì nhớ chọn A để được ăn điểm nhé các đồng chí!

**❌ Tại sao đáp án sai:**
> **B.** Mặc dù thực tế rất dễ bị sập do Governor Limit, nhưng đề thi lại không coi đó là đáp án đúng chính thức.
> **D.** Asynchronous context có giới hạn DML statement vẫn là 150, nên nó vẫn oẳng bình thường.
> **C.** Lỗi thiếu query field chỉ xảy ra khi bạn cố tình ĐỌC một trường chưa được SELECT trong SOQL. Ở đây ta chỉ GHI giá trị (thisAccount.Is_Tech__c = true) nên không bao giờ dính lỗi này.

**💡 Từ khóa ghi nhớ:** `Đi thi gặp câu hỏi DML trong vòng lặp For giới hạn LIMIT 150 -> Nhắm mắt chọn đáp án A (Succeeds...)! Nhưng đi làm thực tế mà viết thế này là bị Senior gõ đầu ngay nhé!`

---

## Câu 81

**🔵 What is the data type returned by the following SOSL search?
[FIND 'Acme*' IN NAME FIELDS RETURNING Account, Opportunity];**

- **A.** List<List<Account>, List<Opportunity>> ❌
- **B.** Map<sObject, sObject> ❌
- **C.** List<List<sObject>> ✅
- **D.** Map<Id, sObject> ❌

**📝 Dịch tiếng Việt:**
> Kiểu dữ liệu nào được trả về bởi câu lệnh truy vấn SOSL tìm kiếm sau đây?
[FIND 'Acme*' IN NAME FIELDS RETURNING Account, Opportunity];

**💬 Giải thích gốc (English):**
> The data type List<List<sObject>> is correct because SOSL searches return a List of Lists of sObjects. In this case, the search query is returning a List of sObjects that include both Account and Opportunity records.

**✅ Tại sao đáp án đúng:**
> SOSL (FIND) là công cụ tối tân dùng để tìm kiếm chuỗi văn bản trên nhiều đối tượng (sObjects) cùng một lúc. Do kết quả trả về là một tập hợp các danh sách bản ghi của các Object khác nhau (ở đây là Account và Opportunity), nên kiểu dữ liệu trả về bắt buộc phải là một danh sách chứa các danh sách của sObject: List<List<sObject>> (C).

**❌ Tại sao đáp án sai:**
> **A.** Cú pháp khai báo kiểu dữ liệu lồng nhau kiểu List<List<Account>, List<Opportunity>> là hoàn toàn sai cú pháp trong Apex, compiler sẽ báo lỗi lập tức.
> **B.** SOSL không bao giờ trả về dữ liệu kiểu Map.
> **D.** SOSL trả về mảng danh sách nhiều đối tượng chứ không nhóm theo Id của bản ghi, cook!

**💡 Từ khóa ghi nhớ:** `Thần chú SOSL: Cứ thấy keyword FIND -> Chọn ngay kiểu dữ liệu trả về là List<List<sObject>>!`

---

## Câu 82

**🔵 A change set deployment from a sandbox to production fails due to a failure in a managed package unit test. The developer spoke with the managed package owner and they determined it is a false positive and can be ignored. What should the developer do to successfully deploy?**

- **A.** Select "Run local tests" to run all tests in the org that are not in the managed package. ✅
- **B.** Select "Fast Deploy" to run only the tests that are in the change set. ❌
- **C.** Select "Run local tests" to run only the tests that are in the change set. ❌
- **D.** Edit the managed package's unit test. ❌

**📝 Dịch tiếng Việt:**
> Quá trình deploy Change Set từ Sandbox lên Production bị thất bại do một test class nằm trong một Managed Package (gói quản lý của bên thứ ba) bị lỗi. Developer đã thảo luận với chủ sở hữu Managed Package và xác định đây chỉ là lỗi cảnh báo giả (false positive) và hoàn toàn có thể bỏ qua. Developer nên làm gì để deploy thành công?

**💬 Giải thích gốc (English):**
> By running only local tests, the deployment will bypass the managed package unit test that caused the failure and proceed with deploying the rest of the changes in the change set.

**✅ Tại sao đáp án đúng:**
> Khi deploy lên Production, Salesforce cho phép bạn chọn các cấp độ chạy test (Test Levels). Để bỏ qua các test class bị lỗi nằm trong các gói cài đặt ngoài (Managed Packages), lập trình viên chỉ cần chọn cấp độ test là 'Run local tests' (A). Cấp độ này sẽ chạy toàn bộ các test class do chính chúng ta viết trong Org (local) và bỏ qua hoàn toàn các test class đi kèm trong Managed Packages, giúp quá trình deploy vượt ải thành công.

**❌ Tại sao đáp án sai:**
> **B.** 'Fast Deploy' chỉ có hiệu lực khi bạn đã thực hiện validate Change Set đó thành công trước đó trong vòng 4 ngày, nó không giúp bỏ qua lỗi test class.
> **C.** 'Run local tests' là để chạy toàn bộ các test local trong Org của bạn chứ không phải chỉ chạy riêng các test class được đóng gói trong Change Set đang deploy.
> **D.** Code bên trong Managed Package đã bị đóng gói và khóa chặt, bạn hoàn toàn không có quyền chỉnh sửa hay sửa lỗi test class của họ.

**💡 Từ khóa ghi nhớ:** `Lỗi test của Managed Package cài ngoài cản đường deploy -> Chọn Test Level là 'Run local tests' để clear map!`

---

## Câu 83

**🔵 Which code displays the contents of a Visualforce page as a PDF?**

- **A.** <apex:page contentType="application/pdf"> ❌
- **B.** <apex:page renderAs="pdf"> ✅
- **C.** <apex:page renderAs="application/pdf"> ❌
- **D.** <apex:page contentType="pdf"> ❌

**📝 Dịch tiếng Việt:**
> Đoạn mã nào giúp hiển thị toàn bộ nội dung của một trang Visualforce dưới dạng một file PDF?

**💬 Giải thích gốc (English):**
> <apex:page renderAs="pdf">
> <!-- Contents of your Visualforce page -->
> </apex:page>

**✅ Tại sao đáp án đúng:**
> Thuộc tính renderAs='pdf' (B) đặt trong thẻ khai báo trang <apex:page> là cú pháp chuẩn và nhanh nhất của Salesforce. Hệ thống sẽ tự động sử dụng bộ chuyển đổi để render toàn bộ mã HTML/CSS của trang thành một file PDF xịn sò cho người dùng xem hoặc tải về.

**❌ Tại sao đáp án sai:**
> **A.** Thuộc tính contentType dùng để chỉ định kiểu định dạng file gửi về trình duyệt (như Excel, Word), hoàn toàn không có tính năng tự động vẽ và chuyển giao diện HTML sang định dạng PDF được.
> **D.** ContentType dùng cho việc download file, không dùng để render trang.
> **C.** Cú pháp giá trị của thuộc tính renderAs chỉ chấp nhận chuỗi ngắn gọn là 'pdf', viết rườm rà kiểu 'application/pdf' là sai cú pháp và trang sẽ báo lỗi ngay.

**💡 Từ khóa ghi nhớ:** `Visualforce sang PDF -> Dùng ngay công thức: renderAs='pdf'!`

---

## Câu 84

**🔵 What is a fundamental difference between a Master-Detail relationship and a Lookup relationship?**

- **A.** In a Master-Detail relationship, when a record of a master object is deleted, the detail records are not deleted. ❌
- **B.** In a Lookup relationship when the parent record is deleted, the child records are always deleted. ❌
- **C.** A Master-Detail relationship detail record inherits the sharing and security of its master record. ✅
- **D.** In a Lookup relationship, the field value is mandatory. ❌

**📝 Dịch tiếng Việt:**
> Sự khác biệt cơ bản nhất giữa mối quan hệ Master-Detail và mối quan hệ Lookup trong Salesforce là gì?

**💬 Giải thích gốc (English):**
> In a Master-Detail relationship, the detail record (child) is considered to be a subordinate of the master record (parent). The detail record inherits the sharing and security settings of its master record. This means that the detail record's access is determined by the access level of the master record.

**✅ Tại sao đáp án đúng:**
> Mối quan hệ Master-Detail là mối quan hệ 'cha con khâu khít / ký sinh'. Bản ghi con (Detail) bắt buộc phải kế thừa hoàn toàn cấu hình bảo mật Sharing và Security từ bản ghi cha (Master) (C). Nếu user không có quyền xem bản ghi cha, họ cũng không bao giờ thấy được bản ghi con.

**❌ Tại sao đáp án sai:**
> **A.** Trong quan hệ Master-Detail, khi bản ghi cha (Master) bị xóa thì các bản ghi con (Detail) liên quan cũng sẽ tự động bị xóa theo (Cascade delete) chứ không có chuyện trơ trơ ở lại.
> **B.** Trong quan hệ Lookup, khi bản ghi cha bị xóa, các bản ghi con mặc định sẽ chỉ bị xóa liên kết ở trường Lookup (trường trở thành null) chứ không bị xóa cả bản ghi con.
> **D.** Trong quan hệ Lookup, trường liên kết mặc định là tùy chọn (Optional - có thể để trống), chỉ có Master-Detail mới bắt buộc phải có giá trị.

**💡 Từ khóa ghi nhớ:** `Master-Detail = 'Sống chết có nhau, chung nhà chung chủ (Inherit Sharing)'. Lookup = 'Bạn bè xã giao, nhà ai nấy ở'.`

---

## Câu 85

**🔵 A developer wants multiple test classes to use the same set of test data. How should the developer create the test data?**

- **A.** Reference a test utility class in each test class. ✅
- **B.** Define variables for test records in each test class. ❌
- **C.** Create a Test Setup method for each test class. ❌
- **D.** Use the SeeAllData=true annotation in each test class. ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên muốn nhiều test class khác nhau có thể sử dụng chung một bộ dữ liệu test mẫu giống nhau. Lập trình viên nên tạo dữ liệu test này bằng cách nào?

**💬 Giải thích gốc (English):**
> Create a test utility class that contains methods to create and insert the common test data.
> Each test class can then reference this test utility class and call its methods to set up the required test data.

**✅ Tại sao đáp án đúng:**
> Cách làm chuẩn mực (Best Practice) nhất là tạo một Test Utility Class (A) chứa các hàm khởi tạo dữ liệu mẫu dạng public static (ví dụ: createTestAccounts()). Mỗi test class chỉ cần gọi hàm này để tự động sinh dữ liệu mẫu. Cách này giúp tái sử dụng code tối đa và cực kỳ dễ bảo trì khi cấu trúc database (Schema) thay đổi.

**❌ Tại sao đáp án sai:**
> **B.** Khai báo và tạo thủ công dữ liệu ở từng class gây lặp code nghiêm trọng, khi thêm trường bắt buộc mới là phải đi sửa từng class test, cực kỳ cồng kềnh và 'gà'.
> **C.** @TestSetup chỉ giúp tạo dữ liệu dùng chung trong nội bộ của duy nhất một class test đó thôi, các class test khác hoàn toàn không thể truy cập được dữ liệu này.
> **D.** Dùng SeeAllData=true là tối kỵ vì nó khiến test class truy cập dữ liệu thực tế của hệ thống. Nếu dữ liệu thật bị xóa hoặc sửa, test class sẽ bị tạch oan uổng, mất đi tính độc lập của unit test.

**💡 Từ khóa ghi nhớ:** `Dùng chung dữ liệu test giữa nhiều class khác nhau -> Tạo ngay một Test Utility Class!`

---

## Câu 86

**🔵 Which two statements are true about using the @testSetup annotation in an Apex test class? (Choose two.)**

- **A.** The @testSetup annotation cannot be used when the @isTest(SeeAllData=True) annotation is used. ✅
- **B.** Test data is inserted once for all test methods in a class. ✅
- **C.** Records created in the @testSetup method cannot be updates in individual test methods. ❌
- **D.** The @testSetup method is automatically executed before each test method in the test class is executed. ❌

**📝 Dịch tiếng Việt:**
> Hai phát biểu nào sau đây là đúng khi sử dụng annotation @testSetup trong một Apex test class? (Chọn hai)

**💬 Giải thích gốc (English):**
> The @testSetup annotation is used to set up test data that will be used by all test methods within a class. This helps to avoid redundant data creation and improves test efficiency.
> Test setup methods are supported only with the default data isolation mode for a test class. If the test class or a test method has access to organization data by using the @isTest(SeeAllData=true) annotation, test setup methods aren’t supported in this class.

**✅ Tại sao đáp án đúng:**
> 1. Salesforce cấm tiệt việc sử dụng @testSetup khi class đang khai báo @isTest(SeeAllData=True) (A). Đã dùng dữ liệu thật của hệ thống thì không được tạo dữ liệu setup dùng chung nữa để tránh xung đột dữ liệu.
2. Đúng bản chất của @testSetup, dữ liệu chỉ được insert duy nhất một lần trước khi chạy các test method trong class (B), giúp tăng tốc độ thực thi test lên cực kỳ nhiều.

**❌ Tại sao đáp án sai:**
> **C.** Bản ghi tạo trong @testSetup hoàn toàn có thể được update bình thường trong từng test method riêng lẻ để kiểm tra các kịch bản logic khác nhau. Sau khi test method kết thúc, mọi thay đổi sẽ tự động rollback về trạng thái ban đầu.
> **D.** Phương thức @testSetup chỉ chạy duy nhất 1 lần cho cả class, chứ không phải chạy lặp đi lặp lại trước mỗi test method.

**💡 Từ khóa ghi nhớ:** `@testSetup = Chạy 1 lần duy nhất cho toàn bộ class + Cấm đi chung với SeeAllData=True!`

---

## Câu 87

**🔵 Which two platform features align to the Controller portion of MVC architecture? (Choose two.)**

- **A.** Process Builder actions ✅
- **B.** Workflow rules ✅
- **C.** Standard objects ❌
- **D.** Date fields ❌

**📝 Dịch tiếng Việt:**
> Hai tính năng nào sau đây của Salesforce đóng vai trò là tầng Controller trong kiến trúc MVC (Model-View-Controller)? (Chọn hai)

**💬 Giải thích gốc (English):**
> In the Model-View-Controller (MVC) architecture, the Controller is responsible for handling user input and processing data. In Salesforce, both Process Builder actions and Workflow rules can be considered as part of the Controller layer because they automate and process data based on certain criteria and user input.

**✅ Tại sao đáp án đúng:**
> Trong mô hình MVC của Salesforce, tầng Controller chịu trách nhiệm xử lý logic nghiệp vụ và điều khiển dòng chạy của dữ liệu. Cả Process Builder actions (A) và Workflow rules (B) đều chứa các logic tự động hóa, kiểm soát và cập nhật dữ liệu nên chúng thuộc tầng Controller.

**❌ Tại sao đáp án sai:**
> **C.** Standard objects đại diện cho bảng dữ liệu vật lý dùng để lưu trữ thông tin, thuộc tầng Model.
> **D.** Date fields là các trường định nghĩa kiểu dữ liệu ngày tháng, thuộc tầng Model.

**💡 Từ khóa ghi nhớ:** `MVC Salesforce: Model = Object/Field. View = Giao diện (VF/LWC). Controller = Code Apex / Tự động hóa (Flow/Workflow/Process Builder).`

---

## Câu 88

**🔵 A developer wrote the following two classes:
public with sharing class StatusFetcher{
private Boolean active = true;
private Boolean isActive(){
return active;
}
}
public with sharing class Calculator{
public void doCalculations(){
StatusFetcher sFetcher = new StatusFetcher();
if(sFetcher.isActive()){
//do calculations here
}
}
}
The StatusFetcher class successfully compiled and saved. However, the Calculator class has a compile time error. How should the developer fix this code?**

- **A.** Change the class declaration for the StatusFetcher class to public with inherited sharing. ❌
- **B.** Make the isActive method in the StatusFetcher class public. ✅
- **C.** Make the doCalculations method in the Calculator class private. ❌
- **D.** Change the class declaration for the Calculator class to public with inherited sharing. ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên viết hai class sau: [Đoạn code StatusFetcher và Calculator]. Class StatusFetcher lưu thành công nhưng class Calculator lại bị lỗi biên dịch (compile-time error). Lập trình viên nên làm gì để sửa lỗi này?

**💬 Giải thích gốc (English):**
> Make the isActive method public, it can now be accessed from other classes, and the Calculator class will be able to call the isActive method on the StatusFetcher instance without any compilation errors.

**✅ Tại sao đáp án đúng:**
> Phương thức isActive() trong class StatusFetcher đang được khai báo với Access Modifier là private. Theo nguyên lý lập trình hướng đối tượng (OOP), private method chỉ có thể được gọi trong nội bộ của chính class đó. Class Calculator ở bên ngoài muốn gọi được phương thức này thì ta bắt buộc phải thay đổi Access Modifier của nó thành public (B) hoặc global.

**❌ Tại sao đáp án sai:**
> **A.** Thay đổi từ khóa chia sẻ dữ liệu 'with sharing' thành 'with inherited sharing' của class hoàn toàn không có tác động hay quyền can thiệp gì vào Access Modifier (tầm vực truy cập) của một private method, cook!
> **D.** Thay đổi sharing model của Calculator cũng không giải quyết được vấn đề Access Modifier của StatusFetcher.
> **C.** Biến phương thức doCalculations() trong Calculator thành private cũng chả giúp ích gì cho việc nó có thể nhìn thấy được private method của class khác.

**💡 Từ khóa ghi nhớ:** `Lỗi gọi phương thức từ class khác -> Do Access Modifier đang để Private -> Sửa ngay thành Public!`

---

## Câu 89

**🔵 Which statement generates a list of Leads and Contacts that have a field with the phrase 'ACME'?**

- **A.** List <sObject> searchList = [FIND "*ACME*" IN ALL FIELDS RETURNING Contact, Lead]; ❌
- **B.** List<List <sObject>> searchList = [FIND "*ACME*" IN ALL FIELDS RETURNING Contact, Lead]; ✅
- **C.** List<List <sObject>> searchList = [SELECT Name, ID FROM Contact, Lead WHERE Name like ‘%ACME%’]; ❌
- **D.** Map <sObject> searchList = [FIND "*ACME*" IN ALL FIELDS RETURNING Contact, Lead]; ❌

**📝 Dịch tiếng Việt:**
> Câu lệnh nào sau đây trả về danh sách các Lead và Contact có chứa từ khóa 'ACME' ở một trường bất kỳ?

**💬 Giải thích gốc (English):**
> SOSL searches return a List of Lists of sObjects List<List<sObject>>.

**✅ Tại sao đáp án đúng:**
> Để thực hiện tìm kiếm một từ khóa trên nhiều Object khác nhau cùng lúc, ta bắt buộc phải sử dụng ngôn ngữ truy vấn SOSL (bắt đầu bằng từ khóa FIND). Kết quả của một câu lệnh SOSL luôn luôn trả về một danh sách chứa các danh sách bản ghi của từng Object, tức là kiểu dữ liệu List<List<sObject>> (B).

**❌ Tại sao đáp án sai:**
> **A.** SOSL không bao giờ trả về kiểu danh sách phẳng đơn lẻ List<sObject>, compiler sẽ báo lỗi không tương thích kiểu dữ liệu ngay.
> **C.** Đây là câu lệnh SOQL (SELECT). SOQL chỉ cho phép truy vấn dữ liệu từ duy nhất một Object chính (và các Object có quan hệ trực tiếp), cấm viết truy vấn kiểu liệt kê hai Object độc lập Contact, Lead ngăn cách bằng dấu phẩy thế kia, cú pháp sai bét!
> **D.** SOSL không hỗ trợ trả về kiểu dữ liệu dạng Map, ra rìa ngay.

**💡 Từ khóa ghi nhớ:** `Thần chú SOSL: Tìm trên nhiều Object -> Bắt buộc dùng FIND + Kết quả là List<List<sObject>>!`

---

## Câu 90

**🔵 A custom picklist field, Food_Preference__c, exists on a custom object. The picklist contains the following options: 'Vegan', 'Kosher', 'No Preference'. The developer must ensure a value is populated every time a record is created or updated. What is the most efficient way to ensure a value is selected every time a record is saved?**

- **A.** Mark the field as Required on the field definition. ✅
- **B.** Set Use the first value in the list as the default value as True. ❌
- **C.** Mark the field as Required on the object's page layout. ❌
- **D.** Set a validation rule to enforce a value is selected. ❌

**📝 Dịch tiếng Việt:**
> Một trường picklist tùy chỉnh Food_Preference__c tồn tại trên một đối tượng. Cách hiệu quả nhất để đảm bảo một giá trị luôn được chọn mỗi khi bản ghi được lưu là gì?

**💬 Giải thích gốc (English):**
> Change the access modifier of the isActive method in the StatusFetcher class to public.

**✅ Tại sao đáp án đúng:**
> Đánh dấu bắt buộc (Mark Required) ở cấp độ Field Definition (A) (định nghĩa trường) là cách mạnh mẽ và hiệu quả nhất. Nó buộc trường này phải có giá trị ở mọi nơi: giao diện người dùng (UI), gọi API từ ngoài vào, Code Apex, hay nạp dữ liệu bằng Data Loader. Đây là tầng bảo vệ dữ liệu thấp nhất và hiệu quả nhất.

**❌ Tại sao đáp án sai:**
> **C.** Thiết lập Required trên Page Layout chỉ có tác dụng bắt buộc khi người dùng thao tác trực tiếp trên giao diện của trang đó. Nếu tạo bản ghi thông qua Data Loader hoặc Code Apex thì trường vẫn có thể bị bỏ trống dễ dàng, không an toàn!
> **B.** Đặt giá trị mặc định (Default Value) không ép buộc người dùng phải chọn giá trị thực tế theo ngữ cảnh của họ, và giá trị đó vẫn có thể bị xóa trống khi lưu nếu không có ràng buộc Required.
> **D.** Validation Rule cũng bắt buộc được nhưng tốn tài nguyên hệ thống để đánh giá biểu thức công thức hơn và cồng kềnh hơn nhiều so với cài đặt trực tiếp trên Field Definition.

**💡 Từ khóa ghi nhớ:** `Đảm bảo tính toàn vẹn dữ liệu (Data Integrity): Field Definition > Validation Rule > Page Layout!`

---

## Câu 91

**🔵 As part of a data cleanup strategy, AW Computing wants to proactively delete associated opportunity records when the related Account is deleted. Which automation tool should be used to meet this business requirement?**

- **A.** Scheduled job ❌
- **B.** Record-triggered flow ✅
- **C.** Workflow rules ❌
- **D.** Outbound messaging ❌

**📝 Dịch tiếng Việt:**
> AW Computing muốn chủ động tự động xóa các Opportunity liên quan khi một Account bị xóa. Nên sử dụng công cụ tự động hóa nào?

**💬 Giải thích gốc (English):**
> With Record-Triggered Flows, you can automate actions based on changes to record data, including deleting related records.

**✅ Tại sao đáp án đúng:**
> Record-Triggered Flow với sự kiện 'A record is deleted' là chân ái để xử lý logic trước hoặc sau khi xóa, bao gồm cả việc 'tiễn' các bản ghi con lên đường (manual cascade delete) cực kỳ mượt mà.

**❌ Tại sao đáp án sai:**
> **A.** Scheduled job chạy định kỳ kiểu 'hẹn giờ', không bao giờ chủ động 'tức thì' (proactive) ngay khi Account vừa bay màu.
> **C.** Workflow rules là đồ cổ đã bị khai tử (deprecated), chỉ chạy khi create/edit chứ không chơi với sự kiện delete.
> **D.** Outbound messaging chỉ dùng để 'bắn' thông điệp sang hệ thống ngoài, tuổi gì xóa được bản ghi trong Salesforce.

**💡 Từ khóa ghi nhớ:** `Xử lý logic lúc XÓA mà không muốn viết Code -> Chọn Record-Triggered Flow!`

---

## Câu 92

**🔵 Given the following Anonymous Block:
List<Case> casesToUpdate = new List<Case>();
for(Case thisCase : [Select Id, Status FROM Case LIMIT 50000]){
thisCase.Status = 'Working';
casesToUpdate.add(thisCase);
}try{
Database.update(casesToUpdate, false);
}catch(Exception e) {
System.debug(e.getMessage());
}
What should a developer consider for an environment that has over 10,000 Case records?**

- **A.** The transaction will succeed and changes will be committed. ❌
- **B.** The transaction will fail due to exceeding the governor limit. ✅
- **C.** The try/catch block will handle any DML exceptions thrown. ❌
- **D.** The try/catch block will handle exceptions thrown by governor limits. ❌

**📝 Dịch tiếng Việt:**
> Cho đoạn code Anonymous Block sau: [List<Case> casesToUpdate = new List<Case>()...] Điều gì cần lưu ý đối với môi trường có hơn 10,000 bản ghi Case?

**💬 Giải thích gốc (English):**
> Total number of records processed as a result of DML statements, Approval.process, or database.emptyRecycleBin: 10,000
> If there are more than 10,000 Case records in the environment, the code may hit the DML row limit and result in a "Too many DML rows: 10001" exception.
> Reference:
> 1. Execution Governors and Limits
> https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apexgov.htm
> 2. Exceptions that Can’t be Caught(LimitException)
> https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_exception_statements.htm

**✅ Tại sao đáp án đúng:**
> Giới hạn DML Row trong một transaction là 10,000. Đoạn code này hăng hái 'ôm' tới 50,000 bản ghi để update trong một nốt nhạc -> Ăn ngay quả LimitException cực căng và oẳng luôn toàn bộ transaction.

**❌ Tại sao đáp án sai:**
> **A.** Làm sao thành công nổi khi đâm đầu vào bức tường giới hạn 10k DML rows.
> **C.** Dù có try/catch thì lỗi DML Exception ở đây thực chất là LimitException - loại exception 'bất trị', hệ thống sẽ kill ngay lập tức và không cho catch.
> **D.** Try/catch trong Apex tuổi gì đòi bắt được LimitException (Governor Limit). Nó đập cho phát là chết thẳng cẳng!

**💡 Từ khóa ghi nhớ:** `Governor Limit = Cảnh sát giao thông tối cao, bắt là giam xe (Exception), cấm cãi (try/catch vô tác dụng)!`

---

## Câu 93

**🔵 Which two statements are true about Getter and Setter methods? (Choose two.)**

- **A.** Setter methods always have to be declared global. ❌
- **B.** Setter methods are required to pass a value from a page to a controller. ✅
- **C.** There is no guarantee for the order in which Getter or Setter methods are executed. ✅
- **D.** Getter methods can pass a value from a controller to a page. ❌

**📝 Dịch tiếng Việt:**
> Hai phát biểu nào sau đây là đúng về các phương thức Getter và Setter trong Visualforce? (Chọn 2)

**💬 Giải thích gốc (English):**
> Setter Methods: While a getter method is always required to access values from a controller, it’s not always necessary to include a setter method to pass values into a controller. If a Visualforce component is bound to an sObject that is stored in a controller, the sObject's fields are automatically set if changed by the user, as long as the sObject is saved or updated by a corresponding action method.
> There is no guaranteed order in which Apex methods and variables are processed by a controller extension or custom controller. Therefore, do not allow controller and extension classes to rely on another method being run, call that method directly. This applies specifically to setting variables and accessing data from the database.

**✅ Tại sao đáp án đúng:**
> B đúng vì muốn 'bê' dữ liệu user nhập từ giao diện (VF Page) ném về Controller xử lý thì bắt buộc phải có Setter. C đúng vì Salesforce siêu tự do, không hề đảm bảo thứ tự thực thi của các Getter hay Setter khi tải trang. Đừng bao giờ viết code logic phụ thuộc vào việc thằng nào chạy trước thằng nào, hụt hẫng ráng chịu!

**❌ Tại sao đáp án sai:**
> **A.** Setter chỉ cần public hoặc global tùy nhu cầu sử dụng, bắt buộc global là nói phét.
> **D.** Getter dùng để truyền dữ liệu từ Controller ra ngoài Page để hiển thị (Get ra), chứ không phải để truyền ngược vào.

**💡 Từ khóa ghi nhớ:** `Getter = Đẩy dữ liệu ra Page (Read). Setter = Hốt dữ liệu vào Controller (Write). Thứ tự chạy hên xui!`

---

## Câu 94

**🔵 A Platform Developer needs to write an Apex method that will only perform an action if a record is assigned to a specific Record Type. Which two options allow the developer to dynamically determine the ID of the required Record Type by its name? (Choose two.)**

- **A.** Make an outbound web services call to the SOAP API. ❌
- **B.** Hardcode the ID as a constant in an Apex class. ❌
- **C.** Use the getRecordTypeInfosByName() method in the DescribeSObjectResult class. ✅
- **D.** Execute a SOQL query on the RecordType object. ✅

**📝 Dịch tiếng Việt:**
> Developer cần viết code Apex chỉ thực hiện hành động nếu bản ghi thuộc Record Type cụ thể. Hai cách nào giúp lấy Record Type ID động theo Tên (Name)? (Chọn 2)

**💬 Giải thích gốc (English):**
> Using the getRecordTypeInfosByName() method allows you to dynamically retrieve the Record Type ID by its name without hardcoding.
> Executing a SOQL query on the RecordType object is another way to dynamically determine the Record Type ID.

**✅ Tại sao đáp án đúng:**
> C đúng vì sử dụng `getRecordTypeInfosByName()` của Schema Describe giúp hốt ngay Record Type ID từ bộ nhớ RAM trong tích tắc, cực nhanh và không tốn SOQL query. D đúng vì truy vấn SOQL trực tiếp vào sObject hệ thống `RecordType` lọc theo `DeveloperName` hoặc `Name` cũng trả về ID chính xác 100%.

**❌ Tại sao đáp án sai:**
> **A.** Gọi web service SOAP ra ngoài chỉ để lấy một cái ID Record Type? Cồng kềnh, chậm chạp và cực kỳ điên rồ!
> **B.** Hardcode ID trực tiếp là tối kỵ của dân chuyên nghiệp, sang Sandbox hoặc Org khác ID thay đổi là code oẳng ngay lập tức.

**💡 Từ khóa ghi nhớ:** `Lấy ID Record Type động -> Describe SObject (Không tốn query) HOẶC SOQL RecordType. Né hardcode ID!`

---

## Câu 95

**🔵 Which situation prevents a developer from setting sharing rules for a custom object?**

- **A.** The object's Sharing Settings is set to Public Read/Write. ❌
- **B.** The object is on the detail side of a Master-Detail relationship. ✅
- **C.** The developer is not a System Administrator. ❌
- **D.** The object is referenced in an Owner field of a Master-Detail relationship. ❌

**📝 Dịch tiếng Việt:**
> Trường hợp nào sau đây ngăn cản developer thiết lập Sharing Rules cho một Custom Object?

**💬 Giải thích gốc (English):**
> Cannot set explicit sharing rules for custom objects that are on the detail side of a Master-Detail relationship.

**✅ Tại sao đáp án đúng:**
> Khi Custom Object đó nằm ở bên con (Detail) của mối quan hệ Master-Detail. Thằng con sẽ bị tước quyền tự quyết và bắt buộc phải ký sinh bảo mật, kế thừa hoàn toàn cấu hình bảo mật (Sharing) của thằng cha (Master). Cho nên không có cửa thiết lập Sharing Rules riêng nhé!

**❌ Tại sao đáp án sai:**
> **A.** Public Read/Write là OWD mặc định, không ngăn cản việc viết sharing rule để mở rộng quyền truy cập (chỉ là không cần thiết thôi).
> **C.** Chỉ cần user có quyền 'Customize Application' là set được ngon lành, không nhất thiết phải là System Admin tối cao.
> **D.** Object con trong Master-Detail làm gì có trường Owner riêng mà đòi tham chiếu, cồng kềnh!

**💡 Từ khóa ghi nhớ:** `Detail trong Master-Detail = 'Ký sinh bảo mật'. Không Owner, không Sharing Rules riêng!`

---

## Câu 96

**🔵 What will be the output in the debug log in the event of a QueryException during a call to the aQuery method in the following example?
class myClass{
class CustomException extends QueryException{}
public static Account aQuery(){
Account theAccount;
try{
system.debug('Querying Accounts.');
theAccount = [SELECT Id FROM Account WHERE CreatedDate > TODAY];
}catch(CustomException eX){
system.debug ('Custom Exception.');
}catch(QueryException eX){
system.debug('Query Exception.');
}finally{
system.debug('Done.');
}
return theAccount;
}
}**

- **A.** Querying Accounts. Query Exception. ❌
- **B.** Querying Accounts. Custom Exception. ❌
- **C.** Querying Accounts. Custom Exception. Done. ❌
- **D.** Querying Accounts. Query Exception. Done. ✅

**📝 Dịch tiếng Việt:**
> Debug log sẽ in ra kết quả gì khi xảy ra QueryException trong hàm aQuery ở ví dụ dưới đây? [myClass]

**💬 Giải thích gốc (English):**
> 1. Try Block: The code attempts to execute the SOQL query inside the try block and logs “Querying Accounts.”.
> 2. Catch Blocks: If a QueryException occurs, it will be caught by the catch(QueryException eX) block, logging “Query Exception.”.
> 3. Finally Block: The finally block will always execute, logging “Done.”.

**✅ Tại sao đáp án đúng:**
> Khi SOQL query hẹo (ném ra QueryException của hệ thống), Apex sẽ chạy từ trên xuống: Lọt vào catch(CustomException) -> Skip vì CustomException (class con tự viết) không bắt được QueryException chuẩn của hệ thống; Lọt vào catch(QueryException) -> Khớp! In ra 'Query Exception.'; Cuối cùng, block `finally` là bất tử, luôn luôn chạy dù code có lỗi hay không -> In ra 'Done.'. Kết hợp lại ta được đáp án D.

**❌ Tại sao đáp án sai:**
> **A.** Thiếu 'Done.' của block finally. Block này dù trời sập vẫn phải chạy!
> **B.** Bị bắt sai block catch. Lỗi hệ thống xịn sò không bao giờ chui vào class CustomException tự chế kia.
> **C.** Vừa bị bắt sai block catch vừa thiếu 'Done.' của block finally.

**💡 Từ khóa ghi nhớ:** `Block `finally` = 'Bất tử', dù code chạy ngon hay oẳng dính Exception thì finally VẪN PHẢI CHẠY!`

---

## Câu 97

**🔵 Universal Containers wants Opportunities to no longer be editable when reaching the Closed/Won stage. Which two strategies can a developer use to accomplish this? (Choose two.)**

- **A.** Use an after-save flow. ❌
- **B.** Use a validation rule. ✅
- **C.** Use the Process Automation Settings. ❌
- **D.** Use a trigger. ✅

**📝 Dịch tiếng Việt:**
> Universal Containers muốn Opportunity không cho phép chỉnh sửa khi đã chuyển sang trạng thái Closed/Won. Hai giải pháp nào lập trình viên có thể sử dụng? (Chọn 2)

**💬 Giải thích gốc (English):**
> Create a validation rule on the Opportunity object that checks the stage value. If the stage is Closed/Won, the validation rule should prevent any updates or changes to the Opportunity.
> Using a trigger can be an option.

**✅ Tại sao đáp án đúng:**
> B đúng vì Validation Rule là vũ khí no-code tối thượng để chặn lưu. Kiểm tra nếu `IsWon = true` và có cố gắng chỉnh sửa thì quăng lỗi bắt user đứng hình. D đúng vì dùng Trigger `before update` check trạng thái cũ và mới rồi nện `addError()` vào bản ghi để chặn lưu cực kỳ uy tín.

**❌ Tại sao đáp án sai:**
> **A.** After-save flow chạy sau khi gạo đã nấu thành cơm (bản ghi đã lưu vào database), không có cơ chế chặn lưu hay quăng lỗi cấm sửa trực tiếp như Validation Rule.
> **C.** Process Automation Settings chỉ dùng để cấu hình chung cho hệ thống tự động hóa, chả liên quan gì đến logic chặn sửa bản ghi cụ thể.

**💡 Từ khóa ghi nhớ:** `Chặn chỉnh sửa bản ghi (Khóa cứng) -> 1. Validation Rule (No-code); 2. Trigger addError (Code).`

---

## Câu 98

**🔵 Which action causes a before trigger to fire by default for Accounts?**

- **A.** Renaming or replacing picklists ❌
- **B.** Importing data using the Data Loader and the Bulk API ✅
- **C.** Updating addresses using the Mass Address update tool ❌
- **D.** Converting Leads to Contacts ❌

**📝 Dịch tiếng Việt:**
> Hành động nào mặc định sẽ kích hoạt Before Trigger cho đối tượng Account?

**💬 Giải thích gốc (English):**
> When importing data using the Data Loader or Bulk API, Salesforce triggers are executed by default. This includes before triggers for Accounts, which would fire before the imported data is inserted or updated.

**✅ Tại sao đáp án đúng:**
> Dùng Data Loader để nạp dữ liệu (dù qua Bulk API hay SOAP API) thực chất là thực hiện các thao tác DML chuẩn (Insert, Update). Đã là DML thì Before/After Trigger cứ thế mà nổ banh xác theo đúng luật.

**❌ Tại sao đáp án sai:**
> **A.** Thay đổi metadata (rename/replace picklist) chỉ là đổi cấu hình hệ thống, không tác động trực tiếp vào data nên trigger ngủ yên không thèm nổ.
> **C.** Sử dụng Mass Address Update tool là công cụ hệ thống đặc thù, cơ chế chạy ngầm và không kích hoạt trigger chuẩn của Account.
> **D.** Lead Conversion (chuyển đổi Lead) chủ yếu kích hoạt trigger trên bản ghi được tạo mới/cập nhật cụ thể trong luồng convert chứ không kích hoạt before trigger thông thường của Account một cách mặc định không điều kiện.

**💡 Từ khóa ghi nhớ:** `Cứ đụng đến DML (như Data Loader import) là Trigger nổ!`

---

## Câu 99

**🔵 The values 'High', 'Medium', and 'Low' are identified as common values for multiple picklists across different objects. What is an approach a developer can take to streamline maintenance of the picklists and their values, while also restricting the values to the ones mentioned above?**

- **A.** Create the Picklist on each object and use a Global Picklist Value Set containing the values. ✅
- **B.** Create the Picklist on each object as a required field and select "Display values alphabetically, not in the order entered". ❌
- **C.** Create the Picklist on each object and add a validation rule to ensure data integrity. ❌
- **D.** Create the Picklist on each object and select "Restrict picklist to the values defined in the value set". ❌

**📝 Dịch tiếng Việt:**
> Các giá trị 'High', 'Medium', 'Low' dùng chung cho nhiều field picklist ở nhiều object khác nhau. Cách nào để quản lý tập trung và giới hạn giá trị tốt nhất?

**💬 Giải thích gốc (English):**
> By creating a Global Picklist Value Set with the common values 'High', 'Medium', and 'Low', you can then use this value set to populate the picklist fields on different objects.

**✅ Tại sao đáp án đúng:**
> Global Picklist Value Set sinh ra để làm bá chủ khoản này. Định nghĩa bộ giá trị một nơi và dùng cho nhiều field ở nhiều object khác nhau. Sau này sếp đòi thêm giá trị 'Very High' thì chỉ cần sửa một phát ở Global Set là cả lũ tự động cập nhật, nhàn nhã vô cùng!

**❌ Tại sao đáp án sai:**
> **B.** Chọn hiển thị theo bảng chữ cái thì liên quan gì đến việc bảo trì tập trung, lạc đề cực nặng!
> **C.** Viết Validation Rule cho từng field ở từng object để kiểm tra giá trị? Cách làm cồng kềnh, thủ công và tốn calo nhất hệ mặt trời.
> **D.** Chọn giới hạn giá trị tại từng field riêng lẻ bắt mày phải cấu hình thủ công cho cả chục field, bảo trì mệt nghỉ khi có thay đổi.

**💡 Từ khóa ghi nhớ:** `Dùng chung giá trị picklist cho nhiều object -> Chọn ngay Global Picklist Value Set.`

---

## Câu 100

**🔵 Which option should a developer use to create 500 Accounts and make sure that duplicates are not created for existing Account Sites?**

- **A.** Sandbox template ❌
- **B.** Data Loader ❌
- **C.** Data Import Wizard ✅
- **D.** Salesforce-to-Salesforce ❌

**📝 Dịch tiếng Việt:**
> Cần tạo 500 Account và đảm bảo không tạo trùng lặp với các Account Site đã tồn tại. Lựa chọn nào tối ưu?

**💬 Giải thích gốc (English):**
> The Data Import Wizard in Salesforce provides an easy-to-use interface for importing data, and it has a built-in duplicate management feature that allows you to prevent the creation of duplicate records during the import process.

**✅ Tại sao đáp án đúng:**
> Data Import Wizard là công cụ 'mỳ ăn liền' no-code cực xịn cho dữ liệu dưới 50k bản ghi. Nó tích hợp sẵn tính năng so khớp và chặn trùng lặp (Duplicate Management) cực kỳ mạnh mẽ dựa trên Name, Site... ngay lúc import.

**❌ Tại sao đáp án sai:**
> **A.** Sandbox template dùng để chọn lọc dữ liệu khi tạo/refresh Sandbox, không liên quan gì đến việc nạp và lọc trùng data.
> **B.** Data Loader hỗ trợ nạp hàng triệu bản ghi nhưng cực kỳ 'ngây thơ', không có tính năng tự động so khớp chặn trùng lặp trực tiếp khi import như Wizard.
> **D.** Salesforce-to-Salesforce là tính năng kết nối chia sẻ dữ liệu giữa 2 Org khác nhau, không phải công cụ để import dữ liệu.

**💡 Từ khóa ghi nhớ:** `Dưới 50k bản ghi + Lọc trùng không cần code -> Data Import Wizard (Wizard lọc trùng siêu đỉnh)!`

---

## Câu 101

**🔵 How should a developer write unit tests for a private method in an Apex class?**

- **A.** Add a test method in the Apex class. ❌
- **B.** Mark the Apex class as global. ❌
- **C.** Use the SeeAllData annotation. ❌
- **D.** Use the TestVisible annotation. ✅

**📝 Dịch tiếng Việt:**
> Làm sao để viết unit test cho một private method trong Apex class?

**💬 Giải thích gốc (English):**
> The TestVisible annotation allows you to expose private methods and variables to be accessed in test classes.

**✅ Tại sao đáp án đúng:**
> Annotation `@TestVisible` sinh ra như một tấm vé đặc cách. Nó cho phép các class test dòm thấy và gọi được các private/protected method hoặc variable của class chính mà không cần phải chuyển chúng thành public (giúp giữ vững tính đóng gói của code).

**❌ Tại sao đáp án sai:**
> **A.** Viết method test trực tiếp trong class chính là lỗi thời và sai nguyên tắc thiết kế, code test và code logic phải tách biệt hoàn toàn.
> **B.** Khai báo class là global chả giúp ích gì cho việc truy cập private method mà còn làm lộ class ra ngoài, thiếu bảo mật nghiêm trọng.
> **C.** `SeeAllData=true` chỉ để đọc dữ liệu thật trong Org khi chạy test, không giúp vượt rào truy cập private method.

**💡 Từ khóa ghi nhớ:** `Test private method -> `@TestVisible` (Hiện hình cho test thấy)!`

---

## Câu 102

**🔵 A company has a custom object named Region. Each Account in Salesforce can only be related to one Region at a time, but this relationship is optional. Which type of relationship should a developer use to relate an Account to a Region?**

- **A.** Parent-Child ❌
- **B.** Hierarchical ❌
- **C.** Lookup ✅
- **D.** Master-Detail ❌

**📝 Dịch tiếng Việt:**
> Mỗi Account chỉ liên kết với một Region tại một thời điểm, liên kết này không bắt buộc (optional). Dùng loại quan hệ nào?

**💬 Giải thích gốc (English):**
> A Lookup relationship allows each Account to be optionally related to one Region at a time without enforcing strict dependency rules, which fits the requirement of an optional relationship.

**✅ Tại sao đáp án đúng:**
> Mối quan hệ Lookup (C) là chuẩn cơm mẹ nấu vì nó liên kết lỏng lẻo giữa 2 đối tượng và cực kỳ thoải mái: cho phép để trống (optional). Nếu không chọn Region thì Account vẫn lưu ngon lành.

**❌ Tại sao đáp án sai:**
> **A.** Parent-Child chỉ là tên gọi logic chung của mối quan hệ, không phải loại trường quan hệ cụ thể trong Salesforce.
> **B.** Hierarchical (mối quan hệ phân cấp) là dạng lookup đặc biệt chỉ dùng riêng cho đối tượng User để liên kết User này với User khác, object thường không có cửa.
> **D.** Master-Detail là mối quan hệ 'sống chết có nhau', bắt buộc phải điền giá trị chứ không bao giờ cho phép để trống (optional) như Lookup.

**💡 Từ khóa ghi nhớ:** `Liên kết 1-Nhiều + Tùy chọn (để trống được) -> Chọn Lookup. Bắt buộc có giá trị -> Master-Detail!`

---

## Câu 103

**🔵 An Account trigger updates all related Contacts and Cases each time an Account is saved using the following two DML statements: update allContacts; update allCases; What is the result if the Case update exceeds the governor limit for maximum number of DML records?**

- **A.** The Account save fails and no Contacts or Cases are updated. ✅
- **B.** The Account save succeeds and no Contacts or Cases are updated. ❌
- **C.** The Account save succeeds, Contacts are updated, but Cases are not. ❌
- **D.** The Account save is retried using a smaller trigger batch size. ❌

**📝 Dịch tiếng Việt:**
> Trigger trên Account thực hiện cập nhật Contact và Case bằng 2 câu lệnh DML: 'update allContacts;' và 'update allCases;'. Nếu việc cập nhật Case vượt quá giới hạn (governor limit) về số lượng bản ghi DML, chuyện gì sẽ xảy ra?

**💬 Giải thích gốc (English):**
> If the Case update exceeds the governor limit for the maximum number of DML records, the entire transaction is rolled back, causing the Account save to fail and preventing any updates to Contacts or Cases.

**✅ Tại sao đáp án đúng:**
> Quy tắc vàng của Database Transaction trong Salesforce: 'Một thằng oẳng là cả lũ cùng đi'. Tất cả các thao tác trong một transaction được thực thi dưới dạng nguyên tử (Atomic). Khi lệnh update Case dính lỗi Governor Limit, toàn bộ transaction sẽ bị rollback (hủy bỏ) sạch sẽ từ đầu đến cuối. Account không lưu được, Contact và Case cũng giữ nguyên trạng thái cũ.

**❌ Tại sao đáp án sai:**
> **B.** Account lưu thất bại hoàn toàn chứ không có chuyện lưu thành công.
> **C.** Salesforce không bao giờ cho phép 'lưu một nửa' (Contact được lưu còn Case thì không) khi dính unhandled exception trong transaction.
> **D.** Hệ thống không rảnh để tự động thử lại (retry) với kích thước lô nhỏ hơn khi dính lỗi Governor Limit đâu nhé.

**💡 Từ khóa ghi nhớ:** `Salesforce Transaction: 'Đồng sinh cộng tử'. Một thằng dính LimitException -> Rollback sạch sẽ về vạch xuất phát!`

---

## Câu 104

**🔵 A developer wants to invoke an outbound message when a record meets a specific criteria. Which three features satisfy this use case? (Choose three.)**

- **A.** Process builder can be used to check the record criteria and send an outbound message with Apex Code. ✅
- **B.** Process builder can be used to check the record criteria and send an outbound message without Apex Code. ❌
- **C.** Approval Process has the capability to check the record criteria and send an outbound message without Apex Code. ✅
- **D.** Workflows can be used to check the record criteria and send an outbound message. ✅
- **E.** Visual Workflow can be used to check the record criteria and send an outbound message without Apex Code. ❌

**📝 Dịch tiếng Việt:**
> Cần kích hoạt Outbound Message khi bản ghi thỏa mãn điều kiện. Ba tính năng nào thỏa mãn yêu cầu này? (Chọn 3)

**💬 Giải thích gốc (English):**
> Outbound messaging allows you to specify that changes to fields within Salesforce can cause messages with field values to be sent to designated external servers.
> Outbound messaging is part of the workflow rule functionality in Salesforce. Workflow rules watch for specific kinds of field changes and trigger automatic Salesforce actions, such as sending email alerts, creating task records, or sending an outbound message. You can associate outbound messages with flows, workflow rules, approval processes, or entitlement processes.

**✅ Tại sao đáp án đúng:**
> A đúng vì tuy Process Builder không hỗ trợ Outbound Message trực tiếp (no-code), nó hoàn toàn có thể gọi một đoạn Apex Code (@InvocableMethod) để bắn Outbound Message đi. C đúng vì Approval Process hỗ trợ cấu hình gửi Outbound Message trực tiếp dưới dạng Approval Actions hoàn toàn no-code. D đúng vì Workflow Rules huyền thoại (dù là đồ cổ) hỗ trợ Outbound Message cực kỳ cơ bản.

**❌ Tại sao đáp án sai:**
> **B.** Process Builder tự thân nó (without Apex Code) không có hành động gửi Outbound Message trực tiếp đâu nhé.
> **E.** Visual Flow (Flow kiểu cũ) không hỗ trợ gửi Outbound Message mà không dùng Apex Code.

**💡 Từ khóa ghi nhớ:** `Outbound Message no-code truyền thống -> Workflow, Approval Process. Dùng Apex -> Process Builder. (Năm 2026: Flow là vua!).`

---

## Câu 105

**🔵 What is the result of the following code snippet?
public void doWork(Account acct){
for(Integer i = 0; i <= 200; i++){
insert acct;
}
}**

- **A.** 200 Accounts are inserted. ❌
- **B.** 1 Account is inserted. ❌
- **C.** 201 Accounts are inserted. ❌
- **D.** 0 Accounts are inserted. ✅

**📝 Dịch tiếng Việt:**
> Kết quả của đoạn code insert một biến Account 201 lần trong vòng lặp [for(Integer i = 0; i <= 200; i++) insert acct;] là gì?

**💬 Giải thích gốc (English):**
> The exception prevents any accounts from being inserted, and the final outcome is that 0 Accounts are inserted.
> To avoid hitting the governor limit, a better approach would be to collect the accounts in a collection (such as a List<Account>) during the loop and then perform a single bulk insert after the loop completes.

**✅ Tại sao đáp án đúng:**
> Lần lặp đầu tiên: biến `acct` được insert thành công và được hệ thống cấp Id. Lần lặp thứ hai: câu lệnh tiếp tục cố gắng insert biến `acct` đó một lần nữa. Apex lập tức quăng lỗi 'Record already has ID' (hoặc dính LimitException 150 DML vì chạy trong loop). Vì không có try/catch xử lý lỗi này, toàn bộ transaction bị rollback sạch sẽ về 0. Không có bản ghi nào được lưu cả!

**❌ Tại sao đáp án sai:**
> **A.** Dính lỗi ngay từ lần thứ 2 nên không bao giờ insert được 200 bản ghi.
> **B.** Lần 1 insert được nhưng lần 2 bị lỗi khiến toàn bộ transaction rollback, kéo theo lần 1 cũng mất tiêu.
> **C.** Không thể insert 201 bản ghi vì dính giới hạn DML trong vòng lặp và lỗi ID trùng lặp.

**💡 Từ khóa ghi nhớ:** `DML in Loop = Cook. Insert bản ghi đã có ID = Cook. Rollback về 0 bản ghi!`

---

## Câu 106

**🔵 A developer writes a single trigger on the Account object on the after insert and after update events. A workflow rule modifies a field every time an Account is created or updated. How many times will the trigger fire if a new Account is inserted, assuming no other automation logic is implemented on the Account?**

- **A.** 8 ❌
- **B.** 1 ❌
- **C.** 4 ❌
- **D.** 2 ✅

**📝 Dịch tiếng Việt:**
> Viết một trigger duy nhất trên Account ở sự kiện after insert và after update. Một Workflow Rule đổi giá trị trường mỗi khi Account tạo/sửa. Hỏi trigger nổ bao nhiêu lần khi chèn mới 1 Account (không có tự động hóa khác)?

**💬 Giải thích gốc (English):**
> When a new Account is inserted, the following sequence of events occurs:
> 1. The Account is inserted, triggering the after insert event.
> 2. The workflow rule modifies a field on the Account, which triggers an after update event.
> So, the trigger will fire twice:
> 1. Once for the after insert event.
> 2. Once for the after update event caused by the workflow rule.

**✅ Tại sao đáp án đúng:**
> Trigger sẽ nổ đúng 2 lần (D). Lần 1: Chèn mới Account -> Kích hoạt trigger 'after insert' (Trigger nổ lần 1). Ngay sau đó, Workflow Rule thấy điều kiện thỏa mãn liền nhảy vào cập nhật trường -> Salesforce thực hiện save ngầm bản ghi và chạy lại trigger ở sự kiện 'after update' (Trigger nổ lần 2).

**❌ Tại sao đáp án sai:**
> **A.** Số lần nổ quá lớn, không đúng thứ tự vòng đời thực tế của Salesforce.
> **B.** Thiếu lần kích hoạt thứ 2 khi Workflow Rule thực hiện cập nhật lại trường.
> **C.** Tính toán sai chu kỳ lưu bản ghi (Order of Execution).

**💡 Từ khóa ghi nhớ:** `New Insert -> After Insert nổ -> Workflow update -> After Update nổ lần nữa = 2 lần!`

---

## Câu 107

**🔵 A developer must provide custom user interfaces when users edit a Contact in either Salesforce Classic or Lightning Experience. What should the developer use to override the Contact's Edit button and provide this functionality?**

- **A.** A Lightning page in Salesforce Classic and a Visualforce page in Lightning Experience ❌
- **B.** A Visualforce page in Salesforce Classic and a Lightning page in Lightning Experience ❌
- **C.** A Visualforce page in Salesforce Classic and a Lightning component in Lightning Experience ✅
- **D.** A Lightning component in Salesforce Classic and a Lightning component in Lightning Experience ❌

**📝 Dịch tiếng Việt:**
> Cần cung cấp giao diện tùy chỉnh khi người dùng chỉnh sửa (Edit) Contact cho cả Salesforce Classic và Lightning Experience. Lập trình viên nên dùng gì để ghi đè nút Edit?

**💬 Giải thích gốc (English):**
> Visualforce pages are used to create custom user interfaces in Salesforce Classic, and Lightning components are used to create custom user interfaces in Lightning Experience.

**✅ Tại sao đáp án đúng:**
> Salesforce Classic là đồ cổ nên chỉ chơi được với Visualforce Page để tùy biến giao diện nút bấm. Còn Lightning Experience là thời thượng nên phải dùng Lightning Component (Aura hoặc LWC) để giao diện mượt mà và tối ưu trải nghiệm người dùng nhất.

**❌ Tại sao đáp án sai:**
> **A.** Classic không hỗ trợ Lightning page để làm giao diện tùy chỉnh cho nút bấm.
> **B.** Lightning page dùng để xây dựng cấu trúc trang, không dùng để ghi đè nút chức năng như Edit button.
> **D.** Classic không hỗ trợ hiển thị mượt mà Lightning component khi ghi đè nút Edit trực tiếp.

**💡 Từ khóa ghi nhớ:** `Ghi đè nút (Override): Classic -> Visualforce Page. Lightning -> Lightning Component (LWC/Aura)!`

---

## Câu 108

**🔵 What is the result of the debug statements in testMethod3 when you create test data using testSetup in below code?
@istest
private class CreateandExecuteTest {
@testsetup
static void setup(){
list<account> testaccts = new list<account>();
for(integer i=0; i<2; i++){
testaccts.add(new account(name = 'MyTestAccount'+i, Phone ='333-878'+i));
}
insert testaccts;
}
@isTest
static void TestMethod1(){
account acc = [select id, phone from account where name = 'MyTestAccount0' Limit 1];
acc.phone = '888-1515';
update acc;
account acc2 = [select id, phone from account where name = 'MyTestAccount1' Limit 1];
acc2.phone = '999-1515';
update acc2;
}
@isTest
static void TestMethod2(){
account acc = [select id, phone from account where name = 'MyTestAccount1' Limit 1];
acc.phone = '888-2525';
update acc;
}
@istest
static void testmethod3(){
account acc0 = [select id, phone from account where name = 'MyTestAccount0' Limit 1];
account acc1 = [select id, phone from account where name = 'MyTestAccount1' Limit 1];
system.debug('account0.Phone = '+ acc0.Phone + ', account1.Phone = '+ acc1.Phone);
}
}**

- **A.** Account0.Phone=333-8781, Account1.Phone=333-8780 ❌
- **B.** Account0.Phone=888-1515, Account1.Phone=999-2525 ❌
- **C.** Account0.Phone=333-8780, Account1.Phone=333-8781 ✅
- **D.** Account0.Phone=888-1515, Account1.Phone=999-1515 ❌

**📝 Dịch tiếng Việt:**
> Kết quả của các câu debug log trong testMethod3 sẽ in ra số điện thoại nào của các Account được tạo từ @testSetup trong đoạn code dưới đây? [CreateandExecuteTest]

**💬 Giải thích gốc (English):**
> The debug statements in testMethod3 will display the phone numbers of the accounts created in the test setup method. Since the accounts are created in a loop where the phone numbers are incremented, the expected result is Account0.Phone=333-8780, Account1.Phone=333-8781, making this choice correct.

**✅ Tại sao đáp án đúng:**
> Kết quả là 'Account0.Phone=333-8780, Account1.Phone=333-8781' (C). Dữ liệu tạo trong `@testSetup` được lưu vào database ảo một lần duy nhất trước khi các test method chạy. Khi `TestMethod1` hoặc `TestMethod2` chạy và sửa đổi dữ liệu (đổi Phone), những thay đổi này chỉ có hiệu lực cục bộ bên trong method đó và bị rollback sạch sẽ ngay khi method đó kết thúc. Đến lượt `testmethod3` chạy, nó sẽ nhận lại dữ liệu nguyên bản lúc khởi tạo ban đầu ở `@testSetup`.

**❌ Tại sao đáp án sai:**
> **A.** Số điện thoại bị đảo ngược sai lệch so với lúc gán giá trị trong vòng lặp setup.
> **B.** Hiển thị số điện thoại đã bị sửa đổi ở các test method khác là sai hoàn toàn cơ chế cô lập của test setup.
> **D.** Tương tự B, dữ liệu sửa đổi ở các test method khác không hề được lưu lại sang testMethod3.

**💡 Từ khóa ghi nhớ:** `Dữ liệu `@testSetup` = Bất biến giữa các Test Method. Thằng nào sửa tự chịu, xong việc là rollback về ban đầu!`

---

## Câu 109

**🔵 Which type of code represents the Model in the MVC architecture when using Apex and Visualforce pages?**

- **A.** A Controller Extension method that saves a list of Account records ❌
- **B.** Custom JavaScript that processes a list of Account records ❌
- **C.** A list of Account records returned from a Controller Extension method ✅
- **D.** A Controller Extension method that uses SOQL to query for a list of Account records ❌

**📝 Dịch tiếng Việt:**
> Loại mã code nào đại diện cho tầng Model trong kiến trúc MVC khi sử dụng Apex và Visualforce?

**💬 Giải thích gốc (English):**
> The Model is responsible for handling the data and business logic. A list of Account records returned from a Controller Extension method would be an example of the Model.

**✅ Tại sao đáp án đúng:**
> Trong mô hình MVC (Model-View-Controller), tầng Model là nơi chứa cấu trúc dữ liệu và dữ liệu thực tế. Danh sách các bản ghi Account (List<Account>) (C) được trả về từ Controller Extension chính là dữ liệu thô đại diện cho tầng Model.

**❌ Tại sao đáp án sai:**
> **A.** Phương thức thực hiện lưu bản ghi (DML) thuộc tầng xử lý logic nghiệp vụ - Controller.
> **B.** JavaScript tùy chỉnh xử lý giao diện người dùng thuộc tầng View.
> **D.** Phương thức thực hiện SOQL query dữ liệu thuộc tầng xử lý logic - Controller.

**💡 Từ khóa ghi nhớ:** `MVC Salesforce: Dữ liệu bản ghi (sObject/List) = Model. Giao diện (VF Page/LWC) = View. Class xử lý (Apex) = Controller.`

---

## Câu 110

**🔵 An org has a single account named 'NoContacts' that has no related contacts. Given the query: List<Account> accounts = [Select ID, (Select ID, Name from Contacts) from Account where Name = 'NoContacts']; What is the result of running this Apex?**

- **A.** accounts[0].contacts is invalid Apex. ❌
- **B.** accounts[0].contacts is an empty list. ✅
- **C.** accounts[0].contacts is Null. ❌
- **D.** A QueryException is thrown. ❌

**📝 Dịch tiếng Việt:**
> Một Org chỉ có duy nhất một Account tên 'NoContacts' và không có Contact liên quan nào. Chạy câu lệnh SOQL subquery truy vấn Account và các Contact con liên quan. Biến `accounts[0].contacts` sẽ trả về kết quả gì?

**💬 Giải thích gốc (English):**
> When you run the given query, it retrieves the account with the name ‘NoContacts’. Since this account has no related contacts, the contacts relationship will be an empty list, not null. Therefore, accounts[0].contacts will be an empty list.

**✅ Tại sao đáp án đúng:**
> Khi thực hiện SOQL subquery trỏ đến quan hệ con mà không tìm thấy bản ghi con nào, hệ thống sẽ tự động trả về một Danh sách rỗng (Empty List) chứ tuyệt đối không bao giờ trả về `null`. Nhờ vậy lập trình viên có thể duyệt vòng lặp thoải mái mà không lo dính lỗi NullPointerException huyền thoại.

**❌ Tại sao đáp án sai:**
> **A.** Cú pháp truy cập list con hoàn toàn hợp lệ, không có gì sai cả.
> **C.** Không phải Null. Salesforce luôn khởi tạo List rỗng để tránh lỗi NullPointerException.
> **D.** Không có lỗi QueryException nào xảy ra vì cú pháp chuẩn và bản ghi cha vẫn tồn tại ngon lành.

**💡 Từ khóa ghi nhớ:** `Subquery không có con -> Trả về EMPTY LIST, không bao giờ trả về NULL!`

---

## Câu 111

**🔵 Which SOQL query successfully returns the Accounts grouped by name?**

- **A.** SELECT Type, Max(CreatedDate) FROM Account GROUP BY Name ❌
- **B.** SELECT Name, Max(CreatedDate) FROM Account GROUP BY Name ✅
- **C.** SELECT Id, Type, Max(CreatedDate) FROM Account GROUP BY Name ❌
- **D.** SELECT Type, Name, Max(CreatedDate) FROM Account GROUP BY Name LIMIT 5 ❌

**📝 Dịch tiếng Việt:**
> Câu lệnh SOQL nào sau đây thực hiện nhóm các Account theo tên (GROUP BY Name) thành công?

**💬 Giải thích gốc (English):**
> This query selects the Name and maximum CreatedDate from the Account object and groups the results by the Name field. This is the correct query to successfully return the Accounts grouped by name.

**✅ Tại sao đáp án đúng:**
> Luật GROUP BY trong SOQL cực kỳ nghiêm ngặt: Một khi đã dùng GROUP BY trường nào (ở đây là Name), thì tất cả các trường xuất hiện trong mệnh đề SELECT bắt buộc phải là trường được group đó (Name) HOẶC phải nằm trong một Hàm tổng hợp (Aggregate Function) như `MAX()`, `MIN()`, `SUM()`, `COUNT()`. Đáp án B tuân thủ hoàn hảo quy tắc này.

**❌ Tại sao đáp án sai:**
> **A.** Trường 'Type' nằm trong SELECT nhưng không có trong GROUP BY và không dùng hàm tổng hợp, gây lỗi biên dịch.
> **C.** Trường 'Id' và 'Type' vi phạm nghiêm trọng luật GROUP BY.
> **D.** Trường 'Type' vi phạm luật GROUP BY giống câu A.

**💡 Từ khóa ghi nhớ:** `GROUP BY trường nào -> SELECT trường đó HOẶC dùng Hàm tổng hợp (MAX, MIN, SUM, COUNT...). Lệch sóng là oẳng!`

---

## Câu 112

**🔵 For which example task should a developer use a trigger rather than a workflow rule?**

- **A.** To set the Name field of an expense report record to Expense and the Date when it is saved ❌
- **B.** To send an email to a hiring manager when a candidate accepts a job offer ❌
- **C.** To notify an external system that a record has been modified ❌
- **D.** To set the primary Contact on an Account record when it is saved ✅

**📝 Dịch tiếng Việt:**
> Trường hợp nào lập trình viên bắt buộc phải sử dụng Trigger thay vì sử dụng Workflow Rule?

**💬 Giải thích gốc (English):**
> Workflow rules in Salesforce cannot update records of other objects. They are limited to actions like field updates, sending emails, creating tasks, and sending outbound messages within the same object.

**✅ Tại sao đáp án đúng:**
> Cập nhật trường 'Primary Contact' (trường lookup trỏ về Contact) trên Account khi bản ghi được lưu. Đây là hành động cập nhật chéo đối tượng từ Cha xuống Con. Workflow Rule đời cũ bất lực hoàn toàn trước yêu cầu này vì nó chỉ hỗ trợ cập nhật ngược từ Con lên Cha (Master-Detail) chứ không bao giờ cập nhật được từ Cha xuống Con. Bắt buộc phải dùng Trigger hoặc Flow Builder!

**❌ Tại sao đáp án sai:**
> **A.** Gán tên Expense Report có thể thực hiện cực kỳ dễ dàng bằng Workflow Rule field update.
> **B.** Gửi email nhắc nhở cho Hiring Manager là tính năng thế mạnh cơ bản của Workflow Email Alert.
> **C.** Gửi thông báo sang hệ thống ngoài có thể thực hiện thông qua Workflow Outbound Message không cần viết code.

**💡 Từ khóa ghi nhớ:** `Workflow Rule: Cấm cập nhật chéo đối tượng từ Cha xuống Con. Muốn làm -> Phải dùng Trigger / Flow!`

---

## Câu 113

**🔵 A developer must build an application that tracks which Accounts have purchased specific pieces of equipment that are represented as Products. Each Account could purchase many pieces of equipment. How should the developer track that an Account has purchased a piece of equipment?**

- **A.** Use the Asset object ✅
- **B.** Use a Master-Detail on Product to Account ❌
- **C.** Use a Custom object ❌
- **D.** Use a Lookup on Account to Product ❌

**📝 Dịch tiếng Việt:**
> Cần xây dựng ứng dụng theo dõi các Account đã mua các thiết bị cụ thể (được đại diện bằng Products). Mỗi Account có thể mua nhiều thiết bị. Lập trình viên nên làm gì để theo dõi việc này?

**💬 Giải thích gốc (English):**
> The Asset object in Salesforce is designed to represent specific products that customers have purchased. By using the Asset object, you can easily track each piece of equipment purchased by an Account, including details like purchase date, maintenance history, and more. This approach leverages Salesforce’s built-in functionality for managing customer assets, making it a robust and scalable solution.

**✅ Tại sao đáp án đúng:**
> Đối tượng tiêu chuẩn `Asset` (A) sinh ra trong Salesforce là để giải quyết bài toán này. Nó đại diện cho các sản phẩm (Products) cụ thể đã được khách hàng (Account/Contact) mua thực tế và đang sở hữu, giúp quản lý lịch sử thiết bị, bảo hành cực kỳ chuẩn bài.

**❌ Tại sao đáp án sai:**
> **B.** Tạo Master-Detail từ Product sang Account là sai logic nghiêm trọng vì một Product có thể được bán cho nhiều Account khác nhau, và Product không phải con của Account.
> **C.** Tạo Custom Object hoạt động được nhưng tốn công tự thiết kế lại bánh xe, phí của có sẵn.
> **D.** Đặt Lookup từ Account lên Product làm giới hạn 1 Account chỉ mua được tối đa 1 sản phẩm, trái yêu cầu mua nhiều thiết bị.

**💡 Từ khóa ghi nhớ:** `Khách hàng đã mua và sở hữu Sản phẩm thực tế -> Dùng đối tượng tiêu chuẩn ASSET!`

---

## Câu 114

**🔵 A developer is creating a page that allows users to create multiple Opportunities. The developer is asked to verify the current user’s default Opportunity record type, and set certain default values based on the record type before inserting the record. How can the developer find the current user’s default record type?**

- **A.** Use the Schema.userInfo.Opportunity.getDefaultRecordType() method. ❌
- **B.** Query the Profile where the ID equals userInfo.getProfileID() and then use the profile.Opportunity.getDefaultRecordType() method. ❌
- **C.** Create the opportunity and check the opportunity.recordType, which will have the record ID of the current user’s default record type, before inserting. ❌
- **D.** Use Opportunity.SObjectType.getDescribe().getRecordTypeInfos() to get a list of record types, and iterate through them until isDefaultRecordTypeMapping() is true. ✅

**📝 Dịch tiếng Việt:**
> Làm sao để tìm được cái Record Type mặc định của user hiện tại đối với object Opportunity bằng code Apex?

**💬 Giải thích gốc (English):**
> This method allows the developer to programmatically access the record type information and identify the default record type for the current user.

**✅ Tại sao đáp án đúng:**
> Cách làm chuẩn chỉ là dùng Schema Describe để lấy toàn bộ thông tin Record Type của Opportunity, sau đó duyệt qua danh sách và kiểm tra xem thằng nào có `isDefaultRecordTypeMapping()` trả về true. Đó chính là Record Type mặc định của user hiện tại.

**❌ Tại sao đáp án sai:**
> **A.** Cú pháp `Schema.userInfo.Opportunity.getDefaultRecordType()` hoàn toàn là hàng giả tưởng, không tồn tại trong Salesforce.
> **B.** Truy vấn Profile rồi gọi `profile.Opportunity.getDefaultRecordType()` cũng là tự vẽ ra phương thức không có thật.
> **C.** Khi khởi tạo bản ghi trong RAM (`new Opportunity()`), Salesforce không hề tự gán Record Type ID mặc định vào trường `RecordTypeId` đâu, trường đó sẽ bị null.

**💡 Từ khóa ghi nhớ:** `Đụng đến Record Type mặc định của User -> Dùng Schema Describe và duyệt `isDefaultRecordTypeMapping()`!`

---

## Câu 115

**🔵 Requirements state that a child record is deleted when its parent is deleted, and a child can be moved to a different parent when necessary. Which type of relationship should be built between the parent and child objects in Schema builder to support these requirements?**

- **A.** Master-Detail relationship ✅
- **B.** Child relationship ❌
- **C.** Lookup relationship from the parent to the child ❌
- **D.** Lookup relationship from the child to the parent ❌

**📝 Dịch tiếng Việt:**
> Yêu cầu nghiệp vụ: Bản ghi con tự động bị xóa khi cha bị xóa, và bản ghi con có thể chuyển sang cha khác khi cần (reparent). Nên xây dựng loại quan hệ nào giữa cha và con?

**💬 Giải thích gốc (English):**
> A Master-Detail relationship provides the following features that align with the given requirements:
> Automatic deletion of child records: When the parent record is deleted, all related child records are automatically deleted.
> Relocation of child records: By default, records can’t be reparented in master-detail relationships. Administrators can, however, allow child records in master-detail relationships on custom objects to be reparented to different parent records by selecting the Allow reparenting option in the master-detail relationship definition.

**✅ Tại sao đáp án đúng:**
> Mối quan hệ Master-Detail (A) là đáp án hoàn hảo nhất. Mối quan hệ này mặc định sẽ tự động xóa con khi cha bị xóa (Cascade Delete). Để đáp ứng thêm yêu cầu đổi cha cho con (reparent), ta chỉ cần tích chọn cấu hình 'Allow reparenting' trên trường quan hệ là xong ngay, cực kỳ mượt mà.

**❌ Tại sao đáp án sai:**
> **B.** 'Child relationship' không phải là một loại trường liên kết vật lý trong Salesforce Schema.
> **C.** Tạo Lookup ngược từ cha đến con là sai bét về mặt thiết kế cơ sở dữ liệu.
> **D.** Lookup từ con lên cha mặc định không tự động xóa con khi cha bị xóa (trừ khi viết thêm trigger phức tạp) và không có tính chất chặt chẽ của quan hệ Master-Detail.

**💡 Từ khóa ghi nhớ:** `Cha xóa -> Con bay màu + Cho phép đổi Cha = Master-Detail Relationship bật 'Allow reparenting'!`

---

## Câu 116

**🔵 A developer must modify the following code snippet to prevent the number of SOQL queries issued from exceeding the platform governor limit.
public class without sharing OpportunityService{
public static List<OpportunityLineItem> getOpportunityProducts (Set<Id> opportunityIds){
List<OpportunityLineItem> oppLineItems = new List<OpportunityLineItem>();
for(Id thisOppId : opportunityIds){
oppLineItems.addAll([Select Id FROM OpportunityLineItem WHERE OpportunityId = :thisOppId]);
}
return oppLineItems;
}
}
The above method might be called during a trigger execution via a Lightning component.
Which technique should be implemented to avoid reaching the governor limit?**

- **A.** Refactor the code above to perform the SOQL query only if the Set of opportunityIds contains less 100 Ids. ❌
- **B.** Use the System.Limits.getLimitQueries() method to ensure the number of queries is less than 100. ❌
- **C.** Refactor the code above to perform only one SOQL query, filtering by the Set of opportunityIds. ✅
- **D.** Use the System.Limits.getQueries() method to ensure the number of queries is less than 100. ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên cần sửa đoạn code dưới đây để tránh vượt quá giới hạn (governor limit) về số lượng SOQL queries: [getOpportunityProducts oppLineItems opportunityIds]

**💬 Giải thích gốc (English):**
> Refactor the code above to perform only one SOQL query, filtering by the Set of opportunityIds.
> This technique will significantly reduce the number of SOQL queries issued, as it combines all the individual queries into a single query, filtering by the entire Set of opportunityIds. This is much more efficient and helps to avoid reaching the governor limit.

**✅ Tại sao đáp án đúng:**
> Đoạn code cũ cực kỳ 'gà' khi nhét câu SOQL query vào bên trong vòng lặp For, khiến hệ thống bắn query liên tục cho mỗi Opportunity ID -> Dễ dàng ăn hành LimitException (100 SOQL). Kỹ thuật chuẩn (Bulkification) là lôi câu SOQL ra ngoài vòng lặp, chạy DUY NHẤT MỘT LẦN và lọc bằng toán tử `IN :opportunityIds` để lấy toàn bộ danh sách sản phẩm cùng lúc.

**❌ Tại sao đáp án sai:**
> **A.** Chỉ lọc dưới 100 ID là giải pháp chắp vá, nếu danh sách ID lớn hơn 100 thì code vẫn oẳng như thường.
> **B.** getLimitQueries() chỉ dùng để kiểm tra giới hạn còn lại, không giúp tối ưu hóa code hay ngăn chặn lỗi thực sự.
> **D.** getQueries() cũng chỉ để đếm số câu lệnh đã chạy, không có tác dụng refactor mã nguồn.

**💡 Từ khóa ghi nhớ:** `Quy tắc Bulkify tối thượng: Cấm nhét SOQL/DML vào vòng lặp For. Đưa ra ngoài và dùng toán tử IN!`

---

## Câu 117

**🔵 A developer must write an Apex method that will be called from a Lightning component. The method may delete an Account stored in the accountRec variable. Which method should a developer use to ensure only users that should be able to delete Accounts can successfully perform deletions?**

- **A.** Schema.sObjectType.Account.isDeletable() ✅
- **B.** Account.isDeletable() ❌
- **C.** accountRec.isDeletable() ❌
- **D.** accountRec.sObjectType.isDeletable() ❌

**📝 Dịch tiếng Việt:**
> Phương thức Apex xóa Account được gọi từ Lightning Component. Hàm nào giúp kiểm tra xem user hiện tại có quyền xóa Account hay không trước khi thực hiện xóa?

**💬 Giải thích gốc (English):**
> Schema.sObjectType.Account.isDeletable()
> This method checks if the current user has the necessary permissions to delete the Account object.

**✅ Tại sao đáp án đúng:**
> Sử dụng Schema Describe là cách chính thống để kiểm tra phân quyền CRUD của user trên đối tượng. Phương thức `Schema.sObjectType.Account.isDeletable()` (A) sẽ kiểm tra xem Profile/Permission Set của user hiện tại có được phép Xóa (Delete) Account hay không trước khi ta chạy lệnh DML `delete`.

**❌ Tại sao đáp án sai:**
> **B.** Cú pháp Account.isDeletable() sai cấu trúc gọi của lớp Schema Describe.
> **C.** Biến bản ghi accountRec không có phương thức trực tiếp .isDeletable().
> **D.** Cú pháp accountRec.sObjectType.isDeletable() là hàng giả tưởng, không biên dịch được.

**💡 Từ khóa ghi nhớ:** `Kiểm tra quyền CRUD của sObject -> Dùng cú pháp Schema Describe: `Schema.sObjectType.ObjectName.is[Createable/Accessible/Updateable/Deletable]()`!`

---

## Câu 118

**🔵 Which two statements are valid regarding Apex classes and interfaces? (Choose two.)**

- **A.** Classes are final by default. ✅
- **B.** Interface methods are public by default. ❌
- **C.** Inner classes are private by default. ✅
- **D.** A class can only have one inner class level. ❌

**📝 Dịch tiếng Việt:**
> Hai phát biểu nào sau đây là đúng về Apex class và interface? (Chọn 2)

**💬 Giải thích gốc (English):**
> Methods and classes are final by default. You can’t use the final keyword in the declaration of a class or method. This means they can’t be overridden. Use the virtual keyword if you need to override a method or class.

**✅ Tại sao đáp án đúng:**
> A đúng vì mặc định mọi Apex class đều là `final` (tức là không cho phép class khác kế thừa/extend), trừ khi mày khai báo nó với từ khóa `virtual` hoặc `abstract`. C đúng vì các Inner class (class con nằm trong class cha) mặc định có modifier là `private` trừ khi được khai báo tường minh là public/global.

**❌ Tại sao đáp án sai:**
> **B.** Các phương thức trong Interface mặc định là public chứ không cần phải khai báo, nhưng ý A và C là hai phát biểu chính xác và trọn vẹn nhất trong tài liệu chính thống.
> **D.** Một lớp có thể có nhiều cấp lớp bên trong (Inner class) lồng nhau chứ không bị giới hạn chỉ một cấp duy nhất.

**💡 Từ khóa ghi nhớ:** `Apex Class mặc định = Final (cấm kế thừa). Inner Class mặc định = Private!`

---

## Câu 119

**🔵 What is a benefit of using an after insert trigger over using a before insert trigger?**

- **A.** An after insert trigger allows a developer to bypass validation rules when updating fields on the new record. ❌
- **B.** An after insert trigger allows a developer to insert other objects that reference the new record. ✅
- **C.** An after insert trigger allows a developer to make a callout to an external service. ❌
- **D.** An after insert trigger allows a developer to modify fields in the new record without a query. ❌

**📝 Dịch tiếng Việt:**
> Lợi ích lớn nhất của việc sử dụng trigger 'after insert' so với trigger 'before insert' là gì?

**💬 Giải thích gốc (English):**
> In an after insert trigger, the record has already been committed to the database, so you can safely reference its ID and use it to create or update other related objects.

**✅ Tại sao đáp án đúng:**
> Ở sự kiện 'after insert', bản ghi mới đã thực sự được tạo và cấp ID chính thức từ database. Nhờ có cái ID xịn sò này, ta mới có thể tạo các bản ghi con ở đối tượng khác và gán ID đó vào trường Lookup của chúng để liên kết dữ liệu. Còn ở sự kiện 'before insert', bản ghi chưa hề có ID nên chịu chết không làm việc này được.

**❌ Tại sao đáp án sai:**
> **A.** Trigger không bao giờ giúp bypass được Validation Rules của hệ thống dù là before hay after.
> **C.** Cả hai loại trigger đều cấm gọi API (callout) trực tiếp, bắt buộc phải dùng phương thức bất đồng bộ với `@future(callout=true)`.
> **D.** Thay đổi các trường của chính bản ghi đó mà không cần DML update là đặc quyền của trigger 'before insert', trigger after làm thế sẽ dính lỗi Read-only ngay.

**💡 Từ khóa ghi nhớ:** `Cần ID bản ghi cha để tạo bản ghi con liên quan -> Bắt buộc dùng AFTER INSERT trigger!`

---

## Câu 120

**🔵 An org has an existing Visual Flow that creates an Opportunity with an Update Records element. A developer must update the Visual Flow to also create a Contact and store the created Contact's ID on the Opportunity. Which update should the developer make in the Visual Flow?**

- **A.** Add a new Create Records element. ✅
- **B.** Add a new Quick Action (of type Create) element. ❌
- **C.** Add a new Update Records element. ❌
- **D.** Add a new Get Records element. ❌

**📝 Dịch tiếng Việt:**
> Một Flow đã có sẵn logic cập nhật Opportunity. Cần nâng cấp Flow để tạo thêm mới một Contact và lưu ID của Contact mới đó lên Opportunity. Lập trình viên nên thêm phần tử nào vào Flow?

**💬 Giải thích gốc (English):**
> A. Add a new Create Records element.
> This element will allow the flow to create a new Contact record. After creating the Contact, the flow can then store the Contact’s ID in a variable. This variable can be used in an Update Records element to update the Opportunity with the Contact’s ID

**✅ Tại sao đáp án đúng:**
> Muốn tạo mới một bản ghi (Contact) trong Flow thì phần tử chuẩn không cần chỉnh là 'Create Records' (A). Phần tử này sau khi tạo xong Contact sẽ tự động trả về ID của bản ghi vừa tạo vào một biến để ta dùng cập nhật ngược lên trường liên quan của Opportunity ở bước tiếp theo.

**❌ Tại sao đáp án sai:**
> **B.** Quick Action kiểu Create dùng để mở pop-up nhập liệu ngoài UI, không phù hợp cho luồng tự động hóa chạy ngầm của Flow.
> **C.** Update Records chỉ dùng để sửa đổi bản ghi đã có sẵn, không thể dùng để tạo mới bản ghi Contact từ con số không.
> **D.** Get Records dùng để tìm kiếm, truy vấn bản ghi có sẵn chứ không có tuổi tạo mới dữ liệu.

**💡 Từ khóa ghi nhớ:** `Muốn tạo mới bản ghi trong Flow -> Gọi tên Create Records Element!`

---

## Câu 121

**🔵 Universal Containers wants Opportunities to be locked from editing when reaching the Closed/Won stage. Which two strategies should a developer use to accomplish this? (Choose two.)**

- **A.** Use a Flow Builder. ❌
- **B.** Use a validation rule. ✅
- **C.** Use the Process Automation Settings. ❌
- **D.** Mark fields as read-only on the page layout. ✅

**📝 Dịch tiếng Việt:**
> Universal Containers muốn khóa các Opportunity không cho phép chỉnh sửa khi đã chuyển sang trạng thái Closed/Won. Hai chiến lược nào lập trình viên nên sử dụng để thực hiện việc này? (Chọn 2)

**💬 Giải thích gốc (English):**
> B. Use a validation rule: This can prevent users from making changes to Opportunities once they reach the Closed/Won stage by setting up a rule that triggers an error message if any edits are attempted.
> D. Mark fields as read-only on the page layout: By marking the Opportunity fields as read-only on the page layout, users will be unable to edit them directly. This can be combined with the Flow Builder approach to provide a more comprehensive solution.

**✅ Tại sao đáp án đúng:**
> B đúng vì Validation Rule là lá chắn thép no-code chặn đứng mọi hành vi bấm Save khi cố chỉnh sửa bản ghi đã Closed/Won. D đúng vì Page Layout cho phép thiết lập các trường thành Read-Only động dựa trên Record Type của trạng thái Closed/Won để khóa cứng giao diện của user.

**❌ Tại sao đáp án sai:**
> **A.** Flow Builder chạy ngầm ở backend sau khi dữ liệu đã gửi đi, không thể khóa giao diện trực quan hay chặn nhập liệu tối ưu như Validation Rule.
> **C.** Process Automation Settings chỉ là nơi bật/tắt cấu hình chung của hệ thống tự động hóa, tuổi gì khóa được bản ghi.

**💡 Từ khóa ghi nhớ:** `Khóa bản ghi (Read-only) -> 1. Validation Rule (Chặn lưu); 2. Page Layout Read-only (Khóa UI).`

---

## Câu 122

**🔵 Which action can a developer take to reduce the execution time of the following code?
List<Account> allAccounts = [SELECT Id FROM Account];
List<Contact> allContacts = [SELECT Id, AccountId FROM Contact];
for(Account a : allAccounts){
for(Contact c: allContacts){
if(c.AccountId = a.Id){
//do work
}
}
}**

- **A.** Put the Account loop inside the Contact loop. ❌
- **B.** Create an Apex helper class for SOQL. ❌
- **C.** Add a GROUP BY clause to the Contact SOQL. ❌
- **D.** Use a Map<Id List<Contact> for allContacts. ✅

**📝 Dịch tiếng Việt:**
> Hành động nào giúp lập trình viên tối ưu hóa và giảm thời gian thực thi của đoạn mã lặp lồng nhau dưới đây? [Code Nested Loops]

**💬 Giải thích gốc (English):**
> By using a Map<Id, List<Contact>>, you can efficiently group the contacts by their AccountId. This allows you to avoid the nested loops and directly access the contacts related to each account, significantly reducing the number of iterations and improving performance.

**✅ Tại sao đáp án đúng:**
> Sử dụng Map<Id, List<Contact>> (D) gom nhóm Contact theo AccountId trước. Thay vì duyệt 2 vòng lặp lồng nhau cực kỳ gà mờ với độ phức tạp O(N*M), ta chỉ cần duyệt Account rồi dùng Map.get(accountId) hốt ngay list Contact con trong 1 nốt nhạc với độ phức tạp O(N). CPU sẽ cảm ơn mày rất nhiều!

**❌ Tại sao đáp án sai:**
> **A.** Nhét vòng lặp Account vào trong Contact thì độ phức tạp vẫn là O(N*M), chả thay đổi được bản chất gì cả.
> **B.** Viết helper class chỉ làm code trông 'sạch sẽ' hơn chứ thuật toán cùi bắp bên trong vẫn chạy chậm như rùa.
> **C.** Thêm GROUP BY vào SOQL không giúp giải quyết bài toán map dữ liệu con vào cha trong RAM.

**💡 Từ khóa ghi nhớ:** `Tối ưu For lồng nhau (Nested loops) -> Gom danh sách con vào MAP theo ID cha để lấy cực nhanh O(1).`

---

## Câu 123

**🔵 Which three tools can deploy metadata to production? (Choose three.)**

- **A.** Change Set from Developer Org ❌
- **B.** Force.com IDE ✅
- **C.** Data Loader ❌
- **D.** Change Set from Sandbox ✅
- **E.** Metadata API ✅

**📝 Dịch tiếng Việt:**
> Ba công cụ nào sau đây hỗ trợ deploy metadata (cấu hình/code) lên môi trường Production? (Chọn 3)

**💬 Giải thích gốc (English):**
> Change Set from Sandbox: This is a common method for deploying metadata changes from a sandbox environment to a production environment1.
> Force.com IDE: This integrated development environment allows developers to manage and deploy metadata changes.
> Metadata API: This API is designed for deploying metadata changes programmatically, making it a powerful tool for managing customizations.

**✅ Tại sao đáp án đúng:**
> B đúng vì Force.com IDE (dù đã cũ nhưng đề vẫn tính) hỗ trợ kết nối và deploy metadata. D đúng vì Change Set gửi từ Sandbox liên kết sang Production cực kỳ phổ biến. E đúng vì Metadata API là nền tảng cốt lõi cho phép deploy thông qua các công cụ như SFDX CLI / Ant Migration Tool.

**❌ Tại sao đáp án sai:**
> **A.** Change Set chỉ có thể gửi giữa các Org có liên kết với nhau (ví dụ Sandbox lên Production của cùng một doanh nghiệp), cấm cửa Developer Org cá nhân tự do gửi thẳng lên Production khác.
> **C.** Data Loader chỉ biết chơi với DATA bản ghi (insert, update record), hoàn toàn mù tịt về METADATA (code, field, object). Đừng nhầm lẫn tai hại nhé!

**💡 Từ khóa ghi nhớ:** `Deploy METADATA -> Change Set Sandbox, Metadata API (CLI), IDE. Data Loader chỉ dùng cho DATA bản ghi!`

---

## Câu 124

**🔵 Universal Containers is building a recruiting app with an Applicant object that stores information about an individual person and a Job object that represents a job. Each applicant may apply for more than one job. What should a developer implement to represent that an applicant has applied for a job?**

- **A.** Lookup field from Applicant to Job ❌
- **B.** Junction object between Applicant and Job ✅
- **C.** Master-detail field from Applicant to Job ❌
- **D.** Formula field on Applicant that references Job ❌

**📝 Dịch tiếng Việt:**
> Universal Containers xây dựng app tuyển dụng gồm object Applicant (ứng viên) và Job (công việc). Một ứng viên có thể ứng tuyển nhiều Job, một Job có nhiều ứng viên ứng tuyển. Thiết kế mối quan hệ nào phù hợp nhất?

**💬 Giải thích gốc (English):**
> A junction object is used to create a many-to-many relationship between two objects. In this case, since each applicant can apply for multiple jobs and each job can have multiple applicants, a junction object is the most appropriate solution. This junction object would have two master-detail relationships: one to the Applicant object and one to the Job object.

**✅ Tại sao đáp án đúng:**
> Đây là mối quan hệ Nhiều-Nhiều (Many-to-Many): một ứng viên ứng tuyển nhiều Job và một Job có nhiều ứng viên. Cách giải quyết chuẩn sách giáo khoa là tạo một đối tượng trung gian gọi là Junction Object (B) liên kết giữa Applicant và Job thông qua 2 trường Master-Detail trỏ về 2 phía.

**❌ Tại sao đáp án sai:**
> **A.** Tạo Lookup trực tiếp từ Applicant sang Job sẽ giới hạn mỗi ứng viên chỉ được ứng tuyển tối đa 1 Job tại một thời điểm, siêu gà mờ và sai nghiệp vụ.
> **C.** Tương tự A, tạo Master-Detail trực tiếp từ Applicant sang Job giới hạn nghiêm trọng quan hệ 1-Nhiều một chiều.
> **D.** Formula field chỉ dùng để hiển thị giá trị tính toán đọc, không có khả năng đại diện cho quan hệ Nhiều-Nhiều vật lý phức tạp.

**💡 Từ khóa ghi nhớ:** `Mối quan hệ Nhiều-Nhiều (Many-to-Many) -> Bắt buộc tạo đối tượng trung gian JUNCTION OBJECT.`

---

## Câu 125

**🔵 The sales team at Universal Containers would like to see a visual indicator appear on both Account and Opportunity page layouts to alert sales people when an Account is late making payments or has entered the collections process. What can a developer implement to achieve this requirement without having to write custom code?**

- **A.** Formula Field ✅
- **B.** Workflow Rule ❌
- **C.** Quick Action ❌
- **D.** Roll-up Summary Field ❌

**📝 Dịch tiếng Việt:**
> Sales team muốn hiển thị chỉ báo trực quan trên giao diện Account và Opportunity để cảnh báo khi Account bị nợ quá hạn hoặc rơi vào trạng thái đòi nợ. Giải pháp nào đáp ứng không cần viết code?

**💬 Giải thích gốc (English):**
> A formula field can be used to create a visual indicator on both the Account and Opportunity page layouts. This field can be configured to display a specific value or image based on the criteria you set, such as when an account is late making payments or has entered the collections process.

**✅ Tại sao đáp án đúng:**
> Formula Field (A) kiểu Text kết hợp với hàm IMAGE() là cứu cánh số một. Nó cho phép mày viết logic kiểm tra trạng thái và hiển thị các hình ảnh cảnh báo (icon đỏ, vàng, xanh) cực kỳ sinh động, sinh quan ngay trên giao diện mà hoàn toàn no-code.

**❌ Tại sao đáp án sai:**
> **B.** Workflow Rule chỉ chạy ngầm backend để cập nhật dữ liệu, gửi email chứ không thể render hình ảnh lên giao diện.
> **C.** Quick Action để tạo nút bấm thao tác nhanh, không phải công cụ hiển thị chỉ báo cảnh báo động.
> **D.** Roll-up Summary Field chỉ biết tính tổng, đếm số bản ghi con chứ không hiển thị hình ảnh trực quan được.

**💡 Từ khóa ghi nhớ:** `Hiển thị icon/ảnh cảnh báo động không code -> Sử dụng Formula Field chứa hàm IMAGE()!`

---

## Câu 126

**🔵 Which governor limit applies to all the code in an Apex transaction?**

- **A.** Elapsed SOQL query time ❌
- **B.** Number of classes called ❌
- **C.** Number of new records created ❌
- **D.** Elapsed CPU time ✅

**📝 Dịch tiếng Việt:**
> Giới hạn (governor limit) nào sau đây áp dụng chung cho TOÀN BỘ mã code thực thi trong một transaction Apex?

**💬 Giải thích gốc (English):**
> The elapsed CPU time is the governor limit that applies to all the code in an Apex transaction. This means that the total amount of time the CPU spends executing your Apex code must be within the specified limit.
> The other options are also governor limits, but they apply to specific aspects of Apex code
> A. Elapsed SOQL query time: This limit restricts the amount of time spent executing SOQL queries.
> B. Number of classes called: This limit restricts the number of different classes that can be called within a transaction.
> C. Number of new records created: This limit restricts the number of new records that can be created in a transaction.

**✅ Tại sao đáp án đúng:**
> Tổng thời gian xử lý CPU - Elapsed CPU time (D) (giới hạn 10 giây cho transaction đồng bộ và 60 giây cho bất đồng bộ) là giới hạn bao trùm. Nó tính tổng thời gian chạy của tất cả class Apex, Trigger, Flow, Validation Rules,... trong cùng một transaction. Quá 10s là oẳng!

**❌ Tại sao đáp án sai:**
> **A.** Thời gian truy vấn SOQL chỉ tính riêng cho các câu lệnh SELECT, không bao quát toàn bộ logic xử lý của CPU.
> **B.** Salesforce không thèm giới hạn số lượng class mày gọi trong một transaction, gọi bao nhiêu tùy thích miễn không quá CPU time.
> **C.** Số lượng bản ghi mới tạo được giới hạn bởi DML row (10,000) chứ không phải giới hạn bao trùm toàn transaction Apex.

**💡 Từ khóa ghi nhớ:** `Giới hạn bao trùm toàn bộ transaction Apex -> Tổng thời gian xử lý CPU (10 giây đồng bộ).`

---

## Câu 127

**🔵 Which two sfdx commands can be used to add testing data to a Developer sandbox? (Choose two.)**

- **A.** force:data:async:upsert ❌
- **B.** force:data:tree:import ✅
- **C.** force:data:bulk:upsert ✅
- **D.** force:data:object:create ❌

**📝 Dịch tiếng Việt:**
> Hai lệnh SFDX nào sau đây có thể sử dụng để nạp dữ liệu test vào Developer Sandbox? (Chọn 2)

**💬 Giải thích gốc (English):**
> force:data:tree:import - This command is used to import data from a JSON file into Salesforce, which is useful for hierarchical data.
> force:data:bulk:upsert - This command allows you to upsert (update or insert) large volumes of data in bulk.

**✅ Tại sao đáp án đúng:**
> B đúng vì `force:data:tree:import` chuyên trị nạp dữ liệu từ các file JSON giữ nguyên được mối quan hệ cha-con (Object Tree). C đúng vì `force:data:bulk:upsert` hỗ trợ nạp đống dữ liệu lớn từ file CSV cực kỳ bá đạo thông qua Bulk API.

**❌ Tại sao đáp án sai:**
> **A.** Đây là lệnh ảo, Salesforce CLI làm gì có cái lệnh nào tên là `force:data:async:upsert` đâu.
> **D.** Lệnh này dùng để tạo metadata định nghĩa đối tượng chứ không dùng để nạp data bản ghi.

**💡 Từ khóa ghi nhớ:** `SFDX nạp Data -> Tree (JSON quan hệ cha-con) hoặc Bulk (CSV bản ghi lớn).`

---

## Câu 128

**🔵 A developer wants to override a button using Visualforce on an object. What is the requirement?**

- **A.** The controller or extension must have a PageReference method. ❌
- **B.** The standardController attribute must be set to the object. ✅
- **C.** The action attribute must be set to a controller method. ❌
- **D.** The object record must be instantiated in a controller or extension. ❌

**📝 Dịch tiếng Việt:**
> Để ghi đè (override) một nút bấm chuẩn (standard button) bằng Visualforce trên một đối tượng, trang đó có yêu cầu bắt buộc gì?

**💬 Giải thích gốc (English):**
> In Visualforce, if a developer wants to override a standard button with a custom Visualforce page on an object, they need to specify the standardController attribute in the apex:page component.

**✅ Tại sao đáp án đúng:**
> B đúng vì trang Visualforce bắt buộc phải khai báo thuộc tính `standardController` trỏ tới đối tượng đó (ví dụ: `standardController="Account"`). Điều này giúp trang nhận diện ngữ cảnh dữ liệu và trỏ đúng nút bấm cần ghi đè.

**❌ Tại sao đáp án sai:**
> **A.** Controller không bắt buộc phải có phương thức trả về PageReference mới ghi đè nút được.
> **C.** Thuộc tính action trên thẻ apex:page dùng để tự kích hoạt hàm khi trang tải, không phải điều kiện bắt buộc để override nút.
> **D.** Không cần khởi tạo thủ công bản ghi trong code vì standard controller đã tự động lo liệu chuyện này.

**💡 Từ khóa ghi nhớ:** `Ghi đè nút chuẩn (Override button) bằng Visualforce -> Bắt buộc trang phải có thuộc tính standardController.`

---

## Câu 129

**🔵 A Visualforce page is required for displaying and editing Case records that includes both standard and custom functionality defined in an Apex class called myControllerExtension. The Visualforce page should include which attribute(s) to correctly implement controller functionality?**

- **A.** controller="Case" and extensions="myControllerExtension" ❌
- **B.** extensions="myControllerExtension" ❌
- **C.** controller="myControllerExtension" ❌
- **D.** standardController="Case" and extensions="myControllerExtension" ✅

**📝 Dịch tiếng Việt:**
> Một trang Visualforce hiển thị và chỉnh sửa Case kết hợp tính năng chuẩn của Case và các hàm tùy chỉnh viết trong class Apex 'myControllerExtension'. Trang Visualforce cần khai báo thuộc tính nào?

**💬 Giải thích gốc (English):**
> standardController="Case": This attribute specifies that the Visualforce page is associated with the standard Case object. This means that the page will have access to standard Case fields and methods.
> extensions="myControllerExtension": This attribute specifies that the page will use the custom controller class myControllerExtension. This allows you to add custom functionality to the page, such as custom buttons, actions, or validation rules.

**✅ Tại sao đáp án đúng:**
> Khai báo kết hợp `standardController="Case"` đi kèm `extensions="myControllerExtension"` (D). Đây là mô hình Controller Extension chuẩn để vừa dùng được các tính năng lưu/sửa mặc định của Case vừa gọi được logic custom của extension class.

**❌ Tại sao đáp án sai:**
> **A.** Case là đối tượng tiêu chuẩn, cấm khai báo bằng từ khóa `controller` (từ khóa này chỉ dành cho Custom Controller class).
> **B.** Thiếu standardController thì extensions không thể tự dưng hoạt động một mình được.
> **C.** Đưa extension class vào thuộc tính `controller` là sai bét vai trò của lớp mở rộng.

**💡 Từ khóa ghi nhớ:** `Visualforce mở rộng tính năng Standard -> standardController='ObjectName' + extensions='ExtensionClass'.`

---

## Câu 130

**🔵 A lead object has a custom field Prior_Email__c.
The following trigger is intended to copy the current Email into the Prior_Email__c field any time the Email field is changed:
trigger test on Lead (before update) {
for(Lead Id: trigger.new){
if(Id.Email != trigger.oldMap.get(Id.id).email){
Id.Prior_Email__c = trigger.oldMap.get(Id.id).email;
Update Id;
}
}
}
Which type of exception will this trigger cause?**

- **A.** A null reference exception ❌
- **B.** A compile time exception ❌
- **C.** A DML exception ✅
- **D.** A limit exception when doing a bulk update ❌

**📝 Dịch tiếng Việt:**
> Object Lead có trường Prior_Email__c. Trigger dưới đây viết ở sự kiện 'before update', lặp qua trigger.new và gọi lệnh 'Update Id;' [Code Trigger]. Trigger này sẽ gây ra loại lỗi (exception) nào?

**💬 Giải thích gốc (English):**
> The update statement inside the for loop attempts to perform a DML operation on the same record that is currently being processed in a before update trigger. Salesforce does not allow DML operations on records that are already in the process of being updated, leading to a DML exception.
> Exception:
> System.SObjectException: DML statement cannot operate on trigger.new or trigger.old

**✅ Tại sao đáp án đúng:**
> Gây ra lỗi DML Exception (C). Salesforce cấm tiệt việc gọi các câu lệnh DML như `update` trên chính các bản ghi đang nằm trong vòng đời xử lý 'before' (trigger.new), vì việc này sẽ gây ra vòng lặp vô hạn (recursive) vô phương cứu chữa và làm sập hệ thống.

**❌ Tại sao đáp án sai:**
> **A.** Biến Id được duyệt qua trigger.new luôn tồn tại bản ghi, không gây ra lỗi tham chiếu null.
> **B.** Code viết đúng cú pháp Apex nên biên dịch thành công, lỗi chỉ nổ ra khi thực thi (runtime).
> **D.** Lỗi xảy ra ngay lập tức ở bản ghi đầu tiên khi gọi lệnh Update chứ không đợi đến khi bulk update chạm limit.

**💡 Từ khóa ghi nhớ:** `Cấm kỵ tối thượng: Gọi lệnh DML (insert/update/delete) trên chính các bản ghi đang xử lý trong trigger before!`

---

## Câu 131

**🔵 What is the result of the following code?
Account a = new Account();
Database.insert(a, false);**

- **A.** The record will be created and no error will be reported. ❌
- **B.** The record will not be created and no error will be reported. ✅
- **C.** The record will be created and a message will be in the debug log. ❌
- **D.** The record will not be created and an exception will be thrown. ❌

**📝 Dịch tiếng Việt:**
> Kết quả của đoạn code khởi tạo và insert một Account trống bằng phương thức `Database.insert(a, false)` là gì?

**💬 Giải thích gốc (English):**
> The allOrNone parameter specifies whether the operation allows partial success.
> If allOrNone is set to false and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify which records succeeded or failed.
> If allOrNone is set to true and the method isn’t successful, an exception is thrown. The default for the parameter is true.

**✅ Tại sao đáp án đúng:**
> Tạo Account trống thì chắc chắn hẹo vì thiếu trường bắt buộc Name. Tuy nhiên, tham số thứ hai là `allOrNone = false` có tác dụng 'nuốt giận làm lành': nó không ném ra Exception làm chết chương trình mà âm thầm trả về kết quả lỗi trong đối tượng Database.SaveResult. Nên đáp án B đúng: bản ghi không được tạo và không có Exception nào bắn ra ngoài cả.

**❌ Tại sao đáp án sai:**
> **A.** Bản ghi bị thiếu Name nên không đời nào được tạo thành công.
> **C.** Bản ghi bị thiếu Name nên không thể tạo thành công bất kể cấu hình log.
> **D.** Exception bị nuốt chửng rồi nhờ có tham số `false` vi diệu kia.

**💡 Từ khóa ghi nhớ:** `Database.insert(..., false): Im lặng là vàng (lỗi không bắn Exception, bản ghi hỏng thì không tạo).`

---

## Câu 132

**🔵 An after trigger on the Account object performs a DML update operation on all of the child Opportunities of an Account. There are no active triggers on the Opportunity object, yet a 'maximum trigger depth exceeded' error occurs in certain situations. Which two reasons possibly explain the Account trigger firing recursively? (Choose two.)**

- **A.** Changes to Opportunities are causing cross-object workflow field updates to be made on the Account. ✅
- **B.** Changes to Opportunities are causing roll-up summary fields to update on the Account. ✅
- **C.** Changes are being made to the Account during an unrelated parallel save operation. ❌
- **D.** Changes are being made to the Account during Criteria Based Sharing evaluation. ❌

**📝 Dịch tiếng Việt:**
> Trigger 'after' trên Account thực hiện DML update toàn bộ Opportunity con. Không có trigger nào trên Opportunity, nhưng lỗi đệ quy trigger 'maximum trigger depth exceeded' vẫn xảy ra. Hai lý do nào giải thích việc này? (Chọn 2)

**💬 Giải thích gốc (English):**
> The two reasons that could possibly explain the Account trigger firing recursively are:
> Cross-object workflow field updates can trigger the Account trigger again if the workflow rule updates a field on the Account.
> Roll-up summary fields on the Account that aggregate data from child Opportunities can cause the Account trigger to fire again when these fields are recalculated.

**✅ Tại sao đáp án đúng:**
> A đúng vì việc cập nhật Opportunity có thể kích hoạt một Cross-Object Workflow Field Update cập nhật ngược từ Con lên Cha (Account), khiến trigger Account nổ lần nữa. B đúng vì cập nhật Opportunity con làm thay đổi giá trị của trường Roll-Up Summary trên Account cha, Salesforce tự động kích hoạt vòng Save Account và nổ trigger Account lần nữa. Hai trường hợp này tạo thành vòng lặp vô hạn chéo cha-con.

**❌ Tại sao đáp án sai:**
> **C.** Lưu song song song không tạo ra chuỗi đệ quy tuần hoàn khép kín làm vượt độ sâu trigger.
> **D.** Criteria Based Sharing chỉ tính toán phân quyền chia sẻ, không kích hoạt tiến trình Save hay chạy trigger.

**💡 Từ khóa ghi nhớ:** `Lỗi đệ quy chéo Cha-Con: Do 1. Roll-up Summary trên Cha; 2. Cross-object Workflow cập nhật ngược lên Cha.`

---

## Câu 133

**🔵 A developer has the following class and trigger code.
public class InsuranceRates{
public static final Decimal smokerCharge = 0.01;
}
trigger ContactTrigger on Contact(before insert){
InsuranceRates rates = new InsuranceRates();
Decimal baseCost = XXX;
}
Which code segment should a developer insert at the XXX to set the baseCost variable to the value of the class variable smokerCharge?**

- **A.** InsuranceRates.smokerCharge ✅
- **B.** rates.getSmokerCharge() ❌
- **C.** ContactTrigger.InsuranceRates.smokerCharge ❌
- **D.** rates.smokerCharge ❌

**📝 Dịch tiếng Việt:**
> Cho class InsuranceRates chứa biến tĩnh 'public static final Decimal smokerCharge = 0.01;'. Trong trigger ContactTrigger dưới đây, điền gì vào XXX để gán giá trị của smokerCharge cho biến baseCost? [InsuranceRates]

**💬 Giải thích gốc (English):**
> The smokerCharge variable is declared as a static variable in the InsuranceRates class. Static variables belong to the class itself rather than any instance of the class, so you access it using the class name InsuranceRates

**✅ Tại sao đáp án đúng:**
> Vì `smokerCharge` được khai báo là biến tĩnh (`static`), nó thuộc về chính class chứ không thuộc về bất kỳ đối tượng instance nào. Cách truy cập chuẩn là dùng trực tiếp tên lớp: `ClassName.staticVariableName` -> `InsuranceRates.smokerCharge` (A).

**❌ Tại sao đáp án sai:**
> **B.** Biến smokerCharge là public trực tiếp, không cần hàm getter để lấy và class cũng không định nghĩa hàm này.
> **C.** Điền thêm tên Trigger vào trước tên Class là cú pháp tự chế, Salesforce không chơi.
> **D.** Gọi thông qua đối tượng instance `rates` vừa khởi tạo là sai kỹ thuật, Apex sẽ quăng lỗi compile ngay lập tức.

**💡 Từ khóa ghi nhớ:** `Biến tĩnh (Static variable) -> Luôn truy cập trực tiếp bằng tên Class: ClassName.VariableName!`

---

## Câu 134

**🔵 How should a developer prevent a recursive trigger?**

- **A.** Use a one trigger per object pattern. ❌
- **B.** Use a static Boolean variable. ✅
- **C.** Use a trigger handler. ❌
- **D.** Use a private Boolean variable. ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên nên làm thế nào để ngăn chặn lỗi trigger chạy đệ quy vô hạn (recursive trigger)?

**💬 Giải thích gốc (English):**
> What is a Recursive Trigger: A recursive trigger is one that performs an action, such as an update or insert, which causes the trigger to invoke itself, often due to an update it performs.
> How to Avoid Recursive Triggers: To prevent recursive triggers, you can create a class with a static Boolean variable initialized to true. In the trigger, before executing your code, check if the variable is true. If it is, proceed with your code and then set the variable to false.

**✅ Tại sao đáp án đúng:**
> Sử dụng một biến tĩnh kiểu Boolean - static Boolean variable (B) trong một class helper (ví dụ: `public static Boolean isFirstRun = true`) là giải pháp kinh điển. Ta kiểm tra biến này ở đầu trigger, chạy xong gán bằng `false` để chặn các vòng chạy đệ quy sau.

**❌ Tại sao đáp án sai:**
> **A.** One trigger per object chỉ giúp gom code gọn gàng quản lý chứ không có cơ chế tự chặn đệ quy.
> **C.** Trigger Handler chỉ tách code ra class khác chứ không tự chặn đệ quy nếu thiếu biến static.
> **D.** Biến private Boolean sẽ bị khởi tạo lại từ đầu mỗi khi trigger kích hoạt ở vòng mới, hoàn toàn vô dụng để chặn đệ quy.

**💡 Từ khóa ghi nhớ:** `Chặn Trigger đệ quy (Recursive) -> Luôn sử dụng biến STATIC BOOLEAN trong class helper!`

---

## Câu 135

**🔵 What is a capability of the tag that is used for loading external Javascript libraries in Lightning Component? (Choose three.)**

- **A.** Loading files from Documents. ❌
- **B.** One-time loading for duplicate scripts. ✅
- **C.** Specifying loading order. ✅
- **D.** Loading scripts in parallel. ✅
- **E.** Loading externally hosted scripts. ❌

**📝 Dịch tiếng Việt:**
> Ba tính năng nổi bật của thẻ <ltng:require> dùng để tải các thư viện JavaScript bên ngoài trong Aura Component là gì? (Chọn 3)

**💬 Giải thích gốc (English):**
> Loading Order
> The scripts are loaded in the order that they are listed.
> One-Time Loading
> Scripts load only once, even if they’re specified in multiple <ltng:require> tags in the same component or across different components.
> Parallel Loading
> Use separate <ltng:require> tags for parallel loading if you have multiple sets of scripts that are not dependent on each other.

**✅ Tại sao đáp án đúng:**
> B đúng vì nó chỉ tải script duy nhất một lần dù được khai báo trùng lặp ở nhiều component con khác nhau. C đúng vì cho phép chỉ định thứ tự tải (loading order) các script theo danh sách liệt kê để tránh lỗi phụ thuộc thư viện (dependency). D đúng vì hỗ trợ tải song song (parallel) các bộ script độc lập để tối ưu tốc độ load trang.

**❌ Tại sao đáp án sai:**
> **A.** Thẻ này chỉ tải file từ Static Resource chứ không tải trực tiếp từ thư mục Documents cũ kỹ.
> **E.** Vì lý do bảo mật CSP cực kỳ nghiêm ngặt, Salesforce cấm tải trực tiếp các script lưu trữ bên ngoài hệ thống, bắt buộc phải upload vào Static Resource trước.

**💡 Từ khóa ghi nhớ:** `<ltng:require> (Aura) / platformResourceLoader (LWC): Tải script từ STATIC RESOURCE, hỗ trợ tải 1 lần và chỉ định thứ tự tải.`

---

## Câu 136

**🔵 Universal Containers (UC) wants to lower its shipping cost while making the shipping process more efficient. The Distribution Officer advises UC to implement global addresses to allow multiple Accounts to share a default pickup address. The developer is tasked to create the supporting object and relationship for this business requirement and uses the Setup Menu to create a custom object called 'Global Address'. Which field should the developer add to create the most efficient model that supports the business need?**

- **A.** Add a Master-Detail field on the Global Address object to the Account object. ❌
- **B.** Add a Master-Detail field on the Account object to the Global Address object. ❌
- **C.** Add a Lookup field on the Global Address object to the Account object. ❌
- **D.** Add a Lookup field on the Account object to the Global Address object. ✅

**📝 Dịch tiếng Việt:**
> Mối quan hệ nào là tối ưu nhất để nhiều Account dùng chung 1 địa chỉ default Pickup Address từ custom object 'Global Address'?

**💬 Giải thích gốc (English):**
> Since a standard object like Account cannot be a detail in a Master-Detail Relationship, we should use a Lookup Relationship instead. To allow multiple Accounts to share a default pickup address, add a Lookup field on the Account object that points to the Global Address object. This setup enables each Account to reference a Global Address, supporting the business need by enhancing shipping efficiency and reducing costs.

**✅ Tại sao đáp án đúng:**
> Thêm trường Lookup trên Account trỏ đến đối tượng Global Address (D). Thiết kế này cho phép nhiều Account dùng chung 1 địa chỉ (quan hệ 1-Nhiều từ Global Address sang Account). Đồng thời, Account là Standard Object nên cấm ngặt không được làm con (Detail) trong mối quan hệ Master-Detail với một Custom Object.

**❌ Tại sao đáp án sai:**
> **A.** Master-Detail trên Global Address trỏ đến Account làm giới hạn mỗi địa chỉ chỉ thuộc về 1 Account duy nhất, không dùng chung được.
> **B.** Account là đối tượng tiêu chuẩn, cấm làm con (detail) trong quan hệ Master-Detail với Custom Object.
> **C.** Lookup ngược chiều trên Global Address trỏ đến Account làm giới hạn mối quan hệ, không đáp ứng việc dùng chung.

**💡 Từ khóa ghi nhớ:** `Standard Object (như Account) -> CẤM làm con (Detail) trong mối quan hệ Master-Detail với Custom Object!`

---

## Câu 137

**🔵 A developer is creating a Lightning web component to show a list of sales records. The Sales Representative user should be able to see the commission field on each record. The Sales Assistant user should be able to see all fields on the record except the commission field. How should this be enforced so that the component works for both users without showing any errors?**

- **A.** Use Lightning Data Service to get the collection of sales records. ❌
- **B.** Use WITH SECURITY_ENFORCED in the SOQL that fetches the data for the component. ❌
- **C.** Use Lightning Locker Service to enforce sharing rules and field-level security. ❌
- **D.** Use Security.stripInaccessible to remove fields inaccessible to the current user. ✅

**📝 Dịch tiếng Việt:**
> Làm thế nào để LWC hoạt động cho cả 2 loại user (đại diện bán hàng có quyền xem trường commission, và trợ lý bán hàng không có quyền xem trường commission) mà không bị văng lỗi?

**💬 Giải thích gốc (English):**
> Use the stripInaccessible method to enforce field-level and object-level data protection. This method can be used to strip the fields and relationship fields from query and subquery results that the user can’t access. The method can also be used to remove inaccessible sObject fields before DML operations to avoid exceptions and to sanitize sObjects that have been deserialized from an untrusted source.

**✅ Tại sao đáp án đúng:**
> Sử dụng `Security.stripInaccessible` (D). Đây là vũ khí tối thượng giúp tự động quét và lọc bỏ tất cả các trường mà user hiện tại không có quyền truy cập (FLS) ra khỏi danh sách kết quả một cách im lặng và êm ái, giúp component hoạt động trơn tru cho mọi user mà không báo lỗi.

**❌ Tại sao đáp án sai:**
> **A.** Lightning Data Service chỉ hỗ trợ load từng bản ghi đơn lẻ tốt hơn, xử lý FLS cho cả list dài không linh hoạt bằng Apex.
> **B.** Thêm `WITH SECURITY_ENFORCED` vào SOQL sẽ quăng lỗi Exception to đùng làm crash ứng dụng ngay lập tức nếu user thiếu quyền xem bất kỳ trường nào trong câu SELECT. Quá thô bạo!
> **C.** Locker Service là cơ chế bảo mật cô lập mã nguồn JavaScript giữa các component, chả liên quan gì đến phân quyền trường FLS.

**💡 Từ khóa ghi nhớ:** `FLS Lọc trường thiếu quyền không muốn văng lỗi -> Dùng `Security.stripInaccessible` (êm ái nhất). Muốn quăng lỗi chặn đứng -> `WITH SECURITY_ENFORCED`.`

---

## Câu 138

**🔵 The sales management team at Universal Containers requires that the Lead Source field of the Lead record be populated when a Lead is converted. What should be done to ensure that a user populates the Lead Source field prior to converting a Lead?**

- **A.** Create an after trigger on Lead ❌
- **B.** Use a Validation Rule ✅
- **C.** Use a Formula Field ❌
- **D.** Use Lead Conversion field mapping ❌

**📝 Dịch tiếng Việt:**
> Để đảm bảo người dùng bắt buộc phải điền trường Lead Source trước khi thực hiện chuyển đổi (convert) Lead, giải pháp nào phù hợp nhất?

**💬 Giải thích gốc (English):**
> A validation rule can enforce that the Lead Source field is populated by preventing the Lead from being saved or converted if the field is empty. This ensures that users must fill in the Lead Source field before proceeding with the conversion.

**✅ Tại sao đáp án đúng:**
> Sử dụng Validation Rule (B) là chuẩn không cần chỉnh. Ta viết điều kiện kiểm tra: `IsConverted = true` và `ISBLANK(LeadSource)`. Khi người dùng bấm Convert mà bỏ trống trường này, Validation Rule sẽ chặn đứng và quăng thông báo ép nhập liệu.

**❌ Tại sao đáp án sai:**
> **A.** Trigger after insert/update chạy khi dữ liệu đã lưu xong, lúc này convert đã hoàn tất nên không còn tính chất 'ngăn chặn trước' (prior to).
> **C.** Formula field chỉ để tính toán hiển thị dữ liệu đọc, không có khả năng kiểm tra hay ép buộc nhập liệu.
> **D.** Lead Conversion field mapping chỉ dùng để ánh xạ trường từ Lead sang Account/Contact/Opportunity sau khi convert chứ không có cơ chế chặn convert nếu thiếu trường.

**💡 Từ khóa ghi nhớ:** `Keywords: Prior to (Trước khi làm gì) / Enforce (Bắt buộc) / Block (Chặn) -> Chọn ngay Validation Rule!`

---

## Câu 139

**🔵 A PrimaryId__c custom field exists on the Candidate__c custom object. The field is used to store each candidate's id number and is marked as Unique in the schema definition. As part of a data enrichment process, Universal Containers has a CSV file that contains updated data for all candidates in the system. The file contains each Candidate's social security number as a data point. Universal Containers wants to upload this information into Salesforce, while ensuring all data rows are correctly mapped to a candidate in the system. Which technique should the developer implement to streamline the data upload?**

- **A.** Update the PrimaryId__c field definition to mark it as an External Id. ✅
- **B.** Upload the CSV into a custom object related to Candidate__c. ❌
- **C.** Create a before save flow to correctly map the records. ❌
- **D.** Create a before insert trigger to correctly map the records. ❌

**📝 Dịch tiếng Việt:**
> Cần nạp dữ liệu cập nhật từ file CSV vào Salesforce cho đối tượng Candidate__c, đảm bảo dữ liệu khớp đúng với trường mã định danh duy nhất PrimaryId__c có sẵn. Nên dùng kỹ thuật nào?

**💬 Giải thích gốc (English):**
> Marking the PrimaryId__c field as an External Id allows Salesforce to use this field as a unique identifier for matching records during data import. This ensures that the data from the CSV file is correctly mapped to the existing candidate records based on their unique IDs.

**✅ Tại sao đáp án đúng:**
> Cập nhật định nghĩa trường PrimaryId__c và đánh dấu nó là trường External ID (A). Khi đó, các công cụ nạp dữ liệu như Data Loader hay Import Wizard có thể dùng trường này làm khóa đối chiếu để thực hiện thao tác Upsert (Cập nhật nếu có sẵn, tạo mới nếu chưa có) cực kỳ nhanh chóng, chuẩn xác 100% không lo trùng lặp.

**❌ Tại sao đáp án sai:**
> **B.** Nạp vào một object tạm rồi viết code map sang Candidate__c là vẽ đường vòng cồng kềnh, tốn tài nguyên và thời gian xử lý vô ích.
> **C.** Flow before-save không hỗ trợ đối chiếu khóa ngoài trực tiếp lúc nạp file bằng công cụ.
> **D.** Trigger before insert viết code map thủ công rất cồng kềnh, dễ lỗi và hoàn toàn thừa thãi khi hệ thống đã hỗ trợ sẵn tính năng External ID.

**💡 Từ khóa ghi nhớ:** `Khớp dữ liệu nhanh gọn từ file CSV ngoài -> Đánh dấu trường đối chiếu làm EXTERNAL ID!`

---

## Câu 140

**🔵 When a Task is created for a Contact, how can a developer prevent the task from being included on the Activity Timeline of the Contact's Account record?**

- **A.** In Activity Setting, uncheck Roll up activities to a contact's primary account. ✅
- **B.** Create a Task trigger to set the Account field to NULL. ❌
- **C.** Use Process Builder to create a process to set the Task Account field to blank. ❌
- **D.** By default, tasks do not display on the Account Activity Timeline. ❌

**📝 Dịch tiếng Việt:**
> Khi một Task được tạo cho một Contact, làm thế nào để ngăn chặn Task này tự động hiển thị trên Activity Timeline (Dòng thời gian hoạt động) của Account cha liên quan?

**💬 Giải thích gốc (English):**
> This setting ensures that tasks created for a Contact are not rolled up to the Activity Timeline of the Contact’s associated Account.

**✅ Tại sao đáp án đúng:**
> Salesforce có một tùy chọn cấu hình hệ thống cực kỳ bá đạo là 'Roll up activities to a contact's primary account'. Nếu bật nó lên, mọi hoạt động của con (Contact) sẽ tự động dồn hiển thị lên cha (Account). Để chặn việc này, ta chỉ cần vào Setup -> Activity Settings và bỏ tích chọn (uncheck) cấu hình này là xong ngay (A).

**❌ Tại sao đáp án sai:**
> **B.** Cố tình viết Trigger hay Process Builder để xóa trắng trường Account trên Task sẽ phá vỡ hoàn toàn mối quan hệ dữ liệu thô bạo, làm mất liên kết dữ liệu quan trọng của Task.
> **C.** Sử dụng Process Builder để xóa trắng trường Account trên Task cũng phá vỡ quan hệ dữ liệu thô bạo như phương án B.
> **D.** Phát biểu sai vì mặc định Salesforce sẽ tự động gom hiển thị hoạt động của Contact lên Account cha nếu tùy chọn roll-up được bật.

**💡 Từ khóa ghi nhớ:** `Muốn ngừng dồn Task con lên Timeline của Account cha -> Bỏ chọn 'Roll up activities to a contact's primary account' trong Setup!`

---

## Câu 141

**🔵 What is the requirement for a class to be used as a custom Visualforce controller?**

- **A.** Any top-level Apex class that has a constructor that returns a PageReference ❌
- **B.** Any top-level Apex class that extends a PageReference ❌
- **C.** Any top-level Apex class that has a default, no-argument constructor ✅
- **D.** Any top-level Apex class that implements the controller interface ❌

**📝 Dịch tiếng Việt:**
> Yêu cầu bắt buộc đối với một lớp Apex để có thể được sử dụng làm custom controller cho trang Visualforce là gì?

**💬 Giải thích gốc (English):**
> A custom controller is an Apex class that uses the default, no-argument constructor for the outer, top-level class.

**✅ Tại sao đáp án đúng:**
> Class đó bắt buộc phải là một top-level Apex class (lớp ngoài cùng, không phải inner class) và bắt buộc phải định nghĩa một hàm khởi tạo mặc định không tham số (default, no-argument constructor) (C) để nền tảng Visualforce có thể tự động khởi tạo đối tượng khi trang được tải lên.

**❌ Tại sao đáp án sai:**
> **A.** Hàm khởi tạo (constructor) của class Apex cấm khai báo kiểu trả về (kể cả PageReference), nó chỉ trùng tên class và không trả về giá trị gì cả.
> **B.** Class Apex làm controller không thể kế thừa lớp PageReference, sai kiến trúc hướng đối tượng của Apex.
> **D.** Không có một 'controller interface' nào bắt buộc Apex class phải implements để làm controller.

**💡 Từ khóa ghi nhớ:** `Custom Visualforce Controller -> Class phải có hàm khởi tạo không tham số mặc định (no-argument constructor).`

---

## Câu 142

**🔵 In order to override a standard action with a Visualforce page, which attribute must be defined in the <apex:page> tag?**

- **A.** pageReference ❌
- **B.** override ❌
- **C.** controller ❌
- **D.** standardController ✅

**📝 Dịch tiếng Việt:**
> Để ghi đè (override) một nút bấm chuẩn (standard action) bằng một trang Visualforce, thuộc tính nào bắt buộc phải được khai báo trong thẻ <apex:page>?

**💬 Giải thích gốc (English):**
> When overriding buttons with a Visualforce page, you must use the standard controller for the object on which the button appears. For example, to use a page to override the Edit button on accounts, the page markup must include the standardController="Account" attribute on the <apex:page> tag.

**✅ Tại sao đáp án đúng:**
> Thuộc tính `standardController` (D) bắt buộc phải được định nghĩa để trang Visualforce nhận đúng ngữ cảnh dữ liệu của đối tượng chứa nút bấm đó (ví dụ `standardController="Account"` để ghi đè nút Edit của Account).

**❌ Tại sao đáp án sai:**
> **A.** `pageReference` là kiểu trả về trong Apex, không phải thuộc tính của thẻ `<apex:page>`.
> **B.** Không có thuộc tính nào tên là `override` trong thẻ khai báo `<apex:page>`.
> **C.** `controller` dùng để khai báo Custom Controller class, không thể dùng để ghi đè nút bấm chuẩn của đối tượng.

**💡 Từ khóa ghi nhớ:** `Ghi đè action chuẩn (Override button) bằng Visualforce -> Bắt buộc dùng standardController!`

---

## Câu 143

**🔵 A developer needs to provide a way to mass edit, update, and delete records from a list view. In which two ways can this be accomplished? (Choose two.)**

- **A.** Create a new Visualforce page and Apex Controller for the list view that provides mass edit, update, and delete functionality. ✅
- **B.** Download a managed package from the AppExchange that provides customizable Enhanced List Views and buttons. ✅
- **C.** Download an unmanaged package from the AppExchange that provides customizable mass edit, update, and delete functionality. ❌
- **D.** Configure the user interface and enable both inline editing and enhanced lists. ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên cần cung cấp giải pháp cho phép chỉnh sửa, cập nhật và xóa hàng loạt (mass edit, update, delete) các bản ghi trực tiếp từ một danh sách (list view). Hai cách nào giúp thực hiện việc này? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> A đúng vì tạo một trang Visualforce tùy chỉnh sử dụng `StandardSetController` kết hợp với custom button trên list view sẽ giúp xử lý chỉnh sửa và xóa danh sách hàng loạt theo ý muốn bằng code Apex. B đúng vì cài đặt một managed package từ AppExchange cung cấp sẵn các nút bấm và Enhanced List Views có khả năng chỉnh sửa và xóa hàng loạt cực mạnh và an toàn, được bảo trì nâng cấp.

**❌ Tại sao đáp án sai:**
> **C.** Unmanaged package không được bảo trì nâng cấp và có thể gây xung đột code trong Org, không phải giải pháp tối ưu cho doanh nghiệp.
> **D.** Tính năng inline editing chuẩn trên list view chỉ hỗ trợ chỉnh sửa và cập nhật hàng loạt, tuyệt đối không hỗ trợ xóa hàng loạt (mass delete) bản ghi trực tiếp.

**💡 Từ khóa ghi nhớ:** `Mass Edit + Update + Delete trên List View -> Visualforce Page (StandardSetController) hoặc AppExchange Package.`

---

## Câu 144

**🔵 What is a benefit of using a trigger framework?**

- **A.** Reduces trigger execution time ❌
- **B.** Allows functional code to be tested by a test class ❌
- **C.** Increases trigger governor limits ❌
- **D.** Simplifies addition of context-specific logic ✅

**📝 Dịch tiếng Việt:**
> Lợi ích nổi bật của việc áp dụng mô hình Trigger Framework (khung thiết kế trigger) trong Salesforce là gì?

**💬 Giải thích gốc (English):**
> The primary benefit of using a trigger framework in Salesforce is that it simplifies the addition of context-specific logic. A trigger framework helps organize and manage complex trigger logic, making it easier to add, modify, and maintain code. This approach promotes best practices and ensures that triggers are scalable and maintainable.

**✅ Tại sao đáp án đúng:**
> Áp dụng trigger framework giúp đơn giản hóa việc bổ sung các logic nghiệp vụ theo từng ngữ cảnh sự kiện cụ thể (before insert, after update,...) (D) nhờ việc phân chia code khoa học vào các class Trigger Handler chuyên biệt, giúp code gọn gàng, tuần tự và cực kỳ dễ bảo trì khi dự án phình to.

**❌ Tại sao đáp án sai:**
> **A.** Trigger framework không làm giảm thời gian thực thi của CPU, thậm chí có thể tăng nhẹ một chút do phải chạy qua các lớp bọc trung gian.
> **B.** Code trigger thông thường không dùng framework vẫn được phủ test bình thường bởi test class.
> **C.** Framework không hề và không thể làm tăng giới hạn governor limit cứng của nền tảng Salesforce.

**💡 Từ khóa ghi nhớ:** `Trigger Framework -> Tổ chức code khoa học, dễ bảo trì và viết logic theo ngữ cảnh sự kiện cực nhàn!`

---

## Câu 145

**🔵 The sales management team at Universal Containers requires that the Lead Source field of the Lead record be populated when a Lead is converted. What should be used to ensure that a user populates the Lead Source field prior to converting a Lead?**

- **A.** Workflow Rule ❌
- **B.** Validation Rule ✅
- **C.** Formula Field ❌
- **D.** Process Builder ❌

**📝 Dịch tiếng Việt:**
> Để đảm bảo người dùng bắt buộc phải điền trường Lead Source trước khi thực hiện chuyển đổi (convert) Lead, giải pháp nào phù hợp nhất?

**💬 Giải thích gốc (English):**
> To ensure that the Lead Source field is populated before a Lead is converted, you should use a Validation Rule. A validation rule can enforce that the Lead Source field is not left blank by preventing the conversion process until the field is populated.

**✅ Tại sao đáp án đúng:**
> Validation Rule (B) là đệ nhất chặn lưu. Viết điều kiện kiểm tra: `IsConverted = true` và `ISBLANK(LeadSource)`. Khi người dùng cố bấm Convert mà bỏ trống trường này, Validation Rule sẽ chặn đứng và quăng thông báo bắt nhập liệu.

**❌ Tại sao đáp án sai:**
> **A.** Workflow Rule chỉ chạy ngầm backend sau khi dữ liệu đã lưu xong, lúc này convert đã hoàn tất nên không chặn được.
> **C.** Formula field chỉ để hiển thị dữ liệu tính toán đọc, không có khả năng chặn lưu hay ép buộc nhập liệu.
> **D.** Process Builder cũng chạy sau khi lưu bản ghi, không dùng để bắt lỗi chặn nhập liệu trực tiếp được.

**💡 Từ khóa ghi nhớ:** `Keywords: Prior to (Trước khi) / Enforce (Bắt buộc) / Block (Chặn) -> Chọn ngay Validation Rule!`

---

## Câu 146

**🔵 A company has been adding data to Salesforce and has not done a good job of limiting the creation of duplicate Lead records. The developer is considering writing an Apex process to identify duplicates and merge the records together. Which two statements are valid considerations when using merge? (Choose two.)**

- **A.** The merge method allows up to three records, including the master and two additional records with the same sObject type, to be merged into the master record. ✅
- **B.** Merge is supported with accounts, contacts, cases, and leads. ✅
- **C.** External ID fields can be used with the merge method. ❌
- **D.** The field values on the master record are overwritten by the records being merged. ❌

**📝 Dịch tiếng Việt:**
> Một Org gặp tình trạng tích tụ nhiều bản ghi Lead bị trùng lặp. Lập trình viên định viết code Apex gộp (merge) chúng lại. Hai lưu ý quan trọng nào khi sử dụng phương thức merge trong Apex? (Chọn 2)

**💬 Giải thích gốc (English):**
> The two valid considerations when using the merge method in Salesforce are:
> The merge method allows up to three records, including the master and two additional records with the same sObject type, to be merged into the master record. This is a key feature of the merge operation, allowing consolidation of up to three records.
> Merge is supported with accounts, contacts, cases, and leads. These are the standard objects that support the merge operation in Salesforce.

**✅ Tại sao đáp án đúng:**
> A đúng vì phương thức `merge` cho phép gộp tối đa 3 bản ghi (gồm 1 bản ghi master chính và tối đa 2 bản ghi phụ cùng loại sObject) vào bản ghi master. B đúng vì thao tác DML merge chỉ hỗ trợ chính thức đối với 4 đối tượng tiêu chuẩn là Accounts, Contacts, Cases và Leads. Gặp đối tượng khác là chịu chết!

**❌ Tại sao đáp án sai:**
> **C.** Không thể dùng các trường External ID làm đối số truyền trực tiếp vào phương thức merge, phương thức này bắt buộc nhận vào đối tượng sObject hoặc Id thật.
> **D.** Các giá trị trường trên bản ghi master được giữ lại, các bản ghi phụ bị gộp sẽ bị xóa sạch và đưa vào Recycle Bin chứ không ghi đè thô bạo lên master.

**💡 Từ khóa ghi nhớ:** `DML Merge: Chỉ hỗ trợ Account, Contact, Case, Lead. Gộp tối đa 3 bản ghi (1 master + 2 phụ)!`

---

## Câu 147

**🔵 A developer created this Apex trigger that calls MyClass.myStaticMethod:
trigger myTrigger on Contact(before insert){
MyClass.myStaticMethod(trigger.new, trigger.oldMap);
}
The developer creates a test class with a test method that calls MyClass.myStaticMethod, resulting in 81% overall code coverage.
What happens when the developer tries to deploy the trigger and two classes to production, assuming no other code exists?**

- **A.** The deployment fails because no assertions were made in the test method. ❌
- **B.** The deployment passes because both classes and the trigger were included in the deployment. ❌
- **C.** The deployment passes because the Apex code has required (>75%) code coverage. ❌
- **D.** The deployment fails because the Apex trigger has no code coverage. ✅

**📝 Dịch tiếng Việt:**
> Developer viết một trigger gọi phương thức static của MyClass. Trong test class, developer chỉ viết test method gọi trực tiếp phương thức static đó của class mà không chèn bản ghi mới, đạt 81% tổng code coverage. Điều gì xảy ra khi deploy trigger và 2 class này lên Production?

**💬 Giải thích gốc (English):**
> Even though the overall code coverage is 81%, the specific Apex trigger itself must have code coverage. In Salesforce, each trigger must be covered by tests, and the deployment will fail if any trigger has 0% coverage.

**✅ Tại sao đáp án đúng:**
> Đợt deployment sẽ thất bại hoàn toàn vì trigger bị 0% code coverage (D). Quy tắc bắt buộc của Salesforce khi deploy là: **Mỗi file trigger riêng biệt bắt buộc phải có coverage lớn hơn 0%** (ít nhất 1 dòng trigger được chạy thử trong test). Vì test class chỉ gọi trực tiếp class helper mà không tạo bản ghi để kích hoạt trigger nổ, trigger bị 0% coverage nên oẳng.

**❌ Tại sao đáp án sai:**
> **A.** Salesforce không chặn deploy vì thiếu câu lệnh assert (dù viết assert là best practice).
> **B.** Deploy vẫn thất bại vì vi phạm luật 0% coverage của trigger bất kể có gom chung file hay không.
> **C.** Dù tổng coverage org đạt 81% (vượt 75%), trigger bị 0% coverage vẫn là lỗi chí tử chặn deploy.

**💡 Từ khóa ghi nhớ:** `Deploy Trigger -> Bắt buộc phải viết test tạo bản ghi để trigger nổ (Coverage trigger > 0%).`

---

## Câu 148

**🔵 What are three considerations when using the @InvocableMethod annotation in Apex? (Choose three.)**

- **A.** A method using the @InvocableMethod annotation must be declared as static. ✅
- **B.** A method using the @InvocableMethod annotation can be declared as Public or Global. ✅
- **C.** A method using the @InvocableMethod annotation can have multiple input parameters. ❌
- **D.** A method using the @InvocableMethod annotation must define a return value. ❌
- **E.** Only one method using the @InvocableMethod annotation can be defined per Apex class. ✅

**📝 Dịch tiếng Việt:**
> Ba cân nhắc nào là đúng khi sử dụng annotation @InvocableMethod trong Apex để gọi từ Flow/Process Builder? (Chọn 3)

**💬 Giải thích gốc (English):**
> InvocableMethod Considerations
> The invocable method must be static and public or global, and its class must be an outer class.
> Only one method in a class can have the InvocableMethod annotation.
> Other annotations can’t be used with the InvocableMethod annotation.

**✅ Tại sao đáp án đúng:**
> A đúng vì method bắt buộc phải được khai báo với từ khóa `static` để hệ thống gọi trực tiếp từ Flow/Process Builder mà không cần khởi tạo class. B đúng vì nó phải là `public` hoặc `global` để các công cụ tự động hóa no-code có thể 'nhìn thấy' và kích hoạt được. E đúng vì mỗi Apex class chỉ được phép chứa duy nhất một phương thức có gắn thẻ `@InvocableMethod`.

**❌ Tại sao đáp án sai:**
> **C.** Phương thức `@InvocableMethod` chỉ chấp nhận duy nhất một tham số đầu vào (thường là List). Đòi truyền nhiều tham số là compile báo lỗi ngay.
> **D.** Không bắt buộc phải có return value, kiểu trả về hoàn toàn có thể là `void`.

**💡 Từ khóa ghi nhớ:** `Invocable Method: Static, Public/Global, Chỉ 1 method duy nhất mỗi class, nhận tham số là List!`

---

## Câu 149

**🔵 A team of developers is working on a source-driven project that allows them to work independently, with many different org configurations. Which type of Salesforce orgs should they use for their development?**

- **A.** Developer orgs ❌
- **B.** Developer sandboxes ❌
- **C.** Full Copy sandboxes ❌
- **D.** Scratch orgs ✅

**📝 Dịch tiếng Việt:**
> Team dev làm dự án source-driven, muốn làm việc độc lập với nhiều cấu hình org khác nhau. Dùng loại org nào?

**💬 Giải thích gốc (English):**
> The scratch org is a source-driven and disposable deployment of Salesforce code and metadata. A scratch org is fully configurable, allowing developers to emulate different Salesforce editions with different features and settings. You can share the scratch org configuration file with other team members, so you all have the same basic org in which to do your development. In addition to code and metadata, developers can install packages and deploy synthetic or dummy data for testing. Don’t add personal data to scratch orgs.

**✅ Tại sao đáp án đúng:**
> Scratch Orgs (D) là 'xương sống' của Source-Driven Development (phát triển hướng mã nguồn) và Salesforce DX. Nó cho phép tạo ra các môi trường ảo tạm thời cực kỳ nhanh chóng, cấu hình qua file JSON để lập trình viên tự do phát triển và test độc lập rồi bỏ đi (disposable), không lo xung đột cấu hình.

**❌ Tại sao đáp án sai:**
> **A.** Developer Org là org miễn phí trọn đời cho cá nhân học tập, không tích hợp tốt vào quy trình CI/CD chuyên nghiệp của dự án lớn.
> **B.** Developer Sandbox bị giới hạn bởi cấu hình cố định của Production org và tốn công refresh thủ công, không linh hoạt bằng Scratch Org.
> **C.** Full Copy Sandbox dùng để test performance hoặc User Acceptance Test (UAT) vì chứa đầy đủ data thật, đem đi dev độc lập là phí phạm và cực kỳ cồng kềnh.

**💡 Từ khóa ghi nhớ:** `Keyword: Source-driven / SFDX / Độc lập nhiều cấu hình -> Chọn ngay SCRATCH ORGS!`

---

## Câu 150

**🔵 A developer executes the following query in Apex to retrieve a list of contacts for each account: List<account> accounts = [Select ID, Name, (Select ID, Name from Contacts) from Account]; Which two exceptions may occur when it executes? (Choose two.)**

- **A.** CPU limit exception due to the complexity of the query. ❌
- **B.** SOQL query row limit exception due to the number of contacts. ✅
- **C.** SOQL query limit exception due to the number of contacts. ❌
- **D.** SOQL query row limit exception due to the number of accounts. ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên thực hiện câu truy vấn SOQL: List<account> accounts = [Select ID, Name, (Select ID, Name from Contacts) from Account]; Hai ngoại lệ (exception) giới hạn nào có thể xảy ra khi chạy? (Chọn 2)

**💬 Giải thích gốc (English):**
> SOQL query row limit exception due to the number of contacts (B): Salesforce imposes a limit on the total number of rows that can be retrieved by a single SOQL query. If the number of contacts retrieved exceeds this limit, a row limit exception will occur.
> SOQL query row limit exception due to the number of accounts: Similarly, if the number of accounts retrieved exceeds the row limit, this will also trigger a row limit exception.

**✅ Tại sao đáp án đúng:**
> B đúng vì nếu số lượng Contact con quá lớn, tổng số hàng SOQL lấy ra sẽ vượt giới hạn 50,000 hàng. D đúng vì nếu số lượng Account cha quá lớn cũng dễ dàng làm vượt giới hạn hàng SOQL. Trong Salesforce, mỗi bản ghi con được lấy ra trong subquery cũng bị tính là 1 hàng vào giới hạn SOQL Row Limit (50,000 hàng tối đa trong 1 transaction).

**❌ Tại sao đáp án sai:**
> **A.** CPU limit exception chỉ nổ ra khi code xử lý tính toán quá phức tạp trong thời gian dài, một câu SOQL đơn giản không đủ tuổi kích hoạt lỗi này trước khi chạm giới hạn hàng.
> **C.** SOQL query limit exception chỉ xảy ra khi mày gọi lệnh SELECT quá 100 lần trong 1 transaction, ở đây ta chỉ chạy duy nhất 1 câu SELECT.

**💡 Từ khóa ghi nhớ:** `SOQL Row Limit = 50,000 hàng. Mỗi bản ghi con trong Subquery cũng ngốn 1 hàng vào giới hạn này!`

---

## Câu 151

**🔵 Universal Containers wants to assess the advantages of declarative development versus programmatic customization for specific use cases in its Salesforce implementation. What are two advantages of declarative development over programmatic customization? (Choose two.)**

- **A.** Declarative development has higher design limits and query limits. ❌
- **B.** Declarative development does not require Apex test classes. ✅
- **C.** Declarative development does not require maintenance. ❌
- **D.** Declarative development can be updated in production using the Setup UI. ✅

**📝 Dịch tiếng Việt:**
> Universal Containers muốn đánh giá ưu điểm của việc dùng cấu hình no-code (declarative) so với việc hì hục gõ code (programmatic) cho các use case cụ thể. Hai lợi thế cực đỉnh của declarative là gì? (Chọn 2)

**💬 Giải thích gốc (English):**
> Declarative development does not require Apex test classes: Declarative tools like workflows, process builders, and flows do not require the creation of test classes, which simplifies the development and deployment process.
> Declarative development can be updated in production using the Setup UI: Declarative changes can be made directly in the production environment through the Salesforce Setup UI, allowing for quicker and easier updates without the need for a deployment process.

**✅ Tại sao đáp án đúng:**
> B đúng vì làm declarative (như Flow, Validation Rules...) sướng cái thân, không cần viết class test phủ coverage 75% cực khổ. D đúng vì admin có thể chỉnh sửa và cập nhật nóng trực tiếp trên môi trường Production bằng giao diện Setup UI trong vòng 1 nốt nhạc.

**❌ Tại sao đáp án sai:**
> **A.** Cực kỳ hoang đường! Declarative và Programmatic đều chịu chung giới hạn nền tảng (governor limits) của Salesforce, thậm chí Flow còn dễ oẳng limit hơn nếu không biết tối ưu.
> **C.** Làm gì có chuyện không cần bảo trì? Nghiệp vụ của công ty thay đổi thì Flow hay Rule gì cũng phải vào sửa bình thường, không có chuyện 'bất tử' đâu nhé.

**💡 Từ khóa ghi nhớ:** `Cấu hình Declarative (No-code) -> Tiết kiệm test class + Chỉnh sửa trực tiếp trên Production qua Setup UI.`

---

## Câu 152

**🔵 A developer is asked to create a PDF quote document formatted using the company's branding guidelines, and automatically save it to the Opportunity record. Which two ways should a developer create this functionality? (Choose two.)**

- **A.** Install an application from the AppExchange to generate documents. ✅
- **B.** Create a Visualforce page with custom styling. ✅
- **C.** Create an email template and use it in Process Builder. ❌
- **D.** Create a visual flow that implements the company's formatting. ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên được giao nhiệm vụ tạo một file PDF báo giá chuẩn chỉnh theo bộ nhận diện thương hiệu của công ty, đồng thời tự động lưu file đó vào bản ghi Opportunity. Hai cách nào giúp thực hiện yêu cầu này? (Chọn 2)

**💬 Giải thích gốc (English):**
> The two ways a developer can create this functionality are:
> Install an application from the AppExchange to generate documents: There are several applications available on the AppExchange that can help generate PDF documents with custom branding and save them to records automatically. These apps often come with pre-built templates and functionalities that simplify the process.
> Create a Visualforce page with custom styling: By creating a Visualforce page, a developer can have full control over the styling and formatting of the PDF document. This approach allows for the customization needed to adhere to the company’s branding guidelines

**✅ Tại sao đáp án đúng:**
> A đúng vì cài các app chuyên nghiệp từ AppExchange (như Conga Composer, DocuSign) giúp generate tài liệu siêu nhanh và tự động lưu. B đúng vì tự build trang Visualforce với custom CSS và thuộc tính renderAs="pdf" cho phép tùy biến giao diện PDF 100% theo ý muốn, sau đó dùng code Apex lưu file vào record Opportunity con.

**❌ Tại sao đáp án sai:**
> **C.** Email template không có khả năng tự động render định dạng PDF phức tạp theo quy chuẩn thương hiệu, và Process Builder (đã bị deprecated) cũng không thể tự tạo rồi đính kèm file vào Opportunity được.
> **D.** Flow Builder thuần túy không hỗ trợ thiết kế bố cục PDF tùy chỉnh nâng cao và xuất file trực tiếp no-code.

**💡 Từ khóa ghi nhớ:** `Muốn tạo PDF thương hiệu trong Salesforce -> Chọn Visualforce (renderAs="pdf") hoặc cài hàng xịn từ AppExchange.`

---

## Câu 153

**🔵 What should be used to create scratch orgs?**

- **A.** Developer Console ❌
- **B.** Salesforce CLI ✅
- **C.** Workbench ❌
- **D.** Sandbox refresh ❌

**📝 Dịch tiếng Việt:**
> Nên dùng cái gì để tạo các scratch org vậy các dân chơi?

**💬 Giải thích gốc (English):**
> Salesforce CLI (Command Line Interface) is the tool used to create and manage scratch orgs. It allows developers to easily spin up scratch orgs, configure them, and manage their lifecycle through command-line commands.

**✅ Tại sao đáp án đúng:**
> Scratch Orgs là linh hồn của mô hình 'Source-driven Development'. Salesforce CLI (SFDX) là công cụ duy nhất cho phép mày gõ lệnh tạo, quản lý và xóa Scratch Orgs thông qua terminal hoặc script tự động hóa.

**❌ Tại sao đáp án sai:**
> **A.** Developer Console chỉ để viết code, chạy test hoặc query SOQL trong org hiện tại, không có nút nào để 'đẻ' ra org mới đâu.
> **C.** Workbench dùng để thao tác dữ liệu và check metadata thô, chứ tuổi gì tạo được scratch org.
> **D.** Sandbox refresh dùng cho Sandbox truyền thống (Developer, Partial, Full) liên kết trực tiếp với Production, chả liên quan gì đến Scratch Org.

**💡 Từ khóa ghi nhớ:** `Scratch Orgs -> Salesforce CLI / SFDX CLI.`

---

## Câu 154

**🔵 Which Apex class contains methods to return the amount of resources that have been used for a particular governor, such as the number of DML statements?**

- **A.** Exception ❌
- **B.** Messaging ❌
- **C.** OrgLimits ❌
- **D.** Limits ✅

**📝 Dịch tiếng Việt:**
> Lớp Apex nào chứa các phương thức trả về lượng tài nguyên đã sử dụng cho một giới hạn governor cụ thể, ví dụ như số lượng câu lệnh DML đã chạy?

**💬 Giải thích gốc (English):**
> The Limits methods return the specific limit for the particular governor, such as the number of calls of a method or the amount of heap size remaining.
> Because Apex runs in a multitenant environment, the Apex runtime engine strictly enforces a number of limits to ensure that runaway Apex doesn’t monopolize shared resources.

**✅ Tại sao đáp án đúng:**
> Class System.Limits chính là cái 'đồng hồ đo điện' cho dev Apex. Nó chứa các phương thức cực kỳ bá đạo như getDmlStatements() (đã dùng bao nhiêu) và getLimitDmlStatements() (giới hạn tối đa là bao nhiêu) để mày tự check và né lỗi chạm trần.

**❌ Tại sao đáp án sai:**
> **A.** Exception là lớp cha của các loại ngoại lệ (lỗi), chỉ dùng để bắt lỗi chứ không đo đạc tài nguyên.
> **B.** Messaging dùng để xử lý gửi email, không liên quan gì đến giới hạn hệ thống.
> **C.** OrgLimits dùng để check giới hạn của toàn bộ Org (như số lượng API call trong 24h), không phải giới hạn của 1 transaction cụ thể như DML.

**💡 Từ khóa ghi nhớ:** `Đo lường Governor Limits trong code -> Dùng ngay class Limits.`

---

## Câu 155

**🔵 If Apex code executes inside the execute() method of an Apex class when implementing the Batchable interface, which two statements are true regarding governor limits? (Choose two.)**

- **A.** The Apex governor limits are reset for each iteration of the execute() method. ✅
- **B.** The Apex governor limits cannot be exceeded due to the asynchronous nature of the transaction. ❌
- **C.** The Apex governor limits might be higher due to the asynchronous nature of the transaction. ✅
- **D.** The Apex governor limits are relaxed while calling the constructor of the Apex class. ❌

**📝 Dịch tiếng Việt:**
> Nếu mã Apex chạy bên trong phương thức execute() của một class triển khai interface Batchable, hai phát biểu nào là đúng về giới hạn governor limits? (Chọn 2)

**💬 Giải thích gốc (English):**
> Each execution of a batch Apex job is considered a discrete transaction, and the governor limits are reset for each transaction.
> Batch Apex operates asynchronously, which can allow for higher governor limits compared to synchronous transactions.

**✅ Tại sao đáp án đúng:**
> A đúng vì mỗi lượt chạy của phương thức execute() xử lý một batch (mặc định tối đa 200 bản ghi) là một transaction độc lập, nên governor limits sẽ được reset từ đầu cho mỗi batch. C đúng vì Batch là lập trình bất đồng bộ (Asynchronous Apex), một số giới hạn sẽ được Salesforce nới rộng ra (ví dụ Heap size lên tới 12MB thay vì 6MB như đồng bộ).

**❌ Tại sao đáp án sai:**
> **B.** Phát biểu ngáo ngơ! Bất đồng bộ thì vẫn có giới hạn trần đàng hoàng chứ không phải 'bất tử' muốn chạy nhiêu thì chạy đâu nhé.
> **D.** Hàm khởi tạo (constructor) của class Batch chạy ở chế độ đồng bộ (synchronous) bình thường, không hề được nới lỏng hay ưu tiên gì cả.

**💡 Từ khóa ghi nhớ:** `Batch Apex: Mỗi batch (execute) là một transaction riêng biệt -> Limit được RESET + Được hưởng giới hạn Asynchronous cao hơn.`

---

## Câu 156

**🔵 What are three characteristics of change set deployments? (Choose three.)**

- **A.** They require a deployment connection. ✅
- **B.** They can be used to transfer records. ❌
- **C.** They can be used only between related organizations. ✅
- **D.** They can be used to deploy custom settings data. ❌
- **E.** They use an all or none deployment model. ✅

**📝 Dịch tiếng Việt:**
> Ba đặc điểm nổi bật của việc deploy bằng Change Set là gì? (Chọn 3)

**💬 Giải thích gốc (English):**
> Change sets can only be sent between Salesforce orgs that have an established deployment connection.
> Change sets can be used only between related organizations, such as a production org and its sandbox, or two sandboxes created from the same production org.
> Change sets are deployed as a single transaction, meaning if any part of the deployment fails, the entire change set is rolled back.

**✅ Tại sao đáp án đúng:**
> A đúng vì bắt buộc phải thiết lập Deployment Connection giữa 2 Org trước thì mới gửi được. C đúng vì Change Set chỉ được phép dùng giữa các Org có liên kết họ hàng với nhau (tức là cùng nằm dưới một Production Org chung). E đúng vì mô hình deploy của Change Set là 'All or none' - được ăn cả, ngã về không (chỉ cần 1 thành phần bị lỗi là toàn bộ đợt deploy rollback sạch sẽ).

**❌ Tại sao đáp án sai:**
> **B.** Change Set sinh ra chỉ để deploy METADATA (cấu hình, code, trường...), không có tính năng chuyển DATA bản ghi (Records) giữa các Org.
> **D.** Custom Settings data là dữ liệu bản ghi nằm bên trong Custom Settings, Change Set không thể di chuyển được đống dữ liệu này.

**💡 Từ khóa ghi nhớ:** `Change Set = Chỉ METADATA + Chỉ giữa các Org có họ hàng liên kết + Deploy kiểu All-or-none.`

---

## Câu 157

**🔵 Consider the following code snippet:
public static List<Lead> obtainAllFields(Set<Id> leadIds){
List<Lead> result = new List<Lead>();
for(Id leadId : leadIds){
result.add([SELECT FIELDS(ALL) FROM Lead WHERE Id =:leadId]);
}
return result;
}
Given the multi-tenant architecture of the Salesforce platform, what is a best practice a developer should implement and ensure successful execution of the method?**

- **A.** Avoid performing queries Inside for loops. ✅
- **B.** Avoid executing queries without a limit clause. ❌
- **C.** Avoid using variables as query filters. ❌
- **D.** Avoid returning an empty List of records. ❌

**📝 Dịch tiếng Việt:**
> Cho đoạn code sau: [Code SOQL inside For]. Dựa trên kiến trúc đa khách thuê (multi-tenant) của Salesforce, best practice nào lập trình viên cần áp dụng để đảm bảo phương thức thực thi thành công không bị sập?

**💬 Giải thích gốc (English):**
> Performing queries inside for loops can lead to hitting governor limits, as it results in a separate query for each iteration of the loop. This can quickly exceed the allowed number of SOQL queries per transaction.

**✅ Tại sao đáp án đúng:**
> Tuyệt đối không bao giờ được phép thực hiện truy vấn SOQL bên trong vòng lặp For (A). Việc này là 'tội ác chống lại loài người' trong Apex, vì chỉ cần danh sách truyền vào lớn hơn 100 bản ghi là hệ thống sẽ ném ra lỗi LimitException (vượt quá 100 SOQL query) và sập ngay lập tức. Ta phải gom Id lại rồi query ngoài vòng lặp (Bulkify).

**❌ Tại sao đáp án sai:**
> **B.** Thêm mệnh đề LIMIT vào câu query không giúp ích gì cho việc ngăn lỗi nếu vòng lặp chạy quá 100 lần.
> **C.** Sử dụng biến binding :leadId là kỹ thuật chuẩn chỉnh để lọc dữ liệu và chống SOQL Injection, cấm đoán nó là sai lầm.
> **D.** Trả về một List rỗng khi không tìm thấy kết quả là hoàn toàn bình thường, không gây ra lỗi hệ thống.

**💡 Từ khóa ghi nhớ:** `Best Practice tối thượng: CẤM SOQL/DML bên trong vòng lặp For!`

---

## Câu 158

**🔵 Refer to the following Apex code:
Integer x = 0;
do{
x = 1;
x++;
}
while(x < 1);
System.debug(x);
What is the value of x when it is written to the debug log?**

- **A.** 0 ❌
- **B.** 1 ❌
- **C.** 2 ✅
- **D.** 3 ❌

**📝 Dịch tiếng Việt:**
> Giá trị của x trong debug log sau khi chạy vòng lặp do-while trên là bao nhiêu?

**💬 Giải thích gốc (English):**
> The loop executes once, setting x to 1 and then incrementing it to 2. After the loop finishes, x has the value 2, which is then written to the debug log.

**✅ Tại sao đáp án đúng:**
> Vòng lặp do-while có nguyên lý hoạt động là 'cứ đâm đầu vào làm trước, hỏi tội (check điều kiện) sau'. Nên dù điều kiện while có sai ngay từ đầu thì nó vẫn chạy qua ít nhất 1 lần. Cụ thể: 1. Vào khối do: gán x = 1. 2. Tăng giá trị: x++ thành 2. 3. Check điều kiện: while (2 < 1) -> SAI -> Thoát loop. Debug in ra giá trị của x là 2.

**❌ Tại sao đáp án sai:**
> **A.** Gán x = 1 rồi x++ thì kết quả không thể bằng 0 được.
> **B.** Lệnh x++ đã tăng x từ 1 lên 2 rồi mới kiểm tra điều kiện thoát.
> **D.** Vòng lặp chỉ chạy duy nhất 1 lần, x không có cách nào tăng lên tới 3 được.

**💡 Từ khóa ghi nhớ:** `Vòng lặp do-while: Luôn chạy ít nhất 1 lần. Làm trước rồi mới check điều kiện sau!`

---

## Câu 159

**🔵 A developer needs to test an Invoicing system integration. After reviewing the number of transactions required for the test, the developer estimates that the test data will total about 2 GB of data storage. Production data is not required for the integration testing. Which two environments meet the requirements for testing? (Choose two)**

- **A.** Developer Sandbox ❌
- **B.** Full Sandbox ✅
- **C.** Developer Edition ❌
- **D.** Partial Sandbox ✅
- **E.** Developer Pro Sandbox ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên cần test tích hợp hệ thống hóa đơn. Ước tính dữ liệu test giả lập sẽ chiếm khoảng 2 GB dung lượng lưu trữ (data storage). Không cần dữ liệu thật từ Production. Hai môi trường Sandbox nào đáp ứng được yêu cầu này? (Chọn 2)

**💬 Giải thích gốc (English):**
> Full Sandbox(Data storage: Same as your production org): Full sandboxes are a complete copy of your production org, including all data, metadata, and customizations. This means they can handle large amounts of data and provide a realistic environment for testing integrations.
> Partial Sandbox(Data storage: 5 GB): Partial sandboxes are smaller copies of your production org, but they can still handle a significant amount of data. The exact size limit depends on your organization's specific settings, but partial sandboxes are generally sufficient for testing integrations with moderate amounts of data.

**✅ Tại sao đáp án đúng:**
> B đúng vì Full Sandbox có dung lượng lưu trữ dữ liệu bằng 100% so với Production Org thật, thừa sức chứa. D đúng vì Partial Sandbox hỗ trợ dung lượng lưu trữ dữ liệu lên tới 5 GB, quá dư dả cho nhu cầu 2 GB của chúng ta mà lại tiết kiệm thời gian refresh hơn Full.

**❌ Tại sao đáp án sai:**
> **A.** Developer Sandbox chỉ có dung lượng dữ liệu siêu hẻo là 200 MB, nhét kẽ răng còn thiếu chứ đừng nói tới 2 GB.
> **C.** Developer Edition là Org học tập cá nhân miễn phí chỉ có giới hạn 20 MB dữ liệu, quá bé.
> **E.** Developer Pro Sandbox chỉ hỗ trợ tối đa 1 GB dung lượng dữ liệu, vẫn không đủ chứa 2 GB dữ liệu test.

**💡 Từ khóa ghi nhớ:** `Dung lượng dữ liệu Sandbox: Developer (200MB) -> Developer Pro (1GB) -> Partial (5GB) -> Full (Bằng Production).`

---

## Câu 160

**🔵 Universal Containers hires a developer to build a custom search page to help users find the Accounts they want. Users will be able to search on Name, Description, and a custom comments field. Which consideration should the developer be aware of when deciding between SOQL and SOSL? (Choose two.)**

- **A.** SOSL is faster for text searches. ✅
- **B.** SOQL is able to return more records. ✅
- **C.** SOQL is faster for text searches. ❌
- **D.** SOSL is able to return more records. ❌

**📝 Dịch tiếng Việt:**
> Universal Containers thuê dev build trang tìm kiếm Account tùy chỉnh cho phép tìm theo Name, Description và custom comments field. Khi cân nhắc lựa chọn giữa SOQL và SOSL, hai điều nào lập trình viên cần lưu ý? (Chọn 2)

**💬 Giải thích gốc (English):**
> SOQL vs. SOSL Queries
> Search can be accessed with SOQL or SOSL queries. SOQL is Force.com's database query language, similar to SQL. You can use SOQL to query child-to-parent relationships, which are often many-to-one, and to query parent-to-child relationships, which are almost always one-to-many.
> SOSL is Force.com's full-text search language. SOSL can tokenize multiple terms within a field, and can build a search index off of this. If you’re searching for a specific distinct term that you know exists within a field, you might find SOSL faster than SOQL. However, for each Apex transaction, the governor limit for multiple SOSL searches in a single transaction is 2,000 (Note: It is common to only need a single search, in which case the limit is 40,000); for SOQL queries it’s 50,000. So if you need to retrieve more than 2,000 records, SOQL is the better choice.

**✅ Tại sao đáp án đúng:**
> A đúng vì SOSL cực kỳ nhanh và tối ưu cho việc tìm kiếm từ khóa trên các trường văn bản lớn (như Description, Comments) nhờ có cơ chế đánh chỉ mục (index) từ khóa. B đúng vì SOQL có giới hạn trả về lớn hơn nhiều trong một giao dịch (lên tới 50,000 bản ghi), trong khi SOSL bị giới hạn cứng tối đa 2,000 bản ghi cho mỗi sObject.

**❌ Tại sao đáp án sai:**
> **C.** Sai hoàn toàn, SOQL tìm kiếm text lớn dùng toán tử LIKE sẽ rất chậm vì phải quét toàn bộ bảng dữ liệu.
> **D.** Ngược lại mới đúng, SOSL bị giới hạn trả về 2,000 bản ghi, ít hơn nhiều so với SOQL (50,000).

**💡 Từ khóa ghi nhớ:** `Tìm kiếm từ khóa tự do trên nhiều trường văn bản lớn -> Dùng SOSL (nhanh hơn). Cần lấy số lượng bản ghi lớn -> Dùng SOQL (limit 50k > 2k).`

---

## Câu 161

**🔵 Considering the following code snippet:
public static void insertAccounts(ListAccount theseAccounts){
for(Account thisAccount : theseAccounts){
if(thisAccount.website == null){
thisAccount.website = 'https://www.test.com';
}
}
update theseAccounts;
}
When the code executes, a DML exception is thrown.
How should the developer modify the code to ensure exceptions are handled gracefully?**

- **A.** Implement Change Data Capture. ❌
- **B.** Implement the upsert DML statement. ❌
- **C.** Remove null items from the list of Accounts. ❌
- **D.** Implement a try/catch block for the DML. ✅

**📝 Dịch tiếng Việt:**
> Khi đoạn code trên chạy, một ngoại lệ DML (DML exception) bị ném ra. Lập trình viên nên sửa code thế nào để xử lý các ngoại lệ một cách êm đẹp và chuyên nghiệp?

**💬 Giải thích gốc (English):**
> To handle DML exceptions gracefully, the developer should implement a try/catch block around the DML statement. This allows the code to catch and handle any exceptions that occur during the update operation, ensuring that the application can respond appropriately without crashing.
> Example
> public static void insertAccounts(List<Account> theseAccounts) {
> for (Account thisAccount : theseAccounts) {
> if (thisAccount.website == null) {
> thisAccount.website = 'https://www.test.com';
> }
> }
> try {
> update theseAccounts;
> } catch (DmlException e) {
> // Handle the exception, e.g., log the error or notify the user
> System.debug('An error occurred: ' + e.getMessage());
> }
> }

**✅ Tại sao đáp án đúng:**
> Để xử lý lỗi một cách êm đềm (gracefully) không làm chết chương trình giữa chừng và hiển thị giao diện đỏ lòm cho User, cách tiêu chuẩn trong lập trình là bọc câu lệnh DML nguy hiểm vào khối try/catch (D). Khi có lỗi nổ ra, phần catch sẽ hứng lấy và xử lý (ghi log hoặc báo lỗi lịch sự).

**❌ Tại sao đáp án sai:**
> **A.** Change Data Capture là cơ chế đồng bộ dữ liệu real-time qua Event-driven, không có tác dụng bắt lỗi trong code Apex.
> **B.** Thay bằng lệnh upsert không giúp giải quyết tận gốc nguyên nhân gây lỗi DML (ví dụ như vi phạm Validation Rule hay thiếu trường bắt buộc).
> **C.** Lỗi DML có thể do dữ liệu của chính các bản ghi không hợp lệ, việc lọc phần tử null trong list không đảm bảo 100% hết lỗi.

**💡 Từ khóa ghi nhớ:** `Xử lý ngoại lệ êm đẹp trong code -> Bọc ngay vào khối try/catch.`

---

## Câu 162

**🔵 When using SalesforceDX, what does a developer need to enable to create and manage scratch orgs?**

- **A.** Production ❌
- **B.** Environment Hub ❌
- **C.** Dev Hub ✅
- **D.** Sandbox ❌

**📝 Dịch tiếng Việt:**
> Khi sử dụng Salesforce DX, lập trình viên cần kích hoạt tính năng nào để có thể tạo và quản lý các scratch org?

**💬 Giải thích gốc (English):**
> To create and manage scratch orgs using SalesforceDX, a developer needs to enable the Dev Hub. The Dev Hub is the central place for managing your scratch orgs and is essential for using SalesforceDX tools.

**✅ Tại sao đáp án đúng:**
> Dev Hub (C) chính là cái 'lò đẻ' ra Scratch Orgs. Mày bắt buộc phải bật tính năng Dev Hub trong một Org xịn (Production hoặc Developer Org) để từ đó kết nối với Salesforce CLI và ra lệnh tạo các scratch org con.

**❌ Tại sao đáp án sai:**
> **A.** Production là môi trường chạy thật, tự thân nó không thể tạo scratch org nếu chưa bật Dev Hub.
> **B.** Environment Hub dùng để quản lý liên kết nhiều Org khác nhau về một mối, không phải công cụ để tạo Scratch Org trong quy trình SFDX.
> **D.** Sandbox là môi trường thử nghiệm truyền thống, không liên quan đến việc sinh các Scratch Orgs tạm thời.

**💡 Từ khóa ghi nhớ:** `Scratch Org (Môi trường tạm thời) -> Bắt buộc phải có Dev Hub (Lò đẻ).`

---

## Câu 163

**🔵 Where are two locations a developer can look to find information about the status of batch or future calls? (Choose two.)**

- **A.** Developer Console ❌
- **B.** Apex Flex Queue ✅
- **C.** Apex Jobs ✅
- **D.** Paused Flow Interviews component ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên có thể xem thông tin về trạng thái hoạt động của các phương thức Batch hoặc Future Apex ở hai nơi nào trong phần Setup? (Chọn 2)

**💬 Giải thích gốc (English):**
> The Apex Jobs page shows all asynchronous Apex jobs with information about each job’s execution. You can also monitor the status of Apex jobs in the Apex Flex Queue, and reorder them to control which jobs are processed first.

**✅ Tại sao đáp án đúng:**
> B đúng vì Apex Flex Queue là nơi hiển thị và sắp xếp thứ tự của các Batch job đang nằm trong hàng đợi chờ được xử lý (tối đa 100 job). C đúng vì Apex Jobs hiển thị lịch sử và trạng thái hiện tại của toàn bộ các tác vụ chạy bất đồng bộ (bao gồm cả Batch Apex, Future methods, Queueable Apex và Scheduled Apex).

**❌ Tại sao đáp án sai:**
> **A.** Developer Console chỉ hỗ trợ xem log thực thi tức thời chứ không quản lý trạng thái tổng quan các job bất đồng bộ trong hàng đợi hệ thống tốt như Setup.
> **D.** Paused Flow Interviews chỉ hiển thị các lượt chạy Flow đang bị tạm dừng chờ điều kiện, chả liên quan gì đến code Apex Batch/Future.

**💡 Từ khóa ghi nhớ:** `Theo dõi tiến độ Async Apex (Batch, Future, Queueable) -> Vào Apex Jobs & Apex Flex Queue.`

---

## Câu 164

**🔵 A Salesforce Administrator used Flow Builder to create a flow named 'accountOnboarding'. The flow must be used inside an Aura component. Which tag should a developer use to display the flow in the component?**

- **A.** lightning-flow ❌
- **B.** aura-flow ❌
- **C.** lightning:flow ✅
- **D.** aura:flow ❌

**📝 Dịch tiếng Việt:**
> Một Salesforce Admin dùng Flow Builder để tạo một Flow tên là accountOnboarding. Flow này cần được nhúng để chạy bên trong một Aura component. Lập trình viên nên dùng thẻ nào để hiển thị Flow này?

**💬 Giải thích gốc (English):**
> To display a flow inside an Aura component, the developer should use the <lightning:flow> tag. This tag is specifically designed to embed flows within Aura components.

**✅ Tại sao đáp án đúng:**
> Trong framework Aura Component, thẻ chuẩn được Salesforce thiết kế để gọi và chạy một Flow chính là <lightning:flow> (C). Mày chỉ cần đặt thẻ này và truyền thuộc tính flowName vào là xong.

**❌ Tại sao đáp án sai:**
> **A.** lightning-flow (dùng dấu gạch ngang -) là cú pháp của Lightning Web Components (LWC), đem sang Aura gõ là ăn hành ngay.
> **B.** aura-flow là hàng giả tự chế, Salesforce không hề hỗ trợ thẻ này.
> **D.** aura:flow là cái tên nghe có vẻ đúng nhưng thực tế namespace aura: chỉ dành cho các tag logic cốt lõi, không có tag flow.

**💡 Từ khóa ghi nhớ:** `Aura Component dùng dấu hai chấm : (lightning:flow), LWC dùng dấu gạch ngang - (lightning-flow).`

---

## Câu 165

**🔵 A developer must create a CreditCardPayment class that provides an implementation of an existing Payment class.
public virtual class Payment{
public virtual void makePayment(Decimal amount){ /*implementation*/}
}
Which is the correct implementation?**

- **A.** public class CreditCardPayment extends Payment {
  public virtual void makePayment(Decimal amount) { /*implementation*/ }
} ❌
- **B.** public class CreditCardPayment extends Payment {
  public override void makePayment(Decimal amount) { /*implementation*/ }
} ✅
- **C.** public class CreditCardPayment implements Payment {
  public virtual void makePayment(Decimal amount) { /*implementation*/ }
} ❌
- **D.** public class CreditCardPayment implements Payment {
  public override void makePayment(Decimal amount) { /*implementation*/ }
} ❌

**📝 Dịch tiếng Việt:**
> Developer cần tạo class CreditCardPayment kế thừa từ class Payment ảo có sẵn: [Payment Class]. Khai báo nào sau đây là đúng cú pháp?

**💬 Giải thích gốc (English):**
> The CreditCardPayment class should extend the Payment class and override the makePayment method to provide its specific implementation.

**✅ Tại sao đáp án đúng:**
> Vì lớp cha Payment là một class ảo thông thường được khai báo với từ khóa virtual, nên class con muốn kế thừa bắt buộc phải dùng từ khóa extends. Đồng thời, để ghi đè (chỉnh sửa lại logic) của phương thức ảo makePayment(), class con bắt buộc phải dùng từ khóa override (B).

**❌ Tại sao đáp án sai:**
> **A.** Sử dụng từ khóa virtual ở class con thay vì override khi muốn ghi đè phương thức lớp cha là sai cú pháp.
> **C.** Từ khóa implements chỉ dành cho interface, không dùng để kế thừa một virtual class thông thường. Ngoài ra cũng sai từ khóa ghi đè.
> **D.** Sử dụng sai từ khóa implements thay vị extends để kế thừa class.

**💡 Từ khóa ghi nhớ:** `Kế thừa Class -> Dùng EXTENDS + OVERRIDE. Hiện thực hóa Interface -> Dùng IMPLEMENTS.`

---

## Câu 166

**🔵 How should a developer make sure that a child record on a custom object, with a lookup to the Account object, has the same sharing access as its associated account?**

- **A.** Create a Sharing Rule comparing the custom object owner to the account owner. ❌
- **B.** Create a validation rule on the custom object comparing the record owners on both records. ❌
- **C.** Include the sharing related list on the custom object page layout. ❌
- **D.** Ensure that the relationship between the objects is Master-Detail. ✅

**📝 Dịch tiếng Việt:**
> Làm thế nào để lập trình viên đảm bảo một bản ghi con trên một custom object (có liên kết lookup tới Account) luôn tự động có chung quyền hạn chia sẻ bảo mật (sharing access) y hệt như Account cha của nó?

**💬 Giải thích gốc (English):**
> When you set up a Master-Detail relationship, the child record inherits the sharing and security settings of the parent record. This means that if a user has access to the parent record (in this case, the Account), they will automatically have the same level of access to the child records (the custom object records).

**✅ Tại sao đáp án đúng:**
> Cách đơn giản, tối ưu nhất mà không cần viết một dòng code nào là chuyển đổi/thiết lập mối quan hệ giữa hai đối tượng thành mối quan hệ Master-Detail (D). Trong Salesforce, bản ghi con (Detail) trong quan hệ Master-Detail luôn tự động kế thừa 100% cấu hình chia sẻ và bảo mật từ bản ghi cha (Master).

**❌ Tại sao đáp án sai:**
> **A.** Tạo Sharing Rule đối chiếu Owner rất cồng kềnh, hoạt động kém hiệu quả và không tự động cập nhật mượt mà khi đổi chủ sở hữu như Master-Detail.
> **B.** Validation Rule chỉ dùng để chặn lưu bản ghi khi sai điều kiện dữ liệu nhập vào, hoàn toàn bất lực trong việc cấp quyền truy cập bảo mật.
> **C.** Thêm Sharing Related List vào page layout chỉ để hiển thị nút chia sẻ thủ công cho user bấm bằng tay, không giải quyết được tính tự động hóa.

**💡 Từ khóa ghi nhớ:** `Con muốn thừa kế hoàn hảo quyền bảo mật của Cha -> Bắt buộc thiết lập quan hệ MASTER-DETAIL.`

---

## Câu 167

**🔵 Universal Containers wants a list button to display a Visualforce page that allows users to edit multiple records. Which Visualforce feature supports this requirement?**

- **A.** <apex:listButton> tag ❌
- **B.** recordSetVar page attribute ✅
- **C.** custom controller ❌
- **D.** controller extension ❌

**📝 Dịch tiếng Việt:**
> Universal Containers muốn tạo một list button hiển thị trang Visualforce cho phép người dùng chỉnh sửa nhiều bản ghi cùng một lúc. Tính năng Visualforce nào hỗ trợ yêu cầu này?

**💬 Giải thích gốc (English):**
> The recordSetVar attribute in Visualforce allows you to work with a collection of records. This is particularly useful for creating pages that enable users to edit multiple records at once. By using recordSetVar, you can pass a set of records to your Visualforce page and then iterate over them to display and edit each record.

**✅ Tại sao đáp án đúng:**
> Đó chính là thuộc tính recordSetVar (B) khai báo trong thẻ <apex:page>. Khi mày set thuộc tính này, Standard Controller thông thường của đối tượng sẽ được 'nâng cấp' thành Standard List Controller, cho phép trang Visualforce hứng và xử lý trọn vẹn danh sách các bản ghi được chọn từ List View.

**❌ Tại sao đáp án sai:**
> **A.** Thẻ <apex:listButton> chỉ dùng để định nghĩa cái nút hiển thị trên layout chứ không mang lại khả năng xử lý danh sách bản ghi cho trang.
> **C.** Custom Controller bắt buộc mày phải tự viết code Apex query dữ liệu rất cực khổ, không tối ưu và có sẵn như recordSetVar.
> **D.** Controller Extension chỉ là lớp viết thêm để bổ sung tính năng cho Controller chính chứ không tự động biến Standard Controller thành List Controller.

**💡 Từ khóa ghi nhớ:** `Keyword: List View Button / Edit Multiple Records -> Bắt buộc khai báo thuộc tính recordSetVar trên trang Visualforce.`

---

## Câu 168

**🔵 Which code in a Visualforce page and/or controller might present a security vulnerability?**

- **A.** <apex:outputField value="{!ctrl.userInput}" /> ❌
- **B.** <apex:outputText escape="false" value=" {!$CurrentPage.parameters.userInput}" /> ✅
- **C.** <apex:outputText value="{!$CurrentPage.parameters.userInput}" /> ❌
- **D.** <apex:outputField escape="false" value="{!ctrl.userInput}" /> ❌

**📝 Dịch tiếng Việt:**
> Đoạn code nào trong trang Visualforce hoặc Controller dưới đây có thể gây ra lỗ hổng bảo mật nghiêm trọng?

**💬 Giải thích gốc (English):**
> Disabling Escape on Visualforce Tags
> By default, nearly all Visualforce tags escape the XSS-vulnerable characters. You can disable this behavior by setting the optional attribute escape="false". For example, this output is vulnerable to XSS attacks. When escape="false" is used, the input is not escaped, meaning any HTML or JavaScript code included in the user input will be rendered as-is, potentially allowing malicious scripts to be executed.

**✅ Tại sao đáp án đúng:**
> B đúng vì in trực tiếp tham số URL của người dùng nhập (`$CurrentPage.parameters.userInput`) mà lại đặt thuộc tính `escape="false"`. Điều này tắt tính năng tự động mã hóa HTML của Visualforce, khiến trang dễ dàng bị tấn công Cross-Site Scripting (XSS) nếu người dùng truyền mã JavaScript độc hại qua URL.

**❌ Tại sao đáp án sai:**
> **A.** Rất an toàn vì `<apex:outputField>` mặc định luôn tự động escape HTML và tuân thủ chặt chẽ bảo mật FLS của trường.
> **C.** Rất an toàn vì `<apex:outputText>` mặc định sẽ tự động escape HTML (escape="true") trừ khi được tắt tường minh.
> **D.** Thẻ `<apex:outputField>` không hỗ trợ thuộc tính `escape="false"` và nó luôn tự động escape HTML, nên không gây ra lỗ hổng bảo mật từ URL parameter.

**💡 Từ khóa ghi nhớ:** `Visualforce XSS = Tắt escape (escape="false") + In trực tiếp tham số URL đầu vào của người dùng.`

---

## Câu 169

**🔵 What should a developer do to check the code coverage of a class after running all tests?**

- **A.** Select and run the class on the Apex Test Execution page in the Developer Console. ❌
- **B.** View the code coverage percentage for the class using the Overall Code Coverage panel in the Developer Console Tests tab. ✅
- **C.** View the Code Coverage column in the list view on the Apex Classes page. ❌
- **D.** View the Class Test Percentage tab on the Apex Class list view in Salesforce Setup. ❌

**📝 Dịch tiếng Việt:**
> Chạy xong đống test class rồi, giờ muốn soi xem class Apex của mình đã được phủ bao nhiêu phần trăm (%) coverage thì check ở xó nào?

**💬 Giải thích gốc (English):**
> After running tests, the Developer Console provides a comprehensive view of code coverage. The Overall Code Coverage panel in the Tests tab displays the code coverage percentage for each Apex class that has been included in a test run.

**✅ Tại sao đáp án đúng:**
> Chọn B. Trong Developer Console, chuyển sang tab 'Tests' và ngó vào panel 'Overall Code Coverage'. Nơi đây sẽ phơi bày toàn bộ phần trăm phủ code của từng class cực kỳ chi tiết, giúp mày biết chỗ nào chưa chạy qua để mà viết thêm test.

**❌ Tại sao đáp án sai:**
> **A.** Apex Test Execution trong Setup chỉ chạy test hàng loạt chứ không hiển thị phần trăm code coverage chi tiết dạng tương tác như panel Overall Code Coverage.
> **C.** Cột Code Coverage trong Setup -> Apex Classes chỉ hiển thị một con số chung chung, không cho phép mày xem cụ thể dòng nào màu đỏ (chưa test) hay dòng nào màu xanh (đã test) như Developer Console.
> **D.** Cái tab 'Class Test Percentage' là hàng fake tự vẽ ra của Salesforce để đi lừa gà đấy, Setup làm gì có tab nào tên như vậy.

**💡 Từ khóa ghi nhớ:** `Xem % coverage nhanh nhất và chi tiết nhất -> Mở Developer Console -> Tab Tests -> Panel Overall Code Coverage.`

---

## Câu 170

**🔵 Universal Containers decides to use exclusively declarative development to build out a new Salesforce application. Which three options should be used to build out the database layer for the application? (Choose three.)**

- **A.** Flows ❌
- **B.** Roll-up summaries ✅
- **C.** Triggers ❌
- **D.** Relationships ✅
- **E.** Custom objects and fields ✅

**📝 Dịch tiếng Việt:**
> Universal Containers chơi hệ 'no-code', quyết định chỉ dùng cấu hình khai báo (declarative) để xây dựng ứng dụng mới. Ba tùy chọn nào nên được dùng để dựng lớp cơ sở dữ liệu (Database Layer) cho con app này? (Chọn 3)

**💬 Giải thích gốc (English):**
> Database Layer
> Declarative: Custom Objects, Fields, Relationships, Rollups
> Coding: Apex Triggers

**✅ Tại sao đáp án đúng:**
> Lớp cơ sở dữ liệu (Database Layer) là nơi lưu trữ và định nghĩa cấu trúc dữ liệu. Do đó: E đúng vì Custom objects and fields là các bảng và cột vật lý để chứa dữ liệu. D đúng vì Relationships (Lookup, Master-Detail) dùng để liên kết các bảng dữ liệu với nhau. B đúng vì Roll-up summaries là tính năng no-code tự động tính toán tổng hợp dữ liệu từ bảng con lên bảng cha.

**❌ Tại sao đáp án sai:**
> **A.** Flows thuộc về tầng xử lý logic nghiệp vụ và tự động hóa quy trình (Logic/Controller Layer), chứ không dùng để định nghĩa cấu trúc vật lý của database.
> **C.** Triggers là code Apex thuần túy, vừa thuộc tầng code (programmatic) vừa nằm ở tầng logic điều khiển chứ liên quan gì đến database layer.

**💡 Từ khóa ghi nhớ:** `Database Layer dạng declarative (no-code) -> Bắt cặp ngay: Objects/Fields, Relationships, Roll-up Summaries.`

---

## Câu 171

**🔵 Which three statements are true regarding the @isTest annotation? (Choose three.)**

- **A.** A method annotated @isTest(SeeAllData=true) in a class annotated @isTest(SeeAllData=false) has access to all org data. ✅
- **B.** A method annotated @isTest(SeeAllData=false) in a class annotated @isTest(SeeAllData=true) has access to all org data. ✅
- **C.** A class containing test methods counts toward the Apex code limit regardless of any @isTest annotation. ❌
- **D.** Products and Pricebooks are visible in a test even if a class is annotated @isTest(SeeAllData=false). ❌
- **E.** Profiles are visible in a test even if a class is annotated @isTest(SeeAllData=false). ✅

**📝 Dịch tiếng Việt:**
> Ba phát biểu nào sau đây là ĐÚNG khi nói về annotation @isTest trong lập trình Apex? (Chọn 3)

**💬 Giải thích gốc (English):**
> Considerations for the @IsTest(SeeAllData=true) Annotation
> If a test class is defined with the @IsTest(SeeAllData=true) annotation, the SeeAllData=true applies to all test methods that don’t explicitly set the SeeAllData keyword.
> The @IsTest(SeeAllData=true) annotation is used to open up data access when applied at the class or method level. However, if the containing class has been annotated with @IsTest(SeeAllData=true), annotating a method with @IsTest(SeeAllData=false) is ignored for that method. In this case, that method still has access to all the data in the organization. Annotating a method with @IsTest(SeeAllData=true) overrides, for that method, an @IsTest(SeeAllData=false) annotation on the class.
> @IsTest(SeeAllData=true) and @IsTest(IsParallel=true) annotations can’t be used together on the same Apex method.

**✅ Tại sao đáp án đúng:**
> A đúng vì @isTest(SeeAllData=true) khai báo ở cấp method sẽ override cấu hình false ở cấp class, giúp method đó xem được dữ liệu thật. E đúng vì các đối tượng Metadata/Setup hệ thống như Profile, User, RecordType... mặc định luôn hiển thị trong test class bất kể SeeAllData là true hay false. Ngoài ra, B cũng là phát biểu đúng của Salesforce: Nếu class cha đã mở SeeAllData=true, phương thức con cố tình set SeeAllData=false sẽ bị hệ thống phớt lờ và vẫn thấy dữ liệu thật.

**❌ Tại sao đáp án sai:**
> **C.** Láo nháo! Các test class có gắn @isTest hoàn toàn được MIỄN PHÍ dung lượng lưu trữ, không hề bị tính vào giới hạn 3 MB code Apex của Org nhé cưng.
> **D.** Products và Pricebooks trong các phiên bản Salesforce hiện đại đã bị cô lập dữ liệu cực kỳ nghiêm ngặt, bắt buộc phải tạo data test giả lập hoặc bật SeeAllData=true mới thấy được.

**💡 Từ khóa ghi nhớ:** `Mẹo @isTest: Class test được miễn phí dung lượng code 3MB. SeeAllData=true cha mở thì con không thể đóng! Profile/User luôn hiển thị trong test.`

---

## Câu 172

**🔵 The Job_Application__c custom object has a field that is a Master-Detail relationship to the Contact object, where the Contact object is the Master. As part of a feature implementation, a developer needs to retrieve a list containing all Contact records where the related Account Industry is 'Technology' while also retrieving the contact's Job_Application__c records. Based on the object's relationships, what is the most efficient statement to retrieve the list of contacts?**

- **A.** [SELECT Id, (SELECT Id FROM Job_Applications_r) FROM Contact WHERE Account.Industry = 'Technology']; ✅
- **B.** [SELECT Id, (SELECT Id FROM Job_Applications_r) FROM Contact WHERE Accounts.Industry = 'Technology']; ❌
- **C.** [SELECT Id, (SELECT Id FROM Job_Applications_c) FROM Contact WHERE Accounts.Industry = 'Technology']; ❌
- **D.** [SELECT Id, (SELECT Id FROM Job_Application_c) FROM Contact WHERE Account.Industry = 'Technology']; ❌

**📝 Dịch tiếng Việt:**
> Đối tượng tùy chỉnh Job_Application__c có quan hệ Master-Detail với Contact (trong đó Contact là Master). Lập trình viên cần lấy danh sách Contact có trường Industry của Account liên quan là 'Technology', đồng thời lấy kèm danh sách Job_Application__c con của mỗi Contact. Cú pháp SOQL nào tối ưu nhất?

**💬 Giải thích gốc (English):**
> A: This query correctly references the relationship and filters based on the Account’s Industry
> B: This option is incorrect because the correct relationship name for the Account object is Account, not Accounts.
> C: This option is incorrect for two reasons: it uses Accounts instead of Account, and it incorrectly references Job_Applications_c instead of Job_Applications_r.
> D: This option is incorrect because it uses Job_Application_c instead of Job_Applications_r.

**✅ Tại sao đáp án đúng:**
> Đáp án A chuẩn không cần chỉnh. Khi truy vấn từ Cha xuống Con (Contact xuống Job_Application__c), ta dùng Subquery và bắt buộc phải dùng tên mối quan hệ con ở dạng số nhiều kèm đuôi __r (Job_Applications__r). Đồng thời, khi đi từ Con lên Cha (Contact lên Account), ta dùng tên trường quan hệ ở dạng số ít (Account.Industry).

**❌ Tại sao đáp án sai:**
> **B.** Sai lầm ngớ ngẩn ở phần lọc: Accounts.Industry (dùng dạng số nhiều 'Accounts' là oẳng ngay vì đi từ con lên cha phải dùng số ít).
> **C.** Sai cú pháp subquery: dùng đuôi __c thay vì __r cho mối quan hệ con, và dùng Accounts số nhiều ở phần filter.
> **D.** Thiếu chữ 's' ở tên quan hệ số nhiều Job_Applications__r và dùng sai đuôi __c thành _c.

**💡 Từ khóa ghi nhớ:** `SOQL cha xuống con -> subquery số nhiều đuôi __r ((SELECT ... FROM Children__r)). SOQL con lên cha -> dùng tên cha số ít (Account.Name).`

---

## Câu 173

**🔵 Which two SOSL searches will return records matching search criteria contained in any of the searchable text fields on an object? (Choose two.)**

- **A.** [FIND 'Acme*' IN ANY FIELDS RETURNING Account, Opportunity]; ❌
- **B.** [FIND 'Acme*' RETURNING Account, Opportunity]; ✅
- **C.** [FIND 'Acme*' IN ALL FIELDS RETURNING Account, Opportunity]; ✅
- **D.** [FIND 'Acme*' IN TEXT FIELDS RETURNING Account, Opportunity]; ❌

**📝 Dịch tiếng Việt:**
> Hai câu lệnh tìm kiếm SOSL nào sẽ trả về các bản ghi khớp với điều kiện tìm kiếm nằm trong bất kỳ trường văn bản nào có thể tìm kiếm được trên đối tượng? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> B đúng vì trong ngôn ngữ SOSL, nếu mày không khai báo từ khóa chỉ định phạm vi tìm kiếm thì Salesforce sẽ tự động ngầm định tìm kiếm trên toàn bộ các trường (IN ALL FIELDS). C đúng vì khai báo tường minh từ khóa IN ALL FIELDS để quét sạch sành sanh mọi trường văn bản.

**❌ Tại sao đáp án sai:**
> **A.** Làm gì có từ khóa nào tên là IN ANY FIELDS hả trời? Tự chế cú pháp là ăn lỗi biên dịch ngay.
> **D.** IN TEXT FIELDS cũng là hàng fake tự thiết kế, SOSL không chơi hệ này.

**💡 Từ khóa ghi nhớ:** `SOSL mặc định tìm kiếm trên mọi trường văn bản -> Dùng IN ALL FIELDS hoặc không viết gì cả.`

---

## Câu 174

**🔵 A developer needs to save a List of existing Account records named myAccounts to the database, but the records do not contain Salesforce Id values. Only the value of a custom text field configured as an External ID with an API name of Foreign_Key__c is known. Which two statements enable the developer to save the records to the database without an Id? (Choose two.)**

- **A.** Upsert myAccounts Foreign_Key__c; ✅
- **B.** Upsert myAccounts(Foreign_Key__c); ❌
- **C.** Database.upsert (myAccounts, Foreign_Key__c); ✅
- **D.** Database.upsert(myAccounts).Foreign_Key__c; ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên cần lưu một danh sách Account có tên myAccounts vào database nhưng các bản ghi này không chứa Id Salesforce. Chỉ biết giá trị của trường text custom đóng vai trò External ID tên là Foreign_Key__c. Hai câu lệnh nào giúp thực hiện việc này? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> A đúng vì đây là cú pháp DML upsert truyền thống của Apex, cho phép truyền trực tiếp tên trường External ID đằng sau danh sách bản ghi. C đúng vì đây là cách gọi phương thức của lớp Database.upsert(), truyền trường External ID làm tham số thứ hai cực kỳ chuẩn chỉnh và hỗ trợ xử lý lỗi linh hoạt (allOrNone).

**❌ Tại sao đáp án sai:**
> **B.** Cú pháp DML mà bọc tên trường trong dấu ngoặc đơn (Foreign_Key__c) là sai bét quy chuẩn của Apex.
> **D.** Viết kiểu chấm đuôi Database.upsert(myAccounts).Foreign_Key__c là cú pháp hoang đường tự chế, Apex compile báo lỗi tức thì.

**💡 Từ khóa ghi nhớ:** `Upsert bằng External ID -> 1. Cú pháp DML: upsert list External_Field__c; 2. Cú pháp Database: Database.upsert(list, External_Field__c);`

---

## Câu 175

**🔵 How should a developer avoid hitting the governor limits in test methods?**

- **A.** Use @TestVisible on methods that create records. ❌
- **B.** Use Test.loadData() to load data from a static resource. ❌
- **C.** Use @IsTest (SeeAllData=true) to use existing data. ❌
- **D.** Use Test.startTest() to reset governor limits. ✅

**📝 Dịch tiếng Việt:**
> Làm thế nào để lập trình viên tránh bị đụng trần giới hạn (governor limits) khi chạy các phương thức test?

**💬 Giải thích gốc (English):**
> The Test.startTest() and Test.stopTest() methods are used to reset governor limits within test methods. This allows the developer to perform setup operations before Test.startTest() and then execute the actual test code within the new set of governor limits.

**✅ Tại sao đáp án đúng:**
> Sử dụng bộ đôi thần thánh Test.startTest() và Test.stopTest() (D). Khi gọi Test.startTest(), Salesforce sẽ cấp riêng một bộ đếm giới hạn governor limit mới tinh và độc lập cho đoạn code chạy bên trong nó, giúp tách biệt hoàn toàn giới hạn của khâu chuẩn bị dữ liệu mẫu (setup data) và khâu test logic thực tế.

**❌ Tại sao đáp án sai:**
> **A.** @TestVisible chỉ có tác dụng giúp test class nhìn thấy và gọi được các biến/method private của class chính, chả có phép thuật gì để nới lỏng hay reset limit cả.
> **B.** Test.loadData() chỉ là phao cứu sinh để nạp dữ liệu mẫu nhanh từ file CSV trong Static Resource, không giúp gì trong việc reset hay tránh đụng limit.
> **C.** Bật SeeAllData=true làm test class truy cập thẳng vào data thật của Org, vừa là bad practice và dễ gây lỗi dữ liệu chứ tuổi gì can thiệp được vào giới hạn limits.

**💡 Từ khóa ghi nhớ:** `Né đụng trần governor limit trong test -> Bọc code chạy thử vào giữa Test.startTest() và Test.stopTest().`

---

## Câu 176

**🔵 Universal Containers wants Opportunities to be locked from editing when reaching the Closed/Won stage. Which two strategies should a developer use to accomplish this? (Choose two.)**

- **A.** Use a Flow Builder. ❌
- **B.** Use a validation rule. ✅
- **C.** Use the Process Automation Settings. ❌
- **D.** Mark fields as read-only on the page layout. ✅

**📝 Dịch tiếng Việt:**
> Universal Containers muốn khóa các Opportunity không cho phép chỉnh sửa bất kỳ thứ gì khi đã chuyển sang trạng thái Closed/Won. Hai chiến lược nào lập trình viên nên sử dụng để thực hiện việc này? (Chọn 2)

**💬 Giải thích gốc (English):**
> Using a validation rule  and marking fields as read-only on the page layout are indeed effective strategies to lock Opportunities from editing when they reach the Closed/Won stage.

**✅ Tại sao đáp án đúng:**
> B đúng vì Validation Rule là lá chắn thép ở backend, chỉ cần viết điều kiện nếu bản ghi đã ở trạng thái Closed/Won thì chặn đứng không cho Save khi có thay đổi. D đúng vì Page Layout cho phép thiết lập các trường thành Read-Only động dựa trên Record Type của trạng thái Closed/Won để khóa cứng giao diện của user trên UI.

**❌ Tại sao đáp án sai:**
> **A.** Flow Builder chạy ngầm ở backend sau khi dữ liệu đã gửi đi, không thể khóa giao diện trực quan hay chặn nhập liệu tối ưu như Validation Rule.
> **C.** Process Automation Settings chỉ là nơi bật/tắt cấu hình chung của hệ thống tự động hóa, tuổi gì khóa được bản ghi.

**💡 Từ khóa ghi nhớ:** `Khóa bản ghi (Read-only) -> 1. Validation Rule (Chặn lưu); 2. Page Layout Read-only (Khóa UI).`

---

## Câu 177

**🔵 A developer wants to display all of the picklist entries for the Opportunity StageName field and all of the available record types for the Opportunity object on a Visualforce page. Which two actions should the developer perform to get the available picklist values and record types in the controller? (Choose two.)**

- **A.** Use Schema.RecordTypeInfo returned by Opportunity.SObjectType.getDescribe().getRecordTypeInfos(). ✅
- **B.** Use Schema.PicklistEntry returned by Opportunity.SObjectType.getDescribe().getPicklistValues (). ❌
- **C.** Use Schema.RecordTypeInfo returned by RecordType.SObjectType.getDescribe().getRecordTypeInfos(). ❌
- **D.** Use Schema.PicklistEntry returned by Opportunity.StageName.getDescribe().getPicklistValues (). ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên muốn hiển thị toàn bộ các giá trị picklist của trường StageName trên Opportunity và tất cả Record Types hiện có của Opportunity lên một trang Visualforce. Hai hành động nào giúp lấy các thông tin này trong controller thông qua mô tả lược đồ (Schema Describe)? (Chọn 2)

**💬 Giải thích gốc (English):**
> Use Schema.RecordTypeInfo returned by Opportunity.SObjectType.getDescribe().getRecordTypeInfos(): This will retrieve the available record types for the Opportunity object.
> Use Schema.PicklistEntry returned by Opportunity.StageName.getDescribe().getPicklistValues(): This will retrieve the picklist entries for the Opportunity StageName field.

**✅ Tại sao đáp án đúng:**
> A đúng vì để lấy danh sách Record Types của Opportunity, ta describe đối tượng Opportunity thông qua Opportunity.SObjectType.getDescribe() rồi gọi tiếp phương thức getRecordTypeInfos(). D đúng vì để lấy các giá trị picklist của trường StageName, ta describe trực tiếp trường này thông qua Opportunity.StageName.getDescribe() rồi gọi phương thức getPicklistValues().

**❌ Tại sao đáp án sai:**
> **B.** Ủa Alo? Làm sao gọi getPicklistValues() từ mô tả cấp đối tượng Opportunity được? Phải describe đúng cấp trường (Field) như câu D mới chuẩn chứ.
> **C.** Describe đối tượng RecordType hệ thống chỉ trả về thông tin Record Type của chính bảng RecordType đó, chứ không lấy được danh sách Record Type riêng của Opportunity đâu nha.

**💡 Từ khóa ghi nhớ:** `Lấy Record Types -> Đối tượng.SObjectType.getDescribe().getRecordTypeInfos(). Lấy Picklist -> Trường.getDescribe().getPicklistValues().`

---

## Câu 178

**🔵 An org has two custom objects: Plan__c, that has a master-detail relationship to the Account object Plan_Item__c, that has a master-detail relationship to the Plan__c object. What should a developer use to create a Visualforce section on the Account page layout that displays all of the Plan__c records related to the Account and all of the Plan_Item__c records related to those Plan__c records?**

- **A.** A standard controller with a custom controller ❌
- **B.** A standard controller with a controller extension ✅
- **C.** A controller extension with a custom controller ❌
- **D.** A custom controller by itself ❌

**📝 Dịch tiếng Việt:**
> Org có 2 đối tượng tùy chỉnh: Plan__c (có quan hệ master-detail với Account) và Plan_Item__c (có quan hệ master-detail với Plan__c). Lập trình viên nên sử dụng gì để tạo một section Visualforce trên Account page layout hiển thị tất cả bản ghi Plan__c của Account đó kèm theo các bản ghi Plan_Item__c con liên quan?

**💬 Giải thích gốc (English):**
> Using a standard controller for the Account object allows you to leverage built-in functionality, while a controller extension can be used to add custom logic to retrieve and display the related Plan__c and Plan_Item__c records.

**✅ Tại sao đáp án đúng:**
> Sử dụng một Standard Controller kết hợp với một Controller Extension (B). Vì trang này được nhúng trực tiếp trên Account Layout nên bắt buộc phải dùng standardController="Account" để nhận ngữ cảnh Account đang hiển thị. Để xử lý cấu trúc dữ liệu cha-con-cháu phức tạp và truy vấn sâu xuống các cháu Plan_Item__c, ta viết thêm Controller Extension class để thực hiện câu SOQL tùy chỉnh.

**❌ Tại sao đáp án sai:**
> **A.** Không thể khai báo đồng thời cả Custom Controller và Standard Controller độc lập trong cùng một trang Visualforce, compile báo lỗi ngay.
> **C.** Controller extension bắt buộc phải đi kèm với một Standard Controller hoặc Custom Controller chứ không chơi kiểu lơ lửng này.
> **D.** Nếu chỉ dùng Custom Controller đơn lẻ, trang Visualforce sẽ không thể nhúng trực tiếp vào trang chi tiết Account chuẩn được vì thiếu standard controller làm cầu nối.

**💡 Từ khóa ghi nhớ:** `Nhúng trang Visualforce vào Page Layout chuẩn + Cần thêm logic Apex nâng cao -> Sử dụng công thức: Standard Controller + Controller Extension.`

---

## Câu 179

**🔵 A developer uses a loop to check each Contact in a list. When a Contact with the Title of 'Boss' is found, the Apex method should jump to the first line of code outside of the for loop. Which Apex solution will let the developer implement this requirement?**

- **A.** return; ❌
- **B.** continue; ❌
- **C.** break; ✅
- **D.** System.assert(false); ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên sử dụng vòng lặp để kiểm tra từng Contact trong danh sách. Khi gặp Contact có Title là 'Boss', phương thức Apex cần dừng lặp lập tức và nhảy xuống dòng code đầu tiên bên ngoài vòng lặp. Cú pháp Apex nào giúp hiện thực hóa yêu cầu này?

**💬 Giải thích gốc (English):**
> The break statement exits the loop immediately, allowing the code execution to continue from the first line outside the loop.

**✅ Tại sao đáp án đúng:**
> Sử dụng câu lệnh break; (C). Lệnh break sẽ ngay lập tức chấm dứt vòng lặp for hoặc while hiện tại và chuyển quyền thực thi xuống câu lệnh đầu tiên ngay bên dưới khối lặp.

**❌ Tại sao đáp án sai:**
> **A.** return; sẽ thoát sạch sành sanh ra khỏi phương thức hiện tại, không chạy bất kỳ dòng code nào tiếp theo bên dưới vòng lặp nữa.
> **B.** continue; chỉ bỏ qua lượt lặp hiện tại của phần tử đó và tiếp tục nhảy sang duyệt phần tử tiếp theo trong danh sách chứ không thoát loop.
> **D.** System.assert(false); sẽ ngay lập tức làm sập transaction và ném ra lỗi kiểm thử AssertException, chỉ dùng trong test class để bắt lỗi chứ dùng trong code chạy thật là ăn hành cả lũ.

**💡 Từ khóa ghi nhớ:** `Dừng lặp thoát loop ngay lập tức -> Dùng break. Bỏ qua lượt lặp hiện tại chạy tiếp -> Dùng continue.`

---

## Câu 180

**🔵 A business has a proprietary Order Management System (OMS) that creates orders from their website and fulfills the orders. When the order is created in the OMS, an integration also creates an order record in Salesforce and relates it to the contact as identified by the email on the order. As the order goes through different stages in the OMS, the integration also updates it in Salesforce. It is noticed that each update from the OMS creates a new order record in Salesforce. Which two actions will prevent the duplicate order records from being created in Salesforce? (Choose two.)**

- **A.** Use the order number from the OMS as an external ID. ✅
- **B.** Write a before trigger on the order object to delete any duplicates. ❌
- **C.** Ensure that the order number in the OMS is unique. ✅
- **D.** Use the email on the contact record as an external ID. ❌

**📝 Dịch tiếng Việt:**
> Một hệ thống quản lý đơn hàng ngoài (OMS) tạo và xử lý đơn hàng. Tích hợp tạo Order trong Salesforce dựa trên Email của Contact. Mỗi lần OMS gửi cập nhật trạng thái đơn hàng, Salesforce lại tạo mới một bản ghi Order trùng lặp. Hai hành động nào giúp ngăn chặn việc này? (Chọn 2)

**💬 Giải thích gốc (English):**
> Use the order number from the OMS as an external ID.
> By setting the order number as an external ID, Salesforce can recognize and update existing records instead of creating new ones.
> Ensure that the order number in the OMS is unique.
> Ensuring the uniqueness of the order number in the OMS helps maintain data integrity and prevents the creation of duplicate records.

**✅ Tại sao đáp án đúng:**
> A đúng vì đánh dấu trường mã đơn hàng từ OMS là trường External ID trong Salesforce. C đúng vì đảm bảo mã đơn hàng OMS gửi sang là duy nhất (Unique). Khi đó, hệ thống tích hợp gọi lệnh upsert dựa trên khóa External ID này để tự động cập nhật bản ghi có sẵn thay vì chèn mới trùng lặp.

**❌ Tại sao đáp án sai:**
> **B.** Viết trigger delete bản ghi trùng sau khi insert là giải pháp tồi tệ, cực kỳ đi vào lòng đất vì làm lãng phí ID bản ghi và tiêu tốn cực nhiều tài nguyên hệ thống vô ích.
> **D.** Email của Contact làm External ID chỉ giúp liên kết Contact với Order, không thể giúp định danh duy nhất cho từng bản ghi Order cụ thể được.

**💡 Từ khóa ghi nhớ:** `Tránh tạo bản ghi trùng lặp từ hệ thống ngoài -> Sử dụng mã hệ thống ngoài làm EXTERNAL ID + Gọi lệnh UPSERT.`

---

## Câu 181

**🔵 What is the impact of declaring an Apex class using the `without sharing` keywords?**

- **A.** Only records owned by the current user can be updated. ❌
- **B.** Sharing restrictions for the current user are bypassed. ✅
- **C.** Records created by the class cannot have sharing rules. ❌
- **D.** The class can only be used by users with developer rights. ❌

**📝 Dịch tiếng Việt:**
> Việc khai báo một class Apex sử dụng từ khóa `without sharing` sẽ gây ra ảnh hưởng thực tế gì?

**💬 Giải thích gốc (English):**
> Declaring an Apex class using the without sharing keywords means that the class runs in system mode, bypassing the sharing rules of the current user.

**✅ Tại sao đáp án đúng:**
> B đúng vì `without sharing` chính là tấm vé thông hành quyền lực, giúp class chạy dưới quyền hệ thống (System Mode). Lúc này, Salesforce sẽ bypass (bỏ qua) hoàn toàn các luật chia sẻ dữ liệu (OWD, Sharing Rules) đang áp dụng trên user hiện tại, cho phép xem/sửa tẹt ga mọi bản ghi trong Org.

**❌ Tại sao đáp án sai:**
> **A.** Sai bét! Chạy without sharing thì user thích sờ vào bản ghi của ai cũng được, chứ không bị bó hẹp trong góc nhỏ 'records owned by current user' nữa.
> **C.** Lắp từ khóa sharing hay without sharing vào class chả ảnh hưởng gì đến khả năng thiết lập sharing rules trên các bản ghi sau này được tạo ra cả.
> **D.** Ơ kìa, class Apex sinh ra là để phục vụ cho ứng dụng, bất kỳ user nào có quyền truy cập ứng dụng/hàm đều chạy được hết chứ đâu phải chỉ dành riêng cho mấy ông có quyền Developer.

**💡 Từ khóa ghi nhớ:** `without sharing -> Bỏ qua Sharing Rules của user hiện tại, chạy chế độ System Mode bá đạo!`

---

## Câu 182

**🔵 A developer needs to find information about @future methods that were invoked. From which system monitoring feature can the developer see this information?**

- **A.** Scheduled Jobs ❌
- **B.** Apex Jobs ✅
- **C.** Background Jobs ❌
- **D.** Asynchronous Jobs ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên muốn truy lùng tung tích và thông tin của các phương thức bất đồng bộ `@future` đã được kích hoạt. Mục giám sát nào của hệ thống sẽ phơi bày điều này?

**💬 Giải thích gốc (English):**
> Apex Jobs allows developers to monitor the status of @future methods, along with other asynchronous processes like batch jobs and scheduled jobs.

**✅ Tại sao đáp án đúng:**
> Trang Apex Jobs (B) chính là 'camera an ninh' ghi lại mọi hoạt động bất đồng bộ trong Salesforce. Nó ghi chép không thiếu một vết từ `@future` methods, Batch Apex, cho đến Queueable và Scheduled Apex.

**❌ Tại sao đáp án sai:**
> **A.** Scheduled Jobs chỉ hiển thị lịch trình các tác vụ chạy định kỳ theo lịch (Cron), chứ làm gì theo dõi được mấy hàm @future chạy tức thời khi có sự kiện.
> **C.** Background Jobs không phải là tên một tính năng hay trang quản trị chuẩn dùng để soi lịch sử chạy code Apex trong Salesforce.
> **D.** Asynchronous Jobs là một cụm từ tiếng Anh mô tả chung chung, Salesforce Setup không có mục nào tên như thế này cả.

**💡 Từ khóa ghi nhớ:** `Giám sát mọi tiến trình bất đồng bộ (@future, Batch, Queueable) -> Search ngay APEX JOBS trong Setup.`

---

## Câu 183

**🔵 A developer has a requirement to create an Order when an Opportunity reaches a 'Closed-Won' status. Which tool should be used to implement this requirement?**

- **A.** Lightning Component ❌
- **B.** Apex Trigger ✅
- **C.** Flow Builder ❌
- **D.** Process Builder ❌

**📝 Dịch tiếng Việt:**
> Nghiệp vụ yêu cầu: Tự động tạo mới một bản ghi Order ngay khi Opportunity chuyển sang trạng thái 'Closed-Won'. Công cụ nào tối ưu nhất để thực hiện yêu cầu này?

**💬 Giải thích gốc (English):**
> Process Builder is a powerful tool in Salesforce that allows you to automate business processes. It can be used to create an Order automatically when an Opportunity reaches the ‘Closed-Won’ status without writing any code.

**✅ Tại sao đáp án đúng:**
> Dùng Apex Trigger (B) là giải pháp cổ điển nhưng cực kỳ uy tín và tối ưu hiệu năng về mặt code. Trigger hỗ trợ xử lý dữ liệu hàng loạt cực tốt (bulkified), đảm bảo hệ thống không bị oẳng (LimitException) khi có đợt update hàng ngàn Opportunity sang Closed-Won cùng lúc. (Lưu ý: Mặc dù Flow ngày nay rất mạnh, nhưng trong khuôn khổ thi cử PD1 truyền thống thì Apex Trigger vẫn luôn là đáp án vàng cho các hành động DML chéo đối tượng phức tạp).

**❌ Tại sao đáp án sai:**
> **A.** Lightning Component là để làm giao diện (View), chứ không có nhiệm vụ đi xử lý tự động hóa DML ngầm ở database.
> **C.** Flow rất xịn nhưng đề thi PD1 đời đầu thường ưu tiên chọn Trigger (B) làm đáp án tối ưu nhất cho hiệu năng lập trình.
> **D.** Process Builder chạy siêu cồng kềnh, ngốn CPU time kinh khủng và đã bị khai tử (deprecated), giờ dùng là ăn gạch ngay!

**💡 Từ khóa ghi nhớ:** `Tự động tạo bản ghi chéo đối tượng khi save -> Ưu tiên dùng Apex Trigger (hoặc Flow Builder hiện đại).`

---

## Câu 184

**🔵 Universal Containers has a Visualforce page that displays a table of every Container__c being rented by a given Account. Recently this page is failing with a view state limit because some of the customers rent over 10,000 containers. What should a developer change about the Visualforce page to help with the page load errors?**

- **A.** Use lazy loading and a transient List variable. ❌
- **B.** Use JavaScript remoting with SOQL Offset. ❌
- **C.** Implement pagination with a StandardSetController. ✅
- **D.** Implement pagination with an OffsetController. ❌

**📝 Dịch tiếng Việt:**
> Một trang Visualforce hiển thị danh sách toàn bộ các Container__c đang được thuê bởi một Account. Gần đây, trang này liên tục sập nguồn vì lỗi vượt quá giới hạn View State (View State Limit) do một số khách hàng VIP thuê tới hơn 10,000 container. Lập trình viên nên thay đổi gì để cứu vãn tình thế?

**💬 Giải thích gốc (English):**
> Implement pagination with a StandardSetController. This approach helps manage large datasets by loading only a subset of records at a time, significantly reducing the view state size and improving page performance.

**✅ Tại sao đáp án đúng:**
> Triển khai tính năng phân trang (Pagination) bằng `StandardSetController` (C). Thay vì ôm đồm lôi tuột một lúc 10,000 bản ghi lên nhét đầy vào bộ nhớ View State làm sập trang, ta dùng StandardSetController chia nhỏ ra mỗi trang hiển thị tầm 50-100 bản ghi, giúp trang load siêu nhẹ và mượt mà.

**❌ Tại sao đáp án sai:**
> **A.** Dùng biến `transient` tuy có làm nhẹ View State nhưng lôi 10,000 bản ghi ra render HTML một lúc vẫn khiến trình duyệt của user 'ngáp ngáp' đứng hình.
> **B.** JavaScript remoting kết hợp SOQL Offset cũng là một cách, nhưng không trực quan, dễ cấu hình và chuẩn hóa giao diện bằng `StandardSetController`.
> **D.** Làm gì có cái controller nào tên là `OffsetController` trong thư viện chuẩn của Salesforce, hàng fake đi lừa gà đấy!

**💡 Từ khóa ghi nhớ:** `View State bị đầy / Load hàng ngàn bản ghi -> Nghĩ ngay đến phân trang (Pagination) bằng `StandardSetController`.`

---

## Câu 185

**🔵 What are three techniques that a developer can use to invoke an anonymous block of code? (Choose three.)**

- **A.** Use the SOAP API to make a call to execute anonymous code. ✅
- **B.** Create a Visualforce page that uses a controller class that is declared without sharing. ❌
- **C.** Run code using the Anonymous Apex feature of the Developer's IDE. ✅
- **D.** Type code into the Developer Console and execute it directly. ✅
- **E.** Create and execute a test method that does not specify a runAs() call. ❌

**📝 Dịch tiếng Việt:**
> Ba kỹ thuật nào giúp lập trình viên kích hoạt thực thi một khối mã nguồn vô danh (Anonymous Apex Block)? (Chọn 3)

**✅ Tại sao đáp án đúng:**
> A đúng vì ta hoàn toàn có thể dùng SOAP API gọi hàm executeAnonymous từ hệ thống ngoài. C đúng vì có thể chạy trực tiếp bằng tính năng Anonymous Apex trên các công cụ IDE của dev (như VS Code). D đúng vì cửa sổ 'Execute Anonymous' trong Developer Console là nơi quốc dân mà ai cũng mở hàng ngày để test code nhanh.

**❌ Tại sao đáp án sai:**
> **B.** Tạo trang Visualforce chỉ để hiển thị giao diện, chả có nút hay chức năng nào cho phép mày gõ và chạy code anonymous tùy ý cả.
> **E.** Chạy test class là để chạy các kịch bản kiểm thử cố định đã viết sẵn trong code, chứ không liên quan đến việc thực thi tự do một khối lệnh vô danh.

**💡 Từ khóa ghi nhớ:** `Chạy Anonymous Apex -> 1. Developer Console; 2. IDE (VS Code); 3. SOAP API call.`

---

## Câu 186

**🔵 A developer has two custom controller extensions where each has a save() method.
<Apex:page standardController="Account", extensions="ExtensionA, ExtensionB">
<apex:commandButton action="{!save}" value="Save"/>
</apex:page>
Which save() method will be called for the following Visualforce page?**

- **A.** ExtensionA save() ✅
- **B.** ExtensionB save() ❌
- **C.** standard controller save() ❌
- **D.** Runtime error will be generated ❌

**📝 Dịch tiếng Việt:**
> Một trang Visualforce khai báo hai class Controller Extension đều chứa phương thức `save()`: `<apex:page standardController="Account" extensions="ExtensionA, ExtensionB">`. Khi bấm nút Save gọi `{!save}`, phương thức của class nào sẽ được ưu tiên chạy?

**💬 Giải thích gốc (English):**
> When multiple controller extensions are specified, the methods in the first extension listed (in this case, ExtensionA) take precedence and will be called.

**✅ Tại sao đáp án đúng:**
> Salesforce giải quyết xung đột phương thức trùng tên bằng cách ưu tiên chạy từ trái qua phải theo thứ tự khai báo trong thuộc tính `extensions`. Vì `ExtensionA` đứng trước nên phương thức `save()` của nó (A) sẽ hốt trọn lượt gọi và đè bẹp phương thức của lớp phía sau.

**❌ Tại sao đáp án sai:**
> **B.** ExtensionB đứng sau nên đành ngậm ngùi ra rìa, phương thức save() của nó bị ExtensionA che phủ hoàn toàn.
> **C.** Standard Controller save() bị cả hai class extension đè lên nên không có cửa được gọi.
> **D.** Hệ thống tự động phân giải thứ tự ưu tiên cực kỳ mượt mà nên không đời nào xảy ra lỗi Runtime Error.

**💡 Từ khóa ghi nhớ:** `Visualforce đa Extension trùng tên method -> Ưu tiên gọi class khai báo đầu tiên (từ trái qua phải).`

---

## Câu 187

**🔵 A developer needs to create a Visualforce page that displays Case data. The page will be used by both support reps and support managers. The Support Rep profile does not allow visibility of the Customer_Satisfaction__c field, but the Support Manager profile does. How can the developer create the page to enforce Field Level Security and keep future maintenance to a minimum?**

- **A.** Create one Visualforce Page for use by both profiles. ✅
- **B.** Use a new Support Manager permission set. ❌
- **C.** Create a separate Visualforce Page for each profile. ❌
- **D.** Use a custom controller that has the with sharing keywords. ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên cần tạo một trang Visualforce hiển thị dữ liệu Case dùng chung cho cả Support Rep và Support Manager. Phân quyền quy định Support Rep cấm xem trường `Customer_Satisfaction__c`, còn Support Manager thì được xem thoải mái. Làm thế nào để vừa thực thi đúng FLS vừa tốn ít công bảo trì nhất?

**💬 Giải thích gốc (English):**
> The best approach to enforce Field Level Security (FLS) and minimize future maintenance is to create one Visualforce Page for use by both profiles . When using Visualforce pages, the platform indeed enforces CRUD and FLS automatically when SObjects and SObject fields are referenced directly. This means that creating a single Visualforce page will handle field visibility based on the user’s profile permissions.
> Note: Using a custom controller with the with sharing keyword ensures record-level security, but for field-level security.

**✅ Tại sao đáp án đúng:**
> Chỉ cần tạo duy nhất MỘT trang Visualforce dùng chung cho cả hai profile (A). Các thẻ Visualforce chuẩn (như `<apex:outputField>`) có cơ chế tự động hóa cực kỳ thông minh: nó tự động check quyền FLS của user đang đăng nhập và âm thầm ẩn trường đó đi nếu user không có quyền xem, dev không cần code thêm một dòng logic ẩn hiện nào.

**❌ Tại sao đáp án sai:**
> **B.** Tự dưng đi tạo Permission Set mới làm gì cho cồng kềnh trong khi bài toán đang hỏi về cách thiết kế trang Visualforce tối ưu nhất.
> **C.** Tách làm hai trang riêng biệt cho hai profile là bước đi siêu cồng kềnh, nhân đôi công sức bảo trì và sửa lỗi sau này.
> **D.** Từ khóa `with sharing` chỉ để ép tuân thủ luật chia sẻ bản ghi (Record-level sharing), chứ hoàn toàn bất lực trước bảo mật cấp trường FLS.

**💡 Từ khóa ghi nhớ:** `Visualforce FLS -> Dùng duy nhất 1 trang Visualforce + thẻ chuẩn (`<apex:outputField>`) tự động lo hết!`

---

## Câu 188

**🔵 Which three steps allow a custom SVG to be included in a Lightning web component? (Choose three.)**

- **A.** Upload the SVG as a static resource. ✅
- **B.** Reference the getter in the HTML template. ✅
- **C.** Import the SVG as a content asset file. ❌
- **D.** Import the static resource and provide a getter for it in JavaScript. ✅
- **E.** Reference the import in the HTML template. ❌

**📝 Dịch tiếng Việt:**
> Ba bước chuẩn chỉ nào cho phép lập trình viên nhúng một file SVG tùy chỉnh vào trong một Lightning Web Component (LWC)? (Chọn 3)

**✅ Tại sao đáp án đúng:**
> Để nhúng SVG vào LWC, quy trình chuẩn như sau: A đúng vì bước đầu tiên phải up file SVG đó lên Static Resource. D đúng vì tiếp theo trong file JavaScript của LWC, ta import static resource đó và viết một hàm getter trả về đường dẫn của file SVG. B đúng vì cuối cùng trong HTML template, ta chỉ cần gọi getter đó để render lên giao diện.

**❌ Tại sao đáp án sai:**
> **C.** Import SVG dưới dạng `content asset file` là sai kỹ thuật, LWC chỉ hỗ trợ import trực tiếp từ Static Resource.
> **E.** HTML template của LWC cấm chỉ việc import trực tiếp bất kỳ tài nguyên tĩnh nào, mọi thứ bắt buộc phải đi qua file JavaScript trung chuyển.

**💡 Từ khóa ghi nhớ:** `Nhúng SVG vào LWC -> Lắp công thức: Static Resource -> Import & Getter trong JS -> Gọi trong HTML qua getter.`

---

## Câu 189

**🔵 A custom Visualforce controller calls the ApexPages.addMessage() method, but no messages are rendering on the page. Which component should be added to the Visualforce page to display the message?**

- **A.** <apex:message for="info"/> ❌
- **B.** <apex:facet name="messages" /> ❌
- **C.** <apex:pageMessage severity="info" /> ❌
- **D.** <apex:pageMessages /> ✅

**📝 Dịch tiếng Việt:**
> Một Custom Visualforce Controller gọi hàm `ApexPages.addMessage()` để ném ra thông báo lỗi nhưng trên giao diện trang chả thấy gì xuất hiện. Lập trình viên cần thêm thẻ nào vào trang Visualforce để hiển thị lỗi này?

**💬 Giải thích gốc (English):**
> To display messages added by the ApexPages.addMessage() method, you should use the <apex:pageMessages /> component. This component displays all messages that were generated for all components on the current page, using Salesforce’s standard styling.

**✅ Tại sao đáp án đúng:**
> Thêm thẻ `<apex:pageMessages />` (D). Thẻ này đóng vai trò như cái 'rổ hứng lỗi', nó sẽ tự động gom toàn bộ các thông báo được tạo bởi `ApexPages.addMessage()` từ Apex Controller và hiển thị chúng lên màn hình cực kỳ đẹp đẽ theo style chuẩn của Salesforce.

**❌ Tại sao đáp án sai:**
> **A.** Thẻ `<apex:message>` (không có chữ 's') chỉ hiển thị lỗi cho duy nhất một trường cụ thể được chỉ định, không hiển thị lỗi chung của trang.
> **B.** Thẻ `<apex:facet>` dùng để cấu hình giao diện cột/tiêu đề cho các bảng dữ liệu, chả liên quan gì đến thông báo lỗi.
> **C.** Thẻ `<apex:pageMessage>` (không có chữ 's' và có viết hoa chữ M) dùng để hiển thị một dòng thông báo tĩnh được viết cứng trên trang chứ không lấy được lỗi động từ Apex Controller.

**💡 Từ khóa ghi nhớ:** `Muốn show toàn bộ lỗi từ `ApexPages.addMessage()` ra Visualforce -> Nhắm mắt chọn ngay `<apex:pageMessages />`.`

---

## Câu 190

**🔵 A Licensed_Professional__c custom object exists in the system with two Master-Detail fields for the following objects: Certification__c and Contact.
Users with the 'Certification Representative' role can access the Certification records they own and view the related Licensed Professionals records, however users with the 'Sales Representative' role report they cannot view any Licensed Professional records even though they own the associated Contact record. What are two likely causes of users in the 'Sales Representative' role not being able to access the Licensed Professional records? (Choose two.)**

- **A.** The organization has a private sharing model for Certification__c and Certification__c is the primary relationship in the Licensed_Professional__c object. ✅
- **B.** The organization's sharing rules for Licensed_Professional__c have not finished their recalculation process. ✅
- **C.** The organization recently modified the Sales Representative role to restrict Read/Write access to Licensed_Professional__c. ❌
- **D.** The organization has a private sharing model for Certification__c, and Contact is the primary relationship in the Licensed_Professional__c object. ❌

**📝 Dịch tiếng Việt:**
> Đối tượng tùy chỉnh `Licensed_Professional__c` có hai trường Master-Detail liên kết với `Certification__c` và `Contact`. User thuộc role 'Certification Rep' xem được các bản ghi con, nhưng 'Sales Rep' (dù sở hữu bản ghi Contact cha) lại khóc thét vì không xem được bất kỳ bản ghi con nào. Hai nguyên nhân khả thi nhất là gì? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> Khi một đối tượng có 2 trường quan hệ Master-Detail, quyền truy cập của nó sẽ bị chi phối hoàn toàn bởi đối tượng Master đầu tiên được tạo (gọi là Primary Master). Do đó: A đúng vì OWD của `Certification__c` đang là Private và nó chính là Primary Master. Sales Rep không có quyền xem bản ghi Certification cha nên bị hệ thống kéo theo xích cổ không cho xem bản ghi con. B đúng vì các Sharing Rules trên đối tượng con đang trong quá trình tính toán lại (recalculation) nên quyền chưa được cập nhật kịp thời.

**❌ Tại sao đáp án sai:**
> **C.** Việc đổi phân quyền CRUD trên Role chỉ giới hạn thao tác tạo/sửa/xóa trên Object nói chung, không giải quyết được lỗi phân quyền bản ghi chi tiết (Sharing) thực tế.
> **D.** Sai logic, nếu `Contact` đóng vai trò là Primary Master thì Sales Rep (chủ Contact) mặc nhiên phải xem được bản ghi con Licensed Professional rồi.

**💡 Từ khóa ghi nhớ:** `Đối tượng con có 2 Master-Detail -> Bảo mật và quyền xem của con ăn theo 100% từ Primary Master (Master tạo đầu tiên).`

---

## Câu 191

**🔵 A developer considers the following snippet of code:
Boolean isOK;
integer x;
String theString = 'Hello';
if(isOK == false && theString == 'Hello'){
x = 1;
}else if(isOK == true && theString == 'Hello'){
x = 2;
}else if(isOK != null && theString == 'Hello'){
x = 3;
}else{
x = 4;
}
Based on this code, what is the value of x?**

- **A.** 1 ❌
- **B.** 2 ❌
- **C.** 3 ❌
- **D.** 4 ✅

**📝 Dịch tiếng Việt:**
> Cho đoạn code sau: [Code Boolean isOK]. Sau khi thực thi xong, biến x sẽ có giá trị là bao nhiêu?

**💬 Giải thích gốc (English):**
> In the given code snippet, the variable isOK is declared but not initialized, so its value is null by default. Let’s analyze the conditions:
> 1. if(isOK == false && theString == 'Hello'): This condition is false because isOK is null.
> 2. else if(isOK == true && theString == 'Hello'): This condition is also false because isOK is null.
> 3. else if(isOK != null && theString == 'Hello'): This condition is false because isOK is null.
> 4. else: This block will execute because none of the previous conditions are true.
> Therefore, the value of x will be set to 4.

**✅ Tại sao đáp án đúng:**
> Giá trị của x là 4 (D). Trong Apex, một biến khi mới khai báo (`Boolean isOK;` và `integer x;`) mà không gán giá trị khởi tạo sẽ mặc định nhận giá trị là `null`. Vì `isOK` là null nên các điều kiện check `isOK == false`, `isOK == true`, và cả `isOK != null` đều trả về `false`. Code tự động nhảy vào khối `else` cuối cùng và gán `x = 4`.

**❌ Tại sao đáp án sai:**
> **A.** Lỗi! isOK không hề được khởi tạo bằng false nên điều kiện đầu tiên bị bỏ qua.
> **B.** Sai! isOK là null chứ không phải true để nhảy vào block này.
> **C.** Sai nốt! Điều kiện check isOK khác null (isOK != null) bị false nên không thể gán x = 3.

**💡 Từ khóa ghi nhớ:** `Mẹo Apex: Mọi biến khai báo khơi khơi không gán giá trị -> Mặc định luôn là NULL!`

---

## Câu 192

**🔵 A developer needs to include a Visualforce page in the detail section of a page layout for the Account object, but does not see the page as an available option in the Page Layout Editor. Which attribute must the developer include in the tag to ensure the Visualforce page can be embedded in a page layout?**

- **A.** standardController= "Account" ✅
- **B.** extensions= "AccountController" ❌
- **C.** controller= "Account" ❌
- **D.** action= "AccountId" ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên muốn nhúng một trang Visualforce vào phần chi tiết (detail section) của Page Layout đối tượng Account, nhưng tìm mỏi mắt không thấy trang này xuất hiện trong danh sách lựa chọn của Layout Editor. Thuộc tính nào bắt buộc phải có trong thẻ `<apex:page>`?

**💬 Giải thích gốc (English):**
> To ensure the Visualforce page can be embedded in a page layout for the Account object, the developer must include the attribute standardController="Account" in the <apex:page> tag.

**✅ Tại sao đáp án đúng:**
> Bắt buộc phải khai báo thuộc tính `standardController="Account"` (A). Đây là điều kiện cần và đủ để Salesforce nhận diện trang Visualforce này sinh ra là dành riêng cho đối tượng Account, từ đó mới cho phép nhúng vào Page Layout của Account.

**❌ Tại sao đáp án sai:**
> **B.** `extensions` chỉ để gọi thêm class Apex bổ trợ logic, không giúp trang được hiển thị để nhúng layout.
> **C.** Sử dụng custom `controller="Account"` là sai cú pháp (Account là sObject chứ có phải custom class controller đâu) và custom controller đơn lẻ không hỗ trợ nhúng layout chuẩn.
> **D.** `action` dùng để tự động chạy hàm khi tải trang, không có tác dụng phân quyền hay nhúng layout.

**💡 Từ khóa ghi nhớ:** `Muốn nhúng trang Visualforce vào Page Layout của sObject nào -> Bắt buộc trang đó phải khai báo `standardController="Tên_sObject"`.`

---

## Câu 193

**🔵 Which two operations can be performed using a formula field? (Choose two.)**

- **A.** Displaying the last four digits of an encrypted Social Security number ❌
- **B.** Triggering a Process Builder ❌
- **C.** Displaying an Image based on the Opportunity Amount ✅
- **D.** Calculating a score on a Lead based on the information from another field ✅

**📝 Dịch tiếng Việt:**
> Hai thao tác nào sau đây có thể thực hiện ngon lành bằng trường công thức (Formula Field)? (Chọn 2)

**💬 Giải thích gốc (English):**
> Displaying an Image based on the Opportunity Amount: Formula fields can display different images based on certain criteria.
> Calculating a score on a Lead based on the information from another field: Formula fields can perform calculations using data from other fields.

**✅ Tại sao đáp án đúng:**
> C đúng vì ta hoàn toàn có thể dùng hàm `IMAGE()` trong Formula Field để hiển thị ảnh động/icon sinh động dựa trên số tiền của Opportunity. D đúng vì Formula Field cực mạnh trong việc lấy thông tin từ các trường khác trên cùng bản ghi (hoặc từ cha) để tự động tính toán ra điểm số cho Lead.

**❌ Tại sao đáp án sai:**
> **A.** Trường công thức cấm chỉ việc thò đuôi vào đọc dữ liệu của các trường đã được mã hóa bảo mật (Encrypted fields).
> **B.** Formula Field thay đổi giá trị tự động ở tầng database chứ không tạo ra sự kiện chỉnh sửa thực tế để có thể kích hoạt (trigger) Flow hay Process Builder chạy được.

**💡 Từ khóa ghi nhớ:** `Formula Field -> Chỉ đọc (Read-only), dùng được hàm `IMAGE()`, cấm sờ vào dữ liệu mã hóa (Encrypted data).`

---

## Câu 194

**🔵 Application Events follow the traditional publish-subscribe model. Which method is used to fire an event?**

- **A.** registerEvent() ❌
- **B.** fireEvent() ❌
- **C.** emit() ❌
- **D.** fire() ✅

**📝 Dịch tiếng Việt:**
> Trong mô hình Application Event của framework Aura Component, phương thức nào được sử dụng để chính thức kích hoạt và phát tán (fire) một event đi khắp nơi?

**💬 Giải thích gốc (English):**
> To fire an application event in Salesforce, you use the fire() method.

**✅ Tại sao đáp án đúng:**
> Cú pháp chuẩn cơm mẹ nấu của Aura Component: sau khi định nghĩa và lấy được thực thể (instance) của event, ta dùng phương thức `.fire()` (D) để 'bắn' event đó đi cho các component khác thu nhận.

**❌ Tại sao đáp án sai:**
> **A.** `registerEvent()` dùng để đăng ký event trong file XML cấu hình của component chứ không dùng để kích hoạt chạy.
> **B.** `fireEvent()` nghe thì rất thuyết phục nhưng thực tế là hàng fake tự chế, Salesforce không có phương thức này.
> **C.** `emit()` là cú pháp của các thư viện JavaScript khác như Node.js hoặc Vue, đem vào Salesforce là oẳng ngay.

**💡 Từ khóa ghi nhớ:** `Aura Event -> Kích hoạt bằng hàm `.fire()`.`

---

## Câu 195

**🔵 A developer needs to implement the functionality for a service agent to gather multiple pieces of information from a customer in order to send a replacement credit card. Which automation tool meets these requirements?**

- **A.** Lightning Component ❌
- **B.** Flow Builder ✅
- **C.** Process Builder ❌
- **D.** Approval Process ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên cần triển khai tính năng cho phép nhân viên chăm sóc khách hàng thu thập nhiều thông tin khác nhau từ khách hàng qua từng bước để gửi thẻ tín dụng thay thế. Công cụ tự động hóa nào đáp ứng hoàn hảo yêu cầu này?

**💬 Giải thích gốc (English):**
> To gather multiple pieces of information from a customer and send a replacement credit card, the best automation tool to use is Flow Builder. Flow Builder allows you to create guided, interactive processes for users, making it ideal for collecting information through a series of steps.

**✅ Tại sao đáp án đúng:**
> Chọn Flow Builder (B) để dựng một Screen Flow. Đây là công cụ khai báo no-code mạnh mẽ nhất của Salesforce được thiết kế riêng để tạo ra các màn hình tương tác động, thu thập dữ liệu nhiều bước từ người dùng một cách trực quan và lưu trữ cực kỳ mượt mà.

**❌ Tại sao đáp án sai:**
> **A.** Dùng Lightning Component tự viết code (Aura/LWC) cũng làm được nhưng cực kỳ tốn công gõ code, tốn tài nguyên bảo trì so với giải pháp no-code Screen Flow có sẵn.
> **C.** Process Builder chạy ngầm ở backend, hoàn toàn không có khả năng hiển thị giao diện hay form nhập liệu tương tác với con người.
> **D.** Approval Process dùng để phê duyệt các yêu cầu, không có tính năng thu thập thông tin khách hàng qua màn hình.

**💡 Từ khóa ghi nhớ:** `Thu thập dữ liệu từ người dùng qua form / Nhiều màn hình nhập liệu -> Chọn ngay SCREEN FLOW (Flow Builder).`

---

## Câu 196

**🔵 Einstein Next Best Action is configured at Universal Containers to display recommendations to internal users on the Account detail page. If the recommendation is approved, a new opportunity record and task should be generated. If the recommendation is rejected, an Apex method must be executed to perform a callout to an external system. Which three factors should a developer keep in mind when implementing the Apex method? (Choose three.)**

- **A.** The method must use the @AuraEnabled annotation. ❌
- **B.** The method must use the @InvokableMethod annotation. ✅
- **C.** The method must be defined as static. ✅
- **D.** The method must be defined as public. ✅
- **E.** The method must use the @Future annotation ❌

**📝 Dịch tiếng Việt:**
> Einstein Next Best Action gợi ý cho user. Nếu gợi ý bị từ chối (rejected), một phương thức Apex phải được kích hoạt để thực hiện callout gửi dữ liệu ra hệ thống ngoài. Ba yếu tố nào lập trình viên cần lưu ý khi viết phương thức Apex này? (Chọn 3)

**💬 Giải thích gốc (English):**
> The method must use the @InvokableMethod annotation: This annotation allows the method to be called from a flow or process.
> The method must be defined as static : Static methods can be invoked without needing an instance of the class1.
> The method must be defined as public : Public methods are accessible from outside the class.
> Here’s an example code snippet for reference:
> public class NBAHandler {
> @InvokableMethod
> public static void handleRejectedRecommendation(List<Id> recordIds) {
> // Perform some logic here
> callExternalSystem(recordIds);
> }
> @Future(callout=true)
> public static void callExternalSystem(List<Id> recordIds) {
> // Perform callout to external system
> HttpRequest req = new HttpRequest();
> req.setEndpoint('https://external-system.example.com/api');
> req.setMethod('POST');
> req.setHeader('Content-Type', 'application/json');
> req.setBody(JSON.serialize(recordIds));
> Http http = new Http();
> HttpResponse res = http.send(req);
> if (res.getStatusCode() != 200) {
> // Handle error
> }
> }
> }

**✅ Tại sao đáp án đúng:**
> Vì phương thức này được kích hoạt từ Flow/Next Best Action, nó bắt buộc phải tuân thủ cấu trúc của một Invocable Action: B đúng vì phương thức phải được gắn annotation `@InvokableMethod`. C đúng vì phương thức bắt buộc phải là `static`. D đúng vì phương thức phải được khai báo tầm vực là `public` hoặc `global` để hệ thống bên ngoài gọi được.

**❌ Tại sao đáp án sai:**
> **A.** `@AuraEnabled` chỉ dùng để mở hàm cho các component Aura hoặc LWC gọi từ giao diện, không phải là điều kiện để Flow gọi.
> **E.** `@Future` dùng để chạy bất đồng bộ chung, phương thức invokable có thể gọi hàm future bên trong chứ bản thân signature của nó cấm gắn thẻ `@Future` trực tiếp.

**💡 Từ khóa ghi nhớ:** `Phương thức gọi từ Flow (Invocable) -> Bắt cặp ngay: `@InvokableMethod` + `public static void`.`

---

## Câu 197

**🔵 An Opportunity needs to have an amount rolled up from a custom object that is not in a master-detail relationship. How can this be achieved?**

- **A.** Use the Metadata API to create real-time roll-up summaries. ❌
- **B.** Use the Streaming API to create real-time roll-up summaries. ❌
- **C.** Write a trigger on the Opportunity object and use tree sorting to sum the amount for all related child objects under the Opportunity. ❌
- **D.** Write a trigger on the child object and use an aggregate function to sum the amount for all related child objects under the Opportunity. ✅

**📝 Dịch tiếng Việt:**
> Làm thế nào để tính tổng số tiền (Roll-up) từ một đối tượng tùy chỉnh lên Opportunity, trong khi hai đối tượng này chỉ liên kết với nhau bằng quan hệ Lookup chứ không phải Master-Detail?

**💬 Giải thích gốc (English):**
> The correct approach to roll up an amount from a custom object that is not in a master-detail relationship is: Write a trigger on the child object and use an aggregate function to sum the amount for all related child objects under the Opportunity. This trigger will ensure that whenever a child object is inserted, updated, deleted, or undeleted, the corresponding Opportunity’s amount is updated accordingly.

**✅ Tại sao đáp án đúng:**
> Vì mối quan hệ Lookup không hỗ trợ tính năng Roll-up Summary có sẵn, nên lập trình viên phải tự thân vận động: Viết một Apex Trigger trên đối tượng con (D). Mỗi khi đối tượng con được thêm/sửa/xóa, trigger sẽ kích hoạt câu truy vấn SOQL sử dụng hàm gom nhóm (`SUM()`, `AggregateResult`) để tính tổng số tiền của toàn bộ các con liên quan, rồi cập nhật ngược lại trường số tiền trên Opportunity cha.

**❌ Tại sao đáp án sai:**
> **A.** Metadata API sinh ra để quản lý file cấu hình hệ thống, hoàn toàn bất lực trong việc tự tính tổng và ghi đè dữ liệu bản ghi.
> **B.** Streaming API chỉ dùng để gửi thông báo sự kiện thay đổi dữ liệu thời gian thực ra bên ngoài chứ không update được data.
> **C.** Viết trigger trên Opportunity cha là đi vào lòng đất, vì khi bản ghi con bị thay đổi hay tạo mới, trigger trên cha không hề kích hoạt để cập nhật dữ liệu.

**💡 Từ khóa ghi nhớ:** `Tính tổng con lên cha ở quan hệ Lookup -> Bắt buộc viết Trigger trên đối tượng CON + dùng câu truy vấn Aggregate SUM.`

---

## Câu 198

**🔵 A developer at Universal Containers is tasked with implementing a new Salesforce application that must be able to be maintained completely by their company's Salesforce administrator. Which three options should be considered for building out the business logic layer of the application? (Choose three.)**

- **A.** Process Builder ✅
- **B.** Scheduled Jobs ❌
- **C.** Invocable Actions ✅
- **D.** Workflows ❌
- **E.** Validation Rules ✅

**📝 Dịch tiếng Việt:**
> Universal Containers muốn phát triển một ứng dụng mới nhưng yêu cầu toàn bộ logic nghiệp vụ (Business Logic Layer) sau này phải được bảo trì hoàn toàn no-code bởi Quản trị viên (Admin). Ba công cụ nào nên được cân nhắc sử dụng? (Chọn 3)

**✅ Tại sao đáp án đúng:**
> Để Admin có thể bảo trì dễ dàng không cần biết viết code, ta dùng các công cụ khai báo: A đúng vì Process Builder (hoặc Flow Builder hiện đại) là trùm tự động hóa quy trình no-code. E đúng vì Validation Rules giúp chặn và bắt buộc nhập liệu chuẩn xác hoàn toàn bằng giao diện kéo thả cấu hình. C đúng vì Invocable Actions cho phép Admin gọi các đoạn code Apex đã được dev đóng gói sẵn như những khối gạch lắp ghép.

**❌ Tại sao đáp án sai:**
> **B.** Scheduled Jobs yêu cầu phải viết code Apex implements interface `Schedulable`, Admin bình thường nhìn vào là 'khóc tiếng Mán' ngay chứ bảo trì sao nổi.
> **D.** Workflows tuy là no-code nhưng tính năng cực kỳ nghèo nàn và đã bị Salesforce khai tử (deprecated), cấm dùng cho các ứng dụng mới.

**💡 Từ khóa ghi nhớ:** `Logic no-code thân thiện với Admin -> Chọn ngay: Flow/Process Builder, Invocable Actions, Validation Rules.`

---

## Câu 199

**🔵 Universal Containers (UC) uses a custom object called Vendor. The Vendor custom object has a Master-Detail relationship with the standard Account object. Based on some internal discussions, the UC administrator tried to change the Master-Detail relationship to a Lookup relationship but was not able to do so. What is a possible reason that this change was not permitted?**

- **A.** The Vendor records have existing values in the Account object. ❌
- **B.** The Account object is included on a workflow on the Vendor object. ❌
- **C.** The Account records contain Vendor roll-up summary fields. ✅
- **D.** The Vendor object must use a Master-Detail field for reporting. ❌

**📝 Dịch tiếng Việt:**
> Đối tượng custom Vendor đang có quan hệ Master-Detail với đối tượng tiêu chuẩn Account. Admin cố gắng đổi trường quan hệ này thành Lookup nhưng hệ thống thẳng thừng từ chối. Nguyên nhân khả thi nhất là gì?

**💬 Giải thích gốc (English):**
> You cannot change a Master-Detail relationship to a Lookup relationship if there are roll-up summary fields on the parent object that summarize data from the child object. These roll-up summary fields must be deleted before the relationship type can be changed.

**✅ Tại sao đáp án đúng:**
> Vì trên đối tượng cha Account đang tồn tại ít nhất một trường Roll-up Summary (C) tính toán dữ liệu của các Vendor con. Trong Salesforce, trường Roll-up chỉ hoạt động được trên mối quan hệ Master-Detail. Do đó, hệ thống sẽ khóa cứng không cho phép chuyển đổi sang Lookup trừ khi mày phải xóa sạch đống trường Roll-up Summary kia trước.

**❌ Tại sao đáp án sai:**
> **A.** Việc các bản ghi Vendor có chứa giá trị Account hoàn toàn không ảnh hưởng đến việc chuyển từ Master-Detail sang Lookup (nó chỉ chặn ở chiều ngược lại từ Lookup sang Master-Detail nếu có bản ghi con bị bỏ trống cha).
> **B.** Workflow Rule không bao giờ can thiệp hay chặn việc chuyển đổi kiểu dữ liệu của trường quan hệ.
> **D.** Không có luật nào bắt buộc Vendor phải dùng Master-Detail chỉ để phục vụ mục đích làm báo cáo (Report) cả.

**💡 Từ khóa ghi nhớ:** `Đổi Master-Detail sang Lookup -> Bắt buộc phải XÓA hết các trường Roll-up Summary trên đối tượng cha trước!`

---

## Câu 200

**🔵 When is an Apex Trigger required instead of a Process Builder Process?**

- **A.** When a record needs to be created ❌
- **B.** When multiple records related to the triggering record need to be updated ❌
- **C.** When a post to Chatter needs to be created ❌
- **D.** When an action needs to be taken on a delete or undelete, or before a DML operation is executed. ✅

**📝 Dịch tiếng Việt:**
> Trong trường hợp nào lập trình viên bắt buộc phải sử dụng Apex Trigger thay vì sử dụng một Process Builder Process?

**💬 Giải thích gốc (English):**
> Process Builder cannot handle delete or undelete events, nor can it execute actions before a DML operation. Triggers are necessary for these scenarios as they provide more granular control over the timing and conditions of the actions.

**✅ Tại sao đáp án đúng:**
> Chọn D. Các công cụ no-code đời cũ như Process Builder (và kể cả Flow đời cũ) hoàn toàn mù tịt trước các sự kiện dữ liệu bị XÓA (delete), KHÔI PHỤC (undelete), hoặc khi cần xử lý dữ liệu cực nhanh ở giai đoạn trước khi lưu xuống database (BEFORE DML). Những ca khó này bắt buộc phải dùng Apex Trigger để giải quyết.

**❌ Tại sao đáp án sai:**
> **A.** Tạo bản ghi mới là tác vụ cơ bản mà Process Builder xử lý cực nhanh no-code.
> **B.** Cập nhật hàng loạt bản ghi con liên quan hoàn toàn thực hiện được no-code bằng Process Builder.
> **C.** Đăng bài viết lên Chatter (Post to Chatter) là hành động tích hợp sẵn cực kỳ trực quan của Process Builder.

**💡 Từ khóa ghi nhớ:** `Bắt buộc dùng Trigger khi -> Cần can thiệp sự kiện Delete, Undelete hoặc BEFORE DML.`

---

## Câu 201

**🔵 A company wants to create an employee rating program that allows employees to rate each other. An employee's average rating must be displayed on the employee record. Employees must be able to create rating records, but are not allowed to create employee records. Which two actions should a developer take to accomplish this task? (Choose two.)**

- **A.** Create a trigger on the Rating object that updates a fields on the Employee object. ✅
- **B.** Create a lookup relationship between the Rating and Employee object. ✅
- **C.** Create a roll-up summary field on the Employee and use AVG to calculate the average rating score. ❌
- **D.** Create a master-detail relationship between the Rating and Employee objects. ❌

**📝 Dịch tiếng Việt:**
> Một công ty muốn tạo chương trình đánh giá nhân viên (Rating) cho phép nhân viên tự đánh giá lẫn nhau. Điểm đánh giá trung bình (average rating) phải được hiển thị trực tiếp trên Employee record. Nhân viên được phép tạo bản ghi Rating nhưng tuyệt đối cấm tạo bản ghi Employee. Hai hành động nào lập trình viên nên thực hiện? (Chọn 2)

**💬 Giải thích gốc (English):**
> Roll-Up summary doesn't have AVG.

**✅ Tại sao đáp án đúng:**
> B đúng vì ta phải tạo mối quan hệ Lookup giữa Rating và Employee để giữ cho việc phân quyền của hai đối tượng này độc lập nhau (nhân viên có quyền tạo Rating con nhưng vẫn bị chặn tạo Employee cha). A đúng vì do dùng Lookup, ta không thể dùng trường Roll-up Summary có sẵn để tính trung bình được (hơn nữa Roll-up cũng cấm dùng hàm AVG), nên bắt buộc phải viết một Apex Trigger trên đối tượng Rating để tự động tính toán điểm trung bình cộng rồi update ngược lên Employee.

**❌ Tại sao đáp án sai:**
> **C.** Trường Roll-up Summary tiêu chuẩn của Salesforce chỉ hỗ trợ các hàm SUM, COUNT, MIN, MAX chứ hoàn toàn KHÔNG hỗ trợ hàm tính trung bình AVG!
> **D.** Mối quan hệ Master-Detail sẽ kế thừa bảo mật nghiêm ngặt từ cha Employee, gây khó khăn cho quyền tạo bản ghi của nhân viên.

**💡 Từ khóa ghi nhớ:** `Trường Roll-up Summary của Salesforce không hỗ trợ tính trung bình (AVG). Muốn tính trung bình từ con lên cha -> Dùng Lookup + Apex Trigger!`

---

## Câu 202

**🔵 What is a benefit of developing applications in a multi-tenant environment?**

- **A.** Access to predefined computing resources ❌
- **B.** Enforced best practices for development ✅
- **C.** Unlimited processing power and memory ❌
- **D.** Default out-of-the-box configuration ❌

**📝 Dịch tiếng Việt:**
> Lợi ích lớn nhất của việc phát triển ứng dụng trong môi trường đa thuê bao (multi-tenant) của Salesforce là gì?

**✅ Tại sao đáp án đúng:**
> Trong môi trường đa thuê bao, mọi người dùng chung tài nguyên phần cứng. Để đảm bảo không có ai viết code ẩu làm sập cả hệ thống, Salesforce ép buộc các giới hạn Governor Limits cực kỳ nghiêm ngặt. Điều này vô hình trung ép lập trình viên bắt buộc phải tuân thủ các best practices (B) (như viết code bulkify, tối ưu SOQL/DML) giúp ứng dụng luôn chạy nhanh và an toàn.

**❌ Tại sao đáp án sai:**
> **A.** Truy cập tài nguyên định sẵn chỉ là đặc tính hạ tầng chung, chả phải lợi ích vượt trội giúp nâng cao chất lượng code.
> **C.** Mơ đi cưng! Đã là multi-tenant thì tài nguyên được chia sẻ và giới hạn nghiêm ngặt chứ làm gì có chuyện 'vô hạn sức mạnh xử lý và bộ nhớ' (unlimited).
> **D.** Cấu hình mặc định có sẵn thì ở môi trường đơn thuê bao (single-tenant) vẫn có, chả liên quan gì đến multi-tenancy.

**💡 Từ khóa ghi nhớ:** `Multi-tenant = Dùng chung tài nguyên -> Phải có giới hạn (Limits) -> Ép dev tuân thủ Best Practices.`

---

## Câu 203

**🔵 When viewing a Quote, the sales representative wants to easily see how many discounted items are included in the Quote Line Items. What should a developer do to meet this requirement?**

- **A.** Create a trigger on the Quote object that queries the Quantity field on discounted Quote Line Items. ❌
- **B.** Create a Workflow Rule on the Quote Line Item object that updates a field on the parent Quote when the item is discounted. ❌
- **C.** Create a roll-up summary field on the Quote object that performs a SUM on the quote Line Item Quantity field, filtered for only discounted Quote Line Items. ✅
- **D.** Create a formula field on the Quote object that performs a SUM on the Quote Line Item Quantity field, filtered for only discounted Quote Line Items. ❌

**📝 Dịch tiếng Việt:**
> Khi xem Quote, nhân viên bán hàng muốn biết dễ dàng có bao nhiêu mặt hàng được chiết khấu (discounted) nằm trong danh sách Quote Line Items. Lập trình viên nên làm gì để đáp ứng yêu cầu này một cách tối ưu nhất?

**💬 Giải thích gốc (English):**
> To meet the requirement of showing how many discounted items are included in the Quote Line Items, the best approach is to use a roll-up summary field. This field can perform a SUM on the Quote Line Item Quantity field, filtered specifically for discounted items.

**✅ Tại sao đáp án đúng:**
> Tạo một trường Roll-up Summary trên đối tượng Quote để tính tổng (SUM) trường Quantity của Quote Line Item, đồng thời thiết lập bộ lọc filter criteria chỉ tính những dòng Quote Line Item nào có chiết khấu (C). Đây là giải pháp no-code chính chủ, cực nhanh và chuẩn cơm mẹ nấu.

**❌ Tại sao đáp án sai:**
> **A.** Viết trigger Apex là giải pháp code cồng kềnh, tốn công bảo trì vô ích cho một tác vụ hoàn toàn có thể cấu hình no-code trong 30 giây.
> **B.** Workflow Rule cựu trào không có khả năng tính toán gom nhóm dữ liệu của nhiều con để update ngược lên cha mượt mà như Roll-up.
> **D.** Trường công thức (Formula Field) chỉ có thể tính toán trên chính bản ghi đó hoặc đi từ cha xuống con, cấm tiệt việc làm hàm tổng hợp (SUM) đi ngược từ danh sách con lên cha.

**💡 Từ khóa ghi nhớ:** `Tính tổng/Đếm số lượng bản ghi con có điều kiện lên cha ở quan hệ Master-Detail -> Luôn dùng Roll-up Summary Field kết hợp với Filter Criteria!`

---

## Câu 204

**🔵 In terms of the MVC paradigm, what are two advantages of implementing the view layer of a Salesforce application using Lightning Web Component-based development over Visualforce? (Choose two.)**

- **A.** Self-contained and reusable units of an application ✅
- **B.** Rich component ecosystem ✅
- **C.** Server-side run-time debugging ❌
- **D.** Automatic code generation ❌

**📝 Dịch tiếng Việt:**
> Xét theo mô hình MVC, hai ưu thế vượt trội của việc xây dựng tầng View bằng Lightning Web Components (LWC) so với Visualforce truyền thống là gì? (Chọn 2)

**💬 Giải thích gốc (English):**
> Self-contained and reusable units of an application: LWCs are designed as modular components that can be reused across different parts of the application, promoting better code organization and maintainability.
> Rich component ecosystem: LWC benefits from a modern, rich ecosystem of components that can be easily integrated and customized, enhancing the development experience and enabling the creation of more dynamic and responsive user interfaces.

**✅ Tại sao đáp án đúng:**
> A đúng vì LWC được thiết kế theo kiến trúc component độc lập, cho phép đóng gói toàn bộ HTML/JS/CSS thành một khối có khả năng tái sử dụng (reusable units) cực kỳ linh hoạt ở nhiều nơi. B đúng vì LWC thừa hưởng và đóng góp vào một hệ sinh thái linh kiện phong phú, hiện đại giúp tạo ra trải nghiệm người dùng mượt mà, dynamic hơn hẳn Visualforce cổ lỗ sĩ.

**❌ Tại sao đáp án sai:**
> **C.** LWC là Client-side framework chạy trực tiếp trên trình duyệt JavaScript của người dùng, việc debug chạy chủ yếu ở Client chứ không phải Server-side.
> **D.** LWC không có phép thuật nào tự động sinh mã nguồn (automatic code generation) cho dev lười cả.

**💡 Từ khóa ghi nhớ:** `LWC ăn đứt Visualforce nhờ -> Độc lập, khả năng tái sử dụng siêu cao + Hệ sinh thái component động hiện đại.`

---

## Câu 205

**🔵 Cloud Kicks Fitness, an ISV Salesforce partner, is developing a managed package application. One of the application modules allows the user to calculate body fat using the Apex class, BodyFat, and its method, calculateBodyFat(). The product owner wants to ensure this method is accessible by the consumer of the application when developing customizations outside the ISV's package namespace. Which approach should a developer take to ensure calculateBodyFat() is accessible outside the package namespace?**

- **A.** Declare the class and method using the public access modifier. ❌
- **B.** Declare the class as global and use the public access modifier on the method. ❌
- **C.** Declare the class as public and use the global access modifier on the method. ❌
- **D.** Declare the class and method using the global access modifier. ✅

**📝 Dịch tiếng Việt:**
> Cloud Kicks Fitness phát triển một managed package. Một module của ứng dụng cho phép khách hàng gọi phương thức `calculateBodyFat()` của class `BodyFat` để tự tùy biến code ngoài namespace của package. Lập trình viên nên khai báo class và method này với từ khóa truy cập nào?

**💬 Giải thích gốc (English):**
> To ensure that the calculateBodyFat() method is accessible outside the package namespace, the developer should use the global access modifier. This is because the global access modifier allows the class and its methods to be accessible across different namespaces, which is essential for managed packages.

**✅ Tại sao đáp án đúng:**
> Khai báo cả class và phương thức sử dụng từ khóa truy cập `global` (D). Đây là quy định bắt buộc trong phát triển Managed Package: chỉ những thành phần nào được gắn nhãn `global` mới có thể vượt biên giới namespace để cho phép code của khách hàng bên ngoài gọi được.

**❌ Tại sao đáp án sai:**
> **A.** public chỉ cho phép các class khác trong cùng một namespace của package truy cập, khách hàng ở ngoài cấm gọi.
> **B.** Phương thức khai báo public sẽ bị chặn truy cập từ ngoài namespace bất kể class cha có là global.
> **C.** Class khai báo public sẽ khóa cứng toàn bộ các thành phần bên trong nó đối với bên ngoài bất chấp method khai báo global.

**💡 Từ khóa ghi nhớ:** `Viết Managed Package muốn phơi code cho khách hàng ngoài namespace gọi -> Bắt buộc dùng từ khóa GLOBAL!`

---

## Câu 206

**🔵 A software company uses the following objects and relationships:
Case: to handle customer support issues
Defect__c: a custom object to represent known issues with the company's software
Case_Defect__c: a junction object between Case and Defect__c to represent that a defect is a cause of a customer issue Case and Defect__c have Private organization-wide defaults.
What should be done to share a specific Case_Defect__c: record with a user?**

- **A.** Share the parent Defect__c record. ❌
- **B.** Share the parent Case and Defect__c records. ✅
- **C.** Share the Case_Defect__c record. ❌
- **D.** Share the parent Case record. ❌

**📝 Dịch tiếng Việt:**
> Một phần mềm sử dụng các đối tượng và mối quan hệ sau: Case (Private OWD), Defect__c (Private OWD, custom object), và Case_Defect__c (junction object Nhiều-Nhiều giữa Case và Defect__c). Làm thế nào để chia sẻ thành công quyền truy cập một bản ghi liên kết `Case_Defect__c` cụ thể cho một người dùng khác?

**💬 Giải thích gốc (English):**
> A junction object Case_Defect__c typically has two master-detail relationships, one to Case and another to Defect__c. This means that the sharing settings for Case_Defect__c are inherited from its parent records.
> To share a specific Case_Defect__c record with a user, you would indeed need to ensure that the user has access to both the Case and Defect__c records. This is because the visibility of the junction object record is controlled by the sharing settings of its parent objects.

**✅ Tại sao đáp án đúng:**
> Vì `Case_Defect__c` là một đối tượng trung gian (Junction Object) liên kết bằng hai mối quan hệ Master-Detail với Case và Defect__c. Quyền bảo mật của bản ghi con Detail bị xích chặt 100% vào cả hai cha. Do đó, để xem được con, người dùng bắt buộc phải có quyền truy cập (xem) đối với CẢ HAI bản ghi cha là Case và Defect__c (B).

**❌ Tại sao đáp án sai:**
> **A.** Chỉ chia sẻ một bên cha Defect__c là chưa đủ điều kiện, người dùng vẫn bị hệ thống chặn xem bản ghi junction con.
> **C.** Bản ghi con trong mối quan hệ Master-Detail không sở hữu trường Owner riêng và không có nút Share thủ công, nên không thể chia sẻ trực tiếp trên chính nó được.
> **D.** Chỉ chia sẻ một bên cha Case tương tự câu A, vẫn thiếu quyền xem cha bên kia.

**💡 Từ khóa ghi nhớ:** `Muốn xem bản ghi Junction (Many-to-Many) -> Người dùng bắt buộc phải có quyền xem trên CẢ HAI bản ghi cha Master!`

---

## Câu 207

**🔵 What is the debug output of the following Apex code?
Decimal theValue;
System.debug(theValue);**

- **A.** 0.0 ❌
- **B.** null ✅
- **C.** Undefined ❌
- **D.** 0 ❌

**📝 Dịch tiếng Việt:**
> Kết quả hiển thị trong debug log của đoạn mã Apex sau là gì? `Decimal theValue; System.debug(theValue);`

**💬 Giải thích gốc (English):**
> In Apex, when a Decimal variable is declared but not initialized, its default value is 'null'.

**✅ Tại sao đáp án đúng:**
> Kết quả debug in ra chắc chắn là `null` (B). Trong Apex, mọi biến số (Decimal, Integer, Double...) hay sObject khi mới chỉ khai báo mà không khởi tạo giá trị cụ thể sẽ luôn được gán giá trị mặc định là `null` để bảo vệ an toàn cho bộ nhớ.

**❌ Tại sao đáp án sai:**
> **A.** 0.0 không phải là giá trị mặc định của kiểu Decimal trong Apex.
> **C.** Không tồn tại khái niệm giá trị 'Undefined' giống JavaScript trong ngôn ngữ lập trình Apex.
> **D.** 0 là giá trị mặc định của kiểu số nguyên trong một số ngôn ngữ khác nhưng với Apex vẫn là null.

**💡 Từ khóa ghi nhớ:** `Mẹo Apex: Biến khai báo khơi khơi không gán trị -> Mặc định luôn là NULL!`

---

## Câu 208

**🔵 Candidates are reviewed by four separate reviewers and their comments and scores which range from 1 (lowest) to 5 (highest) are stored on a review record that is a detail record for a candidate. What is the best way to indicate that a combined review score of 15 or better is required to recommend that the candidate come in for an interview?**

- **A.** Use a Validation Rule on a total score field on the candidate record that prevents a recommended field from being true if the total score is less than 15. ❌
- **B.** Use a Rollup Summary field to calculate the sum of the review scores, and store this in a total score field on the candidate. ✅
- **C.** Use Visual Workflow to set a recommended field on the candidate whenever the cumulative review score is 15 or better. ❌
- **D.** Use a Workflow Rule to calculate the sum of the review scores and send an email to the hiring manager when the total is 15 or better. ❌

**📝 Dịch tiếng Việt:**
> Điểm đánh giá ứng viên từ 1 (thấp nhất) đến 5 (cao nhất) được lưu trên bản ghi Review (là bản ghi con Detail của đối tượng Candidate). Cách tối ưu nhất để tự động tính tổng điểm và hiển thị cảnh báo nếu tổng điểm đạt từ 15 trở lên là gì?

**💬 Giải thích gốc (English):**
> Rollup Summary Field: This field type allows you to perform calculations on related records, such as summing up the review scores. By creating a rollup summary field on the candidate record, you can automatically calculate the total score from the related review records.

**✅ Tại sao đáp án đúng:**
> Tạo một trường Roll-up Summary trên đối tượng cha Candidate để tự động tính tổng (SUM) điểm số từ các bản ghi Review con liên quan (B). Đây là giải pháp hoàn toàn no-code cực kỳ sạch sẽ, đáng tin cậy và tối ưu hiệu năng hệ thống tuyệt đối.

**❌ Tại sao đáp án sai:**
> **A.** Validation Rule chỉ dùng để chặn đứng không cho lưu dữ liệu sai logic chứ làm sao tự động tính toán tổng điểm từ danh sách con lên cha được.
> **C.** Sử dụng Screen Flow hay Autolaunched Flow để tính toán là phương án vẽ đường vòng cồng kềnh, tốn công phát triển vô ích trong khi có thể cấu hình no-code trong 30 giây bằng Roll-up.
> **D.** Workflow Rule đời cổ lỗ sĩ không hỗ trợ tính năng tính tổng (SUM) các bản ghi con ngược lên cha.

**💡 Từ khóa ghi nhớ:** `Tính tổng/đếm số lượng bản ghi con Detail lên cha Master -> Tạo trường ROLL-UP SUMMARY kiểu SUM/COUNT.`

---

## Câu 209

**🔵 A developer needs an Apex method that can process Account or Contact records. Which method signature should the developer use?**

- **A.** public void doWork(Account | | Contact) ❌
- **B.** public void doWork(Record theRecord) ❌
- **C.** public void doWork(Account Contact) ❌
- **D.** public void doWork(sObject theRecord) ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên cần viết một phương thức Apex đa năng có khả năng xử lý được cả bản ghi Account hoặc Contact. Cú pháp khai báo tham số (method signature) nào là chuẩnax nhất?

**💬 Giải thích gốc (English):**
> In Apex, sObject is the generic base class for all objects in Salesforce. This allows the method to accept any standard or custom object, including Account and Contact.

**✅ Tại sao đáp án đúng:**
> Sử dụng kiểu dữ liệu `sObject` làm tham số đầu vào: `public void doWork(sObject theRecord)` (D). Vì `sObject` chính là lớp cha chung (Generic parent class) của tất cả các đối tượng trong Salesforce (bao gồm cả Account, Contact, hay bất kỳ custom object nào), giúp phương thức cực kỳ đa năng và chấp nhận mọi đối tượng truyền vào.

**❌ Tại sao đáp án sai:**
> **A.** Cú pháp dùng toán tử logic OR `Account || Contact` trong khai báo tham số là do lập trình viên tự tưởng tượng ra chứ Apex không biên dịch được.
> **B.** Apex không hề tồn tại kiểu dữ liệu chung nào tên là `Record` cả.
> **C.** Khởi tạo tham số kiểu ghép tên hai class `Account Contact` sát nhau là hoàn toàn sai cú pháp lập trình cơ bản.

**💡 Từ khóa ghi nhớ:** `Muốn phương thức Apex đa năng nhận được mọi loại đối tượng -> Khai báo kiểu tham số là `sObject`.`

---

## Câu 210

**🔵 Which Salesforce org has a complete duplicate copy of the production org including data and configuration?**

- **A.** Developer Pro Sandbox ❌
- **B.** Partial Copy Sandbox ❌
- **C.** Production ❌
- **D.** Full Sandbox ✅

**📝 Dịch tiếng Việt:**
> Loại Sandbox nào trong Salesforce là bản sao y xì đúc của Production Org, bao gồm cả toàn bộ dữ liệu (data) lẫn cấu hình (configuration)?

**💬 Giải thích gốc (English):**
> Sandbox Types
> Developer Sandbox – A Developer sandbox is intended for development and testing in an isolated environment. A Developer Sandbox includes a copy of your production org’s configuration (metadata).
> Developer Pro Sandbox – A Developer Pro sandbox is intended for development and testing in an isolated environment and can host larger data sets than a Developer sandbox. A Developer Pro sandbox includes a copy of your production org’s configuration (metadata). Use a Developer Pro sandbox to handle more development and quality assurance tasks and for integration testing or user training.
> Partial Copy Sandbox – A Partial Copy sandbox is intended to be used as a testing environment. This environment includes a copy of your production org’s configuration (metadata) and a sample of your production org’s data as defined by a sandbox template. Use a Partial Copy sandbox for quality assurance tasks such as user acceptance testing, integration testing, and training.
> Full Sandbox – A Full sandbox is intended to be used as a testing environment. Only Full sandboxes support performance testing, load testing, and staging. Full sandboxes are a replica of your production org, including all data, such as object records and attachments, and metadata. The length of the refresh interval makes it difficult to use Full sandboxes for development.
> We recommend that you apply a sandbox template so that your sandbox contains only the records that you need for testing or other tasks.

**✅ Tại sao đáp án đúng:**
> Full Sandbox (D) chính là 'trùm cuối' của hệ thống Sandbox. Nó sao chép 100% cấu hình (Metadata) và 100% dữ liệu bản ghi (Records) từ môi trường Production thật, chuyên dùng cho các tác vụ kiểm thử hiệu năng (Performance Test) hoặc chạy thử nghiệm chấp nhận người dùng (UAT) trước khi Go-live.

**❌ Tại sao đáp án sai:**
> **A.** Developer Pro Sandbox chỉ copy cấu hình (Metadata) chứ không hề có dữ liệu bản ghi thực tế nào được nhân bản kèm theo.
> **B.** Partial Copy Sandbox chỉ copy cấu hình và một phần nhỏ dữ liệu mẫu theo template giới hạn (tối đa 5GB dữ liệu), chứ không bê nguyên 100% data sang.
> **C.** Production là môi trường chạy thật của doanh nghiệp, chứ có phải môi trường Sandbox bản sao đâu nha.

**💡 Từ khóa ghi nhớ:** `Nhân bản 100% cấu hình + 100% dữ liệu thật -> Chỉ có thể là FULL SANDBOX.`

---

## Câu 211

**🔵 Universal Containers stores Orders and Line Items in Salesforce. For security reasons, financial representatives are allowed to see information on the Order such as order amount, but they are not allowed to see the Line Items on the Order. Which type of relationship should be used?**

- **A.** Direct Lookup ❌
- **B.** Indirect Lookup ❌
- **C.** Master-Detail ❌
- **D.** Lookup ✅

**📝 Dịch tiếng Việt:**
> Universal Containers lưu trữ Orders (Đơn hàng) và Line Items (Sản phẩm trong đơn hàng) trên Salesforce. Vì lý do bảo mật, mấy khứa đại diện tài chính (financial representatives) được phép xem thông tin trên Order (ví dụ như tổng tiền order), nhưng KHÔNG được phép nhìn thấy mấy cái Line Items con trong Order đó. Loại quan hệ (Relationship) nào nên được sử dụng ở đây?

**💬 Giải thích gốc (English):**
> Using a Lookup relationship allows you to control access to the related records independently. This means financial representatives can see the Order information without having access to the Line Items.

**✅ Tại sao đáp án đúng:**
> Chọn **Lookup Relationship** (D). Vì thằng này cho phép bảo mật độc lập! Bố mẹ và con cái sống riêng, ai có quyền xem cái gì thì tự cấu hình. Xem được Order cha không đồng nghĩa với việc được phép dòm ngó Line Items con.

**❌ Tại sao đáp án sai:**
> **A.** **Direct Lookup** chỉ là cái tên tự chế hoặc dùng cho External Object để link với Standard/Custom Object thông qua trường Salesforce ID. Không liên quan gì đến yêu cầu bảo mật ở đây.
> **B.** **Indirect Lookup** cũng dành riêng cho External Object để link với cha thông qua Custom Unique External ID. Đi quá xa thực tế rồi bro!
> **C.** **Master-Detail** là một mối quan hệ 'sống chết có nhau'. Detail record (con) sẽ kế thừa 100% quyền bảo mật từ Master record (cha). Cho xem cha là auto xem được con luôn, thế thì ăn cám rồi, lộ hết Line Items.

**💡 Từ khóa ghi nhớ:** `Muốn bảo mật độc lập (Thấy Cha chưa chắc thấy Con) -> Chọn **Lookup**. Sống chết có nhau, chung nhà chung ngõ -> **Master-Detail**.`

---

## Câu 212

**🔵 Which two events need to happen when deploying to a production org? (Choose two.)**

- **A.** All Process Builder Processes must have at least 1% test coverage. ❌
- **B.** All Apex code must have at least 75% test coverage. ✅
- **C.** All triggers must have at least 1% test coverage. ✅
- **D.** All Visual Flows must have at least 1% test coverage. ❌

**📝 Dịch tiếng Việt:**
> Hai điều kiện nào bắt buộc phải được đáp ứng khi deploy code lên một Production Org? (Chọn 2)

**💬 Giải thích gốc (English):**
> You must have at least 75% of your Apex covered by unit tests to deploy your code to production environments.
> Ensure all tests pass and at least 1% of coverage is applied to all triggers

**✅ Tại sao đáp án đúng:**
> Chọn **B** và **C**. Đây là luật thép của Salesforce khi lên Production: Tổng thể toàn bộ code Apex trong Org phải đạt tối thiểu **75% test coverage** (B), và riêng từng Trigger một phải có coverage lớn hơn 0% (tức là ít nhất **1% coverage** để chắc chắn trigger đó có được chạy qua trong đống test) (C).

**❌ Tại sao đáp án sai:**
> **A.** **Process Builder** là đồ no-code (và đã bị deprecated), không ai rảnh đi bắt test coverage cho nó cả.
> **D.** **Visual Flows** (hay Screen Flows/Autolaunched Flows) cũng là no-code/declarative, Salesforce không ép phải đạt 1% test coverage để deploy.

**💡 Từ khóa ghi nhớ:** `Lên Production: Tổng Apex Org ≥ **75%**, mỗi Trigger phải > **0%** (tức là 1% trở lên). Cứ nhớ '75% Apex' và '1% Trigger' mà phang!`

---

## Câu 213

**🔵 An Approval Process is defined in the Expense_Item__c object. A business rule dictates that whenever a user changes the Status to 'Submitted' on an Expense_Report__c record, all the Expense_Item__c records related to the expense report must enter the approval process individually. Which approach should be used to ensure the business requirement is met?**

- **A.** Create a Process Builder on Expense_Report__c with an 'Apex' action type to submit all related Expense_Item__c records when the criteria is met. ❌
- **B.** Create a Process Builder on Expense_Report__c to mark the related Expense_Item__c as submittable and a trigger on Expense_Item__c to submit the records for approval. ❌
- **C.** Create two Process Builders, one on Expense_Report__c to mark the related Expense_Item__c as submittable and the second on Expense_Item__c to submit the records for approval. ✅
- **D.** Create a Process Builder on Expense_Report__c with a 'Submit for Approval' action type to submit all related Expense_Item__c records when the criteria are met. ❌

**📝 Dịch tiếng Việt:**
> Một Approval Process đã được định nghĩa trên đối tượng Expense_Item__c (bản ghi con). Nghiệp vụ yêu cầu: cứ khi nào user đổi Status thành 'Submitted' trên một bản ghi Expense_Report__c (bản ghi cha), thì tất cả các Expense_Item__c liên quan phải tự động được gửi vào quy trình duyệt một cách RIÊNG LẺ. Giải pháp nào ngon nhất để giải quyết?

**✅ Tại sao đáp án đúng:**
> Chọn **C**. Đây là bài toán kích hoạt đệ quy no-code kinh điển (bây giờ sẽ dùng Record-Triggered Flow thay cho Process Builder). Chúng ta cần 2 bước: 1. Một Flow/PB trên Expense_Report__c (cha) cập nhật một trường đánh dấu (ví dụ check Is_Submittable__c = true) trên toàn bộ Expense_Item__c con liên quan. 2. Một Flow/PB thứ hai trên Expense_Item__c (con) lắng nghe sự thay đổi của trường này và thực hiện Action 'Submit for Approval' cho chính nó. Logic đi từng bước rất mạch lạc và không cần code.

**❌ Tại sao đáp án sai:**
> **A.** Dùng Apex Action để submit thì cũng chạy được đấy, nhưng viết code Apex và viết test class mệt mỏi trong khi no-code xử lý gọn gàng. Tự dưng mang việc vào người làm gì bro?
> **B.** Tự dưng lại nửa nọ nửa kia, vừa dùng Process Builder vừa viết Apex Trigger. Quá cồng kềnh và thiếu nhất quán!
> **D.** Process Builder/Flow chạy trên đối tượng Cha (Expense_Report__c) KHÔNG thể gọi hành động 'Submit for Approval' hàng loạt cho các record con liên quan được. Nút Submit này chỉ chạy trên chính record hiện tại thôi.

**💡 Từ khóa ghi nhớ:** `Submit duyệt con từ cha -> Cần 2 bước tự động hóa (1 cập nhật flag ở con, 1 bắt flag ở con để gửi duyệt). Chọn đáp án có **two Process Builders** (hoặc 2 Flows tương đương)!`

---

## Câu 214

**🔵 A developer is asked to set a picklist field to 'Monitor' on any new Leads owned by a subnet of Users. How should the developer implement this request?**

- **A.** Create an after insert Lead trigger. ❌
- **B.** Create a before insert Lead trigger. ❌
- **C.** Create a record-triggered Flow. ✅
- **D.** Create a Lead formula field. ❌

**📝 Dịch tiếng Việt:**
> Developer được giao task: set một trường Picklist thành 'Monitor' trên mọi bản ghi Lead mới được sở hữu bởi một nhóm User cụ thể. Nên triển khai ca này thế nào cho chuẩn bài?

**💬 Giải thích gốc (English):**
> Creating a record-triggered Flow is indeed a powerful and flexible way to handle this requirement. With a Flow, you can easily set the picklist field to ‘Monitor’ for new Leads owned by a specific subset of Users without writing any code.

**✅ Tại sao đáp án đúng:**
> Chọn **C: Create a record-triggered Flow**. Thời đại 2026, Flow là vua! Mấy vụ gán giá trị trường đơn giản trước khi lưu (Fast Field Updates - before save) thì Record-Triggered Flow đè bẹp mọi đối thủ vì vừa no-code, vừa mượt, vừa dễ bảo trì.

**❌ Tại sao đáp án sai:**
> **A.** **after insert trigger** là quá muộn màng! Lúc này dữ liệu đã ghi xuống DB rồi, muốn sửa lại phải gọi thêm DML Update, tốn thêm 1 transaction và dễ bị loop vô tận. Rất gà!
> **B.** **before insert trigger** giải quyết được về mặt kỹ thuật, nhưng dùng code Apex cho một task cực kỳ đơn giản thế này là cồng kềnh, tốn công viết test class gánh coverage.
> **D.** **Formula field** là trường chỉ đọc (Read-only), không thể là trường Picklist để user chọn hay đổi giá trị được.

**💡 Từ khóa ghi nhớ:** `Gán giá trị trường trước khi lưu -> Ưu tiên tối cao **Record-triggered Flow** (no-code trước, code sau)!`

---

## Câu 215

**🔵 Which three process automations can immediately send an email notification to the owner of an Opportunity when its Amount is changed to be greater than $10,000? (Choose three.)**

- **A.** Process Builder ✅
- **B.** Escalation Rule ❌
- **C.** Flow Builder ✅
- **D.** Approval Process ❌
- **E.** Workflow Rule ✅

**📝 Dịch tiếng Việt:**
> Ba công cụ tự động hóa quy trình (Process Automation) nào có thể LẬP TỨC gửi email thông báo cho chủ sở hữu Opportunity khi trường Amount của nó bị thay đổi thành lớn hơn $10,000? (Chọn 3)

**💬 Giải thích gốc (English):**
> The three process automations that can immediately send an email notification to the owner of an Opportunity when its Amount is changed to be greater than $10,000 are:
> Process Builder
> Flow Builder
> Workflow Rule
> Escalation Rules are primarily used for cases, not opportunities. They are designed to escalate cases to a higher level of support if they are not resolved within a certain time frame. They do not support sending email notifications based on changes to Opportunity fields.
> Approval Processes are used to automate the approval of records. While they can send email notifications, they are triggered by the submission of records for approval, not by changes to field values like the Opportunity Amount. Therefore, they are not suitable for this specific requirement.

**✅ Tại sao đáp án đúng:**
> Chọn **A (Process Builder)**, **C (Flow Builder)** và **E (Workflow Rule)**. Đây đều là những công cụ tự động hóa dạng khai báo (declarative) cho phép bắt sự kiện thay đổi dữ liệu trên Opportunity và kích hoạt hành động gửi Email Alert ngay lập tức không trễ một giây.

**❌ Tại sao đáp án sai:**
> **B.** **Escalation Rule** là tính năng độc quyền của đối tượng Case, dùng để tự động chuyển tiếp các ca hỗ trợ bị quá hạn xử lý. Opportunity không có cửa xài cái này.
> **D.** **Approval Process** là quy trình phê duyệt, bắt buộc phải có bước 'Submit' từ user hoặc hệ thống để kích hoạt các hành động, chứ không tự dưng nhảy ra gửi email khi giá trị trường thay đổi thông thường.

**💡 Từ khóa ghi nhớ:** `Gửi email tự động khi đổi field -> Bộ ba thần thánh: **Workflow**, **Process Builder**, **Flow**!`

---

## Câu 216

**🔵 A developer needs to confirm that a Contact trigger works correctly without changing the organization's data. What should the developer do to test the Contact trigger?**

- **A.** Use Deploy from the VSCode IDE to deploy an 'Insert Contact' Apex class. ❌
- **B.** Use the New button on the Salesforce Contacts Tab to create a new Contact record. ❌
- **C.** Use the Open Execute Anonymous feature on the Developer Console to run an 'Insert Contact' DML statement. ❌
- **D.** Use the Test menu on the Developer Console to run all test classes for the Contact trigger. ✅

**📝 Dịch tiếng Việt:**
> Developer muốn test xem Trigger trên Contact có hoạt động ngon lành cành đào không nhưng TUYỆT ĐỐI không được làm thay đổi dữ liệu thật của hệ thống. Phải làm sao?

**💬 Giải thích gốc (English):**
> Running test classes is the best practice for testing triggers in Salesforce. Test classes allow you to verify that your code works as expected without affecting the actual data in your organization. By using the Test menu in the Developer Console, you can run all test classes that include tests for the Contact trigger. This ensures that the trigger logic is executed and validated in a controlled environment.
> Deploying an ‘Insert Contact’ Apex class from VSCode IDE does not test the trigger directly. It only deploys the class to the organization.
> Creating a new Contact record directly in the Salesforce UI will change the organization’s data.
> Running an ‘Insert Contact’ DML statement using Execute Anonymous will also change the organization’s data.

**✅ Tại sao đáp án đúng:**
> Chọn **D: Chạy các test class của Trigger trong Developer Console**. Các lớp kiểm thử (Apex Unit Tests) trong Salesforce chạy trong một môi trường sandbox cô lập hoàn toàn. Mọi dữ liệu insert/update/delete trong quá trình chạy test sẽ được tự động ROLLBACK (hủy bỏ) 100% sau khi test xong. Org của bạn sẽ sạch bóng như chưa từng có cuộc chia ly.

**❌ Tại sao đáp án sai:**
> **A.** Deploy một Apex class chả liên quan gì đến việc thực thi test cả, code chỉ được đưa lên chứ không chạy.
> **B.** Ấn nút New ngoài giao diện là bạn đang thao tác trên môi trường thật, tạo ra dữ liệu THẬT trên database -> Cook ngay lập tức!
> **C.** **Execute Anonymous** chạy code trực tiếp trên Database thật. Bạn viết `insert new Contact();` trong đó là nó ghi thẳng vào database luôn chứ không hề rollback đâu nhé. Bay màu data thật của người ta đấy!

**💡 Từ khóa ghi nhớ:** `Test an toàn không hại dữ liệu -> Luôn luôn chạy **Apex Unit Test (Run Test)**.`

---

## Câu 217

**🔵 Which control statement should a developer use to ensure that a loop body executes at least once?**

- **A.** for (init_stmt; exit_condition; increment_stmt) {...} ❌
- **B.** do {...} while (condition) ✅
- **C.** while (condition) {...} ❌
- **D.** for (variable : list_or_set) {...} ❌

**📝 Dịch tiếng Việt:**
> Cấu trúc điều khiển vòng lặp nào giúp anh em dev đảm bảo rằng phần thân vòng lặp (loop body) chắc chắn được chạy ÍT NHẤT một lần?

**💬 Giải thích gốc (English):**
> do {…} while (condition): This control statement ensures that the loop body executes at least once because the condition is checked after the loop body has executed.

**✅ Tại sao đáp án đúng:**
> Chọn **B: do {...} while (condition)**. Thằng này thuộc dạng 'cứ làm đi rồi tính sau'. Nó sẽ lao vào thực thi khối code trong `do` trước, sau đó mới ngó xuống `while` để check điều kiện. Điều kiện có sai ngay từ đầu thì thân vòng lặp vẫn kịp chạy được 1 lần.

**❌ Tại sao đáp án sai:**
> **A.** Vòng lặp `for` truyền thống check điều kiện trước rồi mới chạy, điều kiện sai từ đầu là nghỉ khỏe.
> **C.** Vòng lặp `while` cũng check điều kiện ở ngay đầu bài, sai là out luôn không chạy lần nào.
> **D.** Vòng lặp `for-each` duyệt qua list/set. Nếu list/set rỗng (empty) thì nó bỏ qua luôn, chả chạy lần nào.

**💡 Từ khóa ghi nhớ:** `Chạy ít nhất 1 lần -> Cứ **DO** trước rồi **WHILE** sau!`

---

## Câu 218

**🔵 Which two declarative process automation features can be directly invoked when a field value changes on a record? (Choose two.)**

- **A.** Cloud Flow Designer ❌
- **B.** Process Builder processes ✅
- **C.** Validation rules ❌
- **D.** Workflow rules ✅

**📝 Dịch tiếng Việt:**
> Hai tính năng tự động hóa khai báo (declarative process automation) nào có thể được kích hoạt TRỰC TIẾP ngay khi giá trị một trường trên bản ghi thay đổi? (Chọn 2)

**💬 Giải thích gốc (English):**
> Salesforce retired Cloud Flow Designer in Winter '20. Users were encouraged to transition to the newer Flow Builder, which offers a more modern and user-friendly interface for creating flows. Since now Salesforce is retiring the Workflow rules.

**✅ Tại sao đáp án đúng:**
> Chọn **B (Process Builder)** và **D (Workflow rules)** (Và ngày nay là Flow Builder). Cả hai công cụ này đều hỗ trợ cơ chế trigger ngầm dựa trên sự kiện tạo mới hoặc cập nhật bản ghi để thực thi các action tự động ngay tắp lự.

**❌ Tại sao đáp án sai:**
> **A.** **Cloud Flow Designer** là cái tên thời đồ đá của công cụ tạo Flow bằng Flash cũ kỹ, đã bị khai tử từ đời tám hoánh nào rồi.
> **C.** **Validation rules** (Quy tắc xác thực) không phải công cụ tự động hóa quy trình! Nhiệm vụ duy nhất của nó là bắt lỗi và chửi thẳng vào mặt user khi nhập sai data để chặn không cho lưu bản ghi.

**💡 Từ khóa ghi nhớ:** `Kích hoạt tự động hóa khi đổi trường no-code -> Chọn **Process Builder** / **Flow Builder** / **Workflow**.`

---

## Câu 219

**🔵 Which two strategies should a developer use to avoid hitting governor limits when developing in a multi-tenant environment? (Choose two.)**

- **A.** Use collections to store all fields from a related object and not just minimally required fields. ❌
- **B.** Use methods from the "Limits" class to monitor governor limits. ✅
- **C.** Use SOQL for loops to iterate data retrieved from queries that return a high number of rows. ✅
- **D.** Use variables within Apex classes to store large amounts of data. ❌

**📝 Dịch tiếng Việt:**
> Hai chiến lược nào giúp lập trình viên tránh bị 'gõ đầu' bởi Governor Limits khi code trong môi trường chia sẻ tài nguyên (multi-tenant) của Salesforce? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> Chọn **B** và **C**. Lớp **Limits** cung cấp các phương thức siêu xịn như `Limits.getQueries()` giúp bạn tự giám sát xem mình đã ngốn bao nhiêu tài nguyên để kịp thời phanh lại (B). Sử dụng **SOQL for loops** (ví dụ `for (Account acc : [SELECT Id FROM Account])`) giúp Salesforce tự động chia nhỏ dữ liệu trả về thành các lô (batch) 200 bản ghi, giúp giải phóng bộ nhớ heap cực đỉnh khi truy vấn lượng data lớn (C).

**❌ Tại sao đáp án sai:**
> **A.** Query tất cả các trường thay vì chỉ lấy các trường cần thiết sẽ làm phình to bộ nhớ Heap của transaction, dễ dính lỗi `Heap Limit Exception`. Quá cồng kềnh!
> **D.** Dùng biến trong Apex class để nhét một lượng data khổng lồ sẽ trực tiếp làm tràn bộ nhớ heap nhanh như chớp. Cook ngay!

**💡 Từ khóa ghi nhớ:** `Chống Governor Limit: Sử dụng class **Limits** để đo lường + Dùng **SOQL for loops** để tối ưu bộ nhớ.`

---

## Câu 220

**🔵 Which feature should a developer use to update an inventory count on related Product records when the status of an Order is modified to indicate it is fulfilled?**

- **A.** Process Builder process ✅
- **B.** Lightning component ❌
- **C.** Visualforce page ❌
- **D.** Workflow rule ❌

**📝 Dịch tiếng Việt:**
> Tính năng nào nên dùng để tự động cập nhật số lượng tồn kho (inventory count) trên các bản ghi Product liên quan khi trạng thái của Order bị sửa thành 'Fulfilled'?

**✅ Tại sao đáp án đúng:**
> Chọn **A: Process Builder process** (hoặc ngày nay là Flow Builder). Mối quan hệ từ Product sang Order thường là Lookup hoặc có tính chất gián tiếp. Process Builder/Flow cho phép chúng ta thực hiện hành động cập nhật chéo đối tượng (cross-object update) từ bản ghi hiện tại sang các bản ghi liên quan cực kỳ dễ dàng mà không cần viết một dòng code nào.

**❌ Tại sao đáp án sai:**
> **B.** **Lightning Component** là thành phần UI để hiển thị trên màn hình, không phải công cụ tự động hóa chạy ngầm dưới database.
> **C.** **Visualforce page** cũng là công nghệ UI cũ để render trang web, không tự chạy ngầm khi bản ghi thay đổi.
> **D.** **Workflow rule** siêu cùi bắp, chỉ hỗ trợ cập nhật chính bản ghi đó hoặc bản ghi cha trong mối quan hệ Master-Detail cụ thể chứ không thể cập nhật đi ngang hay đi xuống các đối tượng khác tự do như Process Builder/Flow.

**💡 Từ khóa ghi nhớ:** `Cập nhật chéo đối tượng liên quan (con/cháu/bên cạnh) no-code -> Cứ **Flow Builder** hoặc **Process Builder** mà chọn.`

---

## Câu 221

**🔵 The operation manager at a construction company uses a custom object called Machinery to manage the usage and maintenance of its cranes and other machinery. The manager wants to be able to assign machinery to different constructions jobs, and track the dates and costs associated with each job. More than one piece of machinery can be assigned to one construction job. What should a developer do to meet these requirements?**

- **A.** Create a lookup field on the Construction Job object to the Machinery object. ❌
- **B.** Create a lookup field on the Machinery object to the Construction Job object. ❌
- **C.** Create a junction object with Master-Detail Relationship to both the Machinery object and the Construction Job object. ✅
- **D.** Create a Master-Detail Lookup on the Machinery object to the Construction Job object. ❌

**📝 Dịch tiếng Việt:**
> Một công ty xây dựng dùng custom object Machinery để quản lý máy móc (như cần cẩu). Quản lý muốn gán máy móc vào các Construction Job (dự án xây dựng) khác nhau để theo dõi ngày tháng và chi phí cho từng job. Một Job có thể dùng nhiều máy móc, và một máy móc cũng có thể được gán cho nhiều Job khác nhau. Dev phải làm thế nào?

**✅ Tại sao đáp án đúng:**
> Chọn **C: Tạo Junction Object trung gian có hai mối quan hệ Master-Detail** trỏ về cả Machinery và Construction Job. Đây chính là bài toán thiết lập mối quan hệ **Nhiều-Nhiều (Many-to-Many)** kinh điển! Bản ghi của Junction Object này sẽ đại diện cho mỗi lần gán máy móc vào dự án, tha hồ lưu trữ ngày và chi phí riêng biệt.

**❌ Tại sao đáp án sai:**
> **A.** Nếu tạo lookup trên Construction Job trỏ tới Machinery, một Job chỉ có thể chọn được duy nhất 1 máy móc tại một thời điểm. Hẹo luôn!
> **B.** Nếu tạo lookup trên Machinery trỏ tới Construction Job, một máy móc chỉ có thể tham gia đúng 1 dự án duy nhất. Thế thì máy đắp chiếu hết à?
> **D.** **Master-Detail Lookup** là một thuật ngữ râu ông nọ cắm cằm bà kia, không hề tồn tại loại trường này trong Salesforce!

**💡 Từ khóa ghi nhớ:** `Mối quan hệ Nhiều-Nhiều (Many-to-Many) -> Auto chọn **Junction Object** với **2 Master-Detail relationships**.`

---

## Câu 222

**🔵 A developer needs to have records with specific field values in order to test a new Apex class. What should the developer do to ensure the data is available to the test?**

- **A.** Use SOQL to query the org for the required data. ❌
- **B.** Use Anonymous Apex to create the required data. ❌
- **C.** Use Test.loadData() and reference a CSV file. ❌
- **D.** Use Test.loadData() and reference a static resource. ✅

**📝 Dịch tiếng Việt:**
> Developer cần các bản ghi có sẵn một số giá trị cụ thể để test một Apex class mới viết. Làm thế nào để đảm bảo đống dữ liệu này luôn sẵn sàng cho việc chạy test?

**💬 Giải thích gốc (English):**
> Using the Test.loadData method, you can populate data in your test methods without having to write many lines of code.
> Follow these steps:
> 1. Add the data in a .csv file.
> 2. Create a static resource for this file.
> 3. Call Test.loadData within your test method and passing it the sObject type token and the static resource name.

**✅ Tại sao đáp án đúng:**
> Chọn **D: Sử dụng Test.loadData() và truyền vào một Static Resource**. Bạn chỉ cần ném đống data test vào một file CSV, upload file đó lên Salesforce dưới dạng **Static Resource**, sau đó gọi `Test.loadData(Account.sObjectType, 'TênStaticResource')` trong code test. Salesforce sẽ tự động nhét đống record đó vào bộ nhớ test cực kỳ sạch sẽ và nhanh gọn.

**❌ Tại sao đáp án sai:**
> **A.** Query trực tiếp dữ liệu từ Org bằng SOQL là một quả 'anti-pattern' cực mạnh trong unit test. Mặc định môi trường test bị cô lập hoàn toàn với data thật (SeeAllData=false), SOQL sẽ trả về con số 0 tròn trĩnh.
> **B.** Dùng Anonymous Apex để tạo dữ liệu thì dữ liệu đó sẽ được lưu thật vào Org chứ không chui vào môi trường test cô lập, chạy test vẫn fail như thường.
> **C.** Hàm `Test.loadData()` nhận đối số thứ hai là tên của **Static Resource** chứ không thể nhận trực tiếp một đường dẫn file CSV từ máy tính của bạn.

**💡 Từ khóa ghi nhớ:** `Nạp data test từ CSV -> Upload lên **Static Resource** rồi gọi **Test.loadData()**.`

---

## Câu 223

**🔵 A developer created a Lightning component to display a short text summary for an object and wants to use it with multiple Apex classes. How should the developer design the Apex classes?**

- **A.** Have each class define method getObject() that returns the sObject that is controlled by the Apex class. ❌
- **B.** Extend each class from the same base class that has a method getTextSummary() that returns the summary. ❌
- **C.** Have each class implement an interface that defines method getTextSummary() that returns the summary. ✅
- **D.** Have each class define method getTextSummary() that returns the summary. ❌

**📝 Dịch tiếng Việt:**
> Developer tạo ra một Lightning component để hiển thị đoạn text tóm tắt ngắn cho một object và muốn component này dùng chung được với nhiều Apex class khác nhau. Nên thiết kế các Apex class này thế nào cho uy tín?

**✅ Tại sao đáp án đúng:**
> Chọn **C: Cho mỗi class implement một Interface chung có định nghĩa method `getTextSummary()`**. Đây chính là đỉnh cao của tính đa hình (Polymorphism) trong OOP! Chỉ cần các class đều cam kết hiện thực hóa phương thức `getTextSummary()` từ Interface, component có thể gọi hàm này trên bất kỳ class nào mà không cần quan tâm class đó xử lý logic bên trong ra sao.

**❌ Tại sao đáp án sai:**
> **A.** Hàm `getObject()` chỉ trả về sObject thô, không giải quyết được yêu cầu lấy ra chuỗi text tóm tắt được tùy biến riêng bởi từng class.
> **B.** Apex chỉ hỗ trợ đơn kế thừa (single inheritance). Nếu bắt các class phải kế thừa từ một base class chung, bạn sẽ tước đi cơ hội kế thừa các class hữu ích khác sau này. Rất tù túng!
> **D.** Nếu tự định nghĩa method khơi khơi không qua Interface ràng buộc, trình biên dịch sẽ không thể đảm bảo chắc chắn class nào cũng có hàm đó, dẫn đến lỗi runtime sấp mặt.

**💡 Từ khóa ghi nhớ:** `Dùng chung một component với nhiều Apex class khác nhau -> Cho các class **implement một INTERFACE** chung.`

---

## Câu 224

**🔵 A developer wrote Apex code that calls out to an external system. How should a developer write the test to provide test coverage?**

- **A.** Write a class that implements the HTTPCalloutMock interface. ✅
- **B.** Write a class that extends HTTPCalloutMock. ❌
- **C.** Write a class that extends WebserviceMock. ❌
- **D.** Write a class that implements the WebserviceMock interface. ❌

**📝 Dịch tiếng Việt:**
> Developer viết code Apex có thực hiện gọi API (callout) ra hệ thống bên ngoài. Làm sao để viết test class cho đống code này để lấy coverage?

**💬 Giải thích gốc (English):**
> To provide test coverage for Apex code that calls out to an external system, the developer should use the HTTPCalloutMock interface. This allows the developer to mock the HTTP response and test the callout logic without actually making a real HTTP request.

**✅ Tại sao đáp án đúng:**
> Chọn **A: Viết một class implement interface `HttpCalloutMock`**. Salesforce cấm tiệt việc gọi API thật ra Internet khi đang chạy Unit Test để tránh phụ thuộc mạng và làm chậm hệ thống. Bạn phải tạo một class giả lập (Mock) hiện thực hóa interface `HttpCalloutMock` để định nghĩa sẵn dữ liệu trả về giả lập (fake response).

**❌ Tại sao đáp án sai:**
> **B.** `HttpCalloutMock` là một **interface** chứ không phải một class thông thường, nên bạn phải dùng từ khóa `implements` chứ không thể dùng `extends` (kế thừa). Lỗi cú pháp căn bản, cook ngay!
> **C.** `WebserviceMock` dùng cho SOAP API Callout chứ không phải HTTP/REST Callout thông thường, và nó cũng là interface nên không dùng `extends` được.
> **D.** Dù dùng đúng từ khóa `implements` nhưng `WebserviceMock` chỉ dành cho SOAP API (WSDL), đề bài đang nói callout chung chung/HTTP thì phải ưu tiên `HttpCalloutMock`.

**💡 Từ khóa ghi nhớ:** `Mock HTTP Callout Test -> Luôn là **implements HttpCalloutMock**.`

---

## Câu 225

**🔵 What is the maximum number of SOQL queries used by the following code?
List<Account> aList = [SELECT Id FROM Account LIMIT 5];
for(Account a : aList){
List<Contact> cList = [SELECT Id FROM Contact Where AccountId = : a.Id];
}**

- **A.** 1 ❌
- **B.** 5 ❌
- **C.** 6 ✅
- **D.** 2 ❌

**📝 Dịch tiếng Việt:**
> Số lượng câu truy vấn SOQL tối đa sẽ được thực thi khi chạy đoạn mã Apex sau là bao nhiêu? [Mã SOQL inside For]

**💬 Giải thích gốc (English):**
> Initial Query: 1
> Queries Inside Loop: Up to 5 (one for each Account)

**✅ Tại sao đáp án đúng:**
> Chọn **C: 6**. Hãy cùng làm toán tiểu học:
1. Câu truy vấn SOQL đầu tiên `[SELECT Id FROM Account LIMIT 5]` nằm ngoài vòng lặp -> Chạy **1 lần**.
2. Kết quả trả về tối đa **5** bản ghi Account. Vòng lặp `for` sẽ chạy tối đa **5 lần**.
3. Bên trong vòng lặp có 1 câu SOQL truy vấn Contact -> Bị kích hoạt **5 lần**.
Tổng cộng: 1 (ngoài) + 5 (trong) = **6 câu SOQL**.

**❌ Tại sao đáp án sai:**
> **A.** Tính toán sai số lượng thực tế. Câu truy vấn SOQL Account ở ngoài không thể bị biến mất được.
> **B.** Quên tính câu lệnh SOQL query Account nằm ngoài vòng lặp. Quá bất cẩn!
> **D.** Tính toán sai số vòng chạy của list Account. List có tối đa 5 phần tử nên vòng lặp phải chạy tới 5 lần chứ không phải 1 lần.

**💡 Từ khóa ghi nhớ:** `SOQL trong vòng lặp là tối kỵ! Công thức đếm: `1 (ngoài) + LIMIT (vòng lặp) = Tổng SOQL`. Ở đây là 1 + 5 = 6.`

---

## Câu 226

**🔵 Which process automation can be used to calculate the shipping cost for an Order when the Order is placed and apply a percentage of the shipping cost to some of the related Order Products?**

- **A.** Lightning Component ❌
- **B.** Flow Builder ✅
- **C.** Entitlement Rules ❌
- **D.** Approval Process ❌

**📝 Dịch tiếng Việt:**
> Công cụ tự động hóa quy trình nào có thể được sử dụng để tự động tính toán chi phí vận chuyển cho một Đơn hàng (Order) khi nó được đặt, sau đó áp dụng một tỷ lệ phần trăm chi phí vận chuyển đó lên một số Sản phẩm của Đơn hàng (Order Products) liên quan?

**✅ Tại sao đáp án đúng:**
> Chọn **B: Flow Builder**. Đây là công cụ tự động hóa no-code tối thượng của Salesforce! Flow Builder dư sức thực hiện các phép toán phức tạp, duyệt qua danh sách các bản ghi con liên quan (Order Products) và cập nhật giá trị cho chúng một cách mượt mà không cần code.

**❌ Tại sao đáp án sai:**
> **A.** **Lightning Component** là thành phần UI hiển thị giao diện trên màn hình, không phải công cụ tự động hóa xử lý logic lưu trữ cơ sở dữ liệu.
> **C.** **Entitlement Rules** dùng trong Service Cloud để xác định mức độ dịch vụ hỗ trợ (SLA) của khách hàng, chả liên quan gì đến tính toán Order.
> **D.** **Approval Process** dùng để gửi bản ghi cho sếp duyệt (Approve/Reject), hoàn toàn không thể thực hiện các phép tính toán số học phức tạp hay đi cập nhật hàng loạt record con.

**💡 Từ khóa ghi nhớ:** `Tính toán logic + Duyệt cập nhật bản ghi con liên quan (Related Records) -> Chọn ngay **Flow Builder**.`

---

## Câu 227

**🔵 A developer created a child Lightning web component nested inside a parent Lightning web component. The parent component needs to pass a string value to the child component. In which two ways can this be accomplished? (Choose two.)**

- **A.** The parent component can use a custom event to pass the data to the child component. ✅
- **B.** The parent component can invoke a method in the child component. ❌
- **C.** The parent component can use a public property to pass the data to the child component. ✅
- **D.** The parent component can use the Apex controller class to send data to the child component. ❌

**📝 Dịch tiếng Việt:**
> Developer tạo ra một component con (child LWC) nằm trong một component cha (parent LWC). Component cha cần truyền một giá trị dạng String xuống cho component con. Hai cách nào giúp thực hiện nhiệm vụ này? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> Mặc dù trong lập trình LWC chuẩn, để Cha truyền dữ liệu xuống Con ta dùng **Public Property** (C) bằng cách khai báo decorator `@api` ở con, hoặc **Invoke a public method in child** (B) bằng cách gọi hàm `@api` từ con. Tuy nhiên, đề thi Salesforce chính thức thỉnh thoảng ghi nhận đáp án **A (Custom Event)** và **C (Public Property)** là bộ đáp án đúng (có thể là lỗi thiết lập đáp án của Salesforce). Để đảm bảo ăn trọn điểm khi đi thi, bạn cứ chọn **A** và **C** nhé!

**❌ Tại sao đáp án sai:**
> **B.** Trong thực tế lập trình, cha gọi method của con qua `@api` (B) là đúng 100% kỹ thuật, nhưng trong ngân hàng câu hỏi gốc đôi khi nó bị cho ra rìa và chấm sai. Rất ảo ma!
> **D.** Dùng Apex controller để làm cầu nối truyền dữ liệu giữa hai component cùng nằm trên một trình duyệt là siêu cồng kềnh, làm chậm hệ thống vô ích.

**💡 Từ khóa ghi nhớ:** `Lập trình LWC chuẩn: Cha gọi xuống Con dùng `@api` (Property hoặc Method). Đi thi Salesforce: Chọn cặp **Custom Event** và **Public Property** (A & C) cho ăn chắc!`

---

## Câu 228

**🔵 What are two best practices when it comes to Lightning Web Component events? (Choose two.)**

- **A.** Use event.detail to communicate data to elements in the same shadow tree. ❌
- **B.** Use CustomEvent to pass data from a child to a parent component. ✅
- **C.** Use event.target to communicate data to elements that aren't in the same shadow tree. ✅
- **D.** Use events configured with bubbles: false and composed: false. ❌

**📝 Dịch tiếng Việt:**
> Hai best practices (thực hành tốt nhất) nào khi truyền nhận các sự kiện (Events) trong Lightning Web Components (LWC)? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> Chọn **B** và **C**. Sử dụng **CustomEvent** là cách chuẩn mực và an toàn nhất để component con gửi dữ liệu hoặc bắn tín hiệu ngược lên component cha (B). Trình duyệt hỗ trợ thuộc tính **`event.target`** để xác định element phát ra sự kiện, giúp giao tiếp thông tin dễ dàng và hiệu quả hơn kể cả khi đi xuyên shadow boundary (C).

**❌ Tại sao đáp án sai:**
> **A.** `event.detail` chỉ đơn thuần là thuộc tính chứa dữ liệu payload đi kèm sự kiện chứ bản thân nó không quyết định hay giới hạn phạm vi giao tiếp trong shadow tree.
> **D.** Cấu hình mặc định của sự kiện là `bubbles: false` và `composed: false`. Tuy nhiên, việc ép buộc cấu hình này trong mọi trường hợp không phải là best practice duy nhất, mà phải linh hoạt tùy theo bài toán shadow DOM.

**💡 Từ khóa ghi nhớ:** `LWC Events best practice -> Chọn cặp **CustomEvent** truyền con-lên-cha (B) và **event.target** để xác định nguồn phát (C).`

---

## Câu 229

**🔵 A developer migrated functionality from JavaScript Remoting to a Lightning web component and wants to use the existing getOpportunities() method to provide data. Which modification to the method is necessary?**

- **A.** The method must return a String of a serialized JSON Array. ❌
- **B.** The method must be decorated with (cacheable=true). ❌
- **C.** The method must be decorated with @AuraEnabled. ✅
- **D.** The method must return a JSON Object. ❌

**📝 Dịch tiếng Việt:**
> Developer chuyển đổi tính năng từ JavaScript Remoting (Classic) sang LWC (Lightning Web Component) và muốn xài lại method getOpportunities() đã có sẵn bên Apex để lấy data. Cần chỉnh sửa gì trên cái method này?

**✅ Tại sao đáp án đúng:**
> Chọn **C: Gắn thêm annotation `@AuraEnabled`**. Đây là tấm vé thông hành bắt buộc để bất kỳ method nào trong Apex có thể 'nói chuyện' được với các component Lightning (bao gồm cả LWC và Aura Component). Không có `@AuraEnabled` thì LWC coi như mù, không thấy method này đâu cả.

**❌ Tại sao đáp án sai:**
> **A.** Bậy bạ nha! Apex tự động serialize đối tượng sObject thành JSON khi trả về cho LWC, cấm tự viết code serialize thành String JSON Array làm gì cho nặng máy.
> **B.** `cacheable=true` là tùy chọn cực kỳ khuyến khích khi dùng Wire Service để tăng tốc độ lưu cache, nhưng nó không phải điều kiện bắt buộc để LWC có thể gọi được method (Imperative call vẫn gọi method không có `cacheable=true` ngon ơ).
> **D.** Method trả về List sObject trực tiếp của Salesforce là quá đẹp rồi, không cần bắt buộc phải parse thành kiểu JSON Object thô.

**💡 Từ khóa ghi nhớ:** `Muốn Apex method giao tiếp được với LWC -> Bắt buộc phải gắn **@AuraEnabled**.`

---

## Câu 230

**🔵 A developer must provide a custom user interface when users edit a Contact. Users must be able to use the interface in Salesforce Classic and Lightning Experience. What should the developer do to provide the custom user interface?**

- **A.** Override the Contact's Edit button with a Visualforce page in Salesforce Classic and a Lightning component in Lightning Experience. ✅
- **B.** Override the Contact's Edit button with a Visualforce page in Salesforce Classic and a Lightning page in Lightning Experience. ❌
- **C.** Override the Contact's Edit button with a Lightning component in Salesforce Classic and a Lightning component in Lightning Experience. ❌
- **D.** Override the Contact's Edit button with a Lightning page in Salesforce Classic and a Visualforce page in Lightning Experience. ❌

**📝 Dịch tiếng Việt:**
> Developer cần cung cấp giao diện custom khi người dùng Edit một Contact. Giao diện này phải chạy ngon nghẻ trên cả 2 môi trường Salesforce Classic và Lightning Experience. Dev nên làm gì?

**✅ Tại sao đáp án đúng:**
> Chọn **A: Override nút Edit bằng một trang Visualforce trong Classic và một Lightning component trong Lightning Experience**. Đây là cấu hình ghi đè (button override) chuẩn sách giáo khoa! Salesforce cho phép cấu hình ghi đè riêng biệt: môi trường Classic cũ kỹ thì dùng Visualforce Page để tương thích tốt, còn Lightning Experience hiện đại thì dùng Lightning Component để đem lại trải nghiệm mượt mà nhất.

**❌ Tại sao đáp án sai:**
> **B.** **Lightning page** là cả một trang tổng quan (dashboard/home/record page) được kéo thả bằng App Builder, không phải là một component đóng gói có thể dùng để ghi đè trực tiếp nút Edit được.
> **C.** Salesforce Classic là đồ cổ, nó không hỗ trợ render và chạy trực tiếp Lightning Component một cách mượt mà độc lập ngoài giao diện Edit.
> **D.** Bị đảo lộn vị trí công nghệ! Classic đi dùng Lightning Page còn Lightning Experience lại đi dùng Visualforce thì chả khác gì râu ông nọ cắm cằm bà kia.

**💡 Từ khóa ghi nhớ:** `Override button cho cả 2 môi trường -> **Classic = Visualforce Page**, **Lightning = Lightning Component**.`

---

## Câu 231

**🔵 Which Lightning code segment should be written to declare dependencies on a Lightning component, c:accountList, that is used in a Visualforce page?**

- **A.** <aura:application access="GLOBAL"> <aura:dependency resource="c:accountList"/> </aura:application> ❌
- **B.** <aura:application access="GLOBAL" extends="ltng:outApp"> <aura:dependency resource="c:accountList"/> </aura:application> ✅
- **C.** <aura:component access="GLOBAL"> <aura:dependency resource="c:accountList"> </aura:component> ❌
- **D.** <aura:component access="GLOBAL" extends="ltng:outApp"> <aura:dependency resource="c:accountList"/> </aura:component> ❌

**📝 Dịch tiếng Việt:**
> Đoạn code Lightning nào dưới đây dùng để khai báo các thành phần phụ thuộc (dependencies) cho một component c:accountList khi nhúng nó vào trang Visualforce?

**💬 Giải thích gốc (English):**
> To describe the components that you want to deploy outside of Salesforce, create a Lightning Out app. A Lightning Out app is a special standalone Aura app defined with the <aura:application> tag. Add components to the app with the <aura:dependency> tag

**✅ Tại sao đáp án đúng:**
> Chọn **B: `<aura:application access="GLOBAL" extends="ltng:outApp"> <aura:dependency resource="c:accountList"/> </aura:application>`**. Để nhúng được component Lightning vào trang Visualforce (hoặc app ngoài qua công nghệ **Lightning Out**), bạn bắt buộc phải tạo một standalone Aura App làm cầu nối. Cái App này bắt buộc phải có thuộc tính `extends="ltng:outApp"` và bên trong chứa thẻ `<aura:dependency>` để đăng ký trước các component con sẽ sử dụng.

**❌ Tại sao đáp án sai:**
> **A.** Thiếu thuộc tính kế thừa `extends="ltng:outApp"` thì cái App này chỉ là một ứng dụng Lightning độc lập thông thường, không thể kích hoạt chế độ kết nối của Lightning Out được.
> **C.** Thẻ `<aura:component>` không thể đóng vai trò làm app container làm cầu nối cho Lightning Out, và nó cũng viết sai cú pháp đóng thẻ `</aura:dependency>`.
> **D.** Component không hỗ trợ thuộc tính `extends="ltng:outApp"` và không thể thay thế cho thẻ `<aura:application>` trong kịch bản này.

**💡 Từ khóa ghi nhớ:** `Lightning Out nhúng Visualforce -> 100% bắt buộc dùng **`<aura:application extends="ltng:outApp">`**.`

---

## Câu 232

**🔵 A developer can use the debug log to see which three types of information? (Choose three.)**

- **A.** HTTP callouts to external systems ✅
- **B.** Database changes ✅
- **C.** Resource usage and limits ✅
- **D.** User login events ❌
- **E.** Actions triggered by time-based workflow ❌

**📝 Dịch tiếng Việt:**
> Developer có thể dùng Debug Log (Nhật ký gỡ lỗi) trong Salesforce để xem ba loại thông tin nào sau đây? (Chọn 3)

**💬 Giải thích gốc (English):**
> Debug Log
> A debug log can record database operations, system processes, and errors that occur when executing a transaction or running unit tests. Debug logs can contain information about:
> Database changes
> HTTP callouts
> Apex errors
> Resources used by Apex
> Automated workflow processes, such as:
> Workflow rules
> Assignment rules
> Approval processes
> Validation rules

**✅ Tại sao đáp án đúng:**
> Chọn **A (HTTP callouts)**, **B (Database changes)** và **C (Resource usage and limits)**. Khi chạy một transaction (ví dụ Trigger, Apex controller...), Debug Log sẽ ghi lại cực kỳ chi tiết: mọi cuộc gọi API ra ngoài (A), các thao tác DML thêm/sửa/xóa bản ghi dưới database (B), và thống kê tài nguyên đã tiêu thụ so với giới hạn Governor Limits ở cuối log (C).

**❌ Tại sao đáp án sai:**
> **D.** Thông tin đăng nhập của user được quản lý riêng biệt ở trang **Login History** trong Setup chứ không hiện ra trong debug log của Apex transaction.
> **E.** Các hành động kích hoạt bởi time-based workflow được giám sát và xếp hàng đợi ở mục **Time-Based Workflow Queue** trong Setup chứ debug log thông thường không hiển thị cái này.

**💡 Từ khóa ghi nhớ:** `Debug Log ghi nhận: **DML** (Database), **Callouts** (HTTP), **Limits** (Tài nguyên).`

---

## Câu 233

**🔵 A developer created a trigger on the Account object and wants to test if the trigger is properly bulkified. The developer team decided that the trigger should be tested with 200 account records with unique names. What two things should be done to create the test data within the unit test with the least amount of code? (Choose two.)**

- **A.** Use the @isTest(seeAllData=true) annotation in the test class. ❌
- **B.** Create a static resource containing test data. ✅
- **C.** Use the @isTest(isParallel=true) annotation in the test class. ❌
- **D.** Use Test.loadData to populate data in your test methods. ✅

**📝 Dịch tiếng Việt:**
> Developer viết một Trigger trên Account và muốn test xem trigger đó đã được 'bulkified' (xử lý lô lớn) ngon lành chưa. Đội phát triển quyết định test với 200 bản ghi Account có tên duy nhất. Hai việc nào nên được làm để tạo ra đống data test này trong unit test với LƯỢNG CODE ÍT NHẤT? (Chọn 2)

**💬 Giải thích gốc (English):**
> You can create a CSV file with the test data and upload it as a static resource and Use Test.loadData to load test data from a static resource, making it efficient to create multiple records with minimal code.
> Here is sample code:
> @isTest
> public class AccountTriggerTest {
> @isTest
> static void testBulkifiedTrigger() {
> // Load test data from the static resource
> List<Account> accounts = (List<Account>) Test.loadData(Account.class, 'AccountTestData');
> // Perform your test operations
> Test.startTest();
> insert accounts;
> Test.stopTest();
> // Add your assertions here
> // Example: System.assertEquals(200, [SELECT COUNT() FROM Account WHERE Name LIKE 'Account%']);
> }
> }

**✅ Tại sao đáp án đúng:**
> Chọn **B** và **D**. Cách lười viết code nhất mà vẫn chuẩn chỉ là: Tạo một file CSV chứa 200 tên Account độc nhất rồi up lên làm **Static Resource** (B). Sau đó trong test method, chỉ cần gọi đúng một dòng lệnh **`Test.loadData(Account.sObjectType, 'TênStaticResource')`** (D). Salesforce sẽ tự động nạp toàn bộ 200 bản ghi đó vào bộ nhớ test cực kỳ mượt mà, khỏi cần viết vòng lặp `for` insert rườm rà.

**❌ Tại sao đáp án sai:**
> **A.** `seeAllData=true` là một quả 'tối kỵ' (anti-pattern) giúp test class nhìn thấy data thật ngoài đời của Org. Nó không giúp tạo dữ liệu test mới và dễ làm hỏng logic test khi deploy sang Org khác.
> **C.** `isParallel=true` chỉ là cấu hình cho phép các test class chạy song song để tiết kiệm thời gian chạy test tổng thể, chả liên quan gì đến việc tạo hay nạp dữ liệu test.

**💡 Từ khóa ghi nhớ:** `Tạo data test số lượng lớn ít code nhất -> **Static Resource** (file CSV) + **Test.loadData()**.`

---

## Câu 234

**🔵 What can be developed using the Lightning Component framework?**

- **A.** Salesforce integrations ❌
- **B.** Salesforce Classic and Lightning user interface pages ❌
- **C.** Hosted web applications ❌
- **D.** Single-page web apps ✅

**📝 Dịch tiếng Việt:**
> Thế cái Lightning Component framework dùng để phát triển cái gì thế các khứa?

**💬 Giải thích gốc (English):**
> Lightning Component Framework
> The Lightning Component framework is a UI framework for developing single-page web apps for mobile and desktop devices.

**✅ Tại sao đáp án đúng:**
> Chọn **D: Single-page web apps (SPA)**. Lightning Component framework (cả Aura và LWC) được thiết kế hiện đại theo kiến trúc ứng dụng web một trang duy nhất (Single-page app). Dữ liệu được tải động qua lại giữa Client (JavaScript) và Server (Apex) mà không cần tải lại toàn bộ trang web, đem lại trải nghiệm mượt mà y hệt như Facebook hay Gmail.

**❌ Tại sao đáp án sai:**
> **A.** **Salesforce integrations** (tích hợp hệ thống) được phát triển bằng Apex, REST/SOAP APIs hoặc MuleSoft chứ framework UI này chỉ làm nhiệm vụ hiển thị thôi.
> **B.** Salesforce Classic là giao diện đời cổ, không dùng Lightning Component framework làm nền tảng chính.
> **C.** **Hosted web applications** là các app được deploy và host độc lập trên server riêng (ví dụ Heroku, AWS). Salesforce không dùng framework này để tạo các app chạy độc lập bên ngoài nền tảng của mình.

**💡 Từ khóa ghi nhớ:** `Lightning Component framework = **Single-page web apps (SPA)**.`

---

## Câu 235

**🔵 A developer must create an Apex class, ContactController, that a Lightning component can use to search for Contact records. Users of the Lightning component should only be able to search for Contact records to which they have access. Which two will restrict the records correctly? (Choose two.)**

- **A.** public class ContactController ❌
- **B.** public with sharing class ContactController ✅
- **C.** public without sharing class ContactController ❌
- **D.** public inherited sharing class ContactController ✅

**📝 Dịch tiếng Việt:**
> Developer cần viết một class Apex tên là ContactController làm controller cho Lightning component tìm kiếm Contact. Người dùng chỉ được phép tìm thấy những bản ghi Contact mà họ thực sự có quyền truy cập (Sharing Rules/OWD). Hai cách khai báo class nào dưới đây sẽ giới hạn quyền bản ghi chuẩn xác nhất? (Chọn 2)

**💬 Giải thích gốc (English):**
> With Sharing
> Use the with sharing keyword when declaring a class to enforce sharing rules of the current user. Explicitly setting this keyword ensures that Apex code runs in the current user context. Apex code that is executed with the executeAnonymous call and Connect in Apex always execute using the sharing rules of the current user.
> Without Sharing
> Use the without sharing keyword when declaring a class to ensure that the sharing rules for the current user are not enforced. For example, you can explicitly turn off sharing rule enforcement when a class is called from another class that is declared using with sharing.
> Inherited Sharing
> Use the inherited sharing keyword when declaring a class to enforce the sharing rules of the class that calls it. Using inherited sharing is an advanced technique to determine the sharing mode at runtime and design Apex classes that can run in either with sharing or without sharing mode.

**✅ Tại sao đáp án đúng:**
> Chọn **B** và **D**. Khai báo `with sharing` (B) ép class phải tuân thủ nghiêm ngặt luật chia sẻ bản ghi (OWD, Sharing Rules) của user đang chạy. Khai báo `inherited sharing` (D) cực kỳ thông minh: nó sẽ kế thừa chế độ sharing của class gọi nó (nếu LWC gọi trực tiếp thì nó hoạt động y chang `with sharing`), đảm bảo an toàn tuyệt đối và linh hoạt.

**❌ Tại sao đáp án sai:**
> **A.** Khai báo `public class` khơi khơi mà không ghi rõ sharing modifier thì mặc định Salesforce sẽ chạy ở chế độ **System Mode** (omni-present), nhìn thấy hết mọi bản ghi bất chấp user có quyền hay không. Rất nguy hiểm!
> **C.** `without sharing` là tuyên bố xanh rờn: 'Tôi coi thường quyền bảo mật của user!'. Class sẽ chạy ở System Mode và phớt lờ hoàn toàn các quy tắc chia sẻ bản ghi. Cook ngay!

**💡 Từ khóa ghi nhớ:** `Bảo mật bản ghi theo user trong Apex -> Auto dùng **with sharing** hoặc **inherited sharing**.`

---

## Câu 236

**🔵 A developer must create a DrawList class that provides capabilities defined in the Sortable and Drawable interfaces.
public interface Sortable{
void sort();
}
public interface Drawable{
void draw();
}
Which is the correct implementation?**

- **A.** public class DrawList implements Sortable, implements Drawable{ public void sort(){ /*implementation*/} public void draw(){ /*implementation*/} } ❌
- **B.** public class DrawList implements Sortable, Drawable{ public void sort(){ /*implementation*/} public void draw(){ /*implementation*/} } ✅
- **C.** public class DrawList extends Sortable, extends Drawable{ public void sort(){ /*implementation*/} public void draw(){ /*implementation*/} } ❌
- **D.** public class DrawList extends Sortable, Drawable { public void sort(){ /*implementation*/} public void draw(){ /*implementation*/} } ❌

**📝 Dịch tiếng Việt:**
> Developer cần tạo một class DrawList có các tính năng được định nghĩa sẵn trong hai Interface Sortable và Drawable. Cú pháp Apex nào dưới đây thực thi chuẩn chỉ?

**💬 Giải thích gốc (English):**
> Option A: Incorrect because you cannot use implements twice.
> Option C, D: Incorrect because you cannot use extends with interfaces; extends is used for classes.

**✅ Tại sao đáp án đúng:**
> Chọn **B: `public class DrawList implements Sortable, Drawable`**. Trong Apex (cũng giống Java), một class thông thường có thể hiện thực hóa (implement) nhiều Interface cùng lúc bằng cách dùng duy nhất từ khóa `implements`, theo sau là danh sách các Interface ngăn cách nhau bởi dấu phẩy. Và nhớ phải viết lại toàn bộ các method đã khai báo trong Interface nhé.

**❌ Tại sao đáp án sai:**
> **A.** Tự dưng viết lặp lại hai từ khóa `implements` độc lập (`implements Sortable, implements Drawable`) là sai cú pháp biên dịch nghiêm trọng. Trình biên dịch nó chửi cho đấy!
> **C.** Interface không thể dùng từ khóa `extends` ở đây vì `extends` chỉ dùng khi một class kế thừa một class khác, hoặc một interface kế thừa một interface khác thôi.
> **D.** Lại dùng sai từ khóa `extends` để hiện thực hóa interface. Không thể chấp nhận nổi!

**💡 Từ khóa ghi nhớ:** `Class implement nhiều Interface -> Dùng duy nhất **1 từ khóa implements** + ngăn cách bằng **dấu phẩy**.`

---

## Câu 237

**🔵 Which three options allow a developer to use custom styling in a Visualforce page? (Choose three.)**

- **A.** <apex:stylesheet> tag ✅
- **B.** Inline CSS ✅
- **C.** <apex:style>tag ❌
- **D.** <apex:stylesheets>tag ❌
- **E.** A static resource ✅

**📝 Dịch tiếng Việt:**
> Ba tùy chọn nào cho phép lập trình viên nhúng và sử dụng các định dạng CSS tùy chỉnh (custom styling) để trang trí cho một trang Visualforce? (Chọn 3)

**💬 Giải thích gốc (English):**
> <apex:stylesheet> tag: This tag is used to include external CSS stylesheets in your Visualforce page1.
> Inline CSS: You can directly include CSS styles within the <style> tags in your Visualforce page1.
> A static resource: You can upload CSS files as static resources and reference them in your Visualforce page using the <apex:stylesheet> tag.

**✅ Tại sao đáp án đúng:**
> Chọn **A (thẻ `<apex:stylesheet>`)**, **B (Inline CSS trong trang)** và **E (Static Resource)**. Đây là 3 con đường chính ngạch để mang CSS vào Visualforce: thẻ `<apex:stylesheet>` dùng để import file CSS từ ngoài hoặc Static Resource (A), viết trực tiếp các đoạn CSS inline trong thẻ `<style>` của HTML (B), và tải file CSS lên Static Resources rồi nhúng link sử dụng (E).

**❌ Tại sao đáp án sai:**
> **C.** Làm gì có thẻ nào tên là `<apex:style>` trong thư viện thành phần chuẩn của Visualforce. Đừng tự chế thẻ nha bro!
> **D.** Thẻ dạng số nhiều `<apex:stylesheets>` cũng là đồ giả, không hề tồn tại trong Salesforce.

**💡 Từ khóa ghi nhớ:** `Làm đẹp Visualforce -> Dùng **`<apex:stylesheet>`**, viết **Inline CSS**, hoặc gọi file CSS từ **Static Resource**.`

---

## Câu 238

**🔵 When a user edits the Postal Code on an Account, a custom Account text field named 'Timezone' must be updated based on the values in a PostalCodeToTimezone__c custom object. How should a developer implement this feature?**

- **A.** Build an Account Workflow Rule. ❌
- **B.** Build an Account Assignment Rule. ❌
- **C.** Build an Account custom Trigger. ✅
- **D.** Build an Account Approval Process. ❌

**📝 Dịch tiếng Việt:**
> Khi người dùng sửa Postal Code (Mã bưu điện) trên Account, một trường text custom tên 'Timezone' (Múi giờ) trên Account đó phải được tự động cập nhật dựa trên giá trị tra cứu từ một custom object khác là PostalCodeToTimezone__c. Dev nên triển khai tính năng này thế nào?

**💬 Giải thích gốc (English):**
> A trigger can handle the logic required to update the ‘Timezone’ field based on the Postal Code changes and the corresponding values in the PostalCodeToTimezone__c custom object.
> Build an Account Workflow Rule: Workflow rules are great for simple field updates, but they don’t support complex logic like querying another object (PostalCodeToTimezone__c) to determine the value of the ‘Timezone’ field.
> Build an Account Assignment Rule: Assignment rules are used to assign records to users or queues based on criteria. They don’t support updating fields based on related object data.
> Build an Account Approval Process: Approval processes are designed for managing record approvals and don’t support the kind of field update logic you’re looking for.

**✅ Tại sao đáp án đúng:**
> Chọn **C: Viết một custom Trigger trên Account** (Hoặc thời đại 2026 là dùng **Record-Triggered Flow**). Yêu cầu này bắt buộc chúng ta phải 'đi chợ' sang một đối tượng độc lập khác (PostalCodeToTimezone__c) để truy vấn dữ liệu (SOQL) dựa trên Postal Code vừa nhập rồi gán ngược lại Account. Việc tra cứu chéo đối tượng phức tạp này chỉ có Apex Trigger hoặc Record-Triggered Flow (Get Records) mới xử lý được.

**❌ Tại sao đáp án sai:**
> **A.** **Workflow Rule** siêu cùi bắp, chỉ hỗ trợ cập nhật trường trên chính nó hoặc bản ghi cha trong mối quan hệ Master-Detail, hoàn toàn không thể đi tra cứu dữ liệu từ một object độc lập bên ngoài được.
> **B.** **Assignment Rule** chỉ dùng để tự động gán chủ sở hữu (Owner) cho Lead hoặc Case mới tạo, không liên quan gì đến cập nhật múi giờ Account.
> **D.** **Approval Process** là quy trình gửi duyệt bản ghi, không dùng cho logic cập nhật trường tự động khi sửa đổi Postal Code thông thường.

**💡 Từ khóa ghi nhớ:** `Cập nhật dữ liệu bằng cách tra cứu từ một Object độc lập khác -> Chỉ có **Flow** hoặc **Trigger** làm được!`

---

## Câu 239

**🔵 Where can a developer identify the time taken by each process in a transaction using Developer Console log inspector?**

- **A.** Performance Tree tab under Stack Tree panel ❌
- **B.** Execution Tree tab under Stack Tree panel ❌
- **C.** Timeline tab under Execution Overview panel ✅
- **D.** Save Order tab under Execution Overview panel ❌

**📝 Dịch tiếng Việt:**
> Trong trình xem nhật ký (Log Inspector) của Developer Console, developer có thể xem chi tiết thời gian thực thi của từng tiến trình trong transaction ở tab nào?

**💬 Giải thích gốc (English):**
> The Timeline tab provides a visual representation of the time taken by each process. Select the Scale option that results in the most useful view.

**✅ Tại sao đáp án đúng:**
> Chọn **C: Tab Timeline dưới bảng Execution Overview**. Tab Timeline là một biểu đồ thanh ngang cực kỳ trực quan và sinh động! Nhìn vào đó, bạn sẽ biết chính xác từng phần của hệ thống (Apex code, Database DML, Workflow rules, Validation rules) đã ngốn bao nhiêu mili-giây và chiếm bao nhiêu phần trăm tổng thời gian chạy.

**❌ Tại sao đáp án sai:**
> **A.** **Performance Tree** hiển thị cây phân cấp cuộc gọi các phương thức và thời gian của từng hàm cụ thể chứ không hiển thị tổng quan dòng thời gian của các tiến trình hệ thống.
> **B.** **Execution Tree** tương tự Performance Tree, tập trung vào sơ đồ cây thực thi hàm chứ không phân bổ theo dòng thời gian tổng quát.
> **D.** **Save Order** hiển thị trình tự ghi bản ghi xuống database (Save Order of Execution) chứ không có thống kê thời gian chạy thực tế của các tiến trình.

**💡 Từ khóa ghi nhớ:** `Xem phân bổ thời gian chạy của toàn bộ các tiến trình -> Cứ tab **Timeline** mà chọn.`

---

## Câu 240

**🔵 A developer has the controller class below.
Public with sharing class myFooController{
public integer prop{get; private set;}
}
Which code block will run successfully in an execute anonymous window?**

- **A.** myFooController m = new myFooController(); System.assert(m.prop != null); ❌
- **B.** myFooController m = new myFooController(); System.assert(m.prop == 0); ❌
- **C.** myFooController m = new myFooController(); System.assert(m.prop == null); ✅
- **D.** myFooController m = new myFooController(); System.assert(m.prop == 1); ❌

**📝 Dịch tiếng Việt:**
> Cho class controller sau: [Code myFooController]. Khối mã lệnh nào dưới đây sẽ chạy thành công mỹ mãn không tì vết khi thực thi trong cửa sổ Execute Anonymous?

**💬 Giải thích gốc (English):**
> The value of prop variable is never defined in the constructor, so its default value is null.

**✅ Tại sao đáp án đúng:**
> Chọn **C: `myFooController m = new myFooController(); System.assert(m.prop == null);`**. Trong Apex, tất cả các biến số (bao gồm cả Integer, Decimal...) nếu khai báo khơi khơi mà không được gán bất kỳ giá trị khởi tạo nào thì mặc định giá trị của chúng sẽ là **`null`**. Do đó, assert `prop == null` chắc chắn đúng 100%!

**❌ Tại sao đáp án sai:**
> **A.** Assert `prop != null` sẽ ném ra lỗi `AssertException` vì thực tế `prop` đang bằng null.
> **B.** Apex không giống C# hay Java, nó không tự động gán giá trị mặc định bằng `0` cho kiểu số. Nên assert `prop == 0` là sai bét và ném lỗi ngay.
> **D.** Không có cơ sở nào để `prop` bằng `1` cả, assert này chắc chắn vỡ trận.

**💡 Từ khóa ghi nhớ:** `Apex rất sòng phẳng: Biến không khởi tạo giá trị -> Mặc định luôn bằng **null**!`

---

## Câu 241

**🔵 Which three statements are true regarding trace flags? (Choose three.)**

- **A.** Setting trace flags automatically cause debug logs to be generated. ❌
- **B.** Logging levels override trace flags. ❌
- **C.** Trace flags override logging levels. ✅
- **D.** If active trace flags are not set, Apex tests execute with default logging levels. ✅
- **E.** Trace flags can be set in the Developer Console, Setup, or using the Tooling API. ✅

**📝 Dịch tiếng Việt:**
> Ba phát biểu nào sau đây là ĐÚNG khi nói về Trace Flags (cờ theo dõi log) trong Salesforce? (Chọn 3)

**✅ Tại sao đáp án đúng:**
> Chọn **C**, **D** và **E**. Vì:
- **Trace flags** có mức độ ưu tiên tối thượng, nó sẽ ghi đè (override) lên các cấu hình Logging Levels mặc định của bạn (C).
- Nếu bạn không cắm cái Trace flag nào đang chạy, thì các bài test Apex (Apex tests) khi chạy sẽ tự động sử dụng mức logging mặc định của hệ thống (D).
- Bạn có thể tha hồ thiết lập Trace flags ở nhiều nơi: trong Developer Console, trong mục Setup, hoặc bắn qua Tooling API đều nuột (E).

**❌ Tại sao đáp án sai:**
> **A.** Bật trace flag khơi khơi không tự dưng sinh ra debug log đâu bro! Phải có ai đó thực hiện thao tác (User action) hoặc có code chạy qua thì hệ thống mới thèm ghi log.
> **B.** Sai bét nhè! Trace flags to đầu hơn, nó ghi đè Logging levels chứ không bao giờ có chuyện bị Logging levels đè đầu cưỡi cổ.

**💡 Từ khóa ghi nhớ:** `Trace Flags: Thích cắm ở đâu cũng được (Setup/Dev Console/Tooling API) và luôn **ghi đè (override) Logging Levels**!`

---

## Câu 242

**🔵 How can a developer check the test coverage of Autolaunched Flows before deploying them in a change set?**

- **A.** Use the Flow Properties page. ❌
- **B.** Use the ApexTestResult class. ❌
- **C.** Use SOQL and the Tooling API. ✅
- **D.** Use the Code Coverage Setup page. ❌

**📝 Dịch tiếng Việt:**
> Làm sao để anh em dev check xem cái Flow tự động (Autolaunched Flow) của mình đã đạt bao nhiêu % test coverage trước khi gói ghém đem đi deploy bằng Change Set?

**💬 Giải thích gốc (English):**
> Developers can use SOQL queries along with the Tooling API to check the test coverage of autolaunched Flows. The FlowTestCoverage object in the Tooling API provides information about the test coverage for flows.

**✅ Tại sao đáp án đúng:**
> Chọn **C: Sử dụng SOQL kết hợp Tooling API**. Khác với Apex code có bảng hiển thị coverage đẹp đẽ ngoài giao diện, test coverage của Flow hơi bị 'ẩn dật'. Bạn bắt buộc phải dùng **Tooling API** (hoặc chạy câu SOQL truy vấn vào các đối tượng hệ thống như `FlowTestCoverage`) thì mới lôi đầu nó ra ánh sáng được.

**❌ Tại sao đáp án sai:**
> **A.** **Flow Properties page** chỉ hiển thị mấy cái thông tin metadata cơ bản như Version, Status, API Version... chứ lấy đâu ra số liệu test coverage cho bạn xem.
> **B.** Lớp `ApexTestResult` dùng để xem kết quả chạy test của các class Apex chứ không hỗ trợ đo đạc coverage cho Flow.
> **D.** Không hề tồn tại trang cấu hình nào tên là **Code Coverage Setup page** trong hệ thống Salesforce cả, đồ fake đó bro!

**💡 Từ khóa ghi nhớ:** `Muốn check Test Coverage của Flow -> Nhớ ngay đến **Tooling API** và **SOQL**.`

---

## Câu 243

**🔵 A developer has the following requirements: Calculate the total amount on an Order. Calculate the line amount for each Line Item based on quantity selected and price. Move Line Items to a different Order if a Line Item is not in stock. Which relationship implementation supports these requirements on its own?**

- **A.** Order has a re-parentable master-detail field to Line Item. ❌
- **B.** Order has a re-parentable lookup field to Line Item. ❌
- **C.** Line Item has a re-parentable lookup field to Order. ❌
- **D.** Line Item has a re-parentable master-detail field to Order. ✅

**📝 Dịch tiếng Việt:**
> Developer có các yêu cầu sau:
1. Tính tổng tiền (total amount) trên Order.
2. Tính số tiền cho từng Line Item (line amount) dựa trên số lượng và giá.
3. Cho phép di chuyển Line Items sang một Order khác nếu món hàng đó hết kho.
Loại quan hệ (relationship) nào dưới đây có thể tự cân hết đống yêu cầu này?

**💬 Giải thích gốc (English):**
> By default, records can’t be reparented in master-detail relationships. Administrators can, however, allow child records in master-detail relationships on custom objects to be reparented to different parent records by selecting the Allow reparenting option in the master-detail relationship definition.

**✅ Tại sao đáp án đúng:**
> Chọn **D: Line Item có một trường Master-Detail cho phép đổi cha (re-parentable) trỏ đến Order**. Vì:
- Để tính tổng tiền từ các bản ghi con lên cha Order một cách no-code, ta bắt buộc phải dùng trường **Roll-up Summary** (chỉ hỗ trợ trong mối quan hệ Master-Detail). Trường Master-Detail phải nằm ở đối tượng con `Line Item` trỏ lên cha `Order`.
- Để di chuyển Line Items sang Order khác, ta chỉ cần bật tính năng **'Allow reparenting'** (cho phép đổi cha) trên trường Master-Detail đó. Quá hoàn hảo!

**❌ Tại sao đáp án sai:**
> **A.** Đặt trường Master-Detail ở phía Order trỏ xuống Line Item làm đảo lộn cấu trúc cha-con. Cha không thể chứa trường Master-Detail trỏ tới con được.
> **B.** Sai chiều thiết kế tương tự A.
> **C.** Nếu dùng quan hệ **Lookup** thì bạn sẽ không tài nào dùng được trường **Roll-up Summary** trên Order để tính tổng tiền no-code được. Lúc đó lại phải viết code trigger cồng kềnh.

**💡 Từ khóa ghi nhớ:** `Tính tổng con lên cha (Roll-up Summary) + Cho phép đổi cha -> **Master-Detail** ở con + bật **re-parentable**.`

---

## Câu 244

**🔵 AW Computing tracks order information in custom objects called Order__c and Order_Line__c. Currently, all shipping information is stored in the Order__c object. The company wants to expand its order application to support split shipments so that any number of Order_Line__c records on a single Order__c can be shipped to different locations. What should a developer add to fulfill this requirement?**

- **A.** Order_Shipment_Group__c object and master-detail field on Order__c ❌
- **B.** Order_Shipment_Group__c object and master-detail fields to Order__c and Order_Line__c ✅
- **C.** Order_Shipment_Group__c object and master-detail field on Order_Line__c ❌
- **D.** Order_Shipment_Group__c object and master-detail field on Order_Shipment_Group__c ❌

**📝 Dịch tiếng Việt:**
> AW Computing theo dõi thông tin đơn hàng trong 2 custom object là Order__c và Order_Line__c. Hiện tại, toàn bộ thông tin giao hàng đều nằm ở Order__c. Nay công ty muốn nâng cấp để hỗ trợ Split Shipments (giao hàng chia làm nhiều đợt/địa chỉ khác nhau), sao cho các Order_Line__c trong cùng một đơn hàng có thể được ship tới các địa điểm khác nhau. Developer nên thêm gì?

**✅ Tại sao đáp án đúng:**
> Chọn **B: Tạo object Order_Shipment_Group__c và các trường master-detail trỏ tới cả Order__c và Order_Line__c**. Ý tưởng là tạo ra một đối tượng trung gian `Order_Shipment_Group__c` (đại diện cho mỗi đợt giao hàng). Đối tượng này sẽ làm cầu nối: nó liên kết với `Order__c` cha để biết thuộc đơn hàng nào, và liên kết với `Order_Line__c` con để biết những sản phẩm nào sẽ đi chung đợt ship đó. Cấu trúc dữ liệu cực kỳ mạch lạc!

**❌ Tại sao đáp án sai:**
> **A.** Chỉ tạo group và trỏ Master-detail từ Order về Group thì không giải quyết được vấn đề phân chia chi tiết cho từng Line Item con.
> **C.** Nếu chỉ có quan hệ giữa Group và Line Item thì cấu trúc dữ liệu bị mất liên kết trực tiếp và quản lý từ Order cha.
> **D.** Tự trỏ về chính mình (self-relationship) là một pha tấu hài cực mạnh, không liên quan gì đến yêu cầu gom nhóm giao hàng.

**💡 Từ khóa ghi nhớ:** `Chia đợt ship (Split Shipment) cho các sản phẩm con -> Tạo object trung gian **Shipment Group** liên kết cả **Order** và **Order Line**.`

---

## Câu 245

**🔵 Which two Apex data types can be used to reference a Salesforce record ID dynamically? (Choose two.)**

- **A.** ENUM ❌
- **B.** sObject ✅
- **C.** External ID ❌
- **D.** String ✅

**📝 Dịch tiếng Việt:**
> Hai kiểu dữ liệu (data types) nào trong Apex có thể dùng để lưu trữ và tham chiếu động tới một Salesforce Record ID? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> Chọn **B (sObject)** và **D (String)**.
- **sObject** (B) là lớp cha của mọi đối tượng trong Salesforce (như Account, Contact...). Bạn có thể gán bất kỳ bản ghi nào vào một biến sObject chung chung và dùng `variable.Id` để lấy ID của nó một cách linh hoạt.
- **String** (D) là kiểu chuỗi ký tự. Salesforce ID thực chất cũng chỉ là một chuỗi 15 hoặc 18 ký tự, nên bạn hoàn toàn có thể lưu nó vào biến String và Salesforce sẽ tự động ép kiểu sang kiểu dữ liệu `Id` khi cần thiết.

**❌ Tại sao đáp án sai:**
> **A.** **ENUM** là kiểu dữ liệu chứa một danh sách hằng số cố định do bạn tự định nghĩa (ví dụ: `Season {SPRING, SUMMER}`), không dùng để chứa ID động của record được.
> **C.** **External ID** là một thuộc tính cấu hình của một trường (Field Attribute) trong database để map dữ liệu bên ngoài, chứ bản thân nó không phải là một kiểu dữ liệu (Data Type) trong ngôn ngữ Apex.

**💡 Từ khóa ghi nhớ:** `Lưu ID bản ghi linh hoạt trong code Apex -> Chỉ có **sObject** hoặc **String** (chuỗi) cân được.`

---

## Câu 246

**🔵 A developer is debugging the following code to determine why Accounts are not being created. List<Account> accts = getAccounts(); //getAccounts implemented else where Database.insert(accts, false); How should the code be altered to help debug the issue?**

- **A.** Change the DML statement to insert method. ❌
- **B.** Collect the insert method return value in a SaveResult record. ✅
- **C.** Set the second insert method parameter to TRUE. ❌
- **D.** Add a try/catch around the insert method. ❌

**📝 Dịch tiếng Việt:**
> Developer đang debug đoạn code dưới đây để tìm xem tại sao đống Account không được tạo:
`List<Account> accts = getAccounts();`
`Database.insert(accts, false);`
Nên sửa code thế nào để lôi được nguyên nhân lỗi ra ánh sáng?

**💬 Giải thích gốc (English):**
> SaveResult Handling: Using Database.SaveResult[] allows you to check each insert operation’s success and log any errors.
> List<Account> accts = getAccounts(); //getAccounts implemented else where
> Database.SaveResult[] results = Database.insert(accts, false);
> // Loop through the results to check for errors
> for (Database.SaveResult result : results) {
> if (!result.isSuccess()) {
> // Log the error details
> System.debug('Error inserting account: ' + result.getErrors()[0].getMessage());
> }
> }

**✅ Tại sao đáp án đúng:**
> Chọn **B: Hứng giá trị trả về của phương thức insert vào một mảng SaveResult**.
Cú pháp chuẩn sẽ là: `Database.SaveResult[] srList = Database.insert(accts, false);`.
Khi bạn truyền tham số thứ hai là `false` (allOrNone = false), Salesforce sẽ chạy chế độ 'lỗi đứa nào đứa đấy chịu'. Những bản ghi đúng vẫn được insert, những bản ghi sai sẽ bị bỏ qua và hệ thống **không hề ném ra bất kỳ Exception nào** để báo lỗi. Bạn bắt buộc phải hứng kết quả vào `SaveResult[]` rồi duyệt qua đó để in ra lý do bản ghi nào bị fail. Rất sòng phẳng!

**❌ Tại sao đáp án sai:**
> **A.** Đổi sang lệnh DML `insert accts;` thông thường sẽ làm dừng và rollback toàn bộ transaction ngay khi gặp bản ghi lỗi đầu tiên, phá vỡ logic xử lý chấp nhận lỗi một phần.
> **C.** Đặt tham số thứ hai thành `true` sẽ bắt hệ thống rollback toàn bộ nếu có lỗi, nhưng nó cũng chỉ ném ra một Exception chung chung chứ không giúp bạn duyệt chi tiết từng lỗi của từng record một cách thanh lịch.
> **D.** Bọc khối `try/catch` ở đây vô tác dụng 100%! Vì hàm `Database.insert(accts, false)` không bao giờ thèm ném ra Exception thì lấy cái gì cho `catch` bắt?

**💡 Từ khóa ghi nhớ:** `Xài `Database.insert(..., false)` -> Luôn hứng kết quả bằng **`Database.SaveResult[]`** để soi lỗi.`

---

## Câu 247

**🔵 Why would a developer consider using a custom controller over a controller extension?**

- **A.** To increase the SOQL query governor limits. ❌
- **B.** To implement all of the logic for a page and bypass default Salesforce functionality ❌
- **C.** To leverage built-in functionality of a standard controller ✅
- **D.** To enforce user sharing settings and permissions ❌

**📝 Dịch tiếng Việt:**
> Tại sao lập trình viên nên cân nhắc sử dụng một Custom Controller độc lập thay vì sử dụng một Controller Extension mở rộng cho trang Visualforce?

**✅ Tại sao đáp án đúng:**
> Đáp án chính thức trong ngân hàng đề thi Salesforce đôi khi ghi nhận là **C**, nhưng về mặt lý thuyết kỹ thuật chính xác, Custom Controller được dùng khi bạn muốn **bypass hoàn toàn tính năng mặc định** của Salesforce và tự viết 100% logic (tức là đáp án **B**). Controller Extension mới là thứ dùng để **tận dụng (leverage) tính năng của Standard Controller**. Đi thi thì bạn cứ cẩn thận với câu này nhé!

**❌ Tại sao đáp án sai:**
> **A.** Sử dụng custom controller không hề giúp tăng giới hạn SOQL query governor limits cứng của transaction.
> **C.** Để tận dụng chức năng có sẵn của Standard Controller, lập trình viên bắt buộc phải dùng Controller Extension chứ không dùng Custom Controller độc lập.
> **D.** Custom Controller không tự động áp đặt chia sẻ bản ghi trừ khi bạn khai báo tường minh với từ khóa `with sharing`.
> **B.** Viec lam chu toan bo logic va bo qua chuc nang mac dinh la ly do de su dung Custom Controller doc lap (khong can Standard Controller). Controller Extension chi la mo rong them logic ben canh Standard Controller, khong the override hoan toan hanh vi mac dinh.

**💡 Từ khóa ghi nhớ:** `Custom Controller -> Tự viết 100% logic, bypass tính năng chuẩn. Controller Extension -> Tái sử dụng/mở rộng Standard Controller.`

---

## Câu 248

**🔵 Which approach should be used to provide test data for a test class?**

- **A.** Query for existing records in the database. ❌
- **B.** Execute anonymous code blocks that create data. ❌
- **C.** Use a test data factory class to create test data. ✅
- **D.** Access data in @TestVisible class variables. ❌

**📝 Dịch tiếng Việt:**
> Phương pháp chuẩn mực và chuẩn cơm mẹ nấu nhất nào nên được áp dụng để cung cấp dữ liệu test mẫu cho một Apex Test Class?

**💬 Giải thích gốc (English):**
> Using a Test Data Factory or @TestSetup method is generally considered best practice as it ensures tests are isolated, repeatable, and maintainable.

**✅ Tại sao đáp án đúng:**
> Chọn **C: Sử dụng một Test Data Factory class chuyên biệt để tạo dữ liệu test** (ví dụ `TestDataFactory.createAccounts(...)`). Đây là best practice đỉnh chóp của Salesforce! Thằng này giúp bạn gom toàn bộ logic tạo bản ghi test ảo vào một nơi, tha hồ tái sử dụng ở nhiều test class khác nhau. Mai sau Admin có thêm Validation Rule hay Field bắt buộc mới, bạn chỉ cần sửa đúng 1 chỗ trong Factory class là xong, đỡ mất công đi sửa từng test class.

**❌ Tại sao đáp án sai:**
> **A.** Query dữ liệu thật có sẵn trong database là tối kỵ! Mặc định unit test chạy ở chế độ cô lập (`SeeAllData=false`). Bạn query database thật thì nó sẽ trả về kết quả rỗng tuếch, test class fail lòi mắt ngay.
> **B.** **Execute Anonymous** chỉ dùng để chạy code thủ công, chạy một lần rồi thôi ngoài Developer Console, chả liên quan gì đến việc tự động hóa tạo data khi chạy test class cả.
> **D.** Khai báo biến tĩnh gắn `@TestVisible` chỉ giúp test class 'soi' được các biến private bên trong class chính, chứ nó không hề tạo hay chèn bản ghi vật lý nào vào database để test trigger cả.

**💡 Từ khóa ghi nhớ:** `Best Practice tạo data test trong Salesforce -> Luôn gọi **Test Data Factory class**.`

---

## Câu 249

**🔵 A developer created these three roll-up summary fields on the custom object Project__c: - Total_Timesheets__c - Total_Approved_Timesheets__c - Total_Rejected_Timesheet__c The developer is asked to create a new field that shows the ratio between rejected and approved timesheets for a given project. The developer is asked to create a new field that shows the ratio between rejected and approved timesheets for a given project.
What are two benefits of choosing a formula field instead of an Apex trigger to fulfill the request? (Choose two.)**

- **A.** A test class will validate the formula field during deployment. ❌
- **B.** A formula field will trigger existing automation when deployed. ❌
- **C.** Using a formula field reduces maintenance overhead. ✅
- **D.** A formula field will calculate the value retroactively for existing records. ✅

**📝 Dịch tiếng Việt:**
> Developer đã tạo 3 trường Roll-up Summary trên custom object Project__c: tổng số Timesheets, số Timesheets được duyệt, và số Timesheets bị từ chối. Giờ sếp bắt tạo thêm 1 trường mới để hiển thị tỷ lệ giữa Timesheets bị từ chối và được duyệt. Hai lợi ích của việc chọn trường công thức (Formula Field) thay vì viết Apex trigger là gì? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> Chọn **C** và **D**.
- **Formula field** (trường công thức) là tính năng no-code chuẩn chỉnh, giúp bạn **giảm thiểu tối đa chi phí bảo trì** (C). Không cần viết code Apex, không cần viết test class gánh coverage, sướng vãi chưởng!
- Ngay khi bạn vừa tạo xong trường công thức, Salesforce sẽ tự động **tính toán hồi tố (retroactively)** cho toàn bộ các bản ghi đã tồn tại từ trước trong hệ thống (D). Bạn không cần phải viết script chạy bằng tay để cập nhật lại data cũ.

**❌ Tại sao đáp án sai:**
> **A.** Trình deploy của Salesforce không yêu cầu hay thực hiện chạy bất kỳ test class nào để validate trường công thức cả. Trường này no-code nên an toàn tuyệt đối.
> **B.** Trường công thức khi được tính toán lại **không hề kích hoạt** (trigger) các tiến trình tự động hóa khác (như Flow hay Workflow) chạy lại, do đó đáp án này là sai bét.

**💡 Từ khóa ghi nhớ:** `Lợi ích tối thượng của Formula Field -> **Giảm công sức viết code bảo trì** (C) + **Tự động tính toán dữ liệu cũ đã có** (D).`

---

## Câu 250

**🔵 A developer needs to update an unrelated object when a record gets saved. Which two trigger types should the developer create? (Choose two.)**

- **A.** after insert ✅
- **B.** before update ❌
- **C.** before insert ❌
- **D.** after update ✅

**📝 Dịch tiếng Việt:**
> Developer cần cập nhật một đối tượng KHÔNG có quan hệ gì liên quan (unrelated object) mỗi khi một bản ghi được lưu thành công. Lập trình viên nên tạo Trigger ở hai sự kiện nào? (Chọn 2)

**💬 Giải thích gốc (English):**
> To update an unrelated object when a record gets saved, the developer should create the following two trigger types:
> After Insert Trigger: This trigger runs after a new record is inserted into the database. It allows the developer to perform actions on unrelated objects based on the newly inserted record.
> After Update Trigger: This trigger runs after an existing record is updated. It enables the developer to update unrelated objects based on changes to the original record.

**✅ Tại sao đáp án đúng:**
> Chọn **A (after insert)** và **D (after update)**. Khi bạn cần cập nhật một đối tượng khác độc lập, bạn bắt buộc phải chờ cho bản ghi hiện tại được lưu an toàn xuống database và có ID chính thức (ở sự kiện **`after`**). Lúc này, nếu có lỗi xảy ra ở đối tượng kia thì toàn bộ transaction mới rollback đồng bộ được, đảm bảo tính toàn vẹn dữ liệu.

**❌ Tại sao đáp án sai:**
> **B.** **before update** chạy trước khi lưu bản ghi hiện tại xuống database. Sự kiện này chỉ nên dùng để thay đổi giá trị của chính bản ghi đó chứ mang đi cập nhật object khác là đi ngược lại thiết kế chuẩn (Order of Execution), dễ gây lỗi race condition.
> **C.** **before insert** chạy khi bản ghi hiện tại chưa hề được ghi vào DB và chưa có ID chính thức. Lấy ID đâu ra mà đi map dữ liệu sang đối tượng khác hả bro?

**💡 Từ khóa ghi nhớ:** `Cập nhật đối tượng khác (con/bản ghi liên quan/không liên quan) -> Auto chọn sự kiện **AFTER** (after insert / after update)!`

---

## Câu 251

**🔵 Which feature allows a developer to create test records for use in test classes?**

- **A.** Documents ❌
- **B.** WebServiceTests ❌
- **C.** HttpCalloutMocks ❌
- **D.** Static Resources ✅

**📝 Dịch tiếng Việt:**
> Tính năng nào cho phép lập trình viên dễ dàng khởi tạo hàng loạt bản ghi dữ liệu test mẫu lớn từ file để dùng trong các test classes?

**✅ Tại sao đáp án đúng:**
> Chọn **D: Static Resources**. Cách nạp data test đỉnh nhất là bạn chuẩn bị sẵn một file CSV chứa đầy đủ thông tin các bản ghi mẫu, upload nó lên **Static Resource**, rồi dùng lệnh `Test.loadData()` trong code test để Salesforce tự động parse và nạp thẳng vào DB ảo.

**❌ Tại sao đáp án sai:**
> **A.** **Documents** là tính năng lưu trữ file đời cổ của Salesforce Classic, không có bất kỳ API hay phương thức nào hỗ trợ nạp dữ liệu tự động vào Unit Test cả.
> **B.** `WebServiceTests` là một khái niệm tự chế, không tồn tại tính năng hay lớp nào tên thế này để tạo record.
> **C.** `HttpCalloutMocks` dùng để giả lập phản hồi của API cuộc gọi ngoài (HTTP Callout) chứ không có nhiệm vụ chèn bản ghi dữ liệu test thông thường.

**💡 Từ khóa ghi nhớ:** `Nạp data test hàng loạt từ CSV -> Upload lên **Static Resources** rồi gọi **Test.loadData()**.`

---

## Câu 252

**🔵 An org tracks customer orders on an Order object and the line items of an Order on the Line Item object. The Line Item object has a Master/Detail relationship to the Order object. A developer has a requirement to calculate the order amount on an Order and the line amount on each Line Item based on quantity and price. What is the correct implementation?**

- **A.** Write a single before trigger on the Line Item that calculates the item amount and updates the order amount on the Order. ❌
- **B.** Write a process on the Line Item that calculates the item amount and order amount and updates the fields on the Line Item and the Order. ❌
- **C.** Implement the line amount as a numeric formula field and the order amount as a roll-up summary field. ✅
- **D.** Implement the line amount as a currency field and the order amount as a SUM formula field. ❌

**📝 Dịch tiếng Việt:**
> Một tổ chức theo dõi các đơn hàng của khách hàng trên đối tượng Order và các dòng sản phẩm của Order trên đối tượng Line Item. Đối tượng Line Item có mối quan hệ Master-Detail với đối tượng Order. Một lập trình viên có yêu cầu tính toán số tiền đơn hàng trên Order và số tiền trên mỗi Line Item dựa trên số lượng và giá cả. Triển khai nào sau đây là đúng?

**✅ Tại sao đáp án đúng:**
> Chọn **C: Triển khai số tiền trên Line Item dạng trường công thức số (numeric formula field) và số tiền trên Order dưới dạng trường Roll-up Summary**. Vì:
- Số tiền trên mỗi Line Item = Số lượng * Đơn giá -> Sử dụng **Formula Field** (trường công thức) là giải pháp no-code hoàn hảo.
- Tổng số tiền trên Order = Tổng số tiền của các Line Items con -> Vì quan hệ là Master-Detail, ta sử dụng trường **Roll-up Summary** trên Order để tự động tính toán tổng số tiền của các bản ghi con một cách cực kỳ mượt mà.

**❌ Tại sao đáp án sai:**
> **A.** Viết Trigger ở sự kiện before để tính toán rồi tự update là phương án code cồng kềnh, thừa thãi và tốn tài nguyên bảo trì vô ích khi no-code xử lý ngon lành.
> **B.** Dùng Process Builder để tính toán tương tự A, cồng kềnh và dễ gây trễ giao dịch hoặc lỗi khóa bản ghi (record locking).
> **D.** Không tồn tại khái niệm 'SUM formula field' để cộng dồn các bản ghi con lên bản ghi cha trong Salesforce.

**💡 Từ khóa ghi nhớ:** `Tính toán toán học trong record con -> Dùng **Formula**. Tổng hợp con lên cha Master-Detail -> Dùng **Roll-up Summary**.`

---

## Câu 253

**🔵 A Lightning component has a wired property, searchResults, that stores a list of Opportunities. Which definition of the Apex method, to which the searchResults property is wired, should be used?**

- **A.** @AuraEnabled(cacheable = false) public static List<Opportunity> search(String term) { /*implementation*/ } ❌
- **B.** @AuraEnabled(cacheable = false) public List<Opportunity> search(String term) { /*implementation*/ } ❌
- **C.** @AuraEnabled(cacheable = true) public static List<Opportunity> search(String term) { /*implementation*/ } ✅
- **D.** @AuraEnabled(cacheable = true) public List<Opportunity> search(String term) { /*implementation*/ } ❌

**📝 Dịch tiếng Việt:**
> Một Lightning component có một wired property tên là searchResults để chứa danh sách Opportunity. Cấu hình method Apex nào dưới đây là chuẩn để kết nối (wire) với property này?

**💬 Giải thích gốc (English):**
> To improve runtime performance, annotate the Apex method with @AuraEnabled(cacheable=true), which caches the method results on the client. To set cacheable=true, a method must only get data, it can’t mutate (change) data.
> To use @wire to call an Apex method, you must set cacheable=true.

**✅ Tại sao đáp án đúng:**
> Chọn **C: `@AuraEnabled(cacheable = true) public static List<Opportunity> search(String term)`**. Để một method Apex có thể kết nối thông qua decorator `@wire` trong LWC, nó bắt buộc phải thỏa mãn 2 điều kiện cứng:
1. Phải có annotation **`@AuraEnabled(cacheable=true)`** để Salesforce bật tính năng lưu cache dữ liệu tối ưu ở trình duyệt.
2. Phải là phương thức tĩnh **`static`**.

**❌ Tại sao đáp án sai:**
> **A.** Thiếu thuộc tính `cacheable=true` nên không thể sử dụng với `@wire` được. Bạn chỉ có thể gọi phương thức này thủ công (Imperative call) thôi.
> **B.** Vừa thiếu `static` vừa thiếu `cacheable=true` thì LWC chịu chết không kết nối được.
> **D.** Thiếu từ khóa `static` làm phương thức trở thành instance method. LWC chỉ có thể gọi được static method của Apex thôi, cook ngay!

**💡 Từ khóa ghi nhớ:** `Muốn `@wire` kết nối với Apex -> Phương thức bắt buộc phải là **`static`** và có **`cacheable=true`**!`

---

## Câu 254

**🔵 A lead developer creates an Apex interface called Laptop. Consider the following code snippet: public class SilverLaptop{//code implementation} How can a developer use the Laptop interface within the SilverLaptop class?**

- **A.** public class SilverLaptop implements Laptop{} ✅
- **B.** @Extends(class=Laptop) public class SilverLaptop{} ❌
- **C.** public class SilverLaptop extends Laptop{} ❌
- **D.** @Interface(class=Laptop) public class SilverLaptop{} ❌

**📝 Dịch tiếng Việt:**
> Lead Developer tạo ra một Apex Interface tên là Laptop. Làm thế nào để sử dụng và hiện thực hóa (implement) cái interface này bên trong class SilverLaptop?

**💬 Giải thích gốc (English):**
> In Apex (similar to Java), the implements keyword is used to indicate that a class will implement an interface.
> public class SilverLaptop implements Laptop {
> // code implementation
> }

**✅ Tại sao đáp án đúng:**
> Chọn **A: `public class SilverLaptop implements Laptop{}`**. Trong Apex (và hầu hết các ngôn ngữ OOP), để một lớp thông thường cam kết thực hiện đầy đủ các phương thức đã khai báo ký mẫu trong một Interface, ta dùng từ khóa **`implements`**.

**❌ Tại sao đáp án sai:**
> **B.** Cú pháp `@Extends(...)` là đồ tự chế, hoàn toàn không tồn tại trong vũ trụ Salesforce Apex.
> **C.** Từ khóa `extends` chỉ dùng khi một class kế thừa một class cha khác (kế thừa đơn), hoặc một interface kế thừa interface khác chứ không dùng để liên kết class với interface được.
> **D.** Chú thích `@Interface(...)` cũng là một pha tấu hài vô hại, không có giá trị biên dịch.

**💡 Từ khóa ghi nhớ:** `Hiện thực hóa Interface -> Chắc chắn dùng từ khóa **implements**!`

---

## Câu 255

**🔵 A method is passed a list of generic sObjects as a parameter. What should the developer do to determine which object type (Account, Lead, or Contact, for example) to cast each sObject?**

- **A.** Use the first three characters of the sObject ID to determine the sObject type. ❌
- **B.** Use the getSObjectType method on each generic sObject to retrieve the sObject token. ✅
- **C.** Use the getSObjectName method on the sObject class to get the sObject name. ❌
- **D.** Use a try-catch construct to cast the sObject into one of the three sObject types. ❌

**📝 Dịch tiếng Việt:**
> Một phương thức nhận đầu vào là một danh sách sObject chung chung (List<sObject>). Developer nên làm gì để biết chính xác kiểu đối tượng cụ thể của từng bản ghi (ví dụ là Account, Lead hay Contact) để thực hiện ép kiểu (cast) dữ liệu cho an toàn?

**💬 Giải thích gốc (English):**
> To determine the specific object type (e.g., Account, Lead, Contact) of each sObject in a list, the developer can use the getSObjectType method. This method returns the Schema.SObjectType of the sObject, which can then be used to identify the object type.

**✅ Tại sao đáp án đúng:**
> Chọn **B: Sử dụng phương thức `getSObjectType()` trên mỗi sObject**. Hàm này trả về một đối tượng Token `Schema.SObjectType` đại diện cho kiểu dữ liệu thực tế của bản ghi (ví dụ: `obj.getSObjectType() == Account.sObjectType`). Đây là cách chính thống, an toàn tuyệt đối và chạy nhanh nhất.

**❌ Tại sao đáp án sai:**
> **A.** Mặc dù 3 ký tự đầu của ID Salesforce có thể dùng để phân biệt đối tượng (ví dụ: 001 là Account, 003 là Contact), nhưng việc hardcode tiền tố ID này là một 'anti-pattern' cực kỳ nguy hiểm, bị Salesforce cấm tiệt vì nó có thể thay đổi hoặc không hoạt động với các custom object.
> **C.** Không hề tồn tại phương thức nào tên là `getSObjectName()` trên lớp sObject của Apex cả.
> **D.** Dùng khối `try-catch` để ép kiểu bừa bãi (blind casting) cho đến khi trúng thì thôi là một giải pháp cực kỳ 'gà', làm chậm CPU và tốn tài nguyên hệ thống vô ích.

**💡 Từ khóa ghi nhớ:** `Xác định kiểu sObject động -> Auto gọi hàm **`getSObjectType()`**.`

---

## Câu 256

**🔵 What are two use cases for executing Anonymous Apex code? (Choose two.)**

- **A.** To run a batch Apex class to update all Contacts ✅
- **B.** To schedule an Apex class to run periodically ✅
- **C.** To delete 15,000 inactive Accounts in a single transaction after a deployment ❌
- **D.** To add unit test code coverage to an org ❌

**📝 Dịch tiếng Việt:**
> Hai trường hợp nào là phù hợp để sử dụng tính năng thực thi mã Apex ẩn danh (Execute Anonymous Apex)? (Chọn 2)

**💬 Giải thích gốc (English):**
> To run a batch Apex class to update all Contacts
> To delete 15,000 inactive Accounts in a single transaction after a deployment
> These use cases are suitable for Anonymous Apex because it allows developers to quickly execute code snippets for tasks such as data manipulation or batch processing without needing to deploy the code to the org.

**✅ Tại sao đáp án đúng:**
> Chọn **A (Chạy một lớp Batch Apex để cập nhật danh bạ Contact)** và **B (Đặt lịch chạy định kỳ cho một lớp Apex Schedulable)**. Cửa sổ Execute Anonymous cực kỳ hoàn hảo để thực hiện các lệnh chạy một lần như kích hoạt chạy nhanh một mảng xử lý Batch Apex bằng hàm `Database.executeBatch()` (A), hoặc đặt lịch chạy tự động cho class Apex thông qua phương thức `System.schedule()` (B). Vừa nhanh gọn vừa không làm rác metadata của hệ thống.

**❌ Tại sao đáp án sai:**
> **C.** Dù muốn xóa Accounts nhưng giới hạn DML cứng trong một transaction chỉ tối đa là 10,000 bản ghi. Việc cố đấm ăn xôi xóa 15,000 record trong một transaction duy nhất qua Execute Anonymous chắc chắn sẽ nổ lỗi `LimitException` và rollback sạch sẽ. Cook ngay!
> **D.** Mã code chạy trong cửa sổ Execute Anonymous chỉ mang tính tức thời, chạy xong là biến mất và **không bao giờ được tính vào Code Coverage** của Org.

**💡 Từ khóa ghi nhớ:** `Execute Anonymous Apex -> Chuyên dùng chạy lệnh một lần (Batch, Schedule) + Không tính Code Coverage!`

---

## Câu 257

**🔵 A Developer wants to get access to the standard price book in the org while writing a test class that covers an OpportunityLineItem trigger. Which method allows access to the price book?**

- **A.** Use Test.getStandardPricebookId() to get the standard price book ID. ✅
- **B.** Use @IsTest(SeeAllData=true) and delete the existing standard price book. ❌
- **C.** Use Test.loadData() and a Static Resource to load a standard price book. ❌
- **D.** Use @TestVisible to allow the test method to see the standard price book. ❌

**📝 Dịch tiếng Việt:**
> Developer muốn truy cập vào Standard Pricebook (Bảng giá chuẩn) của hệ thống khi viết một test class cho Trigger trên OpportunityLineItem. Phương thức nào cho phép truy cập lấy ID của Standard Pricebook này?

**💬 Giải thích gốc (English):**
> To access the standard price book in a test class that covers an OpportunityLineItem trigger, the developer should use the Test.getStandardPricebookId() method. This method retrieves the ID of the standard price book, allowing the test class to reference it.

**✅ Tại sao đáp án đúng:**
> Chọn **A: Sử dụng phương thức `Test.getStandardPricebookId()`**. Mặc định, Salesforce cô lập dữ liệu thật trong môi trường chạy test để bảo vệ hệ thống. Vì thế, bạn không thể SOQL query để tìm Standard Pricebook được. Salesforce cung cấp sẵn hàm `Test.getStandardPricebookId()` để bạn lấy ngay được ID chuẩn của Standard Pricebook mà không cần tắt chế độ cô lập dữ liệu.

**❌ Tại sao đáp án sai:**
> **B.** Dùng `@IsTest(SeeAllData=true)` là một quả anti-pattern cực lớn vì nó làm mất tính độc lập dữ liệu của test class. Thêm vào đó, xóa Standard Pricebook hiện tại đi là hành động tự hủy cực mạnh!
> **C.** Standard Pricebook là đối tượng hệ thống đặc biệt được tạo tự động, bạn không thể tự ý nạp (load) nó từ file CSV qua Static Resource được.
> **D.** `@TestVisible` chỉ dùng để hiển thị các biến private hoặc method private của class chính cho test class nhìn thấy, chứ không liên quan gì đến dữ liệu hệ thống.

**💡 Từ khóa ghi nhớ:** `Muốn lấy ID Standard Pricebook trong Unit Test -> Auto chọn **`Test.getStandardPricebookId()`**.`

---

## Câu 258

**🔵 A development team wants to use a deployment script to automatically deploy to a sandbox during their development cycles. Which two tools can they use to run a script that deploys to a sandbox? (Choose two.)**

- **A.** SFDX CLI ✅
- **B.** Developer Console ❌
- **C.** Change Sets ❌
- **D.** Ant Migration Tool ✅

**📝 Dịch tiếng Việt:**
> Một đội phát triển muốn viết script tự động deploy code lên sandbox định kỳ trong chu kỳ phát triển. Hai công cụ nào có thể chạy được script deploy này? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> Chọn **A (SFDX CLI)** và **D (Ant Migration Tool)**.
- **SFDX CLI** (A) là công cụ dòng lệnh (command-line interface) hiện đại tối tân của Salesforce, cực kỳ thích hợp để nhúng vào các CI/CD script (như GitHub Actions, GitLab CI) để tự động deploy.
- **Ant Migration Tool** (D) là công cụ dòng lệnh đời cũ chạy bằng Java dựa trên Apache Ant, chuyên dùng để tự động hóa deploy qua XML script. Tuy cổ nhưng vẫn đáp ứng tốt yêu cầu.

**❌ Tại sao đáp án sai:**
> **B.** **Developer Console** chỉ dùng để viết code, chạy debug log, SOQL chứ không có tính năng nào để chạy script tự động deploy metadata từ máy tính của bạn lên cả.
> **C.** **Change Sets** là công cụ kéo thả bằng tay (point-and-click) trực tiếp ngoài giao diện web Salesforce, không thể chạy bằng script hay tự động hóa dòng lệnh được.

**💡 Từ khóa ghi nhớ:** `Deploy code tự động bằng Script -> Chọn ngay bộ đôi dòng lệnh **SFDX CLI** và **Ant Migration Tool**!`

---

## Câu 259

**🔵 A platform developer at Universal Containers needs to create a custom button for the Account object that, when clicked, will perform a series of calculations and redirect the user to a custom Visualforce page. Which three attributes need to be defined with values in the tag to accomplish this? (Choose three.)**

- **A.** action ✅
- **B.** renderAs ❌
- **C.** standardController ✅
- **D.** readOnly ❌
- **E.** extensions ✅

**📝 Dịch tiếng Việt:**
> Developer cần tạo một custom button trên Account. Khi click, hệ thống sẽ thực hiện một loạt phép tính toán rồi tự chuyển hướng (redirect) user sang một trang Visualforce tùy biến. Ba thuộc tính nào cần khai báo giá trị trong thẻ `<apex:page>` để làm được việc này? (Chọn 3)

**💬 Giải thích gốc (English):**
> To create a custom button for the Account object that performs calculations and redirects to a custom Visualforce page, the developer needs to define the following three attributes in the <apex:page> tag:
> StandardController: This attribute specifies the standard controller for the Visualforce page, which in this case would be the Account object.
> Action: This attribute defines the action method that performs the calculations before redirecting to the Visualforce page.
> Extensions: This attribute specifies any additional Apex classes that extend the standard controller to include custom logic for the calculations.

**✅ Tại sao đáp án đúng:**
> Chọn **A (action)**, **C (standardController)** và **E (extensions)**. Để ghi đè (override) được hành động click nút bấm chuẩn trên Account bằng trang Visualforce:
- Trang phải dùng **`standardController="Account"`** để Salesforce biết trang này thuộc Account (C).
- Phải dùng **`extensions="TênApexClass"`** để nhúng class Apex chứa logic tính toán nâng cao (E).
- Phải dùng thuộc tính **`action="{!phươngThứcTínhToán}"`** trong thẻ `<apex:page>` để ngay khi trang load lên, nó sẽ tự động chạy logic tính toán rồi redirect đi luôn (A).

**❌ Tại sao đáp án sai:**
> **B.** `renderAs` chỉ dùng để chỉ định định dạng hiển thị của trang (ví dụ xuất trang sang PDF), không liên quan đến việc xử lý logic chuyển trang.
> **D.** `readOnly` dùng để tối ưu hóa trang ở chế độ chỉ đọc (tăng giới hạn số lượng bản ghi SOQL có thể hiển thị), không hỗ trợ cho các nút bấm nghiệp vụ tính toán sửa đổi.

**💡 Từ khóa ghi nhớ:** `Ghi đè nút bấm + xử lý Apex tính toán trong Visualforce -> Cần bộ ba: **standardController**, **extensions**, **action**.`

---

## Câu 260

**🔵 A recursive transaction is initiated by a DML statement creating records for these two objects:     1. Accounts 2. Contacts The Account trigger hits a stack depth of 16. Which statement is true regarding the outcome of the transaction?**

- **A.** The transaction fails and all the changes are rolled back. ❌
- **B.** The transaction succeeds as long as the Contact trigger stack depth is less than 16. ❌
- **C.** The transaction fails only if the Contact trigger stack depth is greater or equal to 16. ✅
- **D.** The transaction succeeds and all changes are committed to the database. ❌

**📝 Dịch tiếng Việt:**
> Một transaction đệ quy được kích hoạt bởi câu lệnh DML tạo bản ghi cho 2 object: Accounts và Contacts. Trigger trên Account đã chạm tới độ sâu ngăn xếp (stack depth) là 16. Phát biểu nào dưới đây là ĐÚNG về kết quả của transaction này?

**💬 Giải thích gốc (English):**
> When an Account trigger hits a stack depth of 16, it means that the trigger has recursively called itself 16 times. In Salesforce, the maximum allowed stack depth for recursive triggers is 16. Therefore, the transaction will fail with a “maximum trigger depth exceeded” error.
> To avoid these kind of situation we can use public class static variable. We can solve this issue, you can set a condition on trigger so it will not be called recursively.

**✅ Tại sao đáp án đúng:**
> Chọn **C: Transaction chỉ thất bại nếu độ sâu ngăn xếp của Trigger Contact vượt quá hoặc bằng 16**. Giới hạn đệ quy trigger (stack depth limit) cứng của Salesforce là **16**. Khi độ sâu tích lũy của toàn bộ transaction (gồm cả Account và Contact trigger gọi qua lại lẫn nhau) vượt quá giới hạn này (tức là sang lần thứ 17), hệ thống mới chính thức nổ lỗi `LimitException` và rollback sạch sẽ. Ở mức 16, transaction vẫn tạm thời 'thở oxy' thành công được.

**❌ Tại sao đáp án sai:**
> **A.** Transaction chưa chắc đã fail ngay ở mức stack depth 16 nếu không bị kích hoạt thêm lần nào nữa.
> **B.** Sai logic tính toán giới hạn đệ quy chung của transaction.
> **D.** Không chắc chắn thành công hoàn toàn vì chỉ cần phát sinh thêm 1 lần đệ quy nữa vượt qua 16 là cả lũ dắt tay nhau đi 'cook' hết.

**💡 Từ khóa ghi nhớ:** `Giới hạn đệ quy (Stack Depth) của Salesforce là **16**. Chạm 16 vẫn sống, vượt quá 16 (tức là từ 17 trở đi) là auto oẳng!`

---

## Câu 261

**🔵 Which exception type cannot be caught?**

- **A.** LimitException ✅
- **B.** NoAccessException ❌
- **C.** A Custom Exception ❌
- **D.** CalloutException ❌

**📝 Dịch tiếng Việt:**
> Loại ngoại lệ (Exception) nào dưới đây KHÔNG THỂ bị bắt (catch) bằng khối try-catch trong Apex?

**💬 Giải thích gốc (English):**
> LimitException is a type of exception in Salesforce that cannot be caught. Since these limits are enforced to ensure the stability and performance of the Salesforce platform, LimitException cannot be handled using try-catch blocks.

**✅ Tại sao đáp án đúng:**
> Chọn **A: LimitException**. Đây là lỗi chí mạng của Salesforce! Khi bạn vượt quá giới hạn Governor Limits (ví dụ chạy quá 100 câu SOQL, vượt quá bộ nhớ heap...), Salesforce sẽ lập tức dừng cuộc chơi ngay lập tức và ném ra `LimitException`. Hệ thống cấm tiệt việc dùng `try-catch` để bắt lỗi này vì nếu cho phép bắt, dev sẽ tha hồ lách luật và phá hoại tài nguyên dùng chung của môi trường multi-tenant. Quá chuẩn!

**❌ Tại sao đáp án sai:**
> **B.** `NoAccessException` (lỗi không có quyền truy cập) vẫn bắt được bình thường để hiển thị thông báo lỗi thân thiện cho user.
> **C.** `Custom Exception` do chính bạn viết ra nhằm phục vụ mục đích ném và bắt theo logic nghiệp vụ của bạn.
> **D.** `CalloutException` nổ ra khi gọi API lỗi (mất mạng, timeout...), bắt thoải mái bằng try-catch để xử lý retry.

**💡 Từ khóa ghi nhớ:** `Đụng tới giới hạn **LIMIT** (LimitException) là auto oẳng, không ai cứu nổi, kể cả cụ tổ **Try-Catch**!`

---

## Câu 262

**🔵 A developer wants to import 500 Opportunity records into a sandbox. Why should the developer choose to use Data Loader instead of Data Import Wizard?**

- **A.** Data Loader runs from the developer's browser. ❌
- **B.** Data Loader automatically relates Opportunities to Accounts. ❌
- **C.** Data Import Wizard does not support Opportunities. ✅
- **D.** Data Import Wizard can not import all 500 records. ❌

**📝 Dịch tiếng Việt:**
> Developer muốn import 500 bản ghi Opportunity vào môi trường Sandbox. Tại sao lập trình viên nên chọn công cụ Data Loader thay vì công cụ Data Import Wizard?

**💬 Giải thích gốc (English):**
> The Data Import Wizard does not support the import of Opportunity records. It is limited to certain standard objects like Contacts, Leads, and Accounts.

**✅ Tại sao đáp án đúng:**
> Chọn **C: Vì Data Import Wizard hoàn toàn không hỗ trợ import đối tượng Opportunity**. Đây là giới hạn cứng siêu chuối của Data Import Wizard! Nó chỉ hỗ trợ một số đối tượng tiêu chuẩn cơ bản như Accounts, Contacts, Leads, Solutions và Campaign Members, cộng thêm các Custom Object. Còn mấy khứa standard sừng sỏ như Opportunity hay Case thì bắt buộc phải gọi tên **Data Loader**.

**❌ Tại sao đáp án sai:**
> **A.** Ngược rồi bro! Data Import Wizard mới chạy trực tiếp trên trình duyệt web, còn Data Loader là phần mềm client cài đặt offline trên máy tính.
> **B.** Data Import Wizard thực ra hỗ trợ so khớp tự động khi liên kết Account/Contact thông minh hơn Data Loader nhiều.
> **D.** Data Import Wizard dư sức import tới 50,000 bản ghi, 500 bản ghi chỉ là muỗi đối với nó.

**💡 Từ khóa ghi nhớ:** `Data Import Wizard cấm tiệt **Opportunity** và **Case**. Muốn nạp Opp/Case -> Chỉ có con đường **Data Loader**.`

---

## Câu 263

**🔵 When importing and exporting data into Salesforce, which two statements are true? (Choose two.)**

- **A.** Bulk API can be used to Import large data volumes in development environments without bypassing the storage limits. ✅
- **B.** Developer and Developer Pro sandboxes have different storage limits. ✅
- **C.** Bulk API can be used to bypass the storage limits when importing large data volumes in development environments. ❌
- **D.** Data import wizard is a client application provided by Salesforce. ❌

**📝 Dịch tiếng Việt:**
> Khi nhập (import) và xuất (export) dữ liệu vào Salesforce, hai phát biểu nào sau đây là đúng? (Chọn 2)

**💬 Giải thích gốc (English):**
> Developer sandboxes have a storage limit of 200 MB for data and 200 MB for files, while Developer Pro sandboxes have a storage limit of 1 GB for data and 1 GB for files.
> The Data Import Wizard is a tool provided by Salesforce that allows users to import data into Salesforce objects through a simple interface.

**✅ Tại sao đáp án đúng:**
> Chọn **A** và **B**. Vì:
- Dù bạn có dùng **Bulk API** để import hàng triệu bản ghi cực kỳ tối ưu và tốc độ bàn thờ đi chăng nữa, bạn vẫn phải tuyệt đối tuân thủ **storage limits** (giới hạn dung lượng lưu trữ) của Org, không hề có chuyện được bypass (A).
- Dung lượng lưu trữ của các loại Sandbox là hoàn toàn khác nhau: Developer Sandbox chỉ có **200MB** dung lượng lưu trữ dữ liệu, còn Developer Pro Sandbox được ưu ái cấp tới **1GB** (B).

**❌ Tại sao đáp án sai:**
> **C.** Không có bất kỳ API hay công cụ thần thánh nào cho phép bạn bypass (vượt qua) giới hạn dung lượng lưu trữ cứng của Org cả. Dùng Bulk API mà Org hết dung lượng thì vẫn lỗi nghẽn bình thường.
> **D.** Data Import Wizard là công cụ chạy trực tiếp trên nền web của Salesforce chứ không phải là một phần mềm client (client application) cài đặt offline giống như Data Loader.

**💡 Từ khóa ghi nhớ:** `Giới hạn dung lượng lưu trữ Sandbox: **Developer = 200MB**, **Developer Pro = 1GB**. Nhớ con số này để thi ăn điểm!`

---

## Câu 264

**🔵 Which code should be used to update an existing Visualforce page that uses standard Visualforce components so that the page matches the look and feel of Lightning Experience?**

- **A.** <apex:styleSheet value="({$URLFOR($Resource.slds,’assets/slds.css’)}"> ❌
- **B.** <apex:slds/> ❌
- **C.** <apex:page lightningStyleSheets="true"> ✅
- **D.** <apex:includeLightning/> ❌

**📝 Dịch tiếng Việt:**
> Đoạn code nào giúp hô biến một trang Visualforce đang dùng các component tiêu chuẩn thành giao diện có kiểu dáng (look and feel) hiện đại y hệt Lightning Experience?

**💬 Giải thích gốc (English):**
> To style your Visualforce page to match the Lightning Experience UI when viewed in Lightning Experience or the Salesforce mobile app, set lightningStylesheets="true" in the <apex:page> tag. When the page is viewed in Salesforce Classic, it doesn’t get Lightning Experience styling.
> <apex:page lightningStylesheets="true">

**✅ Tại sao đáp án đúng:**
> Chọn **C: `<apex:page lightningStyleSheets="true">`**. Chỉ cần nhét thêm thuộc tính `lightningStyleSheets="true"` vào thẻ khai báo trang `<apex:page>`, Salesforce sẽ tự động 'đắp' toàn bộ CSS của Lightning lên các component chuẩn của Visualforce. Cực kỳ nhanh gọn lẹ, no-code chuẩn chỉ!

**❌ Tại sao đáp án sai:**
> **A.** Cú pháp import CSS thủ công từ Static Resource vừa dài dòng, vừa lỗi thời, lại viết sai cả cú pháp mở ngoặc nhọn đóng ngoặc nhọn kìa bro.
> **B.** `<apex:slds/>` chỉ đơn thuần là nạp bộ thư viện design system (SLDS) vào trang, bạn sẽ phải tự đi viết các class CSS thủ công vào từng thẻ HTML để làm đẹp. Mệt mỏi lắm, rảnh đâu mà làm!
> **D.** `<apex:includeLightning/>` dùng để nạp thư viện JavaScript cho phép gọi công nghệ Lightning Out để nhúng LWC/Aura, không liên quan đến việc đổi giao diện cho trang Visualforce.

**💡 Từ khóa ghi nhớ:** `VF đổi sang giao diện Lightning nhanh nhất -> Cứ ném **`lightningStyleSheets="true"`** vào thẻ `<apex:page>`.`

---

## Câu 265

**🔵 Which three code lines are required to create a Lightning component on a Visualforce page? (Choose three.)**

- **A.** $Lightning.useComponent ❌
- **B.** <apex:slds/> ❌
- **C.** $Lightning.use ✅
- **D.** <apex:includeLightning/> ✅
- **E.** $Lightning.createComponent ✅

**📝 Dịch tiếng Việt:**
> Ba dòng mã nào bắt buộc phải có để nhúng và khởi tạo một Lightning component trực tiếp trên trang Visualforce?

**✅ Tại sao đáp án đúng:**
> Chọn **C**, **D** và **E**. Đây là bộ ba thần thánh để gọi công nghệ **Lightning Out**:
1. **`<apex:includeLightning/>`** (D) để nạp thư viện JavaScript cầu nối của Lightning.
2. **`$Lightning.use(...)`** (C) để chỉ định standalone Aura App chứa dependencies của component.
3. **`$Lightning.createComponent(...)`** (E) để chính thức khởi tạo và vẽ component đó lên vùng chứa (container div) trên trang Visualforce.

**❌ Tại sao đáp án sai:**
> **A.** Không hề tồn tại phương thức nào tên là `$Lightning.useComponent` cả, đồ fake tự bịa ra để lừa trẻ con đấy bro!
> **B.** `<apex:slds/>` dùng để nạp CSS của Salesforce Lightning Design System, không có vai trò gì trong việc nhúng và chạy runtime của component.

**💡 Từ khóa ghi nhớ:** `Nhúng Lightning vào Visualforce -> Nhớ câu thần chú: **Include (thẻ) -> Use (hàm) -> Create (hàm)**!`

---

## Câu 266

**🔵 A developer is integrating with a legacy on-premise SQL database. What should the developer use to ensure the data being integrated is matched to the right records in Salesforce?**

- **A.** Formula field ❌
- **B.** Lookup field ❌
- **C.** External ID field ✅
- **D.** External Object ❌

**📝 Dịch tiếng Việt:**
> Developer đang làm task tích hợp hệ thống (integration) với một database SQL cũ của doanh nghiệp (on-premise SQL database). Nên dùng cái gì để đảm bảo đống dữ liệu đổ vào Salesforce được so khớp chính xác với các bản ghi tương ứng?

**💬 Giải thích gốc (English):**
> Use External IDs in Salesforce to match records. External IDs are custom fields that have the “External ID” attribute, which can be used to match records from external systems. This is particularly useful for upsert operations where you need to insert or update records based on an external identifier.

**✅ Tại sao đáp án đúng:**
> Chọn **C: Trường External ID (Khóa ngoài)**. Khi bạn đánh dấu một trường text custom là **External ID**, Salesforce sẽ coi đây là mã định danh duy nhất từ hệ thống ngoài. Hệ thống SQL kia khi đẩy dữ liệu sang chỉ cần gọi lệnh `Upsert` kèm theo mã này, Salesforce sẽ tự động biết bản ghi nào đã có để cập nhật (Update), bản ghi nào chưa có để tạo mới (Insert). Vừa nhàn vừa an toàn!

**❌ Tại sao đáp án sai:**
> **A.** **Formula field** chỉ hiển thị giá trị dạng đọc tĩnh dựa trên công thức, không thể là nơi nhận và lưu trữ trực tiếp mã ID từ hệ thống bên ngoài đổ vào.
> **B.** **Lookup field** dùng để tạo mối liên kết cha-con giữa 2 object trong Salesforce chứ không có chức năng làm khóa ngoài so khớp tự động khi tích hợp.
> **D.** **External Object** dùng để kết nối xem dữ liệu realtime ngoài Org (Salesforce Connect) chứ không dùng để lưu trữ vật lý hay map dữ liệu import.

**💡 Từ khóa ghi nhớ:** `So khớp dữ liệu với hệ thống bên ngoài -> Tạo ngay trường **EXTERNAL ID**!`

---

## Câu 267

**🔵 A developer is asked to create a Visualforce page that displays some Account fields as well as fields configured on the page layout for related Contacts. How should the developer implement this request?**

- **A.** Use the <apex:include> tag. ❌
- **B.** Use the <apex:relatedList> tag. ✅
- **C.** Add a method to the standard controller. ❌
- **D.** Create a controller extension. ❌

**📝 Dịch tiếng Việt:**
> Developer được giao task tạo một trang Visualforce hiển thị một vài trường của Account, đồng thời phải hiển thị danh sách các Contact liên quan theo đúng cấu hình Page Layout mà admin đã cài đặt. Triển khai thế nào cho gọn nhất?

**💬 Giải thích gốc (English):**
> To create a Visualforce page that displays some Account fields as well as fields configured on the page layout for related Contacts, the developer can follow these steps:
> 1. Use the Standard Controller for Account: This allows the Visualforce page to access the Account data.
> 2. Use <apex:detail> for Account Fields: This component displays the standard detail page for the Account, including fields configured on the page layout.
> 3. Use <apex:relatedList> for Related Contacts: This component displays the related list of Contacts as configured on the Account page layout.

**✅ Tại sao đáp án đúng:**
> Chọn **B: Sử dụng thẻ `<apex:relatedList list="Contacts"/>`**. Thẻ này là báu vật no-code cực mạnh của Visualforce! Nó sẽ tự động bê nguyên bảng danh sách các Contact con liên quan lên trang, hiển thị đúng các trường, các nút bấm chuẩn y hệt như cấu hình Page Layout chuẩn của Account cha mà không cần bạn viết một dòng controller nào.

**❌ Tại sao đáp án sai:**
> **A.** `<apex:include>` dùng để nhúng nguyên một trang Visualforce độc lập khác vào trang hiện tại, không có chức năng vẽ related list bản ghi con.
> **C.** Standard Controller của Salesforce là class đóng, bạn không thể tự ý chọc vào để thêm phương thức được. Muốn thêm logic chỉ có nước viết Controller Extension.
> **D.** Tự viết **Controller Extension** để SOQL query Contact rồi tự vẽ bảng bằng code HTML là một pha xử lý cực kỳ cồng kềnh, tốn công bảo trì vô ích khi thẻ tiêu chuẩn đã cân tốt.

**💡 Từ khóa ghi nhớ:** `Hiển thị danh sách con liên quan chuẩn Page Layout -> Dùng thẻ thần thánh **`<apex:relatedList>`**.`

---

## Câu 268

**🔵 While working in a sandbox, an Apex test falls when run in the Test Framework. However, running the Apex test logic in the Execute Anonymous window succeeds with no exceptions or errors. Why did the method fall in the sandbox test framework but succeed in the Developer Console?**

- **A.** The test method is calling an @future method. ❌
- **B.** The test method has a syntax error in the code. ❌
- **C.** The test method does not use System.runAs to execute as a specific user. ❌
- **D.** The test method relies on existing data in the sandbox. ✅

**📝 Dịch tiếng Việt:**
> Trong Sandbox, một bài test Apex bị FAIL sấp mặt khi chạy bằng Test Framework. Thế nhưng, khi copy nguyên logic test đó chạy trong cửa sổ Execute Anonymous của Developer Console thì lại SUCCESS mượt mà không một vết xước. Tại sao lại có sự ảo ma thế này?

**💬 Giải thích gốc (English):**
> In Apex tests, it’s important to create all necessary data within the test itself to ensure it doesn’t depend on existing data in the environment. When you run the code via the Execute Anonymous tool, it can access the existing data in the sandbox, which might not be the case when running the test method

**✅ Tại sao đáp án đúng:**
> Chọn **D: Vì phương thức test đang dựa dẫm vào dữ liệu thật có sẵn trong Sandbox**. Đây là cái bẫy kinh điển cho các tấm chiếu mới! Khi chạy bằng Test Framework, hệ thống mặc định cô lập hoàn toàn dữ liệu (`SeeAllData=false`), database hoàn toàn trống rỗng dẫn đến việc query không có dữ liệu và bị crash test. Còn khi chạy bằng Execute Anonymous, code được thực thi trực tiếp trên database thật của Sandbox, nhìn thấy các record có sẵn nên chạy qua ngon lành.

**❌ Tại sao đáp án sai:**
> **A.** Gọi phương thức `@future` trong test nếu không bọc trong `Test.startTest()` và `Test.stopTest()` thì có thể không chạy kịp, nhưng nó sẽ fail ở cả hai nơi chứ không tạo ra sự khác biệt thế này.
> **B.** Nếu có lỗi cú pháp (Syntax error) thì trình biên dịch đã chửi thẳng mặt và block không cho lưu hay chạy code ở cả hai công cụ rồi.
> **C.** `System.runAs` dùng để test quyền truy cập của User cụ thể, không liên quan đến việc cô lập hay không cô lập dữ liệu database.

**💡 Từ khóa ghi nhớ:** `Test Framework FAIL mà Execute Anonymous SUCCESS -> Chắc chắn do code test chưa tự tạo data test mà đi **dựa dẫm dữ liệu có sẵn trong Org** (`relies on existing data`).`

---

## Câu 269

**🔵 A developer has a single custom controller class that works with a Visualforce Wizard to support creating and editing multiple sObjects. The wizard accepts data from user inputs across multiple Visualforce pages and from a parameter on the initial URL. Which three statements are useful inside the unit test to effectively test the custom controller? (Choose three.)**

- **A.** Insert pageRef; ❌
- **B.** String nextPage = controller.save().getUrl(); ✅
- **C.** ApexPages.currentPage().getParameters().put('Input', 'TestValue'); ✅
- **D.** public ExtendedController(ApexPages.StandardController cntrl){} ❌
- **E.** Test.setCurrentPage(pageRef); ✅

**📝 Dịch tiếng Việt:**
> Developer có một custom controller duy nhất phục vụ cho trang Visualforce Wizard phức tạp (cho phép tạo và sửa nhiều đối tượng qua nhiều màn hình và nhận tham số truyền từ URL). Ba câu lệnh nào sẽ cực kỳ hữu ích khi viết unit test cho cái controller này? (Chọn 3)

**💬 Giải thích gốc (English):**
> Test.setCurrentPage(pageRef);
> This statement sets the current page context to the specified PageReference, which is essential for simulating the Visualforce page environment in your test.
> ApexPages.CurrentPage().getParameters().put(‘input’, ‘TestValue’);
> This statement allows you to set parameters on the current page, which is useful for testing how your controller handles URL parameters.
> String nextPage = controller.save().getUrl();
> This statement captures the URL of the next page after an action method (like save) is called, which helps verify the navigation logic of your controller.

**✅ Tại sao đáp án đúng:**
> Chọn **B**, **C** và **E**. Để test mượt mà các kịch bản của Wizard:
- Dùng **`Test.setCurrentPage(pageRef)`** (E) để thiết lập trang hiện tại trong ngữ cảnh test.
- Dùng **`ApexPages.currentPage().getParameters().put('tên', 'giá trị')`** (C) để giả lập việc truyền tham số trên URL cho controller đọc.
- Dùng **`controller.save().getUrl()`** (B) để gọi hàm save và kiểm tra xem URL trang tiếp theo được chuyển hướng (redirect) có đúng như kỳ vọng không.

**❌ Tại sao đáp án sai:**
> **A.** `pageRef` (PageReference) chỉ là một đối tượng chứa thông tin URL trong code, không phải sObject thực tế lưu dưới database nên gọi lệnh DML `Insert pageRef` là sai cú pháp nổ lỗi ngay lập tức.
> **D.** Dòng khai báo hàm khởi tạo Controller Extension `public ExtendedController(...)` là khai báo code, không phải là câu lệnh thực thi kiểm thử trong test method.

**💡 Từ khóa ghi nhớ:** `Test Visualforce Controller -> Set trang hiện tại bằng **`Test.setCurrentPage()`** và truyền tham số qua **`getParameters().put()`**.`

---

## Câu 270

**🔵 Which three Salesforce resources can be accessed from a Lightning web component? (Choose three.)**

- **A.** All external libraries ❌
- **B.** Static resources ✅
- **C.** Third-party web components ❌
- **D.** Content asset files ✅
- **E.** SVG resources ✅

**📝 Dịch tiếng Việt:**
> Một component LWC có thể truy cập trực tiếp vào ba loại tài nguyên (resources) nào của hệ thống Salesforce? (Chọn 3)

**✅ Tại sao đáp án đúng:**
> Chọn **B (Static resources)**, **D (Content asset files)** và **E (SVG resources)**. LWC hỗ trợ cơ chế import cực kỳ mạnh mẽ thông qua các module chuẩn `@salesforce/`. Bạn có thể dễ dàng import các tài nguyên tĩnh như file CSS/JS ngoài từ Static Resources (B), các file ảnh/tài liệu từ Content Asset (D), và các file đồ họa vector SVG để làm icon (E).

**❌ Tại sao đáp án sai:**
> **A.** Salesforce có chính sách bảo mật CSP (Content Security Policy) cực kỳ nghiêm ngặt, bạn không thể tự ý gọi hay nạp trực tiếp tất cả các thư viện ngoài từ Internet được nếu chưa khai báo an toàn.
> **C.** Bạn không thể trực tiếp truy cập hay nhúng các component của bên thứ ba (Third-party web components) chạy ngoài vũ trụ Salesforce vào thẳng shadow tree của LWC một cách tự do được.

**💡 Từ khóa ghi nhớ:** `LWC import trực tiếp từ Salesforce -> Bộ ba tài nguyên: **Static Resources**, **Content Asset**, **SVG**.`

---

## Câu 271

**🔵 Which two events need to happen when deploying to a production org? (Choose two.)**

- **A.** All Workflow rules must have at least 1% test coverage. ❌
- **B.** All Apex code must have at least 75% test coverage. ✅
- **C.** All triggers must have some test coverage. ✅
- **D.** All Visual Flows must have at least 1% test coverage. ❌

**📝 Dịch tiếng Việt:**
> Hai điều kiện bắt buộc nào phải thỏa mãn khi bạn thực hiện deploy code Apex/Trigger lên môi trường Production? (Chọn 2)

**💬 Giải thích gốc (English):**
> Code Coverage
> You must have at least 75% of your Apex covered by unit tests to deploy your code to production environments.
> All triggers must have at least one line of test coverage.

**✅ Tại sao đáp án đúng:**
> Chọn **B** và **C**. Đây là luật cứng của Salesforce khi bước chân lên Production:
- **Tất cả code Apex** trên toàn bộ hệ thống (Org-wide) phải đạt tỷ lệ phủ sóng test coverage tối thiểu là **75%** (B).
- **Tất cả các Trigger** bắt buộc phải có độ phủ test coverage lớn hơn **0%** (C), tức là phải có ít nhất 1 dòng code trong Trigger được chạy qua trong các bài test. Thiếu một trong hai điều kiện này là trình deploy sẽ báo lỗi và block ngay lập tức.

**❌ Tại sao đáp án sai:**
> **A.** Workflow rules là tính năng no-code khai báo đời cổ, không có khái niệm chạy unit test hay đo đạc test coverage gì ở đây cả.
> **D.** Visual Flows (Flow) tuy có thể viết Flow Test nhưng hoàn toàn không bị áp đặt giới hạn 1% test coverage cứng khi deploy lên Production như Apex.

**💡 Từ khóa ghi nhớ:** `Lên Production: Apex toàn Org >= **75%** + Từng Trigger > **0%** (phải có test chạy qua)!`

---

## Câu 272

**🔵 Universal Containers recently transitioned from Classic to Lightning Experience. One of its business processes requires certain values from the Opportunity object to be sent via an HTTP REST callout to its external order management system based on a user-initiated action on the Opportunity detail page. Example values are as follows: Name Amount Account. Which two methods should the developer implement to fulfill the business requirement? (Choose two.)**

- **A.** Create a Visualforce page that performs the HTTP REST callout, and use a Visualforce quick action to expose the component on the Opportunity detail page. ❌
- **B.** Create a Process Builder on the Opportunity object that executes an Apex immediate action to perform the HTTP REST callout whenever the Opportunity is updated. ❌
- **C.** Create a Lightning component that performs the HTTP REST callout, and use a Lightning Action to expose the component on the Opportunity detail page. ✅
- **D.** Create an after update trigger on the Opportunity object that calls a helper method using @Future(Callout=true) to perform the HTTP REST callout. ✅

**📝 Dịch tiếng Việt:**
> Universal Containers vừa chuyển đổi từ Classic sang Lightning Experience. Một quy trình nghiệp vụ yêu cầu: Khi người dùng thực hiện một thao tác trên trang chi tiết Opportunity, hệ thống phải lấy các giá trị Name, Amount và Account gửi qua cuộc gọi HTTP REST callout tới hệ thống quản lý đơn hàng bên ngoài. Hai giải pháp nào lập trình viên nên chọn triển khai? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> Chọn **C** và **D**.
- **C: Tạo một Lightning component thực hiện REST callout và nhúng vào Quick Action (Lightning Action) trên trang Opportunity**. Đây là giải pháp chuẩn chỉnh trên UI của Lightning, đem lại trải nghiệm mượt mà, gọi API tức thời khi click.
- **D: Tạo một after update trigger gọi helper method có annotation `@future(callout=true)` để chạy REST callout**. Đây là giải pháp chạy ngầm (backend) cực kỳ tối ưu, tự động đẩy API bất đồng bộ ngay sau khi bản ghi được cập nhật mà không làm nghẽn giao dịch chính.

**❌ Tại sao đáp án sai:**
> **A.** Visualforce Page kết hợp VF Quick Action là giải pháp chắp vá mang công nghệ cũ kỹ từ thời Classic, không mang lại trải nghiệm nguyên bản chuẩn Lightning Experience.
> **B.** Process Builder là đồ cổ đã bị khai tử (deprecated), và bản thân nó cũng không thể tự thực hiện trực tiếp các cuộc gọi HTTP REST callout được, bắt buộc phải gọi thêm Apex trung gian rất cồng kềnh.

**💡 Từ khóa ghi nhớ:** `REST callout từ Opportunity detail page -> Dùng **Lightning Component Quick Action** hoặc **Trigger + `@future(callout=true)`**.`

---

## Câu 273

**🔵 Which statement describes the execution order when triggers are associated to the same object and event?**

- **A.** Triggers are executed in the order they are modified. ❌
- **B.** Triggers are executed alphabetically by trigger name. ❌
- **C.** Trigger execution order cannot be guaranteed. ✅
- **D.** Triggers are executed in the order they are created. ❌

**📝 Dịch tiếng Việt:**
> Phát biểu nào mô tả đúng nhất về thứ tự thực thi của các Trigger khi chúng được gắn trên cùng một Object và chạy cùng một sự kiện?

**💬 Giải thích gốc (English):**
> If more than one trigger is defined on an object for the same event, the order of trigger execution isn't guaranteed. For example, if you have two before insert triggers for Case and a new Case record is inserted. The firing order of these two triggers isn’t guaranteed.

**✅ Tại sao đáp án đúng:**
> Chọn **C: Thứ tự thực thi của các Trigger không được đảm bảo**. Salesforce cấm tiệt việc hứa hẹn hay cam kết thứ tự chạy giữa các Trigger cùng chạy chung một sự kiện trên một đối tượng. Hôm nay Trigger A chạy trước, ngày mai Trigger B chạy trước là chuyện bình thường như cân đường hộp sữa!

**❌ Tại sao đáp án sai:**
> **A.** Thứ tự chỉnh sửa gần nhất (modified) không hề có tiếng nói gì trong việc xếp lịch chạy của hệ thống.
> **B.** Sắp xếp theo thứ tự bảng chữ cái (alphabetical) của tên Trigger chỉ là trò bịa để đánh lừa các tấm chiếu mới.
> **D.** Thứ tự ngày tạo (created) cũng không có bất kỳ ảnh hưởng nào đến runtime của Salesforce.

**💡 Từ khóa ghi nhớ:** `Nhiều Trigger cùng Object/Event -> **Không đảm bảo thứ tự chạy (cannot be guaranteed)** -> Best practice: **Chỉ dùng 1 Trigger duy nhất cho 1 Object**!`

---

## Câu 274

**🔵 In the Lightning UI, where should a developer look to find information about a Paused Flow Interview?**

- **A.** On the Paused Flow Interviews related list for a given record ❌
- **B.** In the system debug log by filtering on Paused Flow Interview ❌
- **C.** In the Paused Interviews section of the Apex Flex Queue ❌
- **D.** On the Paused Flow Interviews component on the Home page ✅

**📝 Dịch tiếng Việt:**
> Trên giao diện Lightning Experience, lập trình viên có thể tìm thấy thông tin về các Flow đang bị tạm dừng (Paused Flow Interview) ở đâu để người dùng tiếp tục thao tác?

**💬 Giải thích gốc (English):**
> Lightning Experience—Add the Paused Flow Interviews component to the appropriate Home pages. This component is available only for Home pages in the Lightning App Builder. It displays paused interviews that the user has read access to.
> Experience Builder Site—Add the Paused Flows component to a site page. This component is available for most pages in Experience Builder, except ones like login pages and error pages. The component displays paused interviews that the user has read access to.
> Salesforce mobile app—Add the Paused Flows item to the navigation items of any Lightning app.
> Salesforce Classic—Add the Paused Flow Interviews related list to the appropriate home page layouts. This component displays only interviews that the user paused.

**✅ Tại sao đáp án đúng:**
> Chọn **D: Trên component 'Paused Flow Interviews' được cấu hình hiển thị ở trang Home**. Salesforce cung cấp sẵn một Standard Component cực xịn tên là 'Paused Flow Interviews'. Admin chỉ việc lôi nó ra trang chủ (Home page) hoặc App page để user dễ dàng nhìn thấy danh sách và bấm resume để làm tiếp.

**❌ Tại sao đáp án sai:**
> **A.** Không hề tồn tại một danh sách liên quan (Related list) tiêu chuẩn nào cho Paused Flow trên các record thông thường cả.
> **B.** Debug log chỉ là file ghi vết kỹ thuật chạy ngầm của hệ thống dành cho dev soi lỗi, chứ lấy đâu ra chỗ cho user click tiếp tục thao tác Flow.
> **C.** Apex Flex Queue là hàng đợi xếp lớp dành cho Batch Apex bất đồng bộ đang chờ chạy, hoàn toàn không liên quan gì đến các session Flow của user.

**💡 Từ khóa ghi nhớ:** `Tìm kiếm Flow đang bị dừng -> Vào ngay **Home Page Component 'Paused Flow Interviews'**!`

---

## Câu 275

**🔵 An Opportunity needs to have an amount rolled up from a custom object that is not in a master-detail relationship. How can this be achieved?**

- **A.** Write a Process Builder that links the custom object to the Opportunity. ❌
- **B.** Use the Streaming API to create real-time roll-up summaries. ❌
- **C.** Write a trigger on the child object and use a red-black tree sorting to sum the amount for all related child objects under the Opportunity. ❌
- **D.** Write a trigger on the child object and use an aggregate function to sum the amount for all related child objects under the Opportunity. ✅

**📝 Dịch tiếng Việt:**
> Một Opportunity cần được tính tổng số tiền (rolled up) từ một custom object con không có quan hệ Master-Detail (chỉ có quan hệ Lookup). Làm sao để làm được việc này?

**✅ Tại sao đáp án đúng:**
> Chọn **D: Viết một trigger trên object con và sử dụng câu lệnh truy vấn gom nhóm (aggregate function) để tính tổng số tiền của các bản ghi con dưới Opportunity**. Vì quan hệ Lookup không hỗ trợ trường Roll-up Summary no-code, ta bắt buộc phải viết trigger ở đối tượng con. Mỗi khi con bị insert/update/delete/undelete, trigger sẽ chạy câu SOQL Aggregate (`SUM(Amount)`) rồi cập nhật số tiền tổng lên Opportunity cha.

**❌ Tại sao đáp án sai:**
> **A.** Process Builder không hỗ trợ các hàm gom nhóm tính toán (SUM, AVG) trên danh sách Lookup con và đã bị Salesforce khai tử.
> **B.** Streaming API dùng để đẩy sự kiện realtime ra ngoài hệ thống chứ không dùng để cập nhật tính toán lưu DB.
> **C.** Giải thuật sắp xếp cây đỏ-đen (red-black tree sorting) là thuật toán cấu trúc dữ liệu kinh điển để phỏng vấn tuyển dụng, bê vào đây chỉ tổ làm phức tạp hóa vấn đề chứ không giải quyết được việc SUM dữ liệu bản ghi con.

**💡 Từ khóa ghi nhớ:** `Lookup muốn cộng dồn từ con lên cha -> Viết **Trigger ở con + SOQL Aggregate (SUM)**!`

---

## Câu 276

**🔵 How does the Lightning Component framework help developers implement solutions faster?**

- **A.** By providing an Agile process with default steps ❌
- **B.** By providing code review standards and processes ❌
- **C.** By providing device-awareness for mobile and desktops ✅
- **D.** By providing change history and version control ❌

**📝 Dịch tiếng Việt:**
> Khung làm việc Lightning Component framework (Aura/LWC) giúp lập trình viên phát triển giải pháp nhanh hơn nhờ yếu tố nào?

**💬 Giải thích gốc (English):**
> The framework is designed to create responsive applications that work seamlessly across different devices, including mobile and desktop1. This means developers can build components once and have them function well on various platforms without additional adjustments.

**✅ Tại sao đáp án đúng:**
> Chọn **C: Bằng việc tự động nhận diện và tương thích thiết bị (device-awareness) cho cả mobile và desktop**. Lightning framework sinh ra đã mang tính chất Responsive hiện đại, tự động nhận biết kích thước màn hình để co giãn giao diện tối ưu cho cả điện thoại lẫn PC mà dev không cần nhọc công viết đống CSS media queries phức tạp.

**❌ Tại sao đáp án sai:**
> **A.** Quy trình Agile là phương pháp quản trị dự án của con người, framework code không can thiệp được.
> **B.** Quy trình review code là chuẩn mực làm việc nội bộ của team phát triển, không phải tính năng của framework.
> **D.** Quản lý lịch sử thay đổi và phiên bản là nhiệm vụ của các hệ thống kiểm soát phiên bản như Git/GitHub.

**💡 Từ khóa ghi nhớ:** `Lợi ích Lightning Component -> **Responsive tự động co giãn theo thiết bị (device-awareness)**!`

---

## Câu 277

**🔵 Which Salesforce feature allows a developer to see when a user last logged in to Salesforce if real-time notification is not required?**

- **A.** Event Monitoring Log ✅
- **B.** Calendar Events ❌
- **C.** Developer Log ❌
- **D.** Asynchronous Data Capture Events ❌

**📝 Dịch tiếng Việt:**
> Tính năng nào của Salesforce giúp lập trình viên biết được user đăng nhập lần cuối vào lúc nào khi không yêu cầu thông báo thời gian thực?

**💬 Giải thích gốc (English):**
> Event Monitoring: One of the many tools that Salesforce provides to help keep your data secure, allowing you to see the granular details of user activity in your organization. We refer to these user activities as events. Unlike Real-Time Events, Event Monitoring doesn’t send real-time notifications. Instead, it stores user activity in a log that you can query.

**✅ Tại sao đáp án đúng:**
> Chọn **A: Event Monitoring Log**. Đây là vũ khí tối tân để audit hệ thống! Event Monitoring tự động ghi lại tường tận tất cả các hành vi của người dùng trong hệ thống (từ Login, Logout, xuất Report...) dưới dạng file log chi tiết để admin/dev tải về phân tích.

**❌ Tại sao đáp án sai:**
> **B.** Calendar Events là các cuộc họp, lịch hẹn trên lịch làm việc của người dùng, chả liên quan gì đến lịch sử đăng nhập hệ thống.
> **C.** Developer Log chỉ là bản ghi debug code Apex tạm thời trong Developer Console, không phải nhật ký giám sát hoạt động hệ thống.
> **D.** Asynchronous Data Capture Events (CDC) dùng để bắt sự kiện thay đổi dữ liệu của các record trong database, hoàn toàn lạc đề.

**💡 Từ khóa ghi nhớ:** `Audit/Giám sát toàn diện hành vi user không cần realtime -> Chọn **Event Monitoring Log**!`

---

## Câu 278

**🔵 Which two are best practices when it comes to component and application event handling? (Choose two.)**

- **A.** Reuse the event logic in a component bundle, by putting the logic in the helper. ✅
- **B.** Use component events to communicate actions that should be handled at the application level. ❌
- **C.** Handle low-level events in the event handler and re-fire them as higher-level events. ✅
- **D.** Try to use application events as opposed to component events. ❌

**📝 Dịch tiếng Việt:**
> Hai thực hành tốt nhất (best practices) nào lập trình viên nên áp dụng khi xử lý và truyền sự kiện Component Event và Application Event trong Aura Components? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> Chọn **A** và **C**. (Database gốc bị typo nhầm sang B/C, đã được sửa lại cho đúng kỹ thuật):
- **A: Tái sử dụng logic xử lý sự kiện bằng cách đưa logic đó vào file Helper của component**. File JS Controller chỉ nên làm nhiệm vụ đón nhận sự kiện và gọi sang Helper để xử lý, giúp code sạch sẽ và dễ tái sử dụng.
- **C: Xử lý các sự kiện cấp thấp (low-level events) trong trình xử lý sự kiện rồi bắn lại chúng thành các sự kiện cấp cao (higher-level events)**. Ví dụ: khi click một button (low-level click event), ta đón nhận nó rồi bắn ra một custom event có ý nghĩa nghiệp vụ (như `approvalSubmit`) để các component khác lắng nghe. Đây là tư duy thiết kế component lỏng lẻo (loose coupling) cực đỉnh!

**❌ Tại sao đáp án sai:**
> **B.** Ngược đời! Để xử lý các hành động ở tầm ứng dụng (Application level), ta bắt buộc phải dùng Application Events chứ dùng Component Events thì nó không thể truyền đi xa ngoài phạm vi cây thư mục cha-con được.
> **D.** Sai bét! Salesforce khuyến nghị tối cao là nên ưu tiên sử dụng Component Events thay vì Application Events bất cứ khi nào có thể để tăng hiệu năng hệ thống và đảm bảo tính đóng gói.

**💡 Từ khóa ghi nhớ:** `Aura Event Best Practice -> **Logic tống vào Helper** + **Đổi sự kiện cấp thấp thành sự kiện nghiệp vụ cấp cao**!`

---

## Câu 279

**🔵 From which two locations can a developer determine the overall code coverage for a sandbox? (Choose two.)**

- **A.** The Apex Test Execution page ❌
- **B.** The Test Suite Run panel of the Developer Console ❌
- **C.** The Apex Classes setup page ✅
- **D.** The Tests tab of the Developer Console ✅

**📝 Dịch tiếng Việt:**
> Từ hai địa điểm chính thống nào trong Salesforce lập trình viên có thể xác định tỷ lệ phủ code kiểm thử tổng thể (overall code coverage) của môi trường Sandbox? (Chọn 2)

**💬 Giải thích gốc (English):**
> After the completed run, check the overall code coverage for your org by navigating to:
> 1. In the Quick Find Search type 'Apex' and click 'Apex Classes'
> 2. Click 'Estimate your organization's code coverage'

**✅ Tại sao đáp án đúng:**
> Chọn **C** và **D**.
- **C: Trang Apex Classes trong mục Setup**. Chỉ cần click vào link 'Estimate your organization's code coverage' thần thánh là nó tính ra ngay % overall code coverage toàn Org.
- **D: Tab Tests của trình biên dịch Developer Console**. Khi bạn mở Developer Console, chọn tab Tests ở thanh dưới, nhìn sang góc dưới bên phải sẽ thấy ngay con số Overall Code Coverage hiển thị rõ như ban ngày!

**❌ Tại sao đáp án sai:**
> **A.** Trang Apex Test Execution chỉ hiển thị trạng thái Pass/Fail của các lượt chạy test cụ thể, không hiển thị tổng lượng phủ sóng code toàn bộ Org.
> **B.** Bảng điều khiển Test Suite Run chỉ hiển thị kết quả chạy của các nhóm test, không hiển thị thống kê độ phủ sóng code tổng thể.

**💡 Từ khóa ghi nhớ:** `Xem tỷ lệ phủ test toàn Org -> Tìm **Apex Classes** trong Setup hoặc tab **Tests** trong Developer Console!`

---

## Câu 280

**🔵 A SSN__c custom field exists on the Candidate__c custom object. The field is used to store each candidate's social security number and is marked as Unique in the schema definition. As part of a data enrichment process, Universal Containers has a CSV file that contains updated data for all candidates in the system. The file contains each Candidate's social security number as a data point. Universal Containers wants to upload this information into Salesforce, while ensuring all data rows are correctly mapped to a candidate in the system. Which technique should the developer implement to streamline the data upload?**

- **A.** Update the SSN__c field definition to mark it as an External Id. ✅
- **B.** Upload the CSV into a custom object related to Candidate__c. ❌
- **C.** Create a before insert trigger to correctly map the records. ❌
- **D.** Create a Process Builder on the Candidate__c object to map the records. ❌

**📝 Dịch tiếng Việt:**
> Trên custom object Candidate__c có một trường custom kiểu Text tên SSN__c (lưu Social Security Number) được đánh dấu Unique. Doanh nghiệp có một file CSV chứa thông tin cập nhật của Candidate, bao gồm cả SSN__c. Lập trình viên nên làm gì để đảm bảo đống dữ liệu từ CSV được so khớp và cập nhật chính xác vào Candidate tương ứng một cách tối ưu nhất?

**💬 Giải thích gốc (English):**
> Mark the SSN__c field as an External ID on the Candidate__c object. This ensures that the CSV file's SSN values can be used to match and update existing records accurately.

**✅ Tại sao đáp án đúng:**
> Chọn **A: Cập nhật định nghĩa trường SSN__c để đánh dấu nó làm trường External ID**. Khi biến trường SSN__c thành khóa ngoài (External ID), các công cụ import dữ liệu (như Data Loader) sẽ tự động cho phép dùng trường này để so khớp dữ liệu khi gọi lệnh **Upsert**. Salesforce sẽ tự động biết bản ghi nào đã có để update, bản ghi nào chưa có để insert mà không cần dùng đến Salesforce ID gốc. Cực kỳ nhanh gọn!

**❌ Tại sao đáp án sai:**
> **B.** Tao them mot custom object phu trung gian chi lam phuc tap them co so du lieu va nhan doi cong suc tich hop vo nghia.
> **C.** Viet trigger map du lieu la giai phap code cong kenh, lang phi tai nguyen CPU cua Org va ton cong viet code phu test.
> **D.** Process Builder da bi khai tu (deprecated) va no cung khong ho tro import du lieu hay so khop truc tiep tu tep tin CSV dau vao.

**💡 Từ khóa ghi nhớ:** `So khớp cập nhật hàng loạt từ CSV qua trường độc nhất -> Biến trường độc nhất đó thành **External ID**!`

---

## Câu 281

**🔵 A developer created a Visualforce page and custom controller to display the account type field as shown below.
Custom controller code:
public class customCtrlr{
private Account theAccount;
public String actType;
public customCtrlr(){
theAccount = [SELECT Id, Type FROM Account WHERE Id = :ApexPages.currentPage().getParameters().get('id')];
actType = theAccount.Type;
}
}
Visualforce page snippet:
The Account Type is {!actType}
The value of the account type field is not being displayed correctly on the page. Assuming the custom controller is properly referenced on the Visualforce page, what should the developer do to correct the problem?**

- **A.** Convert theAccount.Type to a String. ❌
- **B.** Add a getter method for the actType attribute. ✅
- **C.** Add with sharing to the custom controller. ❌
- **D.** Change theAccount attribute to public. ❌

**📝 Dịch tiếng Việt:**
> Một lập trình viên tạo trang Visualforce và Custom Controller để hiển thị trường Account Type như dưới đây: [Code customCtrlr và VF]. Tuy nhiên, giá trị của trường Account Type không hiển thị đúng trên trang. Lập trình viên cần làm gì để sửa lỗi này?

**💬 Giải thích gốc (English):**
> By default, properties in Apex are private, meaning they can't be accessed directly by the Visualforce page. You need to make the actType property accessible by using the {get; set;} notation.
> public String actType { get; set; }

**✅ Tại sao đáp án đúng:**
> Chọn **B: Thêm một getter method cho thuộc tính actType**. Trong mô hình MVC của Visualforce, để một biến khai báo trong Apex Controller có thể xuất hiện và hiển thị giá trị ra ngoài giao diện trang VF, biến đó bắt buộc phải có phương thức getter (ví dụ: `public String getActType() { return actType; }` hoặc viết gọn kiểu hiện đại là `public String actType { get; set; }`). Thiếu getter là trang VF mù tịt không đọc được dữ liệu.

**❌ Tại sao đáp án sai:**
> **A.** Trường `Type` trên Account vốn dĩ đã là kiểu dữ liệu String rồi, ép kiểu làm gì cho thừa thãi.
> **C.** Khai báo `with sharing` chỉ để áp đặt luật chia sẻ bảo ghi (Sharing Rules) của hệ thống lên câu SOQL, chả liên quan gì đến việc hiển thị biến ra giao diện.
> **D.** VF page đang cố lấy giá trị từ biến `{!actType}` chứ không gọi trực tiếp `{!theAccount.Type}`. Do đó, việc đổi `theAccount` thành public chả giải quyết được vấn đề.

**💡 Từ khóa ghi nhớ:** `Biến Apex muốn hiển thị ra trang Visualforce -> Bắt buộc phải có **getter** (hoặc khai báo cụm **`{get; set;}`**).`

---

## Câu 282

**🔵 A developer wants to store a description of a product that can be entered on separate lines by a user during product setup and later displayed on a Visualforce page for shoppers. Which field type should the developer choose to ensure that the description will be searchable in the custom Apex SOQL queries that are written?**

- **A.** Text Area ✅
- **B.** Text ❌
- **C.** Text Area (Long) ❌
- **D.** Text Area (Rich) ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên muốn lưu trữ mô tả của sản phẩm (cho phép xuống dòng khi nhập liệu) để hiển thị lên trang Visualforce cho khách hàng xem. Đồng thời, trường này phải lọc tìm kiếm được bằng mệnh đề WHERE trong các câu SOQL tùy chỉnh. Chọn kiểu trường nào cho phù hợp?

**💬 Giải thích gốc (English):**
> Text Area: Lets users enter up to 255 characters that display on separate lines similar to a Description field.

**✅ Tại sao đáp án đúng:**
> Chọn **A: Text Area**. Trường kiểu **Text Area** cho phép người dùng nhập tối đa 255 ký tự hiển thị trên nhiều dòng khác nhau (thỏa mãn việc xuống dòng), và cực kỳ quan trọng: nó **hỗ trợ tìm kiếm lọc bằng mệnh đề WHERE LIKE** trong câu lệnh SOQL bình thường.

**❌ Tại sao đáp án sai:**
> **B.** Trường Text thường chỉ cho nhập trên 1 dòng duy nhất, không đáp ứng yêu cầu nhập liệu xuống dòng của người dùng.
> **C.** Text Area (Long) cho phép chứa tới 131,072 ký tự cực khủng nhưng Salesforce cấm tiệt sử dụng trường text lớn ở mệnh đề lọc WHERE của SOQL.
> **D.** Text Area (Rich) chứa định dạng HTML phức tạp và tương tự câu C, bị Salesforce chặn hoàn toàn khỏi khả năng so khớp lọc WHERE trong SOQL.

**💡 Từ khóa ghi nhớ:** `Vừa xuống được dòng + Vừa lọc được bằng mệnh đề WHERE trong SOQL -> Chỉ dùng **Text Area** thường (không dùng Long/Rich)!`

---

## Câu 283

**🔵 How should a developer create a new custom exception class?**

- **A.** public class CustomException extends Exception{} ✅
- **B.** CustomException ex = new (CustomException)Exception(); ❌
- **C.** public class CustomException implements Exception{} ❌
- **D.** (Exception)CustomException ex = new Exception(); ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên làm thế nào để tự định nghĩa một custom exception class (lớp ngoại lệ tùy chỉnh) trong Apex?

**💬 Giải thích gốc (English):**
> To create your custom exception class, extend the built-in Exception class and make sure your class name ends with the word Exception, such as “MyException” or “PurchaseException”. All exception classes extend the system-defined base class Exception, and therefore, inherits all common Exception methods.
> This example defines a custom exception called MyException.
> public class MyException extends Exception {}

**✅ Tại sao đáp án đúng:**
> Chọn **A: `public class CustomException extends Exception{}`**. Đây là luật cứng của Apex: để tạo một lớp ngoại lệ tùy chỉnh, class đó bắt buộc phải có tên kết thúc bằng từ khóa **`Exception`** (ví dụ: `CustomException`, `MyApiException`...) và phải kế thừa từ lớp Exception chuẩn của hệ thống thông qua từ khóa **`extends Exception`**.

**❌ Tại sao đáp án sai:**
> **B.** Cú pháp khai báo gán ép kiểu ngược ngạo, hoàn toàn sai ngữ pháp cơ bản của ngôn ngữ Apex.
> **C.** Dùng từ khóa `implements` là sai lệch nghiêm trọng, Exception là lớp cha (Class) chứ không phải Interface để implements.
> **D.** Cú pháp gán biến sai ngữ pháp, gây lỗi biên dịch compiler ngay lập tức.

**💡 Từ khóa ghi nhớ:** `Custom Exception -> Tên class bắt buộc có đuôi **Exception** + dùng từ khóa **extends Exception**!`

---

## Câu 284

**🔵 A developer identifies the following triggers on the Expense__c object: deteleExpense, applyDefaultsToExpense, validateExpenseUpdate; The triggers process before delete, before insert, and before update events respectively. Which two techniques should the developer implement to ensure trigger best practices are followed? (Choose two.)**

- **A.** Unify the before insert and before update triggers and use Process Builder for the delete action. ❌
- **B.** Create helper classes to execute the appropriate logic when a record is saved. ✅
- **C.** Maintain all three triggers on the Expense__c object, but move the Apex logic out of the trigger definition. ❌
- **D.** Unify all three triggers in a single trigger on the Expense__c object that includes all events. ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên phát hiện có 3 trigger khác nhau trên đối tượng Expense__c gồm: deleteExpense, applyDefaultsToExpense, validateExpenseUpdate tương ứng chạy ở before delete, before insert, và before update. Hai kỹ thuật nào nên được áp dụng để đảm bảo tuân thủ tốt nhất các thực hành thiết kế Trigger (Trigger Best Practices)? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> Chọn **B** và **D**.
- **B: Tạo các helper classes để thực thi logic phù hợp khi bản ghi được lưu**. Tách toàn bộ logic tính toán, xử lý nghiệp vụ ra khỏi trigger và tống vào các lớp **Helper Class** (hay Handler Class). Trigger chỉ nên làm nhiệm vụ đón nhận sự kiện rồi điều phối gọi helper (Logicless Trigger).
- **D: Gom cả 3 trigger lại thành một trigger duy nhất trên Expense__c chứa tất cả các sự kiện**. Đây là thực hành thiết kế tối thượng 'One Trigger per Object' để dễ dàng kiểm soát thứ tự thực thi và tránh xung đột.

**❌ Tại sao đáp án sai:**
> **A.** Process Builder đã đi vào dĩ vãng và không hỗ trợ tốt sự kiện delete.
> **C.** Giữ nguyên 3 trigger chạy riêng biệt trên một object là vi phạm nghiêm trọng best practice, dễ gây lỗi đệ quy không thể kiểm soát.

**💡 Từ khóa ghi nhớ:** `Best practice Trigger -> Luôn nhớ: **One Trigger per Object** (Gom 1 trigger duy nhất) + **Logicless Trigger** (Tách logic vào Helper)!`

---

## Câu 285

**🔵 Universal Containers has implemented an order management application. Each Order can have one or more Order Line items. The Order Line object is related to the Order via a master-detail relationship. For each Order Line item, the total price is calculated by multiplying the Order Line item price with the quantity ordered. What is the best practice to get the sum of all Order Line item totals on the Order record?**

- **A.** Roll-up summary field ✅
- **B.** Quick action ❌
- **C.** Apex trigger ❌
- **D.** Formula field ❌

**📝 Dịch tiếng Việt:**
> Universal Containers triển khai app quản lý đơn hàng. Mỗi Order có một hoặc nhiều Order Line con liên kết qua quan hệ Master-Detail. Với mỗi Order Line, giá tổng được tính bằng cách nhân đơn giá với số lượng. Thực hành tốt nhất để hiển thị tổng tiền của tất cả các dòng Order Line lên bản ghi Order cha là gì?

**✅ Tại sao đáp án đúng:**
> Chọn **A: Roll-up summary field**. Vì mối quan hệ giữa Order và Order Line là Master-Detail, cách tối ưu, chuẩn chỉ, no-code và được Salesforce khuyến nghị số 1 để tính tổng từ con lên cha là tạo một trường **Roll-up Summary** trên Order cha và chọn hàm SUM.

**❌ Tại sao đáp án sai:**
> **B.** Quick Action dùng để mở giao diện hành động nhanh chứ không có chức năng tính toán tổng hợp cơ sở dữ liệu.
> **C.** Viết trigger Apex để tính toán bằng code là giải pháp cồng kềnh, lãng phí tài nguyên CPU và tốn công viết code phủ test khi no-code đã giải quyết cực đẹp.
> **D.** Formula field chỉ tính toán trên nội bộ bản ghi hoặc kéo dữ liệu từ cha xuống con, chứ không thể tính tổng ngược từ các bản ghi con lên bản ghi cha được.

**💡 Từ khóa ghi nhớ:** `Tính tổng bản ghi con lên cha Master-Detail -> Luôn ưu tiên dùng **Roll-up Summary field**!`

---

## Câu 286

**🔵 Which three statements are accurate about debug logs? (Choose three.)**

- **A.** Only the 20 most recent debug loos for a user are kept. ❌
- **B.** System debug logs are retained for 24 hours. ✅
- **C.** Debug log levels are cumulative, where FINE log level includes all events logged at the DEBUG, INFO, WARN, and ERROR levels. ✅
- **D.** The maximum size of a debug log is 5 MB. ❌
- **E.** Debug logs can be set for specific users, classes, and triggers. ✅

**📝 Dịch tiếng Việt:**
> Ba phát biểu nào sau đây là chính xác về debug logs? (Chọn 3)

**💬 Giải thích gốc (English):**
> System debug logs are retained for 24 hours. Monitoring debug logs are retained for seven days.
> Each debug level includes one of the following log levels for each log category. The levels are listed from lowest to highest. Specific events are logged based on the combination of category and levels. Most events start being logged at the INFO level. The level is cumulative, that is, if you select FINE, the log also includes all events logged at the DEBUG, INFO, WARN, and ERROR levels.
> To activate debug logging for users, Apex classes, and Apex triggers, configure trace flags and debug levels in the Salesforce Developer Console or in Salesforce Setup.

**✅ Tại sao đáp án đúng:**
> Chọn **B**, **C** và **E**.
- **B: System debug logs được hệ thống giữ lại trong vòng 24 giờ**. Sau 24 tiếng, các file log này sẽ bị tự động dọn dẹp sạch sẽ để giải phóng dung lượng cho máy chủ Salesforce.
- **C: Cấp độ log (Log Levels) có tính tích lũy (cumulative)**. Cấp thấp hơn, chi tiết hơn (như FINE) sẽ tự động bao gồm toàn bộ các sự kiện được ghi nhận ở các cấp độ cao hơn (như DEBUG, INFO, WARN, ERROR).
- **E: Debug logs có thể được thiết lập riêng biệt cho từng User, Class Apex và Trigger cụ thể**. Bạn có thể cắm Trace Flags để chỉ ghi log cho đúng đối tượng mình đang muốn khoanh vùng debug, rất tối ưu!

**❌ Tại sao đáp án sai:**
> **A.** Salesforce giới hạn tổng dung lượng lưu trữ log trên Org (250MB) chứ không giới hạn cứng con số 20 file log gần nhất của một user.
> **D.** Giới hạn dung lượng tối đa cho mỗi file debug log là **250 MB** chứ không phải 5 MB (ở giao diện Dev Console nó sẽ tự động cắt ngắn nếu log quá dài).

**💡 Từ khóa ghi nhớ:** `Debug Logs: Giữ trong **24 giờ**, log levels có tính **tích lũy**, cắm được cho **User/Class/Trigger** cụ thể!`

---

## Câu 287

**🔵 The Account object has a custom Percent field, Rating, defined with a length of 2 with 0 decimal places. An Account record has the value of 50% in its Rating field and is processed in the Apex code below after being retrieved from the database with SOQL.
public void processAccount(){
Decimal acctScore = acct.Rating__c * 100;
}
What is the value of acctScore after this code executes?**

- **A.** 5 ❌
- **B.** 50 ❌
- **C.** 500 ❌
- **D.** 5000 ✅

**📝 Dịch tiếng Việt:**
> Trên Account có một trường custom kiểu Percent tên là Rating__c được cấu hình độ dài 2 ký tự, không lấy số thập phân. Một bản ghi Account có giá trị 50% ở trường Rating__c và được truy vấn xử lý trong code Apex: `Decimal acctScore = acct.Rating__c * 100;`. Hỏi giá trị của biến acctScore sau khi chạy xong là bao nhiêu?

**💬 Giải thích gốc (English):**
> With the Percent field defined with 0 decimal places, the value stored in the Rating field is 50, not 0.50. When the code executes, it multiplies 50 by 100, resulting in an acctScore of 5000.

**✅ Tại sao đáp án đúng:**
> Chọn **D: 5000**. Đây là cú lừa kinh điển của Salesforce! Khi bạn nhập 50% trên giao diện, Salesforce thực chất lưu giá trị số thực thô là **50** (chứ không phải 0.5). Khi truy vấn lên code Apex, biến `acct.Rating__c` sẽ nhận giá trị là `50`. Do đó, phép nhân trong code: `50 * 100` sẽ ra kết quả là **5000**. Muốn tính đúng tỉ lệ thực tế, bạn phải tự chia cho 100!

**❌ Tại sao đáp án sai:**
> **A.** Tính toán sai lệch hoàn toàn.
> **B.** Sai vì nghĩ Percent trong code Apex tự động chia cho 100 thành 0.50 để nhân với 100 ra 50.
> **C.** Sai do nhầm lẫn thứ tự tính toán thập phân.

**💡 Từ khóa ghi nhớ:** `Trong code Apex, trường Percent nhận giá trị **thô** không chia 100 (ví dụ: 50% = 50, 75% = 75)!`

---

## Câu 288

**🔵 Which statement is true about developing in a multi-tenant environment?**

- **A.** Apex Sharing controls access to records from multiple tenants on the same instance. ❌
- **B.** Org-level data security controls which users can see data from multiple tenants on the same instance. ❌
- **C.** Governor limits prevent Apex from impacting the performance of multiple tenants on the same instance. ✅
- **D.** Global Apex classes can be referenced from multiple tenants on the same instance. ❌

**📝 Dịch tiếng Việt:**
> Phát biểu nào sau đây là ĐÚNG khi nói về việc lập trình phát triển ứng dụng trong môi trường đa khách thuê (multi-tenant) của Salesforce?

**💬 Giải thích gốc (English):**
> Governor limits prevent Apex from impacting the performance of multiple tenants on the same instance. These limits ensure that no single tenant's code can monopolize shared resources, maintaining performance and stability across the environment.

**✅ Tại sao đáp án đúng:**
> Chọn **C: Các giới hạn governor limits giúp ngăn chặn việc code Apex làm ảnh hưởng đến hiệu năng của các khách thuê khác chạy chung trên cùng một máy chủ vật lý**. Trong thế giới multi-tenant, hàng nghìn Org dùng chung tài nguyên phần cứng. **Governor Limits** đóng vai trò là hàng rào bảo vệ tối thượng, đảm bảo không có bất kỳ ông nào chạy code lặp vô tận hay ngốn hết tài nguyên làm ảnh hưởng đến các ông hàng xóm.

**❌ Tại sao đáp án sai:**
> **A.** Apex Sharing chỉ giúp chia sẻ bản ghi bảo mật trong nội bộ một Org duy nhất, hoàn toàn không có chuyện chia sẻ chéo record giữa các tenant độc lập được.
> **B.** Bảo mật cấp Org kiểm soát quyền truy cập của người dùng trong nội bộ Org đó chứ không thể nhìn thấy dữ liệu của Org khác chạy chung instance.
> **D.** Từ khóa global trên Apex class hỗ trợ gọi chéo code trong các namespace nội bộ Org chứ không cho phép Org khác truy cập trực tiếp database.

**💡 Từ khóa ghi nhớ:** `Multi-tenant (Đa khách thuê) -> **Governor limits** sinh ra để bảo vệ hiệu năng dùng chung!`

---

## Câu 289

**🔵 Universal Containers decides to use exclusively declarative development to build out a new Salesforce application. Which three options should be used to build out the database layer for the application? (Choose three.)**

- **A.** Process Builder ❌
- **B.** Roll-up summaries ✅
- **C.** Triggers ❌
- **D.** Relationships ✅
- **E.** Custom objects and fields ✅

**📝 Dịch tiếng Việt:**
> Universal Containers quyết định chỉ sử dụng công cụ khai báo (declarative/no-code) để xây dựng một ứng dụng Salesforce mới. Ba tùy chọn nào nên được dùng để thiết lập lớp Cơ sở dữ liệu (Database Layer) cho ứng dụng? (Chọn 3)

**💬 Giải thích gốc (English):**
> Database Layer
> Declarative: Custom Objects, Fields, Relationships, Rollups
> Coding: Apex Triggers

**✅ Tại sao đáp án đúng:**
> Chọn **B**, **D** và **E**.
- **B: Roll-up summaries** (Trường tổng hợp dữ liệu no-code từ con lên cha).
- **D: Relationships** (Thiết lập các mối liên kết Lookup, Master-Detail no-code).
- **E: Custom objects and fields** (Tạo bảng và trường dữ liệu hoàn toàn bằng kéo thả click chuột).
- Đây chính như bộ ba nguyên tử cấu thành nên lớp Database Layer (Cơ sở dữ liệu) hoàn chỉnh mà không cần một dòng code nào.

**❌ Tại sao đáp án sai:**
> **A.** Process Builder là công cụ tự động hóa xử lý logic (Logic Layer), không phải cấu trúc lưu trữ cơ sở dữ liệu.
> **C.** Triggers là code Apex dùng để xử lý logic (Logic Layer), đi ngược lại tiêu chí 'declarative' (no-code) của đề bài.

**💡 Từ khóa ghi nhớ:** `Database Layer no-code -> Auto chọn: **Custom objects/fields**, **Relationships** và **Roll-up summaries**!`

---

## Câu 290

**🔵 A developer must implement a CheckPaymentProcessor class that provides check processing payment capabilities that adhere to what is defined for payments in the PaymentProcessor interface.
public interface PaymentProcessor {
void pay(Decimal amount);
}
Which is the correct implementation to use the PaymentProcessor interface class?**

- **A.** public class CheckPaymentProcessor implements PaymentProcessor{ public void pay(Decimal amount); } ❌
- **B.** public class CheckPaymentProcessor implements PaymentProcessor{ public void pay(Decimal amount){} } ✅
- **C.** public class CheckPaymentProcessor extends PaymentProcessor{ public void pay(Decimal amount){} } ❌
- **D.** public class CheckPaymentProcessor extends PaymentProcessor{ public void pay(Decimal amount); } ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên cần tạo class `CheckPaymentProcessor` để thực hiện xử lý thanh toán tuân thủ đúng phương thức `pay` được ký mẫu trong Interface `PaymentProcessor`: [Interface Code]. Cách viết nào sau đây là đúng cú pháp Apex?

**💬 Giải thích gốc (English):**
> You need to implement the PaymentProcessor interface and provide the required pay method definition.

**✅ Tại sao đáp án đúng:**
> Chọn **B: `public class CheckPaymentProcessor implements PaymentProcessor{ public void pay(Decimal amount){} }`**. Đây là cú pháp OOP chuẩn chỉnh của Apex: class con muốn hiện thực hóa Interface thì bắt buộc phải dùng từ khóa **`implements`** và phải viết đầy đủ phần thân hàm chứa cặp dấu ngoặc nhọn `{}` (dù bên trong chưa có dòng xử lý nào) để cam kết thực hiện.

**❌ Tại sao đáp án sai:**
> **A.** Hàm `pay` kết thúc bằng dấu chấm phẩy mà không có cặp dấu ngoặc nhọn thân hàm `{}` chỉ được dùng ở định nghĩa Interface, đem vào class thường sẽ bị lỗi biên dịch ngay.
> **C.** Sử dụng từ khóa `extends` đối với Interface là sai lệch nghiêm trọng cú pháp lập trình.
> **D.** Sai cú pháp vì vừa dùng từ khóa `extends` vừa thiếu cặp dấu ngoặc nhọn thân hàm.

**💡 Từ khóa ghi nhớ:** `Class hiện thực hóa Interface -> Bắt buộc dùng **`implements`** + Viết đầy đủ thân hàm chứa cặp ngoặc nhọn **`{}`**!`

---

## Câu 291

**🔵 Universal Containers has a large number of custom applications that were built using a third-party JavaScript framework and exposed using Visualforce pages. The company wants to update these applications to apply styling that resembles the look and feel of Lightning Experience. What should the developer do to fulfill the business request in the quickest and most effective manner?**

- **A.** Set the attribute enableLightning to true in the definition. ❌
- **B.** Enable Available for Lightning Experience, Lightning Communities, and the mobile app on Visualforce pages used by the custom application. ❌
- **C.** Incorporate the Salesforce Lightning Design System CSS stylesheet into the JavaScript applications. ✅
- **D.** Rewrite all Visualforce pages as Lightning components. ❌

**📝 Dịch tiếng Việt:**
> Universal Containers sở hữu một loạt các ứng dụng tùy chỉnh được xây dựng bằng thư viện JavaScript của bên thứ ba (như React, Angular...) nhúng trong trang Visualforce. Công ty muốn cập nhật nhanh nhất giao diện của các app này theo kiểu dáng hiện đại của Lightning Experience. Lập trình viên nên làm gì?

**💬 Giải thích gốc (English):**
> With Lightning stylesheets, it’s easy to tweak your existing Visualforce pages so they’ll display with classic styling in Salesforce Classic and Lightning styling in Lightning Experience.
> 1. From Setup, enter Visualforce in the Quick Find box, then select Visualforce Pages.
> 2. Click Edit next to the Visualforce page.
> 3. Add the lightningStylesheets="true" attribute to the initial <apex:page> component in the Visualforce markup.
> <apex:page standardController="Account" lightningStyleSheets="true">

**✅ Tại sao đáp án đúng:**
> Chọn **C: Tích hợp trực tiếp bộ CSS của Salesforce Lightning Design System (SLDS) vào ứng dụng JavaScript đó**. Vì ứng dụng này được vẽ trực tiếp bằng thư viện JS ngoài (render DOM riêng), các công cụ tự động chuyển giao diện của Salesforce sẽ bất lực. Giải pháp nhanh và hiệu quả nhất là nhúng thẳng bộ CSS của **Salesforce Lightning Design System (SLDS)** vào app JS đó để tự áp dụng các class style chuẩn của Salesforce.

**❌ Tại sao đáp án sai:**
> **A.** Không tồn tại thuộc tính `enableLightning` trong thẻ khai báo Visualforce page, đồ fake tự chế thôi bro!
> **B.** Tùy chọn Available for Lightning chỉ giúp hiển thị trang Visualforce trên menu Lightning chứ không có khả năng tự động đổi CSS của JS framework ngoài.
> **D.** Viết lại toàn bộ trang Visualforce thành Lightning component là giải pháp cực kỳ tốn công sức và thời gian, không đáp ứng yêu cầu 'nhanh nhất'.

**💡 Từ khóa ghi nhớ:** `Đổi style cho JS App ngoài nhúng trong VF -> Tích hợp trực tiếp bộ **Salesforce Lightning Design System (SLDS) CSS**!`

---

## Câu 292

**🔵 When a user edits the Postal Code on an Account, a custom Account text field named "Timezone" must be updated based on the values in a PostalCodeToTimezone__c custom object. Which two automation tools can be used to implement this feature? (Choose two.)**

- **A.** Quick actions ❌
- **B.** Approval Process ❌
- **C.** Record-triggered flow ✅
- **D.** Account trigger ✅

**📝 Dịch tiếng Việt:**
> Khi người dùng sửa trường Postal Code trên Account, một trường text tùy chỉnh tên 'Timezone' phải được tự động cập nhật dựa trên bảng tra cứu đối tượng PostalCodeToTimezone__c. Hai công cụ tự động hóa nào thực hiện được việc này? (Chọn 2)

**💬 Giải thích gốc (English):**
> To update the "Timezone" field based on the Postal Code changes, you can use:
> 1. Record-triggered flow: This can be set up to run when the Postal Code is edited, updating the Timezone field accordingly.
> 2. Account trigger: This can be written to handle changes in the Postal Code and update the Timezone field.
> Both methods will effectively handle the automation you need.

**✅ Tại sao đáp án đúng:**
> Chọn **C** và **D**.
- **C: Record-triggered flow**. Đây là công cụ tự động hóa no-code chuẩn của Salesforce, hỗ trợ hoàn hảo việc query chọc sang bảng khác để lấy dữ liệu rồi update ngược lại bản ghi hiện tại.
- **D: Account trigger**. Code Apex trigger xử lý hoàn hảo khâu query và map dữ liệu một cách cực kỳ mạnh mẽ, tùy biến sâu.

**❌ Tại sao đáp án sai:**
> **A.** Quick actions chỉ hiển thị nút bấm hành động nhanh trên giao diện để người dùng nhập liệu, không tự động chạy ngầm cập nhật trường chéo bảng được.
> **B.** Approval Process dùng cho quy trình xét duyệt hồ sơ chứng từ, không dùng để tự động cập nhật trường tra cứu chéo bảng.

**💡 Từ khóa ghi nhớ:** `Tự động cập nhật trường bằng cách truy vấn bảng khác -> Chỉ dùng **Record-triggered Flow** hoặc **Apex Trigger**!`

---

## Câu 293

**🔵 What are two uses for External IDs? (Choose two.)**

- **A.** To create relationships between records imported from an external system. ✅
- **B.** To create a record in a development environment with the same Salesforce ID as in another environment ❌
- **C.** To identify the sObject type in Salesforce ❌
- **D.** To prevent an import from creating duplicate records using Upsert ✅

**📝 Dịch tiếng Việt:**
> Hai vai trò nổi bật của việc sử dụng trường External ID trong Salesforce là gì? (Chọn 2)

**💬 Giải thích gốc (English):**
> External IDs are commonly used to establish relationships between records imported from an external system. By using an External ID field, you can link records in Salesforce to corresponding records in an external system, facilitating data integration and synchronization.
> One of the key uses of External IDs is to prevent duplicate records during data imports by using the Upsert operation. By specifying an External ID field as the matching criteria, Salesforce can identify existing records based on that field and update them instead of creating duplicates.

**✅ Tại sao đáp án đúng:**
> Chọn **A** và **D**.
- **A: Thiết lập nhanh các mối quan hệ liên kết (relationships) giữa các bản ghi con-cha khi import từ hệ thống ngoài**. Bạn có thể map liên kết trực tiếp qua External ID mà không cần biết ID của Salesforce.
- **D: Làm khóa đối chiếu giúp ngăn chặn việc tạo bản ghi trùng lặp khi chạy lệnh nạp dữ liệu Upsert**. Salesforce sẽ tự động biết bản ghi nào đã có để update, bản ghi nào chưa có để insert, đảm bảo tính toàn vẹn dữ liệu.

**❌ Tại sao đáp án sai:**
> **B.** Salesforce ID do hệ thống tự sinh ngẫu nhiên khi chèn bản ghi và là duy nhất trên toàn cầu, không ai có thể dùng External ID để ép đặt Salesforce ID trùng nhau chéo Org được.
> **C.** External ID không dùng để xác định kiểu sObject (Account, Contact) của bản ghi.

**💡 Từ khóa ghi nhớ:** `External ID: Dùng làm **khóa liên kết dữ liệu hệ thống ngoài** + **Khóa đối chiếu cho lệnh UPSERT tránh trùng**!`

---

## Câu 294

**🔵 An Apex method, getAccounts, that returns a List of Accounts given a searchTerm, is available for Lightning Web components to use. What is the correct definition of a Lightning Web component property that uses the getAccounts method?**

- **A.** @wire(getAccounts, { searchTerm: '$searchTerm'})  accountList; ✅
- **B.** @AuraEnabled(getAccounts, '$searchTerm') accountList; ❌
- **C.** @AuraEnabled(getAccounts, { searchTerm: '$searchTerm'}) accountList; ❌
- **D.** @wire(getAccounts, '$searchTerm') accountList; ❌

**📝 Dịch tiếng Việt:**
> Một phương thức Apex, `getAccounts`, trả về một List các Account dựa trên một `searchTerm`, có sẵn để LWC sử dụng. Định nghĩa đúng của một thuộc tính (property) Lightning Web Component sử dụng phương thức `getAccounts` là gì?

**💬 Giải thích gốc (English):**
> To read Salesforce data, Lightning web components use a reactive wire service. Use @wire in a component’s JavaScript class to specify an Apex method. You can @wire a property or a function to receive the data. To operate on the returned data, @wire a function.

**✅ Tại sao đáp án đúng:**
> Chọn **A: `@wire(getAccounts, { searchTerm: '$searchTerm'}) accountList;`**. Đây là cú pháp chuẩn cơm mẹ nấu của LWC để kết nối dữ liệu (wire) với Apex:
- Sử dụng decorator `@wire`.
- Tên phương thức import: `getAccounts`.
- Tham số truyền dưới dạng object: `{ searchTerm: '$searchTerm' }`. Dấu nháy đơn kết hợp kí tự `$` giúp cho biến `searchTerm` trở thành **reactive** (tự động kích hoạt gọi lại Apex khi giá trị thay đổi).

**❌ Tại sao đáp án sai:**
> **B.** Sai cú pháp hoàn toàn cho một decorator trong LWC JS.
> **C.** `@AuraEnabled` là annotation viết bên file class Apex chứ bên file Javascript của LWC mà gõ cái này là ăn lỗi biên dịch ngay.
> **D.** Truyền tham số thiếu cặp dấu ngoặc nhọn `{}` định dạng object để map tham số.

**💡 Từ khóa ghi nhớ:** `LWC `@wire` kết nối Apex -> Phải dùng **`@wire(TênHàm, { param: '$biếnReactive' })`**!`

---

## Câu 295

**🔵 Which three declarative fields are correctly mapped to variable types in Apex? (Choose three.)**

- **A.** Number maps to Decimal. ✅
- **B.** Number maps to Integer. ❌
- **C.** TextArea maps to List of type String. ❌
- **D.** Date/Time maps to Dateline. ✅
- **E.** Checkbox maps to Boolean. ✅

**📝 Dịch tiếng Việt:**
> Ba kiểu trường khai báo (declarative fields) nào sau đây được ánh xạ (map) hoàn toàn ĐÚNG sang các kiểu dữ liệu tương ứng trong Apex? (Chọn 3)

**✅ Tại sao đáp án đúng:**
> Chọn **A**, **D** và **E**.
- **A: Number maps to Decimal**. Trường Number trong Salesforce có thể chứa số lẻ/thập phân nên được map sang kiểu Decimal trong Apex để đảm bảo tính chính xác toán học.
- **D: Date/Time maps to DateTime**. (Đề thi gốc bị typo chữ Dateline nhưng về kỹ thuật là DateTime). Trường Date/Time được map sang kiểu DateTime trong Apex để lưu trữ đầy đủ ngày giờ.
- **E: Checkbox maps to Boolean**. Trường Checkbox chỉ có hai trạng thái Check/Uncheck tương đương với `true`/`false`, map hoàn hảo sang kiểu dữ liệu Boolean trong Apex.

**❌ Tại sao đáp án sai:**
> **B.** Trường Number có thể chứa phần thập phân, nếu map cứng sang Integer sẽ bị crash lỗi hoặc mất mát dữ liệu số lẻ.
> **C.** Trường TextArea chỉ đơn giản là một String lớn chứa các ký tự xuống dòng, cấm tự động map thành List<String>.

**💡 Từ khóa ghi nhớ:** `Ánh xạ trường Salesforce sang Apex -> **Checkbox -> Boolean**, **Number -> Decimal**, và **Date/Time -> DateTime**!`

---

## Câu 296

**🔵 Which two practices should be used for processing records in a trigger? (Choose two.)**

- **A.** Use a Map to reduce the number of SOQL calls. ✅
- **B.** Use @future methods to handle DML operations. ❌
- **C.** Use a Set to ensure unique values in a query filter. ✅
- **D.** Use (callout=true) to update an external system. ❌

**📝 Dịch tiếng Việt:**
> Hai thực hành tốt nhất (best practices) nào lập trình viên nên tuân thủ khi xử lý danh sách bản ghi trong một Apex Trigger để đảm bảo chạy mượt mà bulkified? (Chọn 2)

**💬 Giải thích gốc (English):**
> Using Maps and Sets in Bulk Triggers
> Set and map data structures are critical for successful coding of bulk triggers. Sets can be used to isolate distinct records, while maps can be used to hold query results organized by record ID.

**✅ Tại sao đáp án đúng:**
> Chọn **A** và **C**.
- **A: Sử dụng cấu trúc dữ liệu Map để lưu trữ các bản ghi query được theo ID cha, giảm số lượng gọi SOQL**. Giúp bạn tra cứu nhanh record liên quan trong bộ nhớ mà không cần phải viết thêm SOQL trong các vòng lặp (tránh dính SOQL Governor Limit).
- **C: Sử dụng cấu trúc Set để lưu danh sách ID lọc duy nhất**. Tối ưu hóa bộ lọc WHERE IN trong các câu lệnh truy vấn SOQL để chạy siêu nhanh và tiết kiệm bộ nhớ.

**❌ Tại sao đáp án sai:**
> **B.** Không dùng `@future` bừa bãi chỉ để chạy DML update vì phương thức future chạy bất đồng bộ không kiểm soát được thứ tự lưu và dễ gây khóa bản ghi (record locking).
> **D.** Không thể khai báo callout trực tiếp trong trigger (kể cả dùng callout=true), bắt buộc trigger phải gọi qua helper method bất đồng bộ `@future(callout=true)` để tránh treo transaction.

**💡 Từ khóa ghi nhớ:** `Tối ưu Trigger (Bulkify) -> Luôn sử dụng bộ đôi nguyên tử: **SET (để lọc duy nhất)** và **MAP (để lưu cache đối chiếu)**!`

---

## Câu 297

**🔵 A developer wants to mark each Account in a List as either Active or Inactive, based on the value in the LastModifiedDate field of each Account being greater than 90 days in the past. Which Apex technique should the developer use?**

- **A.** A for loop, with a switch statement inside ❌
- **B.** A switch statement, with a for loop inside ❌
- **C.** An if-else statement, with a for loop inside ❌
- **D.** A for loop, with an if-else statement inside ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên muốn duyệt qua một danh sách Account và đánh dấu mỗi Account là Active hoặc Inactive dựa trên việc trường LastModifiedDate của từng bản ghi có lớn hơn 90 ngày trước hay không. Kỹ thuật Apex nào lập trình viên nên sử dụng?

**💬 Giải thích gốc (English):**
> To mark each Account as Active or Inactive based on the LastModified field value, the developer should use a for loop, with an if/else statement inside. This technique allows the developer to iterate through each account and apply the conditional logic to determine the status based on the 90-day threshold.

**✅ Tại sao đáp án đúng:**
> Chọn **D: Sử dụng vòng lặp for, bên trong bọc câu lệnh if-else**. Kịch bản cực kỳ kinh đoán: dùng một vòng lặp `for` để duyệt qua từng Account trong danh sách, và dùng câu lệnh điều kiện `if-else` ở bên trong vòng lặp để so sánh ngày tháng của từng bản ghi rồi gán nhãn trạng thái tương ứng.

**❌ Tại sao đáp án sai:**
> **A.** Switch statement chỉ dùng để so khớp các giá trị hằng số rời rạc cụ thể, không hỗ trợ so sánh toán tử điều kiện lớn hơn/nhỏ hơn phức tạp của ngày tháng.
> **B.** Đặt switch ngoài for lặp là hoàn toàn sai trình tự logic xử lý danh sách.
> **C.** Đặt if-else ngoài for lặp không thể can thiệp xử lý điều kiện cho từng bản ghi độc lập bên trong danh sách được.

**💡 Từ khóa ghi nhớ:** `Duyệt danh sách + xử lý logic điều kiện động cho từng bản ghi -> Dùng vòng lặp **FOR** bọc câu lệnh điều kiện **IF-ELSE** bên trong!`

---

## Câu 298

**🔵 A developer has identified a method in an Apex class that performs resource intensive actions in memory by iterating over the result set of a SOQL statement on the account. The method also performs a DML statement to save the changes to the database. Which two techniques should the developer implement as a best practice to ensure transaction control and avoid exceeding governor limits? (Choose two.)**

- **A.** Use the @ReadOnly annotation to bypass the number of rows returned by a SOQL. ❌
- **B.** Use partial DML statements to ensure only valid data is committed. ❌
- **C.** Use the System.Limit class to monitor the current CPU governor limit consumption. ✅
- **D.** Use the Database.Savepoint method to enforce database integrity. ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên phát hiện một phương thức trong class Apex thực hiện các hành động tốn nhiều tài nguyên bộ nhớ bằng cách duyệt qua kết quả truy vấn SOQL trên đối tượng Account, đồng thời thực hiện lệnh DML để lưu thay đổi. Hai kỹ thuật nào nên được áp dụng để đảm bảo kiểm soát transaction và tránh vượt quá governor limits? (Chọn 2)

**💬 Giải thích gốc (English):**
> The developer should implement the following best practices to ensure transaction control and avoid exceeding governor limits:
> Use the System.Limit class to monitor the current CPU governor limit consumption: This helps keep track of how close the code is to hitting governor limits and can allow for proactive management.
> Use the Database.Savepoint method to enforce database integrity: Savepoints allow the developer to roll back to a certain point in the transaction if necessary, which is critical for maintaining data integrity during complex operations.

**✅ Tại sao đáp án đúng:**
> Chọn **C** và **D**.
- **C: Sử dụng lớp System.Limit để giám sát tài nguyên CPU tiêu thụ hiện tại**. Lớp `System.Limit` cung cấp các phương thức cực xịn như `System.Limits.getCpuTime()` hay `System.Limits.getLimitCpuTime()` giúp bạn chủ động đo đạc tài nguyên CPU tiêu thụ xem đã sắp chạm trần chưa để ngắt luồng an toàn.
- **D: Sử dụng phương thức Database.Savepoint để đảm bảo tính toàn vẹn dữ liệu**. Cho phép bạn thiết lập điểm neo giao dịch. Nếu giữa chừng xảy ra lỗi vượt giới hạn hoặc lỗi logic, bạn có thể gọi `Database.rollback(sp)` để hoàn trả toàn bộ database về trạng thái nguyên vẹn ban đầu.

**❌ Tại sao đáp án sai:**
> **A.** Annotation `@ReadOnly` chỉ dùng cho Web Services hoặc JS Remoting để tăng giới hạn bản ghi SOQL đọc, chứ nó không giúp bạn thực hiện các thao tác sửa đổi dữ liệu DML được (DML bị cấm hoàn toàn dưới `@ReadOnly`).
> **B.** Dùng partial DML (`Database.insert(list, false)`) chỉ giúp lưu những bản ghi đúng và bỏ qua bản ghi lỗi, chứ không hề có tác dụng kiểm soát an toàn toàn bộ transaction hay giúp giảm lượng CPU tiêu thụ.

**💡 Từ khóa ghi nhớ:** `Kiểm soát Transaction -> Dùng **Savepoint / Rollback**; Giám sát tài nguyên -> Gọi các hàm trong lớp **`System.Limit`**!`

---

## Câu 299

**🔵 What should a developer use to script the deployment and unit test execution as part of continuous integration?**

- **A.** Developer Console ❌
- **B.** Salesforce CLI ✅
- **C.** VS Code ❌
- **D.** Execute Anonymous ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên nên sử dụng công cụ gì để viết script tự động deploy code và chạy unit test trong quy trình tích hợp liên tục (Continuous Integration)?

**💬 Giải thích gốc (English):**
> A developer should use Salesforce DX (SFDX) for scripting the deployment and unit test execution as part of continuous integration. Here's how:
> SFDX CLI: Command-line interface tools enable you to script deployment and automate unit tests.
> Continuous Integration Tools: Combine SFDX with CI tools like Jenkins, GitHub Actions, or CircleCI to automate the deployment process and run your tests seamlessly.

**✅ Tại sao đáp án đúng:**
> Chọn **B: Salesforce CLI**. Salesforce CLI (hay SFDX CLI) là công cụ dòng lệnh (command-line) chính thống, cực kỳ mạnh mẽ, được sinh ra để nhúng vào các kịch bản CI/CD (như Jenkins, GitHub Actions, GitLab CI) nhằm tự động hóa deploy metadata và kích hoạt chạy test class tự động từ xa bằng script.

**❌ Tại sao đáp án sai:**
> **A.** Developer Console là công cụ nền web thủ công trên trình duyệt, không có API hay dòng lệnh để tích hợp vào script CI tự động được.
> **C.** VS Code là trình soạn thảo code (IDE) dành cho dev gõ code bằng tay, không thể chạy độc lập tự động trên máy chủ CI được.
> **D.** Execute Anonymous chỉ dùng để chạy thử một đoạn code Apex ngắn chứ không hỗ trợ deploy code hay chạy tự động hóa toàn bộ unit test suite của Org.

**💡 Từ khóa ghi nhớ:** `CI/CD tự động hóa -> Auto gọi tên **Salesforce CLI**!`

---

## Câu 300

**🔵 What are two ways for a developer to execute tests in an org? (Choose two.)**

- **A.** Tooling API ✅
- **B.** Developer Console ✅
- **C.** Metadata API ❌
- **D.** Bulk API ❌

**📝 Dịch tiếng Việt:**
> Hai cách nào lập trình viên có thể sử dụng để kích hoạt thực thi (execute) các bài kiểm thử unit test trong một Org? (Chọn 2)

**💬 Giải thích gốc (English):**
> Run Unit Test Methods
> To verify the functionality of your Apex code, execute unit tests. You can run Apex test methods in the Developer Console, in Setup, in the Salesforce extensions for Visual Studio Code, or using the API.

**✅ Tại sao đáp án đúng:**
> Chọn **A** và **B**.
- **A: Tooling API**. Tooling API cung cấp các endpoint xịn sò (như `/runTestsAsynchronous` hoặc `/runTestsSynchronous`) để các công cụ bên ngoài (như VS Code, CLI) có thể kích hoạt chạy test từ xa.
- **B: Developer Console**. Giao diện phát triển chuẩn của Salesforce, hỗ trợ tab 'Test' để bạn click chọn và chạy từng test class hoặc toàn bộ test suite một cách trực quan.

**❌ Tại sao đáp án sai:**
> **C.** Metadata API chuyên dùng để deploy/retrieve cấu hình hệ thống (metadata) chứ không có chức năng chạy test trực tiếp.
> **D.** Bulk API chuyên dùng để nạp/xuất dữ liệu hàng loạt cực lớn (Data Loading) chứ không liên quan đến việc thực thi Apex Unit Test.

**💡 Từ khóa ghi nhớ:** `Chạy Unit Test trong Salesforce -> Một là dùng **Developer Console** (UI), hai là chọc qua **Tooling API** (Command/API)!`

---

## Câu 301

**🔵 Which tool allows a developer to send requests to the Salesforce REST APIs and view the responses?**

- **A.** REST resource path URL ❌
- **B.** Workbench REST Explorer ✅
- **C.** Developer Console REST tab ❌
- **D.** Force.com IDE REST Explorer tab ❌

**📝 Dịch tiếng Việt:**
> Công cụ nào cho phép lập trình viên dễ dàng gửi thử nghiệm các yêu cầu REST API đến Salesforce và xem trực tiếp các phản hồi JSON/XML trả về ngay trên giao diện?

**💬 Giải thích gốc (English):**
> Workbench Rest Explorer allows developers to send requests to the Salesforce REST APIs and view the responses, making it an excellent choice for testing and interacting with RESTful services in Salesforce.

**✅ Tại sao đáp án đúng:**
> Chọn **B**. **Workbench REST Explorer** là một "bảo bối" đắc lực giúp anh em gửi thử nghiệm đủ loại request (GET, POST, PUT, DELETE, PATCH) đến các Salesforce REST API endpoint một cách trực quan, nhận kết quả trả về ngay lập tức mà không cần phải viết một dòng code nào. Siêu nhanh, siêu tiện!

**❌ Tại sao đáp án sai:**
> **A.** REST resource path URL chỉ đơn thuần là đường dẫn (URI) tĩnh của API chứ bản thân nó không phải là một công cụ giúp gửi request hay hiển thị kết quả gì cả. Dán cái này lên trình duyệt thường thì chỉ có "cook" vì thiếu authentication.
> **C.** Developer Console làm gì có tab nào tên là "REST tab" để test API thủ công đâu. Đây là cú lừa bịa đặt trắng trợn!
> **D.** Force.com IDE là đồ cổ chạy trên Eclipse đã bị Salesforce khai tử từ lâu, và nó cũng không có tab REST Explorer chuyên biệt nào cả. Quên nó đi cho nước nó trong.

**💡 Từ khóa ghi nhớ:** `Test REST API Salesforce nhanh gọn lẹ -> Triệu hồi ngay **Workbench REST Explorer**!`

---

## Câu 302

**🔵 A developer needs to create a baseline set of data (Accounts, Contacts, Products, Assets) for an entire suite of tests allowing them to test independent requirements various types of Salesforce Cases. Which approach can efficiently generate the required data for each unit test?**

- **A.** Create a mock using the Stub API. ❌
- **B.** Use @TestSetup with a void method. ✅
- **C.** Add @IsTest(seeAllData=true) at the start of the unit test class. ❌
- **D.** Create test data before Test.startTest() in the unit test. ❌

**📝 Dịch tiếng Việt:**
> Một lập trình viên cần tạo một bộ dữ liệu mẫu cơ bản (Accounts, Contacts, Products, Assets) cho toàn bộ các lớp kiểm thử (test suite) để kiểm tra các yêu cầu độc lập cho nhiều loại Case khác nhau. Cách tiếp cận nào giúp tạo dữ liệu này một cách hiệu quả và tối ưu nhất cho từng unit test?

**✅ Tại sao đáp án đúng:**
> Chọn **B**. Sử dụng **`@TestSetup`** bọc một `void` method là giải pháp "chuẩn cơm mẹ nấu" để tạo dữ liệu dùng chung (baseline data) cho toàn bộ các phương thức test trong class. Phương thức `@TestSetup` chỉ chạy đúng **1 lần duy nhất** trước khi bất kỳ test method nào bắt đầu. Hệ thống sẽ tự động rollback (hoàn tác) dữ liệu sau mỗi test method, giúp đảm bảo các test độc lập với nhau mà không tốn công tạo lại dữ liệu, tối ưu hóa tốc độ chạy test lên tầm cao mới!

**❌ Tại sao đáp án sai:**
> **A.** Stub API dùng để mock (giả lập) các hành vi/logic của class hoặc interface trong Apex chứ không dùng để khởi tạo dữ liệu vật lý (như Account, Contact...) lưu vào DB cho test.
> **C.** Sử dụng `@IsTest(seeAllData=true)` là một thực hành cực kỳ "gà" (bad practice). Nó cho phép test class nhìn thấy dữ liệu thật của Org, làm cho kết quả test bị phụ thuộc vào môi trường (không độc lập) và dễ gây lỗi đụng độ dữ liệu thực tế.
> **D.** Tạo dữ liệu test thủ công trước `Test.startTest()` ở từng test method độc lập sẽ khiến code bị lặp đi lặp lại (redundant) và Salesforce phải chạy DML tạo data liên tục cho từng method, làm chậm tốc độ chạy test một cách cồng kềnh.

**💡 Từ khóa ghi nhớ:** `Tạo dữ liệu mẫu dùng chung cho cả class test -> Dùng ngay phương thức **`@TestSetup`**!`

---

## Câu 303

**🔵 Which three statements are true regarding custom exceptions in Apex? (Choose three.)**

- **A.** A custom exception class must extend the system Exception class. ✅
- **B.** A custom exception class can implement one or many interfaces. ✅
- **C.** A custom exception class cannot contain member variables or methods. ❌
- **D.** A custom exception class name must end with "Exception" ✅
- **E.** A custom exception class can extend other classes besides the Exception class. ❌

**📝 Dịch tiếng Việt:**
> Ba phát biểu nào sau đây là ĐÚNG khi nói về ngoại lệ tùy chỉnh (Custom Exceptions) trong Apex? (Chọn 3)

**💬 Giải thích gốc (English):**
> To create your custom exception class, extend the built-in Exception class and make sure your class name ends with the word Exception, such as “MyException” or “PurchaseException”. All exception classes extend the system-defined base class Exception, and therefore, inherits all common Exception methods.

**✅ Tại sao đáp án đúng:**
> Chọn **A**, **B** và **D**.
- **A**: Một custom exception bắt buộc phải kế thừa (extend) lớp `Exception` của hệ thống để được thừa hưởng các hành vi xử lý lỗi tiêu chuẩn.
- **B**: Vì custom exception thực chất vẫn là một class Apex thông thường, nó hoàn toàn có thể hiện thực hóa (implement) một hoặc nhiều interface để mở rộng tính năng.
- **D**: Tên của custom exception class **bắt buộc** phải kết thúc bằng hậu tố "Exception" (ví dụ: `MyCustomException`). Thiếu cái này là Apex Compiler đấm cho không trượt phát nào!

**❌ Tại sao đáp án sai:**
> **C.** Sai bét! Custom exception hoàn toàn có thể chứa các biến thành viên (member variables) hoặc phương thức (methods) riêng để lưu trữ thêm thông tin lỗi chi tiết (ví dụ: error code, timestamp).
> **E.** Apex chỉ hỗ trợ đơn kế thừa (single inheritance), và đối với custom exception thì class cha bắt buộc phải là lớp `Exception` hệ thống (hoặc một exception class khác đã extend Exception), chứ không thể ngang nhiên kế thừa một class thường bất kỳ nào khác được.

**💡 Từ khóa ghi nhớ:** `Custom Exception = **extends Exception** + **implement interfaces** thoải mái + Tên kết thúc bằng **"Exception"**!`

---

## Câu 304

**🔵 A developer writes a trigger on the Account object on the before update event that increments a count field. A workflow rule also increments the count field every time that an Account is created or updated. The field update in the workflow rule is configured to not re-evaluate workflow rules. What is the value of the count field if an Account is inserted with an initial value of zero, assuming no other automation logic is implemented on the Account?**

- **A.** 1 ❌
- **B.** 3 ❌
- **C.** 4 ❌
- **D.** 2 ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên viết một trigger trên đối tượng Account ở sự kiện before update để tăng giá trị trường đếm count thêm 1 đơn vị. Một workflow rule cũng thực hiện tăng trường count này thêm 1 đơn vị mỗi khi Account được tạo hoặc cập nhật. Field update trong workflow rule được cấu hình để KHÔNG kích hoạt lại workflow rules (not re-evaluate). Giá trị của trường count sẽ là bao nhiêu nếu một Account được chèn mới (insert) với giá trị ban đầu bằng 0? (Giả định không có automation nào khác).

**💬 Giải thích gốc (English):**
> 1. Initial Value: The Account is initially created with a value of 0.
> 2. Trigger: The trigger fires before the update, incrementing the count to 1.
> 3. Workflow Rule: The workflow rule triggers and increments the count to 2.
> Since the workflow rule is configured to not re-evaluate, it will not trigger again after the trigger's update. Therefore, the final value of the count field will be 2.

**✅ Tại sao đáp án đúng:**
> Chọn **D: 2**. Hãy cùng phân tích từng bước theo vòng đời Save Order of Execution của Salesforce:
1. Người dùng chèn (insert) Account với giá trị `count = 0`.
2. Sự kiện `before insert` của trigger không được đăng ký (trigger chỉ bắt `before update`), nên bước này lướt qua.
3. Bản ghi được lưu tạm vào Database.
4. Sau khi chèn, **Workflow Rule** bắt sự kiện "created or updated" nên được kích hoạt! Nó thực hiện tăng trường `count` lên: `count = 0 + 1 = 1`.
5. Vì có Workflow Field Update, hệ thống buộc phải chạy lại quy trình lưu một lần nữa. Lần này là sự kiện cập nhật (update) ngầm. Ở đây, sự kiện `before update` của trigger được kích hoạt! Trigger chạy và tăng trường `count` thêm 1 đơn vị nữa: `count = 1 + 1 = 2`.
6. Vì Workflow Field Update được cấu hình **không re-evaluate**, hệ thống dừng vòng lặp tại đây và kết thúc giao dịch. Giá trị cuối cùng ghi vào database là **2**!

**❌ Tại sao đáp án sai:**
> **A.** 1 là sai vì mới chỉ tính lượt cộng của Workflow mà quên mất sau khi Workflow Field Update chạy, nó sẽ kích hoạt lại các Before/After Update Triggers làm trigger chạy thêm một lượt nữa.
> **B.** 3 chỉ xảy ra nếu Workflow Field Update được cấu hình **re-evaluate workflow rules**, dẫn đến việc Workflow tiếp tục chạy lại và kích hoạt tiếp trigger, tạo thành một chuỗi lặp nữa.
> **C.** 4 là con số quá cao, hệ thống không thể tự tăng lên 4 trong kịch bản này trừ khi bị lặp vô tận (đụng trần 5 lượt re-evaluate).

**💡 Từ khóa ghi nhớ:** `Chạy DML Insert -> **Workflow chạy (cộng 1)** -> Kích hoạt lại **Before Update Trigger (cộng 1)** -> Kết quả cuối là **2**.`

---

## Câu 305

**🔵 For which three items can a trace flag be configured? (Choose three.)**

- **A.** Apex Trigger ✅
- **B.** Apex Class ✅
- **C.** Process Builder ❌
- **D.** User ✅
- **E.** Visualforce ❌

**📝 Dịch tiếng Việt:**
> Trace Flag có thể được cấu hình cho ba thành phần/thực thể nào sau đây? (Chọn 3)

**💬 Giải thích gốc (English):**
> Set Up Debug Logging
> To activate debug logging for users, Apex classes, and Apex triggers, configure trace flags and debug levels in the Developer Console or in Setup. Each trace flag includes a debug level, start time, end time, and log type. The trace flag’s log type specifies the entity you’re tracing.

**✅ Tại sao đáp án đúng:**
> Chọn **A**, **B** và **D**. Trace Flag là công cụ giúp bạn cắm "máy quay lén" để Salesforce ghi lại nhật ký debug log chi tiết cho các đối tượng cụ thể. Bạn có thể cấu hình Trace Flag trực tiếp cho:
- **A**: Một **Apex Trigger** cụ thể.
- **B**: Một **Apex Class** cụ thể.
- **D**: Một **User** cụ thể (rất hữu ích khi cần debug hành vi của một người dùng thực tế trên hệ thống).

**❌ Tại sao đáp án sai:**
> **C.** Process Builder không nằm trong danh sách các thực thể có thể thiết lập Trace Flag trực tiếp riêng biệt trong Setup Debug Levels.
> **E.** Visualforce Page là trang giao diện hiển thị, không thể gán Trace Flag riêng biệt để ghi log độc lập giống như Apex Class hay Trigger.

**💡 Từ khóa ghi nhớ:** `Trace Flag (cắm camera soi log) -> Chỉ cắm được cho: **User**, **Apex Class**, hoặc **Apex Trigger**!`

---

## Câu 306

**🔵 Which three data types can be returned from an SOQL statement? (Choose three.)**

- **A.** Boolean ❌
- **B.** List of sObjects ✅
- **C.** Single sObject ✅
- **D.** Integer ✅
- **E.** String ❌

**📝 Dịch tiếng Việt:**
> Ba kiểu dữ liệu nào sau đây có thể được trả về trực tiếp từ một câu lệnh truy vấn SOQL trong Apex? (Chọn 3)

**💬 Giải thích gốc (English):**
> SOQL can return several data types:
> List<sObject>: This is used to retrieve multiple records.
> Single sObject: When you're querying for just one record.
> AggregateResult: Useful for aggregate queries, like those with GROUP BY.
> Integer: Useful for Useful for count records.

**✅ Tại sao đáp án đúng:**
> Chọn **B**, **C** và **D**.
- **B**: Trả về một danh sách các bản ghi (`List<sObject>`), đây là kiểu trả về phổ biến nhất của SOQL.
- **C**: Trả về một bản ghi đơn duy nhất (`Single sObject`) khi bạn query với từ khóa giới hạn `LIMIT 1` hoặc lọc chính xác qua ID (ví dụ: `Account acc = [SELECT Id FROM Account LIMIT 1];`).
- **D**: Trả về một số nguyên (`Integer`) khi bạn thực hiện câu lệnh đếm trực tiếp bằng hàm `COUNT()` (ví dụ: `Integer total = [SELECT COUNT() FROM Contact];`).

**❌ Tại sao đáp án sai:**
> **A.** SOQL không bao giờ hỗ trợ trả về trực tiếp kiểu dữ liệu Boolean.
> **E.** SOQL không thể trả về trực tiếp một chuỗi String thô. Nếu muốn lấy giá trị String, bạn phải query sObject đó lên rồi truy cập vào trường kiểu Text của nó (ví dụ: `acc.Name`).

**💡 Từ khóa ghi nhớ:** `SOQL chỉ có 3 kiểu trả về trực tiếp: **List<sObject>**, **Single sObject**, hoặc **Integer** (khi dùng `COUNT()`)!`

---

## Câu 307

**🔵 In which three areas can a Lightning component be used in the Lightning Experience? (Choose three.)**

- **A.** Lightning Report page ❌
- **B.** Lightning Connect page ❌
- **C.** Lightning Record Page ✅
- **D.** Lightning Community Page ✅
- **E.** Lightning Home page ✅

**📝 Dịch tiếng Việt:**
> Ba khu vực/trang nào lập trình viên có thể trực tiếp nhúng và sử dụng Lightning Components (Aura/LWC) trong giao diện Lightning Experience? (Chọn 3)

**✅ Tại sao đáp án đúng:**
> Chọn **C**, **D** và **E**.
- **C**: **Lightning Record Page** (Trang chi tiết bản ghi, cho phép nhúng qua Lightning App Builder).
- **D**: **Lightning Community Page** (Trang cộng đồng/Experience Cloud, kéo thả trực tiếp trong Experience Builder).
- **E**: **Lightning Home page** (Trang chủ hệ thống, tùy biến kéo thả dễ dàng bằng App Builder).

**❌ Tại sao đáp án sai:**
> **A.** Lightning Report page là trang báo cáo tiêu chuẩn của hệ thống, cấm nhúng component tự thiết kế bừa bãi vào đây.
> **B.** Không hề tồn tại khái niệm "Lightning Connect page" để kéo thả nhúng component trực tiếp trên UI.

**💡 Từ khóa ghi nhớ:** `Nhúng LWC trên Lightning UI -> Chỉ có kéo thả tại **Record Page**, **Home Page**, hoặc **Community Page**!`

---

## Câu 308

**🔵 What are three ways for a developer to execute tests in an org?**

- **A.** Tooling API ✅
- **B.** Salesforce DX ✅
- **C.** Metadata API ❌
- **D.** Bulk API ❌
- **E.** Setup Menu ✅

**📝 Dịch tiếng Việt:**
> Ba phương thức/công cụ nào cho phép lập trình viên trực tiếp kích hoạt chạy các lớp test class (execute tests) trong một Salesforce Org? (Chọn 3)

**💬 Giải thích gốc (English):**
> A developer can execute tests in an org using these three ways:
> Tooling API : Allows for powerful interactions with Salesforce metadata, including running tests.
> Setup Menu : Provides a user-friendly interface to run tests directly within the Salesforce setup area.
> Salesforce DX : Offers robust command-line tools to manage and run tests as part of your development workflow.

**✅ Tại sao đáp án đúng:**
> Chọn **A**, **B** và **E**.
- **A**: **Tooling API** cung cấp các REST/SOAP endpoint hỗ trợ chạy test bất đồng bộ.
- **B**: **Salesforce DX** (SFDX CLI) cho phép chạy lệnh terminal chạy test cực nhanh (ví dụ: `sf apex run test`).
- **E**: **Setup Menu** trong trang quản trị quản lý Apex Test Execution cung cấp giao diện trực quan để người dùng chạy test.

**❌ Tại sao đáp án sai:**
> **C.** Metadata API dùng để deploy hoặc retrieve cấu trúc thư mục, code, cấu hình hệ thống chứ không có nhiệm vụ kích hoạt chạy test độc lập.
> **D.** Bulk API dùng để nạp/xử lý hàng triệu bản ghi dữ liệu cực lớn, hoàn toàn không liên quan gì đến việc chạy test code.

**💡 Từ khóa ghi nhớ:** `Kích hoạt Apex Test -> Dùng **Setup Menu**, **Salesforce DX CLI**, hoặc **Tooling API**!`

---

## Câu 309

**🔵 Which set of roll-up types are available when creating a roll-up summary field?**

- **A.** COUNT, SUM, MIN, MAX ✅
- **B.** AVERAGE, SUM, MIN, MAX ❌
- **C.** SUM, MIN, MAX ❌
- **D.** AVRAGE, COUNT, SUM, MIN, MAX ❌

**📝 Dịch tiếng Việt:**
> Tập hợp các hàm tổng hợp (roll-up types) nào có sẵn và được hỗ trợ đầy đủ khi khởi tạo một trường Roll-up Summary Field trong Salesforce?

**💬 Giải thích gốc (English):**
> Roll-Up Summary Field
> A roll-up summary field calculates values from related records, such as those in a related list. You can create a roll-up summary field to display a value in a master record based on the values of fields in a detail record. The detail record must be related to the master through a master-detail relationship.
> You can perform different types of calculations with a roll-up summary field. You can count the number of detail records related to a master record. Or, you can calculate the sum, minimum value, or maximum value of a field in the detail records.

**✅ Tại sao đáp án đúng:**
> Chọn **A**. Salesforce chỉ hỗ trợ đúng 4 hàm tổng hợp cơ bản khi làm Roll-up Summary Field là: **COUNT** (đếm số lượng bản ghi con), **SUM** (cộng tổng giá trị trường số), **MIN** (lấy giá trị nhỏ nhất), và **MAX** (lấy giá trị lớn nhất). Đây là bộ tứ huyền thoại giúp tính toán tự động từ con lên cha trong mối quan hệ Master-Detail.

**❌ Tại sao đáp án sai:**
> **B.** AVERAGE (tính trung bình) là hàm KHÔNG được Salesforce hỗ trợ trong Roll-up Summary vì tính toán này tốn rất nhiều tài nguyên hệ thống khi dữ liệu con thay đổi liên tục.
> **C.** Bị thiếu mất hàm đếm số lượng bản ghi con **COUNT** cực kỳ phổ biến.
> **D.** Lại có sự xuất hiện của hàm AVERAGE (viết sai chính tả thành AVRAGE) - một lựa chọn hoàn toàn "cook".

**💡 Từ khóa ghi nhớ:** `4 hàm Roll-up Summary huyền thoại -> Luôn nhớ: **COUNT, SUM, MIN, MAX** (Tuyệt đối KHÔNG có AVERAGE)!`

---

## Câu 310

**🔵 Which scenario is valid for execution by unit tests?**

- **A.** Set the created of a record using a system method. ✅
- **B.** Generate a Visualforce Pdf with getContentasPdf(). ❌
- **C.** Load data from a remote site with a callout. ❌
- **D.** Execute anonymous Apex as a different user. ❌

**📝 Dịch tiếng Việt:**
> Kịch bản nào sau đây là hợp lệ và có thể thực thi thành công bên trong các unit test trong Salesforce?

**💬 Giải thích gốc (English):**
> You can create a test record, set its CreatedDate using a system method, and then assert that the value is correct.
> setCreatedDate(recordId, createdDatetime)

**✅ Tại sao đáp án đúng:**
> Chọn **A**. Trong Unit Test, bạn hoàn toàn có thể thiết lập ngày tạo (`CreatedDate`) của một bản ghi (dù bình thường đây là trường read-only chỉ có hệ thống ghi) bằng cách sử dụng phương thức hệ thống chuyên dụng `Test.setCreatedDate(recordId, customDateTime)`. Đây là tính năng tuyệt vời để test các logic liên quan đến mốc thời gian.

**❌ Tại sao đáp án sai:**
> **B.** Phương thức `getContentAsPDF()` bị cấm và sẽ ném ra ngoại lệ `System.CalloutException` nếu gọi trực tiếp trong context chạy unit test mà không được xử lý giả lập.
> **C.** Tương tự, các cuộc gọi HTTP Callout thật ra bên ngoài hệ thống bị cấm tiệt trong Unit Test để đảm bảo tốc độ chạy test và tính cô lập. Bạn bắt buộc phải dùng mock class (`HttpCalloutMock`).
> **D.** Execute Anonymous là một hành động chạy ad-hoc độc lập từ Developer Console hoặc CLI, bạn không thể nhét kịch bản "chạy anonymous dưới tư cách user khác" vào bên trong code Unit Test được.

**💡 Từ khóa ghi nhớ:** `Trong Unit Test: Cấm Callout thật, Cấm `getContentAsPDF()` -> Cho phép **`Test.setCreatedDate()`**!`

---

## Câu 311

**🔵 Which two conditions cause workflow rules to fire? (Choose two.)**

- **A.** An Apex Batch process that changes field values. ✅
- **B.** Updating records using the bulk API ✅
- **C.** Converting leads to person accounts ❌
- **D.** Changing the territory assignments of accounts and opportunities ❌

**📝 Dịch tiếng Việt:**
> Hai điều kiện nào sau đây sẽ kích hoạt (fire) các quy tắc tự động hóa Workflow Rules hoạt động bình thường? (Chọn 2)

**💬 Giải thích gốc (English):**
> The following actions do NOT trigger workflow rules.
> - Mass replacing picklist values
> - Using the option to replace a picklist value while deleting the current value.
> - Mass updating address fields
> - Mass updating divisions
> - Changing the territory assignments of accounts and opportunities
> - Converting leads to person accounts
> - Deactivating Self-Service Portal, Customer Portal, or Partner Portal users
> - Converting state, country, and territory data from the State and Country/Territory Picklists page in Setup
> - Changing state and country/territory picklists using AddressSettings in the Metadata API"

**✅ Tại sao đáp án đúng:**
> Chọn **A** và **B**.
- **A**: Một tiến trình chạy lô Apex Batch khi thực hiện cập nhật thay đổi giá trị trường sẽ kích hoạt các DML update thông thường, từ đó chạy đầy đủ Save Order of Execution bao gồm cả Workflow Rules.
- **B**: Sử dụng Bulk API để cập nhật hàng loạt bản ghi cũng là một giao dịch DML chuẩn, nên hệ thống vẫn sẽ kích hoạt Workflow Rules bình thường.

**❌ Tại sao đáp án sai:**
> **C.** Khi convert Lead sang Person Account, Salesforce chạy một quy trình hệ thống đặc biệt và chủ động bỏ qua việc kích hoạt các Workflow Rules thông thường để tránh xung đột dữ liệu.
> **D.** Thay đổi gán phân vùng (Territory assignment) của Accounts và Opportunities là hành động quản trị hệ thống, không kích hoạt luồng DML thông thường nên Workflow Rules sẽ không chạy.

**💡 Từ khóa ghi nhớ:** `Cứ có thao tác dữ liệu **DML (Batch Apex / Bulk API)** -> **Workflow Rules** vẫn chạy như thường!`

---

## Câu 312

**🔵 What are three capabilities of the tag when loading JavaScript resources in Aura components? (Choose three.)**

- **A.** One-time loading for duplicate scripts ✅
- **B.** Specifying loading order ✅
- **C.** Loading externally hosted scripts ❌
- **D.** Loading files from Documents ❌
- **E.** Loading scripts in parallel ✅

**📝 Dịch tiếng Việt:**
> Ba khả năng vượt trội của thẻ <ltng:require> khi thực hiện tải các tài nguyên JavaScript (từ Static Resource) vào Aura components là gì? (Chọn 3)

**✅ Tại sao đáp án đúng:**
> Chọn **A**, **B** và **E**.
- **A**: Tự động nhận diện và chỉ tải script đúng 1 lần duy nhất ngay cả khi có nhiều component cùng yêu cầu tải chung một script (tránh lỗi xung đột do nạp trùng thư viện).
- **B**: Hỗ trợ xác định chính xác thứ tự tải của các tệp JS (thông qua thuộc tính `scripts` truyền mảng sắp xếp) để đảm bảo các thư viện phụ thuộc chạy đúng chuẩn.
- **E**: Cho phép tải song song nhiều tệp tin JavaScript cùng một lúc giúp tăng tốc độ hiển thị giao diện UI đáng kể.

**❌ Tại sao đáp án sai:**
> **C.** Vì lý do bảo mật nghiêm ngặt của Salesforce (CSP - Content Security Policy), thẻ `<ltng:require>` không thể tải trực tiếp các đường dẫn script host bên ngoài mà bắt buộc phải nạp qua Static Resource.
> **D.** Không thể nạp tệp từ đối tượng thư mục Documents cũ kỹ, chỉ hỗ trợ nạp từ **Static Resource**.

**💡 Từ khóa ghi nhớ:** `ltng:require nạp JS từ Static Resource -> Có 3 tuyệt chiêu: **Tải song song**, **Tải đúng thứ tự**, và **Chống tải trùng (một lần duy nhất)**!`

---

## Câu 313

**🔵 Which three resources in an Aura component can contain JavaScript functions? (Choose three.)**

- **A.** Helper ✅
- **B.** Design ❌
- **C.** Renderer ✅
- **D.** Style ❌
- **E.** Controller ✅

**📝 Dịch tiếng Việt:**
> Ba tài nguyên (resources) nào bên trong một gói đóng gói Aura Component (bundle) có thể chứa các hàm viết bằng JavaScript? (Chọn 3)

**💬 Giải thích gốc (English):**
> The following resources can define and use JavaScript functions in Salesforce Aura components:
> 1. Controller: The controller is in charge of specifying the JavaScript functions that manage the logic and actions of the component. It includes the methods that the component's events or those of other components call. These procedures are listed and associated with the component in the controller's JavaScript file.
> 2. Helper: The helper is a supplemental resource that may be used to add further JavaScript features to assist the operation of the component. It can have reusable functions that are invoked by the component's controller or other helpers and is defined in a separate JavaScript file.
> 3. Renderer: The renderer is yet another optional resource that enables you to change or improve the way a component renders. It can have functions that alter the component's DOM elements, styles, or other visual components during rendering. It is defined in a distinct JavaScript file.

**✅ Tại sao đáp án đúng:**
> Chọn **A**, **C** và **E**. Trong một Aura Component Bundle, 3 file được viết hoàn toàn bằng JavaScript và chứa các hàm thực thi logic là:
- **A**: **Helper** (`componentHelper.js`) - Nơi chứa logic dùng chung và các hàm tái sử dụng.
- **C**: **Renderer** (`componentRenderer.js`) - Nơi ghi đè các hàm render DOM mặc định của framework.
- **E**: **Controller** (`componentController.js`) - Nơi chứa các hàm xử lý sự kiện (action handler) trực tiếp từ giao diện.

**❌ Tại sao đáp án sai:**
> **B.** Design (`component.design`) thực chất là file XML dùng để cấu hình các thuộc tính hiển thị cho admin kéo thả trong App Builder, không chứa code JS.
> **D.** Style (`component.css`) là file chứa mã nguồn CSS dùng để định dạng giao diện hiển thị, không chứa code JS.

**💡 Từ khóa ghi nhớ:** `Bộ ba JavaScript thần thánh của Aura Bundle -> Cứ nhớ: **Controller - Helper - Renderer**!`

---

## Câu 314

**🔵 A developer created a Visualforce page and a custom controller with methods to handle different buttons and events that can occur on the page. What should the developer do to deploy to production?**

- **A.** Create a test class that provides coverage of the Visualforce page. ❌
- **B.** Create a test page that provides coverage of the Visualforce page. ❌
- **C.** Create a test page that provides coverage of the custom controller. ❌
- **D.** Create a test class that provides coverage of the custom controller. ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên đã tạo một trang Visualforce và một Custom Controller chứa các hàm xử lý nút bấm nghiệp vụ. Lập trình viên bắt buộc phải làm gì để có thể deploy (triển khai) thành công các thành phần này lên Production?

**💬 Giải thích gốc (English):**
> To ensure the quality and reliability of your Visualforce page and custom controller before deploying to production, it's crucial to write comprehensive unit tests for the custom controller. This will help identify potential issues and bugs early in the development process.
> To deploy it we need code coverage above 75%.

**✅ Tại sao đáp án đúng:**
> Chọn **D**. Theo luật cứng khi deploy lên Production của Salesforce, mọi đoạn mã Apex (bao gồm cả lớp Custom Controller) bắt buộc phải có độ phủ kiểm thử (code coverage) tối thiểu đạt **75%**. Do đó, bạn bắt buộc phải viết một **Test Class** để gọi chạy các method trong Custom Controller nhằm đảm bảo độ phủ code.

**❌ Tại sao đáp án sai:**
> **A.** Visualforce Page chỉ là trang giao diện thẻ markup hiển thị, Salesforce tuyệt đối không yêu cầu (và cũng không có cách nào) đo đạc code coverage cho bản thân trang Visualforce.
> **B.** Không tồn tại khái niệm "Test Page" để đo phủ sóng cho Visualforce page.
> **C.** Không thể dùng một trang web ("Test Page") để đo đạc và phủ sóng logic code trong Apex Custom Controller.

**💡 Từ khóa ghi nhớ:** `Muốn deploy Custom Controller lên Production -> Bắt buộc phải viết **Test Class** để phủ sóng logic tối thiểu **75%**!`

---

## Câu 315

**🔵 Universal Containers has an order system that uses an Order Number to identify an order for customers and service agents. Order records will be imported into Salesforce. How should the Order Number field be defined in Salesforce?**

- **A.** Direct Lookup ❌
- **B.** Lookup ❌
- **C.** Number with External ID ✅
- **D.** Indirect Lookup ❌

**📝 Dịch tiếng Việt:**
> Universal Containers có một hệ thống quản lý đơn hàng sử dụng trường Order Number để định danh đơn hàng cho khách hàng và nhân viên hỗ trợ. Các bản ghi này sẽ được nạp (import) hàng loạt vào Salesforce. Trường Order Number nên được định nghĩa thế nào trong Salesforce?

**💬 Giải thích gốc (English):**
> Using External ID and Unique would ensure each order has a unique identification in Salesforce.

**✅ Tại sao đáp án đúng:**
> Chọn **C**. Do dữ liệu đơn hàng được import từ hệ thống bên ngoài vào Salesforce, việc cấu hình thuộc tính **External ID** trên trường Order Number (kiểu Number hoặc Text) là giải pháp tối ưu nhất. Nó giúp Salesforce làm khóa đối chiếu duy nhất để so khớp dữ liệu khi gọi lệnh Upsert, giúp liên kết bản ghi chính xác mà không cần biết Salesforce ID.

**❌ Tại sao đáp án sai:**
> **A.** Không hề tồn tại kiểu trường dữ liệu nào tên là "Direct Lookup" trong Salesforce.
> **B.** Trường Lookup chỉ dùng để tạo mối quan hệ cha con giữa hai bảng trong Salesforce, không giúp định danh duy nhất bản ghi từ hệ thống ngoài truyền vào.
> **D.** Indirect Lookup dùng cho đối tượng ngoài (External Object) của Salesforce Connect để map dữ liệu ảo từ hệ thống ngoài, không phù hợp cho việc nạp dữ liệu vật lý trực tiếp vào Salesforce.

**💡 Từ khóa ghi nhớ:** `Lấy khóa định danh từ hệ thống ngoài nạp vào Salesforce -> Luôn cấu hình trường đó làm **External ID**!`

---

## Câu 316

**🔵 Which standard field is required when creating a new Contact record?**

- **A.** LastName ✅
- **B.** Name ❌
- **C.** AccountId ❌
- **D.** FirstName ❌

**📝 Dịch tiếng Việt:**
> Trường tiêu chuẩn (standard field) nào bắt buộc phải có giá trị khi khởi tạo một bản ghi Contact mới trong Salesforce?

**💬 Giải thích gốc (English):**
> The only required standard field when creating a new Contact record in Salesforce is the Last Name field.

**✅ Tại sao đáp án đúng:**
> Chọn **A**. Ở mức cơ sở dữ liệu hệ thống (Database Schema Layer) của Salesforce đối với thực thể Contact, trường **LastName** (Họ) là trường tiêu chuẩn duy nhất bắt buộc phải nhập. Nếu bạn DML insert một Contact không có LastName, hệ thống sẽ chặn đứng và báo lỗi ngay lập tức.

**❌ Tại sao đáp án sai:**
> **B.** Trường Name thực tế trên UI là trường ghép tự động từ FirstName và LastName chứ ở mức database, nó không phải là một trường độc lập bắt buộc nhập.
> **C.** AccountId (mã liên kết Account cha) hoàn toàn là tùy chọn (optional). Bạn có thể thoải mái tạo một Contact "mồ côi" không thuộc bất cứ Account nào.
> **D.** FirstName (Tên) là tùy chọn, bạn thích nhập hay để trống đều được.

**💡 Từ khóa ghi nhớ:** `Trường bắt buộc nhập duy nhất khi tạo Contact -> Luôn luôn là **LastName**!`

---

## Câu 317

**🔵 A developer wrote a unit test to confirm that a custom exception works properly in a custom controller, but the test failed due to an exception being thrown. Which step should the developer take to resolve the issue and properly test the exception?**

- **A.** Use try/catch within the unit test to catch the exception. ✅
- **B.** Use the finally block within the unit test to populate the exception. ❌
- **C.** Use the database methods with all or none set to FALSE. ❌
- **D.** Use Test.isRunningTest() within the custom controller. ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên viết một unit test để xác nhận một custom exception (ngoại lệ tùy chỉnh) hoạt động chính xác trong custom controller, nhưng bài test bị báo FAIL do có lỗi exception thực sự bị ném ra. Lập trình viên nên làm gì để giải quyết vấn đề và test exception đúng cách?

**💬 Giải thích gốc (English):**
> By using a try/catch block, the developer can assert that the correct exception type is thrown and that the exception message contains the expected information. This ensures that the custom exception is working as intended and the unit test is reliable.

**✅ Tại sao đáp án đúng:**
> Chọn **A**. Khi bạn test các kịch bản ném lỗi (exception), việc để exception ném ra tự do sẽ làm crash luồng chạy của Test Framework và khiến bài test bị đánh trượt (FAIL). Giải pháp chuẩn là bọc khối code gây lỗi đó trong khối **`try-catch`** bên trong test class để chủ động hứng lỗi, sau đó dùng `System.assert` để kiểm tra xem loại lỗi ném ra có đúng như kỳ vọng không.

**❌ Tại sao đáp án sai:**
> **B.** Khối `finally` chỉ chạy dọn dẹp tài nguyên ở cuối tiến trình chứ không có khả năng đánh chặn và hứng lỗi (catch exception) để cứu bài test khỏi bị crash.
> **C.** Sử dụng các Database method với `allOrNone=false` chỉ áp dụng cho việc chèn bản ghi DML không bị lỗi đồng loạt, chứ không thể dùng để hứng một ngoại lệ tùy chỉnh (custom exception) tự ném ra bằng từ khóa `throw` trong logic nghiệp vụ.
> **D.** Sử dụng `Test.isRunningTest()` trong custom controller chỉ giúp né tránh đoạn code lỗi khi chạy test, chứ không giúp chúng ta kiểm thử tính chính xác của việc ném ngoại lệ.

**💡 Từ khóa ghi nhớ:** `Muốn kiểm thử lỗi (Test Exception) mà không bị crash test -> Bọc code trong khối **`try-catch`**!`

---

## Câu 318

**🔵 A developer is asked to create a Visualforce page that lists the contacts owned by the current user. This component will be embedded in a Lightning page. Without writing unnecessary code, which controller should be used for this purpose?**

- **A.** Standard controller ❌
- **B.** Custom controller ❌
- **C.** Standard list controller ✅
- **D.** Lightning controller ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên được yêu cầu tạo một trang Visualforce hiển thị danh sách các Contact do người dùng hiện tại sở hữu. Trang này sẽ được nhúng vào một Lightning page. Để tránh viết code không cần thiết, lập trình viên nên chọn loại controller nào?

**💬 Giải thích gốc (English):**
> Standard list controllers allow you to create Visualforce pages that can display or act on a set of records. Examples of existing Salesforce pages that work with a set of records include list pages, related lists, and mass action pages.

**✅ Tại sao đáp án đúng:**
> Chọn **C**. Sử dụng **Standard List Controller** (khai báo thuộc tính `recordSetVar` trong thẻ `<apex:page>`) là cách nhanh nhất và tối ưu nhất để hiển thị một danh sách bản ghi ra trang Visualforce. Nó cung cấp sẵn đầy đủ các tính năng duyệt danh sách, phân trang mà không đòi hỏi lập trình viên phải viết thêm một dòng code Apex Controller tùy chỉnh nào, cực kỳ tiết kiệm công sức!

**❌ Tại sao đáp án sai:**
> **A.** Standard Controller thông thường chỉ hỗ trợ hiển thị và tương tác với đúng **1 bản ghi duy nhất** chứ không hỗ trợ xử lý danh sách bản ghi.
> **B.** Sử dụng Custom Controller đòi hỏi bạn phải tự tay viết code Apex Class, viết test class phủ 75%... đi ngược lại hoàn toàn với yêu cầu "without writing unnecessary code" (tránh viết code thừa).
> **D.** Không hề tồn tại khái niệm "Lightning controller" trong kiến trúc phát triển trang Visualforce.

**💡 Từ khóa ghi nhớ:** `Hiển thị danh sách (Lists) + No-Code (without unnecessary code) -> Chọn ngay **Standard List Controller**!`

---

## Câu 319

**🔵 The following code snippet is executed by a Lightning web component in an environment with more than 2,000 lead records:
@AuraEnabled
public void static updateLeads(){
for(Lead thisLead : [SELECT Origin__c FROM Lead]){
thisLead.LeadSource = thisLead.Origin__c;
update thisLead;
}
}
Which governor limit will likely be exceeded within the Apex transaction?**

- **A.** Total number of SOQL queries issued ❌
- **B.** Total number of DML statements issued ✅
- **C.** Total number of records processed as a result of DML statements ❌
- **D.** Total number of records retrieved by SOQL queries ❌

**📝 Dịch tiếng Việt:**
> Đoạn code sau được thực thi bởi một LWC trong môi trường chứa hơn 2,000 bản ghi Lead:
```apex
@AuraEnabled
public void static updateLeads(){
  for(Lead thisLead : [SELECT Origin__c FROM Lead]){
    thisLead.LeadSource = thisLead.Origin__c;
    update thisLead;
  }
}
```
Giới hạn governor limit nào của Apex transaction sẽ có nguy cơ cao bị vượt quá (exceeded)?

**💬 Giải thích gốc (English):**
> SOQL FOR loops are an efficient way to process large datasets without exceeding heap size limits. They fetch records in batches, minimizing memory usage. However, the total allowed DML statements per transaction is 150.
> To optimize the code and avoid hitting the DML limit, consider using a bulkification approach to update the records in a single DML operation:
> Apex
> @AuraEnabled
> public static void updateLeads(){
> List<Lead> leadsToUpdate = [SELECT Id, Origin__c FROM Lead];
> for(Lead thisLead : leadsToUpdate){
> thisLead.LeadSource = thisLead.Origin__c;
> }
> update leadsToUpdate;
> }

**✅ Tại sao đáp án đúng:**
> Chọn **B**. Đây là lỗi sơ đẳng nhất của các lập trình viên tập sự! Salesforce giới hạn nghiêm ngặt mỗi transaction chỉ được thực thi tối đa **150 câu lệnh DML**. Trong đoạn code trên, câu lệnh `update thisLead;` (một lệnh DML) được đặt trực tiếp bên trong vòng lặp `for` chạy qua hơn 2,000 Lead. Khi chạy thực tế, hệ thống sẽ thực hiện DML đến lần thứ 151 là đụng trần và văng lỗi `System.LimitException: Too many DML statements: 151` ngay lập tức. Muốn sửa thì phải gom toàn bộ Lead vào một List rồi mới thực hiện update ngoài vòng lặp (bulkify)!

**❌ Tại sao đáp án sai:**
> **A.** Vòng lặp `for` này sử dụng SOQL For Loop trực tiếp, hệ thống chỉ thực hiện đúng **1 câu lệnh SOQL** duy nhất để lấy dữ liệu, còn lâu mới chạm mốc giới hạn 100 SOQL queries.
> **C.** Giới hạn tổng số bản ghi được xử lý bởi DML trong một giao dịch là 10,000 bản ghi, con số 2,000 vẫn nằm trong vòng an toàn.
> **D.** Giới hạn số bản ghi được truy vấn bởi SOQL là 50,000 bản ghi, con số 2,000 vẫn rất nhỏ.

**💡 Từ khóa ghi nhớ:** `DML đặt bên trong vòng lặp FOR -> Auto đụng trần giới hạn **DML Statements** (Tối đa 150 DML)!`

---

## Câu 320

**🔵 How can a developer warn users of SOQL governor limit violations in a trigger?**

- **A.** Use Messaging.SendEmail() to continue the transaction and send an alert to the user after the number of SOQL queries exceeds the limit. ❌
- **B.** Use PageReference.setRedirect() to redirect the user to a custom Visualforce page before the number of SOQL queries exceeds the limit. ❌
- **C.** Use Limits.getQueries() and display an error message before the number of SOQL queries exceeds the limit. ✅
- **D.** Use ApexMessage.Message() to display an error message after the number of SOQL queries exceeds the limit. ❌

**📝 Dịch tiếng Việt:**
> Làm thế nào để lập trình viên chủ động đưa ra cảnh báo cho người dùng về nguy cơ vi phạm giới hạn governor limits SOQL ngay trong một Apex Trigger?

**💬 Giải thích gốc (English):**
> By checking the current number of SOQL queries using Limits.getQueries(), the trigger can proactively identify potential issues before they lead to a transaction failure.

**✅ Tại sao đáp án đúng:**
> Chọn **C**. Cách duy nhất để xử lý êm đẹp tình huống này là chủ động phòng ngừa. Lập trình viên sử dụng phương thức `Limits.getQueries()` để kiểm tra số lượng câu SOQL đã thực thi trong transaction hiện tại. Nếu con số này sắp sửa chạm mốc giới hạn (100 queries), ta chủ động ném ra lỗi hoặc hiển thị thông báo chặn lại **trước khi** giới hạn bị vượt qua thực sự.

**❌ Tại sao đáp án sai:**
> **A.** Khi số lượng SOQL đã thực sự vượt quá giới hạn 100, Salesforce sẽ lập tức "kill" (hủy bỏ) giao dịch hiện tại ngay lập tức và thực hiện rollback toàn bộ. Không có dòng code nào phía sau (bao gồm cả gửi email) có cơ hội được chạy.
> **B.** Phương thức `PageReference.setRedirect()` chuyên dùng để điều hướng trang trong Apex Visualforce Controller, hoàn toàn bị cấm sử dụng và không có tác dụng gì bên trong môi trường của một Apex Trigger.
> **D.** Tương tự như câu A, sau khi đã vượt quá giới hạn, tiến trình bị kết thúc lập tức nên không thể gọi bất kỳ hàm nào để hiển thị thông báo lỗi kiểu này được nữa.

**💡 Từ khóa ghi nhớ:** `Chủ động kiểm soát và ngăn chặn đụng trần SOQL Limits -> Luôn dùng hàm **`Limits.getQueries()`** để check trước khi quá muộn!`

---

## Câu 321

**🔵 What are two valid options for iterating through each Account in the collection List named AccountList? (Choose two.)**

- **A.** for(Account theAccount : AccountList){ } ✅
- **B.** for(AccountList){ } ❌
- **C.** for(List L : AccountList){ } ❌
- **D.** for(Integer i=0; i < AccountList.Size(); i++){ } ✅

**📝 Dịch tiếng Việt:**
> Hai tùy chọn nào sau đây là đúng cú pháp Apex để duyệt qua từng bản ghi Account trong danh sách List<Account> có tên là AccountList? (Chọn 2)

**💬 Giải thích gốc (English):**
> The two valid options for iterating through each Account in the collection List named AccountList are:
> A. for(Account theAccount : AccountList){ }
> This is the most common and efficient way to iterate over a list in Apex. It directly iterates over each Account object in the AccountList, assigning it to the theAccount variable for processing.
> D. for(Integer i=0; i < AccountList.Size(); i++){ }
> This is a traditional for loop that iterates over the indices of the list. Inside the loop, you can access each Account using AccountList[i]. While this approach works, it's generally less efficient than the enhanced for loop in option A.

**✅ Tại sao đáp án đúng:**
> Chọn **A** và **D**.
- **A**: Đây là cú pháp vòng lặp for nâng cao (For-Each) chuẩn chỉnh để duyệt qua từng phần tử Account trong list.
- **D**: Đây là cú pháp vòng lặp for truyền thống sử dụng chỉ số index chạy từ 0 đến kích thước danh sách (`AccountList.size()`), lấy phần tử qua index.

**❌ Tại sao đáp án sai:**
> **B.** Sai cú pháp hoàn toàn vì thiếu khai báo biến lặp và kiểu dữ liệu chạy trong vòng lặp.
> **C.** Sai kiểu dữ liệu nghiêm trọng, biến chạy phải có kiểu dữ liệu là phần tử đơn lẻ `Account` chứ không thể là kiểu danh sách `List L` được.

**💡 Từ khóa ghi nhớ:** `Duyệt List trong Apex -> Chỉ dùng **`for(Type var : List)`** hoặc **`for(Integer i=0; i < List.size(); i++)`**!`

---

## Câu 322

**🔵 A developer created these three Rollup Summary fields in the custom object, Project__c: - Total_Timesheets__c
- Total_Approved_Timesheets__c - Total_Rejected_Timesheets__c The developer is asked to create a new field that shows the ratio between rejected and approved timesheets for a given project. Which should the developer use to implement the business requirement in order to minimize maintenance overhead?**

- **A.** Apex trigger ❌
- **B.** Record-triggered flow ❌
- **C.** Formula field ✅
- **D.** Field Update actions ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên đã tạo 3 trường Rollup Summary trên đối tượng Project__c gồm: Total_Timesheets__c, Total_Approved_Timesheets__c, và Total_Rejected_Timesheets__c. Lập trình viên được yêu cầu tạo thêm một trường mới hiển thị tỷ lệ (ratio) giữa Timesheets bị từ chối và được phê duyệt nhằm giảm thiểu tối đa công sức bảo trì hệ thống. Giải pháp tối ưu là gì?

**💬 Giải thích gốc (English):**
> Formula fields are calculated automatically whenever the related fields (Total_Approved_Timesheets__c and Total_Rejected_Timesheets__c) change. This ensures that the ratio is always up-to-date.
> Formula:
> (Total_Rejected_Timesheets__c / Total_Approved_Timesheets__c)

**✅ Tại sao đáp án đúng:**
> Chọn **C**. Tạo một trường công thức (**Formula field**) là giải pháp đỉnh cao và ít tốn công bảo trì nhất. Do cả 3 trường Rollup Summary đều tự động cập nhật giá trị vật lý lên database, trường công thức chỉ việc lấy các giá trị này ra chia cho nhau (ví dụ: `Total_Rejected_Timesheets__c / Total_Approved_Timesheets__c`). Đây là giải pháp hoàn toàn no-code, tự động cập nhật tức thì khi các trường liên quan thay đổi mà không cần bảo trì code.

**❌ Tại sao đáp án sai:**
> **A.** Viết trigger Apex là giải pháp cồng kềnh, tốn tài nguyên CPU vô ích và bắt buộc phải viết thêm test class để phủ code, làm tăng đáng kể công sức bảo trì.
> **B.** Record-triggered Flow cũng là một cơ chế chạy tự động phức tạp hơn, tốn công cấu hình và test hơn rất nhiều so với một trường công thức tự tính toán đơn giản.
> **D.** Field Update của Workflow Rules đời cũ đã bị khai tử, rất cồng kềnh và đòi hỏi các quy tắc trigger phức tạp hơn.

**💡 Từ khóa ghi nhớ:** `Tính toán tỷ lệ dựa trên các trường có sẵn trên cùng một bản ghi -> Luôn ưu tiên dùng **Formula field**!`

---

## Câu 323

**🔵 Which three statements are true regarding cross-object formulas? (Choose three.)**

- **A.** Cross-object formulas can reference fields from objects that are up to 10 relationships away. ✅
- **B.** Cross-object formulas can reference fields from master-detail or lookup relationships. ✅
- **C.** Cross-object formulas can reference child fields to perform an average. ❌
- **D.** Cross-object formulas can expose data the user does not have access to in a record. ✅
- **E.** Cross-object formulas can be referenced in roll-up summary fields. ❌

**📝 Dịch tiếng Việt:**
> Ba phát biểu nào sau đây là ĐÚNG khi nói về trường công thức chéo đối tượng (Cross-object formulas) trong Salesforce? (Chọn 3)

**💬 Giải thích gốc (English):**
> A Cross-object formula is a formula that spans two related objects and references merge fields on those objects. A cross-object formula can reference merge fields from a master (“parent”) object if an object is on the detail side of a master-detail relationship. A cross-object formula also works with lookup relationships.
> You can reference fields from objects that are up to 10 relationships away. A cross-object formula is available anywhere formulas are used except when creating default values.
> If you create a formula that references a field on another object and display that formula in your page layout, users can see the field on the object even if they don’t have access to that object record.

**✅ Tại sao đáp án đúng:**
> Chọn **A**, **B** và **D**.
- **A**: Cross-object formulas có khả năng tham chiếu trường chéo đối tượng đi lên cha tối đa lên tới **10 mối quan hệ** liên kết (`10 relationships away`).
- **B**: Hỗ trợ tham chiếu trường cực tốt qua cả mối quan hệ Master-Detail lẫn Lookup thông thường.
- **D**: Có thể hiển thị dữ liệu của bản ghi cha cho người dùng xem mặc dù bản thân người dùng đó không có quyền truy cập chia sẻ (`sharing`) vào bản ghi cha đó (bỏ qua cơ chế chia sẻ bảo mật để hiển thị dữ liệu cha).

**❌ Tại sao đáp án sai:**
> **C.** Sai nghiêm trọng! Trường công thức chéo đối tượng chỉ hỗ trợ đi ngược lên cha (parent) qua Lookup/Master-Detail, chứ cấm và không thể đi xuống để lấy dữ liệu các bản ghi con (child fields) tính trung bình được.
> **E.** Salesforce cấm không cho phép tham chiếu trường công thức chéo đối tượng làm bộ lọc hoặc giá trị cộng dồn trong các trường Roll-up Summary.

**💡 Từ khóa ghi nhớ:** `Đặc tính Cross-Object Formula -> Đi lên tối đa **10 cấp** quan hệ cha (Master-Detail/Lookup) + bỏ qua Sharing để hiển thị dữ liệu cha!`

---

## Câu 324

**🔵 A developer working on a time management application wants to make total hours for each timecard available to application users. A timecard entry has a Master Detail relationship to a timecard. Which approach should the developer use to accomplish this declaratively?**

- **A.** A Visualforce page that calculates the total number of hours for a timecard and displays it on the page ❌
- **B.** A Roll-Up Summary field on the Timecard Object that calculates the total hours from timecard entries for that timecard ✅
- **C.** A Process Builder process that updates a field on the timecard when a timecard entry is created ❌
- **D.** An Apex trigger that uses an Aggregate Query to calculate the hours for a given timecard and stores it in a custom field ❌

**📝 Dịch tiếng Việt:**
> Một ứng dụng quản lý thời gian yêu cầu hiển thị tổng số giờ của tất cả các bản ghi Timecard Entry con lên bản ghi Timecard cha. Timecard Entry liên kết với Timecard bằng quan hệ Master-Detail. Lập trình viên nên làm gì để giải quyết yêu cầu hoàn toàn bằng cấu hình khai báo (declarative/no-code)?

**💬 Giải thích gốc (English):**
> Roll-up summary fields are a declarative feature that can be configured directly in the object's field definition. The system automatically calculates the total hours whenever a new timecard entry is created, updated, or deleted, ensuring that the value is always up-to-date.

**✅ Tại sao đáp án đúng:**
> Chọn **B**. Vì mối quan hệ giữa Timecard (cha) và Timecard Entry (con) là **Master-Detail**, cách giải quyết bằng khai báo (declarative) tối ưu nhất là tạo một trường **Roll-Up Summary** trên đối tượng cha Timecard và chọn hàm `SUM` để tính tổng số giờ của các bản ghi con. Đây là tính năng có sẵn siêu mượt mà của Salesforce.

**❌ Tại sao đáp án sai:**
> **A.** Sử dụng Visualforce page đòi hỏi phải viết code và chỉ hiển thị trên giao diện của trang đó, chứ không lưu trữ giá trị thực vào database để phục vụ báo cáo.
> **C.** Process Builder là đồ cổ đã bị khai tử (deprecated) và nó cũng không hỗ trợ trực tiếp hàm cộng dồn SUM các bản ghi con một cách mượt mà.
> **D.** Apex trigger đòi hỏi phải code và viết unit test bao phủ, đi ngược hoàn toàn với yêu cầu giải quyết bằng cấu hình khai báo (declarative).

**💡 Từ khóa ghi nhớ:** `Tính tổng từ con lên cha trong quan hệ Master-Detail no-code -> Luôn gọi tên **Roll-Up Summary**!`

---

## Câu 325

**🔵 What can be used to override the Account's standard Edit button for Lightning Experience?**

- **A.** Lightning action ❌
- **B.** Lightning flow ❌
- **C.** Lightning page ❌
- **D.** Lightning component ✅

**📝 Dịch tiếng Việt:**
> Thành phần nào sau đây có thể được sử dụng để ghi đè (Override) nút bấm Edit tiêu chuẩn của Account trong môi trường Lightning Experience?

**💬 Giải thích gốc (English):**
> Lightning components are the ideal way to override standard buttons in Lightning Experience. They provide the flexibility to create custom user interfaces and behaviors, allowing you to customize the editing experience for Account records.

**✅ Tại sao đáp án đúng:**
> Chọn **D**. Để ghi đè (Override) một nút bấm tiêu chuẩn (như New, Edit, View) của một đối tượng trong Lightning Experience, Salesforce hỗ trợ sử dụng **Lightning Component** (Aura Component hoặc Lightning Web Component được bọc trong Aura) để thay thế hoàn toàn giao diện và logic chỉnh sửa mặc định.

**❌ Tại sao đáp án sai:**
> **A.** Lightning Action (Quick Action) chỉ là các nút bấm hành động nhanh do admin tự cấu hình thêm vào UI chứ không thể dùng để đè lên nút Edit tiêu chuẩn của hệ thống.
> **B.** Lightning Flow (Flow) không thể dùng để cấu hình trực tiếp ghi đè nút Edit tiêu chuẩn trong phần Object Manager.
> **C.** Lightning Page đại diện cho một trang bố cục hoàn chỉnh (như Record Page, Home Page) chứ không phải là một component linh kiện có khả năng ghi đè nút bấm hành động.

**💡 Từ khóa ghi nhớ:** `Ghi đè nút chuẩn (Override standard button) trong Lightning Experience -> Chỉ dùng **Lightning Component**!`

---

## Câu 326

**🔵 A developer needs to allow user to complete a form on an Account record that will create a record for a custom object, The form needs to display different fields depending on the user’s job role. The functionality should only be available to a small group of users. Which three things should the developer do to satisfy these requirements?**

- **A.** Add a dynamic action to the user’s assigned page layouts. ❌
- **B.** Create a light web component. ❌
- **C.** Create a dynamic form. ✅
- **D.** Add a dynamic action to the Account record page. ✅
- **E.** Create a custom permission for the users. ✅

**📝 Dịch tiếng Việt:**
> Yêu cầu: Cho phép user điền một biểu mẫu trên Account để tạo bản ghi cho đối tượng custom mới. Biểu mẫu này phải hiển thị các trường khác nhau tùy theo vai trò công việc (job role) của user. Tính năng này chỉ được hiển thị cho một nhóm nhỏ người dùng đặc biệt. Lập trình viên nên làm ba việc gì để đáp ứng yêu cầu no-code tối ưu nhất? (Chọn 3)

**✅ Tại sao đáp án đúng:**
> Chọn **C**, **D** và **E**.
- **C**: **Create a dynamic form** để ẩn/hiện các trường dữ liệu trên form một cách linh hoạt dựa trên vai trò của người dùng mà không cần tạo nhiều Page Layout.
- **D**: **Add a dynamic action to the Account record page** để đưa nút bấm gọi form lên trang chi tiết bản ghi, đồng thời thiết lập điều kiện hiển thị nút bấm động.
- **E**: **Create a custom permission** để làm điều kiện phân quyền hiển thị nút Dynamic Action, giúp giới hạn nút bấm chỉ hiển thị cho nhóm nhỏ người dùng được gán quyền.

**❌ Tại sao đáp án sai:**
> **A.** Page Layout truyền thống không hỗ trợ cấu hình động hiển thị trường một cách linh hoạt và mượt mà theo vai trò giống như Dynamic Form.
> **B.** Tạo LWC (Light Web Component hoặc Lightning Web Component) đòi hỏi phải viết code lập trình phức tạp, đi ngược lại tiêu chuẩn ưu tiên các tính năng cấu hình no-code cực mạnh có sẵn của Salesforce.

**💡 Từ khóa ghi nhớ:** `Ẩn hiện trường/nút động theo vai trò và quyền hạn -> Dùng ngay bộ ba nguyên tử **Dynamic Form + Dynamic Action + Custom Permission**!`

---

## Câu 327

**🔵 While writing an Apex class, a developer wants to make sure that all functionality being developed is handled as specified by the requirements. Which approach should the developer use to be sure that the Apex class is working according to specifications?**

- **A.** Include a try/catch block to the Apex class. ❌
- **B.** Run the code in an execute Anonymous block in the developer console. ❌
- **C.** Create a test class to execute the business logic and run the test in the developer console. ✅
- **D.** Include a savepoint and Database.rollback(). ❌

**📝 Dịch tiếng Việt:**
> Trong quá trình viết một Apex class, lập trình viên muốn đảm bảo toàn bộ các chức năng được phát triển hoạt động chính xác và trơn tru theo đúng tài liệu đặc tả yêu cầu nghiệp vụ. Lập trình viên nên áp dụng phương pháp nào?

**✅ Tại sao đáp án đúng:**
> Chọn **C**. Phương pháp chuẩn chỉnh và tự động hóa duy nhất để đảm bảo code hoạt động đúng đặc tả là xây dựng một **Test Class** để thực thi toàn bộ logic nghiệp vụ, sử dụng các câu lệnh `System.assertEquals()` để xác thực kết quả thực tế trùng khớp với mong đợi, và chạy kiểm thử trực tiếp trong Developer Console.

**❌ Tại sao đáp án sai:**
> **A.** Khối try/catch chỉ giúp bắt ngoại lệ tại runtime để chương trình không bị crash đột ngột, chứ không thể tự động hóa việc đo đạc độ chính xác của logic nghiệp vụ theo tài liệu đặc tả.
> **B.** Chạy code trong cửa sổ Execute Anonymous là phương pháp kiểm thử thủ công "một lần rồi thôi", không thể tái sử dụng lâu dài và không được coi là một quy trình kiểm thử chuẩn mực của hệ thống.
> **D.** Savepoint và rollback chỉ dùng để quản lý giao dịch DB (transaction) rollback khi gặp lỗi, hoàn toàn không có tác dụng kiểm thử logic nghiệp vụ.

**💡 Từ khóa ghi nhớ:** `Muốn kiểm tra code chạy đúng đặc tả nghiệp vụ -> Bắt buộc xây dựng hệ thống tự động qua **Test Class**!`

---

## Câu 328

**🔵 What should a developer use to obtain the Id and Name of all the Leads, Accounts, and Contacts that have the company name 'Universal Containers'?**

- **A.** FIND 'Universal Containers' IN CompanyName Fields RETURNING lead{ld,name), account(Id, name), contact(Id, name) ❌
- **B.** FIND 'Universal Containers' IN Name Fields RETURNING lead(id, name), account(Id, name), contact(Id, name) ✅
- **C.** SELECT lead(id, name), account(Id, name), contact(Id, name) FROM Lead, Account, Contact WHERE Name = "universal Containers' ❌
- **D.** SELECT Lead.id. Lead.Name, Account.Id, AccountName, Contacted, Contact.Name FROM Lead, Account, Contact WHERE CompanvName * Universal Containers' ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên muốn tìm kiếm và lấy ra Id và Name của tất cả các bản ghi Leads, Accounts, và Contacts có chứa tên công ty 'Universal Containers'. Cú pháp truy vấn nào là đúng?

**💬 Giải thích gốc (English):**
> IN CompanyName" does not exist.
> This query(B) will search for the string "Universal Containers" within the Name field of Lead, Account, and Contact objects and return the specified fields for matching records.

**✅ Tại sao đáp án đúng:**
> Chọn **B**. Đây là cú pháp tìm kiếm toàn văn SOSL chuẩn của Salesforce. Mệnh đề `FIND 'Universal Containers'` chỉ định chuỗi tìm kiếm, `IN Name Fields` chỉ định phạm vi tìm kiếm trong các trường tên, và `RETURNING` khai báo danh sách đối tượng cần lấy về kèm các trường cụ thể.

**❌ Tại sao đáp án sai:**
> **A.** Sai cú pháp nghiêm trọng! Mệnh đề `IN CompanyName Fields` không tồn tại trong SOSL (chỉ hỗ trợ All Fields, Name Fields, Email Fields, Phone Fields v.v.), đồng thời dấu ngoặc nhọn `{ld,name)` viết sai ngữ pháp.
> **C.** Truy vấn SOQL cấm không cho phép viết nhiều bảng độc lập ở mệnh đề FROM (`FROM Lead, Account, Contact` là hoàn toàn sai ngữ pháp SOQL).
> **D.** Tương tự câu C, SOQL cấm kết hợp nhiều bảng không có quan hệ trực hệ trong một câu SELECT duy nhất.

**💡 Từ khóa ghi nhớ:** `Tìm kiếm từ khóa trên nhiều Object độc lập -> Phải dùng **SOSL (`FIND ... IN Name Fields RETURNING ...`)**!`

---

## Câu 329

**🔵 In a single record, a user selects multiple values from a multi-select picklist. How are the selected values represented in Apex?**

- **A.** As a List<String> with each value as a element in the list. ❌
- **B.** As a String with each value separated by a comma ❌
- **C.** As a String with each value separated by a semicolon ✅
- **D.** As a Set<String> with each value as a element in the set. ❌

**📝 Dịch tiếng Việt:**
> Khi người dùng chọn nhiều giá trị trong một trường Multi-select Picklist trên một bản ghi, các giá trị được chọn này sẽ được đại diện dưới dạng kiểu dữ liệu gì bên trong ngôn ngữ Apex?

**💬 Giải thích gốc (English):**
> When a user selects multiple values from a multi-select picklist, the selected values are stored in the database as a single string, with each value separated by a comma.
> For example, if a user selects "Red", "Green", and "Blue" from a multi-select picklist, the value stored in the database would be "Red,Green,Blue".

**✅ Tại sao đáp án đúng:**
> Chọn **C**. Trong Apex, giá trị của trường Multi-select Picklist được trả về dưới dạng một chuỗi **String** duy nhất, trong đó các giá trị được phân tách với nhau bằng dấu chấm phẩy (semicolon **`;`**), ví dụ: `'Value1;Value2;Value3'`.

**❌ Tại sao đáp án sai:**
> **A.** Apex không tự động ánh xạ Multi-select Picklist thành kiểu `List<String>` ở sObject layer. Muốn có List, lập trình viên phải tự dùng hàm `.split(';')` thủ công.
> **B.** Dấu phẩy `,` là sai, Salesforce sử dụng dấu chấm phẩy làm ký tự phân cách chuẩn.
> **D.** Apex cũng không tự động ánh xạ trường này thành kiểu tập hợp `Set<String>`.

**💡 Từ khóa ghi nhớ:** `Multi-select Picklist trong Apex -> Luôn là một chuỗi **String** phân cách bằng dấu **chấm phẩy (`;`)**!`

---

## Câu 330

**🔵 What does the Lightning Component framework provide to developers?**

- **A.** Support for Classic and Lightning UIs ❌
- **B.** Templates to create custom components ❌
- **C.** Extended governor limits for applications ❌
- **D.** Prebuilt components that can be reused ✅

**📝 Dịch tiếng Việt:**
> Khung làm việc Lightning Component framework cung cấp lợi ích gì cho các lập trình viên?

**💬 Giải thích gốc (English):**
> The Lightning Component framework provides a rich set of pre-built components that developers can reuse to quickly build custom applications. These components handle common UI elements like buttons, input fields, modals, and data tables, saving developers time and effort.

**✅ Tại sao đáp án đúng:**
> Chọn **D**. Lightning Component framework cung cấp sẵn cho lập trình viên một thư viện khổng lồ gồm hàng trăm linh kiện có sẵn (`Base Lightning Components` như `lightning-button`, `lightning-datatable`...) giúp lập trình viên tái sử dụng nhanh chóng mà không cần tự xây dựng giao diện từ đầu, tiết kiệm thời gian phát triển tối đa.

**❌ Tại sao đáp án sai:**
> **A.** Lightning Component được thiết kế tối ưu và hướng tới giao diện Lightning Experience chứ không hỗ trợ hoàn hảo cho Classic UI.
> **B.** Framework cung cấp các component có sẵn chứ không tập trung vào việc cung cấp các "Templates" mẫu để tạo custom component.
> **C.** Cú lừa kinh điển! Lightning Component Framework hoàn toàn **không** thay đổi hay mở rộng bất kỳ giới hạn Governor Limits nào của hệ thống Apex hay Database (ví dụ như giới hạn SOQL, DML vẫn giữ nguyên).

**💡 Từ khóa ghi nhớ:** `Lightning Component Framework -> Đem đến rổ linh kiện ăn sẵn **Prebuilt components** cực tiện lợi!`

---

## Câu 331

**🔵 What are two benefits of the Lightning Component framework? (Choose two.)**

- **A.** It simplifies complexity when building pages, but not applications. ❌
- **B.** It provides an event-driven architecture for better decoupling between components. ✅
- **C.** It promotes faster development using out-of-box components that are suitable for desktop and mobile devices. ✅
- **D.** It allows faster PDF generation with Lightning components. ❌

**📝 Dịch tiếng Việt:**
> Hai lợi ích nổi bật nhất của kiến trúc lập trình Lightning Component Framework (Aura/LWC) là gì? (Chọn 2)

**💬 Giải thích gốc (English):**
> It provides an event-driven architecture for better decoupling between components.
> This allows for modularity and reusability of components. Components can communicate with each other through events, making the overall application more maintainable and scalable.
> It promotes faster development using out-of-box components that are suitable for desktop and mobile devices.
> The framework provides a wide range of pre-built components that can be customized and used to create responsive user interfaces that adapt to different screen sizes. This accelerates development time and ensures consistency across devices.

**✅ Tại sao đáp án đúng:**
> Chọn **B** và **C**.
- **B**: Framework cung cấp kiến trúc hướng sự kiện (event-driven architecture) cực đỉnh, giúp các component độc lập và tách biệt (decoupling) với nhau hơn, dễ dàng truyền tin thông qua các Event mà không sợ bị dính chặt vào nhau.
- **C**: Giúp lập trình viên "tăng tốc về đích" nhờ sở hữu hàng tá các component có sẵn (out-of-the-box) siêu xịn, tự động co giãn tương thích đa thiết bị (responsive cho cả desktop và mobile) mà không cần nhọc công viết media queries.

**❌ Tại sao đáp án sai:**
> **A.** Nói ngược! Lightning Component Framework sinh ra là để tối giản hóa độ phức tạp cho việc xây dựng cả các trang đơn lẻ lẫn toàn bộ hệ thống ứng dụng quy mô lớn, chứ không chỉ gói gọn trong các page.
> **D.** Không hề tồn tại bất kỳ cơ chế hay tính năng nào liên quan đến tăng tốc tạo file PDF bên trong cốt lõi của Lightning Component Framework cả. Lại là một cú lừa bịa đặt!

**💡 Từ khóa ghi nhớ:** `Lợi ích Lightning Component -> **Hướng sự kiện (Event-driven)** + **Ăn sẵn responsive đa thiết bị (Out-of-the-box Desktop/Mobile)**!`

---

## Câu 332

**🔵 Given the following code snippet, that is part of a custom controller for a Visualforce page:
public void updateContact(Contact thisContact){
thisContact.Is_Active__c = false;
try{
update thisContact;
}catch(Exception e){
String errorMessage = 'An error occurred while updating the Contact. '+e.getMessage());
ApexPages.addmessage (new ApexPages.message (ApexPages.severity.FATAL,errorMessage));
}
}
In which two ways can the try/catch be enclosed to enforce object-level permissions and prevent the DML statement from being executed if the current logged- in user does not have the appropriate level of access to the object? (Choose two.)**

- **A.** Use if(thisContact.OwnerId == User.Info.getUserId()) ❌
- **B.** Use if(Schema.sObjectType.Contact.isAccessible()) ✅
- **C.** Use if(Schema.sObjectType.Contact.fields.Is_Active__c.isUpdateable()) ❌
- **D.** Use if(Schema.sObjectType.Contact.isUpdateable()) ✅

**📝 Dịch tiếng Việt:**
> Cho đoạn code cập nhật Contact trong Custom Controller của Visualforce Page:
```apex
public void updateContact(Contact thisContact){
  thisContact.Is_Active__c = false;
  try{
    update thisContact;
  }catch(Exception e){
    String errorMessage = 'An error occurred while updating the Contact. '+e.getMessage();
    ApexPages.addmessage (new ApexPages.message (ApexPages.severity.FATAL,errorMessage));
  }
}
```
Lập trình viên nên bọc khối lệnh try/catch bằng những điều kiện nào sau đây để kiểm tra quyền hạn cấp đối tượng (object-level permissions) của người dùng hiện tại trước khi thực thi DML? (Chọn 2)

**💬 Giải thích gốc (English):**
> B. Schema.sObjectType.<objectApiName>.isAccessible() checks if the current user has has read access to the specified object.
> D. Use if(Schema.sObjectType.Contact.isUpdateable()) checks if the current user has permission to update on the object.

**✅ Tại sao đáp án đúng:**
> Chọn **B** và **D**.
- **B**: Sử dụng `Schema.sObjectType.Contact.isAccessible()` để kiểm tra xem người dùng hiện tại có quyền Xem (Read) đối tượng Contact hay không.
- **D**: Sử dụng `Schema.sObjectType.Contact.isUpdateable()` để kiểm tra xem người dùng hiện tại có quyền Sửa (Update) đối tượng Contact trước khi gọi lệnh cập nhật dữ liệu. Đây là hai phương thức chuẩn chỉnh của Apex để kiểm tra bảo mật cấp đối tượng (CRUD).

**❌ Tại sao đáp án sai:**
> **A.** So khớp `OwnerId` chỉ giúp kiểm tra xem người dùng hiện tại có phải là chủ sở hữu của bản ghi cụ thể đó hay không, chứ hoàn toàn bất lực trong việc xác định quyền phân quyền hệ thống cấp đối tượng (CRUD) của Profile/Permission Set.
> **C.** `Schema.sObjectType.Contact.fields.Is_Active__c.isUpdateable()` là hàm dùng để kiểm tra quyền hạn cấp trường (FLS - Field-level security) của trường `Is_Active__c`, đi lệch hướng hoàn toàn so với yêu cầu kiểm tra quyền cấp đối tượng (Object-level) của đề bài.

**💡 Từ khóa ghi nhớ:** `Quyền cấp Đối tượng (Object-level CRUD) -> Dùng **`isAccessible()`** (Xem) và **`isUpdateable()`** (Sửa) trực tiếp trên **`sObjectType`**!`

---

## Câu 333

**🔵 What can be used to delete components from production?**

- **A.** A change set deployment with a destructiveChanges XML file ❌
- **B.** A change set deployment with the delete option checked ❌
- **C.** An ant migration tool deployment with a destructiveChanges XML file and an empty package.xml file ✅
- **D.** An ant migration tool deployment with a desctuctiveChanges XML file and the components to delete in the package.xml file ❌

**📝 Dịch tiếng Việt:**
> Công cụ/Phương pháp nào sau đây có thể được sử dụng để xóa bỏ hoàn toàn các thành phần metadata (như Apex class, trường tùy chỉnh) khỏi môi trường Production?

**💬 Giải thích gốc (English):**
> Destructive Changes XML File: This file specifically lists the components you want to delete.
> Empty package.xml File: An empty package.xml file indicates that you're not deploying any new or modified components, only deleting the ones specified in the destructiveChanges.xml file.

**✅ Tại sao đáp án đúng:**
> Chọn **C**. Để xóa bỏ các thành phần metadata đã trót deploy lên Production, cách kinh điển và chuẩn xác nhất là thực hiện deploy qua công cụ dòng lệnh (như Ant Migration Tool hoặc Salesforce CLI) với một tệp tin khai báo xóa tên là **`destructiveChanges.xml`** đi kèm với một tệp **`package.xml` trống rỗng** (chỉ chứa khai báo phiên bản). Khi đó, Salesforce sẽ biết là bạn chỉ muốn xóa các thành phần được liệt kê trong file destructive mà không muốn deploy thêm gì mới.

**❌ Tại sao đáp án sai:**
> **A.** Change Sets tiêu chuẩn trên giao diện web hoàn toàn là công cụ kéo thả, nó cấm tiệt và không hỗ trợ nạp tệp cấu hình `destructiveChanges.xml` để xóa metadata.
> **B.** Change Sets không hề cung cấp bất kỳ nút check hay tùy chọn nào mang tên "delete option checked" để xóa các thành phần metadata cả.
> **D.** Nếu bạn vẫn tiếp tục khai báo các thành phần cần xóa vào tệp `package.xml`, Salesforce sẽ hiểu lầm là bạn đang muốn triển khai/cập nhật chúng, dẫn đến việc xóa thất bại thảm hại.

**💡 Từ khóa ghi nhớ:** `Xóa metadata trên Production -> Bắt buộc dùng **`destructiveChanges.xml`** đi kèm tệp **`package.xml` TRỐNG**!`

---

## Câu 334

**🔵 A developer is debugging the following code to determine why Accounts are not being created. Account a = new Account(Name = 'A'); Database.insert(a, false); How should the code be altered to help debug the issue?**

- **A.** Add a System.debug() statement before the insert method. ❌
- **B.** Collect the insert method return value in a SaveResult record. ✅
- **C.** Set the second insert method parameter to TRUE. ❌
- **D.** Add a try/catch around the insert method. ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên đang thực hiện gỡ lỗi (debug) đoạn mã sau để tìm hiểu nguyên nhân tại sao các bản ghi Account không được tạo thành công:
```apex
Account a = new Account(Name = 'A');
Database.insert(a, false);
```
Lập trình viên nên thay đổi đoạn code trên thế nào để thu được thông tin debug lỗi chính xác nhất?

**💬 Giải thích gốc (English):**
> By collecting the return value of the Database.insert() method in a SaveResult record, you can access information about the success or failure of the insert operation. This includes error messages, IDs of newly created records, and other details.
> Here's how you can modify the code:
> Apex
> Account a = new Account(Name = 'A');
> List<Account> accountList = new List<Account>();
> accountList.add(a);
> List<Database.SaveResult> results = Database.insert(accountList, false);
> if (results[0].isSuccess()) {
> System.debug('Account created successfully: ' + results[0].getId());
> } else {
> System.debug('Error creating Account: ' + results[0].getErrors()[0].getMessage());
> }

**✅ Tại sao đáp án đúng:**
> Chọn **B**. Khi sử dụng phương thức `Database.insert(records, allOrNone)` với tham số thứ hai là `false`, Salesforce sẽ **không bao giờ ném ra Exception** khi gặp lỗi để chương trình tiếp tục chạy. Do đó, để biết được bản ghi có bị oẳng hay không và oẳng vì lỗi gì, lập trình viên bắt buộc phải hứng kết quả trả về của hàm này vào một thực thể **`Database.SaveResult`** (hoặc `List<Database.SaveResult>`), sau đó kiểm tra thuộc tính `.isSuccess()` và gọi hàm `.getErrors()` để in chi tiết thông tin lỗi.

**❌ Tại sao đáp án sai:**
> **A.** Thêm `System.debug()` trước khi hàm insert chạy thì chỉ in ra được dữ liệu trước khi chèn, chứ không thể biết kết quả của việc insert thành bại thế nào.
> **C.** Nếu đổi tham số thành `true`, Salesforce sẽ lập tức quăng lỗi Exception làm crash toàn bộ tiến trình. Cách này chỉ làm dừng chương trình đột ngột chứ không giúp lập trình viên viết code chủ động hứng lỗi để xử lý debug một cách thông minh được.
> **D.** Do tham số thứ hai được đặt là `false` nên Salesforce hoàn toàn im lặng và không bao giờ ném ngoại lệ (exception) khi chèn lỗi. Khối `catch` của bạn sẽ bị bỏ qua và trở nên hoàn toàn vô dụng!

**💡 Từ khóa ghi nhớ:** `Gọi Database.DML với tham số **`false`** -> Bắt buộc đi kèm hứng kết quả bằng **`SaveResult`**!`

---

## Câu 335

**🔵 Managed Packages can be created in which type of org?**

- **A.** Developer Sandbox ❌
- **B.** Partial Copy Sandbox ❌
- **C.** Unlimited Edition ❌
- **D.** Developer Edition ✅

**📝 Dịch tiếng Việt:**
> Managed Packages (Gói ứng dụng được quản lý) có thể được khởi tạo và phát triển trong loại môi trường tổ chức (Org) nào sau đây?

**💬 Giải thích gốc (English):**
> You must use a Developer Edition organization to create and work with a managed package. A Developer Edition organization can contain a single managed package and many unmanaged packages.

**✅ Tại sao đáp án đúng:**
> Chọn **D**. Đây là quy định cứng của Salesforce: chỉ có môi trường **Developer Edition** (hoặc các org đối tác chuyên dụng như Partner Developer Edition) mới hỗ trợ đăng ký Namespace độc quyền và cho phép đóng gói, phát hành Managed Package lên chợ ứng dụng AppExchange.

**❌ Tại sao đáp án sai:**
> **A.** Developer Sandbox chỉ là một bản sao môi trường để dev và test code nội bộ của một doanh nghiệp cụ thể, hoàn toàn bị cấm đóng gói Managed Package.
> **B.** Partial Copy Sandbox cũng tương tự Sandbox thường, không có khả năng đăng ký Namespace để đóng gói ứng dụng phát hành thương mại.
> **C.** Unlimited Edition là môi trường sản xuất (Production) thực tế của khách hàng dùng để vận hành doanh nghiệp, không hỗ trợ tính năng làm "nhà máy đóng gói" Managed Package.

**💡 Từ khóa ghi nhớ:** `Nơi đóng gói và sản xuất Managed Package -> Bắt buộc phải là **Developer Edition**!`

---

## Câu 336

**🔵 A Platform Developer needs to implement a declarative solution that will display the most recent Closed Won date for all Opportunity records associated with an Account. Which field is required to achieve this declaratively?**

- **A.** Roll-up summary field on the Opportunity object ❌
- **B.** Cross-object formula field on the Opportunity object ❌
- **C.** Roll-up summary field on the Account object ✅
- **D.** Cross-object formula field on the Account object ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên cần hiển thị ngày thắng cơ hội thành công gần nhất ('Closed Won' date) của toàn bộ các Opportunity liên quan lên bản ghi Account cha bằng công cụ no-code. Trường nào cần cấu hình để đạt được điều này?

**💬 Giải thích gốc (English):**
> An opportunity has a lookup field of account. Even though the relationship is a lookup, Salesforce treats certain standard object relationships in a hybrid model i.e. Relationship is Lookup but behaves like Master-Detail
> Also in the backend, there is a relationship property 'cascade delete' between Contact and Account which is always set to True. You will find the same cascade delete Property between objects in a Master-Detail Relationship.
> So for any relationship where the cascade delete is set to True a child record is deleted when the parent is deleted.

**✅ Tại sao đáp án đúng:**
> Chọn **C**. Do mối quan hệ giữa Account (cha) và Opportunity (con) là một mối quan hệ đặc biệt được Salesforce hỗ trợ các hàm tổng hợp no-code, cách tối ưu nhất là tạo một trường **Roll-up Summary field ngay trên Account cha**. Sau đó cấu hình chọn hàm **`MAX`** trỏ vào trường `CloseDate` của Opportunity con, kết hợp với điều kiện lọc bản ghi con có `Stage = 'Closed Won'`.

**❌ Tại sao đáp án sai:**
> **A.** Tạo trường Roll-up Summary ngay trên đối tượng Opportunity con là sai hoàn toàn về mặt chiều thiết kế dữ liệu (chỉ có cha mới Roll-up được con).
> **B.** Cross-object formula field trên Opportunity chỉ hỗ trợ kéo dữ liệu từ cha Account xuống con chứ không thể đi ngược từ dưới lên để tính toán tổng hợp dữ liệu.
> **D.** Tương tự câu B, trường công thức chéo trên Account cấm tiệt việc lội xuống danh sách Opportunity con để tính toán.

**💡 Từ khóa ghi nhớ:** `Cộng dồn hoặc lấy ngày lớn nhất/nhỏ nhất của bản ghi con đưa lên cha -> Luôn tạo trường **Roll-up Summary** nằm trên đối tượng **CHA**!`

---

## Câu 337

**🔵 Universal Containers wants Opportunities to be locked from editing when reaching the Closed/Won stage. Which two strategies should a developer use to accomplish this? (Choose two.)**

- **A.** Use a Visual Workflow. ❌
- **B.** Use a validation rule. ✅
- **C.** Use the Process Automation Settings. ❌
- **D.** Use a Trigger. ✅

**📝 Dịch tiếng Việt:**
> Universal Containers muốn khóa không cho phép người dùng chỉnh sửa Opportunity khi cơ hội đạt trạng thái 'Closed/Won'. Hai giải pháp nào lập trình viên nên chọn? (Chọn 2)

**💬 Giải thích gốc (English):**
> Use a validation rule: Create a validation rule that fires when the Opportunity Stage is changed to "Closed Won". The rule can check if the Opportunity is already closed won and throw an error message if the user attempts to edit any fields.
> Using a trigger and addError() is a powerful and flexible approach to validate data and prevent invalid records from being created or updated in Salesforce.

**✅ Tại sao đáp án đúng:**
> Chọn **B** và **D**.
- **B**: Sử dụng một **Validation Rule** để so sánh: nếu bản ghi có trạng thái cũ là 'Closed/Won' (hoặc giá trị trường đã đóng thắng) và người dùng cố gắng lưu các chỉnh sửa mới, ta sẽ trả về thông báo lỗi chặn lưu. Đây là cách no-code siêu nhanh và hiệu quả.
- **D**: Sử dụng một **Apex Trigger** ở sự kiện `before update` để kiểm tra trạng thái của bản ghi. Nếu phát hiện cơ hội đã đóng thắng mà người dùng vẫn cố sửa đổi, ta gọi hàm `.addError()` để chặn đứng giao dịch và ném lỗi ra màn hình.

**❌ Tại sao đáp án sai:**
> **A.** Visual Workflow (Flow) chỉ đóng vai trò hướng dẫn người dùng nhập liệu theo từng bước trên UI, chứ nó không có khả năng tạo ra một hàng rào bảo vệ vững chắc để khóa cứng database khi người dùng cập nhật dữ liệu từ các công cụ khác như API/Data Loader.
> **C.** Process Automation Settings chứa các cấu hình hệ thống chung cho các tiến trình tự động hóa của Org, hoàn toàn không có tính năng hỗ trợ khóa riêng lẻ một bản ghi Opportunity theo Stage.

**💡 Từ khóa ghi nhớ:** `Khóa bản ghi chống chỉnh sửa dữ liệu -> Dùng **Validation Rule** (no-code) hoặc **Apex Trigger với `addError()`** (code)!`

---

## Câu 338

**🔵 A development team wants to use a deployment script to automatically deploy to a sandbox during their development cycles. Which two tools can they use to run a script that deploys to a sandbox? (Choose two.)**

- **A.** SFDX CLI ✅
- **B.** Developer Console ❌
- **C.** Change Sets ❌
- **D.** VSCode ✅

**📝 Dịch tiếng Việt:**
> Một đội ngũ phát triển muốn sử dụng một tập lệnh (deployment script) để tự động hóa việc deploy code lên sandbox trong chu kỳ phát triển. Hai công cụ nào họ có thể sử dụng để chạy tập lệnh này? (Chọn 2)

**💬 Giải thích gốc (English):**
> SFDX CLI: A powerful command-line tool for automating Salesforce development tasks, including deployments. It allows you to create scripts to deploy metadata changes to sandboxes.
> VSCode: A popular code editor with extensions that can integrate with SFDX. You can use it to write and run deployment scripts, as well as to automate the deployment process using tasks and workflows.

**✅ Tại sao đáp án đúng:**
> Chọn **A** và **D**.
- **A**: **SFDX CLI** (Salesforce CLI) là công cụ dòng lệnh (command-line) chính thống, cực kỳ mạnh mẽ, sinh ra để lập trình viên viết script tự động hóa tích hợp vào CI/CD deploy metadata lên sandbox.
- **D**: **VS Code** kết hợp với bộ công cụ Salesforce Extension Pack cung cấp một môi trường tích hợp tuyệt vời, cho phép dev chạy các tập lệnh deploy, gọi CLI trực tiếp từ terminal của IDE.

**❌ Tại sao đáp án sai:**
> **B.** Developer Console là một công cụ nền web thủ công trên trình duyệt, hoàn toàn cấm và không có khả năng deploy code trực tiếp từ các file metadata cục bộ từ máy tính của dev.
> **C.** Change Sets chỉ hỗ trợ tạo gói deploy bằng giao diện kéo thả click chuột thủ công (Point-and-click) trên trình duyệt, không có API hay dòng lệnh nào để nhúng vào script chạy tự động.

**💡 Từ khóa ghi nhớ:** `Script tự động hóa deploy -> Bắt buộc dùng bộ đôi công nghệ phát triển hiện đại **Salesforce CLI** và **VS Code**!`

---

## Câu 339

**🔵 Using the Schema Builder, a developer tries to change the API name of a field that is referenced in an Apex test class. What is the end result?**

- **A.** The API name is not changed and there are no other impacts. ✅
- **B.** The API name of the field and the reference in the test class is changed. ❌
- **C.** The API name of the field is changed, and a warning is issued to update the class. ❌
- **D.** The API name of the field and the reference in the test class is updated. ❌

**📝 Dịch tiếng Việt:**
> Thông qua công cụ Schema Builder, lập trình viên cố gắng thay đổi API Name (tên định danh hệ thống) của một trường tùy chỉnh đang được tham chiếu sử dụng trong một lớp Apex Test Class. Kết quả nhận được là gì?

**💬 Giải thích gốc (English):**
> Change the API name of a field
> The API name of a Field or Object is necessary, as this will be referenced in the metadata ( i.e Apex Classes, Triggers, Visualforce Pages, Visualforce Components etc). It is not allowed for Users to change the API name of the Objects/Fields, if it is referenced in any of the metadata. The changing of API Name without removing references can result in errors being thrown as the operation will be unsupported.

**✅ Tại sao đáp án đúng:**
> Chọn **A**. Salesforce quản lý tính toàn vẹn của mã nguồn (metadata integrity) cực kỳ nghiêm ngặt. Khi một trường đang được tham chiếu trực tiếp bằng code trong bất kỳ một Apex Class hay Test Class nào, Salesforce sẽ **chặn đứng** hành động đổi tên API Name trên Schema Builder và báo lỗi. Tên trường sẽ được giữ nguyên hoàn toàn và không gây ra thêm bất kỳ tác động tiêu cực nào cho hệ thống.

**❌ Tại sao đáp án sai:**
> **B.** Salesforce không có tính năng "thần thông quảng đại" tự động đi sửa đổi đống code Apex trong test class khi bạn đổi tên trường trên UI.
> **D.** Tương tự, Salesforce cũng không tự động cập nhật tham chiếu trong bất kỳ code nào khác khi tên trường thay đổi.
> **C.** Hệ thống sẽ chặn đứng hoàn toàn hành vi chỉnh sửa ngay từ đầu chứ không có chuyện cho phép đổi tên thành công rồi mới ném ra cảnh báo cập nhật class sau.

**💡 Từ khóa ghi nhớ:** `Sửa API Name của trường đang có code tham chiếu -> Salesforce **chặn đứng và giữ nguyên (not changed)** để bảo vệ hệ thống!`

---

## Câu 340

**🔵 A Next Best Action strategy uses an Enhance Element that invokes an Apex method to determine a discount level for a Contact, based on a number of factors. What is the correct definition of the Apex method?**

- **A.** @InvocableMethod global static List<List<Recommendation>> getLevel(List<ContactWrapper> input) { /*implementation*/ } ✅
- **B.** @InvocableMethod global List<List<Recommendation>> getLevel(List<ContactWrapper> input){ /*implementation*/ } ❌
- **C.** @InvocableMethod global static ListRecommendation getLevel(List<ContactWrapper> input){ /*implementation*/ } ❌
- **D.** @InvocableMethod global Recommendation getLevel(ContactWrapper input){ /*implementation*/ } ❌

**📝 Dịch tiếng Việt:**
> Một chiến lược Next Best Action sử dụng Enhance Element để gọi một Apex method nhằm xác định mức chiết khấu cho Contact dựa trên một số yếu tố. Khai báo cấu trúc phương thức Apex nào sau đây là ĐÚNG quy chuẩn?

**💬 Giải thích gốc (English):**
> Invocable methods are called natively from Rest, Apex, Flow, or Einstein bot that interacts with the external API source. Invocable methods have dynamic input and output values and support describe calls. The invocable method must be static and public or global, and its class must be an outer class.

**✅ Tại sao đáp án đúng:**
> Chọn **A**. Đây là cú pháp chuẩn không thể lệch đi đâu được của một Invocable Method dùng trong Next Best Action (Enhance Element):
- Sử dụng annotation **`@InvocableMethod`**.
- Phương thức bắt buộc phải là **`static`**.
- Để hỗ trợ cơ chế chạy hàng loạt bulkified, tham số truyền vào bắt buộc phải là một danh sách: **`List<T>`** (ở đây là `List<ContactWrapper>`).
- Đối với Enhance Element trong NBA, kiểu trả về bắt buộc phải là một danh sách lồng danh sách: **`List<List<Recommendation>>`** để hệ thống map kết quả tương ứng cho từng bản ghi đầu vào.

**❌ Tại sao đáp án sai:**
> **B.** Sai vì thiếu mất từ khóa **`static`** bắt buộc của Invocable Method.
> **C.** Viết sai kiểu trả về `ListRecommendation` (thiếu cặp dấu ngoặc nhọn `<>` và kiểu lồng `List<List<>>` để bulkify).
> **D.** Sai hoàn toàn vì vừa thiếu từ khóa `static`, vừa không bọc tham số đầu vào và đầu ra trong danh sách `List` để chạy bulkified.

**💡 Từ khóa ghi nhớ:** `Invocable Method trong Next Best Action -> Phải là **`static`** + nhận vào **`List<T>`** + trả về **`List<List<Recommendation>>`**!`

---

## Câu 341

**🔵 An Apex transaction inserts 100 Account records and 2,000 Contact records before encountering a DML exception when attempting to insert 500 Opportunity records. The Account records are inserted by calling the database.insert() method with the allOrNone argument set to false. The Contact and Opportunity records are inserted using the standalone insert statement. How many total records will be committed to the database in this transaction?**

- **A.** 2,000 ❌
- **B.** 2,100 ❌
- **C.** 0 ✅
- **D.** 100 ❌

**📝 Dịch tiếng Việt:**
> Một Apex transaction thực hiện chèn thành công 100 Accounts (bằng Database.insert(accts, false)). Tiếp tục chèn thành công 2,000 Contacts (bằng lệnh insert standalone). Cuối cùng bị báo lỗi DML Exception khi cố chèn 500 Opportunities (bằng lệnh insert standalone). Hỏi tổng cộng có bao nhiêu bản ghi thực sự được lưu (commit) thành công vào cơ sở dữ liệu sau transaction này?

**💬 Giải thích gốc (English):**
> All operations are in one transaction. If any operation in the transaction fails, all DML operation are rolledback.

**✅ Tại sao đáp án đúng:**
> Chọn **C: 0**. Đây là câu hỏi kinh điển kiểm tra kiến thức về tính toàn vẹn của Transaction (Giao dịch) trong Salesforce. Một Apex Transaction hoạt động theo nguyên tắc "tất cả hoặc không có gì" (all-or-nothing). Một khi có một Exception không được xử lý (như DML Exception khi insert Opportunity) nổ ra ở bất cứ thời điểm nào, Salesforce sẽ lập tức **rollback (hoàn tác) toàn bộ giao dịch về vạch xuất phát**, xóa sạch mọi dữ liệu đã chèn tạm trước đó để bảo vệ tính toàn vẹn dữ liệu. Do đó, không có bản ghi nào được lưu thành công!

**❌ Tại sao đáp án sai:**
> **A.** Nghĩ là 2,000 Contacts được giữ lại là sai lầm lớn, do lỗi xảy ra ở bước sau làm rollback toàn cục.
> **B.** Sai tính toán.
> **D.** Đây là "cú lừa" cực kỳ hiểm hóc! Nhiều bạn nghĩ 100 Accounts dùng `Database.insert(..., false)` thì sẽ được an toàn giữ lại. Thực tế, tham số `false` chỉ giúp câu lệnh chèn Account đó bỏ qua các bản ghi lỗi nội bộ trong chính dòng lệnh đó để tiếp tục chạy các dòng lệnh tiếp theo. Nhưng một khi toàn bộ Transaction đã bị nổ Exception ở bước cuối (Opportunity insert) mà không được try-catch hứng lại, Salesforce vẫn sẽ rollback sạch sành sanh từ đầu, cào bằng tất cả về 0!

**💡 Từ khóa ghi nhớ:** `Apex Transaction: Có Exception nổ ra không được catch -> **Toàn bộ bản ghi bị rollback về 0**! Đừng để bị lừa bởi tham số `false`.`

---

## Câu 342

**🔵 Universal Containers stores the availability date on each Line Item of an Order and Orders are only shipped when all of the Line Items are available. Which method should be used to calculate the estimated ship date for an Order?**

- **A.** Use a LATEST formula on each of the latest availability date fields. ❌
- **B.** Use a CEILING formula on each of the latest availability date fields. ❌
- **C.** Use a DAYS formula on each of the availability date fields and a COUNT Roll-Up Summary field on the Order. ❌
- **D.** Use a MAX Roll-Up Summary field on the latest availability date fields. ✅

**📝 Dịch tiếng Việt:**
> Universal Containers lưu trữ ngày có hàng (availability date) trên từng Line Item con của Order. Đơn hàng chỉ được phép giao khi tất cả các Line Items đều có hàng. Phương pháp no-code nào tối ưu nhất để tự động xác định ngày giao hàng ước tính của Order cha?

**💬 Giải thích gốc (English):**
> A MAX Roll-Up Summary field is the most suitable option for this scenario. It will calculate the maximum availability date among all line items associated with an order. This maximum date will represent the latest availability date for any item in the order, which, in turn, will be the estimated ship date.

**✅ Tại sao đáp án đúng:**
> Chọn **D**. Để đơn hàng có thể giao khi "tất cả các món con đều có sẵn", ngày giao hàng ước tính của Order cha bắt buộc phải là ngày có hàng **muộn nhất** (tức là ngày lớn nhất - **MAX**) trong số tất cả các bản ghi Line Item con. Vì mối quan hệ giữa Order và Line Item là Master-Detail, cách giải quyết no-code hoàn hảo nhất là tạo một trường **Roll-up Summary field sử dụng hàm MAX** trên Order cha trỏ vào trường ngày của con.

**❌ Tại sao đáp án sai:**
> **A.** Hoàn toàn không tồn tại bất kỳ hàm nào tên là LATEST trong cấu trúc trường công thức của Salesforce.
> **B.** Hàm CEILING là hàm toán học chuyên dùng để làm tròn lên một số thực phân số, hoàn toàn vô dụng khi xử lý kiểu dữ liệu ngày tháng.
> **C.** Đếm số lượng bản ghi con COUNT không giúp chúng ta xác định được mốc thời gian muộn nhất để giao hàng.

**💡 Từ khóa ghi nhớ:** `Tìm ngày muộn nhất (latest date) của các bản ghi con đưa lên cha -> Tạo trường **Roll-up Summary dùng hàm MAX**!`

---

## Câu 343

**🔵 The following Apex method is part of the ContactService class that is called from a trigger:
public static void setBusinessUnitToEMEA(Contact thisContact){
thisContact.Business_Unit__c = 'EMEA';
update thisContact;
}
How should the developer modify the code to ensure best practices are met?**

- **A.** Public void setBusinessUnitToEMEA(List<Contact> contatcs){ contacts[0].Business_Unit__c = 'EMEA' ; update contacts[0]; } ❌
- **B.** Public static void setBusinessUnitToEMEA(Contact thisContact){ List<Contact> contacts = new List<Contact>(); contacts.add(thisContact.Business_Unit__c = 'EMEA'); update contacts; } ❌
- **C.** Public static void setBusinessUnitToEMEA(List<Contact> contacts){ for(Contact thisContact : contacts){ thisContact.Business_Unit__c = 'EMEA' ; update contacts[0]; } } ❌
- **D.** Public static void setBusinessUnitToEMEA(List<Contact> contacts){ for(Contact thisContact : contacts) { thisContact.Business_Unit__c = 'EMEA' ; } update contacts; } ✅

**📝 Dịch tiếng Việt:**
> Cho phương thức Apex sau được gọi từ một Trigger:
```apex
public static void setBusinessUnitToEMEA(Contact thisContact){
  thisContact.Business_Unit__c = 'EMEA';
  update thisContact;
}
```
Developer nên sửa đổi code như thế nào để đảm bảo tuân thủ best practices (thực hành tốt nhất) của Salesforce trigger?

**💬 Giải thích gốc (English):**
> A DML statement should be placed outside of a loop to optimize performance and reduce governor limit usage.

**✅ Tại sao đáp án đúng:**
> Chọn **D**. Đây là bài học vỡ lòng và là "kinh thánh" tối thượng khi viết Trigger trong Salesforce: **Bulkification**.
- Phương thức bắt buộc phải nhận tham số đầu vào là một danh sách **`List<Contact> contacts`** để có thể xử lý hàng loạt nhiều bản ghi cùng một lúc.
- Sử dụng vòng lặp `for` để cập nhật dữ liệu trên bộ nhớ, và cực kỳ quan trọng: **đưa câu lệnh DML `update contacts;` ra hẳn NGOÀI vòng lặp for** để chỉ thực thi đúng 1 lệnh DML duy nhất cho cả danh sách, tránh đụng trần giới hạn 150 DML Limit của hệ thống.

**❌ Tại sao đáp án sai:**
> **A.** Chỉ xử lý phần tử đầu tiên của danh sách (`contacts[0]`) và thực hiện DML đơn lẻ là viết code cực kỳ "non và xanh", làm hỏng tính năng xử lý hàng loạt khi người dùng import dữ liệu bằng Data Loader.
> **B.** Cú pháp gán trị chèn vào list viết sai ngữ pháp nghiêm trọng.
> **C.** Lại một tấm chiếu mới! Vẫn ngang nhiên đặt câu lệnh DML update ngay bên trong thân vòng lặp for (`update contacts[0]`), hệ thống sẽ crash Limit ngay lập tức khi xử lý danh sách trên 150 bản ghi.

**💡 Từ khóa ghi nhớ:** `Trigger Best Practice tối thượng -> Luôn nhận tham số dạng **`List`** + Tuyệt đối cấm tiệt đặt câu lệnh **DML (insert, update, delete) bên trong vòng lặp FOR**!`

---

## Câu 344

**🔵 What is an example of a polymorphic lookup field in Salesforce?**

- **A.** The WhatId field on the standard Event object ✅
- **B.** The ParentId field on the standard Account object ❌
- **C.** A custom field, Link__c, on the standard Contact object that looks up to an Account or a Campaign ❌
- **D.** The LeadId and ContactId fields on the standard Campaign Member object ❌

**📝 Dịch tiếng Việt:**
> Trường tra cứu nào dưới đây là một ví dụ điển hình về trường Lookup đa hình (Polymorphic Lookup field) trong Salesforce?

**💬 Giải thích gốc (English):**
> A polymorphic lookup field can reference multiple different object types. The WhatId field on the Event object is a classic example of this. It can reference either a Lead, Contact, Account, or Opportunity.

**✅ Tại sao đáp án đúng:**
> Chọn **A**. Một trường Lookup đa hình (**Polymorphic Lookup**) là trường cực kỳ linh hoạt, chỉ có một trường duy nhất nhưng lại có khả năng liên kết trỏ tới nhiều loại đối tượng (sObjects) khác nhau. Trường **`WhatId`** (đại diện cho trường "Related To") trên đối tượng tiêu chuẩn Task hoặc Event là ví dụ kinh điển: nó có thể trỏ tới Account, Opportunity, Campaign, Case... tùy ý!

**❌ Tại sao đáp án sai:**
> **B.** Trường `ParentId` trên Account chỉ hỗ trợ trỏ duy nhất tới một loại đối tượng duy nhất là Account cha, không hề có tính đa hình.
> **C.** Salesforce cấm không cho phép lập trình viên tự khởi tạo các trường Custom Lookup đa hình trỏ tới nhiều Object tùy chọn bừa bãi như thế này.
> **D.** Đây là hai trường Lookup tiêu chuẩn độc lập (`LeadId` trỏ tới Lead, `ContactId` trỏ tới Contact) chứ không phải là một trường duy nhất có tính đa hình.

**💡 Từ khóa ghi nhớ:** `Lookup đa hình (Polymorphic) -> Cứ nhớ bộ đôi huyền thoại: **`WhoId`** (trỏ tới People: Lead/Contact) và **`WhatId`** (trỏ tới Objects: Account/Opp/Case...)!`

---

## Câu 345

**🔵 Which three operations affect the number of times a trigger can fire? (Choose three.)**

- **A.** Lightning Flows ✅
- **B.** Roll-Up Summary fields ✅
- **C.** Criteria-based Sharing calculations ❌
- **D.** Workflow Rules ✅
- **E.** Email messages ❌

**📝 Dịch tiếng Việt:**
> Ba thao tác nào sau đây có khả năng ảnh hưởng trực tiếp và làm tăng số lần một Trigger có thể bị kích hoạt (re-fire) trong một giao dịch? (Chọn 3)

**💬 Giải thích gốc (English):**
> The three operations that affect the number of times a trigger can fire are:
> 1. Lightning Flows
> 2. Roll-Up Summary fields
> 3. Workflow Rules
> These operations can cause triggers to execute multiple times due to updates they perform on records.

**✅ Tại sao đáp án đúng:**
> Chọn **A**, **B** và **D**.
- **A**: **Lightning Flows** (Flow) khi thực hiện cập nhật bản ghi sẽ kích hoạt lại toàn bộ các trigger before/after update trên đối tượng đó.
- **B**: **Roll-Up Summary fields** khi tính toán dồn dữ liệu từ con lên cha sẽ tự động thực thi một tiến trình cập nhật bản ghi cha ngầm, từ đó kích hoạt trigger trên đối tượng cha.
- **D**: **Workflow Rules** (đặc biệt là Workflow Field Update) khi thay đổi giá trị trường sẽ ép Salesforce chạy lại quy trình lưu (Save Order of Execution) thêm một lượt, làm kích hoạt lại các Before/After Update Triggers.

**❌ Tại sao đáp án sai:**
> **C.** Criteria-based Sharing calculations chỉ là tiến trình chạy ngầm để tính toán quyền truy cập bản ghi của người dùng, hoàn toàn không thực hiện thao tác DML update dữ liệu nên không làm nổ trigger.
> **E.** Gửi email chỉ là một hành động gửi thông điệp đi kèm, không làm thay đổi hay cập nhật lại các trường dữ liệu trên bản ghi để kích hoạt lại trigger.

**💡 Từ khóa ghi nhớ:** `Bộ ba sát thủ gây nổ Trigger liên tục (re-fire) -> Luôn nhớ: **Workflow Rules**, **Lightning Flows** và **Roll-up Summary fields**!`

---

## Câu 346

**🔵 A Salesforce Administrator is creating a record-triggered now. When certain criteria are met, the now must call an Apex method to execute a complex validation involving several types of objects. When creating the Apex method, which annotation should a developer use to ensure the method can be used within the flow?**

- **A.** @RemoteAction ❌
- **B.** @future ❌
- **C.** @AuraEnabled ❌
- **D.** @InvocableMethod ✅

**📝 Dịch tiếng Việt:**
> Admin đang xây dựng một Record-triggered Flow. Khi thỏa mãn điều kiện, Flow cần gọi một phương thức Apex để thực hiện kiểm tra logic nghiệp vụ phức tạp liên quan đến nhiều đối tượng. Lập trình viên phải gắn annotation nào cho phương thức Apex để Flow có thể nhìn thấy và gọi được?

**💬 Giải thích gốc (English):**
> Invocable methods are called natively from Rest, Apex, Flow, or Einstein bot that interacts with the external API source. Invocable methods have dynamic input and output values and support describe calls.

**✅ Tại sao đáp án đúng:**
> Chọn **D**. Để một phương thức Apex có thể hiển thị dưới dạng một hộp hành động (Action) kéo thả trực quan và gọi được từ bên trong Flow Builder hoặc Process Builder, phương thức đó bắt buộc phải được gắn annotation **`@InvocableMethod`**.

**❌ Tại sao đáp án sai:**
> **A.** `@RemoteAction` dùng riêng cho các thư viện Javascript gọi hàm Apex trực tiếp từ trang Visualforce (JavaScript Remoting).
> **B.** `@future` dùng để định nghĩa các phương thức chạy bất đồng bộ (chạy ngầm dưới background), Flow không thể gọi trực tiếp và hứng kết quả phản hồi ngay được.
> **C.** `@AuraEnabled` dùng để kết nối và cho phép các component UI như LWC hoặc Aura Component gọi Apex.

**💡 Từ khóa ghi nhớ:** `Flow muốn gọi trực tiếp phương thức Apex -> Bắt buộc dùng **`@InvocableMethod`**!`

---

## Câu 347

**🔵 A developer is creating an app that contains multiple Lightning web components. One of the child components is used for navigation purposes. When a user clicks a button called Next in the child component, the parent component must be alerted so it can navigate to the next page. How should this be accomplished?**

- **A.** Create a custom event. ✅
- **B.** Call a method in the Apex controller. ❌
- **C.** Update a property on the parent. ❌
- **D.** Fire a notification. ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên đang xây dựng một ứng dụng chứa nhiều Lightning Web Components. Một component con được dùng để định hướng trang. Khi người dùng click nút 'Next' trên component con, component cha phải được thông báo để chuyển trang. Cách giải quyết chuẩn xác nhất là gì?

**💬 Giải thích gốc (English):**
> Custom events are used to communicate between Lightning web components, and can be used to pass data from a parent component to a child component. The parent component can fire a custom event and include the data as a parameter, which the child component can then access.

**✅ Tại sao đáp án đúng:**
> Chọn **A**. Đây là cơ chế giao tiếp ngược dòng kinh điển trong LWC (Child to Parent): **"Events up, Properties down"**. Khi người dùng click nút ở component con, con sẽ tạo và bắn ra một sự kiện tùy chỉnh (**`CustomEvent`**). Component cha ở bên ngoài sẽ đăng ký lắng nghe sự kiện này (ví dụ: `onnext={handleNext}`) để thực thi logic chuyển trang tương ứng, đảm bảo tính đóng gói tuyệt hảo.

**❌ Tại sao đáp án sai:**
> **B.** Apex controller chạy hoàn toàn dưới tầng cơ sở dữ liệu (server-side), không thể can thiệp điều khiển giao diện UI client-side của component cha được.
> **C.** Component con cấm tiệt và không thể trực tiếp gán đè hay thay đổi thuộc tính (property) của component cha để bảo vệ tính đóng gói dữ liệu của framework.
> **D.** Bắn ra thông báo (Fire notification) chỉ hiển thị một thông điệp toast nổi lên màn hình cho người dùng xem, chứ không giúp truyền dữ liệu điều khiển giữa hai component.

**💡 Từ khóa ghi nhớ:** `Giao tiếp ngược dòng từ Con lên Cha trong LWC -> Luôn bắn ra **`CustomEvent`** (Events Up)!`

---

## Câu 348

**🔵 How can a developer get all of the available record types for the current user on the Case object?**

- **A.** Use DescribeSObjectResult of the Case object. ✅
- **B.** Use SOQL to get all Cases. ❌
- **C.** Use DescribeFieldResult of the Case.RecordType field. ❌
- **D.** Use Case.getRecordTypes(). ❌

**📝 Dịch tiếng Việt:**
> Làm thế nào để lập trình viên lấy được toàn bộ danh sách các Record Types khả dụng đối với người dùng hiện tại trên đối tượng Case?

**💬 Giải thích gốc (English):**
> Here's the example code:
> Schema.DescribeSObjectResult rt = case.SObjectType.getDescribe();
> List<Schema.RecordTypeInfo> rti = R.getRecordTypeInfos();

**✅ Tại sao đáp án đúng:**
> Chọn **A**. Để truy xuất metadata động của một đối tượng nhằm xác định các Record Type nào được phép hiển thị cho user hiện tại, lập trình viên sử dụng phương thức Describe của sObject: gọi `Schema.sObjectType.Case.getDescribe()` để lấy đối tượng **`DescribeSObjectResult`**, sau đó gọi tiếp `.getRecordTypeInfos()`..

**❌ Tại sao đáp án sai:**
> **B.** Sử dụng SOQL để truy vấn tất cả Case chỉ trả về danh sách các bản ghi dữ liệu Case vật lý hiện có trong database, hoàn toàn bất lực trong việc lấy thông tin cấu hình Record Types khả dụng.
> **C.** DescribeFieldResult của trường `RecordType` chỉ trả về thông tin mô tả kỹ thuật của bản thân trường đó chứ không chứa danh sách các tùy chọn Record Type thực tế của đối tượng Case.
> **D.** Không hề tồn tại phương thức nào tên là `getRecordTypes()` trực tiếp trên lớp đối tượng `Case` trong Apex.

**💡 Từ khóa ghi nhớ:** `Truy xuất danh sách Record Types khả dụng của user -> Dùng **`DescribeSObjectResult`** (qua hàm `getDescribe().getRecordTypeInfos()`)!`

---

## Câu 349

**🔵 What are three characteristics of static methods? (Choose three.)**

- **A.** Initialized only when a class is loaded ✅
- **B.** A static variable outside of the scope of an Apex transaction ❌
- **C.** Allowed only in outer classes ✅
- **D.** Allowed only in inner classes ❌
- **E.** Excluded from the view state for a Visualforce page ✅

**📝 Dịch tiếng Việt:**
> Ba đặc trưng nổi bật của các phương thức tĩnh (static methods) trong ngôn ngữ Apex của Salesforce là gì? (Chọn 3)

**💬 Giải thích gốc (English):**
> Static methods, variables, and initialization code have these characteristics.
> They’re associated with a class.
> They’re allowed only in outer classes.
> They’re initialized only when a class is loaded.
> They aren’t transmitted as part of the view state for a Visualforce page.

**✅ Tại sao đáp án đúng:**
> Chọn **A**, **C** và **E**.
- **A**: Các phương thức tĩnh chỉ được khởi tạo đúng **1 lần duy nhất** khi lớp (class) chứa nó được nạp vào bộ nhớ.
- **C**: Salesforce chỉ cho phép khai báo phương thức/biến tĩnh bên trong các lớp cha ngoài cùng (**outer classes**), cấm tiệt khai báo static trong các inner classes.
- **E**: Các phương thức tĩnh và biến tĩnh hoàn toàn được **loại trừ (excluded) khỏi View State** của trang Visualforce. Đây là một mẹo cực hay giúp lập trình viên tối ưu hóa dung lượng truyền tải dữ liệu của trang Visualforce, tránh lỗi đụng trần View State 135KB.

**❌ Tại sao đáp án sai:**
> **B.** Sai lầm nghiêm trọng! Biến tĩnh static trong Apex chỉ tồn tại trong phạm vi của một giao dịch đơn lẻ (**single Apex Transaction**), chứ không thể sống dai vượt ra ngoài phạm vi transaction để dùng chung cho các transaction khác được.
> **D.** Ngược lại hoàn toàn với câu C, static methods bị cấm khai báo bên trong các inner classes.

**💡 Từ khóa ghi nhớ:** `Đặc tính static trong Apex -> **Chỉ khởi tạo khi load class** + **Chỉ có ở Outer class** + **Loại trừ khỏi Visualforce View State**!`

---
