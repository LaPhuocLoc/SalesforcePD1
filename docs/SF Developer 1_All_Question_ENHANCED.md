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
> Hai thành phần nào sau đây có thể triển khai (deploy) bằng Metadata API? (Chọn hai.)

**💬 Giải thích gốc (English):**
> Web-to-Case and Web-to-Lead option are not available Metadata API​​​​​​​

**✅ Tại sao đáp án đúng:**
> Lead Conversion Settings và Case Settings là các cài đặt cấu hình hệ thống (Settings) được hỗ trợ đầy đủ bởi Metadata API để deploy giữa các môi trường.

**❌ Tại sao đáp án sai:**
> **B.** Web-to-Case là tính năng tạo Case từ Web, cấu hình này không được Metadata API hỗ trợ trực tiếp để deploy.
> **C.** Web-to-Lead là tính năng tạo Lead từ Web, cũng không nằm trong danh sách các component deploy được qua Metadata API.

**💡 Từ khóa ghi nhớ:** `Settings (Lead Conversion, Case Settings) deploy được bằng Metadata API; Web-to-Lead/Case thì KHÔNG.`

---

## Câu 2

**🔵 A developer created a custom order management app that uses an Apex class. The order is represented by an Order object and an OrderItem object that has a master-detail relationship to Order. During order processing, an order may be split into multiple orders. What should a developer do to allow their code to move some existing OrderItem records to a new Order record?**

- **A.** Select the Allow reparenting option on the master-detail relationship. ✅
- **B.** Change the master-detail relationship to an external lookup relationship. ❌
- **C.** Add without sharing to the Apex class declaration. ❌
- **D.** Create a junction object between OrderItem and Order. ❌

**📝 Dịch tiếng Việt:**
> Một nhà phát triển đã tạo một ứng dụng quản lý đơn hàng tùy chỉnh sử dụng Apex class. Đơn hàng được đại diện bởi object Order và object OrderItem có mối quan hệ master-detail với Order. Trong quá trình xử lý, một đơn hàng có thể bị chia thành nhiều đơn hàng. Nhà phát triển nên làm gì để cho phép code của họ chuyển một số record OrderItem hiện có sang một record Order mới?

**💬 Giải thích gốc (English):**
> "Allow reparenting" the developer enables the ability to change the parent of a child record (OrderItem) from one master record (Order) to another. This allows the developer to move certain OrderItem records to a new Order record, effectively splitting the order into multiple orders.

**✅ Tại sao đáp án đúng:**
> Chọn tùy chọn 'Allow reparenting' trên mối quan hệ master-detail cho phép thay đổi bản ghi cha (Order) của bản ghi con (OrderItem), giúp chuyển các OrderItem sang Order mới một cách hợp lệ.

**❌ Tại sao đáp án sai:**
> **B.** Chuyển master-detail thành external lookup relationship là không cần thiết và làm mất đi các tính năng của master-detail như cascade delete hay roll-up summary.
> **C.** Thêm 'without sharing' chỉ bỏ qua luật chia sẻ record (sharing rules), không giải quyết được giới hạn reparenting của master-detail.
> **D.** Tạo junction object giữa OrderItem và Order là sai thiết kế và làm phức tạp hóa mô hình dữ liệu không cần thiết.

**💡 Từ khóa ghi nhớ:** `Muốn đổi cha (reparent) trong quan hệ Master-Detail thì phải tích chọn 'Allow reparenting'.`

---

## Câu 3

**🔵 A developer is implementing an Apex class for a financial system. Within the class, the variables 'creditAmount' and 'debitAmount' should not be able to change once a value is assigned. In which two ways can the developer declare the variables to ensure their value can only be assigned one time? (Choose two.)**

- **A.** Use the static keyword and assign its value in a static initializer. ❌
- **B.** Use the final keyword and assign its value when declaring the variable. ✅
- **C.** Use the final keyword and assign its value in the class constructor. ✅
- **D.** Use the static keyword and assign its value in the class constructor. ❌

**📝 Dịch tiếng Việt:**
> Trong một class Apex, làm sao để đảm bảo các biến 'creditAmount' và 'debitAmount' chỉ được gán giá trị một lần duy nhất? (Chọn 2)

**💬 Giải thích gốc (English):**
> The variables 'creditAmount' and 'debitAmount' can only be assigned one time, the developer should use the 'final' keyword and assign their values when declaring the variables. This will make the variables constant and their values cannot be changed after assignment.

**✅ Tại sao đáp án đúng:**
> Từ khóa 'final' trong Apex dùng để tạo hằng số cho instance. Mày có thể gán giá trị ngay lúc khai báo (A) hoặc gán duy nhất 1 lần trong Constructor (B). Sau đó đố ai sửa được.

**❌ Tại sao đáp án sai:**
> **C.** Static đơn thuần chỉ là biến dùng chung, vẫn sửa giá trị bình thường.
> **D.** Static initializer gán giá trị cho biến static, nhưng nếu không có 'final' thì vẫn bị ghi đè sau đó.

**💡 Từ khóa ghi nhớ:** `Assign only once = FINAL. Nhớ nhé mày!`

---

## Câu 4

**🔵 Which three web technologies can be integrated into a Visualforce page? (Choose three.)**

- **A.** JavaScript ✅
- **B.** CSS ✅
- **C.** Java ❌
- **D.** PHP ❌
- **E.** HTML ✅

**📝 Dịch tiếng Việt:**
> Ba công nghệ web nào sau đây có thể được tích hợp vào một trang Visualforce? (Chọn ba.)

**💬 Giải thích gốc (English):**
> You can't write any Java/Php code in VF page.
> https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/pages_intro_what_is_it.htm

**✅ Tại sao đáp án đúng:**
> Visualforce là công nghệ render ở phía client-side, do đó nó hỗ trợ hoàn toàn các công nghệ web cơ bản như HTML để tạo cấu trúc, CSS để tạo kiểu dáng và JavaScript để xử lý logic tương tác.

**❌ Tại sao đáp án sai:**
> **C.** Java là ngôn ngữ chạy phía server-side và không thể chạy trực tiếp trong Visualforce page.
> **D.** PHP cũng là ngôn ngữ server-side và không tích hợp trực tiếp được vào Visualforce page chạy trên nền tảng Force.com.

**💡 Từ khóa ghi nhớ:** `Visualforce chỉ tích hợp công nghệ frontend (HTML, CSS, JS); KHÔNG chơi với Java và PHP.`

---

## Câu 5

**🔵 Which is a valid Apex assignment?**

- **A.** Integer x=5*1.0; ❌
- **B.** Integer x =5.0; ❌
- **C.** Double x =5; ✅
- **D.** Float x =5.0; ❌

**📝 Dịch tiếng Việt:**
> Phép gán Apex nào sau đây là hợp lệ?

**💬 Giải thích gốc (English):**
> An Integer can be assigned to a Double, but a Double cannot be directly assigned to an Integer.

**✅ Tại sao đáp án đúng:**
> Apex hỗ trợ ngầm định chuyển đổi kiểu dữ liệu từ Integer sang Double (Double x = 5), vì Double có độ rộng dữ liệu lớn hơn Integer.

**❌ Tại sao đáp án sai:**
> **A.** Phép nhân 5 * 1.0 trả về kết quả kiểu Double, không thể gán trực tiếp cho biến kiểu Integer mà không có ép kiểu (cast).
> **B.** 5.0 là giá trị kiểu Double, không thể gán trực tiếp cho biến kiểu Integer.
> **D.** Apex không có kiểu dữ liệu nguyên bản là Float, chỉ có Decimal hoặc Double.

**💡 Từ khóa ghi nhớ:** `Integer gán cho Double được (tự động ép kiểu lên), Double gán cho Integer thì BỊ LỖI.`

---

## Câu 6

**🔵 A developer completed modifications to a customized feature that is comprised of two elements: 1. Apex trigger 2. Trigger handler Apex class. What are two factors that the developer must take into account to properly deploy the modification to the production environment? (Choose two.)**

- **A.** Apex classes must have at least 75% code coverage org-wide. ✅
- **B.** At least one line of code must be executed for the Apex trigger. ✅
- **C.** All methods in the test classes must use @isTest. ❌
- **D.** Test methods must be declared with the testMethod keyword. ❌

**📝 Dịch tiếng Việt:**
> Một nhà phát triển đã hoàn thành các sửa đổi cho một tính năng tùy chỉnh gồm hai phần: 1. Apex trigger, 2. Trigger handler Apex class. Có hai yếu tố nào mà nhà phát triển phải lưu ý để deploy thành công sửa đổi này lên môi trường production? (Chọn hai.)

**💬 Giải thích gốc (English):**
> To deploy your code to production environments, it is mandatory to achieve a minimum of 75% code coverage for your Apex through unit tests. Additionally, all triggers must have at least one line of test coverage.

**✅ Tại sao đáp án đúng:**
> Khi deploy lên production, Salesforce yêu cầu tổng độ bao phủ code (code coverage) của toàn bộ Apex class trong org phải đạt ít nhất 75%, và mọi Apex trigger phải có ít nhất 1 dòng code được chạy qua kiểm thử.

**❌ Tại sao đáp án sai:**
> **C.** Không phải tất cả các method trong test class đều phải dùng @isTest. Chỉ cần bản thân class và các method test được đánh dấu đúng.
> **D.** Từ khóa testMethod đã bị deprecated và không còn bắt buộc, khuyến nghị dùng annotation @isTest thay thế.

**💡 Từ khóa ghi nhớ:** `Deploy lên Production: Code coverage org-wide >= 75% và Trigger phải chạy qua ít nhất 1 dòng test.`

---

## Câu 7

**🔵 How many levels of child records can be returned in a single SOQL query from one parent object?**

- **A.** 1 ❌
- **B.** 3 ❌
- **C.** 5 ✅
- **D.** 7 ❌

**📝 Dịch tiếng Việt:**
> Một SOQL query từ một parent object có thể trả về tối đa bao nhiêu cấp độ của child record?

**💬 Giải thích gốc (English):**
> Query Five Levels of Parent-to-Child Relationships in SOQL Queries
> https://help.salesforce.com/s/articleView?id=release-notes.rn_api_soql_5level.htm&release=244&type=5

**✅ Tại sao đáp án đúng:**
> Salesforce cho phép một SOQL query truy vấn tối đa 5 cấp độ mối quan hệ từ parent đến child. Giới hạn này đã được tăng lên từ 3 cấp độ trước đây để hỗ trợ việc truy xuất dữ liệu phức tạp hơn trong một truy vấn duy nhất. Đây là một governor limit quan trọng cần nhớ khi thiết kế các truy vấn SOQL.

**❌ Tại sao đáp án sai:**
> **A.** 1 cấp độ là quá hạn chế; SOQL được thiết kế để truy vấn các mối quan hệ phức tạp hơn giữa các object.
> **B.** 3 cấp độ từng là giới hạn trước đây của SOQL cho các mối quan hệ parent-to-child, nhưng nó đã được tăng lên và không còn là giới hạn hiện tại.
> **D.** 7 cấp độ vượt quá giới hạn governor limit hiện tại mà Salesforce đặt ra cho các truy vấn SOQL parent-to-child.

**💡 Từ khóa ghi nhớ:** `SOQL parent-to-child: tối đa 5 cấp độ. Đây là một governor limit quan trọng trong Salesforce.`

---

## Câu 8

**🔵 When an Account's custom picklist field called Customer Sentiment is changed to a value of 'Confused', a new related Case should automatically be created. Which two methods should a developer use to create this case? (Choose two.)**

- **A.** Process Builder ✅
- **B.** Apex Trigger ✅
- **C.** Custom Button ❌
- **D.** Workflow Rule ❌

**📝 Dịch tiếng Việt:**
> Khi trường picklist tùy chỉnh Customer Sentiment trên một Account được thay đổi thành giá trị 'Confused', một Case liên quan mới phải được tự động tạo. Hai phương pháp nào sau đây nhà phát triển nên sử dụng để tạo Case này? (Chọn hai.)

**💬 Giải thích gốc (English):**
> 1. Apex Trigger: The developer can write an Apex trigger on the Account object to detect changes in the Customer Sentiment picklist field. When the picklist field value changes to 'Confused,' the trigger can create a new Case record and establish the necessary relationship between the Account and the Case.
> 2. Process Builder: The developer can use Process Builder, a declarative automation tool in Salesforce, to create the automation flow. The process builder can be configured to monitor changes on the Account object and specifically check for the Customer Sentiment picklist field value change to 'Confused.' When the condition is met, the process builder can take action to create a new related Case record.

**✅ Tại sao đáp án đúng:**
> Process Builder là một công cụ tự động hóa declarative mạnh mẽ, có thể được kích hoạt bởi các thay đổi trên record (như cập nhật trường picklist) và thực hiện các hành động như tạo record mới (Case). Apex Trigger là một giải pháp programmatic, cho phép nhà phát triển viết code để lắng nghe các sự kiện trên Account (như cập nhật trường Customer Sentiment) và tự động tạo một Case mới khi điều kiện được đáp ứng.

**❌ Tại sao đáp án sai:**
> **C.** Custom Button yêu cầu người dùng phải click vào để kích hoạt hành động, trong khi yêu cầu là Case phải được 'tự động' tạo.
> **D.** Workflow Rule không có khả năng tạo record mới. Nó chỉ có thể tạo task, cập nhật trường, gửi email alert hoặc gửi outbound message.

**💡 Từ khóa ghi nhớ:** `Để tự động tạo record mới khi một trường thay đổi, hãy nghĩ đến Process Builder (declarative) hoặc Apex Trigger (programmatic).`

---

## Câu 9

**🔵 Which statement results in an Apex compiler error?**

- **A.** Map<Id, Lead> lmap = new Map<Id, Lead>([Select ID from Lead Limit 8]); ❌
- **B.** Date d1 = Date.Today(), d2 = Date.ValueOf('2018-01-01'); ❌
- **C.** Integer a=5, b=6, c, d = 7; ❌
- **D.** List<string> s = List<string>{'a','b','c'}; ✅

**📝 Dịch tiếng Việt:**
> Câu lệnh nào sau đây gây ra lỗi trình biên dịch Apex?

**💬 Giải thích gốc (English):**
> D is not correct because of the missing new operator
> List<string> s = new List<string>{'a','b','c'};

**✅ Tại sao đáp án đúng:**
> Câu lệnh `List<string> s = List<string>{'a','b','c'};` thiếu từ khóa `new` khi khởi tạo một List bằng cú pháp collection literal. Trong Apex, mọi khởi tạo collection (List, Set, Map) đều yêu cầu từ khóa `new`. Việc thiếu `new` sẽ dẫn đến lỗi trình biên dịch.

**❌ Tại sao đáp án sai:**
> **A.** Câu lệnh này hợp lệ. Khi khởi tạo một Map bằng kết quả SOQL, Apex sẽ tự động sử dụng Id làm key và sObject làm value. Ngay cả khi SOQL chỉ chọn ID, Apex vẫn sẽ lấy toàn bộ bản ghi Lead và tạo Map đúng cách.
> **B.** Đây là cách khai báo và khởi tạo nhiều biến cùng kiểu (`Date`) trên một dòng hợp lệ trong Apex. Các phương thức `Date.Today()` và `Date.ValueOf()` đều đúng cú pháp.
> **C.** Đây là cách khai báo và khởi tạo nhiều biến cùng kiểu (`Integer`) trên một dòng hợp lệ. Biến `c` được khai báo nhưng không khởi tạo là hoàn toàn chấp nhận được trong Apex.

**💡 Từ khóa ghi nhớ:** `Luôn nhớ từ khóa `new` khi khởi tạo bất kỳ collection nào (List, Set, Map) trong Apex, kể cả với cú pháp collection literal.`

---

## Câu 10

**🔵 A developer has a Visualforce page and custom controller to save Account records. The developer wants to display any validation rule violations to the user. How can the developer make sure that validation rule violations are displayed?**

- **A.** Add custom controller attributes to display the message. ❌
- **B.** Use a try/catch with a custom exception class. ❌
- **C.** Include<apex:messages>on the Visualforce page. ✅
- **D.** Perform the DML using the Database.upsert() method. ❌

**📝 Dịch tiếng Việt:**
> Một developer có một Visualforce page và custom controller để lưu các bản ghi Account. Developer muốn hiển thị bất kỳ vi phạm validation rule nào cho người dùng. Làm thế nào developer có thể đảm bảo rằng các vi phạm validation rule được hiển thị?

**💬 Giải thích gốc (English):**
> Display Errors on the Visualforce Page: In the Visualforce page, utilize the Visualforce markup and Apex expressions to iterate over the error messages collection and display them to the user. This can be achieved using components like <apex:pageMessages> or by manually rendering error messages using <apex:outputPanel> and <apex:repeat>.

**✅ Tại sao đáp án đúng:**
> Khi một DML operation trong Apex controller gặp lỗi validation rule, Salesforce sẽ tự động thêm các thông báo lỗi này vào ApexPages.Message list. Component <apex:messages> (hoặc <apex:pageMessages>) trên Visualforce page được thiết kế để tự động hiển thị tất cả các thông báo lỗi này, bao gồm cả lỗi validation rule, mà không cần code xử lý lỗi tường minh trong controller.

**❌ Tại sao đáp án sai:**
> **A.** Việc thêm các custom controller attributes để hiển thị thông báo sẽ yêu cầu developer phải tự parse lỗi DML và gán chúng, đây là một cách tiếp cận phức tạp và không cần thiết khi Visualforce đã có sẵn cơ chế chuẩn.
> **B.** Sử dụng try/catch là tốt để bắt DMLExceptions, nhưng việc dùng custom exception class là không cần thiết cho việc hiển thị lỗi validation rule tiêu chuẩn. Các lỗi này đã được Salesforce xử lý và đưa vào ApexPages để hiển thị.
> **D.** Database.upsert() là một phương thức DML, nhưng nó không thay đổi cách thức hiển thị các vi phạm validation rule. Bất kể phương thức DML nào (insert, update, upsert), lỗi validation rule vẫn sẽ được xử lý và hiển thị qua <apex:messages>.

**💡 Từ khóa ghi nhớ:** `Visualforce: <apex:messages> tự động hiển thị validation rule errors và DML errors từ controller mà không cần code xử lý lỗi phức tạp.`

---

## Câu 11

**🔵 A developer encounters APEX heap limit errors in a trigger. Which two methods should the developer use to avoid this error? (Choose two.)**

- **A.** Use the transient keyword when declaring variables. ❌
- **B.** Query and store fields from the related object in a collection when updating related objects. ❌
- **C.** Remove or set collections to null after use. ✅
- **D.** Use SOQL for loops instead of assigning large queries results to a single collection and looping through the collection. ✅

**📝 Dịch tiếng Việt:**
> Một developer gặp lỗi APEX heap limit trong một trigger. Hai phương pháp nào sau đây developer nên sử dụng để tránh lỗi này? (Chọn hai.)

**💬 Giải thích gốc (English):**
> Use the transient keyword to declare instance variables that can't be saved, and shouldn't be transmitted as part of the view state for a Visualforce page -> For VF 'heap' limit.
> Reduce heap size during runtime by removing items from the collection as you iterate over it.
> To avoid heap size limits, developers should always use a SOQL "for" loop to process query results that return many records.

**✅ Tại sao đáp án đúng:**
> Để tránh lỗi APEX heap limit, việc giải phóng bộ nhớ không còn sử dụng là rất quan trọng. Xóa hoặc đặt các collection thành null sau khi dùng cho phép garbage collector thu hồi bộ nhớ, giảm kích thước heap. Ngoài ra, sử dụng SOQL for loops giúp xử lý kết quả truy vấn theo từng batch nhỏ, thay vì tải tất cả dữ liệu vào bộ nhớ cùng lúc, từ đó giảm đáng kể mức tiêu thụ heap.

**❌ Tại sao đáp án sai:**
> **A.** Từ khóa transient được sử dụng chủ yếu trong Visualforce để ngăn biến được lưu vào view state, không trực tiếp giải quyết lỗi APEX heap limit trong trigger.
> **B.** Việc query và lưu trữ các trường từ related object vào một collection thực tế sẽ làm tăng mức sử dụng heap, đặc biệt nếu có nhiều bản ghi hoặc nhiều trường, và có thể gây ra lỗi heap limit thay vì tránh nó.

**💡 Từ khóa ghi nhớ:** `Tránh APEX heap limit: dùng SOQL for loops, giải phóng collection sau dùng. Transient cho Visualforce view state.`

---

## Câu 12

**🔵 Which two are phases in the Salesforce Application Event propagation framework? (Choose two.)**

- **A.** Bubble ✅
- **B.** Default ✅
- **C.** Control ❌
- **D.** Emit ❌

**📝 Dịch tiếng Việt:**
> Hai giai đoạn nào nằm trong khung lan truyền Aura Application Event của Salesforce? (Chọn 2)

**💬 Giải thích gốc (English):**
> Here is the sequence of application event propagation.
> 1. Event fired—An application event is fired. The component that fires the event is known as the source component.
> 2. Capture phase—The framework executes the capture phase from the application root to the source component until all components are traversed. Any handling event can stop propagation by calling stopPropagation() on the event.
> 3. Bubble phase—The framework executes the bubble phase from the source component to the application root until all components are traversed or stopPropagation() is called.
> 4. Default phase—The framework executes the default phase from the root node unless preventDefault() was called in the capture or bubble phases. If the event’s propagation wasn’t stopped in a previous phase, the root node defaults to the application root. If the event’s propagation was stopped in a previous phase, the root node is set to the component whose handler invoked event.stopPropagation().

**✅ Tại sao đáp án đúng:**
> Application Event trong Aura có 3 phase: Capture, Bubble (lan tỏa từ con lên cha) và Default (chạy các handler đã đăng ký). Trong đáp án này, A và C là đúng quy chuẩn.

**❌ Tại sao đáp án sai:**
> **B.** Emit là thuật ngữ thường dùng trong các JS Framework khác như Vue, Aura không sử dụng phase này.
> **D.** Control không phải là một giai đoạn trong vòng đời lan truyền event của Aura.

**💡 Từ khóa ghi nhớ:** `Aura Event Phases: Capture -> Bubble -> Default.`

---

## Câu 13

**🔵 A custom object Trainer__c has a lookup field to another custom object Gym__c. Which SOQL query will get the record for the Viridian City Gym and all its trainers?**

- **A.** SELECT ID FROM Trainer__c WHERE Gym__r.Name = 'Viridian City Gym' ❌
- **B.** SELECT Id, (SELECT Id FROM Trainers__c) FROM Gym__c WHERE Name = 'Viridian City Gym' ❌
- **C.** SELECT Id, (SELECT Id FROM Trainer__c) FROM Gym__c WHERE Name = 'Viridian City Gym' ❌
- **D.** SELECT Id, (SELECT Id FROM Trainers__r) FROM Gym__c WHERE Name = 'Viridian City Gym' ✅

**📝 Dịch tiếng Việt:**
> Câu query SOQL nào lấy được bản ghi Gym và tất cả các Trainer liên quan của nó?

**✅ Tại sao đáp án đúng:**
> Đây là 'Parent-to-Child' query. Khi truy vấn từ cha xuống con của Custom Object, mày phải dùng Child Relationship Name kèm hậu tố __r. Ở đây là (SELECT Id FROM Trainers__r).

**❌ Tại sao đáp án sai:**
> **B.** Dùng __c là tên object, trong sub-query bắt buộc phải dùng tên quan hệ (Relationship Name).
> **C.** Gym__r là sai, Gym là cha thì phải dùng Gym__c. Ngoài ra sub-query phải nằm trong ngoặc.
> **D.** Câu này là Child-to-Parent query, nó chỉ lấy Trainer chứ không lấy theo kiểu 'Gym và các Trainer của nó'.

**💡 Từ khóa ghi nhớ:** `Query Cha xuống Con: Dùng Relationship Name + __r.`

---

## Câu 14

**🔵 A developer needs to create an audit trail for records that are sent to the recycle bin. Which type of trigger is most appropriate to create?**

- **A.** after delete ✅
- **B.** after undelete ❌
- **C.** before undelete ❌
- **D.** before delete ❌

**📝 Dịch tiếng Việt:**
> Một nhà phát triển cần tạo một audit trail cho các record được gửi vào recycle bin. Loại trigger nào phù hợp nhất để tạo?

**✅ Tại sao đáp án đúng:**
> Trigger 'after delete' được kích hoạt sau khi một record đã được xóa và chuyển vào recycle bin. Tại thời điểm này, bạn có thể truy cập các giá trị của record đã bị xóa để ghi lại thông tin vào audit trail, đảm bảo rằng việc xóa đã thực sự xảy ra. Đây là thời điểm lý tưởng để ghi nhận sự kiện xóa.

**❌ Tại sao đáp án sai:**
> **B.** Trigger 'after undelete' được kích hoạt sau khi một record được khôi phục từ recycle bin, không phải khi nó được gửi vào đó.
> **C.** Trigger 'before undelete' được kích hoạt trước khi một record được khôi phục từ recycle bin, không liên quan đến việc xóa record.
> **D.** Trigger 'before delete' được kích hoạt trước khi record bị xóa. Mặc dù nó có thể ghi lại thông tin, nhưng 'after delete' đảm bảo rằng hành động xóa đã hoàn tất, phù hợp hơn cho một audit trail về sự kiện xóa.

**💡 Từ khóa ghi nhớ:** `Để tạo audit trail cho record bị xóa (gửi vào recycle bin), hãy dùng 'after delete' trigger vì nó xác nhận hành động xóa đã xảy ra.`

---

## Câu 15

**🔵 Where are two locations a developer can look to find information about the status of asynchronous or future calls? (Choose two.)**

- **A.** Time-Based Workflow Monitor ❌
- **B.** Apex Flex Queue ✅
- **C.** Apex Jobs ✅
- **D.** Paused Flow Interviews component ❌

**📝 Dịch tiếng Việt:**
> Hai vị trí nào mà lập trình viên có thể tìm thấy thông tin về trạng thái của các phương thức batch hoặc future?

**💬 Giải thích gốc (English):**
> AsyncApexJob Object: The AsyncApexJob object represents the status of asynchronous Apex jobs, which include future calls, batch Apex jobs, and scheduled Apex jobs.
> Apex Flex Queue is where a developer can find information about the status of asynchronous or future calls in Salesforce. The Apex Flex Queue is a mechanism introduced to manage the execution of asynchronous Apex jobs when there is a large backlog.

**✅ Tại sao đáp án đúng:**
> D: Apex Jobs hiển thị mọi tác vụ không đồng bộ. C: Apex Flex Queue hiển thị các Batch job đang nằm chờ trước khi xử lý.

**❌ Tại sao đáp án sai:**
> **A.** Paused Flow Interviews chỉ hiển thị các luồng Flow đang bị tạm dừng, không liên quan đến Batch hay Future Apex.
> **B.** Time-Based Workflow Monitor chỉ dùng để theo dõi các Workflow Rule có cài đặt thời gian thực hiện (Time-dependent actions).

**💡 Từ khóa ghi nhớ:** `Keyword: Monitor Async Apex -> Apex Jobs & Flex Queue.`

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
> Cho đoạn mã dưới đây:
```apex
public class AccountListController {
public List<Account> getAccounts() {
return controller.getRecords();
}
}
```
Ba câu lệnh nào có thể được sử dụng để tạo biến `controller`? (Chọn ba.)

**💬 Giải thích gốc (English):**
> The StandardController has getRecord() not getRecords().

**✅ Tại sao đáp án đúng:**
> Phương thức `getRecords()` chỉ có sẵn trên `ApexPages.StandardSetController`, không phải `ApexPages.StandardController`. Do đó, biến `controller` phải là một instance của `StandardSetController`. `StandardSetController` có thể được khởi tạo với một `List<SObject>` (như kết quả của `Database.query()`) hoặc một `Database.QueryLocator` (như kết quả của `Database.getQueryLocator()`).

**❌ Tại sao đáp án sai:**
> **C.** `ApexPages.StandardController` không có phương thức `getRecords()`, mà chỉ có `getRecord()`. Ngoài ra, constructor của `StandardController` mong đợi một SObject duy nhất, không phải `Database.QueryLocator`.
> **D.** `ApexPages.StandardController` không có phương thức `getRecords()`. Constructor của `StandardController` mong đợi một SObject duy nhất, trong khi `[SELECT Id FROM Account]` trả về một `List<Account>`.

**💡 Từ khóa ghi nhớ:** `Nhớ `getRecords()` cho `StandardSetController` và `getRecord()` cho `StandardController`. `StandardSetController` chấp nhận `List<SObject>` hoặc `QueryLocator`.`

---

## Câu 17

**🔵 Given: Map<ID, Account> accountMap = new Map<ID, Account> ([SELECT Id, Name FROM Account]); What are three valid Apex loop structures for iterating through items in the collection? (Choose three.)**

- **A.** for (ID accountID : accountMap.keySet()) { } ❌
- **B.** for (Account accountRecord : accountMap.values()) { } ✅
- **C.** for (Integer i = 0; i < accountMap.size(); i++) { } ✅
- **D.** for (ID accountID : accountMap) { } ❌
- **E.** for (Account accountRecord : accountMap.keySet()) { } ❌

**📝 Dịch tiếng Việt:**
> Cho khai báo: Map<ID, Account> accountMap = new Map<ID, Account> ([SELECT Id, Name FROM Account]); Ba cấu trúc vòng lặp Apex nào sau đây là hợp lệ để duyệt qua các phần tử trong collection này? (Chọn 3)

**💬 Giải thích gốc (English):**
> Problem:
> D: Loop must iterate over collection: Map<Id,Account>
> E: Invalid loop variable type expected Id was Account.

**✅ Tại sao đáp án đúng:**
> A: keySet() trả về Set<ID>, nên duyệt bằng biến kiểu ID là chuẩn. B: values() trả về List<Account>, duyệt bằng biến kiểu Account là quá đẹp. C: Vòng lặp for truyền thống dùng chỉ số chạy từ 0 đến size() của map hoàn toàn hợp lệ về mặt cú pháp.

**❌ Tại sao đáp án sai:**
> **D.** Apex cấm duyệt trực tiếp trên đối tượng Map (accountMap) như một collection. Mày phải gọi keySet() hoặc values().
> **E.** keySet() trả về Set<ID>, nhưng biến chạy lại khai báo kiểu Account thì compiler nó đập vào mặt ngay lập tức.

**💡 Từ khóa ghi nhớ:** `Duyệt Map: keySet() cho ID, values() cho sObject. Tuyệt đối không duyệt trực tiếp Map!`

---

## Câu 18

**🔵 What is the order of operations when a record is saved in Salesforce?**

- **A.** workflow, process flows, triggers, commit ❌
- **B.** process flows, triggers, workflow, commit ❌
- **C.** triggers, workflow, process flows, commit ✅
- **D.** workflow, triggers, process flows, commit ❌

**📝 Dịch tiếng Việt:**
> Thứ tự các thao tác khi một record được lưu trong Salesforce là gì?

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
> Khi một record được lưu, Salesforce tuân theo một thứ tự thực thi cụ thể. Triggers (cả before và after) chạy trước tiên để xử lý logic cấp thấp. Sau đó, các Workflow Rules được thực thi, tiếp theo là Process Builders hoặc Flows (được gọi chung là 'process flows' trong các tùy chọn). Cuối cùng, các thay đổi được commit vào database.

**❌ Tại sao đáp án sai:**
> **A.** Workflow Rules và Process Flows luôn chạy SAU Triggers trong thứ tự thực thi khi một record được lưu.
> **B.** Process Flows và Workflow Rules luôn chạy SAU Triggers trong thứ tự thực thi khi một record được lưu.
> **D.** Workflow Rules luôn chạy SAU Triggers trong thứ tự thực thi khi một record được lưu.

**💡 Từ khóa ghi nhớ:** `Thứ tự thực thi cơ bản: Triggers -> Workflow Rules -> Process Flows (Flow/Process Builder) -> Commit.`

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
> Formula fields rất linh hoạt, cho phép tạo các liên kết động đến record (sử dụng hàm HYPERLINK), thực hiện các phép so sánh ngày giờ sử dụng hàm NOW() để kiểm tra thời gian đã qua, và hiển thị nội dung có điều kiện như văn bản hoặc hình ảnh (kết hợp hàm IF và IMAGE).

**❌ Tại sao đáp án sai:**
> **B.** Hàm PRIORVALUE() được sử dụng trong validation rules, Workflow Rules, Process Builder hoặc Flow để so sánh giá trị hiện tại với giá trị trước đó, không phải để hiển thị giá trị trước đó trực tiếp trong formula field.
> **D.** Formula fields trong Salesforce không hỗ trợ hàm VLOOKUP() như trong Excel. Để truy xuất giá trị từ các object liên quan, bạn sử dụng dot notation (ví dụ: `RelatedObject__r.FieldName__c`).

**💡 Từ khóa ghi nhớ:** `Formula fields: HYPERLINK, NOW, IF/IMAGE. Không PRIORVALUE (chỉ validation/workflow/flow), không VLOOKUP (dùng dot notation).`

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
> Hai cách cập nhật phương thức để ngăn chặn cuộc tấn công SOQL Injection? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> A: Variable Binding (:var) trong Static SOQL là cách an toàn nhất. B: escapeSingleQuotes() giúp vô hiệu hóa các ký tự điều khiển trong Dynamic SOQL.

**❌ Tại sao đáp án sai:**
> **C.** Dùng regex tự viết rất dễ sai sót và không bao quát được mọi kiểu tấn công như hàm chuẩn của Salesforce.
> **D.** @ReadOnly và with sharing liên quan đến hiệu suất và quyền truy cập bản ghi, không chống được lỗi bảo mật Injection.

**💡 Từ khóa ghi nhớ:** `Chống SOQL Injection -> Static SOQL / escapeSingleQuotes.`

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
> Một lập trình viên viết đoạn mã sau:
List<Account> acc = [Select Id From Account Limit 10];
Delete acc;
Database.emptyRecyclebin(acc);
System.Debug(Limits.getDMLStatements() +', ' + Limits.getLimitDMLStatements());
Kết quả hiển thị trong debug log là gì?

**💬 Giải thích gốc (English):**
> getDMLStatements() Returns the number of DML statements (such as insert, update or the database.EmptyRecycleBin method) that have been called.
> getLimitDMLStatements() Returns the total number of DML statements or the database.EmptyRecycleBin methods that can be called.

**✅ Tại sao đáp án đúng:**
> Cả hai lệnh 'Delete' và 'Database.emptyRecyclebin()' đều được tính là 1 câu lệnh DML riêng biệt. Do đó Limits.getDMLStatements() trả về 2. Giới hạn tổng số lệnh DML trong 1 transaction đồng bộ là 150.

**❌ Tại sao đáp án sai:**
> **A.** Sai số lượng lệnh DML đã chạy và sai giới hạn tối đa.
> **B.** Sai số lượng lệnh DML đã chạy (lệnh emptyRecyclebin cũng bị tính là DML).
> **D.** Sai giới hạn tối đa (150 chứ không phải 200).

**💡 Từ khóa ghi nhớ:** `DML Limit = 150. Cả 'Delete' và 'emptyRecyclebin' đều ngốn 1 DML statement.`

---

## Câu 22

**🔵 Which approach should a developer take to automatically add a 'Maintenance Plan' to each Opportunity that includes an 'Annual Subscription' when an opportunity is closed?**

- **A.** Build a OpportunityLineItem trigger that adds a PriceBookEntry record. ❌
- **B.** Build an OpportunityLineItem trigger to add an OpportunityLineItem record. ❌
- **C.** Build an Opportunity trigger that adds a PriceBookEntry record. ❌
- **D.** Build an Opportunity trigger that adds an OpportunityLineItem record. ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên nên thực hiện cách nào để tự động thêm một 'Maintenance Plan' vào mỗi Opportunity có chứa 'Annual Subscription' khi opportunity đó được đóng?

**💬 Giải thích gốc (English):**
> Write an Apex trigger on the Opportunity object that fires when an Opportunity is closed.

**✅ Tại sao đáp án đúng:**
> OpportunityLineItem là sản phẩm trong Opportunity. Để thêm một sản phẩm mới tự động khi Opportunity đóng (sự kiện trên Opportunity), mày phải viết trigger trên Opportunity để chèn bản ghi OpportunityLineItem (D).

**❌ Tại sao đáp án sai:**
> **A.** Trigger trên OpportunityLineItem không kích hoạt khi Opportunity chính bị đóng.
> **B.** Tương tự A, trigger ở con không dùng để lắng nghe sự kiện thay đổi trạng thái ở cha.
> **C.** PriceBookEntry định nghĩa giá sản phẩm trong bảng giá, chứ không phải bản ghi sản phẩm của Opportunity.

**💡 Từ khóa ghi nhớ:** `Sự kiện xảy ra ở đâu -> Viết Trigger ở đó. Đóng Opportunity -> Trigger trên Opportunity.`

---

## Câu 23

**🔵 Which action may cause triggers to fire?**

- **A.** Renaming or replacing a picklist entry ❌
- **B.** Updates to Feed Items ✅
- **C.** Cascading delete operations ❌
- **D.** Changing a user's default division when the transfer division option is checked ❌

**📝 Dịch tiếng Việt:**
> Hành động nào sau đây có thể khiến các trigger được kích hoạt?

**💬 Giải thích gốc (English):**
> Record Update: When an existing record is updated, triggers associated with the object can fire. This includes both before and after update triggers.

**✅ Tại sao đáp án đúng:**
> FeedItem là một sObject (Chatter post). Khi cập nhật bài đăng, trigger trên FeedItem sẽ nổ như bao object khác.

**❌ Tại sao đáp án sai:**
> **A.** Thay đổi giá trị trong Picklist setup không làm nổ trigger của các bản ghi đang sử dụng giá trị đó.
> **B.** Cascading delete (ví dụ xóa Parent làm bay màu Child) thường không kích hoạt trigger của bản ghi con.
> **D.** Thay đổi division của user là thao tác quản trị tài khoản, không kích hoạt trigger dữ liệu thông thường.

**💡 Từ khóa ghi nhớ:** `Trigger: Cứ đụng đến thao tác dữ liệu (Insert/Update/Delete) trên sObject là trigger nổ.`

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
> Sửa trigger Account để load được 179 bản ghi qua Data Loader mà không bị Exception?

**💬 Giải thích gốc (English):**
> The two actions the developer should take to fix the code segment are:
> 1. Move the DML that saves opportunities outside of the for loop.
> 2. Query for existing opportunities outside of the for loop.

**✅ Tại sao đáp án đúng:**
> 179 > 100 (Limit SOQL), nên phải đưa Query (A) và DML (D) ra ngoài vòng lặp (Bulkification).

**❌ Tại sao đáp án sai:**
> **B.** Đây là lỗi logic về Governor Limit, không phải thiếu field.
> **C.** Database.query vẫn tốn 1 query, không giải quyết được việc gọi lặp lại.

**💡 Từ khóa ghi nhớ:** `Bulkification: No Query/DML in For loop. Nhớ con số 179 > 100 (Limit SOQL).`

---

## Câu 25

**🔵 An org has a data model with a Buyer__c object that has a lookup relationship to Region__c and a Supplier__c object has a lookup relationship to Region___c. How can a developer display data from the related Supplier__c records on a Visualforce page that has a standard controller for the Buyer__c object?**

- **A.** Use rollup formula fields on the Buyer__c object to reference the related Supplier__c records through the Region__c. ❌
- **B.** Use SOQL in a controller extension to query for related Supplier__c records. ✅
- **C.** Use a second standard controller for the Region__c object on a page to display the related Supplier__c records. ❌
- **D.** Use merge field syntax to retrieve the Supplier__c records related to the Buyer__c record through the Region__c. ❌

**📝 Dịch tiếng Việt:**
> Một org có data model gồm object Buyer__c có quan hệ lookup với Region__c, và object Supplier__c cũng có quan hệ lookup với Region__c. Làm thế nào để hiển thị dữ liệu từ các bản ghi Supplier__c liên quan trên một trang Visualforce sử dụng standard controller của Buyer__c?

**💬 Giải thích gốc (English):**
> 1. Create a Custom Controller Extension: Create a custom Apex controller extension for the Visualforce page. The controller extension allows you to add custom logic to the standard controller's functionality.
> 2. Query Related Supplier__c Records: In the custom controller extension, use a SOQL query to retrieve the Supplier__c records related to the Buyer__c record being displayed on the Visualforce page. This can be achieved by using the Buyer__c object's lookup relationship field (e.g., Region__c) to traverse to the related Supplier__c records.

**✅ Tại sao đáp án đúng:**
> Vì Buyer__c và Supplier__c không có quan hệ trực tiếp mà chỉ 'bắc cầu' qua Region__c, standard controller của Buyer không thể tự lấy data của Supplier. Lập trình viên phải dùng Controller Extension viết SOQL để query danh sách Supplier liên quan theo Region (B).

**❌ Tại sao đáp án sai:**
> **A.** Roll-up summary chỉ dùng cho mối quan hệ Master-Detail, không chơi với quan hệ Lookup.
> **C.** Visualforce không cho phép khai báo hai standard controller song song trên cùng một trang.
> **D.** Merge field syntax chỉ đi lên từ con đến cha (quan hệ trực tiếp), không đi vòng qua Region rồi xuống Supplier được.

**💡 Từ khóa ghi nhớ:** `Quan hệ bắc cầu / Không trực tiếp -> Phải dùng Controller Extension viết SOQL query.`

---

## Câu 26

**🔵 A developer is asked to create a custom Visualforce page that will be used as a dashboard component. Which three are valid controller options for this page? (Choose three.)**

- **A.** Use a standard controller. ❌
- **B.** Use a standard controller with extensions. ❌
- **C.** Use a custom controller with extensions. ✅
- **D.** Do not specify a controller. ✅
- **E.** Use a custom controller. ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên được yêu cầu tạo một trang Visualforce tùy chỉnh để dùng làm dashboard component. Ba lựa chọn controller nào sau đây là hợp lệ cho trang này? (Chọn 3)

**✅ Tại sao đáp án đúng:**
> Để trang Visualforce dùng được làm dashboard component, nó KHÔNG ĐƯỢC PHÉP dùng Standard Controller đơn lẻ (vì dashboard cần hiển thị dữ liệu tổng hợp từ nhiều nguồn). Các tùy chọn hợp lệ là: C (Custom với Extension), D (Không dùng controller), E (Custom Controller).

**❌ Tại sao đáp án sai:**
> **A.** Dùng Standard Controller thuần túy sẽ khóa trang vào một bản ghi cụ thể, cấm dùng làm Dashboard.
> **B.** Tương tự A, Standard Controller có thêm Extension vẫn bị giới hạn bởi record context của Standard Controller.

**💡 Từ khóa ghi nhớ:** `Visualforce Dashboard Component = KHÔNG dùng Standard Controller.`

---

## Câu 27

**🔵 Universal Hiring is using Salesforce to capture job applications. A salesforce administrator created two custom objects: Job__c acting as the master object, Job_Application__c acting as the detail. Within the Job__c object, a custom multi-select picklist, Preferred_Locations__c, contains a list of approved states for the position. Each Job_Application__c record relates to a Contact within the system through a master-detail relationship. 	Recruiters have requested the ability to view whether the Contact's Mailing State value matches a value selected on the Preferred_Locations__c field, within the Job_Application__c record. Recruiters would like this value to be kept in sync, if changes occur to the Contact's Mailing State or if the Job's Preferred_Locations__c field is updated. What is the recommended tool a developer should use to meet the business requirement?**

- **A.** Apex Trigger ❌
- **B.** Process Builder ❌
- **C.** Record-triggered flow ✅
- **D.** Formula field ❌

**📝 Dịch tiếng Việt:**
> Object Job__c là Master, Job_Application__c là Detail. Job_Application__c cũng có quan hệ Master-Detail với Contact. Trên Job__c có trường multi-select picklist Preferred_Locations__c. Recruiters muốn xem Contact Mailing State có khớp với Preferred_Locations__c trên Job_Application__c hay không và phải đồng bộ tự động khi một trong hai thay đổi. Công cụ khai báo nào là tối ưu nhất?

**✅ Tại sao đáp án đúng:**
> Yêu cầu đòi hỏi theo dõi thay đổi ở cả hai đầu (Contact hoặc Job) và cập nhật bản ghi trung gian Job_Application__c. Record-triggered flow (C) là công cụ low-code mạnh mẽ nhất hiện nay để xử lý logic đồng bộ phức tạp này.

**❌ Tại sao đáp án sai:**
> **A.** Apex Trigger giải quyết tốt nhưng tốn công viết code và deploy, không phải công cụ khai báo (declarative) được ưu tiên.
> **B.** Process Builder đã bị Salesforce khai tử (deprecated) và hiệu năng kém hơn nhiều so với Flow.
> **D.** Formula field không thể tự động so sánh giá trị Mailing State với một trường Multi-select Picklist và giữ đồng bộ hai chiều phức tạp.

**💡 Từ khóa ghi nhớ:** `Đồng bộ phức tạp + Low-code = Record-triggered flow.`

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
> Một lập trình viên khai báo một class như sau:
public class wysiwyg {
//properties and methods including DML
}
Cách gọi phương thức nào của class này sẽ tuân thủ OWD và sharing settings của user đang chạy trong Salesforce org?

**✅ Tại sao đáp án đúng:**
> Vì class không khai báo từ khóa sharing, mặc định nó sẽ chạy ở 'system mode' (bỏ qua sharing). Tuy nhiên, khi gọi code từ Anonymous Block (B), Salesforce luôn ép buộc tuân thủ quyền hạn và sharing của user đang đăng nhập.

**❌ Tại sao đáp án sai:**
> **A.** Trigger luôn chạy ở system mode, nên gọi class helper cũng sẽ bỏ qua sharing rules.
> **C.** Visualforce controller chạy ở system mode mặc định, trừ khi class controller khai báo 'with sharing'.
> **D.** API call từ hệ thống ngoài vào Salesforce chạy với ngữ cảnh tích hợp, mặc định cũng bỏ qua sharing nếu class không khai báo rõ ràng.

**💡 Từ khóa ghi nhớ:** `Execute Anonymous = Luôn tuân thủ quyền hạn của User đang đăng nhập.`

---

## Câu 29

**🔵 Universal Containers uses a simple Order Management app. On the Order Lines, the order line total is calculated by multiplying the item price with the quantity ordered. There is a Master-Detail relationship between the Order and the Order Lines object. What is the best practice to get the sum of all order line totals on the order header?**

- **A.** Declarative Roll-Up Summaries App ❌
- **B.** Roll-Up Summary field ✅
- **C.** Process Builder ❌
- **D.** Apex Trigger ❌

**📝 Dịch tiếng Việt:**
> Universal Containers sử dụng một ứng dụng quản lý đơn hàng đơn giản. Trên OpportunityLineItem (sản phẩm), tổng tiền được tính bằng cách nhân đơn giá với số lượng. Có quan hệ Master-Detail giữa Opportunity (Order) và OpportunityLineItem. Cách tốt nhất để tính tổng tiền của tất cả các dòng sản phẩm lên Opportunity là gì?

**💬 Giải thích gốc (English):**
> Roll-Up Summary Fields are a powerful feature in Salesforce that allow you to calculate and display aggregate values (such as sum, count, max, min, etc.) from child records on a parent record. In this case, you can create a Roll-Up Summary Field on the Order object to calculate the total order amount by summing up the order line totals from all related Order Line records.

**✅ Tại sao đáp án đúng:**
> Vì mối quan hệ là Master-Detail, sử dụng Roll-Up Summary field (B) là giải pháp 'chân ái' nhất: không cần viết code, cực kỳ tối ưu, tự động cập nhật real-time và đúng chuẩn Salesforce Best Practice.

**❌ Tại sao đáp án sai:**
> **A.** Hệ thống đã có sẵn tính năng Roll-Up Summary field rồi, không cần cài thêm app ngoài làm gì cho mệt.
> **C.** Process Builder không hỗ trợ tính toán tổng hợp (SUM, COUNT) trên danh sách con một cách trực tiếp.
> **D.** Apex Trigger hoạt động tốt nhưng viết code cho một tính năng đã có sẵn no-code là vi phạm nguyên tắc tối ưu.

**💡 Từ khóa ghi nhớ:** `Master-Detail + Sum/Count lên Cha = Roll-Up Summary Field.`

---

## Câu 30

**🔵 Given the following Apex statement: Account myAccount = [SELECT Id, Name FROM Account]; What occurs when more than one Account is returned by the SOQL query?**

- **A.** The variable, myAccount, is automatically cast to the List data type. ❌
- **B.** The first Account returned is assigned to myAccount. ❌
- **C.** The query fails and an error is written to the debug log. ❌
- **D.** An unhandled exception is thrown and the code terminates. ✅

**📝 Dịch tiếng Việt:**
> Điều gì xảy ra khi câu query trả về nhiều hơn một bản ghi và được gán cho một biến đơn?

**💬 Giải thích gốc (English):**
> When the query returns multiple records (multiple Accounts in this case), Salesforce will raise a QueryException because you cannot assign a list of records to a single record variable.

**✅ Tại sao đáp án đúng:**
> Bắn lỗi `QueryException: List has more than 1 row for assignment`. Nếu không bắt lỗi bằng try/catch, code sẽ dừng đột ngột.

**❌ Tại sao đáp án sai:**
> **A.** Apex không tự động đổi kiểu dữ liệu từ sObject sang List cho mày.
> **B.** Hệ thống không tự ý lấy bản ghi đầu tiên, trừ khi mày thêm `LIMIT 1` vào câu query.
> **C.** Không chỉ ghi log, nó còn dừng thực thi và rollback transaction nếu là exception không được xử lý.

**💡 Từ khóa ghi nhớ:** `An toàn: Luôn query vào List.`

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
> **A.** Cộng chuỗi trực tiếp từ user input là con đường nhanh nhất để bị hack.
> **D.** Database.query() với chuỗi được cộng trực tiếp mà không qua sanitize cực kỳ nguy hiểm và dễ bị injection.

**💡 Từ khóa ghi nhớ:** `Chống SOQL Injection: 1. Static SOQL (:bind), 2. escapeSingleQuotes().`

---

## Câu 36

**🔵 A developer must create a ShippingCalculator class that cannot be instantiated and must include a working default implementation of a calculate method, that sub-classes can override. What is the correct implementation of the ShippingCalculator class?
A.
public abstract class ShippingCalculator{
public abstract calculate() { /*implementation*/}
}
B.
public abstract class ShippingCalculator{
public virtual void calculate() { /*implementation*/}
}
C.
public abstract class ShippingCalculator{
public void calculate() { /*implementation*/}
}
D.
public abstract class ShippingCalculator{
public override calculate() { /*implementation*/}
}**


**📝 Dịch tiếng Việt:**
> Lập trình viên cần tạo class ShippingCalculator không được phép khởi tạo trực tiếp (cannot be instantiated) nhưng phải chứa một phương thức calculate có sẵn mã xử lý mặc định để các class con có thể ghi đè (override). Khai báo nào sau đây là đúng?

**💬 Giải thích gốc (English):**
> To create a ShippingCalculator class that cannot be instantiated and includes a default implementation of a calculate method that sub-classes can override, you can use the abstract keyword for the class and the virtual keyword for the calculate method.

**✅ Tại sao đáp án đúng:**
> Để class không được khởi tạo trực tiếp, ta dùng từ khóa 'abstract class'. Để phương thức có code mặc định và cho phép class con ghi đè, ta dùng từ khóa 'virtual void calculate()' (B).

**❌ Tại sao đáp án sai:**
> **A.** calculate() khai báo abstract thì cấm viết body code mặc định (bắt buộc class con tự viết).
> **C.** calculate() thiếu từ khóa 'virtual' thì các class con không thể override ghi đè được.
> **D.** Từ khóa 'override' chỉ dùng ở class con để ghi đè, không dùng ở class cha để khai báo ban đầu.

**💡 Từ khóa ghi nhớ:** `Cấm new (instantiate) -> abstract class. Cho phép con ghi đè -> virtual method.`

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
> **C.** Strategy Builder dùng để đề xuất ưu đãi/hành động trong Next Best Action, không hỗ trợ gửi Outbound Message.
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
> **B.** escapeSingleQuotes() dùng cho SOQL Injection (SQL), không phải XSS (HTML).
> **D.** Lấy trực tiếp mà không xử lý là dâng "tận miệng" cho hacker hack XSS.

**💡 Từ khóa ghi nhớ:** `XSS = Hacker nhồi script vào UI. Cách chống: .escapeHtml() hoặc dùng <apex:outputText> mặc định.`

---

## Câu 40

**🔵 A Visual Flow uses an Apex Action to provide additional information about multiple Contacts, stored in a custom class, ContactInfo. Which is the correct definition of the Apex method that gets the additional information?
A.
@InvocableMethod(label='Additional Info')
public ContactInfo getInfo(Id contactId) { /*implementation*/ }
B.
@InvocableMethod(label='Additional Info')
public List<ContactInfo> getInfo(List<Contact> contactIds) { /*implementation*/ }
C.
@InvocableMethod(label='Additional Info')
public static ContactInfo getInfo(Id contactId) { /*implementation*/ }
D.
@InvocableMethod(label='Additional Info')
public static List<ContactInfo> getInfo(List<Contact> contactIds) { /*implementation*/ }**


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
> Phương thức gắn @InvocableMethod bắt buộc phải là 'static' để Salesforce gọi được trực tiếp. Đồng thời, để hỗ trợ xử lý hàng loạt (bulkified), tham số đầu vào và kiểu trả về phải là List. Do đó, câu D là hoàn toàn chính xác.

**❌ Tại sao đáp án sai:**
> **A.** Thiếu từ khóa 'static' và tham số đầu vào không phải là List.
> **B.** Thiếu từ khóa 'static' (bắt buộc phải có để Flow gọi).
> **C.** Tham số đầu vào không ở dạng List, không hỗ trợ bulkification.

**💡 Từ khóa ghi nhớ:** `@InvocableMethod: Luôn có STATIC, input và output luôn ở dạng LIST.`

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
> **B.** Org giới hạn tổng dung lượng code (6MB cho Apex), chứ không giới hạn cứng số lượng class theo kiểu transaction limit.
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
> **B.** Ngược lại, LDS rất tôn trọng FLS.
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
> **C.** Without sharing là 'mở toang' hết, ai cũng thấy hết mọi thứ.
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
> **A.** Admin validate không giải quyết được lỗi logic code.
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
> **C.** Bản ghi Junction kiểu MD không có quyền Sharing độc lập để mày set riêng.

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
> **D.** Thiếu static thì mỗi lần gọi class nó lại tạo ra instance mới, không giữ được state.

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
> Universal Containers có quy trình cho phép người dùng yêu cầu hỗ trợ từ đội kỹ thuật qua object tùy chỉnh Engineering_Support__c. Một Opportunity có thể có nhiều bản ghi hỗ trợ liên quan, và thông tin tổng hợp (aggregate) của các bản ghi hỗ trợ này phải được hiển thị trên Opportunity. Developer nên làm gì?

**💬 Giải thích gốc (English):**
> Implementing a Master-detail relationship from the Engineering_Support__c custom object to the Opportunity standard object ensures that the support records are tightly associated with specific Opportunities. This relationship allows for automatic aggregation of information and cascading behavior, which is essential for displaying aggregate data on the Opportunity record.

**✅ Tại sao đáp án đúng:**
> Để hiển thị thông tin tổng hợp (như Sum, Count, Min, Max) bằng công cụ Roll-up Summary field mà không cần code, mày bắt buộc phải thiết lập quan hệ Master-Detail. Trong đó, Engineering_Support__c là con (Detail) trỏ về Opportunity là cha (Master).

**❌ Tại sao đáp án sai:**
> **B.** Lookup trỏ từ cha sang con là sai hoàn toàn về logic quan hệ.
> **C.** Master-detail trỏ từ cha sang con cũng sai, field quan hệ phải nằm ở bên 'Nhiều' (phía con).
> **D.** Lookup field không hỗ trợ tính năng Roll-up Summary để lấy thông tin tổng hợp lên bản ghi cha.

**💡 Từ khóa ghi nhớ:** `Mẹo thi: Thấy chữ 'Aggregate information' + 'Related records' -> Nghĩ ngay đến Roll-up Summary -> Chọn Master-Detail.`

---

## Câu 62

**🔵 When a user edits the Postal Code on an Account, a custom Account text field named 'Timezone' must be updated based on the values in another custom object called PostalCodeToTimezone__c. What is the optimal way to implement this feature?**

- **A.** Build an account assignment rule. ❌
- **B.** Build a flow with Flow Builder. ✅
- **C.** Create an account approval process. ❌
- **D.** Create a formula field. ❌

**📝 Dịch tiếng Việt:**
> Khi user sửa mã bưu điện (Postal Code) trên Account, một trường text tùy chỉnh tên 'Timezone' phải được update tự động dựa trên data từ custom object `PostalCodeToTimezone__c`. Cách nào là tối ưu nhất để làm vụ này?

**💬 Giải thích gốc (English):**
> The flow can then perform actions such as querying the PostalCodeToTimezone__c custom object, retrieving the relevant timezone value, and updating the ‘Timezone’ field on the Account.
> Formula fields are used to calculate values based on other fields on the same object or related objects, but they cannot perform lookups to other custom objects.

**✅ Tại sao đáp án đúng:**
> C là chân ái vì Flow Builder xử lý ngon ơ các vụ: (1) Trigger khi field thay đổi, (2) Query data từ object khác (Get Records), (3) Update field — tất cả đều là low-code, đúng chuẩn 'optimal'.

**❌ Tại sao đáp án sai:**
> **A.** Account Assignment Rule chỉ dùng để chia lead/case hoặc gán owner cho Account dựa trên territory, không dùng để update field kiểu lookup data thế này.
> **B.** Formula field chỉ chơi được 'Cross-object formula' hướng từ con lên cha (Lookup/Master-Detail), không thể đi query một object 'người dưng' như `PostalCodeToTimezone__c` được.
> **D.** Approval Process dùng để duyệt đơn, duyệt lương... chứ ai rảnh đi duyệt cái Postal Code để update field.

**💡 Từ khóa ghi nhớ:** `Mẹo PD1: Cứ thấy update field mà cần 'tra cứu' (Lookup) sang object khác không có quan hệ trực tiếp thì gọi tên Flow ngay và luôn.`

---

## Câu 63

**🔵 A team of many developers work in their own individual orgs that have the same configuration as the production org. Which type of org is best suited for this scenario?**

- **A.** Developer Sandbox ✅
- **B.** Developer Edition ❌
- **C.** Full Sandbox ❌
- **D.** Partner Developer Edition ❌

**📝 Dịch tiếng Việt:**
> Loại tổ chức (org) nào phù hợp nhất cho nhiều dev làm việc độc lập với cấu hình giống Production?

**💬 Giải thích gốc (English):**
> A Developer Sandbox is a copy of the production org with the same configuration and data. Each developer can have their own Developer Sandbox, which allows them to work independently without interfering with each other's work.

**✅ Tại sao đáp án đúng:**
> Developer Sandbox copy toàn bộ Metadata (cấu hình) từ Production, miễn phí (với hầu hết license) và khởi tạo cực nhanh, phù hợp cho cá nhân dev.

**❌ Tại sao đáp án sai:**
> **A.** Developer Edition là org cá nhân trống rỗng, không tự động có cấu hình giống Production của khách hàng.
> **C.** Full Sandbox cực kỳ đắt đỏ, dung lượng lớn và thời gian refresh rất lâu, không ai cấp Full Sandbox cho từng dev làm việc lẻ tẻ.

**💡 Từ khóa ghi nhớ:** `Sandbox: Developer (Metadata only), Full (All Data).`

---

## Câu 64

**🔵 Universal Containers uses Service Cloud with a custom field, Stage__c, on the Case object. Management wants to send a follow-up email reminder 6 hours after the Stage__c field is set to 'Waiting on Customer'. The Salesforce Administrator wants to ensure the solution used is bulk safe. Which automation tool should a developer recommend to meet these business requirements? (Choose two)**

- **A.** Record-Triggered Flow ✅
- **B.** Entitlement Process ❌
- **C.** Einstein Next Best Action ❌
- **D.** Scheduled Flow ✅

**📝 Dịch tiếng Việt:**
> Universal Containers muốn gửi email nhắc nhở tự động sau 6 giờ kể từ khi trường Stage__c trên Case chuyển sang 'Waiting on Customer'. Giải pháp nào vừa tối ưu, không code và đảm bảo an toàn xử lý hàng loạt (bulk safe)? (Chọn 2)

**💬 Giải thích gốc (English):**
> A Record-Triggered Flow can be used to detect when the Stage__c field is updated to ‘Waiting on Customer’. Then, a Scheduled Flow can be set to execute 6 hours later to send the follow-up email.

**✅ Tại sao đáp án đúng:**
> A: Record-Triggered Flow hỗ trợ tính năng Scheduled Paths, cho phép lên lịch chạy sau 6 giờ cực kỳ bulk-safe. D: Scheduled Flow cũng là công cụ chuyên dụng để quét định kỳ và gửi mail hàng loạt rất an toàn.

**❌ Tại sao đáp án sai:**
> **B.** Entitlement Process dùng để quản lý SLA/Milestone của Case hỗ trợ gửi mail nhưng phức tạp và không chuyên dụng bằng Flow cho yêu cầu này.
> **C.** Einstein Next Best Action dùng để hiển thị gợi ý cho nhân viên trên màn hình, không phải tự động gửi email ngầm.

**💡 Từ khóa ghi nhớ:** `Tự động hóa theo thời gian (Time-dependent) + Low-code = Scheduled Path trong Flow.`

---

## Câu 65

**🔵 A developer observes that an Apex test method fails in the Sandbox. To identify the issue, the developer copies the code inside the test method and executes it via the Execute Anonymous tool in the Developer Console. The code then executes with no exceptions or errors. Why did the test method fail in the sandbox and pass in the Developer Console?**

- **A.** The test method has a syntax error in the code. ❌
- **B.** The test method does not use System.runAs to execute as a specific user. ❌
- **C.** The test method is calling an @future method. ❌
- **D.** The test method relies on existing data in the sandbox. ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên thấy một test method bị FAIL trong Sandbox. Nhưng khi copy toàn bộ code đó chạy thử ở Execute Anonymous trong Dev Console thì lại PASS không lỗi gì. Tại sao có sự kỳ lạ này?

**💬 Giải thích gốc (English):**
> When running the same code in the Execute Anonymous tool in the Developer Console, it executes within the current user's context and can access the existing data, which might result in successful execution.

**✅ Tại sao đáp án đúng:**
> Khi chạy unit test, Salesforce mặc định cô lập dữ liệu (SeeAllData=false), không thấy được bản ghi thật. Còn Execute Anonymous thì chạy trên data thật của Org. Lỗi xảy ra vì code test phụ thuộc vào dữ liệu thật có sẵn trong Sandbox mà class test chưa tự tạo ra (D).

**❌ Tại sao đáp án sai:**
> **A.** Nếu có lỗi cú pháp (syntax error) thì cả Test Class và Execute Anonymous đều cấm biên dịch thành công.
> **B.** Thiếu runAs chỉ làm sai ngữ cảnh phân quyền chứ không làm thay đổi sự khác biệt về cô lập dữ liệu giữa 2 môi trường.
> **C.** Gọi phương thức @future trong test bắt buộc phải bọc trong Test.startTest() / stopTest(), chạy Execute Anonymous vẫn nổ lỗi nếu sai quy tắc.

**💡 Từ khóa ghi nhớ:** `Test FAIL nhưng Execute Anonymous PASS -> Chắc chắn do thiếu dữ liệu giả lập (Test Data isolation).`

---

## Câu 66

**🔵 A developer is writing tests for a class and needs to insert records to validate functionality. Which annotation method should be used to create records for every method in the test class?**

- **A.** @StartTest ❌
- **B.** @PreTest ❌
- **C.** @TestSetup ✅
- **D.** @isTest(SeeAllData=true) ❌

**📝 Dịch tiếng Việt:**
> Dùng annotation nào để tạo dữ liệu dùng chung cho tất cả các test method trong class?

**💬 Giải thích gốc (English):**
> @TestSetup annotation
> Can create common test data once, which will be available for all test methods in the test class. This helps reduce duplicate code and ensures that the test data is consistent across all test methods.

**✅ Tại sao đáp án đúng:**
> @TestSetup giúp tạo dữ liệu một lần duy nhất cho cả class test, giúp tiết kiệm thời gian chạy đáng kể.

**❌ Tại sao đáp án sai:**
> **B.** SeeAllData=true là 'tối kỵ' vì nó làm test bị phụ thuộc vào data thật của Org.
> **C.** Giống B, cực kỳ không khuyến khích trừ trường hợp bất khả kháng.
> **D.** @PreTest là annotation 'pha kè', Salesforce không có cái này.

**💡 Từ khóa ghi nhớ:** `Keyword: Common test data -> @TestSetup. Chạy 1 lần, dùng cả đời (class).`

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
> Trong ví dụ trên, phương thức myMethod sẽ thực thi trong ngữ cảnh chia sẻ (sharing context) nào?

**💬 Giải thích gốc (English):**
> Since the class myClass does not explicitly specify a sharing context (using with sharing or without sharing), it defaults to “without sharing”. This means that the method myMethod will execute without enforcing the sharing rules of the running user.

**✅ Tại sao đáp án đúng:**
> Nếu một class không khai báo rõ 'with sharing' hay 'without sharing', nó sẽ ở trạng thái mặc định: kế thừa ngữ cảnh từ class gọi nó (Calling context). Nếu thằng gọi có sharing, nó có; nếu không, nó không.

**❌ Tại sao đáp án sai:**
> **A.** Đây là hành vi của 'without sharing', không phải mặc định khi omit từ khóa.
> **C.** Đây là hành vi của 'with sharing'.
> **D.** Instantiating class chính là calling context trong nhiều trường hợp, nhưng thuật ngữ 'inherited from calling context' là chuẩn nhất của Salesforce.

**💡 Từ khóa ghi nhớ:** `No keyword = Inherited sharing. Như kiểu con nhà tông, không giống lông cũng giống cánh.`

---

## Câu 68

**🔵 A developer created a new after insert trigger on the Lead object that creates Task records for each Lead. After deploying to production, an existing outside integration that inserts Lead records in batches to Salesforce is occasionally reporting total batch failures being caused by the Task insert statement. This causes the integration process in the outside system to stop, requiring a manual restart. 	Which change should the developer make to allow the integration to continue when some records in a batch cause failures due to the Task insert statement, so that manual restarts are not needed?**

- **A.** Deactivate the trigger before the integration runs. ❌
- **B.** Use a try-catch block after the insert statement. ❌
- **C.** Use the Database method with allOrNone set to false. ✅
- **D.** Remove the Apex class from the integration user’s profile. ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên tạo trigger 'after insert' trên Lead để tạo Task cho mỗi Lead. Khi deploy lên Production, một hệ thống tích hợp bên ngoài nạp Lead theo lô (batch) thỉnh thoảng báo lỗi cả lô do câu lệnh insert Task thất bại. Việc này làm dừng tiến trình của hệ thống ngoài và yêu cầu restart thủ công. Thay đổi nào giúp tiến trình tiếp tục chạy khi một vài bản ghi trong lô bị lỗi?

**💬 Giải thích gốc (English):**
> When using the Database.insert() method with allOrNone set to false, if there are any errors during the insert operation (such as validation rule failures or triggers that cause an exception), the successful records will be committed, and the failed records will generate errors but won't cause the entire batch to fail. This way, the integration process will continue without requiring a manual restart.

**✅ Tại sao đáp án đúng:**
> Sử dụng phương thức Database.insert(tasks, false) (C) với tham số allOrNone = false. Khi đó, những bản ghi Task hợp lệ vẫn được insert thành công, còn bản ghi lỗi sẽ được ghi nhận vào SaveResult mà không bắn ra unhandled exception làm oẳng cả transaction của hệ thống tích hợp.

**❌ Tại sao đáp án sai:**
> **A.** Deactivate trigger là giải pháp trốn tránh, làm mất đi tính năng tạo Task tự động rất quan trọng.
> **B.** Dùng try-catch sau khi insert không giúp cứu vãn các bản ghi khác trong lô nếu lệnh DML insert chuẩn thất bại (vì nó sẽ rollback toàn bộ lô nếu dính lỗi DML).
> **D.** Xóa quyền truy cập class sẽ làm hệ thống tích hợp lỗi 100% thay vì chạy tiếp.

**💡 Từ khóa ghi nhớ:** `Muốn lô chạy tiếp dù có vài bản ghi lỗi -> Database.insert(..., false).`

---

## Câu 69

**🔵 A developer needs to join data received from an integration with an external system with parent records in Salesforce. The data set does not contain the Salesforce IDs of the parent records, but it does have a foreign key attribute that can be used to identify the parent. Which action will allow the developer to relate records in the data model without knowing the Salesforce ID?**

- **A.** Create and populate a custom field on the parent object marked as Unique. ❌
- **B.** Create a custom field on the child object of type External Relationship. ❌
- **C.** Create and populate a custom field on the parent object marked as an External ID. ✅
- **D.** Create a custom field on the child object of type Foreign Key. ❌

**📝 Dịch tiếng Việt:**
> Làm sao để liên kết bản ghi mà không cần Salesforce ID?

**💬 Giải thích gốc (English):**
> An External ID field is used to store unique identifiers from an external system and allows the developer to use this external identifier to match records in Salesforce with records in the external system.

**✅ Tại sao đáp án đúng:**
> External ID cho phép Salesforce map bản ghi dựa trên mã định danh từ hệ thống bên ngoài.

**❌ Tại sao đáp án sai:**
> **A.** External Relationship dùng cho External Objects (Salesforce Connect).
> **C.** Unique chỉ chống trùng, không giúp map bản ghi khi Upsert/Insert.
> **D.** Lookup field bình thường vẫn 'đòi' ID của Salesforce.

**💡 Từ khóa ghi nhớ:** `No ID? -> Use External ID.`

---

## Câu 70

**🔵 A developer creates a new Apex trigger with a helper class, and writes a test class that only exercises 95% coverage of the new Apex helper class. Change Set deployment to production fails with the test coverage warning: Test coverage of selected Apex Trigger is 0%, at least 1% test coverage is required. What should the developer do to successfully deploy the new Apex trigger and helper class?**

- **A.** Increase the test class coverage on the helper class. ❌
- **B.** Remove the failing test methods from the test class. ❌
- **C.** Run the tests using the 'Run All Tests' method. ❌
- **D.** Create a test class and methods to cover the Apex trigger. ✅

**📝 Dịch tiếng Việt:**
> Helper class đạt 95% nhưng Trigger 0% làm deployment thất bại. Phải làm gì?

**💬 Giải thích gốc (English):**
> To successfully deploy the new Apex trigger and helper class, the developer needs to create a test class that provides test coverage for both the trigger and the helper class.

**✅ Tại sao đáp án đúng:**
> Trigger bắt buộc phải được kích hoạt trong code test (qua lệnh DML) để có coverage > 0%. Dù helper 100% mà trigger không chạy thì vẫn tạch.

**❌ Tại sao đáp án sai:**
> **A.** Tăng coverage cho helper không giúp gì cho việc trigger đang 0%.
> **C.** Xóa test method hỏng không giúp trigger có thêm phần trăm coverage nào.
> **D.** Run All Tests chỉ là chạy lại đống cũ, nếu chưa viết code test cho trigger thì kết quả vẫn là 0%.

**💡 Từ khóa ghi nhớ:** `Deployment Rule: Toàn Org 75%, nhưng mỗi Trigger phải > 0%.`

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
> Có bao nhiêu Account sẽ được insert thành công bởi đoạn mã trên?

**💬 Giải thích gốc (English):**
> DML Exception

**✅ Tại sao đáp án đúng:**
> Đáp án là 0. Đến vòng lặp thứ 151, hệ thống bắn lỗi `LimitException: Too many DML statements: 151`. Toàn bộ transaction bị rollback, không có account nào được lưu.

**❌ Tại sao đáp án sai:**
> **D.** Dù limit là 150, nhưng vì transaction là atomic (nguyên tử), lỗi xảy ra làm hủy hết mọi kết quả trước đó.
> **A.** Vượt xa giới hạn cho phép của Salesforce.

**💡 Từ khóa ghi nhớ:** `DML Limit = 150. Nhét DML vào For là 'cook'!`

---

## Câu 72

**🔵 A developer needs to implement a custom SOAP Web Service that is used by an external Web Application. The developer chooses to Include helper methods that are not used by the Web Application in the implementation of the Web Service Class. Which code segment shows the correct declaration of the class and methods?
A.
Webservice class WebserviceClass{
private Boolean helperMethod(){ /*implementation ...*/}
global static String updateRecords(){ /*implementation ...*/}
}
B.
global class WebserviceClass{
private Boolean helperMethod(){ /*implementation ...*/}
webservice static String updateRecords(){ /*implementation ...*/}
}
C.
Webservice class WebserviceClass{
private Boolean helperMethod(){ /*implementation ...*/}
Webservice static String updateRecords(){ /*implementation ...*/}
}
D.
global class WebserviceClass{
private Boolean helperMethod(){ /*implementation ...*/}
global String updateRecords(){ /*implementation ...*/}
}**


**📝 Dịch tiếng Việt:**
> Lập trình viên cần tạo một SOAP Web Service tùy chỉnh để ứng dụng ngoài gọi vào. Lập trình viên muốn viết thêm các phương thức helper nội bộ không dùng cho bên ngoài. Khai báo class và method nào sau đây là đúng chuẩn?

**💬 Giải thích gốc (English):**
> The class must be declared as global to be accessible by external applications.
> The method that is exposed as a web service must be declared with the webservice keyword.

**✅ Tại sao đáp án đúng:**
> Class chứa SOAP Web Service bắt buộc phải khai báo là 'global'. Phương thức phơi ra cho bên ngoài gọi phải dùng annotation 'webservice static'. Các phương thức helper nội bộ có thể để 'private' bình thường (B).

**❌ Tại sao đáp án sai:**
> **A.** Cú pháp 'Webservice class' ở đầu định nghĩa class là sai hoàn toàn, class phải khai báo bằng 'global class'.
> **C.** Sai cú pháp khai báo class giống câu A.
> **D.** Phương thức phơi ra làm API SOAP thiếu từ khóa 'webservice' và thiếu 'static'.

**💡 Từ khóa ghi nhớ:** `SOAP Web Service: Class phải GLOBAL, Method phải WEBSERVICE STATIC.`

---

## Câu 73

**🔵 A developer is asked to prevent anyone other than a user with Sales Manager profile from changing the Opportunity Status to Closed Lost if the lost reason is blank. Which automation allows the developer to satisfy this requirement in the most efficient manner?**

- **A.** An error condition formula on a validation rule on Opportunity ✅
- **B.** An Apex trigger on the Opportunity object ❌
- **C.** A record trigger flow on the Opportunity object ❌
- **D.** An approval process on the Opportunity object ❌

**📝 Dịch tiếng Việt:**
> Ngăn không cho ai (ngoại trừ Sales Manager) chuyển Status Opportunity sang 'Closed Lost' mà lại để trống lý do (Lost Reason). Dùng cái gì nhanh gọn lẹ nhất?

**💬 Giải thích gốc (English):**
> Using a validation rule is the most efficient way to enforce this requirement. The validation rule can be set up to check if the Opportunity Status is being changed to “Closed Lost” and if the “Lost Reason” field is blank.
> Here’s an example of how the validation rule might look:
> AND(
> ISPICKVAL(StageName, "Closed Lost"),
> ISBLANK(Lost_Reason__c),
> $Profile.Name <> "Sales Manager"
> )

**✅ Tại sao đáp án đúng:**
> D là đỉnh nhất. Validation Rule sinh ra là để chặn data sai format/điều kiện. Vừa nhanh, vừa không tốn code, vừa dễ bảo trì.

**❌ Tại sao đáp án sai:**
> **A.** Flow cũng làm được nhưng nó giống như dùng dao mổ trâu để giết gà, phức tạp hơn Validation Rule nhiều.
> **B.** Approval Process dùng để duyệt, không phải để check logic field đơn giản thế này.
> **C.** Apex Trigger thì thôi, viết mớ code chỉ để check một cái field thì quá là lãng phí tài nguyên và thời gian deploy.

**💡 Từ khóa ghi nhớ:** `Mẹo PD1: Cứ thấy 'Prevent', 'Block', 'Validation' là nghĩ ngay đến Validation Rule đầu tiên. Đừng ham code!`

---

## Câu 74

**🔵 A developer needs to prevent the creation of Request records when certain conditions exist in the system. A RequestLogic class exists that checks the conditions. What is the correct implementation?
A.
trigger RequestTrigger on Request(before insert){
if(RequestLogic.isValid(Request))
Request.addError('Your request cannot be created at this time.');
}
B.
trigger RequestTrigger on Request(after insert){
if(RequestLogic.isValid(Request))
Request.addError('Your request cannot be created at this time.');
}
C.
trigger RequestTrigger on Request(after insert){
RequestLogic.validateRecords(trigger.new)
}
D.
trigger RequestTrigger on Request(before insert){
RequestLogic.validateRecords(trigger.new)
}**


**📝 Dịch tiếng Việt:**
> Lập trình viên cần chặn việc tạo bản ghi Request khi có một số điều kiện nhất định xảy ra trong hệ thống. Một class RequestLogic đã có sẵn hàm kiểm tra. Khai báo trigger nào là đúng chuẩn để thực hiện việc này?

**💬 Giải thích gốc (English):**
> This implementation ensures that the validation logic is applied before the records are inserted into the database, allowing the trigger to prevent the creation of invalid records.

**✅ Tại sao đáp án đúng:**
> Để CHẶN (prevent) việc lưu dữ liệu, ta bắt buộc phải dùng sự kiện 'before insert' (D) để gọi hàm addError() trước khi dữ liệu chạm xuống ổ cứng. Đồng thời, truyền toàn bộ 'trigger.new' vào class helper để xử lý bulkified là chuẩn bài nhất.

**❌ Tại sao đáp án sai:**
> **A.** Trigger này viết loop gọi addError thủ công nhưng cú pháp sai hoàn toàn (Request là tên đối tượng chứ không phải biến chạy).
> **B.** after insert là quá muộn để chặn tạo bản ghi, vì dữ liệu đã ghi xuống database rồi, gọi addError lúc này sẽ tốn tài nguyên rollback.
> **C.** after insert là sai thời điểm giống câu B.

**💡 Từ khóa ghi nhớ:** `Muốn CHẶN tạo bản ghi -> Dùng trigger BEFORE INSERT + addError().`

---

## Câu 75

**🔵 Which annotation exposes an Apex class as a RESTful web service?**

- **A.** @RemoteAction ❌
- **B.** @RestResource ✅
- **C.** @HttpInvocable ❌
- **D.** @AuraEnabled ❌

**📝 Dịch tiếng Việt:**
> Annotation nào biến class thành REST service?

**✅ Tại sao đáp án đúng:**
> @RestResource dùng để khai báo class là REST service.

**❌ Tại sao đáp án sai:**
> **A.** Dùng cho Visualforce JS Remoting.
> **B.** Dùng cho LWC/Aura gọi Apex.
> **D.** @HttpInvocable là một cái tên giả tưởng, không tồn tại.

**💡 Từ khóa ghi nhớ:** `Keywords: REST API -> @RestResource.`

---

## Câu 76

**🔵 A developer must troubleshoot to pinpoint the causes of performance issues when a custom page loads in their org. Which tool should the developer use to troubleshoot?**

- **A.** Visual Studio Code IDE ❌
- **B.** AppExchange ❌
- **C.** Developer Console ✅
- **D.** Setup Menu ❌

**📝 Dịch tiếng Việt:**
> Một developer cần tìm nguyên nhân gây ra vấn đề về hiệu suất khi một trang tùy chỉnh tải trong Org. Developer nên sử dụng công cụ nào?

**💬 Giải thích gốc (English):**
> The Developer Console allows developers to set up debug logs for specific users or classes. These logs capture detailed information about the execution of Apex code, including any SOQL queries, DML operations, and method calls.

**✅ Tại sao đáp án đúng:**
> Developer Console cung cấp các công cụ như 'Timeline' và 'Execution Log' cực kỳ chi tiết. Nó cho mày biết câu query nào tốn bao nhiêu giây, code Apex nào ngốn CPU nhất để mà tối ưu.

**❌ Tại sao đáp án sai:**
> **A.** AppExchange là cái 'chợ' ứng dụng, không giúp ích gì cho việc debug hiệu năng.
> **B.** Setup Menu chỉ để cấu hình, không soi được log hay timeline thực thi của code.
> **D.** VS Code dùng để viết và deploy code, mặc dù có thể xem log nhưng không có giao diện phân tích Timeline trực quan như Dev Console.

**💡 Từ khóa ghi nhớ:** `Soi lỗi, soi hiệu năng, soi log real-time -> Developer Console là 'chân ái'.`

---

## Câu 77

**🔵 What should a developer use to implement an automatic Approval Process submission for Cases?**

- **A.** An Assignment Rule ❌
- **B.** Scheduled Apex ❌
- **C.** Process Builder ✅
- **D.** A Workflow Rule ❌

**📝 Dịch tiếng Việt:**
> Công cụ nào nên được sử dụng để tự động gửi yêu cầu phê duyệt (Approval Process submission) cho Case khi thỏa mãn điều kiện?

**💬 Giải thích gốc (English):**
> Process Builder is a declarative automation tool that allows you to create automated processes by defining a set of criteria and actions to be executed when those criteria are met.

**✅ Tại sao đáp án đúng:**
> Process Builder (C) hoặc Flow Builder (hiện đại) hỗ trợ hành động gọi 'Submit for Approval' cực kỳ trực quan và hoàn toàn không cần code.

**❌ Tại sao đáp án sai:**
> **A.** Assignment Rule chỉ dùng để chia Case/Lead cho Owner/Queue, không có tính năng gửi phê duyệt.
> **B.** Scheduled Apex dùng để lập lịch chạy định kỳ, không mang tính tức thời khi Case thỏa mãn điều kiện như Process Builder.
> **D.** Workflow Rule đời cũ không hề hỗ trợ hành động gửi bản ghi vào Approval Process.

**💡 Từ khóa ghi nhớ:** `Tự động gửi phê duyệt (Approval) -> Gọi tên Process Builder hoặc Flow.`

---

## Câu 78

**🔵 What are two ways a developer can get the status of an enqueued job for a class that implements the queueable interface? (Choose two.)**

- **A.** View the Apex Jobs Page ✅
- **B.** View the Apex Status Page ❌
- **C.** Query the AsyncApexJob object ✅
- **D.** View the Apex Flex Queue ❌

**📝 Dịch tiếng Việt:**
> Làm sao để kiểm tra trạng thái của một Queueable job đã được đẩy vào hàng đợi?

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
> A: Query bảng hệ thống `AsyncApexJob` bằng JobId. B: Vào trang 'Apex Jobs' trong Setup để xem trực quan.

**❌ Tại sao đáp án sai:**
> **C.** Flex Queue chỉ dành cho các Batch job đang ở trạng thái 'Holding'.
> **D.** Salesforce không có trang nào tên là 'apex status Page'.

**💡 Từ khóa ghi nhớ:** `Async Status = Query AsyncApexJob hoặc Setup -> Apex Jobs.`

---

## Câu 79

**🔵 The Review_c object has a lookup relationship up to the Job_Application_c object. The Job_Application_c object has a master-detail relationship up to the Position_c object. The relationship field names are based on the auto-populated defaults. What is the recommended way to display field data from the related Position_c record on a Visualforce page for a single Review_c record?**

- **A.** Use the Standard Controller for Review_c and cross-object Formula Fields on the Position_c object to display Position_c data. ❌
- **B.** Use the Standard Controller for Job_Application_c and a Controller Extension to query for Position_c data. ✅
- **C.** Use the Standard Controller for Job_Application_c and cross-object Formula Fields on the Review_c object to display Position_c data. ❌
- **D.** Use the Standard Controller for Review_c and expression syntax in the Page to display related Position_c data through the Job_Application_c object. ❌

**📝 Dịch tiếng Việt:**
> Review__c có quan hệ lookup với Job_Application__c. Job_Application__c lại có quan hệ Master-Detail với Position__c. Cách tốt nhất để hiển thị thông tin của Position__c trên trang Visualforce của một bản ghi Review__c là gì?

**✅ Tại sao đáp án đúng:**
> Visualforce cho phép hiển thị dữ liệu từ các object cha thông qua cú pháp merge field đi xuyên mối quan hệ (cross-object) lên tới 5 cấp. Do đó, cách tốt nhất không cần viết code là dùng Standard Controller của Review__c và gọi trực tiếp {!Review__c.Job_Application__r.Position__r.Name} trên trang (D). (Lưu ý: Đáp án B trong đề gốc là một sai sót dữ liệu vì nó đòi viết code extension rất cồng kềnh).

**❌ Tại sao đáp án sai:**
> **A.** Viết Formula Field trên Position__c để hiển thị data của chính nó là vô nghĩa.
> **B.** Dùng controller của Job_Application__c là sai ngữ cảnh của trang Review__c, viết extension query là quá phức tạp.
> **C.** Dùng controller của Job_Application__c là sai ngữ cảnh trang Review__c.

**💡 Từ khóa ghi nhớ:** `VF hiển thị cha của cha -> Dùng Standard Controller của con + cú pháp chấm '.' đi xuyên quan hệ.`

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
> Cho đoạn code sau thực thi trên môi trường có hơn 200 Account thuộc ngành 'Technology': [Code For Loop]. Khi code chạy, điều gì sẽ xảy ra với transaction Apex này?

**✅ Tại sao đáp án đúng:**
> Đáp án thực tế đúng về mặt kỹ thuật là B: Nếu chạy đồng bộ (synchronous), transaction chắc chắn sẽ OẰNG vì chạm giới hạn DML row hoặc DML statement. Lệnh 'update thisAccount;' nằm TRONG vòng lặp For chạy tới 150 lần, vượt quá giới hạn 150 DML statements cực nhanh chỉ với một vài tác vụ trigger kèm theo. (Mẹo thi: Đề bài gốc đánh dấu đáp án A là đúng, đây là một lỗi đề thi phổ biến cần cực kỳ lưu ý).

**❌ Tại sao đáp án sai:**
> **C.** Trường Is_Tech__c được gán bình thường, không gây ra lỗi thiếu query field vì đây là lệnh gán trị ghi chứ không phải đọc giá trị chưa query.
> **D.** Asynchronous context có giới hạn DML statement vẫn là 150, nên nó vẫn oẳng bình thường.

**💡 Từ khóa ghi nhớ:** `Mẹo thi PD1: Thấy DML trong For -> 100% dính Limit Exception. Đề thi thỉnh thoảng lỗi đáp án, cứ nhớ quy tắc bulkify!`

---

## Câu 81

**🔵 What is the data type returned by the following SOSL search?
[FIND 'Acme*' IN NAME FIELDS RETURNING Account, Opportunity];**

- **A.** List<List<Account>, List<Opportunity>> ❌
- **B.** Map<sObject, sObject> ❌
- **C.** List<List<sObject>> ✅
- **D.** Map<Id, sObject> ❌

**📝 Dịch tiếng Việt:**
> Kiểu dữ liệu nào được trả về bởi câu lệnh truy vấn SOSL sau đây?
[FIND 'Acme*' IN NAME FIELDS RETURNING Account, Opportunity];

**💬 Giải thích gốc (English):**
> The data type List<List<sObject>> is correct because SOSL searches return a List of Lists of sObjects. In this case, the search query is returning a List of sObjects that include both Account and Opportunity records.

**✅ Tại sao đáp án đúng:**
> SOSL dùng để tìm kiếm trên nhiều Object cùng lúc. Kết quả trả về luôn luôn là một List chứa các List của sObject: `List<List<sObject>>` (C). List ngoài chứa các object, mỗi List trong chứa các bản ghi của từng object cụ thể.

**❌ Tại sao đáp án sai:**
> **A.** Cú pháp định nghĩa kiểu dữ liệu lồng nhau sai quy chuẩn Apex.
> **B.** SOSL không trả về kiểu Map.
> **D.** SOSL trả về danh sách kết quả nhiều đối tượng chứ không trả về Map theo Id.

**💡 Từ khóa ghi nhớ:** `Thần chú SOSL: FIND -> Trả về List<List<sObject>>.`

---

## Câu 82

**🔵 A change set deployment from a sandbox to production fails due to a failure in a managed package unit test. The developer spoke with the managed package owner and they determined it is a false positive and can be ignored. What should the developer do to successfully deploy?**

- **A.** Select "Run local tests" to run all tests in the org that are not in the managed package. ✅
- **B.** Select "Fast Deploy" to run only the tests that are in the change set. ❌
- **C.** Select "Run local tests" to run only the tests that are in the change set. ❌
- **D.** Edit the managed package's unit test. ❌

**📝 Dịch tiếng Việt:**
> Khi deploy Change Set từ Sandbox lên Production bị thất bại do một lỗi test class nằm trong một Managed Package của bên thứ ba. Developer và đối tác xác định đây là lỗi cảnh báo giả và có thể bỏ qua. Developer nên làm gì để deploy thành công?

**💬 Giải thích gốc (English):**
> By running only local tests, the deployment will bypass the managed package unit test that caused the failure and proceed with deploying the rest of the changes in the change set.

**✅ Tại sao đáp án đúng:**
> Khi thực hiện deploy, chọn chế độ Test Level là 'Run local tests' (A). Chế độ này sẽ chạy toàn bộ các test class tự viết trong Org (local) và bỏ qua hoàn toàn các test class nằm trong các Managed Package cài thêm, giúp vượt qua lỗi.

**❌ Tại sao đáp án sai:**
> **B.** Fast Deploy chỉ dùng khi change set đã được validate thành công trước đó trong vòng 4 ngày, không giúp bỏ qua lỗi test.
> **C.** Run local tests chạy toàn bộ test local trong Org chứ không chỉ chạy riêng test có trong change set.
> **D.** Managed Package là code đã đóng gói và khóa, developer không có quyền chỉnh sửa test class của họ.

**💡 Từ khóa ghi nhớ:** `Lỗi test của Managed Package cài thêm -> Chọn Test Level = 'Run local tests' để bỏ qua.`

---

## Câu 83

**🔵 Which code displays the contents of a Visualforce page as a PDF?**

- **A.** <apex:page contentType="application/pdf"> ❌
- **B.** <apex:page renderAs="pdf"> ✅
- **C.** <apex:page renderAs="application/pdf"> ❌
- **D.** <apex:page contentType="pdf"> ❌

**📝 Dịch tiếng Việt:**
> Dùng mã nào để biến một trang Visualforce thành file PDF?

**💬 Giải thích gốc (English):**
> <apex:page renderAs="pdf">
> <!-- Contents of your Visualforce page -->
> </apex:page>

**✅ Tại sao đáp án đúng:**
> Thuộc tính `renderAs='pdf'` là cách chuẩn nhất để Salesforce render toàn bộ HTML trang VF sang PDF.

**❌ Tại sao đáp án sai:**
> **B.** contentType chỉ báo định dạng file cho trình duyệt nhưng không tự chuyển đổi giao diện HTML sang PDF được.
> **C.** Cú pháp giá trị của renderAs chỉ là 'pdf', không dài dòng kiểu mime-type như vậy.
> **D.** ContentType dùng cho việc download file, không dùng để render trang.

**💡 Từ khóa ghi nhớ:** `VF sang PDF -> renderAs='pdf'.`

---

## Câu 84

**🔵 What is a fundamental difference between a Master-Detail relationship and a Lookup relationship?**

- **A.** In a Master-Detail relationship, when a record of a master object is deleted, the detail records are not deleted. ❌
- **B.** In a Lookup relationship when the parent record is deleted, the child records are always deleted. ❌
- **C.** A Master-Detail relationship detail record inherits the sharing and security of its master record. ✅
- **D.** In a Lookup relationship, the field value is mandatory. ❌

**📝 Dịch tiếng Việt:**
> Sự khác biệt cơ bản giữa mối quan hệ Master-Detail và mối quan hệ Lookup là gì?

**💬 Giải thích gốc (English):**
> In a Master-Detail relationship, the detail record (child) is considered to be a subordinate of the master record (parent). The detail record inherits the sharing and security settings of its master record. This means that the detail record's access is determined by the access level of the master record.

**✅ Tại sao đáp án đúng:**
> Master-Detail ép buộc thằng con (Detail) phải kế thừa hoàn toàn quyền Sharing & Security từ thằng cha (Master).

**❌ Tại sao đáp án sai:**
> **A.** Trong Lookup, khi cha bị xóa, con thường giữ nguyên (mặc định xóa link cha chứ không xóa con).
> **C.** Ngược lại, trong Master-Detail, cha đi đời thì con cũng bay màu (Cascade delete).
> **D.** Lookup field có thể để trống (Optional), Master-Detail mới bắt buộc phải có giá trị.

**💡 Từ khóa ghi nhớ:** `Master-Detail = Ký sinh. Lookup = Bạn bè.`

---

## Câu 85

**🔵 A developer wants multiple test classes to use the same set of test data. How should the developer create the test data?**

- **A.** Reference a test utility class in each test class. ✅
- **B.** Define variables for test records in each test class. ❌
- **C.** Create a Test Setup method for each test class. ❌
- **D.** Use the SeeAllData=true annotation in each test class. ❌

**📝 Dịch tiếng Việt:**
> Developer muốn nhiều class test khác nhau có thể dùng chung một bộ dữ liệu test mẫu. Developer nên tạo dữ liệu test này bằng cách nào?

**💬 Giải thích gốc (English):**
> Create a test utility class that contains methods to create and insert the common test data.
> Each test class can then reference this test utility class and call its methods to set up the required test data.

**✅ Tại sao đáp án đúng:**
> Tạo một 'Test Utility Class' (A) chứa các hàm public static chuyên tạo dữ liệu mẫu (ví dụ: createAccounts()). Mỗi class test chỉ cần gọi hàm từ class utility này để lấy data test cực kỳ sạch sẽ và dễ bảo trì.

**❌ Tại sao đáp án sai:**
> **B.** Khai báo thủ công ở mỗi class test gây lặp code, cực kỳ khó bảo trì khi schema thay đổi.
> **C.** @TestSetup chỉ tạo dữ liệu dùng chung trong NỘI BỘ 1 class test đó, các class test khác không 'với' tới được.
> **D.** SeeAllData=true làm test truy cập dữ liệu thật của Org, cực kỳ không khuyến khích vì làm test mất tính độc lập và dễ tạch.

**💡 Từ khóa ghi nhớ:** `Dùng chung data test giữa các Class -> Tạo Test Utility Class.`

---

## Câu 86

**🔵 Which two statements are true about using the @testSetup annotation in an Apex test class? (Choose two.)**

- **A.** The @testSetup annotation cannot be used when the @isTest(SeeAllData=True) annotation is used. ✅
- **B.** Test data is inserted once for all test methods in a class. ✅
- **C.** Records created in the @testSetup method cannot be updates in individual test methods. ❌
- **D.** The @testSetup method is automatically executed before each test method in the test class is executed. ❌

**📝 Dịch tiếng Việt:**
> Hai phát biểu nào đúng về annotation @testSetup?

**💬 Giải thích gốc (English):**
> The @testSetup annotation is used to set up test data that will be used by all test methods within a class. This helps to avoid redundant data creation and improves test efficiency.
> Test setup methods are supported only with the default data isolation mode for a test class. If the test class or a test method has access to organization data by using the @isTest(SeeAllData=true) annotation, test setup methods aren’t supported in this class.

**✅ Tại sao đáp án đúng:**
> E: Data trong setup chỉ insert 1 lần cho cả class dùng chung, giúp test chạy cực nhanh. A: Nếu dùng SeeAllData=true (truy cập data thật) thì Salesforce cấm dùng @testSetup để đảm bảo tính độc lập của test.

**❌ Tại sao đáp án sai:**
> **B.** Dữ liệu tạo trong setup hoàn toàn có thể được update bởi các test method lẻ, nhưng sau mỗi method nó sẽ tự rollback về trạng thái ban đầu.
> **C.** Nó chỉ chạy DUY NHẤT một lần cho toàn bộ class, không phải chạy lặp lại cho từng method.
> **D.** Câu này thiếu ngữ cảnh rõ ràng, nhưng ý E và A là những đặc tính cốt lõi nhất được hỏi trong PD1.

**💡 Từ khóa ghi nhớ:** `@testSetup = Tiết kiệm thời gian + Data dùng chung cho toàn bộ class.`

---

## Câu 87

**🔵 Which two platform features align to the Controller portion of MVC architecture? (Choose two.)**

- **A.** Process Builder actions ✅
- **B.** Workflow rules ✅
- **C.** Standard objects ❌
- **D.** Date fields ❌

**📝 Dịch tiếng Việt:**
> Hai tính năng nào của Salesforce đóng vai trò là tầng 'Controller' trong kiến trúc MVC? (Chọn 2)

**💬 Giải thích gốc (English):**
> In the Model-View-Controller (MVC) architecture, the Controller is responsible for handling user input and processing data. In Salesforce, both Process Builder actions and Workflow rules can be considered as part of the Controller layer because they automate and process data based on certain criteria and user input.

**✅ Tại sao đáp án đúng:**
> Trong mô hình MVC của Salesforce, tầng Controller xử lý logic nghiệp vụ và điều khiển dữ liệu. Cả Process Builder actions (A) và Workflow rules (B) đều chứa các logic điều khiển, tự động hóa cập nhật dữ liệu nên thuộc tầng Controller.

**❌ Tại sao đáp án sai:**
> **C.** Standard objects đại diện cho bảng dữ liệu vật lý lưu trữ, thuộc tầng Model.
> **D.** Fields (các trường dữ liệu) định nghĩa cấu trúc dữ liệu, thuộc tầng Model.

**💡 Từ khóa ghi nhớ:** `MVC Salesforce: Model = Objects/Fields. View = Visualforce/LWC. Controller = Apex/Workflows/Flows.`

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
> Làm thế nào lập trình viên có thể sửa lỗi biên dịch trong đoạn mã trên?

**💬 Giải thích gốc (English):**
> Make the isActive method public, it can now be accessed from other classes, and the Calculator class will be able to call the isActive method on the StatusFetcher instance without any compilation errors.

**✅ Tại sao đáp án đúng:**
> Method `isActive()` đang để `private`. Class Calculator muốn gọi nó thì mày phải đổi modifier sang `public` (hoặc global).

**❌ Tại sao đáp án sai:**
> **B.** inherited sharing không làm thay đổi quyền visibility (tầm nhìn) của một private method.
> **C.** Làm method docalculations thành private không giúp nó 'thấy' được method của class khác.
> **D.** Thay đổi sharing model của Calculator cũng không giải quyết được vấn đề Access Modifier của StatusFetcher.

**💡 Từ khóa ghi nhớ:** `OOP: Muốn thằng khác dùng đồ của mình -> Để Public.`

---

## Câu 89

**🔵 Which statement generates a list of Leads and Contacts that have a field with the phrase 'ACME'?**

- **A.** List <sObject> searchList = [FIND "*ACME*" IN ALL FIELDS RETURNING Contact, Lead]; ❌
- **B.** List<List <sObject>> searchList = [FIND "*ACME*" IN ALL FIELDS RETURNING Contact, Lead]; ✅
- **C.** List<List <sObject>> searchList = [SELECT Name, ID FROM Contact, Lead WHERE Name like ‘%ACME%’]; ❌
- **D.** Map <sObject> searchList = [FIND "*ACME*" IN ALL FIELDS RETURNING Contact, Lead]; ❌

**📝 Dịch tiếng Việt:**
> Câu lệnh nào lấy danh sách cả Lead và Contact có chứa từ khóa 'ACME'?

**💬 Giải thích gốc (English):**
> SOSL searches return a List of Lists of sObjects List<List<sObject>>.

**✅ Tại sao đáp án đúng:**
> Để tìm trên nhiều object, dùng SOSL (`FIND`). Kết quả luôn là `List<List<sObject>>`.

**❌ Tại sao đáp án sai:**
> **A.** SOSL không trả về Map.
> **C.** SOQL không thể query nhiều object theo kiểu liệt kê dấu phẩy như vậy.
> **D.** Kiểu dữ liệu trả về bị thiếu một tầng List lồng.

**💡 Từ khóa ghi nhớ:** `SOSL Thần chú: FIND {Text} -> List<List<sObject>>.`

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
> Mark Required ở cấp độ 'Field Definition' (Universal Required) là mạnh nhất. Nó bắt buộc ở mọi nơi: giao diện (UI), API, Code Apex, Data Loader. Đây là tầng bảo vệ dữ liệu thấp nhất và hiệu quả nhất.

**❌ Tại sao đáp án sai:**
> **A.** Page Layout chỉ có tác dụng trên giao diện, nếu dùng Data Loader hoặc Code thì vẫn bỏ trống field được.
> **B.** Default value không bắt người dùng phải 'chọn' theo ý họ, nó chỉ tự điền thôi và có thể bị xóa trắng nếu không có ràng buộc Required.
> **D.** Validation Rule cũng hiệu quả nhưng tốn tài nguyên xử lý hơn so với việc định nghĩa trực tiếp trên field.

**💡 Từ khóa ghi nhớ:** `Data Integrity: Field Definition > Validation Rule > Page Layout.`

---

## Câu 91

**🔵 As part of a data cleanup strategy, AW Computing wants to proactively delete associated opportunity records when the related Account is deleted. Which automation tool should be used to meet this business requirement?**

- **A.** Scheduled job ❌
- **B.** Record-triggered flow ✅
- **C.** Workflow rules ❌
- **D.** Outbound messaging ❌

**📝 Dịch tiếng Việt:**
> AW Computing muốn tự động xóa các Opportunity liên quan khi một Account bị xóa. Công cụ tự động hóa nào nên được sử dụng?

**💬 Giải thích gốc (English):**
> With Record-Triggered Flows, you can automate actions based on changes to record data, including deleting related records.

**✅ Tại sao đáp án đúng:**
> Record-Triggered Flow với sự kiện 'A record is deleted' là công cụ khai báo mạnh mẽ nhất hiện nay để xử lý logic trước hoặc sau khi xóa, bao gồm cả việc xóa các bản ghi liên quan (Cascade Delete thủ công).

**❌ Tại sao đáp án sai:**
> **A.** Scheduled Job chạy định kỳ, không mang tính tức thời (proactive) ngay khi Account bị xóa.
> **C.** Process Builder không hỗ trợ sự kiện xóa (Delete).
> **D.** Workflow Rules chỉ hỗ trợ Create/Edit, không chơi với sự kiện Delete.

**💡 Từ khóa ghi nhớ:** `Khi cần xử lý logic lúc XÓA (Delete) mà không muốn viết Code -> Chọn Record-Triggered Flow.`

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
> Đoạn mã Anonymous Block trên xử lý cập nhật 50,000 Case. Với môi trường có hơn 10,000 bản ghi, điều gì sẽ xảy ra?

**💬 Giải thích gốc (English):**
> Total number of records processed as a result of DML statements, Approval.process, or database.emptyRecycleBin: 10,000
> If there are more than 10,000 Case records in the environment, the code may hit the DML row limit and result in a "Too many DML rows: 10001" exception.
> Reference:
> 1. Execution Governors and Limits
> https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apexgov.htm
> 2. Exceptions that Can’t be Caught(LimitException)
> https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_exception_statements.htm

**✅ Tại sao đáp án đúng:**
> Giới hạn DML Row trong một transaction là 10,000. Đoạn code này cố gắng update tới 50,000 bản ghi trong 1 nốt nhạc, chắc chắn sẽ 'ăn' LimitException và oẳng luôn cả transaction.

**❌ Tại sao đáp án sai:**
> **A.** Governor Limit Exception (như LimitException) là loại 'bất trị', Try/Catch KHÔNG BAO GIỜ bắt được nó.
> **C.** Dù bắt được DML Exception thì transaction vẫn tạch vì dính limit 10k bản ghi trước khi kịp chạy Database.update thành công.
> **D.** Không bao giờ thành công nổi với cái LIMIT 50,000 to đùng kia.

**💡 Từ khóa ghi nhớ:** `Governor Limits = Cảnh sát giao thông. Mày vi phạm là nó 'cẩu xe' (Exception), không có Try/Catch nào xin xỏ được đâu.`

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
> B: Phương thức Setter là bắt buộc để truyền dữ liệu người dùng nhập từ giao diện (VF Page) ngược về Controller xử lý. C: Salesforce không hề đảm bảo thứ tự thực thi giữa các phương thức Getter hay Setter khi trang tải, do đó cấm viết code logic phụ thuộc vào thứ tự chạy của chúng.

**❌ Tại sao đáp án sai:**
> **A.** Setter chỉ cần khai báo public hoặc global tùy thuộc vào phạm vi sử dụng của controller, không bắt buộc luôn là global.
> **D.** Ngược lại, Getter dùng để truyền dữ liệu từ Controller ra hiển thị trên giao diện (Page), chứ không phải ngược lại.

**💡 Từ khóa ghi nhớ:** `Getter = Đẩy dữ liệu RA Page. Setter = Hốt dữ liệu VÀO Controller. Thứ tự chạy ngẫu nhiên!`

---

## Câu 94

**🔵 A Platform Developer needs to write an Apex method that will only perform an action if a record is assigned to a specific Record Type. Which two options allow the developer to dynamically determine the ID of the required Record Type by its name? (Choose two.)**

- **A.** Make an outbound web services call to the SOAP API. ❌
- **B.** Hardcode the ID as a constant in an Apex class. ❌
- **C.** Use the getRecordTypeInfosByName() method in the DescribeSObjectResult class. ✅
- **D.** Execute a SOQL query on the RecordType object. ✅

**📝 Dịch tiếng Việt:**
> Developer cần viết code Apex chỉ thực hiện hành động khi bản ghi thuộc một Record Type cụ thể. Hai cách nào giúp lấy Record Type ID động theo Tên (Name) của nó? (Chọn 2)

**💬 Giải thích gốc (English):**
> Using the getRecordTypeInfosByName() method allows you to dynamically retrieve the Record Type ID by its name without hardcoding.
> Executing a SOQL query on the RecordType object is another way to dynamically determine the Record Type ID.

**✅ Tại sao đáp án đúng:**
> C: Sử dụng hàm getRecordTypeInfosByName() của lớp DescribeSObjectResult để lấy mô tả Record Type trực tiếp từ bộ nhớ RAM cực nhanh. D: Thực hiện câu truy vấn SOQL trên đối tượng hệ thống RecordType lọc theo DeveloperName hoặc Name để lấy ID.

**❌ Tại sao đáp án sai:**
> **A.** Gọi API SOAP ra ngoài chỉ để lấy 1 cái ID Record Type là quá cồng kềnh và điên rồ.
> **B.** Hardcode ID là tối kỵ vì ID ở Sandbox và Production sẽ khác nhau, gây lỗi khi deploy.

**💡 Từ khóa ghi nhớ:** `Lấy Record Type ID: 1. Schema Describe (getRecordTypeInfosByName) - Khuyến nghị; 2. SOQL RecordType.`

---

## Câu 95

**🔵 Which situation prevents a developer from setting sharing rules for a custom object?**

- **A.** The object's Sharing Settings is set to Public Read/Write. ❌
- **B.** The object is on the detail side of a Master-Detail relationship. ✅
- **C.** The developer is not a System Administrator. ❌
- **D.** The object is referenced in an Owner field of a Master-Detail relationship. ❌

**📝 Dịch tiếng Việt:**
> Trường hợp nào sau đây ngăn cản developer thiết lập Sharing Rules (luật chia sẻ quyền truy cập) cho một Custom Object?

**💬 Giải thích gốc (English):**
> Cannot set explicit sharing rules for custom objects that are on the detail side of a Master-Detail relationship.

**✅ Tại sao đáp án đúng:**
> Khi Custom Object đó nằm ở bên Detail (con) của mối quan hệ Master-Detail (B). Thằng con sẽ bị tước quyền tự quyết và bắt buộc phải kế thừa hoàn toàn cấu hình bảo mật Sharing từ thằng cha (Master).

**❌ Tại sao đáp án sai:**
> **A.** Public Read/Write là cấu hình OWD mặc định, hoàn toàn không ngăn cản việc viết sharing rule sau đó nếu cần thu hẹp/mở rộng.
> **C.** Chỉ cần có quyền Customize Application (thường là Admin hoặc Dev có quyền) là set được, không bắt buộc phải là System Admin tối cao.
> **D.** Không có khái niệm 'Owner field' của mối quan hệ Master-Detail vì bản ghi Detail không hề có trường Owner riêng.

**💡 Từ khóa ghi nhớ:** `Detail trong Master-Detail = Ký sinh bảo mật. Không có Owner riêng, không có Sharing Rule riêng!`

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
> Cho ví dụ xử lý Exception sau: [Class myClass]. Kết quả hiển thị trong debug log khi có lỗi QueryException xảy ra trong hàm aQuery là gì?

**💬 Giải thích gốc (English):**
> 1. Try Block: The code attempts to execute the SOQL query inside the try block and logs “Querying Accounts.”.
> 2. Catch Blocks: If a QueryException occurs, it will be caught by the catch(QueryException eX) block, logging “Query Exception.”.
> 3. Finally Block: The finally block will always execute, logging “Done.”.

**✅ Tại sao đáp án đúng:**
> Khi truy vấn SOQL thất bại (QueryException), hệ thống ném ra QueryException chuẩn. Lỗi sẽ đi qua block catch đầu tiên (CustomException - không khớp vì đây là class con tự viết) và rơi trúng block catch thứ hai catch(QueryException eX), in ra 'Query Exception.'. Cuối cùng, block finally luôn luôn chạy và in ra 'Done.' (D).

**❌ Tại sao đáp án sai:**
> **A.** Thiếu chữ 'Done.' của block finally vốn dĩ bắt buộc phải chạy.
> **B.** QueryException chuẩn của hệ thống không thể bị bắt bởi lớp CustomException tự chế được.
> **C.** Bị bắt sai block catch.

**💡 Từ khóa ghi nhớ:** `Finally block: Dù code chạy ngon hay oẳng dính Exception, block finally VẪN PHẢI CHẠY!`

---

## Câu 97

**🔵 Universal Containers wants Opportunities to no longer be editable when reaching the Closed/Won stage. Which two strategies can a developer use to accomplish this? (Choose two.)**

- **A.** Use an after-save flow. ❌
- **B.** Use a validation rule. ✅
- **C.** Use the Process Automation Settings. ❌
- **D.** Use a trigger. ✅

**📝 Dịch tiếng Việt:**
> Universal Containers muốn các Opportunity khi đã chuyển sang trạng thái Closed/Won thì KHÔNG cho phép người dùng chỉnh sửa nữa. Hai giải pháp nào hỗ trợ việc này? (Chọn 2)

**💬 Giải thích gốc (English):**
> Create a validation rule on the Opportunity object that checks the stage value. If the stage is Closed/Won, the validation rule should prevent any updates or changes to the Opportunity.
> Using a trigger can be an option.

**✅ Tại sao đáp án đúng:**
> B: Sử dụng Validation Rule kiểm tra điều kiện IsWon = true và PRIORVALUE(StageName) = 'Closed/Won' để chặn lưu mọi thay đổi. D: Viết trigger 'before update' trên Opportunity check trạng thái cũ và mới để gọi addError() chặn lưu.

**❌ Tại sao đáp án sai:**
> **A.** After-save flow chỉ chạy sau khi bản ghi đã lưu thành công vào database, không có tính năng chặn (block) cập nhật như Validation Rule.
> **C.** Process Automation Settings cấu hình chung cho hệ thống tự động hóa, không chứa logic chặn chỉnh sửa bản ghi cụ thể.

**💡 Từ khóa ghi nhớ:** `Chặn chỉnh sửa bản ghi (Read-only khóa cứng) -> 1. Validation Rule (No-code); 2. Trigger addError (Code).`

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
> Khi sử dụng Data Loader (dù là Bulk API hay SOAP API) để nạp dữ liệu, Salesforce coi đây là các thao tác DML chuẩn. Do đó, tất cả các trigger liên quan (Before/After Insert/Update) đều sẽ được kích hoạt.

**❌ Tại sao đáp án sai:**
> **A.** Mass Address update tool là công cụ hệ thống, đôi khi không kích hoạt trigger thông thường tùy vào phiên bản và cấu hình.
> **C.** Lead Conversion chủ yếu kích hoạt trigger trên bản ghi được tạo/cập nhật nhưng cơ chế của nó phức tạp và ưu tiên các event đặc thù của Conversion hơn là Before trigger mặc định như Data Loader.
> **D.** Thay đổi metadata (đổi tên picklist) không phải là thao tác trên data, nên trigger sẽ không nổ.

**💡 Từ khóa ghi nhớ:** `Data Loader = DML = Trigger nổ banh xác. Cứ nhớ thế cho nhanh!`

---

## Câu 99

**🔵 The values 'High', 'Medium', and 'Low' are identified as common values for multiple picklists across different objects. What is an approach a developer can take to streamline maintenance of the picklists and their values, while also restricting the values to the ones mentioned above?**

- **A.** Create the Picklist on each object and use a Global Picklist Value Set containing the values. ✅
- **B.** Create the Picklist on each object as a required field and select "Display values alphabetically, not in the order entered". ❌
- **C.** Create the Picklist on each object and add a validation rule to ensure data integrity. ❌
- **D.** Create the Picklist on each object and select "Restrict picklist to the values defined in the value set". ❌

**📝 Dịch tiếng Việt:**
> Các giá trị 'High', 'Medium', 'Low' được dùng chung cho nhiều field picklist ở nhiều object khác nhau. Làm sao để quản lý đống này một cách tập trung và chuyên nghiệp nhất?

**💬 Giải thích gốc (English):**
> By creating a Global Picklist Value Set with the common values 'High', 'Medium', and 'Low', you can then use this value set to populate the picklist fields on different objects.

**✅ Tại sao đáp án đúng:**
> D đúng vì Global Picklist Value Set cho phép mày định nghĩa bộ giá trị một nơi và dùng nhiều nẻo. Sau này muốn thêm giá trị 'Very High' thì chỉ cần sửa một chỗ là cả org cùng hưởng.

**❌ Tại sao đáp án sai:**
> **A.** Cái này chỉ là sắp xếp thứ tự hiển thị, chả giúp ích gì cho việc bảo trì tập trung cả.
> **B.** Validation rule trên mỗi object là cách làm thủ công, tốn sức và dễ sai sót khi có thay đổi.
> **C.** Cái này chỉ giới hạn giá trị cho riêng cái field đó, nếu có 10 object thì mày phải làm 10 lần. Quá mệt!

**💡 Từ khóa ghi nhớ:** `Mẹo PD1: Dùng chung giá trị cho nhiều picklist = Global Picklist Value Set.`

---

## Câu 100

**🔵 Which option should a developer use to create 500 Accounts and make sure that duplicates are not created for existing Account Sites?**

- **A.** Sandbox template ❌
- **B.** Data Loader ❌
- **C.** Data Import Wizard ✅
- **D.** Salesforce-to-Salesforce ❌

**📝 Dịch tiếng Việt:**
> Lựa chọn nào mà lập trình viên nên sử dụng để tạo mới 500 Account và đảm bảo rằng không tạo ra các bản ghi trùng lặp đối với các Account Site đã tồn tại?

**💬 Giải thích gốc (English):**
> The Data Import Wizard in Salesforce provides an easy-to-use interface for importing data, and it has a built-in duplicate management feature that allows you to prevent the creation of duplicate records during the import process.

**✅ Tại sao đáp án đúng:**
> Data Import Wizard (C) là công cụ no-code chuẩn của Salesforce, tích hợp sẵn tính năng đối chiếu và chặn bản ghi trùng lặp (Duplicate Management) dựa trên các tiêu chí như Name, Site cực kỳ tiện lợi cho số lượng bản ghi dưới 50,000.

**❌ Tại sao đáp án sai:**
> **A.** Sandbox template dùng để chọn lọc dữ liệu khi tạo/refesh Sandbox, không liên quan đến việc nạp và chặn trùng.
> **B.** Data Loader hỗ trợ nạp số lượng lớn nhưng không có tính năng so khớp và tự động chặn trùng lặp trực tiếp lúc import như Wizard.
> **D.** Salesforce-to-Salesforce là tính năng kết nối chia sẻ dữ liệu giữa 2 Org khác nhau, không phải công cụ import dữ liệu thông thường.

**💡 Từ khóa ghi nhớ:** `Import dưới 50k bản ghi + Chặn trùng lặp không code -> Data Import Wizard.`

---

## Câu 101

**🔵 How should a developer write unit tests for a private method in an Apex class?**

- **A.** Add a test method in the Apex class. ❌
- **B.** Mark the Apex class as global. ❌
- **C.** Use the SeeAllData annotation. ❌
- **D.** Use the TestVisible annotation. ✅

**📝 Dịch tiếng Việt:**
> Làm thế nào để lập trình viên có thể viết unit tests cho một private method trong một Apex class?

**💬 Giải thích gốc (English):**
> The TestVisible annotation allows you to expose private methods and variables to be accessed in test classes.

**✅ Tại sao đáp án đúng:**
> Annotation @TestVisible cho phép các class test truy cập được vào các member (variable/method) vốn dĩ là private hoặc protected mà không cần phải thay đổi modifier của chúng sang public.

**❌ Tại sao đáp án sai:**
> **B.** Global làm lộ code ra toàn hệ thống, cực kỳ thiếu bảo mật chỉ để phục vụ testing.
> **C.** SeeAllData liên quan đến việc truy cập dữ liệu trong Org, không liên quan đến khả năng truy cập private method.
> **D.** Sai practice. Code logic và Code test phải tách biệt hoàn toàn để đảm bảo tính đóng gói.

**💡 Từ khóa ghi nhớ:** `Keyword: Private method test -> @TestVisible.`

---

## Câu 102

**🔵 A company has a custom object named Region. Each Account in Salesforce can only be related to one Region at a time, but this relationship is optional. Which type of relationship should a developer use to relate an Account to a Region?**

- **A.** Parent-Child ❌
- **B.** Hierarchical ❌
- **C.** Lookup ✅
- **D.** Master-Detail ❌

**📝 Dịch tiếng Việt:**
> Một công ty có đối tượng tùy chỉnh tên là Region. Mỗi Account trong Salesforce chỉ có thể liên kết với một Region tại một thời điểm, nhưng liên kết này là không bắt buộc (tùy chọn). Loại mối quan hệ nào nên được sử dụng?

**💬 Giải thích gốc (English):**
> A Lookup relationship allows each Account to be optionally related to one Region at a time without enforcing strict dependency rules, which fits the requirement of an optional relationship.

**✅ Tại sao đáp án đúng:**
> Mối quan hệ Lookup (C) là lựa chọn hoàn hảo vì nó liên kết hai đối tượng một cách lỏng lẻo và cho phép trường liên kết bị bỏ trống (optional). Nếu dùng Master-Detail, trường liên kết sẽ bị bắt buộc phải điền giá trị.

**❌ Tại sao đáp án sai:**
> **A.** Parent-Child là tên gọi chung của mối quan hệ cha-con, không phải là tên một kiểu trường quan hệ trong Salesforce.
> **B.** Hierarchical (mối quan hệ phân cấp) là một loại Lookup đặc biệt chỉ dùng riêng cho đối tượng User để liên kết User này với User khác.
> **D.** Master-Detail là quan hệ chặt chẽ, bắt buộc phải có giá trị ở con và không cho phép để trống trường liên kết.

**💡 Từ khóa ghi nhớ:** `Mối quan hệ 1-Nhiều + Tùy chọn (Optional) cho phép trống -> Dùng Lookup Relationship.`

---

## Câu 103

**🔵 An Account trigger updates all related Contacts and Cases each time an Account is saved using the following two DML statements: update allContacts; update allCases; What is the result if the Case update exceeds the governor limit for maximum number of DML records?**

- **A.** The Account save fails and no Contacts or Cases are updated. ✅
- **B.** The Account save succeeds and no Contacts or Cases are updated. ❌
- **C.** The Account save succeeds, Contacts are updated, but Cases are not. ❌
- **D.** The Account save is retried using a smaller trigger batch size. ❌

**📝 Dịch tiếng Việt:**
> Một trigger trên Account cập nhật tất cả các Contact và Case liên quan mỗi khi Account được lưu bằng 2 câu lệnh DML: 'update allContacts;' và 'update allCases;'. Điều gì xảy ra nếu việc cập nhật Case vượt quá giới hạn (governor limit) về số lượng bản ghi DML tối đa?

**💬 Giải thích gốc (English):**
> If the Case update exceeds the governor limit for the maximum number of DML records, the entire transaction is rolled back, causing the Account save to fail and preventing any updates to Contacts or Cases.

**✅ Tại sao đáp án đúng:**
> Trong Salesforce, mọi hành động diễn ra trong cùng một transaction. Nếu có bất kỳ lỗi Governor Limit nào xảy ra ở bất kỳ bước nào (ví dụ ở lệnh update Case), toàn bộ transaction sẽ bị rollback (hủy bỏ) hoàn toàn (A). Không có Account, Contact hay Case nào được lưu hết để đảm bảo toàn vẹn dữ liệu.

**❌ Tại sao đáp án sai:**
> **B.** Account lưu thất bại hoàn toàn chứ không phải lưu thành công.
> **C.** Salesforce không cho phép lưu một nửa (Contacts được lưu còn Cases thì không) khi có unhandled exception xảy ra trong transaction.
> **D.** Hệ thống không tự động thử lại (retry) với kích thước lô nhỏ hơn khi dính lỗi Governor Limit.

**💡 Từ khóa ghi nhớ:** `Transaction Rule: Một thằng oẳng -> Cả lũ oẳng theo (Rollback sạch sẽ)!`

---

## Câu 104

**🔵 A developer wants to invoke an outbound message when a record meets a specific criteria. Which three features satisfy this use case? (Choose three.)**

- **A.** Process builder can be used to check the record criteria and send an outbound message with Apex Code. ✅
- **B.** Process builder can be used to check the record criteria and send an outbound message without Apex Code. ❌
- **C.** Approval Process has the capability to check the record criteria and send an outbound message without Apex Code. ✅
- **D.** Workflows can be used to check the record criteria and send an outbound message. ✅
- **E.** Visual Workflow can be used to check the record criteria and send an outbound message without Apex Code. ❌

**📝 Dịch tiếng Việt:**
> Cần gửi Outbound Message khi bản ghi thỏa mãn điều kiện. Hai tính năng nào hỗ trợ việc này?

**💬 Giải thích gốc (English):**
> Outbound messaging allows you to specify that changes to fields within Salesforce can cause messages with field values to be sent to designated external servers.
> Outbound messaging is part of the workflow rule functionality in Salesforce. Workflow rules watch for specific kinds of field changes and trigger automatic Salesforce actions, such as sending email alerts, creating task records, or sending an outbound message. You can associate outbound messages with flows, workflow rules, approval processes, or entitlement processes.

**✅ Tại sao đáp án đúng:**
> C: Approval Process hỗ trợ Outbound Message trong các hành động phê duyệt. D: Flow Builder hiện nay đã hỗ trợ gọi Outbound Message trực tiếp thông qua Action cực kỳ xịn xò.

**❌ Tại sao đáp án sai:**
> **A.** Process Builder KHÔNG hỗ trợ Outbound Message trực tiếp. Muốn dùng phải gọi qua Apex (@InvocableMethod) hoặc Workflow.
> **B.** Next Best Action là tool gợi ý cho người dùng, không phải tool tự động hóa backend để gửi tin nhắn ra ngoài hệ thống.

**💡 Từ khóa ghi nhớ:** `Outbound Message: Workflow (xưa rồi), Approval Process, Flow (vua bây giờ).`

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
> Kết quả của việc insert cùng 1 biến acct 201 lần trong vòng lặp là gì?

**💬 Giải thích gốc (English):**
> The exception prevents any accounts from being inserted, and the final outcome is that 0 Accounts are inserted.
> To avoid hitting the governor limit, a better approach would be to collect the accounts in a collection (such as a List<Account>) during the loop and then perform a single bulk insert after the loop completes.

**✅ Tại sao đáp án đúng:**
> Lần 2 sẽ báo lỗi 'Record already has ID'. Vì không có catch lỗi, cả transaction rollback sạch sẽ.

**❌ Tại sao đáp án sai:**
> **A.** Vượt limit 150 DML và lỗi 'Already has ID' sẽ giết chết transaction.
> **C.** Lỗi ngay từ lần thứ 2 thì không thể tới 200 được.
> **D.** Dù lần 1 thành công nhưng lần 2 lỗi làm rollback cả lần 1.

**💡 Từ khóa ghi nhớ:** `DML in Loop = Bad. Insert record with ID = Bad. Cả 2 cộng lại = 0 bản ghi.`

---

## Câu 106

**🔵 A developer writes a single trigger on the Account object on the after insert and after update events. A workflow rule modifies a field every time an Account is created or updated. How many times will the trigger fire if a new Account is inserted, assuming no other automation logic is implemented on the Account?**

- **A.** 8 ❌
- **B.** 1 ❌
- **C.** 4 ❌
- **D.** 2 ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên viết một trigger duy nhất trên Account ở hai sự kiện 'after insert' và 'after update'. Một workflow rule sẽ thay đổi giá trị một trường mỗi khi Account được tạo hoặc cập nhật. Hỏi trigger sẽ nổ bao nhiêu lần khi chèn mới 1 Account (không có tự động hóa nào khác)?

**💬 Giải thích gốc (English):**
> When a new Account is inserted, the following sequence of events occurs:
> 1. The Account is inserted, triggering the after insert event.
> 2. The workflow rule modifies a field on the Account, which triggers an after update event.
> So, the trigger will fire twice:
> 1. Once for the after insert event.
> 2. Once for the after update event caused by the workflow rule.

**✅ Tại sao đáp án đúng:**
> Trigger sẽ nổ đúng 2 lần (D). Lần 1: Khi Account mới được chèn vào, trigger nổ ở sự kiện 'after insert'. Lần 2: Sau khi insert, workflow rule kích hoạt cập nhật trường, hệ thống thực hiện save ngầm khiến trigger nổ lần 2 ở sự kiện 'after update'.

**❌ Tại sao đáp án sai:**
> **A.** Số lần nổ quá nhiều, không khớp với số vòng đời lưu bản ghi.
> **B.** Sai vì workflow update trường sẽ kích hoạt trigger nổ thêm một lần nữa.
> **C.** Sai số lượng vòng đời thực tế.

**💡 Từ khóa ghi nhớ:** `Insert mới -> Trigger after insert nổ -> Workflow chạy -> Trigger after update nổ lần nữa (Tổng cộng = 2).`

---

## Câu 107

**🔵 A developer must provide custom user interfaces when users edit a Contact in either Salesforce Classic or Lightning Experience. What should the developer use to override the Contact's Edit button and provide this functionality?**

- **A.** A Lightning page in Salesforce Classic and a Visualforce page in Lightning Experience ❌
- **B.** A Visualforce page in Salesforce Classic and a Lightning page in Lightning Experience ❌
- **C.** A Visualforce page in Salesforce Classic and a Lightning component in Lightning Experience ✅
- **D.** A Lightning component in Salesforce Classic and a Lightning component in Lightning Experience ❌

**📝 Dịch tiếng Việt:**
> Ghi đè nút Edit của Contact cho cả Classic và Lightning? (Chọn 1)

**💬 Giải thích gốc (English):**
> Visualforce pages are used to create custom user interfaces in Salesforce Classic, and Lightning components are used to create custom user interfaces in Lightning Experience.

**✅ Tại sao đáp án đúng:**
> Classic bắt buộc dùng Visualforce. Lightning Experience khuyến khích dùng Lightning Component (Aura/LWC) để tối ưu trải nghiệm.

**❌ Tại sao đáp án sai:**
> **A.** Classic không hỗ trợ Lightning page để làm giao diện tùy chỉnh cho nút bấm.
> **B.** Lightning page dùng để xây dựng cấu trúc trang, không dùng để ghi đè nút chức năng như Edit button.
> **C.** Classic không hỗ trợ hiển thị mượt mà Lightning component khi ghi đè nút Edit trực tiếp.

**💡 Từ khóa ghi nhớ:** `Override: Classic -> Visualforce; Lightning -> Lightning Component.`

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
> Kết quả của các câu debug log trong testMethod3 là gì khi tạo dữ liệu test bằng phương thức @testSetup trong đoạn code dưới đây? [Code @testSetup]

**💬 Giải thích gốc (English):**
> The debug statements in testMethod3 will display the phone numbers of the accounts created in the test setup method. Since the accounts are created in a loop where the phone numbers are incremented, the expected result is Account0.Phone=333-8780, Account1.Phone=333-8781, making this choice correct.

**✅ Tại sao đáp án đúng:**
> Kết quả là 'Account0.Phone=333-8780, Account1.Phone=333-8781' (C). Dữ liệu tạo trong `@testSetup` là bất biến đối với các phương thức test. Mỗi phương thức testMethod1 và testMethod2 khi chạy sẽ được cấp một bản sao dữ liệu ảo riêng và mọi thay đổi sẽ bị rollback sạch sẽ khi method đó kết thúc, nên testMethod3 hoàn toàn không bị ảnh hưởng.

**❌ Tại sao đáp án sai:**
> **A.** Giá trị số điện thoại bị đảo ngược sai lệch so với lúc insert trong vòng lặp setup.
> **B.** Hiển thị các số điện thoại đã bị sửa đổi ở testMethod1 và testMethod2 là sai cơ chế cô lập dữ liệu của test setup.
> **D.** Tương tự B, dữ liệu sửa đổi ở các test method khác không hề được lưu lại sang testMethod3.

**💡 Từ khóa ghi nhớ:** `Dữ liệu @testSetup: Mỗi Test Method chạy xong đều rollback, không bao giờ ảnh hưởng đến nhau!`

---

## Câu 109

**🔵 Which type of code represents the Model in the MVC architecture when using Apex and Visualforce pages?**

- **A.** A Controller Extension method that saves a list of Account records ❌
- **B.** Custom JavaScript that processes a list of Account records ❌
- **C.** A list of Account records returned from a Controller Extension method ✅
- **D.** A Controller Extension method that uses SOQL to query for a list of Account records ❌

**📝 Dịch tiếng Việt:**
> Loại mã code nào đại diện cho tầng 'Model' trong kiến trúc MVC khi sử dụng Apex và Visualforce?

**💬 Giải thích gốc (English):**
> The Model is responsible for handling the data and business logic. A list of Account records returned from a Controller Extension method would be an example of the Model.

**✅ Tại sao đáp án đúng:**
> Tầng Model đại diện cho cấu trúc và dữ liệu. Danh sách các bản ghi Account được trả về từ Controller Extension (C) chính là dữ liệu thực tế sẽ được hiển thị ra giao diện (View), đóng vai trò là tầng Model.

**❌ Tại sao đáp án sai:**
> **A.** Phương thức thực hiện lưu bản ghi (DML) thuộc tầng xử lý logic nghiệp vụ - Controller.
> **B.** JavaScript tùy chỉnh xử lý giao diện người dùng thuộc tầng View.
> **D.** Phương thức thực hiện SOQL query dữ liệu thuộc tầng xử lý logic - Controller.

**💡 Từ khóa ghi nhớ:** `MVC: Dữ liệu bản ghi (sObject/List sObject) = Model. Giao diện (VF/LWC/JS) = View. Apex Class/Logic = Controller.`

---

## Câu 110

**🔵 An org has a single account named 'NoContacts' that has no related contacts. Given the query: List<Account> accounts = [Select ID, (Select ID, Name from Contacts) from Account where Name = 'NoContacts']; What is the result of running this Apex?**

- **A.** accounts[0].contacts is invalid Apex. ❌
- **B.** accounts[0].contacts is an empty list. ✅
- **C.** accounts[0].contacts is Null. ❌
- **D.** A QueryException is thrown. ❌

**📝 Dịch tiếng Việt:**
> Một org chỉ có duy nhất một Account tên là 'NoContacts' và không có bất kỳ Contact liên quan nào. Chạy câu lệnh SOQL: List<Account> accounts = [Select ID, (Select ID, Name from Contacts) from Account where Name = 'NoContacts']; Kết quả của biến accounts[0].contacts là gì?

**💬 Giải thích gốc (English):**
> When you run the given query, it retrieves the account with the name ‘NoContacts’. Since this account has no related contacts, the contacts relationship will be an empty list, not null. Therefore, accounts[0].contacts will be an empty list.

**✅ Tại sao đáp án đúng:**
> Trong Salesforce, câu truy vấn quan hệ con (subquery) khi không tìm thấy bản ghi con nào sẽ trả về một Danh sách rỗng (empty list) (B), chứ tuyệt đối không bao giờ trả về giá trị null.

**❌ Tại sao đáp án sai:**
> **A.** Cú pháp truy cập list con hoàn toàn hợp lệ trong Apex.
> **C.** Không phải Null, Salesforce luôn khởi tạo List rỗng để tránh lỗi NullPointerException.
> **D.** Không có lỗi QueryException nào bị ném ra vì câu lệnh SOQL hoàn toàn đúng cú pháp và bản ghi cha vẫn tồn tại.

**💡 Từ khóa ghi nhớ:** `SOQL Subquery không có con -> Trả về EMPTY LIST, không bao giờ trả về NULL!`

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
> Khi sử dụng GROUP BY Name, mọi trường nằm trong mệnh đề SELECT bắt buộc phải là trường được nhóm (Name) hoặc phải nằm trong một hàm tổng hợp (Aggregate Function) như Max(CreatedDate). Do đó, câu B là hoàn toàn đúng cú pháp.

**❌ Tại sao đáp án sai:**
> **A.** Trường 'Type' nằm trong SELECT nhưng không có trong GROUP BY và không dùng hàm tổng hợp, gây lỗi biên dịch.
> **C.** Trường 'Id' và 'Type' vi phạm nghiêm trọng luật GROUP BY.
> **D.** Trường 'Type' vi phạm luật GROUP BY giống câu A.

**💡 Từ khóa ghi nhớ:** `Quy tắc GROUP BY: Trường nào trong SELECT thì bắt buộc phải nằm trong GROUP BY hoặc phải nằm trong HÀM TỔNG HỢP (SUM, MAX, MIN, COUNT).`

---

## Câu 112

**🔵 For which example task should a developer use a trigger rather than a workflow rule?**

- **A.** To set the Name field of an expense report record to Expense and the Date when it is saved ❌
- **B.** To send an email to a hiring manager when a candidate accepts a job offer ❌
- **C.** To notify an external system that a record has been modified ❌
- **D.** To set the primary Contact on an Account record when it is saved ✅

**📝 Dịch tiếng Việt:**
> Trong trường hợp nào sau đây lập trình viên bắt buộc phải sử dụng Trigger thay vì sử dụng Workflow Rule?

**💬 Giải thích gốc (English):**
> Workflow rules in Salesforce cannot update records of other objects. They are limited to actions like field updates, sending emails, creating tasks, and sending outbound messages within the same object.

**✅ Tại sao đáp án đúng:**
> Để cập nhật trường 'Primary Contact' (trường lookup trỏ đến con Contact) trên Account cha khi nó được lưu (D). Workflow Rule đời cũ cấm ngặt việc cập nhật chéo đối tượng đi xuống đối tượng con (từ Cha cập nhật xuống Con).

**❌ Tại sao đáp án sai:**
> **A.** Gán tên Expense Report có thể thực hiện cực kỳ dễ dàng bằng Workflow Rule field update.
> **B.** Gửi email nhắc nhở cho Hiring Manager là tính năng thế mạnh cơ bản của Workflow Email Alert.
> **C.** Gửi thông báo sang hệ thống ngoài có thể thực hiện thông qua Workflow Outbound Message không cần viết code.

**💡 Từ khóa ghi nhớ:** `Workflow Rule: Cấm cập nhật chéo đối tượng từ Cha xuống Con. Muốn làm -> Phải dùng Trigger / Flow.`

---

## Câu 113

**🔵 A developer must build an application that tracks which Accounts have purchased specific pieces of equipment that are represented as Products. Each Account could purchase many pieces of equipment. How should the developer track that an Account has purchased a piece of equipment?**

- **A.** Use the Asset object ✅
- **B.** Use a Master-Detail on Product to Account ❌
- **C.** Use a Custom object ❌
- **D.** Use a Lookup on Account to Product ❌

**📝 Dịch tiếng Việt:**
> Developer cần xây dựng ứng dụng theo dõi các Account đã mua các thiết bị cụ thể (được định nghĩa trong bảng Products). Mỗi Account có thể mua nhiều thiết bị. Lập trình viên nên làm gì để theo dõi việc mua bán này?

**💬 Giải thích gốc (English):**
> The Asset object in Salesforce is designed to represent specific products that customers have purchased. By using the Asset object, you can easily track each piece of equipment purchased by an Account, including details like purchase date, maintenance history, and more. This approach leverages Salesforce’s built-in functionality for managing customer assets, making it a robust and scalable solution.

**✅ Tại sao đáp án đúng:**
> Sử dụng đối tượng tiêu chuẩn Asset (A). Đối tượng Asset trong Salesforce sinh ra là để theo dõi các sản phẩm (Products) cụ thể đã được khách hàng (Account/Contact) mua và đang sở hữu thực tế, hỗ trợ tốt quản lý bảo hành.

**❌ Tại sao đáp án sai:**
> **B.** Quan hệ Master-Detail trực tiếp giữa Product và Account là sai logic vì một Product có thể được bán cho nhiều Account khác nhau.
> **C.** Sử dụng Custom Object hoạt động được nhưng tốn công tự thiết kế và bỏ phí đối tượng tiêu chuẩn Asset rất tối ưu có sẵn.
> **D.** Đặt Lookup từ Account lên Product làm giới hạn 1 Account chỉ mua được tối đa 1 sản phẩm, trái yêu cầu mua nhiều thiết bị.

**💡 Từ khóa ghi nhớ:** `Khách hàng mua Sản phẩm thực tế -> Dùng đối tượng tiêu chuẩn ASSET.`

---

## Câu 114

**🔵 A developer is creating a page that allows users to create multiple Opportunities. The developer is asked to verify the current user’s default Opportunity record type, and set certain default values based on the record type before inserting the record. How can the developer find the current user’s default record type?**

- **A.** Use the Schema.userInfo.Opportunity.getDefaultRecordType() method. ❌
- **B.** Query the Profile where the ID equals userInfo.getProfileID() and then use the profile.Opportunity.getDefaultRecordType() method. ❌
- **C.** Create the opportunity and check the opportunity.recordType, which will have the record ID of the current user’s default record type, before inserting. ❌
- **D.** Use Opportunity.SObjectType.getDescribe().getRecordTypeInfos() to get a list of record types, and iterate through them until isDefaultRecordTypeMapping() is true. ✅

**📝 Dịch tiếng Việt:**
> Làm sao để lấy được cái Record Type mặc định của user hiện tại đối với object Opportunity bằng code Apex?

**💬 Giải thích gốc (English):**
> This method allows the developer to programmatically access the record type information and identify the default record type for the current user.

**✅ Tại sao đáp án đúng:**
> C là cách chuẩn bài (best practice). Dùng Schema Describe để lấy danh sách Record Type, sau đó check xem thằng nào có `isDefaultRecordTypeMapping()` bằng true.

**❌ Tại sao đáp án sai:**
> **A.** Sai cú pháp trầm trọng. Object Profile không có cái method `getDefaultRecordType()` nào cho Opportunity cả.
> **B.** Khi mày khởi tạo record trong memory (`new Opportunity()`), Salesforce không tự gán record type ID mặc định vào field đó đâu, nó chỉ gán khi mày insert hoặc qua UI thôi.
> **D.** Method `Schema.userInfo...` là đồ tự chế, Salesforce không có cái này.

**💡 Từ khóa ghi nhớ:** `Mẹo PD1: Đụng đến Record Type, Permission, hay Metadata của Object thì 90% là dùng Describe SObject.`

---

## Câu 115

**🔵 Requirements state that a child record is deleted when its parent is deleted, and a child can be moved to a different parent when necessary. Which type of relationship should be built between the parent and child objects in Schema builder to support these requirements?**

- **A.** Master-Detail relationship ✅
- **B.** Child relationship ❌
- **C.** Lookup relationship from the parent to the child ❌
- **D.** Lookup relationship from the child to the parent ❌

**📝 Dịch tiếng Việt:**
> Yêu cầu nghiệp vụ: Khi bản ghi cha bị xóa thì bản ghi con phải tự động bị xóa theo, và bản ghi con có thể chuyển sang bản ghi cha khác khi cần thiết (reparented). Loại quan hệ nào giữa cha và con hỗ trợ yêu cầu này?

**💬 Giải thích gốc (English):**
> A Master-Detail relationship provides the following features that align with the given requirements:
> Automatic deletion of child records: When the parent record is deleted, all related child records are automatically deleted.
> Relocation of child records: By default, records can’t be reparented in master-detail relationships. Administrators can, however, allow child records in master-detail relationships on custom objects to be reparented to different parent records by selecting the Allow reparenting option in the master-detail relationship definition.

**✅ Tại sao đáp án đúng:**
> Mối quan hệ Master-Detail (A). Mối quan hệ này có tính năng tự động xóa con khi cha bị xóa (cascade delete). Đồng thời, ta chỉ cần tích chọn tùy chọn 'Allow reparenting' trên cấu hình trường để cho phép con chuyển đổi cha tự do.

**❌ Tại sao đáp án sai:**
> **B.** Child relationship không phải là một kiểu trường quan hệ vật lý trong Salesforce Schema Builder.
> **C.** Tạo lookup từ cha đến con là ngược chiều quan hệ, không đúng thiết kế dữ liệu.
> **D.** Mối quan hệ Lookup từ con lên cha mặc định không tự động xóa con khi cha bị xóa (trừ khi tự cấu hình thêm) và không có tính chất Master-Detail chặt chẽ.

**💡 Từ khóa ghi nhớ:** `Cha xóa -> Con tự xóa + Cho phép đổi Cha = Master-Detail Relationship bật 'Allow reparenting'.`

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
> Developer cần sửa đoạn code dưới đây để tránh lỗi vượt quá giới hạn (governor limit) về số lượng SOQL queries: [Code SOQL in For Loop]. Kỹ thuật nào nên được áp dụng?

**💬 Giải thích gốc (English):**
> Refactor the code above to perform only one SOQL query, filtering by the Set of opportunityIds.
> This technique will significantly reduce the number of SOQL queries issued, as it combines all the individual queries into a single query, filtering by the entire Set of opportunityIds. This is much more efficient and helps to avoid reaching the governor limit.

**✅ Tại sao đáp án đúng:**
> Refactor đoạn code để chỉ thực hiện duy nhất MỘT câu truy vấn SOQL nằm ngoài vòng lặp (C), sử dụng từ khóa 'IN :opportunityIds' để lọc toàn bộ danh sách sản phẩm cùng một lúc cực kỳ tối ưu (Bulkification).

**❌ Tại sao đáp án sai:**
> **A.** Giới hạn 100 SOQL vẫn sẽ bị chạm nếu số lượng ID lớn hơn 100, cách này không giải quyết triệt để gốc rễ vấn đề.
> **B.** getLimitQueries() chỉ dùng để kiểm tra giới hạn còn lại, không giúp tối ưu hóa code hay ngăn chặn lỗi thực sự.
> **D.** getQueries() cũng chỉ để đếm số câu lệnh đã chạy, không có tác dụng refactor mã nguồn.

**💡 Từ khóa ghi nhớ:** `Quy tắc Bulkify tối thượng: Đưa câu truy vấn SOQL ra ngoài vòng lặp For và dùng toán tử IN!`

---

## Câu 117

**🔵 A developer must write an Apex method that will be called from a Lightning component. The method may delete an Account stored in the accountRec variable. Which method should a developer use to ensure only users that should be able to delete Accounts can successfully perform deletions?**

- **A.** Schema.sObjectType.Account.isDeletable() ✅
- **B.** Account.isDeletable() ❌
- **C.** accountRec.isDeletable() ❌
- **D.** accountRec.sObjectType.isDeletable() ❌

**📝 Dịch tiếng Việt:**
> Developer viết phương thức Apex xóa Account được gọi từ Lightning Component. Hàm nào giúp kiểm tra xem user hiện tại có quyền xóa Account hay không trước khi thực hiện xóa?

**💬 Giải thích gốc (English):**
> Schema.sObjectType.Account.isDeletable()
> This method checks if the current user has the necessary permissions to delete the Account object.

**✅ Tại sao đáp án đúng:**
> Sử dụng Schema.sObjectType.Account.isDeletable() (A). Đây là phương thức mô tả (describe) chuẩn của Salesforce để kiểm tra phân quyền CRUD (Delete) của user hiện tại trên đối tượng Account.

**❌ Tại sao đáp án sai:**
> **B.** Cú pháp Account.isDeletable() sai cấu trúc gọi của lớp Schema Describe.
> **C.** Biến bản ghi accountRec không có phương thức trực tiếp .isDeletable().
> **D.** Cú pháp accountRec.sObjectType.isDeletable() là hàng giả tưởng, không biên dịch được.

**💡 Từ khóa ghi nhớ:** `Kiểm tra quyền Xóa (Delete) của sObject -> Dùng Schema.sObjectType.ObjectName.isDeletable().`

---

## Câu 118

**🔵 Which two statements are valid regarding Apex classes and interfaces? (Choose two.)**

- **A.** Classes are final by default. ✅
- **B.** Interface methods are public by default. ❌
- **C.** Inner classes are private by default. ✅
- **D.** A class can only have one inner class level. ❌

**📝 Dịch tiếng Việt:**
> Hai phát biểu đúng về Apex class và interface?

**💬 Giải thích gốc (English):**
> Methods and classes are final by default. You can’t use the final keyword in the declaration of a class or method. This means they can’t be overridden. Use the virtual keyword if you need to override a method or class.

**✅ Tại sao đáp án đúng:**
> A: Mặc định class là final (không cho kế thừa). D: Apex giới hạn chỉ có 1 tầng inner class bên trong top-level class.

**❌ Tại sao đáp án sai:**
> **B.** Inner class mặc định là private, phải khai báo public mới dùng ngoài được.
> **C.** Phương thức trong interface mặc định là global/public tùy modifier của interface, nhưng ý D là quy tắc kiến trúc chuẩn hơn trong bài thi này.

**💡 Từ khóa ghi nhớ:** `Mặc định Apex Class = Final. Top-level = Chỉ có 1 tầng inner class.`

---

## Câu 119

**🔵 What is a benefit of using an after insert trigger over using a before insert trigger?**

- **A.** An after insert trigger allows a developer to bypass validation rules when updating fields on the new record. ❌
- **B.** An after insert trigger allows a developer to insert other objects that reference the new record. ✅
- **C.** An after insert trigger allows a developer to make a callout to an external service. ❌
- **D.** An after insert trigger allows a developer to modify fields in the new record without a query. ❌

**📝 Dịch tiếng Việt:**
> Lợi ích nổi bật của việc sử dụng trigger 'after insert' so với trigger 'before insert' là gì?

**💬 Giải thích gốc (English):**
> In an after insert trigger, the record has already been committed to the database, so you can safely reference its ID and use it to create or update other related objects.

**✅ Tại sao đáp án đúng:**
> Trigger after insert cho phép lập trình viên chèn các bản ghi đối tượng khác có liên quan tham chiếu đến bản ghi mới (B). Vì ở sự kiện 'after', bản ghi mới đã được cấp ID chính thức từ hệ thống, ta có thể lấy ID đó gán vào trường Lookup của bản ghi liên quan.

**❌ Tại sao đáp án sai:**
> **A.** Trigger không thể giúp bypass validation rules của hệ thống bất kể là before hay after.
> **C.** Cả hai loại trigger đều cấm gọi API (callout) trực tiếp, bắt buộc phải dùng phương thức bất đồng bộ @future(callout=true).
> **D.** Ngược lại, chỉ có trigger 'before insert' mới cho phép thay đổi giá trị các trường của chính bản ghi đó mà không cần thực hiện lệnh DML Update bổ sung.

**💡 Từ khóa ghi nhớ:** `Cần ID của bản ghi để tạo dữ liệu liên quan -> Bắt buộc dùng AFTER INSERT Trigger.`

---

## Câu 120

**🔵 An org has an existing Visual Flow that creates an Opportunity with an Update Records element. A developer must update the Visual Flow to also create a Contact and store the created Contact's ID on the Opportunity. Which update should the developer make in the Visual Flow?**

- **A.** Add a new Create Records element. ✅
- **B.** Add a new Quick Action (of type Create) element. ❌
- **C.** Add a new Update Records element. ❌
- **D.** Add a new Get Records element. ❌

**📝 Dịch tiếng Việt:**
> Một Visual Flow đã có sẵn logic cập nhật Opportunity. Developer cần nâng cấp Flow này để tạo thêm mới 1 Contact và lưu ID của Contact mới đó lên Opportunity. Lập trình viên nên thêm phần tử nào vào Flow?

**💬 Giải thích gốc (English):**
> A. Add a new Create Records element.
> This element will allow the flow to create a new Contact record. After creating the Contact, the flow can then store the Contact’s ID in a variable. This variable can be used in an Update Records element to update the Opportunity with the Contact’s ID

**✅ Tại sao đáp án đúng:**
> Thêm phần tử 'Create Records' mới (A). Phần tử này cho phép Flow tạo mới bản ghi Contact và tự động xuất (output) ID của Contact vừa tạo vào một biến để dùng cập nhật cho Opportunity ở bước sau.

**❌ Tại sao đáp án sai:**
> **B.** Quick Action Create dùng để kích hoạt action trên giao diện, không linh hoạt và đúng chuẩn bằng Create Records trong Flow xử lý ngầm.
> **C.** Update Records chỉ dùng để sửa bản ghi đã tồn tại, không thể dùng để tạo mới bản ghi Contact.
> **D.** Get Records dùng để tìm kiếm truy vấn bản ghi có sẵn, không có khả năng tạo mới.

**💡 Từ khóa ghi nhớ:** `Muốn tạo mới bản ghi trong Flow -> Gọi tên Create Records Element.`

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
> B: Sử dụng Validation Rule kiểm tra nếu StageName chuyển sang Closed/Won thì chặn chỉnh sửa toàn bộ trường. D: Đánh dấu các trường là Read-only trên Page Layout tương ứng với Record Type trạng thái Closed/Won để khóa giao diện người dùng.

**❌ Tại sao đáp án sai:**
> **A.** Flow Builder không thể khóa cứng giao diện nhập liệu trực tiếp của người dùng một cách tối ưu như Validation Rule.
> **C.** Process Automation Settings dùng để thiết lập chung cho hệ thống tự động hóa, không hỗ trợ logic khóa bản ghi cụ thể.

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
> Sử dụng một Map<Id, List<Contact>> (D) gom nhóm toàn bộ Contact theo AccountId trước. Khi đó, thay vì duyệt vòng lặp O(N*M) lồng nhau cực kỳ chậm chạp, ta chỉ cần duyệt Account và gọi map.get(a.Id) trong O(1) để lấy ngay danh sách Contact con liên quan.

**❌ Tại sao đáp án sai:**
> **A.** Đảo ngược vị trí hai vòng lặp lồng nhau vẫn giữ nguyên độ phức tạp thuật toán O(N*M), không giải quyết được vấn đề.
> **B.** Tạo helper class chỉ làm sạch code chứ không làm thay đổi bản chất thuật toán và thời gian thực thi của CPU.
> **C.** Thêm GROUP BY vào SOQL không giúp giải quyết thuật toán so khớp danh sách trong RAM.

**💡 Từ khóa ghi nhớ:** `Tối ưu For lồng nhau -> Gom danh sách con vào MAP theo ID cha để lấy cực nhanh O(1).`

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
> B: Force.com IDE (môi trường phát triển tích hợp dựa trên Eclipse dù đã cũ nhưng đề vẫn tính). D: Change Set gửi từ môi trường Sandbox lên Production. E: Metadata API dùng để deploy programmatic thông qua các công cụ như Ant Migration Tool hoặc Salesforce CLI.

**❌ Tại sao đáp án sai:**
> **A.** Không thể gửi Change Set trực tiếp từ một Developer Org (Org cá nhân) lên một Production Org thật được (chỉ Sandbox gửi được cho Production liên kết).
> **C.** Data Loader chỉ dùng để import/export DỮ LIỆU bản ghi (Data), tuyệt đối không dùng để deploy METADATA (cấu hình/code).

**💡 Từ khóa ghi nhớ:** `Deploy Metadata -> Change Set Sandbox, Metadata API, CLI. Data Loader chỉ dùng cho DATA bản ghi.`

---

## Câu 124

**🔵 Universal Containers is building a recruiting app with an Applicant object that stores information about an individual person and a Job object that represents a job. Each applicant may apply for more than one job. What should a developer implement to represent that an applicant has applied for a job?**

- **A.** Lookup field from Applicant to Job ❌
- **B.** Junction object between Applicant and Job ✅
- **C.** Master-detail field from Applicant to Job ❌
- **D.** Formula field on Applicant that references Job ❌

**📝 Dịch tiếng Việt:**
> Universal Containers xây dựng app tuyển dụng gồm object Applicant (ứng viên) và Job (công việc). Một ứng viên có thể nộp nhiều Job, một Job có nhiều ứng viên ứng tuyển. Thiết kế mối quan hệ nào là phù hợp nhất?

**💬 Giải thích gốc (English):**
> A junction object is used to create a many-to-many relationship between two objects. In this case, since each applicant can apply for multiple jobs and each job can have multiple applicants, a junction object is the most appropriate solution. This junction object would have two master-detail relationships: one to the Applicant object and one to the Job object.

**✅ Tại sao đáp án đúng:**
> Mối quan hệ là Nhiều-Nhiều (Many-to-Many). Giải pháp chuẩn là tạo một đối tượng trung gian gọi là Junction Object (B) liên kết giữa Applicant và Job thông qua hai trường Master-Detail trỏ về hai phía.

**❌ Tại sao đáp án sai:**
> **A.** Tạo Lookup trực tiếp từ Applicant đến Job làm giới hạn mỗi ứng viên chỉ được ứng tuyển tối đa 1 Job tại 1 thời điểm.
> **C.** Tương tự A, Master-Detail trực tiếp từ Applicant đến Job giới hạn nghiêm trọng quan hệ 1-Nhiều một chiều.
> **D.** Formula field chỉ để hiển thị giá trị đọc, không thể đại diện cho mối quan hệ dữ liệu vật lý Nhiều-Nhiều phức tạp.

**💡 Từ khóa ghi nhớ:** `Mối quan hệ Nhiều-Nhiều (Many-to-Many) -> Bắt buộc tạo đối tượng trung gian JUNCTION OBJECT.`

---

## Câu 125

**🔵 The sales team at Universal Containers would like to see a visual indicator appear on both Account and Opportunity page layouts to alert sales people when an Account is late making payments or has entered the collections process. What can a developer implement to achieve this requirement without having to write custom code?**

- **A.** Formula Field ✅
- **B.** Workflow Rule ❌
- **C.** Quick Action ❌
- **D.** Roll-up Summary Field ❌

**📝 Dịch tiếng Việt:**
> Sales team muốn hiển thị biểu tượng cảnh báo trực quan trên giao diện Account và Opportunity để báo khi Account bị nợ quá hạn hoặc rơi vào trạng thái đòi nợ. Giải pháp nào đáp ứng không cần viết code?

**💬 Giải thích gốc (English):**
> A formula field can be used to create a visual indicator on both the Account and Opportunity page layouts. This field can be configured to display a specific value or image based on the criteria you set, such as when an account is late making payments or has entered the collections process.

**✅ Tại sao đáp án đúng:**
> Sử dụng Formula Field (A) kiểu Text kết hợp với hàm IMAGE() để kiểm tra điều kiện nợ và hiển thị các icon cảnh báo (đỏ, vàng, xanh) cực kỳ sinh động trên page layout hoàn toàn no-code.

**❌ Tại sao đáp án sai:**
> **B.** Workflow Rule chỉ dùng để chạy hành động tự động ngầm, không có khả năng hiển thị giao diện hay hình ảnh cảnh báo trực quan.
> **C.** Quick Action dùng để tạo nút bấm thao tác nhanh, không phải công cụ hiển thị chỉ báo trạng thái.
> **D.** Roll-up Summary Field chỉ dùng để tính tổng số lượng/tiền từ con lên cha, không có tính năng hiển thị hình ảnh.

**💡 Từ khóa ghi nhớ:** `Hiển thị icon/ảnh cảnh báo động không code -> Sử dụng Formula Field chứa hàm IMAGE().`

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
> Tổng thời gian CPU xử lý - Elapsed CPU time (D) (giới hạn 10 giây cho transaction đồng bộ) áp dụng chung cho toàn bộ trigger, class Apex, validation rules, flows,... chạy trong transaction đó.

**❌ Tại sao đáp án sai:**
> **A.** Thời gian SOQL chỉ tính riêng cho các câu lệnh truy vấn, không bao quát toàn bộ xử lý logic của CPU.
> **B.** Không có giới hạn cụ thể về số lượng class Apex được gọi trong một transaction.
> **C.** Giới hạn DML row (10,000 bản ghi) tính trên số lượng bản ghi được thao tác, không phải giới hạn thời gian chạy chung.

**💡 Từ khóa ghi nhớ:** `Giới hạn bao trùm toàn bộ transaction Apex -> Tổng thời gian xử lý CPU (10 giây đồng bộ).`

---

## Câu 127

**🔵 Which two sfdx commands can be used to add testing data to a Developer sandbox? (Choose two.)**

- **A.** force:data:async:upsert ❌
- **B.** force:data:tree:import ✅
- **C.** force:data:bulk:upsert ✅
- **D.** force:data:object:create ❌

**📝 Dịch tiếng Việt:**
> Hai lệnh SFDX nào dùng để nạp dữ liệu test vào sandbox?

**💬 Giải thích gốc (English):**
> force:data:tree:import - This command is used to import data from a JSON file into Salesforce, which is useful for hierarchical data.
> force:data:bulk:upsert - This command allows you to upsert (update or insert) large volumes of data in bulk.

**✅ Tại sao đáp án đúng:**
> A: `tree:import` nạp dữ liệu từ file JSON có quan hệ cha-con. C: `bulk:upsert` dùng cho các file CSV lớn.

**❌ Tại sao đáp án sai:**
> **B.** Đây là lệnh không tồn tại trong Salesforce CLI.
> **D.** Lệnh này dùng để tạo Metadata (định nghĩa object), không phải tạo Data (bản ghi).

**💡 Từ khóa ghi nhớ:** `SFDX Data: Tree (JSON) hoặc Bulk (CSV).`

---

## Câu 128

**🔵 A developer wants to override a button using Visualforce on an object. What is the requirement?**

- **A.** The controller or extension must have a PageReference method. ❌
- **B.** The standardController attribute must be set to the object. ✅
- **C.** The action attribute must be set to a controller method. ❌
- **D.** The object record must be instantiated in a controller or extension. ❌

**📝 Dịch tiếng Việt:**
> Để ghi đè (override) một nút bấm chuẩn (standard button) của một Object bằng trang Visualforce, trang đó có yêu cầu bắt buộc gì?

**💬 Giải thích gốc (English):**
> In Visualforce, if a developer wants to override a standard button with a custom Visualforce page on an object, they need to specify the standardController attribute in the apex:page component.

**✅ Tại sao đáp án đúng:**
> Trang Visualforce đó bắt buộc phải khai báo thuộc tính standardController trỏ đến đúng API Name của Object đó (B) để hệ thống nhận diện và truyền ngữ cảnh bản ghi khi bấm nút.

**❌ Tại sao đáp án sai:**
> **A.** Controller không bắt buộc phải có phương thức trả về PageReference mới ghi đè được.
> **C.** Thuộc tính action trên thẻ apex:page dùng để tự kích hoạt hàm khi trang load, không phải điều kiện bắt buộc để override nút.
> **D.** Không cần khởi tạo thủ công bản ghi trong code vì standard controller đã tự động làm việc này.

**💡 Từ khóa ghi nhớ:** `Override nút chuẩn bằng Visualforce -> Bắt buộc trang phải khai báo standardController='ObjectName'.`

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
> Khai báo kết hợp standardController='Case' đi kèm extensions='myControllerExtension' (D). Đây là mô hình Controller Extension chuẩn để vừa dùng được các hàm lưu/sửa mặc định của Case vừa gọi được logic custom của extension class.

**❌ Tại sao đáp án sai:**
> **A.** Case là đối tượng tiêu chuẩn, cấm khai báo bằng từ khóa 'controller' (từ khóa này chỉ dành cho Custom Controller class).
> **B.** Thiếu standardController thì extensions không thể chạy độc lập được.
> **C.** Khai báo extension class vào thuộc tính 'controller' là sai vai trò của lớp mở rộng.

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
> Gây ra lỗi DML Exception (C). Salesforce cấm tuyệt đối việc thực hiện câu lệnh DML Update trên chính các bản ghi đang nằm trong trigger xử lý 'before' (trigger.new), vì việc này sẽ gây ra vòng lặp vô hạn (recursive) vô phương cứu chữa và làm sập hệ thống.

**❌ Tại sao đáp án sai:**
> **A.** Biến Id được duyệt qua trigger.new luôn tồn tại bản ghi, không gây ra lỗi tham chiếu null.
> **B.** Code viết đúng cú pháp Apex nên biên dịch thành công, lỗi chỉ nổ ra khi thực thi (runtime).
> **D.** Lỗi xảy ra ngay lập tức ở bản ghi đầu tiên khi gọi lệnh Update chứ không đợi đến khi bulk update chạm limit.

**💡 Từ khóa ghi nhớ:** `Cấm kỵ tối thượng: Gọi lệnh DML (insert/update/delete) trên chính danh sách trigger.new trong trigger!`

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
> Kết quả của đoạn code insert Account rỗng với tham số false là gì?

**💬 Giải thích gốc (English):**
> The allOrNone parameter specifies whether the operation allows partial success.
> If allOrNone is set to false and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify which records succeeded or failed.
> If allOrNone is set to true and the method isn’t successful, an exception is thrown. The default for the parameter is true.

**✅ Tại sao đáp án đúng:**
> Thiếu Name nên lỗi, nhưng tham số `false` ngăn việc bắn Exception. Code chạy tiếp bình thường nhưng bản ghi không được tạo.

**❌ Tại sao đáp án sai:**
> **A.** Bản ghi lỗi thì không bao giờ được tạo.
> **B.** Bản ghi lỗi nên không có chuyện được tạo thành công.
> **D.** Exception bị nuốt mất rồi vì tham số allOrNone = false.

**💡 Từ khóa ghi nhớ:** `Database.insert(..., false): Im lặng là vàng (không bắn Exception).`

---

## Câu 132

**🔵 An after trigger on the Account object performs a DML update operation on all of the child Opportunities of an Account. There are no active triggers on the Opportunity object, yet a 'maximum trigger depth exceeded' error occurs in certain situations. Which two reasons possibly explain the Account trigger firing recursively? (Choose two.)**

- **A.** Changes to Opportunities are causing cross-object workflow field updates to be made on the Account. ✅
- **B.** Changes to Opportunities are causing roll-up summary fields to update on the Account. ✅
- **C.** Changes are being made to the Account during an unrelated parallel save operation. ❌
- **D.** Changes are being made to the Account during Criteria Based Sharing evaluation. ❌

**📝 Dịch tiếng Việt:**
> Trigger 'after' trên Account thực hiện DML update toàn bộ Opportunity con liên quan. Không có trigger nào trên Opportunity, nhưng lỗi 'maximum trigger depth exceeded' (vượt quá độ sâu đệ quy) vẫn xảy ra. Hai lý do nào giải thích việc này? (Chọn 2)

**💬 Giải thích gốc (English):**
> The two reasons that could possibly explain the Account trigger firing recursively are:
> Cross-object workflow field updates can trigger the Account trigger again if the workflow rule updates a field on the Account.
> Roll-up summary fields on the Account that aggregate data from child Opportunities can cause the Account trigger to fire again when these fields are recalculated.

**✅ Tại sao đáp án đúng:**
> A: Cập nhật Opportunity kích hoạt Cross-object Workflow Field Update cập nhật ngược trường lên Account cha -> nổ trigger Account lần nữa. B: Cập nhật Opportunity làm thay đổi trường Roll-up Summary trên Account cha -> kích hoạt vòng Save Account và nổ trigger Account lần nữa.

**❌ Tại sao đáp án sai:**
> **C.** Lưu song song không liên quan không tạo ra chuỗi đệ quy tuần hoàn khép kín làm vượt độ sâu trigger.
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
> Cho class InsuranceRates chứa biến tĩnh 'public static final Decimal smokerCharge = 0.01;'. Trong trigger ContactTrigger dưới đây, lập trình viên điền gì vào XXX để gán giá trị của smokerCharge cho biến baseCost? [Code Trigger]

**💬 Giải thích gốc (English):**
> The smokerCharge variable is declared as a static variable in the InsuranceRates class. Static variables belong to the class itself rather than any instance of the class, so you access it using the class name InsuranceRates

**✅ Tại sao đáp án đúng:**
> Vì smokerCharge là một biến tĩnh (static variable), nó thuộc về class chứ không thuộc về đối tượng instance. Ta truy cập trực tiếp bằng cú pháp: ClassName.staticVariableName -> InsuranceRates.smokerCharge (A).

**❌ Tại sao đáp án sai:**
> **B.** Biến smokerCharge là public trực tiếp, không cần hàm getter để lấy và class cũng không định nghĩa hàm này.
> **C.** Sai đường dẫn tham chiếu lớp hệ thống.
> **D.** Cố gắng gọi biến tĩnh thông qua đối tượng instance 'rates' là sai nguyên tắc lập trình hướng đối tượng trong Apex.

**💡 Từ khóa ghi nhớ:** `Biến Static -> Luôn truy cập thông qua tên Class: ClassName.VariableName.`

---

## Câu 134

**🔵 How should a developer prevent a recursive trigger?**

- **A.** Use a one trigger per object pattern. ❌
- **B.** Use a static Boolean variable. ✅
- **C.** Use a trigger handler. ❌
- **D.** Use a private Boolean variable. ❌

**📝 Dịch tiếng Việt:**
> Phương pháp nào lập trình viên nên sử dụng để ngăn chặn lỗi trigger chạy đệ quy vô hạn (recursive trigger)?

**💬 Giải thích gốc (English):**
> What is a Recursive Trigger: A recursive trigger is one that performs an action, such as an update or insert, which causes the trigger to invoke itself, often due to an update it performs.
> How to Avoid Recursive Triggers: To prevent recursive triggers, you can create a class with a static Boolean variable initialized to true. In the trigger, before executing your code, check if the variable is true. If it is, proceed with your code and then set the variable to false.

**✅ Tại sao đáp án đúng:**
> Sử dụng một biến tĩnh kiểu Boolean - static Boolean variable (B) trong một class helper (ví dụ: public static Boolean isFirstRun = true). Check biến này ở đầu trigger, chạy xong gán bằng false để chặn các vòng sau.

**❌ Tại sao đáp án sai:**
> **A.** Mô hình một trigger trên một object giúp quản lý code sạch sẽ, không giúp ngăn đệ quy chéo giữa các object khác nhau.
> **C.** Trigger Handler pattern là kiến trúc tách code xử lý, không có cơ chế tự chặn đệ quy nếu thiếu biến tĩnh.
> **D.** Biến private Boolean sẽ bị khởi tạo lại từ đầu mỗi khi trigger kích hoạt, hoàn toàn vô dụng để chặn đệ quy.

**💡 Từ khóa ghi nhớ:** `Chặn Trigger đệ quy (Recursive) -> Luôn sử dụng biến STATIC BOOLEAN trong class helper.`

---

## Câu 135

**🔵 What is a capability of the tag that is used for loading external Javascript libraries in Lightning Component? (Choose three.)**

- **A.** Loading files from Documents. ❌
- **B.** One-time loading for duplicate scripts. ✅
- **C.** Specifying loading order. ✅
- **D.** Loading scripts in parallel. ✅
- **E.** Loading externally hosted scripts. ❌

**📝 Dịch tiếng Việt:**
> Ba khả năng nổi bật của thẻ <ltng:require> dùng để tải các thư viện JavaScript bên ngoài trong Aura Component là gì? (Chọn 3)

**💬 Giải thích gốc (English):**
> Loading Order
> The scripts are loaded in the order that they are listed.
> One-Time Loading
> Scripts load only once, even if they’re specified in multiple <ltng:require> tags in the same component or across different components.
> Parallel Loading
> Use separate <ltng:require> tags for parallel loading if you have multiple sets of scripts that are not dependent on each other.

**✅ Tại sao đáp án đúng:**
> B: Cơ chế One-time loading chỉ tải script duy nhất một lần dù khai báo ở nhiều component khác nhau. C: Cho phép chỉ định thứ tự tải (loading order) các script theo danh sách liệt kê. D: Tải song song (parallel) các bộ script độc lập bằng các thẻ riêng biệt để tối ưu tốc độ.

**❌ Tại sao đáp án sai:**
> **A.** Thẻ này tải file từ Static Resource chứ không tải trực tiếp từ thư mục Documents cũ kỹ.
> **E.** Vì lý do bảo mật CSP, <ltng:require> cấm tải trực tiếp các script lưu trữ bên ngoài Salesforce, bắt buộc phải upload vào Static Resource.

**💡 Từ khóa ghi nhớ:** `ltng:require (Aura) / lightning/platformResourceLoader (LWC): Tải script từ STATIC RESOURCE, hỗ trợ thứ tự tải và chạy duy nhất 1 lần.`

---

## Câu 136

**🔵 Universal Containers (UC) wants to lower its shipping cost while making the shipping process more efficient. The Distribution Officer advises UC to implement global addresses to allow multiple Accounts to share a default pickup address. The developer is tasked to create the supporting object and relationship for this business requirement and uses the Setup Menu to create a custom object called 'Global Address'. Which field should the developer add to create the most efficient model that supports the business need?**

- **A.** Add a Master-Detail field on the Global Address object to the Account object. ❌
- **B.** Add a Master-Detail field on the Account object to the Global Address object. ❌
- **C.** Add a Lookup field on the Global Address object to the Account object. ❌
- **D.** Add a Lookup field on the Account object to the Global Address object. ✅

**📝 Dịch tiếng Việt:**
> Universal Containers muốn tạo Custom Object 'Global Address' chứa các địa chỉ mặc định dùng chung cho nhiều Account. Mối quan hệ nào là tối ưu nhất giữa Account và Global Address?

**💬 Giải thích gốc (English):**
> Since a standard object like Account cannot be a detail in a Master-Detail Relationship, we should use a Lookup Relationship instead. To allow multiple Accounts to share a default pickup address, add a Lookup field on the Account object that points to the Global Address object. This setup enables each Account to reference a Global Address, supporting the business need by enhancing shipping efficiency and reducing costs.

**✅ Tại sao đáp án đúng:**
> Thêm trường Lookup trên Account trỏ đến đối tượng Global Address (D). Mối quan hệ này cho phép nhiều Account dùng chung 1 địa chỉ (1-Nhiều từ Global Address đến Account) và Account là Standard Object nên cấm làm con trong quan hệ Master-Detail với Custom Object.

**❌ Tại sao đáp án sai:**
> **A.** Master-Detail trên Global Address trỏ đến Account làm giới hạn mỗi địa chỉ chỉ thuộc về 1 Account duy nhất, không dùng chung được.
> **B.** Account là đối tượng tiêu chuẩn của Salesforce, cấm ngặt việc làm con (detail) trong quan hệ Master-Detail với Custom Object.
> **C.** Lookup trên Global Address trỏ đến Account giới hạn quan hệ ngược chiều, không đáp ứng chia sẻ địa chỉ.

**💡 Từ khóa ghi nhớ:** `Standard Object (như Account) -> CẤM làm con (detail) trong mối quan hệ Master-Detail!`

---

## Câu 137

**🔵 A developer is creating a Lightning web component to show a list of sales records. The Sales Representative user should be able to see the commission field on each record. The Sales Assistant user should be able to see all fields on the record except the commission field. How should this be enforced so that the component works for both users without showing any errors?**

- **A.** Use Lightning Data Service to get the collection of sales records. ❌
- **B.** Use WITH SECURITY_ENFORCED in the SOQL that fetches the data for the component. ❌
- **C.** Use Lightning Locker Service to enforce sharing rules and field-level security. ❌
- **D.** Use Security.stripInaccessible to remove fields inaccessible to the current user. ✅

**📝 Dịch tiếng Việt:**
> Làm thế nào để LWC hoạt động cho cả 2 loại user (có quyền và không có quyền xem field) mà không báo lỗi?

**💬 Giải thích gốc (English):**
> Use the stripInaccessible method to enforce field-level and object-level data protection. This method can be used to strip the fields and relationship fields from query and subquery results that the user can’t access. The method can also be used to remove inaccessible sObject fields before DML operations to avoid exceptions and to sanitize sObjects that have been deserialized from an untrusted source.

**✅ Tại sao đáp án đúng:**
> Security.stripInaccessible sẽ tự động lọc bỏ các field thiếu quyền ra khỏi kết quả trả về, giúp code chạy trơn tru cho mọi user mà không 'văng' Exception.

**❌ Tại sao đáp án sai:**
> **A.** WITH SECURITY_ENFORCED sẽ bắn Exception và làm app bị crash nếu user thiếu quyền xem bất kỳ field nào trong query.
> **B.** LDS thường dùng cho 1 bản ghi hoặc tập hợp nhỏ, việc 'lọc field' theo quyền trong một list lớn không linh hoạt bằng stripInaccessible trong Apex.
> **C.** Locker Service là cơ chế bảo mật cô lập component, không liên quan đến việc lọc dữ liệu theo FLS.

**💡 Từ khóa ghi nhớ:** `Security Practice: Muốn app chạy 'êm' dù thiếu quyền -> Dùng Security.stripInaccessible.`

---

## Câu 138

**🔵 The sales management team at Universal Containers requires that the Lead Source field of the Lead record be populated when a Lead is converted. What should be done to ensure that a user populates the Lead Source field prior to converting a Lead?**

- **A.** Create an after trigger on Lead ❌
- **B.** Use a Validation Rule ✅
- **C.** Use a Formula Field ❌
- **D.** Use Lead Conversion field mapping ❌

**📝 Dịch tiếng Việt:**
> Đảm bảo điền Lead Source trước khi chuyển đổi (convert) Lead?

**💬 Giải thích gốc (English):**
> A validation rule can enforce that the Lead Source field is populated by preventing the Lead from being saved or converted if the field is empty. This ensures that users must fill in the Lead Source field before proceeding with the conversion.

**✅ Tại sao đáp án đúng:**
> Validation Rule giúp chặn lại nếu thiếu dữ liệu khi field IsConverted = true.

**❌ Tại sao đáp án sai:**
> **A.** Formula chỉ để tính toán hiển thị, không ép buộc nhập liệu được.
> **B.** Workflow chỉ chạy sau khi đã lưu/convert xong, không có tính năng chặn (block).
> **C.** Process Builder cũng vậy, không dùng để validation và chặn hành động của user.

**💡 Từ khóa ghi nhớ:** `Keywords: Prior to / Enforce / Block -> Validation Rule.`

---

## Câu 139

**🔵 A PrimaryId__c custom field exists on the Candidate__c custom object. The field is used to store each candidate's id number and is marked as Unique in the schema definition. As part of a data enrichment process, Universal Containers has a CSV file that contains updated data for all candidates in the system. The file contains each Candidate's social security number as a data point. Universal Containers wants to upload this information into Salesforce, while ensuring all data rows are correctly mapped to a candidate in the system. Which technique should the developer implement to streamline the data upload?**

- **A.** Update the PrimaryId__c field definition to mark it as an External Id. ✅
- **B.** Upload the CSV into a custom object related to Candidate__c. ❌
- **C.** Create a before save flow to correctly map the records. ❌
- **D.** Create a before insert trigger to correctly map the records. ❌

**📝 Dịch tiếng Việt:**
> Trường tùy chỉnh PrimaryId__c trên Candidate__c dùng để lưu ID ứng viên và được đánh dấu Unique. Để nạp dữ liệu cập nhật từ file CSV một cách nhanh nhất, đảm bảo các bản ghi được khớp đúng, developer nên làm gì?

**💬 Giải thích gốc (English):**
> Marking the PrimaryId__c field as an External Id allows Salesforce to use this field as a unique identifier for matching records during data import. This ensures that the data from the CSV file is correctly mapped to the existing candidate records based on their unique IDs.

**✅ Tại sao đáp án đúng:**
> Sửa định nghĩa trường PrimaryId__c và đánh dấu nó là trường External ID (A). Khi đó, các công cụ như Data Loader có thể sử dụng trường này làm khóa đối chiếu để thực hiện thao tác Upsert (chèn/cập nhật) cực kỳ nhanh chóng và an toàn.

**❌ Tại sao đáp án sai:**
> **B.** Nạp vào custom object phụ rồi viết code map làm tăng độ phức tạp và tốn tài nguyên xử lý dữ liệu.
> **C.** Flow before save không hỗ trợ đối chiếu khóa ngoài trực tiếp lúc nạp file bằng công cụ.
> **D.** Trigger before insert viết code map thủ công rất cồng kềnh và dễ lỗi hơn nhiều so với tính năng External ID có sẵn của hệ thống.

**💡 Từ khóa ghi nhớ:** `Nạp file CSV khớp dữ liệu nhanh gọn no-code -> Đánh dấu trường đối chiếu là EXTERNAL ID.`

---

## Câu 140

**🔵 When a Task is created for a Contact, how can a developer prevent the task from being included on the Activity Timeline of the Contact's Account record?**

- **A.** In Activity Setting, uncheck Roll up activities to a contact's primary account. ✅
- **B.** Create a Task trigger to set the Account field to NULL. ❌
- **C.** Use Process Builder to create a process to set the Task Account field to blank. ❌
- **D.** By default, tasks do not display on the Account Activity Timeline. ❌

**📝 Dịch tiếng Việt:**
> Khi một Task được tạo cho một Contact, làm thế nào để lập trình viên ngăn chặn việc Task này tự động hiển thị trên mục Activity Timeline (Dòng thời gian hoạt động) của Account cha liên quan?

**💬 Giải thích gốc (English):**
> This setting ensures that tasks created for a Contact are not rolled up to the Activity Timeline of the Contact’s associated Account.

**✅ Tại sao đáp án đúng:**
> Trong Salesforce, có một cấu hình hệ thống là 'Roll up activities to a contact's primary account'. Nếu tính năng này được bật, mọi hoạt động của con sẽ bị hiển thị dồn lên cha. Để ngăn chặn điều này, chỉ cần vào Setup -> Activity Settings và bỏ chọn (uncheck) tùy chọn này (A).

**❌ Tại sao đáp án sai:**
> **B.** Set Account field về null trên Task trigger sẽ ngắt kết nối hoàn toàn của Task đó với Account, làm mất dữ liệu quan hệ rất quan trọng chứ không chỉ đơn giản là ẩn timeline.
> **C.** Sử dụng Process Builder để xóa trắng trường Account trên Task cũng phá vỡ quan hệ dữ liệu thô bạo như phương án B.
> **D.** Ngược lại, theo mặc định của Salesforce, các hoạt động của Contact luôn được hiển thị dồn lên timeline của Account cha nếu OWD của Activity bật roll-up.

**💡 Từ khóa ghi nhớ:** `Ẩn Task con trên Timeline của Account cha -> Bỏ chọn 'Roll up activities to a contact's primary account' trong Setup.`

---

## Câu 141

**🔵 What is the requirement for a class to be used as a custom Visualforce controller?**

- **A.** Any top-level Apex class that has a constructor that returns a PageReference ❌
- **B.** Any top-level Apex class that extends a PageReference ❌
- **C.** Any top-level Apex class that has a default, no-argument constructor ✅
- **D.** Any top-level Apex class that implements the controller interface ❌

**📝 Dịch tiếng Việt:**
> Yêu cầu bắt buộc để một lớp Apex có thể được sử dụng làm custom controller cho trang Visualforce là gì?

**💬 Giải thích gốc (English):**
> A custom controller is an Apex class that uses the default, no-argument constructor for the outer, top-level class.

**✅ Tại sao đáp án đúng:**
> Class đó bắt buộc phải là một top-level Apex class (lớp ngoài cùng, không phải inner class) và bắt buộc phải định nghĩa một hàm khởi tạo mặc định không tham số (default, no-argument constructor) (C) để Visualforce có thể tự động instanciate khi trang tải.

**❌ Tại sao đáp án sai:**
> **A.** Hàm khởi tạo (constructor) của class Apex cấm khai báo kiểu trả về (kể cả PageReference), nó chỉ trùng tên class và không có giá trị trả về.
> **B.** Class Apex làm controller không cần và không thể kế thừa lớp PageReference.
> **D.** Không tồn tại một 'controller interface' cụ thể nào bắt buộc Apex class phải implements để làm controller cả.

**💡 Từ khóa ghi nhớ:** `Custom Visualforce Controller -> Class bắt buộc có hàm khởi tạo không tham số mặc định (no-argument constructor).`

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
> Thuộc tính standardController (D) bắt buộc phải được định nghĩa để trang Visualforce nhận đúng ngữ cảnh dữ liệu của đối tượng chứa nút bấm đó (ví dụ standardController='Account' để ghi đè nút Edit của Account).

**❌ Tại sao đáp án sai:**
> **A.** pageReference là kiểu trả về trong Apex, không phải thuộc tính của thẻ <apex:page>.
> **B.** Không có thuộc tính 'override' trong thẻ khai báo <apex:page>.
> **C.** controller dùng để khai báo Custom Controller class, không thể dùng để ghi đè nút bấm chuẩn của đối tượng.

**💡 Từ khóa ghi nhớ:** `Ghi đè action chuẩn (Override button) bằng Visualforce -> Bắt buộc dùng standardController.`

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
> A: Tạo một trang Visualforce tùy chỉnh sử dụng StandardSetController kết hợp với Apex custom button trên list view để xử lý danh sách. B: Cài đặt một managed package từ AppExchange cung cấp sẵn các nút bấm và Enhanced List Views có khả năng chỉnh sửa và xóa hàng loạt cực mạnh.

**❌ Tại sao đáp án sai:**
> **C.** Unmanaged package không được bảo trì nâng cấp và có thể gây xung đột code trong Org, không phải giải pháp tối ưu và an toàn.
> **D.** Tính năng inline editing chuẩn trên list view chỉ hỗ trợ chỉnh sửa và cập nhật hàng loạt, tuyệt đối không hỗ trợ xóa hàng loạt (mass delete) bản ghi.

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
> Áp dụng trigger framework giúp đơn giản hóa việc bổ sung các logic nghiệp vụ theo từng ngữ cảnh sự kiện cụ thể (before insert, after update,...) (D) nhờ việc phân chia code khoa học vào các class Trigger Handler chuyên biệt, giúp code gọn gàng và cực kỳ dễ bảo trì.

**❌ Tại sao đáp án sai:**
> **A.** Trigger framework không làm giảm thời gian thực thi của CPU, thậm chí có thể tăng nhẹ một chút do phải chạy qua các lớp bọc trung gian.
> **B.** Code trigger thông thường không dùng framework vẫn được phủ test bình thường bởi test class.
> **C.** Framework không hề và không thể làm tăng giới hạn governor limit cứng của nền tảng Salesforce.

**💡 Từ khóa ghi nhớ:** `Trigger Framework -> Tổ chức code khoa học, dễ bảo trì và viết logic theo ngữ cảnh sự kiện.`

---

## Câu 145

**🔵 The sales management team at Universal Containers requires that the Lead Source field of the Lead record be populated when a Lead is converted. What should be used to ensure that a user populates the Lead Source field prior to converting a Lead?**

- **A.** Workflow Rule ❌
- **B.** Validation Rule ✅
- **C.** Formula Field ❌
- **D.** Process Builder ❌

**📝 Dịch tiếng Việt:**
> Đảm bảo điền Lead Source trước khi chuyển đổi (convert) Lead?

**💬 Giải thích gốc (English):**
> To ensure that the Lead Source field is populated before a Lead is converted, you should use a Validation Rule. A validation rule can enforce that the Lead Source field is not left blank by preventing the conversion process until the field is populated.

**✅ Tại sao đáp án đúng:**
> Validation Rule giúp chặn lại nếu thiếu dữ liệu khi field IsConverted = true.

**❌ Tại sao đáp án sai:**
> **A.** Formula chỉ để tính toán hiển thị, không ép buộc nhập liệu được.
> **B.** Workflow chỉ chạy sau khi đã lưu/convert xong, không có tính năng chặn (block).
> **C.** Process Builder cũng vậy, không dùng để validation và chặn hành động của user.

**💡 Từ khóa ghi nhớ:** `Keywords: Prior to / Enforce / Block -> Validation Rule.`

---

## Câu 146

**🔵 A company has been adding data to Salesforce and has not done a good job of limiting the creation of duplicate Lead records. The developer is considering writing an Apex process to identify duplicates and merge the records together. Which two statements are valid considerations when using merge? (Choose two.)**

- **A.** The merge method allows up to three records, including the master and two additional records with the same sObject type, to be merged into the master record. ✅
- **B.** Merge is supported with accounts, contacts, cases, and leads. ✅
- **C.** External ID fields can be used with the merge method. ❌
- **D.** The field values on the master record are overwritten by the records being merged. ❌

**📝 Dịch tiếng Việt:**
> Một Org gặp tình trạng tích tụ nhiều bản ghi Lead bị trùng lặp do quản lý dữ liệu kém. Lập trình viên định viết code Apex gộp (merge) chúng lại. Hai lưu ý quan trọng nào khi sử dụng phương thức merge trong Apex? (Chọn 2)

**💬 Giải thích gốc (English):**
> The two valid considerations when using the merge method in Salesforce are:
> The merge method allows up to three records, including the master and two additional records with the same sObject type, to be merged into the master record. This is a key feature of the merge operation, allowing consolidation of up to three records.
> Merge is supported with accounts, contacts, cases, and leads. These are the standard objects that support the merge operation in Salesforce.

**✅ Tại sao đáp án đúng:**
> A: Lệnh merge cho phép gộp tối đa 3 bản ghi (gồm 1 master chính và tối đa 2 bản ghi phụ cùng loại sObject) vào bản ghi master. B: Thao tác DML merge chỉ hỗ trợ chính thức đối với 4 đối tượng tiêu chuẩn là Accounts, Contacts, Cases và Leads.

**❌ Tại sao đáp án sai:**
> **C.** Không thể dùng các trường External ID làm đối số truyền trực tiếp vào phương thức merge, phương thức này bắt buộc nhận vào đối tượng sObject hoặc Id thật.
> **D.** Ngược lại, các giá trị trường trên bản ghi master được giữ lại, các bản ghi phụ bị gộp sẽ bị xóa và đưa vào Recycle Bin.

**💡 Từ khóa ghi nhớ:** `DML Merge: Chỉ hỗ trợ Account, Contact, Case, Lead. Gộp tối đa 3 bản ghi (1 master + 2 phụ).`

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
> Đợt deployment sẽ thất bại hoàn toàn vì trigger có 0% code coverage (D). Quy tắc bắt buộc của Salesforce khi deploy là: **Mỗi file trigger riêng biệt bắt buộc phải có coverage lớn hơn 0%** (ít nhất 1 dòng trigger được chạy thử trong test). Vì test class chỉ gọi trực tiếp class helper mà không tạo bản ghi để kích hoạt trigger nổ, trigger bị 0% coverage nên oẳng.

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
> Ba cân nhắc nào là đúng khi sử dụng annotation @InvocableMethod trong Apex? (Chọn 3)

**💬 Giải thích gốc (English):**
> InvocableMethod Considerations
> The invocable method must be static and public or global, and its class must be an outer class.
> Only one method in a class can have the InvocableMethod annotation.
> Other annotations can’t be used with the InvocableMethod annotation.

**✅ Tại sao đáp án đúng:**
> B: Phải là 'static' để Salesforce gọi được mà không cần khởi tạo class. C: Mỗi class chỉ được phép có duy nhất 1 method gắn tag này. D: Phải có modifier là Public hoặc Global để các công cụ bên ngoài truy cập được.

**❌ Tại sao đáp án sai:**
> **A.** InvocableMethod chỉ chấp nhận DUY NHẤT một tham số đầu vào (thường là List).
> **E.** Không bắt buộc phải có return value (có thể là void).

**💡 Từ khóa ghi nhớ:** `Invocable: Static, 1 method/class, input là List.`

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
> Scratch Orgs là 'xương sống' của Source-driven development. Nó cho phép tạo ra các môi trường tạm thời, cấu hình qua file json để code và test độc lập.

**❌ Tại sao đáp án sai:**
> **A.** Developer Org là org miễn phí trọn đời cho cá nhân, không tích hợp tốt vào quy trình CI/CD chuyên nghiệp.
> **C.** Sandbox vẫn mang nặng tính thủ công và bị giới hạn bởi cấu hình của Production org.
> **D.** Full Copy Sandbox dùng để test performance hoặc User Acceptance Test (UAT) vì nó chứa toàn bộ data, không dùng để dev độc lập.

**💡 Từ khóa ghi nhớ:** `Keyword: Source-driven -> Scratch Orgs.`

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
> B: Lỗi vượt quá giới hạn hàng SOQL (SOQL query row limit) do số lượng Contact quá lớn. D: Lỗi vượt quá giới hạn hàng SOQL do số lượng Account quá lớn. (Vì tổng số hàng tối đa được query trong 1 transaction là 50,000 bản ghi, và trong subquery mỗi bản ghi con Contact được lấy ra cũng bị tính là 1 hàng vào giới hạn này).

**❌ Tại sao đáp án sai:**
> **A.** SOQL query đơn giản không tiêu tốn quá nhiều CPU time của transaction để ném ra CPU limit exception trước khi chạm giới hạn hàng.
> **C.** SOQL query limit exception chỉ xảy ra khi mày gọi lệnh SELECT quá 100 lần trong transaction, ở đây chỉ có duy nhất 1 câu SELECT.

**💡 Từ khóa ghi nhớ:** `SOQL Row Limit = 50,000 hàng. Mỗi bản ghi con trong Subquery cũng ngốn 1 hàng!`

---

## Câu 151

**🔵 Universal Containers wants to assess the advantages of declarative development versus programmatic customization for specific use cases in its Salesforce implementation. What are two advantages of declarative development over programmatic customization? (Choose two.)**

- **A.** Declarative development has higher design limits and query limits. ❌
- **B.** Declarative development does not require Apex test classes. ✅
- **C.** Declarative development does not require maintenance. ❌
- **D.** Declarative development can be updated in production using the Setup UI. ✅

**📝 Dịch tiếng Việt:**
> Universal Containers muốn đánh giá lợi thế của phát triển dạng khai báo (declarative - no code) so với lập trình code (programmatic). Hai ưu điểm nổi bật của declarative là gì? (Chọn 2)

**💬 Giải thích gốc (English):**
> Declarative development does not require Apex test classes: Declarative tools like workflows, process builders, and flows do not require the creation of test classes, which simplifies the development and deployment process.
> Declarative development can be updated in production using the Setup UI: Declarative changes can be made directly in the production environment through the Salesforce Setup UI, allowing for quicker and easier updates without the need for a deployment process.

**✅ Tại sao đáp án đúng:**
> B: Cấu hình dạng khai báo hoàn toàn không yêu cầu viết class test để phủ coverage, tiết kiệm nhiều công sức. D: Admin có thể sửa đổi và cập nhật trực tiếp các công cụ khai báo (như Flow, Workflow) ngay trên môi trường Production thông qua giao diện Setup UI cực nhanh.

**❌ Tại sao đáp án sai:**
> **A.** Cả hai hình thức đều phải chịu chung các giới hạn thiết kế và giới hạn nền tảng của Salesforce.
> **C.** Declarative vẫn cần bảo trì bình thường khi các quy trình nghiệp vụ thay đổi.

**💡 Từ khóa ghi nhớ:** `Lợi thế Declarative (No-code) -> Không cần viết test class + Cho phép chỉnh sửa nóng trực tiếp trên Production.`

---

## Câu 152

**🔵 A developer is asked to create a PDF quote document formatted using the company's branding guidelines, and automatically save it to the Opportunity record. Which two ways should a developer create this functionality? (Choose two.)**

- **A.** Install an application from the AppExchange to generate documents. ✅
- **B.** Create a Visualforce page with custom styling. ✅
- **C.** Create an email template and use it in Process Builder. ❌
- **D.** Create a visual flow that implements the company's formatting. ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên được yêu cầu tạo một file PDF báo giá có định dạng tuân thủ quy chuẩn thương hiệu của công ty, và tự động lưu file đó vào bản ghi Opportunity liên quan. Hai cách nào giúp hiện thực hóa yêu cầu này? (Chọn 2)

**💬 Giải thích gốc (English):**
> The two ways a developer can create this functionality are:
> Install an application from the AppExchange to generate documents: There are several applications available on the AppExchange that can help generate PDF documents with custom branding and save them to records automatically. These apps often come with pre-built templates and functionalities that simplify the process.
> Create a Visualforce page with custom styling: By creating a Visualforce page, a developer can have full control over the styling and formatting of the PDF document. This approach allows for the customization needed to adhere to the company’s branding guidelines

**✅ Tại sao đáp án đúng:**
> A: Cài đặt một ứng dụng chuyên tạo tài liệu từ AppExchange (như Conga Composer). B: Tạo một trang Visualforce sử dụng custom styling CSS và thiết lập thuộc tính renderAs='pdf' để xuất file PDF, viết code Apex tự động lưu file vào Opportunity.

**❌ Tại sao đáp án sai:**
> **C.** Email template không có khả năng tự sinh file PDF định dạng thương hiệu phức tạp và tự lưu vào Opportunity.
> **D.** Flow Builder thuần túy không hỗ trợ thiết kế bố cục tài liệu PDF tùy chỉnh và xuất file trực tiếp no-code.

**💡 Từ khóa ghi nhớ:** `Tạo PDF thương hiệu chuyên nghiệp trong Salesforce -> Dùng Visualforce (renderAs='pdf') hoặc AppExchange Document App.`

---

## Câu 153

**🔵 What should be used to create scratch orgs?**

- **A.** Developer Console ❌
- **B.** Salesforce CLI ✅
- **C.** Workbench ❌
- **D.** Sandbox refresh ❌

**📝 Dịch tiếng Việt:**
> Nên sử dụng công cụ nào để tạo các scratch org?

**💬 Giải thích gốc (English):**
> Salesforce CLI (Command Line Interface) is the tool used to create and manage scratch orgs. It allows developers to easily spin up scratch orgs, configure them, and manage their lifecycle through command-line commands.

**✅ Tại sao đáp án đúng:**
> Scratch Orgs là thành phần cốt lõi của 'Source-driven Development'. Salesforce CLI (SFDX) là công cụ duy nhất cho phép mày ra lệnh tạo, quản lý và xóa Scratch Orgs thông qua terminal hoặc script.

**❌ Tại sao đáp án sai:**
> **A.** Workbench dùng để thao tác dữ liệu và metadata thủ công, không có tính năng tạo Org.
> **C.** Sandbox refresh dùng cho Sandbox truyền thống, không liên quan đến Scratch Org.
> **D.** Developer Console chỉ để viết code và chạy test trong Org hiện tại.

**💡 Từ khóa ghi nhớ:** `Keywords: Scratch Orgs -> Salesforce CLI / SFDX. Nhớ nhé: Scratch Org giống như mì ăn liền, dùng xong bỏ, và CLI là cái ấm đun nước.`

---

## Câu 154

**🔵 Which Apex class contains methods to return the amount of resources that have been used for a particular governor, such as the number of DML statements?**

- **A.** Exception ❌
- **B.** Messaging ❌
- **C.** OrgLimits ❌
- **D.** Limits ✅

**📝 Dịch tiếng Việt:**
> Class Apex nào giúp kiểm tra lượng tài nguyên đã dùng (như số lệnh DML) so với giới hạn Governor?

**💬 Giải thích gốc (English):**
> The Limits methods return the specific limit for the particular governor, such as the number of calls of a method or the amount of heap size remaining.
> Because Apex runs in a multitenant environment, the Apex runtime engine strictly enforces a number of limits to ensure that runaway Apex doesn’t monopolize shared resources.

**✅ Tại sao đáp án đúng:**
> Class `System.Limits` chứa các phương thức như `getDmlStatements()` (đã dùng) và `getLimitDmlStatements()` (tổng cho phép). Nó là 'đồng hồ đo' tài nguyên cho dev.

**❌ Tại sao đáp án sai:**
> **A.** Messaging dùng để gửi email.
> **C.** OrgLimits dùng để check giới hạn của toàn bộ Org (như số lượng API call trong 24h), không phải giới hạn của 1 transaction cụ thể như DML.

**💡 Từ khóa ghi nhớ:** `Check Governor Limits in Code -> Dùng class Limits.`

---

## Câu 155

**🔵 If Apex code executes inside the execute() method of an Apex class when implementing the Batchable interface, which two statements are true regarding governor limits? (Choose two.)**

- **A.** The Apex governor limits are reset for each iteration of the execute() method. ✅
- **B.** The Apex governor limits cannot be exceeded due to the asynchronous nature of the transaction. ❌
- **C.** The Apex governor limits might be higher due to the asynchronous nature of the transaction. ✅
- **D.** The Apex governor limits are relaxed while calling the constructor of the Apex class. ❌

**📝 Dịch tiếng Việt:**
> Nếu mã Apex thực thi bên trong phương thức execute() của một Apex class khi triển khai interface Batchable, hai phát biểu nào sau đây là đúng về governor limits? (Chọn 2)

**💬 Giải thích gốc (English):**
> Each execution of a batch Apex job is considered a discrete transaction, and the governor limits are reset for each transaction.
> Batch Apex operates asynchronously, which can allow for higher governor limits compared to synchronous transactions.

**✅ Tại sao đáp án đúng:**
> C: Mỗi lần execute() chạy một batch (thường là 200 records), Salesforce sẽ cấp một 'hạn mức' mới hoàn toàn. D: Asynchronous Apex (như Batch) có một số limit cao hơn (ví dụ: Heap size 12MB thay vì 6MB).

**❌ Tại sao đáp án sai:**
> **A.** Dù là không đồng bộ thì vẫn có limit, không phải là 'không thể vượt quá'.
> **B.** Constructor của class không được hưởng cơ chế 'relaxed' limits.

**💡 Từ khóa ghi nhớ:** `Batch Apex: Mỗi batch là một transaction riêng biệt. Limit được RESET.`

---

## Câu 156

**🔵 What are three characteristics of change set deployments? (Choose three.)**

- **A.** They require a deployment connection. ✅
- **B.** They can be used to transfer records. ❌
- **C.** They can be used only between related organizations. ✅
- **D.** They can be used to deploy custom settings data. ❌
- **E.** They use an all or none deployment model. ✅

**📝 Dịch tiếng Việt:**
> 3 đặc điểm của Change Set deployment? (Chọn 3)

**💬 Giải thích gốc (English):**
> Change sets can only be sent between Salesforce orgs that have an established deployment connection.
> Change sets can be used only between related organizations, such as a production org and its sandbox, or two sandboxes created from the same production org.
> Change sets are deployed as a single transaction, meaning if any part of the deployment fails, the entire change set is rolled back.

**✅ Tại sao đáp án đúng:**
> C: Cần Connection. D: Deploy kiểu Atomic (được hết hoặc mất sạch). E: Chỉ dùng được trong cùng 1 môi trường (Sandbox -> Prod).

**❌ Tại sao đáp án sai:**
> **A.** Change set không deploy Data, chỉ deploy Metadata.
> **B.** Không dùng để chuyển bản ghi (Records) giữa các Org.

**💡 Từ khóa ghi nhớ:** `Change Set = Metadata Only.`

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
> Cho đoạn code sau thực thi trên nền tảng đa khách thuê (multi-tenant) của Salesforce: [Code SOQL in For]. Lập trình viên nên thực hiện best practice nào để đảm bảo phương thức chạy thành công không bị lỗi giới hạn?

**💬 Giải thích gốc (English):**
> Performing queries inside for loops can lead to hitting governor limits, as it results in a separate query for each iteration of the loop. This can quickly exceed the allowed number of SOQL queries per transaction.

**✅ Tại sao đáp án đúng:**
> Tránh hoàn toàn việc thực hiện truy vấn SOQL bên trong vòng lặp For (A). Việc này sẽ nhanh chóng làm sập hệ thống do vượt giới hạn 100 câu truy vấn SOQL cho phép trong một transaction khi danh sách Id lớn hơn 100.

**❌ Tại sao đáp án sai:**
> **B.** Thêm LIMIT clause không giải quyết được lỗi nổ 100 SOQL query nếu vòng lặp lặp quá nhiều lần.
> **C.** Sử dụng biến truyền làm bộ lọc (:leadId) là cú pháp bind biến vô cùng an toàn và được khuyến khích để chống SOQL Injection.
> **D.** Trả về List rỗng khi không có kết quả là hoàn toàn bình thường, không gây ra lỗi hệ thống.

**💡 Từ khóa ghi nhớ:** `Best Practice SOQL tối thượng: Tuyệt đối không bao giờ viết truy vấn SOQL bên trong vòng lặp For!`

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
> Vòng lặp `do-while` luôn chạy ít nhất một lần. 1. Vào vòng lặp: x = 1. 2. Tăng giá trị: x++ thành 2. 3. Check điều kiện: `while (2 < 1)` là SAI -> Dừng. Kết quả x = 2.

**❌ Tại sao đáp án sai:**
> **A.** x đã bị gán lại bằng 1 ngay dòng đầu của khối `do`.
> **B.** Không có logic nào làm x tăng lên tới 3 trong đoạn code này.
> **D.** Lệnh x++ đã tăng giá trị lên 2 trước khi điều kiện dừng được kiểm tra.

**💡 Từ khóa ghi nhớ:** `Do-while: Cứ đâm đầu vào làm trước, hỏi tội (check điều kiện) sau. Luôn chạy >= 1 lần.`

---

## Câu 159

**🔵 A developer needs to test an Invoicing system integration. After reviewing the number of transactions required for the test, the developer estimates that the test data will total about 2 GB of data storage. Production data is not required for the integration testing. Which two environments meet the requirements for testing? (Choose two)**

- **A.** Developer Sandbox ❌
- **B.** Full Sandbox ✅
- **C.** Developer Edition ❌
- **D.** Partial Sandbox ✅
- **E.** Developer Pro Sandbox ❌

**📝 Dịch tiếng Việt:**
> Developer cần test hệ thống tích hợp hóa đơn. Số lượng giao dịch giả lập ước tính ngốn khoảng 2 GB dung lượng lưu trữ dữ liệu (data storage). Không cần dữ liệu thật từ Production. Hai môi trường Sandbox nào đáp ứng yêu cầu lưu trữ này? (Chọn 2)

**💬 Giải thích gốc (English):**
> Full Sandbox(Data storage: Same as your production org): Full sandboxes are a complete copy of your production org, including all data, metadata, and customizations. This means they can handle large amounts of data and provide a realistic environment for testing integrations.
> Partial Sandbox(Data storage: 5 GB): Partial sandboxes are smaller copies of your production org, but they can still handle a significant amount of data. The exact size limit depends on your organization's specific settings, but partial sandboxes are generally sufficient for testing integrations with moderate amounts of data.

**✅ Tại sao đáp án đúng:**
> B: Full Sandbox (có dung lượng lưu trữ tương đương Org Production thật). D: Partial Sandbox (có dung lượng lưu trữ dữ liệu lên tới 5 GB, thừa sức chứa 2 GB dữ liệu test).

**❌ Tại sao đáp án sai:**
> **A.** Developer Sandbox chỉ có giới hạn lưu trữ dữ liệu cực kỳ ít ỏi là 200 MB, không đủ nhét kẽ răng.
> **C.** Developer Edition là môi trường phát triển cá nhân miễn phí chỉ có 20 MB bộ nhớ dữ liệu.
> **E.** Developer Pro Sandbox chỉ hỗ trợ tối đa 1 GB bộ nhớ dữ liệu, vẫn không đủ chứa 2 GB.

**💡 Từ khóa ghi nhớ:** `Dung lượng dữ liệu Sandbox: Developer (200MB) -> Dev Pro (1GB) -> Partial (5GB) -> Full (Bằng Production).`

---

## Câu 160

**🔵 Universal Containers hires a developer to build a custom search page to help users find the Accounts they want. Users will be able to search on Name, Description, and a custom comments field. Which consideration should the developer be aware of when deciding between SOQL and SOSL? (Choose two.)**

- **A.** SOSL is faster for text searches. ✅
- **B.** SOQL is able to return more records. ✅
- **C.** SOQL is faster for text searches. ❌
- **D.** SOSL is able to return more records. ❌

**📝 Dịch tiếng Việt:**
> Universal Containers muốn xây dựng trang tìm kiếm Account tùy chỉnh cho phép tìm kiếm theo Name, Description và custom comments field. Lập trình viên nên lưu ý hai điều nào khi cân nhắc lựa chọn giữa SOQL và SOSL? (Chọn 2)

**💬 Giải thích gốc (English):**
> SOQL vs. SOSL Queries
> Search can be accessed with SOQL or SOSL queries. SOQL is Force.com's database query language, similar to SQL. You can use SOQL to query child-to-parent relationships, which are often many-to-one, and to query parent-to-child relationships, which are almost always one-to-many.
> SOSL is Force.com's full-text search language. SOSL can tokenize multiple terms within a field, and can build a search index off of this. If you’re searching for a specific distinct term that you know exists within a field, you might find SOSL faster than SOQL. However, for each Apex transaction, the governor limit for multiple SOSL searches in a single transaction is 2,000 (Note: It is common to only need a single search, in which case the limit is 40,000); for SOQL queries it’s 50,000. So if you need to retrieve more than 2,000 records, SOQL is the better choice.

**✅ Tại sao đáp án đúng:**
> A: SOSL tìm kiếm chuỗi văn bản tự do (text search) nhanh hơn nhiều nhờ cơ chế lập chỉ mục từ khóa chuyên dụng. B: SOQL có khả năng trả về nhiều bản ghi hơn trong một lần truy vấn (giới hạn SOQL tối đa 50,000 hàng, trong khi SOSL giới hạn trả về tối đa 2,000 hàng cho mỗi sObject).

**❌ Tại sao đáp án sai:**
> **C.** Ngược lại, SOQL tìm kiếm các trường text lớn (như Description, Comments) bằng toán tử LIKE sẽ rất chậm vì phải quét toàn bộ bảng dữ liệu vật lý.
> **D.** SOSL bị giới hạn trả về tối đa 2,000 bản ghi, ít hơn nhiều so với 50,000 của SOQL.

**💡 Từ khóa ghi nhớ:** `So sánh: Tìm kiếm từ khóa tự do trên trường text lớn -> Dùng SOSL (Nhanh hơn). Cần lấy nhiều bản ghi -> Dùng SOQL (Giới hạn lớn hơn).`

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
> Đoạn code trên bị bắn lỗi DML Exception. Lập trình viên nên sửa thế nào để xử lý lỗi một cách êm đẹp?

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
> Sử dụng cấu trúc Try/Catch là cách tiêu chuẩn để 'bắt' lỗi khi thực hiện DML. Nếu có lỗi, code trong phần Catch sẽ chạy thay vì làm cả hệ thống 'văng' lỗi ra màn hình người dùng.

**❌ Tại sao đáp án sai:**
> **A.** Lỗi có thể đến từ Validation Rule hoặc Duplicate Rule, chứ không chỉ là list có null.
> **B.** Upsert chỉ giúp chọn giữa Insert hoặc Update, không liên quan đến việc xử lý lỗi ngoại lệ (Exception).
> **D.** CDC là tính năng đồng bộ dữ liệu real-time, không phải công cụ xử lý lỗi trong code Apex.

**💡 Từ khóa ghi nhớ:** `Graceful handling = Try/Catch. Đừng để User thấy cái màn hình lỗi đỏ lòm của Salesforce!`

---

## Câu 162

**🔵 When using SalesforceDX, what does a developer need to enable to create and manage scratch orgs?**

- **A.** Production ❌
- **B.** Environment Hub ❌
- **C.** Dev Hub ✅
- **D.** Sandbox ❌

**📝 Dịch tiếng Việt:**
> Để dùng Scratch Org trong SFDX, mày cần bật tính năng gì?

**💬 Giải thích gốc (English):**
> To create and manage scratch orgs using SalesforceDX, a developer needs to enable the Dev Hub. The Dev Hub is the central place for managing your scratch orgs and is essential for using SalesforceDX tools.

**✅ Tại sao đáp án đúng:**
> Mày phải bật 'Dev Hub' trong một Org xịn (Production hoặc Business). Org này sẽ quản lý việc 'đẻ' ra và kiểm soát các Scratch Orgs con.

**❌ Tại sao đáp án sai:**
> **C.** Sandbox là Org truyền thống, không có chức năng tạo Scratch Org.
> **D.** Environment Hub dùng để quản lý nhiều Org khác nhau nhưng không phải là điều kiện tiên quyết để tạo scratch org cho SFDX.

**💡 Từ khóa ghi nhớ:** `Scratch Org = Mì ăn liền; Dev Hub = Cái ấm đun nước.`

---

## Câu 163

**🔵 Where are two locations a developer can look to find information about the status of batch or future calls? (Choose two.)**

- **A.** Developer Console ❌
- **B.** Apex Flex Queue ✅
- **C.** Apex Jobs ✅
- **D.** Paused Flow Interviews component ❌

**📝 Dịch tiếng Việt:**
> Hai vị trí nào mà lập trình viên có thể tìm thấy thông tin về trạng thái của các phương thức batch hoặc future?

**💬 Giải thích gốc (English):**
> The Apex Jobs page shows all asynchronous Apex jobs with information about each job’s execution. You can also monitor the status of Apex jobs in the Apex Flex Queue, and reorder them to control which jobs are processed first.

**✅ Tại sao đáp án đúng:**
> D: Apex Jobs hiển thị mọi tác vụ không đồng bộ. C: Apex Flex Queue hiển thị các Batch job đang nằm chờ trước khi xử lý.

**❌ Tại sao đáp án sai:**
> **A.** Paused Flow Interviews chỉ hiển thị các luồng Flow đang bị tạm dừng, không liên quan đến Batch hay Future Apex.
> **B.** Time-Based Workflow Monitor chỉ dùng để theo dõi các Workflow Rule có cài đặt thời gian thực hiện (Time-dependent actions).

**💡 Từ khóa ghi nhớ:** `Keyword: Monitor Async Apex -> Apex Jobs & Flex Queue.`

---

## Câu 164

**🔵 A Salesforce Administrator used Flow Builder to create a flow named 'accountOnboarding'. The flow must be used inside an Aura component. Which tag should a developer use to display the flow in the component?**

- **A.** lightning-flow ❌
- **B.** aura-flow ❌
- **C.** lightning:flow ✅
- **D.** aura:flow ❌

**📝 Dịch tiếng Việt:**
> Admin tạo một Flow tên là 'accountOnboarding'. Để nhúng Flow này vào một Aura Component, mày dùng tag nào?

**💬 Giải thích gốc (English):**
> To display a flow inside an Aura component, the developer should use the <lightning:flow> tag. This tag is specifically designed to embed flows within Aura components.

**✅ Tại sao đáp án đúng:**
> Trong Aura, tag chuẩn để chứa và chạy Flow là `<lightning:flow />`. Mày chỉ cần truyền `flowName` vào là xong.

**❌ Tại sao đáp án sai:**
> **A.** lightning-flow (dùng dấu gạch ngang) là cú pháp của LWC, không phải Aura.
> **B.** aura-flow là hàng giả, Salesforce không có tag này.
> **C.** aura:flow là cái tên nghe có vẻ đúng nhưng thực tế namespace `aura:` chỉ dành cho các tag điều khiển logic cốt lõi, không có tag flow.

**💡 Từ khóa ghi nhớ:** `Aura dùng dấu hai chấm (:), LWC dùng dấu gạch ngang (-). Nhớ kỹ để không bị lừa!`

---

## Câu 165

**🔵 A developer must create a CreditCardPayment class that provides an implementation of an existing Payment class.
public virtual class Payment{
public virtual void makePayment(Decimal amount){ /*implementation*/}
}
Which is the correct implementation?
A.
public class CreditCardPayment extends Payment{
public virtual void makePayment(Decimal amount){ /*implementation*/}
}
B.
public class CreditCardPayment extends Payment{
public override void makePayment(Decimal amount){ /*implementation*/}
}
C.
public class CreditCardPayment implements Payment{
public virtual void makePayment(Decimal amount){ /*implementation*/}
}
D.
public class CreditCardPayment implements Payment{
public override void makePayment(Decimal amount){ /*implementation*/}
}**


**📝 Dịch tiếng Việt:**
> Developer cần tạo class CreditCardPayment kế thừa từ class Payment ảo có sẵn: [Payment Class]. Khai báo nào sau đây là đúng cú pháp?

**💬 Giải thích gốc (English):**
> The CreditCardPayment class should extend the Payment class and override the makePayment method to provide its specific implementation.

**✅ Tại sao đáp án đúng:**
> Vì lớp cha Payment là một class thông thường được gắn từ khóa 'virtual class' chứ không phải Interface, nên class con bắt buộc phải dùng từ khóa 'extends' để kế thừa. Để ghi đè phương thức makePayment(), class con phải dùng từ khóa 'override' (B).

**❌ Tại sao đáp án sai:**
> **A.** Dùng lại từ khóa 'virtual' ở class con là sai cú pháp ghi đè phương thức.
> **C.** Dùng từ khóa 'implements' chỉ dành cho việc hiện thực hóa các lớp Interface, dùng cho class thường sẽ báo lỗi biên dịch.
> **D.** Tương tự C, sử dụng sai từ khóa implements.

**💡 Từ khóa ghi nhớ:** `Kế thừa Class -> Dùng EXTENDS + OVERRIDE. Hiện thực hóa Interface -> Dùng IMPLEMENTS.`

---

## Câu 166

**🔵 How should a developer make sure that a child record on a custom object, with a lookup to the Account object, has the same sharing access as its associated account?**

- **A.** Create a Sharing Rule comparing the custom object owner to the account owner. ❌
- **B.** Create a validation rule on the custom object comparing the record owners on both records. ❌
- **C.** Include the sharing related list on the custom object page layout. ❌
- **D.** Ensure that the relationship between the objects is Master-Detail. ✅

**📝 Dịch tiếng Việt:**
> Làm thế nào để lập trình viên đảm bảo một bản ghi con tùy chỉnh (có trường Lookup trỏ đến Account) luôn có chung quyền hạn chia sẻ (sharing access) giống hệt với Account cha liên quan?

**💬 Giải thích gốc (English):**
> When you set up a Master-Detail relationship, the child record inherits the sharing and security settings of the parent record. This means that if a user has access to the parent record (in this case, the Account), they will automatically have the same level of access to the child records (the custom object records).

**✅ Tại sao đáp án đúng:**
> Đảm bảo rằng mối quan hệ giữa hai đối tượng là mối quan hệ Master-Detail (D). Trong Salesforce, bản ghi con Detail luôn tự động kế thừa 100% cấu hình bảo mật và chia sẻ (Sharing/Security) từ bản ghi cha Master mà không cần viết code.

**❌ Tại sao đáp án sai:**
> **A.** Viết sharing rule đối chiếu owner rất phức tạp, dễ lỗi và không tự động cập nhật mượt mà khi đổi chủ như Master-Detail.
> **B.** Validation rule chỉ dùng để chặn lưu bản ghi sai điều kiện, không có khả năng phân phối quyền chia sẻ bảo mật.
> **C.** Thêm Sharing Related List chỉ để hiển thị nút phân quyền thủ công trên giao diện, không giúp tự động đồng bộ bảo mật.

**💡 Từ khóa ghi nhớ:** `Con muốn thừa kế hoàn hảo quyền bảo mật của Cha -> Bắt buộc thiết lập quan hệ MASTER-DETAIL.`

---

## Câu 167

**🔵 Universal Containers wants a list button to display a Visualforce page that allows users to edit multiple records. Which Visualforce feature supports this requirement?**

- **A.** <apex:listButton> tag ❌
- **B.** recordSetVar page attribute ✅
- **C.** custom controller ❌
- **D.** controller extension ❌

**📝 Dịch tiếng Việt:**
> Tính năng VF nào giúp sửa nhiều bản ghi cùng lúc từ một list button?

**💬 Giải thích gốc (English):**
> The recordSetVar attribute in Visualforce allows you to work with a collection of records. This is particularly useful for creating pages that enable users to edit multiple records at once. By using recordSetVar, you can pass a set of records to your Visualforce page and then iterate over them to display and edit each record.

**✅ Tại sao đáp án đúng:**
> Đó là thuộc tính recordSetVar. Khi mày khai báo nó, Standard Controller sẽ biến hình thành Standard List Controller, cho phép mày hốt trọn danh sách các bản ghi được chọn từ List View.

**❌ Tại sao đáp án sai:**
> **A.** Custom controller phải tự viết logic lấy list cực khổ, không có sẵn như recordSetVar.
> **D.** <apex:listButton> chỉ để hiện cái nút, không xử lý data cho mày.

**💡 Từ khóa ghi nhớ:** `Keyword: List Button / Edit Multiple -> recordSetVar.`

---

## Câu 168

**🔵 Which code in a Visualforce page and/or controller might present a security vulnerability?
A . <apex:outputField value="{!ctrl.userInput}" />
B . <apex:outputText escape="false" value=" {!$CurrentPage.parameters.userInput}" />
C . <apex:outputText value="{!£CurrentPage.parameters.userInput}" />
D . <apex:outputField escape="false" value="{!ctrl.userInput}" />**


**📝 Dịch tiếng Việt:**
> Đoạn code nào trong trang Visualforce hoặc Controller dưới đây có thể gây ra lỗ hổng bảo mật nghiêm trọng?

**💬 Giải thích gốc (English):**
> Disabling Escape on Visualforce Tags
> By default, nearly all Visualforce tags escape the XSS-vulnerable characters. You can disable this behavior by setting the optional attribute escape="false". For example, this output is vulnerable to XSS attacks. When escape="false" is used, the input is not escaped, meaning any HTML or JavaScript code included in the user input will be rendered as-is, potentially allowing malicious scripts to be executed.

**✅ Tại sao đáp án đúng:**
> Cú pháp B: <apex:outputText escape='false' value=' {!$CurrentPage.parameters.userInput}' />. Thuộc tính escape='false' tắt cơ chế tự động mã hóa ký tự độc hại của Visualforce, kết hợp với việc in trực tiếp dữ liệu thô do người dùng nhập từ URL parameter ($CurrentPage.parameters.userInput) sẽ tạo ra lỗ hổng tấn công Cross-Site Scripting (XSS) cực kỳ nguy hiểm.

**❌ Tại sao đáp án sai:**
> **A.** Thẻ <apex:outputField> mặc định cực kỳ an toàn, tự động mã hóa XSS và tôn trọng phân quyền FLS của người dùng.
> **C.** Thẻ <apex:outputText> mặc định không khai báo escape='false' sẽ tự động mã hóa an toàn tất cả ký tự HTML/JS do người dùng nhập.
> **D.** Tắt escape trên thẻ <apex:outputField> tuy không khuyến khích nhưng an toàn hơn nhiều so với <apex:outputText> vì outputField chỉ hiển thị dữ liệu của trường đã được lưu trữ và có kiểm duyệt kiểu dữ liệu trong DB.

**💡 Từ khóa ghi nhớ:** `Visualforce dính XSS bảo mật -> Tìm thẻ có 'escape=false' + tham số URL đầu vào người dùng.`

---

## Câu 169

**🔵 What should a developer do to check the code coverage of a class after running all tests?**

- **A.** Select and run the class on the Apex Test Execution page in the Developer Console. ❌
- **B.** View the code coverage percentage for the class using the Overall Code Coverage panel in the Developer Console Tests tab. ✅
- **C.** View the Code Coverage column in the list view on the Apex Classes page. ❌
- **D.** View the Class Test Percentage tab on the Apex Class list view in Salesforce Setup. ❌

**📝 Dịch tiếng Việt:**
> Chạy test xong hết rồi, giờ muốn xem cái class của mình được bao nhiêu % coverage thì xem ở đâu cho nhanh?

**💬 Giải thích gốc (English):**
> After running tests, the Developer Console provides a comprehensive view of code coverage. The Overall Code Coverage panel in the Tests tab displays the code coverage percentage for each Apex class that has been included in a test run.

**✅ Tại sao đáp án đúng:**
> B đúng vì trong Setup -> Apex Classes, có một cột tên là 'Code Coverage' hiển thị trực tiếp con số % cho mày xem. Rất trực quan và nhanh chóng.

**❌ Tại sao đáp án sai:**
> **A.** Cái tab này không có thật, Salesforce bịa ra để lừa mày đấy.
> **C.** Panel này trong Dev Console hiển thị tổng coverage của cả Org, không phải của riêng lẻ từng class mày đang cần soi.
> **D.** Cái này là để CHẠY test, không phải để XEM kết quả coverage sau khi chạy.

**💡 Từ khóa ghi nhớ:** `Mẹo PD1: Xem coverage nhanh nhất là ra list view của Apex Classes trong Setup.`

---

## Câu 170

**🔵 Universal Containers decides to use exclusively declarative development to build out a new Salesforce application. Which three options should be used to build out the database layer for the application? (Choose three.)**

- **A.** Flows ❌
- **B.** Roll-up summaries ✅
- **C.** Triggers ❌
- **D.** Relationships ✅
- **E.** Custom objects and fields ✅

**📝 Dịch tiếng Việt:**
> Universal Containers quyết định sử dụng hoàn toàn các tính năng khai báo no-code để xây dựng một ứng dụng Salesforce mới. Ba lựa chọn nào nên được sử dụng để xây dựng lớp Cơ sở dữ liệu (Database Layer) cho ứng dụng này? (Chọn 3)

**💬 Giải thích gốc (English):**
> Database Layer
> Declarative: Custom Objects, Fields, Relationships, Rollups
> Coding: Apex Triggers

**✅ Tại sao đáp án đúng:**
> B: Roll-up summaries (tính tổng/đếm từ con lên cha). D: Relationships (các trường quan hệ lookup/master-detail). E: Custom objects and fields (các đối tượng và trường dữ liệu tùy chỉnh). Đây là các khối xây dựng cơ sở dữ liệu vật lý hoàn toàn no-code trong Salesforce.

**❌ Tại sao đáp án sai:**
> **A.** Flows thuộc về tầng xử lý logic nghiệp vụ và tự động hóa quy trình (Logic/Controller Layer), không thuộc lớp định nghĩa cấu trúc cơ sở dữ liệu.
> **C.** Triggers là code Apex thuộc tầng xử lý logic (programmatic controller), không phải khai báo no-code.

**💡 Từ khóa ghi nhớ:** `Database Layer dạng khai báo (No-code) -> Objects/Fields, Relationships, Roll-up Summaries.`

---

## Câu 171

**🔵 Which three statements are true regarding the @isTest annotation? (Choose three.)**

- **A.** A method annotated @isTest(SeeAllData=true) in a class annotated @isTest(SeeAllData=false) has access to all org data. ✅
- **B.** A method annotated @isTest(SeeAllData=false) in a class annotated @isTest(SeeAllData=true) has access to all org data. ❌
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
> A: Cấu hình SeeAllData=true cấp phương thức sẽ override cấu hình SeeAllData=false cấp class để truy cập dữ liệu thật. B: Lớp cha đã mở SeeAllData=true thì phương thức con không thể đóng lại bằng SeeAllData=false (bị ignore và vẫn có quyền truy cập dữ liệu thực). E: Các đối tượng Metadata/Setup hệ thống như Profile, User, RecordType luôn hiển thị trong test class bất kể SeeAllData là true hay false.

**❌ Tại sao đáp án sai:**
> **C.** Các test class có gắn @isTest hoàn toàn được MIỄN PHÍ dung lượng lưu trữ, không hề bị tính vào giới hạn 3 MB code Apex của Org.
> **D.** Products và Pricebooks trong các phiên bản Salesforce hiện đại đã bị cô lập dữ liệu, bắt buộc phải tạo data test giả lập hoặc bật SeeAllData=true mới thấy.

**💡 Từ khóa ghi nhớ:** `Mẹo @isTest: Class test được miễn phí dung lượng code 3MB. SeeAllData=true cha mở thì con không thể đóng!`

---

## Câu 172

**🔵 The Job_Application__c custom object has a field that is a Master-Detail relationship to the Contact object, where the Contact object is the Master. As part of a feature implementation, a developer needs to retrieve a list containing all Contact records where the related Account Industry is 'Technology' while also retrieving the contact's Job_Application__c records. Based on the object's relationships, what is the most efficient statement to retrieve the list of contacts?**

- **A.** [SELECT Id, (SELECT Id FROM Job_Applications_r) FROM Contact WHERE Account.Industry = 'Technology']; ✅
- **B.** [SELECT Id, (SELECT Id FROM Job_Applications_r) FROM Contact WHERE Accounts.Industry = 'Technology']; ❌
- **C.** [SELECT Id, (SELECT Id FROM Job_Applications_c) FROM Contact WHERE Accounts.Industry = 'Technology']; ❌
- **D.** [SELECT Id, (SELECT Id FROM Job_Application_c) FROM Contact WHERE Account.Industry = 'Technology']; ❌

**📝 Dịch tiếng Việt:**
> Job_Application__c có quan hệ Master-Detail với Contact (Contact là Master). Developer cần truy vấn toàn bộ bản ghi Contact có Account Industry là 'Technology', đồng thời lấy kèm danh sách Job_Application__c con liên quan. Cú pháp SOQL nào là tối ưu nhất?

**💬 Giải thích gốc (English):**
> A: This query correctly references the relationship and filters based on the Account’s Industry
> B: This option is incorrect because the correct relationship name for the Account object is Account, not Accounts.
> C: This option is incorrect for two reasons: it uses Accounts instead of Account, and it incorrectly references Job_Applications_c instead of Job_Applications_r.
> D: This option is incorrect because it uses Job_Application_c instead of Job_Applications_r.

**✅ Tại sao đáp án đúng:**
> Cú pháp A: [SELECT Id, (SELECT Id FROM Job_Applications__r) FROM Contact WHERE Account.Industry = 'Technology']. Cú pháp này sử dụng đúng tên mối quan hệ con ở dạng số nhiều và có đuôi '__r' (Job_Applications__r), đồng thời đi xuyên lên cha Account ở dạng số ít cực kỳ chính xác.

**❌ Tại sao đáp án sai:**
> **B.** Sử dụng tên cha dạng số nhiều 'Accounts.Industry' là sai cú pháp truy vấn mối quan hệ.
> **C.** Dùng đuôi '__c' (Job_Applications_c) cho subquery con là sai, quan hệ con bắt buộc dùng đuôi '__r'.
> **D.** Dùng tên quan hệ con dạng số ít 'Job_Application_c' vừa thiếu chữ 's' vừa sai đuôi '__r'.

**💡 Từ khóa ghi nhớ:** `SOQL con lên cha -> Tên cha số ít (Account.Name). SOQL cha xuống con -> subquery số nhiều đuôi '__r' (Job_Applications__r).`

---

## Câu 173

**🔵 Which two SOSL searches will return records matching search criteria contained in any of the searchable text fields on an object? (Choose two.)**

- **A.** [FIND 'Acme*' IN ANY FIELDS RETURNING Account, Opportunity]; ❌
- **B.** [FIND 'Acme*' RETURNING Account, Opportunity]; ✅
- **C.** [FIND 'Acme*' IN ALL FIELDS RETURNING Account, Opportunity]; ✅
- **D.** [FIND 'Acme*' IN TEXT FIELDS RETURNING Account, Opportunity]; ❌

**📝 Dịch tiếng Việt:**
> Hai câu lệnh tìm kiếm SOSL nào sẽ thực hiện tìm kiếm từ khóa trên tất cả các trường văn bản được hỗ trợ tìm kiếm của một đối tượng? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> B: [FIND 'Acme*' RETURNING Account, Opportunity] - khi không khai báo phạm vi, hệ thống tự động ngầm định tìm trên toàn bộ các trường text. C: [FIND 'Acme*' IN ALL FIELDS RETURNING Account, Opportunity] - khai báo tường minh phạm vi tìm kiếm trên tất cả các trường.

**❌ Tại sao đáp án sai:**
> **A.** Không tồn tại từ khóa 'IN ANY FIELDS' trong cú pháp chuẩn của ngôn ngữ SOSL.
> **D.** Không có từ khóa 'IN TEXT FIELDS' trong cú pháp của SOSL, chỉ có ALL FIELDS, NAME FIELDS, EMAIL FIELDS, PHONE FIELDS, SIDEBAR FIELDS.

**💡 Từ khóa ghi nhớ:** `SOSL mặc định tìm kiếm -> IN ALL FIELDS (hoặc không viết gì).`

---

## Câu 174

**🔵 A developer needs to save a List of existing Account records named myAccounts to the database, but the records do not contain Salesforce Id values. Only the value of a custom text field configured as an External ID with an API name of Foreign_Key__c is known. Which two statements enable the developer to save the records to the database without an Id? (Choose two.)**

- **A.** Upsert myAccounts Foreign_Key__c; ✅
- **B.** Upsert myAccounts(Foreign_Key__c); ❌
- **C.** Database.upsert (myAccounts, Foreign_Key__c); ✅
- **D.** Database.upsert(myAccounts).Foreign_Key__c; ❌

**📝 Dịch tiếng Việt:**
> Developer cần upsert một danh sách Account tên myAccounts nhưng không có ID Salesforce. Các bản ghi chỉ có một trường text Unique đóng vai trò External ID tên là Foreign_Key__c. Hai câu lệnh nào thực thi thành công? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> A: Sử dụng cú pháp DML truyền thống: 'upsert myAccounts Foreign_Key__c;'. C: Sử dụng phương thức của lớp Database: 'Database.upsert(myAccounts, Foreign_Key__c);'. Đây là hai cách chuẩn mực để chỉ định trường External ID làm khóa đối chiếu khi thực hiện Upsert.

**❌ Tại sao đáp án sai:**
> **B.** Cú pháp DML truyền thống dùng dấu ngoặc đơn quanh tên trường là sai quy chuẩn biên dịch của Apex.
> **D.** Gọi thuộc tính Foreign_Key__c chấm phía sau phương thức Database.upsert là hoàn toàn sai cú pháp lập trình.

**💡 Từ khóa ghi nhớ:** `Cú pháp Upsert bằng External ID -> 1. upsert list ExternalField__c; 2. Database.upsert(list, ExternalField__c);`

---

## Câu 175

**🔵 How should a developer avoid hitting the governor limits in test methods?**

- **A.** Use @TestVisible on methods that create records. ❌
- **B.** Use Test.loadData() to load data from a static resource. ❌
- **C.** Use @IsTest (SeeAllData=true) to use existing data. ❌
- **D.** Use Test.startTest() to reset governor limits. ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên nên làm gì để tránh việc bị chạm giới hạn governor limits (như SOQL/DML) trong các phương thức test?

**💬 Giải thích gốc (English):**
> The Test.startTest() and Test.stopTest() methods are used to reset governor limits within test methods. This allows the developer to perform setup operations before Test.startTest() and then execute the actual test code within the new set of governor limits.

**✅ Tại sao đáp án đúng:**
> Sử dụng phương thức Test.startTest() và Test.stopTest() (D). Hàm startTest() sẽ cấp riêng một bộ đếm giới hạn governor limit mới tinh và độc lập cho đoạn code chạy bên trong nó, giúp cô lập hoàn toàn giới hạn của khâu chuẩn bị dữ liệu mẫu.

**❌ Tại sao đáp án sai:**
> **A.** @TestVisible chỉ giúp test class nhìn thấy các biến/method private của class chính, không giúp reset hay tối ưu hóa giới hạn limit.
> **B.** Test.loadData() giúp nạp nhanh dữ liệu test từ Static Resource CSV, không có tính năng reset hay cấp mới bộ đếm limit.
> **C.** SeeAllData=true làm test truy cập dữ liệu thật, không có tác động gì đến việc nới rộng hay reset giới hạn governor limit.

**💡 Từ khóa ghi nhớ:** `Muốn reset cấp mới giới hạn governor limit trong test class -> Bọc code vào Test.startTest() và Test.stopTest().`

---

## Câu 176

**🔵 Universal Containers wants Opportunities to be locked from editing when reaching the Closed/Won stage. Which two strategies should a developer use to accomplish this? (Choose two.)**

- **A.** Use a Flow Builder. ❌
- **B.** Use a validation rule. ✅
- **C.** Use the Process Automation Settings. ❌
- **D.** Mark fields as read-only on the page layout. ✅

**📝 Dịch tiếng Việt:**
> Universal Containers muốn khóa Opportunities không cho phép chỉnh sửa khi đã chuyển sang trạng thái Closed/Won. Hai chiến lược nào lập trình viên nên sử dụng để thực hiện việc này? (Chọn 2)

**💬 Giải thích gốc (English):**
> Using a validation rule  and marking fields as read-only on the page layout are indeed effective strategies to lock Opportunities from editing when they reach the Closed/Won stage.

**✅ Tại sao đáp án đúng:**
> B: Tạo một Validation Rule kiểm tra nếu trạng thái cũ là Closed/Won thì chặn chỉnh sửa. D: Cấu hình Page Layout với tất cả các trường là Read-only đối với Record Type thuộc trạng thái Closed/Won.

**❌ Tại sao đáp án sai:**
> **A.** Flow Builder không thể khóa cứng các thao tác chỉnh sửa trực tiếp trên giao diện người dùng một cách tối ưu như Validation Rule.
> **C.** Process Automation Settings dùng để cấu hình chung cho hệ thống tự động hóa, không hỗ trợ logic khóa bản ghi cụ thể.

**💡 Từ khóa ghi nhớ:** `Khóa bản ghi (Read-only) -> 1. Validation Rule (Chặn lưu); 2. Page Layout Read-only (Khóa UI).`

---

## Câu 177

**🔵 A developer wants to display all of the picklist entries for the Opportunity StageName field and all of the available record types for the Opportunity object on a Visualforce page. Which two actions should the developer perform to get the available picklist values and record types in the controller? (Choose two.)**

- **A.** Use Schema.RecordTypeInfo returned by Opportunity.SObjectType.getDescribe().getRecordTypeInfos(). ✅
- **B.** Use Schema.PicklistEntry returned by Opportunity.SObjectType.getDescribe().getPicklistValues (). ❌
- **C.** Use Schema.RecordTypeInfo returned by RecordType.SObjectType.getDescribe().getRecordTypeInfos(). ❌
- **D.** Use Schema.PicklistEntry returned by Opportunity.StageName.getDescribe().getPicklistValues (). ✅

**📝 Dịch tiếng Việt:**
> Developer muốn hiển thị toàn bộ giá trị picklist của trường StageName trên Opportunity và toàn bộ Record Types hiện có của Opportunity lên trang Visualforce. Hai hành động nào giúp lấy các thông tin này trong controller? (Chọn 2)

**💬 Giải thích gốc (English):**
> Use Schema.RecordTypeInfo returned by Opportunity.SObjectType.getDescribe().getRecordTypeInfos(): This will retrieve the available record types for the Opportunity object.
> Use Schema.PicklistEntry returned by Opportunity.StageName.getDescribe().getPicklistValues(): This will retrieve the picklist entries for the Opportunity StageName field.

**✅ Tại sao đáp án đúng:**
> A: Lấy Record Types bằng cách describe đối tượng Opportunity: 'Opportunity.SObjectType.getDescribe().getRecordTypeInfos()'. D: Lấy các giá trị picklist bằng cách describe trực tiếp trường StageName của Opportunity: 'Opportunity.StageName.getDescribe().getPicklistValues()'.

**❌ Tại sao đáp án sai:**
> **B.** Không thể gọi getPicklistValues() từ mô tả sObject Opportunity cấp cao được, bắt buộc phải describe cấp trường (Field).
> **C.** Describe đối tượng RecordType hệ thống chỉ trả về Record Type của chính bảng RecordType đó chứ không trả về danh sách Record Type của đối tượng Opportunity.

**💡 Từ khóa ghi nhớ:** `Lấy Record Types -> Đối tượng.getDescribe().getRecordTypeInfos(). Lấy Picklist -> Trường.getDescribe().getPicklistValues().`

---

## Câu 178

**🔵 An org has two custom objects: Plan__c, that has a master-detail relationship to the Account object Plan_Item__c, that has a master-detail relationship to the Plan__c object. What should a developer use to create a Visualforce section on the Account page layout that displays all of the Plan__c records related to the Account and all of the Plan_Item__c records related to those Plan__c records?**

- **A.** A standard controller with a custom controller ❌
- **B.** A standard controller with a controller extension ✅
- **C.** A controller extension with a custom controller ❌
- **D.** A custom controller by itself ❌

**📝 Dịch tiếng Việt:**
> Org có 2 custom object: Plan__c (quan hệ Master-Detail với Account) và Plan_Item__c (quan hệ Master-Detail với Plan__c). Lập trình viên nên sử dụng gì để tạo một section Visualforce hiển thị Plan__c của Account và toàn bộ Plan_Item__c liên quan trực tiếp trên trang Account layout?

**💬 Giải thích gốc (English):**
> Using a standard controller for the Account object allows you to leverage built-in functionality, while a controller extension can be used to add custom logic to retrieve and display the related Plan__c and Plan_Item__c records.

**✅ Tại sao đáp án đúng:**
> Sử dụng một Standard Controller kết hợp với một Controller Extension (B). Vì trang này được nhúng trực tiếp trên Account Layout nên bắt buộc phải dùng standardController='Account'. Để xử lý hiển thị cấu trúc dữ liệu cha-con-cháu phức tạp, ta viết thêm Controller Extension class để query dữ liệu.

**❌ Tại sao đáp án sai:**
> **A.** Không thể khai báo đồng thời cả Custom Controller và Standard Controller độc lập trong cùng một trang Visualforce.
> **C.** Controller extension bắt buộc phải đi kèm với một standardController hoặc custom controller chứ không thể đi kèm custom controller độc lập.
> **D.** Dùng Custom Controller đơn lẻ sẽ làm mất khả năng nhúng trực tiếp trang Visualforce vào page layout chuẩn của Account.

**💡 Từ khóa ghi nhớ:** `Nhúng trang Visualforce vào Layout chuẩn + Viết thêm logic query nâng cao -> Dùng Standard Controller + Controller Extension.`

---

## Câu 179

**🔵 A developer uses a loop to check each Contact in a list. When a Contact with the Title of 'Boss' is found, the Apex method should jump to the first line of code outside of the for loop. Which Apex solution will let the developer implement this requirement?**

- **A.** return; ❌
- **B.** continue; ❌
- **C.** break; ✅
- **D.** System.assert(false); ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên sử dụng vòng lặp để kiểm tra danh sách Contact. Khi gặp Contact có Title là 'Boss', phương thức Apex cần dừng lặp lập tức và nhảy xuống dòng code đầu tiên bên ngoài vòng lặp. Cú pháp nào đáp ứng yêu cầu?

**💬 Giải thích gốc (English):**
> The break statement exits the loop immediately, allowing the code execution to continue from the first line outside the loop.

**✅ Tại sao đáp án đúng:**
> Sử dụng câu lệnh break; (C). Lệnh break sẽ lập tức chấm dứt vòng lặp for/while hiện tại và chuyển quyền thực thi xuống câu lệnh đầu tiên ngay sau khối lặp.

**❌ Tại sao đáp án sai:**
> **A.** return; sẽ thoát hoàn toàn khỏi phương thức hiện tại, không chạy bất kỳ dòng code nào tiếp theo bên dưới vòng lặp nữa.
> **B.** continue; chỉ bỏ qua lượt lặp hiện tại của phần tử đó và tiếp tục nhảy sang duyệt phần tử tiếp theo trong danh sách chứ không thoát loop.
> **D.** System.assert(false) sẽ ngay lập tức làm sập transaction và ném ra lỗi kiểm thử AssertException, cấm dùng trong code chạy thật.

**💡 Từ khóa ghi nhớ:** `Thoát vòng lặp ngay lập tức -> Dùng BREAK. Bỏ qua lượt lặp hiện tại -> Dùng CONTINUE.`

---

## Câu 180

**🔵 A business has a proprietary Order Management System (OMS) that creates orders from their website and fulfills the orders. When the order is created in the OMS, an integration also creates an order record in Salesforce and relates it to the contact as identified by the email on the order. As the order goes through different stages in the OMS, the integration also updates it in Salesforce. It is noticed that each update from the OMS creates a new order record in Salesforce. Which two actions will prevent the duplicate order records from being created in Salesforce? (Choose two.)**

- **A.** Use the order number from the OMS as an external ID. ✅
- **B.** Write a before trigger on the order object to delete any duplicates. ❌
- **C.** Ensure that the order number in the OMS is unique. ✅
- **D.** Use the email on the contact record as an external ID. ❌

**📝 Dịch tiếng Việt:**
> Hệ thống quản lý đơn hàng ngoài (OMS) tạo và xử lý đơn hàng. Tích hợp tạo Order trong Salesforce dựa trên Email của Contact. Mỗi lần OMS gửi cập nhật trạng thái đơn hàng, Salesforce lại tạo mới một bản ghi Order trùng lặp. Hai hành động nào giúp ngăn chặn việc này? (Chọn 2)

**💬 Giải thích gốc (English):**
> Use the order number from the OMS as an external ID.
> By setting the order number as an external ID, Salesforce can recognize and update existing records instead of creating new ones.
> Ensure that the order number in the OMS is unique.
> Ensuring the uniqueness of the order number in the OMS helps maintain data integrity and prevents the creation of duplicate records.

**✅ Tại sao đáp án đúng:**
> A: Đánh dấu mã đơn hàng từ OMS là trường External ID trong Salesforce. C: Đảm bảo mã đơn hàng OMS là duy nhất (Unique). Khi đó, hệ thống tích hợp gọi lệnh Upsert dựa trên khóa này để tự động cập nhật bản ghi có sẵn thay vì chèn mới trùng lặp.

**❌ Tại sao đáp án sai:**
> **B.** Viết trigger delete bản ghi trùng sau khi insert là giải pháp tồi tệ, làm lãng phí ID bản ghi và tiêu tốn cực nhiều tài nguyên hệ thống.
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
> Ảnh hưởng thực tế của việc khai báo một class Apex sử dụng từ khóa 'without sharing' là gì?

**💬 Giải thích gốc (English):**
> Declaring an Apex class using the without sharing keywords means that the class runs in system mode, bypassing the sharing rules of the current user.

**✅ Tại sao đáp án đúng:**
> Lớp Apex đó sẽ chạy dưới quyền hệ thống (System Mode), bỏ qua hoàn toàn các giới hạn chia sẻ dữ liệu (Sharing Rules, OWD) đối với user hiện tại (B), cho phép truy cập toàn bộ dữ liệu của Org.

**❌ Tại sao đáp án sai:**
> **A.** Apex chạy ở chế độ without sharing cho phép update tất cả các bản ghi thỏa mãn điều kiện chứ không bị giới hạn chỉ bản ghi của user hiện tại sở hữu.
> **C.** Từ khóa sharing trên class không hề ảnh hưởng đến khả năng thiết lập sharing rules trên các bản ghi được tạo ra.
> **D.** Class không bị giới hạn quyền gọi theo vai trò developer, mọi user thông thường có quyền truy cập class đều chạy được.

**💡 Từ khóa ghi nhớ:** `without sharing -> Chạy quyền hệ thống (System Mode), BỎ QUA Sharing Rules của User!`

---

## Câu 182

**🔵 A developer needs to find information about @future methods that were invoked. From which system monitoring feature can the developer see this information?**

- **A.** Scheduled Jobs ❌
- **B.** Apex Jobs ✅
- **C.** Background Jobs ❌
- **D.** Asynchronous Jobs ❌

**📝 Dịch tiếng Việt:**
> Developer cần tìm thông tin và theo dõi nhật ký thực thi của các phương thức bất đồng bộ @future đã được gọi. Lập trình viên có thể xem thông tin này ở mục giám sát nào của hệ thống?

**💬 Giải thích gốc (English):**
> Apex Jobs allows developers to monitor the status of @future methods, along with other asynchronous processes like batch jobs and scheduled jobs.

**✅ Tại sao đáp án đúng:**
> Trang Apex Jobs (B) trong Setup hiển thị danh sách toàn bộ các tác vụ xử lý bất đồng bộ bao gồm @future, Batch Apex, Queueable Apex, và Scheduled Apex kèm trạng thái chi tiết.

**❌ Tại sao đáp án sai:**
> **A.** Scheduled Jobs chỉ hiển thị các tác vụ được lập lịch chạy định kỳ (Cron trigger), không hiển thị phương thức @future chạy tức thời.
> **C.** Background Jobs không phải là tên một trang quản trị chuẩn mực để giám sát code Apex bất đồng bộ trong Salesforce.
> **D.** Asynchronous Jobs là thuật ngữ mô tả chung chung, trang Setup thực tế tên là Apex Jobs.

**💡 Từ khóa ghi nhớ:** `Giám sát tiến trình bất đồng bộ (@future, Batch, Queueable) -> Vào Setup gõ APEX JOBS.`

---

## Câu 183

**🔵 A developer has a requirement to create an Order when an Opportunity reaches a 'Closed-Won' status. Which tool should be used to implement this requirement?**

- **A.** Lightning Component ❌
- **B.** Apex Trigger ✅
- **C.** Flow Builder ❌
- **D.** Process Builder ❌

**📝 Dịch tiếng Việt:**
> Yêu cầu nghiệp vụ: Tự động tạo mới một bản ghi Order khi Opportunity chuyển sang trạng thái 'Closed-Won'. Công cụ nào tốt nhất và chuẩn mực nhất của Salesforce nên được sử dụng?

**💬 Giải thích gốc (English):**
> Process Builder is a powerful tool in Salesforce that allows you to automate business processes. It can be used to create an Order automatically when an Opportunity reaches the ‘Closed-Won’ status without writing any code.

**✅ Tại sao đáp án đúng:**
> Sử dụng Apex Trigger (B) (hoặc Flow Builder hiện đại). Apex Trigger hỗ trợ xử lý hàng loạt cực tốt (bulkified), đảm bảo hệ thống không bị oẳng khi cập nhật đồng thời nhiều Opportunity sang Closed-Won. (Mẹo thi: Trong các đề thi Salesforce cũ, Apex Trigger hoặc Process Builder thường được chọn làm đáp án đúng tùy theo ngữ cảnh, tuy nhiên Trigger là lựa chọn an toàn nhất về mặt kỹ thuật code).

**❌ Tại sao đáp án sai:**
> **A.** Lightning Component là công cụ xây dựng giao diện người dùng, không phải công cụ tự động hóa ngầm ở database layer.
> **C.** Flow Builder rất mạnh nhưng trắc nghiệm PD1 thời kỳ đầu chưa cập nhật Flow làm đáp án chuẩn tối thượng hoặc trong đề thi gốc đánh dấu Trigger (B) là lựa chọn tối ưu.
> **D.** Process Builder hiện tại đã bị Salesforce khai tử (deprecated) do hiệu năng kém và không khuyến khích sử dụng nữa.

**💡 Từ khóa ghi nhớ:** `Tự động tạo bản ghi liên quan khi lưu -> Dùng Apex Trigger (hoặc Flow Builder hiện đại).`

---

## Câu 184

**🔵 Universal Containers has a Visualforce page that displays a table of every Container__c being rented by a given Account. Recently this page is failing with a view state limit because some of the customers rent over 10,000 containers. What should a developer change about the Visualforce page to help with the page load errors?**

- **A.** Use lazy loading and a transient List variable. ❌
- **B.** Use JavaScript remoting with SOQL Offset. ❌
- **C.** Implement pagination with a StandardSetController. ✅
- **D.** Implement pagination with an OffsetController. ❌

**📝 Dịch tiếng Việt:**
> Sửa lỗi View State limit trong Visualforce khi hiển thị 10k bản ghi?

**💬 Giải thích gốc (English):**
> Implement pagination with a StandardSetController. This approach helps manage large datasets by loading only a subset of records at a time, significantly reducing the view state size and improving page performance.

**✅ Tại sao đáp án đúng:**
> Dùng StandardSetController để phân trang (Pagination), giúp giảm tải View State.

**❌ Tại sao đáp án sai:**
> **A.** Transient giúp giảm dung lượng nhưng load 10k record lên 1 trang vẫn làm trình duyệt 'ngáp'.
> **B.** OffsetController không phải controller chuẩn của platform.
> **D.** JS Remoting giúp tải data nhanh nhưng không trực quan bằng pagination controller có sẵn.

**💡 Từ khóa ghi nhớ:** `Keywords: View State limit -> Pagination -> StandardSetController.`

---

## Câu 185

**🔵 What are three techniques that a developer can use to invoke an anonymous block of code? (Choose three.)**

- **A.** Use the SOAP API to make a call to execute anonymous code. ✅
- **B.** Create a Visualforce page that uses a controller class that is declared without sharing. ❌
- **C.** Run code using the Anonymous Apex feature of the Developer's IDE. ✅
- **D.** Type code into the Developer Console and execute it directly. ✅
- **E.** Create and execute a test method that does not specify a runAs() call. ❌

**📝 Dịch tiếng Việt:**
> Ba kỹ thuật nào mà lập trình viên có thể sử dụng để kích hoạt thực thi một khối mã nguồn vô danh (Anonymous Apex Block)? (Chọn 3)

**✅ Tại sao đáp án đúng:**
> A: Sử dụng SOAP API gọi hàm executeAnonymous từ bên ngoài. C: Chạy code bằng tính năng Anonymous Apex trên các công cụ IDE của lập trình viên (như VS Code). D: Nhập trực tiếp code Apex vào cửa sổ Execute Anonymous của Developer Console để chạy.

**❌ Tại sao đáp án sai:**
> **B.** Trang Visualforce chỉ hiển thị giao diện, không phải là công cụ gọi khối lệnh anonymous tùy ý.
> **E.** Chạy test class là để kiểm thử các phương thức test cụ thể trong hệ thống, không liên quan đến việc thực thi khối lệnh anonymous tự do.

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
> Một trang Visualforce khai báo hai class Controller Extension đều chứa phương thức save(): [Code apex:page]. Phương thức save() của class nào sẽ được gọi khi bấm nút Save?

**💬 Giải thích gốc (English):**
> When multiple controller extensions are specified, the methods in the first extension listed (in this case, ExtensionA) take precedence and will be called.

**✅ Tại sao đáp án đúng:**
> Khi trang Visualforce chứa nhiều controller extensions có các phương thức trùng tên nhau, Salesforce sẽ giải quyết xung đột bằng cách ưu tiên thực thi phương thức của class khai báo đầu tiên từ trái qua phải (A) (ở đây là ExtensionA).

**❌ Tại sao đáp án sai:**
> **B.** ExtensionB xếp ở sau nên phương thức trùng tên của nó bị ExtensionA ghi đè (override) và bỏ qua.
> **C.** Phương thức save chuẩn của Standard Controller bị class extension ExtensionA ghi đè hoàn toàn.
> **D.** Không có runtime error nào xảy ra vì Salesforce xử lý thứ tự ưu tiên rất mượt mà theo cấu hình khai báo.

**💡 Từ khóa ghi nhớ:** `Visualforce đa Extension trùng method -> Ưu tiên gọi class khai báo đầu tiên (từ trái qua phải).`

---

## Câu 187

**🔵 A developer needs to create a Visualforce page that displays Case data. The page will be used by both support reps and support managers. The Support Rep profile does not allow visibility of the Customer_Satisfaction__c field, but the Support Manager profile does. How can the developer create the page to enforce Field Level Security and keep future maintenance to a minimum?**

- **A.** Create one Visualforce Page for use by both profiles. ✅
- **B.** Use a new Support Manager permission set. ❌
- **C.** Create a separate Visualforce Page for each profile. ❌
- **D.** Use a custom controller that has the with sharing keywords. ❌

**📝 Dịch tiếng Việt:**
> Trang Visualforce hiển thị dữ liệu Case dùng cho cả Support Rep và Support Manager. Support Rep không có quyền xem trường Customer_Satisfaction__c còn Support Manager thì có. Làm thế nào để thực thi đúng FLS và tốn ít công bảo trì nhất?

**💬 Giải thích gốc (English):**
> The best approach to enforce Field Level Security (FLS) and minimize future maintenance is to create one Visualforce Page for use by both profiles . When using Visualforce pages, the platform indeed enforces CRUD and FLS automatically when SObjects and SObject fields are referenced directly. This means that creating a single Visualforce page will handle field visibility based on the user’s profile permissions.
> Note: Using a custom controller with the with sharing keyword ensures record-level security, but for field-level security.

**✅ Tại sao đáp án đúng:**
> Tạo duy nhất MỘT trang Visualforce dùng chung cho cả hai profile (A). Các thẻ Visualforce chuẩn (như <apex:outputField>) tích hợp sẵn tính năng tự động tôn trọng bảo mật cấp trường FLS của user hiện tại, tự ẩn trường nếu user không có quyền xem mà không cần viết code.

**❌ Tại sao đáp án sai:**
> **B.** Permission Set giúp cấp thêm quyền chứ không phải giải pháp thiết kế trang Visualforce tối ưu FLS.
> **C.** Tạo nhiều trang Visualforce riêng biệt cho từng profile làm nhân đôi công sức phát triển và cực kỳ khó khăn bảo trì sau này.
> **D.** with sharing chỉ kiểm soát quyền truy cập bản ghi (Record-level sharing), hoàn toàn không có tác dụng phân quyền bảo mật cấp trường (FLS).

**💡 Từ khóa ghi nhớ:** `Visualforce FLS -> Dùng duy nhất 1 trang Visualforce + thẻ chuẩn (outputField) tự động ẩn/hiển thị theo quyền User.`

---

## Câu 188

**🔵 Which three steps allow a custom SVG to be included in a Lightning web component? (Choose three.)**

- **A.** Upload the SVG as a static resource. ✅
- **B.** Reference the getter in the HTML template. ✅
- **C.** Import the SVG as a content asset file. ❌
- **D.** Import the static resource and provide a getter for it in JavaScript. ✅
- **E.** Reference the import in the HTML template. ❌

**📝 Dịch tiếng Việt:**
> 3 bước nhúng SVG tùy chỉnh vào LWC?

**✅ Tại sao đáp án đúng:**
> A: Up lên Static Resource. E: Import vào JS và tạo getter. D: Dùng getter đó trong HTML.

**❌ Tại sao đáp án sai:**
> **B.** Content asset file không dùng để nhúng trực tiếp kiểu này trong LWC.
> **C.** HTML không thể 'import' trực tiếp từ static resource mà phải qua JS.

**💡 Từ khóa ghi nhớ:** `LWC SVG: Static Resource -> Import in JS -> Getter in HTML.`

---

## Câu 189

**🔵 A custom Visualforce controller calls the ApexPages.addMessage() method, but no messages are rendering on the page. Which component should be added to the Visualforce page to display the message?**

- **A.** <apex:message for="info"/> ❌
- **B.** <apex:facet name="messages" /> ❌
- **C.** <apex:pageMessage severity="info" /> ❌
- **D.** <apex:pageMessages /> ✅

**📝 Dịch tiếng Việt:**
> Một Custom Visualforce Controller gọi hàm 'ApexPages.addMessage()' để báo lỗi nhưng không thấy thông báo nào hiển thị trên giao diện trang. Lập trình viên nên thêm thành phần nào vào trang Visualforce?

**💬 Giải thích gốc (English):**
> To display messages added by the ApexPages.addMessage() method, you should use the <apex:pageMessages /> component. This component displays all messages that were generated for all components on the current page, using Salesforce’s standard styling.

**✅ Tại sao đáp án đúng:**
> Thêm thành phần <apex:pageMessages /> (D). Thẻ này đóng vai trò là phễu thu thập và hiển thị toàn bộ danh sách thông báo lỗi/cảnh báo được ném ra từ ApexPages.addMessage() theo đúng giao diện tiêu chuẩn của Salesforce.

**❌ Tại sao đáp án sai:**
> **A.** <apex:message> chỉ hiển thị lỗi cho duy nhất một trường dữ liệu cụ thể được chỉ định, không hiển thị lỗi chung từ addMessage.
> **B.** <apex:facet> dùng để cấu hình layout/header của bảng dữ liệu, không có tính năng hiển thị thông báo lỗi.
> **C.** <apex:pageMessage> hiển thị một thông báo tĩnh cố định do lập trình viên viết cứng trên trang, không hiển thị động các lỗi từ code Apex ném ra.

**💡 Từ khóa ghi nhớ:** `Hiển thị lỗi từ ApexPages.addMessage() ra giao diện -> Luôn dùng thẻ <apex:pageMessages />.`

---

## Câu 190

**🔵 A Licensed_Professional__c custom object exists in the system with two Master-Detail fields for the following objects: Certification__c and Contact.
Users with the 'Certification Representative' role can access the Certification records they own and view the related Licensed Professionals records, however users with the 'Sales Representative' role report they cannot view any Licensed Professional records even though they own the associated Contact record. What are two likely causes of users in the 'Sales Representative' role not being able to access the Licensed Professional records? (Choose two.)**

- **A.** The organization has a private sharing model for Certification__c and Certification__c is the primary relationship in the Licensed_Professional__c object. ✅
- **B.** The organization's sharing rules for Licensed_Professional__c have not finished their recalculation process. ✅
- **C.** The organization recently modified the Sales Representative role to restrict Read/Write access to Licensed_Professional__c. ❌
- **D.** The organization has a private sharing model for Certification__c, and Contact is the primary relationship in the Licensed_Professional__c object. ❌

**📝 Dịch tiếng Việt:**
> Object Licensed_Professional__c có 2 quan hệ Master-Detail với Certification__c và Contact. User có role 'Certification Rep' xem được các bản ghi con, nhưng user 'Sales Rep' dù là chủ sở hữu Contact lại báo không xem được bất kỳ bản ghi con nào. Hai nguyên nhân nào gây ra việc này? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> A: OWD của Certification__c là Private và nó là Primary Relationship (quan hệ Master được tạo đầu tiên). Khi đó, quyền bảo mật chia sẻ của con hoàn toàn kế thừa từ Primary Master. Sales Rep không có quyền xem Certification cha nên bị chặn xem con. B: Các Sharing Rules của Licensed_Professional__c đang trong quá trình tính toán lại (recalculation) nên quyền chưa được phân phối.

**❌ Tại sao đáp án sai:**
> **C.** Chỉnh sửa role phân quyền CRUD trên đối tượng không giải quyết được vấn đề phân quyền chia sẻ (Sharing) thực tế của bản ghi con.
> **D.** Nếu Contact là Primary Relationship thì Sales Rep (chủ Contact) phải xem được con, trái ngược với thực trạng lỗi của đề bài.

**💡 Từ khóa ghi nhớ:** `Custom con có 2 Master-Detail -> Bảo mật con kế thừa hoàn toàn từ Primary Master (Master đầu tiên).`

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
> Cho đoạn code sau thực thi trong Apex: [Code Boolean isOK]. Hỏi sau khi chạy xong, giá trị của biến x là bao nhiêu?

**💬 Giải thích gốc (English):**
> In the given code snippet, the variable isOK is declared but not initialized, so its value is null by default. Let’s analyze the conditions:
> 1. if(isOK == false && theString == 'Hello'): This condition is false because isOK is null.
> 2. else if(isOK == true && theString == 'Hello'): This condition is also false because isOK is null.
> 3. else if(isOK != null && theString == 'Hello'): This condition is false because isOK is null.
> 4. else: This block will execute because none of the previous conditions are true.
> Therefore, the value of x will be set to 4.

**✅ Tại sao đáp án đúng:**
> Giá trị của x là 4 (D). Biến Boolean isOK chỉ được khai báo và không được khởi tạo giá trị nên nó nhận giá trị mặc định là null. Do đó, các điều kiện check so sánh isOK == false, isOK == true và isOK != null đều trả về false. Luồng chạy rơi vào block else và gán x = 4.

**❌ Tại sao đáp án sai:**
> **A.** Sai vì isOK là null chứ không phải false.
> **B.** Sai vì isOK là null chứ không phải true.
> **C.** Sai vì isOK là null nên điều kiện check khác null bị loại.

**💡 Từ khóa ghi nhớ:** `Mẹo Apex: Biến khai báo không gán trị -> Mặc định luôn là NULL!`

---

## Câu 192

**🔵 A developer needs to include a Visualforce page in the detail section of a page layout for the Account object, but does not see the page as an available option in the Page Layout Editor. Which attribute must the developer include in the tag to ensure the Visualforce page can be embedded in a page layout?**

- **A.** standardController= "Account" ✅
- **B.** extensions= "AccountController" ❌
- **C.** controller= "Account" ❌
- **D.** action= "AccountId" ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên muốn nhúng một trang Visualforce vào phần chi tiết (detail section) của Page Layout đối tượng Account, nhưng không tìm thấy trang này trong trình biên tập Layout. Thuộc tính nào bắt buộc phải khai báo?

**💬 Giải thích gốc (English):**
> To ensure the Visualforce page can be embedded in a page layout for the Account object, the developer must include the attribute standardController="Account" in the <apex:page> tag.

**✅ Tại sao đáp án đúng:**
> Khai báo thuộc tính standardController='Account' (A) trong thẻ <apex:page>. Chỉ những trang Visualforce sử dụng Standard Controller của đối tượng tương ứng mới đủ điều kiện hiển thị trong danh sách nhúng layout của đối tượng đó.

**❌ Tại sao đáp án sai:**
> **B.** extensions chỉ để khai báo lớp Apex mở rộng, không quyết định khả năng nhúng layout.
> **C.** controller dùng để khai báo Custom Controller class, trang dùng custom controller cấm nhúng trực tiếp vào layout chuẩn.
> **D.** action dùng để gọi hàm khi tải trang, không liên quan đến cấu hình nhúng layout.

**💡 Từ khóa ghi nhớ:** `Muốn nhúng trang Visualforce vào Page Layout của sObject -> Bắt buộc dùng standardController='sObjectName'.`

---

## Câu 193

**🔵 Which two operations can be performed using a formula field? (Choose two.)**

- **A.** Displaying the last four digits of an encrypted Social Security number ❌
- **B.** Triggering a Process Builder ❌
- **C.** Displaying an Image based on the Opportunity Amount ✅
- **D.** Calculating a score on a Lead based on the information from another field ✅

**📝 Dịch tiếng Việt:**
> Hai thao tác nào thực hiện được bằng Formula field? (Chọn 2)

**💬 Giải thích gốc (English):**
> Displaying an Image based on the Opportunity Amount: Formula fields can display different images based on certain criteria.
> Calculating a score on a Lead based on the information from another field: Formula fields can perform calculations using data from other fields.

**✅ Tại sao đáp án đúng:**
> A: Tính toán dựa trên field khác. B: Dùng hàm IMAGE() để hiển thị ảnh động.

**❌ Tại sao đáp án sai:**
> **C.** Formula không thể 'nhìn' thấy data bên trong encrypted fields.
> **D.** Formula field thay đổi giá trị không làm 'fire' trigger hay PB.

**💡 Từ khóa ghi nhớ:** `Formula: Read-only, IMAGE(), No Encrypted Data.`

---

## Câu 194

**🔵 Application Events follow the traditional publish-subscribe model. Which method is used to fire an event?**

- **A.** registerEvent() ❌
- **B.** fireEvent() ❌
- **C.** emit() ❌
- **D.** fire() ✅

**📝 Dịch tiếng Việt:**
> Application Events tuân theo mô hình publish-subscribe truyền thống. Phương thức nào được sử dụng để kích hoạt (fire) một event?

**💬 Giải thích gốc (English):**
> To fire an application event in Salesforce, you use the fire() method.

**✅ Tại sao đáp án đúng:**
> Trong lập trình Aura Component, sau khi lấy được instance của event bằng $A.getEvt()$, ta sử dụng phương thức .fire() để đẩy event đó vào hệ thống.

**❌ Tại sao đáp án sai:**
> **B.** registerEvent() dùng trong component để khai báo event chứ không phải để kích hoạt.
> **C.** emit() là từ khóa thường dùng trong Node.js hoặc Vue, không tồn tại trong Aura/LWC.
> **D.** fireEvent() là một cái tên gây nhầm lẫn, Salesforce chỉ dùng .fire().

**💡 Từ khóa ghi nhớ:** `Keywords: Aura Event -> .fire(). Nhớ nhé: 'Fire' là bắn, 'Event' là đạn.`

---

## Câu 195

**🔵 A developer needs to implement the functionality for a service agent to gather multiple pieces of information from a customer in order to send a replacement credit card. Which automation tool meets these requirements?**

- **A.** Lightning Component ❌
- **B.** Flow Builder ✅
- **C.** Process Builder ❌
- **D.** Approval Process ❌

**📝 Dịch tiếng Việt:**
> Công cụ nào dùng để thu thập nhiều thông tin từ khách hàng (nhập liệu nhiều trang)?

**💬 Giải thích gốc (English):**
> To gather multiple pieces of information from a customer and send a replacement credit card, the best automation tool to use is Flow Builder. Flow Builder allows you to create guided, interactive processes for users, making it ideal for collecting information through a series of steps.

**✅ Tại sao đáp án đúng:**
> Screen Flow (Flow Builder) là công cụ khai báo (No-code) tốt nhất để tạo các form thu thập dữ liệu nhiều bước từ người dùng.

**❌ Tại sao đáp án sai:**
> **A.** Làm được nhưng tốn thời gian code hơn Flow rất nhiều.
> **C.** Process Builder không có khả năng hiển thị giao diện nhập liệu.
> **D.** Approval Process dùng để phê duyệt, không phải để thu thập thông tin khách hàng.

**💡 Từ khóa ghi nhớ:** `Gather information / User Input / Multi-screen -> Screen Flow.`

---

## Câu 196

**🔵 Einstein Next Best Action is configured at Universal Containers to display recommendations to internal users on the Account detail page. If the recommendation is approved, a new opportunity record and task should be generated. If the recommendation is rejected, an Apex method must be executed to perform a callout to an external system. Which three factors should a developer keep in mind when implementing the Apex method? (Choose three.)**

- **A.** The method must use the @AuraEnabled annotation. ❌
- **B.** The method must use the @InvokableMethod annotation. ✅
- **C.** The method must be defined as static. ✅
- **D.** The method must be defined as public. ✅
- **E.** The method must use the @Future annotation ❌

**📝 Dịch tiếng Việt:**
> Einstein Next Best Action hiển thị gợi ý trên Account. Khi gợi ý bị từ chối (rejected), một phương thức Apex phải được thực thi để gọi API ra ngoài. Ba yếu tố nào lập trình viên cần lưu ý khi viết phương thức Apex này? (Chọn 3)

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
> B: Phương thức bắt buộc phải sử dụng annotation @InvokableMethod để Flow/Next Best Action nhận diện và gọi được. C: Phương thức bắt buộc phải khai báo là static. D: Phương thức bắt buộc phải là public (hoặc global) để bên ngoài truy cập.

**❌ Tại sao đáp án sai:**
> **A.** @AuraEnabled chỉ dùng để phơi hàm cho Lightning Component (Aura/LWC) gọi, không dùng cho Next Best Action gọi trực tiếp.
> **E.** @Future là annotation chạy bất đồng bộ chung, phương thức invokable có thể gọi hàm future bên trong chứ chính nó không bắt buộc phải là @Future.

**💡 Từ khóa ghi nhớ:** `Invokable Method tiêu chuẩn -> @InvokableMethod + public static void name(List<T> input).`

---

## Câu 197

**🔵 An Opportunity needs to have an amount rolled up from a custom object that is not in a master-detail relationship. How can this be achieved?**

- **A.** Use the Metadata API to create real-time roll-up summaries. ❌
- **B.** Use the Streaming API to create real-time roll-up summaries. ❌
- **C.** Write a trigger on the Opportunity object and use tree sorting to sum the amount for all related child objects under the Opportunity. ❌
- **D.** Write a trigger on the child object and use an aggregate function to sum the amount for all related child objects under the Opportunity. ✅

**📝 Dịch tiếng Việt:**
> Làm sao để tính tổng (Roll-up) lên Opportunity khi quan hệ chỉ là Lookup?

**💬 Giải thích gốc (English):**
> The correct approach to roll up an amount from a custom object that is not in a master-detail relationship is: Write a trigger on the child object and use an aggregate function to sum the amount for all related child objects under the Opportunity. This trigger will ensure that whenever a child object is inserted, updated, deleted, or undeleted, the corresponding Opportunity’s amount is updated accordingly.

**✅ Tại sao đáp án đúng:**
> Lookup không hỗ trợ field Roll-up Summary. Mày phải viết Trigger trên object con, dùng SOQL Aggregate (SUM) để tính toán rồi update ngược lại Opportunity cha bằng code.

**❌ Tại sao đáp án sai:**
> **A.** Streaming API chỉ để hóng data, không dùng để tính toán và lưu trữ dữ liệu.
> **B.** Giải thuật red-black tree cực kỳ phức tạp và không liên quan gì đến việc SUM dữ liệu bản ghi con.
> **D.** Process Builder không hỗ trợ các hàm Aggregate (SUM, AVG) trên danh sách con.

**💡 Từ khóa ghi nhớ:** `No Master-Detail -> Dùng Trigger + Aggregate Query.`

---

## Câu 198

**🔵 A developer at Universal Containers is tasked with implementing a new Salesforce application that must be able to be maintained completely by their company's Salesforce administrator. Which three options should be considered for building out the business logic layer of the application? (Choose three.)**

- **A.** Process Builder ✅
- **B.** Scheduled Jobs ❌
- **C.** Invocable Actions ✅
- **D.** Workflows ❌
- **E.** Validation Rules ✅

**📝 Dịch tiếng Việt:**
> Universal Containers muốn xây dựng một ứng dụng Salesforce mới mà toàn bộ logic nghiệp vụ sau này có thể được bảo trì hoàn toàn no-code bởi Quản trị viên (Admin). Ba công cụ nào nên được xem xét? (Chọn 3)

**✅ Tại sao đáp án đúng:**
> A: Process Builder (no-code tự động hóa nghiệp vụ). C: Invocable Actions (gọi các tiến trình đóng gói sẵn từ Flow/Process). E: Validation Rules (quy tắc chặn dữ liệu hoàn toàn no-code). Các công cụ này giúp admin dễ dàng chỉnh sửa mà không cần đụng đến code Apex.

**❌ Tại sao đáp án sai:**
> **B.** Scheduled Jobs yêu cầu lập trình class Apex implements Schedulable, admin không thể viết code bảo trì được.
> **D.** Workflows tuy no-code nhưng tính năng quá nghèo nàn và đã bị Salesforce ngừng phát triển nâng cấp (deprecated).

**💡 Từ khóa ghi nhớ:** `Logic no-code cho Admin dễ bảo trì -> Process Builder/Flow Builder, Invocable Actions, Validation Rules.`

---

## Câu 199

**🔵 Universal Containers (UC) uses a custom object called Vendor. The Vendor custom object has a Master-Detail relationship with the standard Account object. Based on some internal discussions, the UC administrator tried to change the Master-Detail relationship to a Lookup relationship but was not able to do so. What is a possible reason that this change was not permitted?**

- **A.** The Vendor records have existing values in the Account object. ❌
- **B.** The Account object is included on a workflow on the Vendor object. ❌
- **C.** The Account records contain Vendor roll-up summary fields. ✅
- **D.** The Vendor object must use a Master-Detail field for reporting. ❌

**📝 Dịch tiếng Việt:**
> Admin của Universal Containers cố gắng chuyển đổi trường quan hệ Master-Detail trên đối tượng Vendor thành quan hệ Lookup với Account nhưng bị hệ thống báo lỗi không cho phép. Nguyên nhân khả thi nhất là gì?

**💬 Giải thích gốc (English):**
> You cannot change a Master-Detail relationship to a Lookup relationship if there are roll-up summary fields on the parent object that summarize data from the child object. These roll-up summary fields must be deleted before the relationship type can be changed.

**✅ Tại sao đáp án đúng:**
> Trên đối tượng cha Account đang tồn tại các trường Roll-up Summary (C) tính toán dữ liệu của Vendor con. Đây là ràng buộc cứng của Salesforce, ta bắt buộc phải xóa hoàn toàn các trường Roll-up Summary này trước khi đổi kiểu quan hệ.

**❌ Tại sao đáp án sai:**
> **A.** Việc bản ghi Vendor có giá trị liên kết Account hoàn toàn không cản trở việc đổi sang Lookup (chỉ có chiều ngược lại từ Lookup sang Master-Detail mới yêu cầu Vendor không được có dữ liệu trống).
> **B.** Workflow không chặn việc chuyển đổi kiểu trường quan hệ cơ bản.
> **D.** Không có ràng buộc hệ thống nào bắt buộc Vendor phải dùng Master-Detail chỉ để phục vụ báo cáo.

**💡 Từ khóa ghi nhớ:** `Đổi Master-Detail sang Lookup -> Bắt buộc phải XÓA hết các trường Roll-up Summary trên cha trước!`

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
> Khi cần thực hiện hành động khi bản ghi bị XÓA (delete), KHÔI PHỤC (undelete), hoặc cần can thiệp xử lý dữ liệu ở giai đoạn BEFORE DML (D) trước khi lưu xuống database. Các sự kiện này Process Builder/Flow đời cũ hoàn toàn không hỗ trợ.

**❌ Tại sao đáp án sai:**
> **A.** Tạo mới bản ghi là thế mạnh cơ bản của Process Builder với hành động Create Record.
> **B.** Cập nhật hàng loạt bản ghi con liên quan hoàn toàn thực hiện được no-code bằng Process Builder.
> **C.** Đăng bài viết lên Chatter (Post to Chatter) là hành động tích hợp sẵn cực kỳ trực quan của Process Builder.

**💡 Từ khóa ghi nhớ:** `Bắt buộc dùng Trigger khi -> Muốn bắt sự kiện Before DML, hoặc sự kiện Delete/Undelete.`

---

## Câu 201

**🔵 A company wants to create an employee rating program that allows employees to rate each other. An employee's average rating must be displayed on the employee record. Employees must be able to create rating records, but are not allowed to create employee records. Which two actions should a developer take to accomplish this task? (Choose two.)**

- **A.** Create a trigger on the Rating object that updates a fields on the Employee object. ✅
- **B.** Create a lookup relationship between the Rating and Employee object. ✅
- **C.** Create a roll-up summary field on the Employee and use AVG to calculate the average rating score. ❌
- **D.** Create a master-detail relationship between the Rating and Employee objects. ❌

**📝 Dịch tiếng Việt:**
> Công ty muốn tạo tính năng đánh giá nhân viên (Rating). Điểm đánh giá trung bình của nhân viên (Employee's average rating) phải được hiển thị trên Employee record. Nhân viên được phép tạo Rating nhưng cấm sửa Employee. Hai hành động nào developer nên chọn? (Chọn 2)

**💬 Giải thích gốc (English):**
> Roll-Up summary doesn't have AVG.

**✅ Tại sao đáp án đúng:**
> A: Viết trigger trên đối tượng Rating để tự động tính trung bình cộng và update lên trường của Employee. B: Tạo mối quan hệ Lookup giữa Rating và Employee. (Vì sao không dùng Master-Detail và Roll-up? Vì hàm tổng hợp AVG không hề được hỗ trợ trong trường Roll-up Summary chuẩn của Salesforce!).

**❌ Tại sao đáp án sai:**
> **C.** Hàm tổng hợp AVG (Average) KHÔNG HỀ TỒN TẠI trong tính năng Roll-up Summary Field của Salesforce (chỉ có SUM, COUNT, MIN, MAX).
> **D.** Mối quan hệ Master-Detail sẽ kế thừa bảo mật nghiêm ngặt từ cha Employee, gây khó khăn cho quyền tạo bản ghi của nhân viên.

**💡 Từ khóa ghi nhớ:** `Salesforce Roll-up Summary: Cấm dùng hàm tính trung bình AVG. Muốn tính trung bình -> Dùng Lookup + Trigger!`

---

## Câu 202

**🔵 What is a benefit of developing applications in a multi-tenant environment?**

- **A.** Access to predefined computing resources ❌
- **B.** Enforced best practices for development ✅
- **C.** Unlimited processing power and memory ❌
- **D.** Default out-of-the-box configuration ❌

**📝 Dịch tiếng Việt:**
> Lợi ích của việc phát triển ứng dụng trong môi trường đa thuê bao (multi-tenant) là gì?

**✅ Tại sao đáp án đúng:**
> Để đảm bảo một khách hàng không làm sập server dùng chung, Salesforce ép buộc các giới hạn Governor Limits, từ đó hình thành các Best Practices (như bulkify code) mà mọi dev phải tuân theo.

**❌ Tại sao đáp án sai:**
> **B.** Cấu hình mặc định có sẵn ở mọi môi trường, không phải lợi ích riêng biệt của multi-tenancy.
> **C.** Sai bét! Multi-tenant là tài nguyên có hạn (Limits), làm gì có chuyện vô hạn (unlimited).
> **D.** Truy cập tài nguyên định sẵn là đặc tính kỹ thuật, không phải là 'lợi ích' lớn nhất về mặt chất lượng app như ý A.

**💡 Từ khóa ghi nhớ:** `Multi-tenant = 'Chung chạ' tài nguyên -> Phải có 'Luật' (Governor Limits) để giữ trật tự.`

---

## Câu 203

**🔵 When viewing a Quote, the sales representative wants to easily see how many discounted items are included in the Quote Line Items. What should a developer do to meet this requirement?**

- **A.** Create a trigger on the Quote object that queries the Quantity field on discounted Quote Line Items. ❌
- **B.** Create a Workflow Rule on the Quote Line Item object that updates a field on the parent Quote when the item is discounted. ❌
- **C.** Create a roll-up summary field on the Quote object that performs a SUM on the quote Line Item Quantity field, filtered for only discounted Quote Line Items. ✅
- **D.** Create a formula field on the Quote object that performs a SUM on the Quote Line Item Quantity field, filtered for only discounted Quote Line Items. ❌

**📝 Dịch tiếng Việt:**
> Khi xem Quote, sales rep muốn thấy nhanh tổng số lượng các mặt hàng được chiết khấu (discounted) có trong Quote Line Items. Lập trình viên nên làm gì?

**💬 Giải thích gốc (English):**
> To meet the requirement of showing how many discounted items are included in the Quote Line Items, the best approach is to use a roll-up summary field. This field can perform a SUM on the Quote Line Item Quantity field, filtered specifically for discounted items.

**✅ Tại sao đáp án đúng:**
> Tạo trường Roll-up Summary trên Quote thực hiện tính SUM trường Quantity của Quote Line Item, đồng thời cấu hình bộ lọc filter criteria chỉ tính các dòng Quote Line Item có chiết khấu (C). Đây là giải pháp no-code chuẩn và tối ưu nhất.

**❌ Tại sao đáp án sai:**
> **A.** Viết trigger Apex là giải pháp code cồng kềnh và tốn tài nguyên bảo trì không cần thiết cho một tác vụ có thể làm no-code.
> **B.** Workflow rule field update không thể thực hiện tính tổng và cập nhật ngược dòng dữ liệu hiệu quả bằng Roll-up Summary.
> **D.** Formula field chỉ có thể tính toán trên chính bản ghi đó hoặc từ cha xuống con, cấm thực hiện hàm tổng hợp (SUM) đi ngược từ con lên cha.

**💡 Từ khóa ghi nhớ:** `Đếm/Tổng con có điều kiện lên Cha (ở quan hệ Master-Detail) -> Luôn dùng Roll-up Summary Field bật filter!`

---

## Câu 204

**🔵 In terms of the MVC paradigm, what are two advantages of implementing the view layer of a Salesforce application using Lightning Web Component-based development over Visualforce? (Choose two.)**

- **A.** Self-contained and reusable units of an application ✅
- **B.** Rich component ecosystem ✅
- **C.** Server-side run-time debugging ❌
- **D.** Automatic code generation ❌

**📝 Dịch tiếng Việt:**
> Xét về mô hình MVC, hai ưu điểm vượt trội của việc xây dựng tầng View bằng Lightning Web Components (LWC) so với Visualforce là gì? (Chọn 2)

**💬 Giải thích gốc (English):**
> Self-contained and reusable units of an application: LWCs are designed as modular components that can be reused across different parts of the application, promoting better code organization and maintainability.
> Rich component ecosystem: LWC benefits from a modern, rich ecosystem of components that can be easily integrated and customized, enhancing the development experience and enabling the creation of more dynamic and responsive user interfaces.

**✅ Tại sao đáp án đúng:**
> A: LWCs được thiết kế dưới dạng các khối thành phần độc lập và có khả năng tái sử dụng cực cao (reusable units). B: LWC sở hữu một hệ sinh thái linh kiện phong phú, hiện đại giúp xây dựng giao diện động mượt mà hơn nhiều.

**❌ Tại sao đáp án sai:**
> **C.** LWC chạy và debug chủ yếu dưới Client-side (trình duyệt JavaScript), không phải server-side.
> **D.** LWC không có tính năng tự động sinh mã nguồn (automatic code generation) kỳ diệu nào cả.

**💡 Từ khóa ghi nhớ:** `Ưu thế LWC so với Visualforce -> Độc lập, tái sử dụng cao và hệ sinh thái hiện đại mượt mà.`

---

## Câu 205

**🔵 Cloud Kicks Fitness, an ISV Salesforce partner, is developing a managed package application. One of the application modules allows the user to calculate body fat using the Apex class, BodyFat, and its method, calculateBodyFat(). The product owner wants to ensure this method is accessible by the consumer of the application when developing customizations outside the ISV's package namespace. Which approach should a developer take to ensure calculateBodyFat() is accessible outside the package namespace?**

- **A.** Declare the class and method using the public access modifier. ❌
- **B.** Declare the class as global and use the public access modifier on the method. ❌
- **C.** Declare the class as public and use the global access modifier on the method. ❌
- **D.** Declare the class and method using the global access modifier. ✅

**📝 Dịch tiếng Việt:**
> Cloud Kicks Fitness phát triển một managed package. Một module cho phép khách hàng gọi hàm calculateBodyFat() trong Apex class BodyFat để tùy biến. Developer nên khai báo class và method như thế nào để khách hàng ngoài package có thể gọi được?

**💬 Giải thích gốc (English):**
> To ensure that the calculateBodyFat() method is accessible outside the package namespace, the developer should use the global access modifier. This is because the global access modifier allows the class and its methods to be accessible across different namespaces, which is essential for managed packages.

**✅ Tại sao đáp án đúng:**
> Khai báo cả class và method sử dụng từ khóa truy cập global (D). Trong managed package, chỉ các class và method khai báo global mới có thể được truy cập và gọi từ bên ngoài namespace của gói.

**❌ Tại sao đáp án sai:**
> **A.** public chỉ cho phép các class khác trong cùng một namespace của package truy cập, khách hàng ở ngoài cấm gọi.
> **B.** Phương thức khai báo public sẽ bị chặn truy cập từ ngoài namespace bất kể class cha có là global.
> **C.** Class khai báo public sẽ khóa cứng toàn bộ các thành phần bên trong nó đối với bên ngoài bất chấp method khai báo global.

**💡 Từ khóa ghi nhớ:** `Managed Package phơi code cho khách hàng ngoài gọi -> Bắt buộc dùng từ khóa GLOBAL!`

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
> Một công ty phần mềm sử dụng các đối tượng và mối quan hệ sau: Case (Private OWD), Defect__c (Private OWD, custom object), và Case_Defect__c (junction object Nhiều-Nhiều giữa Case và Defect__c). Làm thế nào để chia sẻ quyền truy cập một bản ghi Case_Defect__c cụ thể cho một người dùng?

**💬 Giải thích gốc (English):**
> A junction object Case_Defect__c typically has two master-detail relationships, one to Case and another to Defect__c. This means that the sharing settings for Case_Defect__c are inherited from its parent records.
> To share a specific Case_Defect__c record with a user, you would indeed need to ensure that the user has access to both the Case and Defect__c records. This is because the visibility of the junction object record is controlled by the sharing settings of its parent objects.

**✅ Tại sao đáp án đúng:**
> Vì Case_Defect__c là đối tượng trung gian (Junction Object) được liên kết bằng hai mối quan hệ Master-Detail trỏ về hai cha Case và Defect__c. Quyền bảo mật chia sẻ của nó hoàn toàn kế thừa trực tiếp từ hai cha. Do đó, người dùng bắt buộc phải có quyền truy cập (xem) đối với cả hai bản ghi cha là Case và Defect__c (B) thì mới có thể nhìn thấy bản ghi liên kết con Case_Defect__c.

**❌ Tại sao đáp án sai:**
> **A.** Chỉ chia sẻ bản ghi Defect__c cha là chưa đủ quyền đối với cha bên kia (Case), người dùng vẫn bị chặn xem bản ghi junction.
> **C.** Không thể thiết lập Sharing Rules hay chia sẻ trực tiếp trên bản ghi Case_Defect__c con được vì đối tượng con trong mối quan hệ Master-Detail không sở hữu trường Owner riêng và không có nút chia sẻ thủ công.
> **D.** Chỉ chia sẻ bản ghi Case cha tương tự lỗi của câu A, vẫn thiếu quyền xem Defect__c.

**💡 Từ khóa ghi nhớ:** `Chia sẻ bản ghi Junction (Many-to-Many) -> Bắt buộc phải có quyền truy cập đối với CẢ HAI bản ghi cha!`

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
> Kết quả hiển thị trong debug log của đoạn mã Apex sau là gì? [Code Decimal theValue]

**💬 Giải thích gốc (English):**
> In Apex, when a Decimal variable is declared but not initialized, its default value is 'null'.

**✅ Tại sao đáp án đúng:**
> Kết quả debug in ra là 'null' (B). Trong ngôn ngữ Apex, mọi biến số (Decimal, Double, Integer,...) khi mới khai báo mà không khởi tạo giá trị cụ thể sẽ luôn luôn nhận giá trị mặc định là null để bảo vệ bộ nhớ.

**❌ Tại sao đáp án sai:**
> **A.** 0.0 không phải là giá trị mặc định của kiểu Decimal trong Apex.
> **C.** Không tồn tại khái niệm giá trị 'Undefined' giống JavaScript trong ngôn ngữ lập trình Apex.
> **D.** 0 là giá trị mặc định của kiểu số nguyên trong một số ngôn ngữ khác nhưng với Apex vẫn là null.

**💡 Từ khóa ghi nhớ:** `Mẹo Apex: Mọi biến số khai báo không gán trị mặc định -> Luôn nhận giá trị NULL!`

---

## Câu 208

**🔵 Candidates are reviewed by four separate reviewers and their comments and scores which range from 1 (lowest) to 5 (highest) are stored on a review record that is a detail record for a candidate. What is the best way to indicate that a combined review score of 15 or better is required to recommend that the candidate come in for an interview?**

- **A.** Use a Validation Rule on a total score field on the candidate record that prevents a recommended field from being true if the total score is less than 15. ❌
- **B.** Use a Rollup Summary field to calculate the sum of the review scores, and store this in a total score field on the candidate. ✅
- **C.** Use Visual Workflow to set a recommended field on the candidate whenever the cumulative review score is 15 or better. ❌
- **D.** Use a Workflow Rule to calculate the sum of the review scores and send an email to the hiring manager when the total is 15 or better. ❌

**📝 Dịch tiếng Việt:**
> Ứng viên được đánh giá bởi 4 người phỏng vấn khác nhau. Điểm số từ 1 (thấp nhất) đến 5 (cao nhất) được lưu trên bản ghi Review (là bản ghi con Detail của đối tượng Candidate). Cách tốt nhất để hiển thị tổng điểm đánh giá từ 15 trở lên để đề xuất phỏng vấn tiếp theo là gì?

**💬 Giải thích gốc (English):**
> Rollup Summary Field: This field type allows you to perform calculations on related records, such as summing up the review scores. By creating a rollup summary field on the candidate record, you can automatically calculate the total score from the related review records.

**✅ Tại sao đáp án đúng:**
> Tạo một trường Roll-up Summary trên đối tượng cha Candidate để tự động tính tổng (SUM) điểm số từ các bản ghi Review con liên quan (B). Đây là giải pháp hoàn toàn no-code cực kỳ sạch sẽ và tối ưu hiệu năng của hệ thống.

**❌ Tại sao đáp án sai:**
> **A.** Validation Rule chỉ dùng để chặn lưu dữ liệu sai logic chứ không thể tự động tính toán tổng điểm từ con lên cha.
> **C.** Sử dụng Visual Flow để set đề xuất là phương án quá phức tạp và thừa thãi khi ta hoàn toàn có thể giải quyết nhanh bằng công cụ Roll-up no-code có sẵn.
> **D.** Workflow Rule đời cũ không hỗ trợ tính tổng SUM các bản ghi con ngược lên cha một cách trực tiếp như Roll-up.

**💡 Từ khóa ghi nhớ:** `Tính tổng điểm từ các bản ghi con Detail lên cha Master -> Tạo trường ROLL-UP SUMMARY kiểu SUM.`

---

## Câu 209

**🔵 A developer needs an Apex method that can process Account or Contact records. Which method signature should the developer use?**

- **A.** public void doWork(Account | | Contact) ❌
- **B.** public void doWork(Record theRecord) ❌
- **C.** public void doWork(Account Contact) ❌
- **D.** public void doWork(sObject theRecord) ✅

**📝 Dịch tiếng Việt:**
> Dùng kiểu dữ liệu nào để xử lý cả Account và Contact trong 1 method?

**💬 Giải thích gốc (English):**
> In Apex, sObject is the generic base class for all objects in Salesforce. This allows the method to accept any standard or custom object, including Account and Contact.

**✅ Tại sao đáp án đúng:**
> Dùng `sObject` vì nó là lớp cha của mọi object.

**❌ Tại sao đáp án sai:**
> **A.** Sai cú pháp khai báo tham số.
> **C.** Apex không cho phép dùng toán tử OR trong signature.
> **D.** Không có kiểu dữ liệu nào tên là 'Record' trong Apex.

**💡 Từ khóa ghi nhớ:** `Muốn đa năng -> Dùng sObject.`

---

## Câu 210

**🔵 Which Salesforce org has a complete duplicate copy of the production org including data and configuration?**

- **A.** Developer Pro Sandbox ❌
- **B.** Partial Copy Sandbox ❌
- **C.** Production ❌
- **D.** Full Sandbox ✅

**📝 Dịch tiếng Việt:**
> Loại sandbox nào là bản sao y hệt của Production bao gồm cả dữ liệu và cấu hình?

**💬 Giải thích gốc (English):**
> Sandbox Types
> Developer Sandbox – A Developer sandbox is intended for development and testing in an isolated environment. A Developer Sandbox includes a copy of your production org’s configuration (metadata).
> Developer Pro Sandbox – A Developer Pro sandbox is intended for development and testing in an isolated environment and can host larger data sets than a Developer sandbox. A Developer Pro sandbox includes a copy of your production org’s configuration (metadata). Use a Developer Pro sandbox to handle more development and quality assurance tasks and for integration testing or user training.
> Partial Copy Sandbox – A Partial Copy sandbox is intended to be used as a testing environment. This environment includes a copy of your production org’s configuration (metadata) and a sample of your production org’s data as defined by a sandbox template. Use a Partial Copy sandbox for quality assurance tasks such as user acceptance testing, integration testing, and training.
> Full Sandbox – A Full sandbox is intended to be used as a testing environment. Only Full sandboxes support performance testing, load testing, and staging. Full sandboxes are a replica of your production org, including all data, such as object records and attachments, and metadata. The length of the refresh interval makes it difficult to use Full sandboxes for development.
> We recommend that you apply a sandbox template so that your sandbox contains only the records that you need for testing or other tasks.

**✅ Tại sao đáp án đúng:**
> Full Sandbox là 'trùm cuối'. Nó copy 100% Metadata và 100% Records từ Production. Thường dùng cho Performance Test hoặc UAT.

**❌ Tại sao đáp án sai:**
> **A.** Partial Copy chỉ copy cấu hình và một lượng data nhỏ theo mẫu (Template).
> **B.** Developer Pro chỉ copy cấu hình (Metadata), không có dữ liệu thực tế.
> **D.** Production là môi trường thật, không phải là một bản sao sandbox.

**💡 Từ khóa ghi nhớ:** `Sandbox: Full = Tất cả; Partial = Một phần; Dev = Trắng bóc (chỉ cấu hình).`

---

## Câu 211

**🔵 Universal Containers stores Orders and Line Items in Salesforce. For security reasons, financial representatives are allowed to see information on the Order such as order amount, but they are not allowed to see the Line Items on the Order. Which type of relationship should be used?**

- **A.** Direct Lookup ❌
- **B.** Indirect Lookup ❌
- **C.** Master-Detail ❌
- **D.** Lookup ✅

**📝 Dịch tiếng Việt:**
> Dùng loại quan hệ nào để user thấy Order nhưng không được thấy Line Items?

**💬 Giải thích gốc (English):**
> Using a Lookup relationship allows you to control access to the related records independently. This means financial representatives can see the Order information without having access to the Line Items.

**✅ Tại sao đáp án đúng:**
> Lookup cho phép bảo mật độc lập. Thấy Cha chưa chắc đã thấy Con.

**❌ Tại sao đáp án sai:**
> **A.** Indirect lookup chỉ dành cho External Objects.
> **B.** Direct Lookup không giúp giải quyết vấn đề phân tách quyền Sharing.
> **D.** Master-Detail kế thừa quyền. Thấy cha là thấy con ngay -> Sai yêu cầu.

**💡 Từ khóa ghi nhớ:** `Bảo mật riêng tư = Lookup. Sống chết có nhau = Master-Detail.`

---

## Câu 212

**🔵 Which two events need to happen when deploying to a production org? (Choose two.)**

- **A.** All Process Builder Processes must have at least 1% test coverage. ❌
- **B.** All Apex code must have at least 75% test coverage. ✅
- **C.** All triggers must have at least 1% test coverage. ✅
- **D.** All Visual Flows must have at least 1% test coverage. ❌

**📝 Dịch tiếng Việt:**
> 2 điều kiện cần khi deploy lên Production?

**💬 Giải thích gốc (English):**
> You must have at least 75% of your Apex covered by unit tests to deploy your code to production environments.
> Ensure all tests pass and at least 1% of coverage is applied to all triggers

**✅ Tại sao đáp án đúng:**
> B: Tổng Org phải đạt 75%. D: Mỗi trigger phải có coverage > 0%.

**❌ Tại sao đáp án sai:**
> **A.** Flow không bắt buộc test coverage.
> **C.** Process Builder cũng không bắt buộc test coverage.

**💡 Từ khóa ghi nhớ:** `Deploy Pro: Toàn Org 75%, Mỗi Trigger > 0%.`

---

## Câu 213

**🔵 An Approval Process is defined in the Expense_Item__c object. A business rule dictates that whenever a user changes the Status to 'Submitted' on an Expense_Report__c record, all the Expense_Item__c records related to the expense report must enter the approval process individually. Which approach should be used to ensure the business requirement is met?**

- **A.** Create a Process Builder on Expense_Report__c with an 'Apex' action type to submit all related Expense_Item__c records when the criteria is met. ❌
- **B.** Create a Process Builder on Expense_Report__c to mark the related Expense_Item__c as submittable and a trigger on Expense_Item__c to submit the records for approval. ❌
- **C.** Create two Process Builders, one on Expense_Report__c to mark the related Expense_Item__c as submittable and the second on Expense_Item__c to submit the records for approval. ✅
- **D.** Create a Process Builder on Expense_Report__c with a 'Submit for Approval' action type to submit all related Expense_Item__c records when the criteria are met. ❌

**📝 Dịch tiếng Việt:**
> Làm sao để khi đổi Status trên Expense_Report__c thì tất cả các bản ghi Expense_Item__c liên quan đều được gửi duyệt riêng lẻ?

**✅ Tại sao đáp án đúng:**
> Đây là bài toán đệ quy logic. PB 1 trên Report sẽ update 1 hidden field trên Items. PB 2 trên Item thấy field đó đổi thì kích hoạt Action 'Submit for Approval' cho chính nó.

**❌ Tại sao đáp án sai:**
> **B.** Kết hợp Trigger thì cũng được nhưng dùng 2 PB (No-code) sẽ đồng nhất và dễ quản lý hơn trong trường hợp này.
> **C.** Gọi Apex thì overkill và tốn công viết code test, trong khi No-code xử lý được.
> **D.** PB trên bản ghi cha không thể gọi hành động 'Submit for Approval' cho danh sách các bản ghi con cùng một lúc được.

**💡 Từ khóa ghi nhớ:** `Keywords: Individual Approval -> Action 'Submit for Approval' phải nằm trên chính Object đó.`

---

## Câu 214

**🔵 A developer is asked to set a picklist field to 'Monitor' on any new Leads owned by a subnet of Users. How should the developer implement this request?**

- **A.** Create an after insert Lead trigger. ❌
- **B.** Create a before insert Lead trigger. ❌
- **C.** Create a record-triggered Flow. ✅
- **D.** Create a Lead formula field. ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên được yêu cầu tự động gán một trường picklist thành giá trị 'Monitor' đối với bất kỳ bản ghi Lead mới nào được sở hữu bởi một nhóm nhỏ người dùng (Users subnet). Giải pháp thiết kế nào là tối ưu và phù hợp nhất?

**💬 Giải thích gốc (English):**
> Creating a record-triggered Flow is indeed a powerful and flexible way to handle this requirement. With a Flow, you can easily set the picklist field to ‘Monitor’ for new Leads owned by a specific subset of Users without writing any code.

**✅ Tại sao đáp án đúng:**
> Tạo một Record-triggered Flow (C). Đây là công cụ tự động hóa no-code hiện đại được Salesforce khuyến nghị tối cao hiện nay thay cho code trigger, có khả năng so khớp chủ sở hữu và cập nhật giá trị trường cực kỳ mượt mà trước khi bản ghi lưu xuống DB.

**❌ Tại sao đáp án sai:**
> **A.** after insert trigger là quá muộn để cập nhật trường trên chính bản ghi đó, vì dữ liệu đã ghi xuống ổ cứng, bắt buộc phải dùng thêm câu lệnh DML update gây lãng phí tài nguyên.
> **B.** before insert trigger viết code giải quyết tốt nhưng tốn công bảo trì hơn nhiều so với Flow no-code tiện lợi.
> **D.** Formula field chỉ hiển thị giá trị dạng đọc (Read-only), người dùng không thể chỉnh sửa và không thể gán giá trị cứng cố định như picklist.

**💡 Từ khóa ghi nhớ:** `Tự động gán trị khi lưu bản ghi no-code -> Luôn chọn RECORD-TRIGGERED FLOW.`

---

## Câu 215

**🔵 Which three process automations can immediately send an email notification to the owner of an Opportunity when its Amount is changed to be greater than $10,000? (Choose three.)**

- **A.** Process Builder ✅
- **B.** Escalation Rule ❌
- **C.** Flow Builder ✅
- **D.** Approval Process ❌
- **E.** Workflow Rule ✅

**📝 Dịch tiếng Việt:**
> Ba công cụ tự động hóa quy trình nào sau đây có thể lập tức gửi một thông báo email (email notification) cho chủ sở hữu Opportunity khi trường Amount bị thay đổi lớn hơn $10,000? (Chọn 3)

**💬 Giải thích gốc (English):**
> The three process automations that can immediately send an email notification to the owner of an Opportunity when its Amount is changed to be greater than $10,000 are:
> Process Builder
> Flow Builder
> Workflow Rule
> Escalation Rules are primarily used for cases, not opportunities. They are designed to escalate cases to a higher level of support if they are not resolved within a certain time frame. They do not support sending email notifications based on changes to Opportunity fields.
> Approval Processes are used to automate the approval of records. While they can send email notifications, they are triggered by the submission of records for approval, not by changes to field values like the Opportunity Amount. Therefore, they are not suitable for this specific requirement.

**✅ Tại sao đáp án đúng:**
> A: Process Builder. C: Flow Builder (hiện đại). E: Workflow Rule (cổ điển). Cả 3 công cụ no-code này đều hỗ trợ bắt sự kiện thay đổi dữ liệu và kích hoạt hành động gửi Email Alert ngay lập tức.

**❌ Tại sao đáp án sai:**
> **B.** Escalation Rule chỉ dùng riêng cho đối tượng Case để tự động chuyển tiếp vụ việc quá hạn hỗ trợ, không dùng cho Opportunity.
> **D.** Approval Process dùng cho quy trình duyệt bản ghi, không dùng cho việc tự động gửi email cảnh báo thông thường khi cập nhật trường.

**💡 Từ khóa ghi nhớ:** `Tự động gửi Email cảnh báo khi đổi trường -> Dùng Flow Builder, Process Builder, hoặc Workflow Rule.`

---

## Câu 216

**🔵 A developer needs to confirm that a Contact trigger works correctly without changing the organization's data. What should the developer do to test the Contact trigger?**

- **A.** Use Deploy from the VSCode IDE to deploy an 'Insert Contact' Apex class. ❌
- **B.** Use the New button on the Salesforce Contacts Tab to create a new Contact record. ❌
- **C.** Use the Open Execute Anonymous feature on the Developer Console to run an 'Insert Contact' DML statement. ❌
- **D.** Use the Test menu on the Developer Console to run all test classes for the Contact trigger. ✅

**📝 Dịch tiếng Việt:**
> Làm sao để kiểm tra Trigger Contact chạy đúng mà không làm hỏng/thay đổi dữ liệu thật của Org?

**💬 Giải thích gốc (English):**
> Running test classes is the best practice for testing triggers in Salesforce. Test classes allow you to verify that your code works as expected without affecting the actual data in your organization. By using the Test menu in the Developer Console, you can run all test classes that include tests for the Contact trigger. This ensures that the trigger logic is executed and validated in a controlled environment.
> Deploying an ‘Insert Contact’ Apex class from VSCode IDE does not test the trigger directly. It only deploys the class to the organization.
> Creating a new Contact record directly in the Salesforce UI will change the organization’s data.
> Running an ‘Insert Contact’ DML statement using Execute Anonymous will also change the organization’s data.

**✅ Tại sao đáp án đúng:**
> Chỉ có chạy Unit Test (A) mới đảm bảo an toàn. Salesforce Unit Test chạy trong môi trường cô lập, dữ liệu tạo ra sẽ bị Rollback hoàn toàn sau khi test xong, Org vẫn sạch bóng quân thù.

**❌ Tại sao đáp án sai:**
> **B.** Execute Anonymous sẽ insert data THẬT vào Org, hỏng hết data.
> **D.** Tạo tay trên giao diện cũng là tạo data THẬT, làm sao mà 'không thay đổi dữ liệu' được.

**💡 Từ khóa ghi nhớ:** `Test an toàn = Unit Test Class. Dữ liệu Test chỉ là 'phù du', chạy xong là biến mất.`

---

## Câu 217

**🔵 Which control statement should a developer use to ensure that a loop body executes at least once?**

- **A.** for (init_stmt; exit_condition; increment_stmt) {...} ❌
- **B.** do {...} while (condition) ✅
- **C.** while (condition) {...} ❌
- **D.** for (variable : list_or_set) {...} ❌

**📝 Dịch tiếng Việt:**
> Cấu trúc vòng lặp điều khiển nào giúp lập trình viên đảm bảo rằng phần thân của vòng lặp (loop body) sẽ được thực thi ít nhất một lần?

**💬 Giải thích gốc (English):**
> do {…} while (condition): This control statement ensures that the loop body executes at least once because the condition is checked after the loop body has executed.

**✅ Tại sao đáp án đúng:**
> Cú pháp do {...} while (condition) (B). Vòng lặp do-while sẽ thực hiện toàn bộ khối mã lệnh trong thân trước rồi mới tiến hành kiểm tra điều kiện lặp ở cuối, do đó bảo đảm chạy ít nhất 1 lần bất chấp điều kiện đúng hay sai.

**❌ Tại sao đáp án sai:**
> **A.** Vòng lặp for cơ bản kiểm tra điều kiện thoát ngay ở đầu, nếu sai từ đầu sẽ không chạy lần nào.
> **C.** Vòng lặp while kiểm tra điều kiện lặp trước khi chạy thân vòng lặp nên có thể không chạy lần nào.
> **D.** Vòng lặp for-each (duyệt list/set) sẽ hoàn toàn không chạy lần nào nếu danh sách truyền vào bị rỗng.

**💡 Từ khóa ghi nhớ:** `Muốn chạy loop ít nhất 1 lần -> Chọn ngay cấu trúc DO - WHILE!`

---

## Câu 218

**🔵 Which two declarative process automation features can be directly invoked when a field value changes on a record? (Choose two.)**

- **A.** Cloud Flow Designer ❌
- **B.** Process Builder processes ✅
- **C.** Validation rules ❌
- **D.** Workflow rules ✅

**📝 Dịch tiếng Việt:**
> Hai tính năng tự động hóa quy trình dạng khai báo no-code nào có thể được kích hoạt trực tiếp ngay khi giá trị một trường trên bản ghi bị thay đổi? (Chọn 2)

**💬 Giải thích gốc (English):**
> Salesforce retired Cloud Flow Designer in Winter '20. Users were encouraged to transition to the newer Flow Builder, which offers a more modern and user-friendly interface for creating flows. Since now Salesforce is retiring the Workflow rules.

**✅ Tại sao đáp án đúng:**
> B: Process Builder processes. D: Workflow rules. Cả hai công cụ này đều có bộ lọc tiêu chí kích hoạt chạy ngay khi bản ghi được tạo hoặc cập nhật sửa đổi trường dữ liệu.

**❌ Tại sao đáp án sai:**
> **A.** Cloud Flow Designer là trình thiết kế Flow đời cũ bằng Flash đã bị Salesforce khai tử hoàn toàn từ lâu.
> **C.** Validation rules chỉ dùng để chặn lưu bản ghi sai logic và ném ra thông báo lỗi, không phải là công cụ thực thi hành động tự động hóa.

**💡 Từ khóa ghi nhớ:** `Tự động hóa kích hoạt khi đổi trường no-code -> Dùng Flow/Process Builder hoặc Workflow Rule.`

---

## Câu 219

**🔵 Which two strategies should a developer use to avoid hitting governor limits when developing in a multi-tenant environment? (Choose two.)**

- **A.** Use collections to store all fields from a related object and not just minimally required fields. ❌
- **B.** Use methods from the "Limits" class to monitor governor limits. ✅
- **C.** Use SOQL for loops to iterate data retrieved from queries that return a high number of rows. ✅
- **D.** Use variables within Apex classes to store large amounts of data. ❌

**📝 Dịch tiếng Việt:**
> Hai chiến lược nào lập trình viên nên sử dụng để tránh bị chạm giới hạn governor limits khi lập trình trên môi trường đa khách thuê (multi-tenant) của Salesforce? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> B: Sử dụng các phương thức từ lớp Limits (như Limits.getQueries()) để theo dõi lượng tài nguyên đã ngốn và có logic ứng biến. C: Sử dụng cú pháp vòng lặp SOQL For Loop (for(Account a : [SELECT ...])) để Salesforce tự động chia lô nhỏ 200 bản ghi xử lý, tối ưu bộ nhớ heap tuyệt đối.

**❌ Tại sao đáp án sai:**
> **A.** Lấy thừa thãi các trường không cần thiết vào collection làm phình to bộ nhớ heap cực nhanh, tăng nguy cơ dính lỗi LimitException.
> **D.** Lưu trữ lượng dữ liệu khổng lồ vào các biến tĩnh trong Apex class dễ gây tràn bộ nhớ heap (Heap limit exception).

**💡 Từ khóa ghi nhớ:** `Tránh giới hạn Governor Limits -> Dùng lớp Limits để theo dõi + Sử dụng SOQL For Loop tối ưu bộ nhớ.`

---

## Câu 220

**🔵 Which feature should a developer use to update an inventory count on related Product records when the status of an Order is modified to indicate it is fulfilled?**

- **A.** Process Builder process ✅
- **B.** Lightning component ❌
- **C.** Visualforce page ❌
- **D.** Workflow rule ❌

**📝 Dịch tiếng Việt:**
> Tính năng nào lập trình viên nên sử dụng để tự động cập nhật số lượng tồn kho trên Product records liên quan khi trạng thái của Order thay đổi thành 'Fulfilled'?

**✅ Tại sao đáp án đúng:**
> Sử dụng Process Builder process (A) (hoặc Flow Builder hiện đại). Mối quan hệ từ Product sang Order có thể là nhiều chiều, việc cập nhật chéo đối tượng từ Order sang Product cha/con có thể thực hiện no-code dễ dàng bằng Process/Flow.

**❌ Tại sao đáp án sai:**
> **B.** Lightning Component xây dựng giao diện tương tác người dùng, không phải công cụ tự động hóa chạy ngầm dưới database layer.
> **C.** Visualforce page tương tự LWC, chỉ phục vụ hiển thị giao diện.
> **D.** Workflow rule đời cũ cấm cập nhật chéo đối tượng đi ngang/xuống (chỉ hỗ trợ cập nhật chéo từ con lên cha trong lookup đặc biệt).

**💡 Từ khóa ghi nhớ:** `Cập nhật chéo đối tượng con-cha-cháu no-code -> Dùng Flow Builder hoặc Process Builder.`

---

## Câu 221

**🔵 The operation manager at a construction company uses a custom object called Machinery to manage the usage and maintenance of its cranes and other machinery. The manager wants to be able to assign machinery to different constructions jobs, and track the dates and costs associated with each job. More than one piece of machinery can be assigned to one construction job. What should a developer do to meet these requirements?**

- **A.** Create a lookup field on the Construction Job object to the Machinery object. ❌
- **B.** Create a lookup field on the Machinery object to the Construction Job object. ❌
- **C.** Create a junction object with Master-Detail Relationship to both the Machinery object and the Construction Job object. ✅
- **D.** Create a Master-Detail Lookup on the Machinery object to the Construction Job object. ❌

**📝 Dịch tiếng Việt:**
> Một công ty xây dựng dùng custom object Machinery để quản lý máy móc. Manager muốn gán máy móc cho các Construction Jobs khác nhau để theo dõi ngày và chi phí. Một Construction Job có thể dùng nhiều máy móc, một máy móc dùng cho nhiều Job. Lập trình viên nên làm gì?

**✅ Tại sao đáp án đúng:**
> Tạo một Junction Object (C) trung gian có hai mối quan hệ Master-Detail trỏ về hai đối tượng Machinery và Construction Job. Đây là thiết kế chuẩn mực cho mối quan hệ Nhiều-Nhiều (Many-to-Many) để theo dõi các thông số riêng của mỗi lần gán.

**❌ Tại sao đáp án sai:**
> **A.** Đặt lookup trên Job trỏ đến Machinery giới hạn mỗi Job chỉ được gán tối đa 1 máy móc tại một thời điểm.
> **B.** Đặt lookup trên Machinery trỏ đến Job giới hạn mỗi máy móc chỉ được tham gia tối đa 1 Job tại một thời điểm.
> **D.** Master-Detail Lookup là khái niệm bị ghép sai thuật ngữ, không tồn tại loại trường này trong Salesforce.

**💡 Từ khóa ghi nhớ:** `Mối quan hệ Nhiều-Nhiều (Many-to-Many) -> Bắt buộc tạo đối tượng trung gian JUNCTION OBJECT.`

---

## Câu 222

**🔵 A developer needs to have records with specific field values in order to test a new Apex class. What should the developer do to ensure the data is available to the test?**

- **A.** Use SOQL to query the org for the required data. ❌
- **B.** Use Anonymous Apex to create the required data. ❌
- **C.** Use Test.loadData() and reference a CSV file. ❌
- **D.** Use Test.loadData() and reference a static resource. ✅

**📝 Dịch tiếng Việt:**
> Làm sao để nạp bản ghi có sẵn các giá trị cụ thể phục vụ việc test Apex?

**💬 Giải thích gốc (English):**
> Using the Test.loadData method, you can populate data in your test methods without having to write many lines of code.
> Follow these steps:
> 1. Add the data in a .csv file.
> 2. Create a static resource for this file.
> 3. Call Test.loadData within your test method and passing it the sObject type token and the static resource name.

**✅ Tại sao đáp án đúng:**
> Sử dụng `Test.loadData(SObjectType, 'StaticResourceName')`. Mày chuẩn bị file CSV, đẩy lên Static Resource, rồi gọi hàm này trong code test để nó tự nạp data vào, vừa sạch vừa nhanh.

**❌ Tại sao đáp án sai:**
> **C.** Hàm loadData nhận vào tên 'Static Resource', không phải đường dẫn trực tiếp tới file CSV trên máy mày.
> **A.** Anonymous Apex không giúp ích gì cho việc chạy Unit Test tự động.

**💡 Từ khóa ghi nhớ:** `Data Test nhiều/phức tạp -> CSV + Static Resource + Test.loadData().`

---

## Câu 223

**🔵 A developer created a Lightning component to display a short text summary for an object and wants to use it with multiple Apex classes. How should the developer design the Apex classes?**

- **A.** Have each class define method getObject() that returns the sObject that is controlled by the Apex class. ❌
- **B.** Extend each class from the same base class that has a method getTextSummary() that returns the summary. ❌
- **C.** Have each class implement an interface that defines method getTextSummary() that returns the summary. ✅
- **D.** Have each class define method getTextSummary() that returns the summary. ❌

**📝 Dịch tiếng Việt:**
> Developer tạo một component Lightning hiển thị văn bản tóm tắt ngắn gọn và muốn dùng chung component này với nhiều class Apex khác nhau. Lập trình viên nên thiết kế các class Apex này như thế nào?

**✅ Tại sao đáp án đúng:**
> Cho mỗi class Apex implements chung một Interface (C). Interface này định nghĩa phương thức ký mẫu 'getTextSummary()' trả về chuỗi văn bản tóm tắt. Component chỉ việc gọi hàm thông qua Interface, đạt tính đa hình tối cao trong lập trình.

**❌ Tại sao đáp án sai:**
> **A.** Hàm getObject trả về sObject thô không giải quyết được tính đồng bộ hóa logic định dạng tóm tắt văn bản tùy chỉnh của từng class.
> **B.** Apex chỉ hỗ trợ đơn kế thừa (single inheritance) từ lớp cha base class, việc bắt ép kế thừa base class làm hạn chế khả năng mở rộng của các class sau này.
> **D.** Tự định nghĩa hàm không qua Interface làm mất đi tính ràng buộc biên dịch mạnh, component không thể gọi động một cách an toàn.

**💡 Từ khóa ghi nhớ:** `Linh hoạt dùng chung LWC với nhiều Apex Class khác nhau -> Thiết kế các class implements chung một INTERFACE.`

---

## Câu 224

**🔵 A developer wrote Apex code that calls out to an external system. How should a developer write the test to provide test coverage?**

- **A.** Write a class that implements the HTTPCalloutMock interface. ✅
- **B.** Write a class that extends HTTPCalloutMock. ❌
- **C.** Write a class that extends WebserviceMock. ❌
- **D.** Write a class that implements the WebserviceMock interface. ❌

**📝 Dịch tiếng Việt:**
> Viết test cho Callout thế nào cho đúng?

**💬 Giải thích gốc (English):**
> To provide test coverage for Apex code that calls out to an external system, the developer should use the HTTPCalloutMock interface. This allows the developer to mock the HTTP response and test the callout logic without actually making a real HTTP request.

**✅ Tại sao đáp án đúng:**
> Implements interface `HttpCalloutMock`.

**❌ Tại sao đáp án sai:**
> **A.** Dùng cho SOAP API, không phải REST/HTTP.
> **C.** Sai cả về kiểu API lẫn cách dùng (implements vs extends).
> **D.** Apex dùng Interface (implements), không dùng kế thừa class cho Mock này.

**💡 Từ khóa ghi nhớ:** `Keyword: HTTP Callout Test -> implements HttpCalloutMock.`

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
> Số lượng câu truy vấn SOQL tối đa sẽ được thực thi khi chạy đoạn mã Apex dưới đây là bao nhiêu? [Code SOQL inside For]

**💬 Giải thích gốc (English):**
> Initial Query: 1
> Queries Inside Loop: Up to 5 (one for each Account)

**✅ Tại sao đáp án đúng:**
> Số lượng SOQL tối đa là 6 (C). Câu truy vấn SOQL đầu tiên lấy ra danh sách tối đa 5 bản ghi Account (LIMIT 5). Vòng lặp for chạy đúng 5 lần, mỗi lần nổ thêm 1 câu truy vấn SOQL con bên trong. Tổng cộng tối đa là 1 + 5 = 6 câu lệnh.

**❌ Tại sao đáp án sai:**
> **A.** Sai số lượng tính toán thực tế.
> **B.** Quên tính câu lệnh SOQL query Account nằm ngoài vòng lặp.
> **D.** Tính toán sai số vòng chạy của list Account.

**💡 Từ khóa ghi nhớ:** `Mẹo đếm SOQL: Số SOQL = (SOQL ngoài loop) + (Số vòng lặp * SOQL trong loop).`

---

## Câu 226

**🔵 Which process automation can be used to calculate the shipping cost for an Order when the Order is placed and apply a percentage of the shipping cost to some of the related Order Products?**

- **A.** Lightning Component ❌
- **B.** Flow Builder ✅
- **C.** Entitlement Rules ❌
- **D.** Approval Process ❌

**📝 Dịch tiếng Việt:**
> Hai loại tự động hóa quy trình nào có thể được sử dụng để tính toán chi phí vận chuyển cho một Đơn hàng (Order) khi Đơn hàng được tạo và áp dụng một tỷ lệ phần trăm của chi phí vận chuyển cho một số Sản phẩm của Đơn hàng (Order Products) liên quan? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> Cả Flow và Process Builder đều có khả năng thực hiện logic tính toán và duyệt qua các bản ghi liên quan (Child records) để cập nhật dữ liệu.

**❌ Tại sao đáp án sai:**
> **A.** Workflow chỉ update được field của chính bản ghi đó hoặc Parent (Master-Detail).
> **C.** Approval Process dùng để phê duyệt, không phải để tính toán logic phức tạp cho record con.

**💡 Từ khóa ghi nhớ:** `Keywords: Update Related Records -> Flow hoặc Process Builder.`

---

## Câu 227

**🔵 A developer created a child Lightning web component nested inside a parent Lightning web component. The parent component needs to pass a string value to the child component. In which two ways can this be accomplished? (Choose two.)**

- **A.** The parent component can use a custom event to pass the data to the child component. ✅
- **B.** The parent component can invoke a method in the child component. ❌
- **C.** The parent component can use a public property to pass the data to the child component. ✅
- **D.** The parent component can use the Apex controller class to send data to the child component. ❌

**📝 Dịch tiếng Việt:**
> Component Cha truyền data xuống cho Component Con bằng cách nào? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> C: Dùng @api trên property của Con. D: Dùng @api trên method của Con để Cha gọi xuống.

**❌ Tại sao đáp án sai:**
> **A.** Custom Event dùng để truyền ngược từ Con LÊN Cha.
> **B.** Dùng Apex để truyền data giữa 2 component cùng nằm trên trình duyệt là cực kỳ kém hiệu quả.

**💡 Từ khóa ghi nhớ:** `Giao tiếp LWC: Xuống dùng @api, Lên dùng Event.`

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
> B: Sử dụng CustomEvent để truyền dữ liệu và thông báo từ component con ngược lên component cha. D: Sử dụng cấu hình mặc định an toàn: 'bubbles: false' và 'composed: false' để ngăn chặn event nổi loạn ra ngoài shadow DOM. (Lưu ý: Đáp án C trong ngân hàng đề thi gốc thỉnh thoảng có sai sót lý thuyết, tuy nhiên B và D mới là best practice chuẩn nhất của LWC).

**❌ Tại sao đáp án sai:**
> **A.** event.detail dùng để truyền data đi, chứ bản thân nó không quyết định phạm vi giao tiếp trong shadow tree.
> **C.** Sai bảo mật shadow DOM vì event.target bị retargeted khi đi xuyên ranh giới shadow tree để tránh rò rỉ cấu trúc linh kiện nội bộ.

**💡 Từ khóa ghi nhớ:** `LWC Events: Luôn dùng CustomEvent từ con lên cha. Cấu hình bubbles: false và composed: false để bảo mật shadow DOM!`

---

## Câu 229

**🔵 A developer migrated functionality from JavaScript Remoting to a Lightning web component and wants to use the existing getOpportunities() method to provide data. Which modification to the method is necessary?**

- **A.** The method must return a String of a serialized JSON Array. ❌
- **B.** The method must be decorated with (cacheable=true). ❌
- **C.** The method must be decorated with @AuraEnabled. ✅
- **D.** The method must return a JSON Object. ❌

**📝 Dịch tiếng Việt:**
> Developer di chuyển một tính năng từ JavaScript Remoting cũ sang Lightning Web Component (LWC) mới và muốn sử dụng lại phương thức Apex getOpportunities() có sẵn. Lập trình viên bắt buộc phải chỉnh sửa gì đối với phương thức này?

**✅ Tại sao đáp án đúng:**
> Phương thức Apex đó bắt buộc phải được gắn annotation @AuraEnabled (C) ở đầu để LWC có thể nhận diện, kết nối và gọi lấy dữ liệu thành công.

**❌ Tại sao đáp án sai:**
> **A.** Apex tự động serialize các đối tượng sObject thành JSON khi trả về cho LWC, lập trình viên cấm tự viết code serialize thành String JSON Array thủ công gây nặng nề.
> **B.** cacheable=true là tùy chọn khuyến khích để tăng tốc độ lưu cache dữ liệu, không phải điều kiện bắt buộc để LWC kết nối được.
> **D.** LWC nhận kiểu sObject chuẩn trực tiếp từ Apex, không bắt buộc phải trả về kiểu đối tượng JSON.

**💡 Từ khóa ghi nhớ:** `Muốn LWC gọi được method trong Apex Class -> Bắt buộc gắn annotation @AuraEnabled.`

---

## Câu 230

**🔵 A developer must provide a custom user interface when users edit a Contact. Users must be able to use the interface in Salesforce Classic and Lightning Experience. What should the developer do to provide the custom user interface?**

- **A.** Override the Contact's Edit button with a Visualforce page in Salesforce Classic and a Lightning component in Lightning Experience. ✅
- **B.** Override the Contact's Edit button with a Visualforce page in Salesforce Classic and a Lightning page in Lightning Experience. ❌
- **C.** Override the Contact's Edit button with a Lightning component in Salesforce Classic and a Lightning component in Lightning Experience. ❌
- **D.** Override the Contact's Edit button with a Lightning page in Salesforce Classic and a Visualforce page in Lightning Experience. ❌

**📝 Dịch tiếng Việt:**
> Developer cần cung cấp giao diện người dùng tùy chỉnh khi người dùng Edit một Contact. Giao diện này phải hoạt động được trên cả hai môi trường Salesforce Classic và Lightning Experience. Lập trình viên nên làm gì?

**✅ Tại sao đáp án đúng:**
> Ghi đè (Override) nút Edit của Contact bằng một trang Visualforce trong môi trường Salesforce Classic, và ghi đè bằng một Lightning component trong môi trường Lightning Experience (A) để tối ưu giao diện trên cả hai môi trường.

**❌ Tại sao đáp án sai:**
> **B.** Lightning Page dùng để xây dựng trang tổng quan chứ không phải thành phần đóng gói có thể dùng để ghi đè trực tiếp nút Edit.
> **C.** Salesforce Classic đời cũ không hỗ trợ biên dịch và hiển thị trực tiếp Lightning Component nguyên bản mượt mà bằng Visualforce.
> **D.** Bị đảo ngược sai vị trí công nghệ giữa Classic (dùng Visualforce) và Lightning (dùng Lightning Component).

**💡 Từ khóa ghi nhớ:** `Ghi đè action chuẩn (Override button) -> Classic dùng Visualforce Page. Lightning Experience dùng Lightning Component.`

---

## Câu 231

**🔵 Which Lightning code segment should be written to declare dependencies on a Lightning component, c:accountList, that is used in a Visualforce page?
A.
<aura:application access="GLOBAL">
<aura:dependency resource="c:accountList"/>
</aura:application>
B.
<aura:application access="GLOBAL" extends="ltng:outApp">
<aura:dependency resource="c:accountList"/>
</aura:application>
C.
<aura:component access="GLOBAL">
<aura:dependency resource="c:accountList">
</aura:component>
D.
<aura:component access="GLOBAL" extends="ltng:outApp">
<aura:dependency resource="c:accountList"/>
</aura:component>**


**📝 Dịch tiếng Việt:**
> Đoạn code Lightning nào dưới đây được viết đúng cú pháp để khai báo các thành phần phụ thuộc (dependencies) cho một component c:accountList khi nhúng vào trang Visualforce?

**💬 Giải thích gốc (English):**
> To describe the components that you want to deploy outside of Salesforce, create a Lightning Out app. A Lightning Out app is a special standalone Aura app defined with the <aura:application> tag. Add components to the app with the <aura:dependency> tag

**✅ Tại sao đáp án đúng:**
> Cú pháp B: <aura:application access='GLOBAL' extends='ltng:outApp'> <aura:dependency resource='c:accountList'/> </aura:application>. Để chạy được Lightning Out (nhúng component Lightning vào trang Visualforce hoặc app ngoài), bắt buộc phải tạo một standalone Aura App dùng từ khóa extends='ltng:outApp' và khai báo phụ thuộc bằng thẻ <aura:dependency>.

**❌ Tại sao đáp án sai:**
> **A.** Thiếu thuộc tính extends='ltng:outApp' làm ứng dụng độc lập thông thường, không thể kích hoạt được chế độ kết nối Lightning Out.
> **C.** Thẻ <aura:component> cấm khai báo thuộc tính extends='ltng:outApp' và không thể đóng vai trò làm app cầu nối cho Lightning Out.
> **D.** Tương tự C, Aura component không hỗ trợ làm app container kết nối cho Lightning Out.

**💡 Từ khóa ghi nhớ:** `Lightning Out kết nối Visualforce -> App cầu nối bắt buộc phải dùng <aura:application extends='ltng:outApp'>.`

---

## Câu 232

**🔵 A developer can use the debug log to see which three types of information? (Choose three.)**

- **A.** HTTP callouts to external systems ✅
- **B.** Database changes ✅
- **C.** Resource usage and limits ✅
- **D.** User login events ❌
- **E.** Actions triggered by time-based workflow ❌

**📝 Dịch tiếng Việt:**
> Lập trình viên có thể sử dụng Debug Log (Nhật ký gỡ lỗi) trong Salesforce để theo dõi ba loại thông tin nào sau đây? (Chọn 3)

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
> A: Các cuộc gọi API HTTP callouts ra hệ thống ngoài. B: Các thay đổi cơ sở dữ liệu (DML operations). C: Mức độ tiêu thụ tài nguyên và giới hạn governor limits của transaction. Đây là các dữ liệu cốt lõi ghi nhận cực kỳ tường tận trong debug log.

**❌ Tại sao đáp án sai:**
> **D.** Thông tin đăng nhập của người dùng được quản lý và theo dõi ở trang Login History riêng biệt, không hiển thị trong Apex transaction debug log.
> **E.** Các hành động kích hoạt bởi time-based workflow được giám sát riêng ở mục Time-Based Workflow Queue trong Setup.

**💡 Từ khóa ghi nhớ:** `Debug Log Salesforce hiển thị -> DML (Database), Callouts (HTTP), Resource & Limits.`

---

## Câu 233

**🔵 A developer created a trigger on the Account object and wants to test if the trigger is properly bulkified. The developer team decided that the trigger should be tested with 200 account records with unique names. What two things should be done to create the test data within the unit test with the least amount of code? (Choose two.)**

- **A.** Use the @isTest(seeAllData=true) annotation in the test class. ❌
- **B.** Create a static resource containing test data. ✅
- **C.** Use the @isTest(isParallel=true) annotation in the test class. ❌
- **D.** Use Test.loadData to populate data in your test methods. ✅

**📝 Dịch tiếng Việt:**
> Tạo 200 bản ghi test trong unit test với lượng mã ít nhất? (Chọn 2)

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
> A: Tạo file CSV làm Static Resource. D: Gọi `Test.loadData()` để nạp 200 bản ghi từ file đó mà không cần viết vòng lặp DML.

**❌ Tại sao đáp án sai:**
> **B.** isParallel giúp các class test chạy song song để tiết kiệm thời gian, không giúp tạo data test.
> **C.** seeAllData=true cho phép truy cập data thật của Org, không phải cách tạo data ảo cho việc test bulkification.

**💡 Từ khóa ghi nhớ:** `Test Data Bulk: Static Resource (CSV) + Test.loadData().`

---

## Câu 234

**🔵 What can be developed using the Lightning Component framework?**

- **A.** Salesforce integrations ❌
- **B.** Salesforce Classic and Lightning user interface pages ❌
- **C.** Hosted web applications ❌
- **D.** Single-page web apps ✅

**📝 Dịch tiếng Việt:**
> Lightning Component framework dùng để phát triển cái gì?

**💬 Giải thích gốc (English):**
> Lightning Component Framework
> The Lightning Component framework is a UI framework for developing single-page web apps for mobile and desktop devices.

**✅ Tại sao đáp án đúng:**
> Framework này được thiết kế theo kiến trúc Single-Page Application (SPA), dữ liệu load động giúp trải nghiệm mượt mà trên cùng một trang.

**❌ Tại sao đáp án sai:**
> **B.** Integration thường dùng Apex hoặc External Services, framework UI chỉ là phần hiển thị.
> **C.** Dynamic web sites là khái niệm chung chung, trong Salesforce người ta gọi chính xác là SPA.
> **D.** Salesforce không 'host' các ứng dụng web thông thường kiểu này.

**💡 Từ khóa ghi nhớ:** `Lightning = SPA (Single Page App).`

---

## Câu 235

**🔵 A developer must create an Apex class, ContactController, that a Lightning component can use to search for Contact records. Users of the Lightning component should only be able to search for Contact records to which they have access. Which two will restrict the records correctly? (Choose two.)**

- **A.** public class ContactController ❌
- **B.** public with sharing class ContactController ✅
- **C.** public without sharing class ContactController ❌
- **D.** public inherited sharing class ContactController ✅

**📝 Dịch tiếng Việt:**
> Hai cách nào để giới hạn bản ghi theo quyền user cho một LWC controller?

**💬 Giải thích gốc (English):**
> With Sharing
> Use the with sharing keyword when declaring a class to enforce sharing rules of the current user. Explicitly setting this keyword ensures that Apex code runs in the current user context. Apex code that is executed with the executeAnonymous call and Connect in Apex always execute using the sharing rules of the current user.
> Without Sharing
> Use the without sharing keyword when declaring a class to ensure that the sharing rules for the current user are not enforced. For example, you can explicitly turn off sharing rule enforcement when a class is called from another class that is declared using with sharing.
> Inherited Sharing
> Use the inherited sharing keyword when declaring a class to enforce the sharing rules of the class that calls it. Using inherited sharing is an advanced technique to determine the sharing mode at runtime and design Apex classes that can run in either with sharing or without sharing mode.

**✅ Tại sao đáp án đúng:**
> A: with sharing ép class tuân thủ luật. C: inherited sharing kế thừa quyền từ class gọi nó (rất an toàn).

**❌ Tại sao đáp án sai:**
> **B.** Mặc định không ghi gì sẽ chạy ở chế độ System (thấy hết), không an toàn.
> **D.** without sharing là phớt lờ hoàn toàn quyền chia sẻ của user.

**💡 Từ khóa ghi nhớ:** `Apex Security: with sharing là lựa chọn an toàn nhất cho mọi controller.`

---

## Câu 236

**🔵 A developer must create a DrawList class that provides capabilities defined in the Sortable and Drawable interfaces.
public interface Sortable{
void sort();
}
public interface Drawable{
void draw();
}
Which is the correct implementation?
A.
public class DrawList implements Sortable, implements Drawable{
public void sort(){ /*implementation*/}
public void draw(){ /*implementation*/}
}
B.
public class DrawList implements Sortable, Drawable{
public void sort(){ /*implementation*/}
public void draw(){ /*implementation*/}
}
C.
public class DrawList extends Sortable, extends Drawable{
public void sort(){ /*implementation*/}
public void draw(){ /*implementation*/}
}
D.
public class DrawList extends Sortable, Drawable {
public void sort(){ /*implementation*/}
public void draw(){ /*implementation*/}
}**


**📝 Dịch tiếng Việt:**
> Lập trình viên cần tạo một class DrawList hiện thực hóa các chức năng được định nghĩa trong hai Interface Sortable và Drawable: [Interface Code]. Cách viết nào sau đây là đúng cú pháp Apex?

**💬 Giải thích gốc (English):**
> Option A: Incorrect because you cannot use implements twice.
> Option C, D: Incorrect because you cannot use extends with interfaces; extends is used for classes.

**✅ Tại sao đáp án đúng:**
> Cú pháp B: 'public class DrawList implements Sortable, Drawable'. Trong Apex, một lớp thông thường có thể hiện thực hóa nhiều interface cùng lúc bằng cách liệt kê tên các interface ngăn cách nhau bằng dấu phẩy sau một từ khóa 'implements' duy nhất.

**❌ Tại sao đáp án sai:**
> **A.** Sử dụng lặp lại từ khóa 'implements' hai lần độc lập là sai cú pháp biên dịch nghiêm trọng.
> **C.** Dùng từ khóa 'extends' đối với Interface là hoàn toàn sai, extends chỉ dùng khi một class kế thừa class khác.
> **D.** Tương tự C, không được phép extends interface trực tiếp ở khai báo class.

**💡 Từ khóa ghi nhớ:** `Apex Class implements nhiều Interface -> Chỉ dùng duy nhất 1 từ khóa 'implements', ngăn cách các interface bằng dấu phẩy.`

---

## Câu 237

**🔵 Which three options allow a developer to use custom styling in a Visualforce page? (Choose three.)**

- **A.** <apex:stylesheet> tag ✅
- **B.** Inline CSS ✅
- **C.** <apex:style>tag ❌
- **D.** <apex:stylesheets>tag ❌
- **E.** A static resource ✅

**📝 Dịch tiếng Việt:**
> Ba tùy chọn nào cho phép lập trình viên nhúng và sử dụng các định dạng CSS tùy chỉnh (custom styling) trong một trang Visualforce? (Chọn 3)

**💬 Giải thích gốc (English):**
> <apex:stylesheet> tag: This tag is used to include external CSS stylesheets in your Visualforce page1.
> Inline CSS: You can directly include CSS styles within the <style> tags in your Visualforce page1.
> A static resource: You can upload CSS files as static resources and reference them in your Visualforce page using the <apex:stylesheet> tag.

**✅ Tại sao đáp án đúng:**
> A: Thẻ <apex:stylesheet> để import file CSS. B: Viết mã CSS nội tuyến (Inline CSS) trực tiếp trong thẻ <style> của trang. E: Tải file CSS lên Static Resources và liên kết sử dụng trong trang. Đây là các kỹ thuật chuẩn để làm đẹp trang Visualforce.

**❌ Tại sao đáp án sai:**
> **C.** Không tồn tại thẻ nào tên là <apex:style> trong thư viện thành phần chuẩn của Visualforce.
> **D.** Không có thẻ dạng số nhiều <apex:stylesheets> trong hệ thống Visualforce.

**💡 Từ khóa ghi nhớ:** `Styling Visualforce -> 1. Thẻ <apex:stylesheet>; 2. Thẻ HTML <style> (inline); 3. File CSS trong Static Resource.`

---

## Câu 238

**🔵 When a user edits the Postal Code on an Account, a custom Account text field named 'Timezone' must be updated based on the values in a PostalCodeToTimezone__c custom object. How should a developer implement this feature?**

- **A.** Build an Account Workflow Rule. ❌
- **B.** Build an Account Assignment Rule. ❌
- **C.** Build an Account custom Trigger. ✅
- **D.** Build an Account Approval Process. ❌

**📝 Dịch tiếng Việt:**
> Khi Postal Code trên Account đổi, cần tra cứu Timezone từ một custom object khác để update lại Account. Dùng gì?

**💬 Giải thích gốc (English):**
> A trigger can handle the logic required to update the ‘Timezone’ field based on the Postal Code changes and the corresponding values in the PostalCodeToTimezone__c custom object.
> Build an Account Workflow Rule: Workflow rules are great for simple field updates, but they don’t support complex logic like querying another object (PostalCodeToTimezone__c) to determine the value of the ‘Timezone’ field.
> Build an Account Assignment Rule: Assignment rules are used to assign records to users or queues based on criteria. They don’t support updating fields based on related object data.
> Build an Account Approval Process: Approval processes are designed for managing record approvals and don’t support the kind of field update logic you’re looking for.

**✅ Tại sao đáp án đúng:**
> Flow Builder có thể thực hiện lệnh 'Get Records' để truy vấn dữ liệu từ object khác (cross-object) rồi gán ngược lại, cực kỳ linh hoạt.

**❌ Tại sao đáp án sai:**
> **A.** Workflow Rule chỉ có thể update field trên chính nó hoặc bản ghi cha (Master-detail), không thể 'đi chợ' sang object khác lấy data.
> **B.** Approval Process dùng để duyệt bản ghi, không liên quan đến logic tự động gán timezone.
> **D.** Assignment Rule chỉ dùng để gán 'chủ sở hữu' (Owner) cho Lead hoặc Case.

**💡 Từ khóa ghi nhớ:** `Mẹo thi: Cứ thấy logic 'Tra cứu Object khác rồi Update' -> Chọn Flow.`

---

## Câu 239

**🔵 Where can a developer identify the time taken by each process in a transaction using Developer Console log inspector?**

- **A.** Performance Tree tab under Stack Tree panel ❌
- **B.** Execution Tree tab under Stack Tree panel ❌
- **C.** Timeline tab under Execution Overview panel ✅
- **D.** Save Order tab under Execution Overview panel ❌

**📝 Dịch tiếng Việt:**
> Trong trình giám sát log (Log Inspector) của Developer Console, lập trình viên có thể xác định thời gian thực thi cụ thể của từng tiến trình trong transaction ở tab nào?

**💬 Giải thích gốc (English):**
> The Timeline tab provides a visual representation of the time taken by each process. Select the Scale option that results in the most useful view.

**✅ Tại sao đáp án đúng:**
> Tab Timeline nằm trong bảng điều khiển Execution Overview (C). Tab này cung cấp một biểu đồ dạng thanh trực quan hiển thị chi tiết thời gian chạy và tỷ lệ % tiêu tốn tài nguyên của từng loại tiến trình (Apex, Database, Workflow, Validation) trong transaction.

**❌ Tại sao đáp án sai:**
> **A.** Performance Tree chỉ hiển thị cây phân cấp cuộc gọi các phương thức, không hiển thị tổng quan dòng thời gian phân bổ tài nguyên.
> **B.** Execution Tree tương tự A, hiển thị sơ đồ phân cấp thực thi hàm.
> **D.** Save Order hiển thị trình tự ghi bản ghi (Save Order of Execution), không hiển thị thời gian chạy thực tế của từng tiến trình.

**💡 Từ khóa ghi nhớ:** `Xem phân bổ dòng thời gian thực thi của các tiến trình trong Developer Console -> Vào tab TIMELINE.`

---

## Câu 240

**🔵 A developer has the controller class below.
Public with sharing class myFooController{
public integer prop{get; private set;}
}
Which code block will run successfully in an execute anonymous window?
A.
myFooController m = new myFooController();
System.assert(m.prop != null);
B.
myFooController m = new myFooController();
System.assert(m.prop == 0);
C.
myFooController m = new myFooController();
System.assert(m.prop == null);
D.
myFooController m = new myFooController();
System.assert(m.prop == 1);**


**📝 Dịch tiếng Việt:**
> Cho class controller sau: [Code myFooController]. Khối lệnh nào dưới đây sẽ chạy thành công không báo lỗi khi thực thi trong cửa sổ Execute Anonymous?

**💬 Giải thích gốc (English):**
> The value of prop variable is never defined in the constructor, so its default value is null.

**✅ Tại sao đáp án đúng:**
> Khối lệnh C: myFooController m = new myFooController(); System.assert(m.prop == null);. Vì thuộc tính 'prop' kiểu Integer không được gán bất kỳ giá trị khởi tạo nào trong class, nên theo quy định mặc định của Apex, nó sẽ tự động nhận giá trị null.

**❌ Tại sao đáp án sai:**
> **A.** Báo lỗi AssertException vì prop đang là null chứ không phải khác null.
> **B.** Báo lỗi assert vì prop là null chứ không phải bằng 0.
> **D.** Báo lỗi assert vì prop là null chứ không phải bằng 1.

**💡 Từ khóa ghi nhớ:** `Mẹo Assert Apex: Thuộc tính không gán trị mặc định -> Luôn assert bằng NULL.`

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
> C: Trace flags ghi đè và có độ ưu tiên cao hơn Logging Levels cấu hình mặc định. D: Nếu không có trace flags nào đang kích hoạt, các bài test Apex sẽ tự động chạy với Logging Levels mặc định của hệ thống. E: Trace flags có thể được thiết lập linh hoạt thông qua Developer Console, mục Setup hệ thống, hoặc sử dụng Tooling API.

**❌ Tại sao đáp án sai:**
> **A.** Chỉ bật trace flags không tự động sinh log nếu không có user action hoặc code thực thi chạy qua đối tượng được cắm cờ.
> **B.** Sai vì Trace flags có mức ưu tiên cao nhất, nó ghi đè chứ không bị ghi đè bởi Logging Levels.

**💡 Từ khóa ghi nhớ:** `Trace Flags -> Thiết lập qua Setup/Dev Console/Tooling API. Bất chấp tất cả, Trace Flags luôn ghi đè Logging Levels!`

---

## Câu 242

**🔵 How can a developer check the test coverage of Autolaunched Flows before deploying them in a change set?**

- **A.** Use the Flow Properties page. ❌
- **B.** Use the ApexTestResult class. ❌
- **C.** Use SOQL and the Tooling API. ✅
- **D.** Use the Code Coverage Setup page. ❌

**📝 Dịch tiếng Việt:**
> Làm sao để biết cái Flow tự động (autolaunched) của mình đã được test bao nhiêu % trước khi mang đi deploy?

**💬 Giải thích gốc (English):**
> Developers can use SOQL queries along with the Tooling API to check the test coverage of autolaunched Flows. The FlowTestCoverage object in the Tooling API provides information about the test coverage for flows.

**✅ Tại sao đáp án đúng:**
> B đúng vì Flow coverage không hiển thị đẹp đẽ trong UI như Apex. Mày phải dùng Tooling API hoặc chạy câu SOQL vào object `FlowTestCoverage` thì mới soi được.

**❌ Tại sao đáp án sai:**
> **A.** Flow Properties chỉ cho thấy mấy cái metadata vớ vẩn như version, status thôi, không có coverage.
> **C.** Cái này dùng để xem kết quả test của code Apex, không chơi được với Flow.
> **D.** Trang này không tồn tại cho Flow.

**💡 Từ khóa ghi nhớ:** `Mẹo PD1: Check Flow Coverage = Tooling API / SOQL.`

---

## Câu 243

**🔵 A developer has the following requirements: Calculate the total amount on an Order. Calculate the line amount for each Line Item based on quantity selected and price. Move Line Items to a different Order if a Line Item is not in stock. Which relationship implementation supports these requirements on its own?**

- **A.** Order has a re-parentable master-detail field to Line Item. ❌
- **B.** Order has a re-parentable lookup field to Line Item. ❌
- **C.** Line Item has a re-parentable lookup field to Order. ❌
- **D.** Line Item has a re-parentable master-detail field to Order. ✅

**📝 Dịch tiếng Việt:**
> Yêu cầu nghiệp vụ: Tính tổng tiền trên Order. Tính tiền cho mỗi Line Item theo số lượng và giá. Cho phép di chuyển Line Items sang Order khác nếu hết hàng. Mối quan hệ nào đáp ứng trọn vẹn các yêu cầu trên?

**💬 Giải thích gốc (English):**
> By default, records can’t be reparented in master-detail relationships. Administrators can, however, allow child records in master-detail relationships on custom objects to be reparented to different parent records by selecting the Allow reparenting option in the master-detail relationship definition.

**✅ Tại sao đáp án đúng:**
> Đối tượng Line Item chứa một trường Master-Detail trỏ lên Order và được cấu hình cho phép đổi cha ('Allow reparenting' hay re-parentable) (D). Thiết kế này giúp vừa dùng được trường Roll-up Summary để tính tổng tiền no-code lên cha Order, vừa cho phép linh hoạt cập nhật đổi cha cho Line Item khi cần.

**❌ Tại sao đáp án sai:**
> **A.** Đặt trường Master-Detail ở phía Order trỏ xuống Line Item làm đảo ngược cấu trúc cha-con, không thể tạo được quan hệ 1-nhiều chuẩn xác.
> **B.** Đặt quan hệ ở Order tương tự A, sai chiều thiết kế dữ liệu.
> **C.** Dùng quan hệ Lookup (C) sẽ làm mất đi khả năng sử dụng trường Roll-up Summary để tự động tính tổng tiền no-code từ con lên cha.

**💡 Từ khóa ghi nhớ:** `Tính tổng con lên cha + Cho phép đổi cha -> Dùng MASTER-DETAIL ở phía con trỏ lên cha + Bật 'Allow reparenting'.`

---

## Câu 244

**🔵 AW Computing tracks order information in custom objects called Order__c and Order_Line__c. Currently, all shipping information is stored in the Order__c object. The company wants to expand its order application to support split shipments so that any number of Order_Line__c records on a single Order__c can be shipped to different locations. What should a developer add to fulfill this requirement?**

- **A.** Order_Shipment_Group__c object and master-detail field on Order__c ❌
- **B.** Order_Shipment_Group__c object and master-detail fields to Order__c and Order_Line__c ✅
- **C.** Order_Shipment_Group__c object and master-detail field on Order_Line__c ❌
- **D.** Order_Shipment_Group__c object and master-detail field on Order_Shipment_Group__c ❌

**📝 Dịch tiếng Việt:**
> Thiết kế object để hỗ trợ split shipment (giao hàng chia nhỏ)?

**✅ Tại sao đáp án đúng:**
> Thêm Group object và trỏ từ Line Item về Group đó.

**❌ Tại sao đáp án sai:**
> **A.** Trỏ từ Order về Group thì cả đơn hàng vẫn đi chung 1 chỗ.
> **C.** Sai quan hệ logic, Master-Detail chỉ nên trỏ về 1 phía.
> **D.** Tự trỏ về chính mình không giải quyết được bài toán liên kết dữ liệu đơn hàng.

**💡 Từ khóa ghi nhớ:** `Thiết kế: Cha (Order) -> Con (Group) -> Cháu (Line Items).`

---

## Câu 245

**🔵 Which two Apex data types can be used to reference a Salesforce record ID dynamically? (Choose two.)**

- **A.** ENUM ❌
- **B.** sObject ✅
- **C.** External ID ❌
- **D.** String ✅

**📝 Dịch tiếng Việt:**
> Hai kiểu dữ liệu Apex nào sau đây có thể được sử dụng để tham chiếu linh hoạt và động đến một ID bản ghi Salesforce? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> B: sObject (đối tượng Apex sObject dùng chung đại diện cho mọi bản ghi, truy cập ID qua obj.Id). D: String (chuỗi ký tự lưu mã ID 15/18 ký tự và có thể tự động ép kiểu sang Id cực kỳ linh hoạt).

**❌ Tại sao đáp án sai:**
> **A.** ENUM là kiểu liệt kê tập hợp các hằng số cố định, không thể dùng để đại diện dynamic cho ID bản ghi.
> **C.** External ID là thuộc tính cấu hình của trường dữ liệu trong Database, không phải là một kiểu dữ liệu (data type) độc lập trong ngôn ngữ lập trình Apex.

**💡 Từ khóa ghi nhớ:** `Tham chiếu dynamic ID bản ghi trong code Apex -> Dùng kiểu sObject hoặc String.`

---

## Câu 246

**🔵 A developer is debugging the following code to determine why Accounts are not being created. List<Account> accts = getAccounts(); //getAccounts implemented else where Database.insert(accts, false); How should the code be altered to help debug the issue?**

- **A.** Change the DML statement to insert method. ❌
- **B.** Collect the insert method return value in a SaveResult record. ✅
- **C.** Set the second insert method parameter to TRUE. ❌
- **D.** Add a try/catch around the insert method. ❌

**📝 Dịch tiếng Việt:**
> Developer chạy đoạn code sau: 'Database.insert(accts, false);' và nhận thấy Account không được tạo nhưng hệ thống không báo lỗi gì. Nên thay đổi code thế nào để gỡ lỗi hiệu quả?

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
> Hứng giá trị trả về của phương thức insert vào một mảng đối tượng SaveResult: 'Database.SaveResult[] results = Database.insert(accts, false);' và duyệt qua mảng để in debug thông tin lỗi cụ thể (B). Do tham số allOrNone = false, Salesforce sẽ bỏ qua bản ghi lỗi và chạy tiếp mà không ném ra exception, làm cho khối try/catch hoàn toàn vô dụng.

**❌ Tại sao đáp án sai:**
> **A.** Đổi sang lệnh DML insert thông thường sẽ làm dừng transaction lập tức khi gặp bản ghi lỗi đầu tiên, phá vỡ logic xử lý chấp nhận lỗi một phần của hệ thống.
> **C.** Đặt tham số thứ hai thành TRUE sẽ bắt hệ thống rollback toàn bộ nếu có lỗi, nhưng không giúp lấy chi tiết danh sách lỗi cụ thể của từng bản ghi để debug mượt mà.
> **D.** Bọc khối try/catch vô tác dụng vì hàm Database.insert(list, false) tuyệt đối không bao giờ ném ra Exception khi gặp lỗi dữ liệu bản ghi.

**💡 Từ khóa ghi nhớ:** `Sử dụng Database.insert(list, false) -> Bắt buộc phải hứng và duyệt qua Database.SaveResult[] để kiểm tra lỗi!`

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
> Để tự xây dựng 100% logic nghiệp vụ của riêng mình cho trang và chạy hoàn toàn dưới quyền hệ thống (System Mode), bỏ qua hoàn toàn các chức năng xử lý mặc định của Salesforce (B). (Lưu ý: Đáp án C của đề gốc bị gắn sai đáp án chuẩn, trong thực tế Custom Controller dùng để bypass mặc định Salesforce).

**❌ Tại sao đáp án sai:**
> **A.** Sử dụng custom controller không hề giúp tăng giới hạn governor limits SOQL cứng của transaction.
> **C.** Để tận dụng chức năng có sẵn của Standard Controller, lập trình viên bắt buộc phải dùng Controller Extension chứ không dùng Custom Controller độc lập.
> **D.** Custom Controller mặc định chạy không có chia sẻ (without sharing) bỏ qua sharing rules của user trừ khi khai báo tường minh.

**💡 Từ khóa ghi nhớ:** `Custom Controller -> Tự viết 100% logic, chạy quyền hệ thống (System Mode) và bypass hoàn toàn tính năng mặc định của Salesforce.`

---

## Câu 248

**🔵 Which approach should be used to provide test data for a test class?**

- **A.** Query for existing records in the database. ❌
- **B.** Execute anonymous code blocks that create data. ❌
- **C.** Use a test data factory class to create test data. ✅
- **D.** Access data in @TestVisible class variables. ❌

**📝 Dịch tiếng Việt:**
> Phương pháp chuẩn mực và tốt nhất nào nên được áp dụng để cung cấp dữ liệu test mẫu cho một Apex Test Class?

**💬 Giải thích gốc (English):**
> Using a Test Data Factory or @TestSetup method is generally considered best practice as it ensures tests are isolated, repeatable, and maintainable.

**✅ Tại sao đáp án đúng:**
> Sử dụng một class Test Data Factory chuyên biệt để tạo lập dữ liệu test mẫu (C). Kỹ thuật này giúp tái sử dụng code tạo dữ liệu, giảm thiểu trùng lặp mã nguồn và dễ bảo trì khi Org thay đổi validation rules hay schema trường.

**❌ Tại sao đáp án sai:**
> **A.** Query dữ liệu thật trong DB là tối kỵ vì test class bị cô lập dữ liệu mặc định (SeeAllData=false) sẽ trả về danh sách rỗng.
> **B.** Execute Anonymous chỉ chạy thủ công trên Developer Console, không thể nhúng tự động hóa vào quá trình chạy test của Org được.
> **D.** Khai báo biến tĩnh có gắn @TestVisible chỉ giúp truyền biến, không giúp chèn vật lý các bản ghi test cần thiết vào database.

**💡 Từ khóa ghi nhớ:** `Best Practice tạo dữ liệu test -> Xây dựng class tiện ích chung dạng TEST DATA FACTORY.`

---

## Câu 249

**🔵 A developer created these three roll-up summary fields on the custom object Project__c: - Total_Timesheets__c - Total_Approved_Timesheets__c - Total_Rejected_Timesheet__c The developer is asked to create a new field that shows the ratio between rejected and approved timesheets for a given project. The developer is asked to create a new field that shows the ratio between rejected and approved timesheets for a given project.
What are two benefits of choosing a formula field instead of an Apex trigger to fulfill the request? (Choose two.)**

- **A.** A test class will validate the formula field during deployment. ❌
- **B.** A formula field will trigger existing automation when deployed. ❌
- **C.** Using a formula field reduces maintenance overhead. ✅
- **D.** A formula field will calculate the value retroactively for existing records. ✅

**📝 Dịch tiếng Việt:**
> Developer tạo 3 trường Roll-up Summary trên Project__c để tính tổng số lượng Timesheets theo trạng thái. Yêu cầu tạo thêm trường hiển thị tỷ lệ giữa Timesheets bị từ chối và được duyệt. Hai lợi ích của việc chọn trường công thức (Formula Field) thay vì viết Trigger là gì? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> C: Sử dụng trường công thức giúp loại bỏ hoàn toàn mã nguồn, giảm tải công sức bảo trì và không cần viết test class phủ coverage. D: Trường công thức tự động tính toán giá trị hồi tố (retroactively) cho toàn bộ các bản ghi đã tồn tại từ trước trong hệ thống ngay khi vừa được tạo.

**❌ Tại sao đáp án sai:**
> **A.** Hệ thống không yêu cầu hay thực hiện chạy test class để validate trường công thức khi deploy.
> **B.** Trường công thức không tự động kích hoạt lại các tiến trình tự động hóa (Workflow/Flow) khác khi deploy trường mới.

**💡 Từ khóa ghi nhớ:** `Lợi ích tối thượng của Formula Field -> Không tốn công viết code bảo trì (No-code) + Tự động tính toán dữ liệu lịch sử lịch trình.`

---

## Câu 250

**🔵 A developer needs to update an unrelated object when a record gets saved. Which two trigger types should the developer create? (Choose two.)**

- **A.** after insert ✅
- **B.** before update ❌
- **C.** before insert ❌
- **D.** after update ✅

**📝 Dịch tiếng Việt:**
> Developer cần viết code tự động cập nhật một đối tượng khác không có quan hệ liên quan (unrelated object) mỗi khi một bản ghi được lưu thành công. Lập trình viên nên tạo Trigger ở hai sự kiện nào? (Chọn 2)

**💬 Giải thích gốc (English):**
> To update an unrelated object when a record gets saved, the developer should create the following two trigger types:
> After Insert Trigger: This trigger runs after a new record is inserted into the database. It allows the developer to perform actions on unrelated objects based on the newly inserted record.
> After Update Trigger: This trigger runs after an existing record is updated. It enables the developer to update unrelated objects based on changes to the original record.

**✅ Tại sao đáp án đúng:**
> A: after insert (sau khi chèn mới thành công). D: after update (sau khi cập nhật thành công). Vì đối tượng không liên quan cần thông tin ID và dữ liệu đã được ghi an toàn xuống database ở sự kiện after để tránh lỗi tham chiếu dữ liệu chéo.

**❌ Tại sao đáp án sai:**
> **B.** before update chạy trước khi dữ liệu lưu vào DB, không an toàn và dễ bị rollback gây mất mát đồng bộ dữ liệu.
> **C.** before insert chạy khi bản ghi chưa hề có ID Salesforce thực tế, cấm thực hiện cập nhật chéo đối tượng khác.

**💡 Từ khóa ghi nhớ:** `Cập nhật chéo đối tượng khác không liên quan -> Bắt buộc thực hiện ở sự kiện AFTER (after insert, after update).`

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
> Static Resources (D). Lập trình viên có thể upload file dữ liệu CSV lên Static Resources, sau đó trong test class dùng hàm 'Test.loadData(SObjectType, ResourceName)' để nạp nhanh toàn bộ bản ghi cực kỳ tiện lợi.

**❌ Tại sao đáp án sai:**
> **A.** Documents là nơi lưu trữ tài liệu giao diện Classic, không hỗ trợ tính năng nạp dữ liệu test tự động.
> **B.** WebServiceTests dùng để kiểm thử Web service, không có chức năng nạp dữ liệu mẫu.
> **C.** HttpCalloutMocks dùng để giả lập phản hồi của API cuộc gọi ngoài (callout), không dùng để chèn bản ghi dữ liệu mẫu.

**💡 Từ khóa ghi nhớ:** `Nạp nhanh dữ liệu test giả lập từ file CSV -> Upload lên STATIC RESOURCES + Sử dụng Test.loadData().`

---

## Câu 252

**🔵 An org tracks customer orders on an Order object and the line items of an Order on the Line Item object. The Line Item object has a Master/Detail relationship to the Order object. A developer has a requirement to calculate the order amount on an Order and the line amount on each Line Item based on quantity and price. What is the correct implementation?**

- **A.** Write a single before trigger on the Line Item that calculates the item amount and updates the order amount on the Order. ❌
- **B.** Write a process on the Line Item that calculates the item amount and order amount and updates the fields on the Line Item and the Order. ❌
- **C.** Implement the line amount as a numeric formula field and the order amount as a roll-up summary field. ❌
- **D.** Implement the line amount as a currency field and the order amount as a SUM formula field. ✅

**📝 Dịch tiếng Việt:**
> Một tổ chức theo dõi các đơn hàng của khách hàng trên đối tượng Order và các dòng sản phẩm của Order trên đối tượng Line Item. Đối tượng Line Item có mối quan hệ Master-Detail với đối tượng Order. Một lập trình viên có yêu cầu tính toán số tiền đơn hàng trên Order và số tiền trên mỗi Line Item dựa trên số lượng và giá cả. Triển khai nào sau đây là đúng?

**✅ Tại sao đáp án đúng:**
> Line Item tính giá dựa trên Price * Quantity -> Dùng Formula Field cho khỏe. Order tổng hợp từ Line Items -> Dùng Roll-up Summary (vì là Master-Detail) là chuẩn 'Architect' nhất.

**❌ Tại sao đáp án sai:**
> **A.** Dùng Process Builder cập nhật field thủ công là dư thừa và dễ lỗi race condition.
> **C.** Không có khái niệm 'SUM formula field' để cộng dồn các bản ghi con lên bản ghi cha.
> **D.** Trigger là giải pháp cuối cùng khi No-code không làm được. Ở đây No-code làm quá tốt.

**💡 Từ khóa ghi nhớ:** `Thần chú: Master-Detail + Sum/Min/Max = Roll-up Summary.`

---

## Câu 253

**🔵 A Lightning component has a wired property, searchResults, that stores a list of Opportunities. Which definition of the Apex method, to which the searchResults property is wired, should be used?**

- **A.** @AuraEnabled(cacheable = false) public static List<Opportunity> search(String term) { /*implementation*/ } ❌
- **B.** @AuraEnabled(cacheable = false) public List<Opportunity> search(String term) { /*implementation*/ } ❌
- **C.** @AuraEnabled(cacheable = true) public static List<Opportunity> search(String term) { /*implementation*/ } ✅
- **D.** @AuraEnabled(cacheable = true) public List<Opportunity> search(String term) { /*implementation*/ } ❌

**📝 Dịch tiếng Việt:**
> Cấu trúc Apex method nào đúng để dùng với decorator @wire trong LWC?

**💬 Giải thích gốc (English):**
> To improve runtime performance, annotate the Apex method with @AuraEnabled(cacheable=true), which caches the method results on the client. To set cacheable=true, a method must only get data, it can’t mutate (change) data.
> To use @wire to call an Apex method, you must set cacheable=true.

**✅ Tại sao đáp án đúng:**
> Để dùng `@wire`, method phải có 2 điều kiện: 1. `static` (để gọi từ UI) và 2. `cacheable=true` (để tối ưu hóa lưu kết quả vào bộ nhớ đệm).

**❌ Tại sao đáp án sai:**
> **B.** Thiếu từ khóa `static`, framework sẽ không khởi tạo được class để gọi method.
> **C.** Sai cả `static` lẫn `cacheable`.
> **D.** Thiếu `cacheable=true` nên không thể dùng với `@wire` (chỉ dùng được khi gọi thủ công - imperative call).

**💡 Từ khóa ghi nhớ:** `@wire + Apex = static + cacheable=true.`

---

## Câu 254

**🔵 A lead developer creates an Apex interface called Laptop. Consider the following code snippet: public class SilverLaptop{//code implementation} How can a developer use the Laptop interface within the SilverLaptop class?**

- **A.** public class SilverLaptop implements Laptop{} ✅
- **B.** @Extends(class=Laptop) public class SilverLaptop{} ❌
- **C.** public class SilverLaptop extends Laptop{} ❌
- **D.** @Interface(class=Laptop) public class SilverLaptop{} ❌

**📝 Dịch tiếng Việt:**
> Developer định nghĩa một Apex Interface tên là Laptop. Làm thế nào để sử dụng và triển khai interface này trong class SilverLaptop?

**💬 Giải thích gốc (English):**
> In Apex (similar to Java), the implements keyword is used to indicate that a class will implement an interface.
> public class SilverLaptop implements Laptop {
> // code implementation
> }

**✅ Tại sao đáp án đúng:**
> Cú pháp A: public class SilverLaptop implements Laptop{}. Trong Apex, để một class kế thừa và hiện thực hóa các phương thức ký mẫu được khai báo trong một Interface, ta bắt buộc phải sử dụng từ khóa 'implements'.

**❌ Tại sao đáp án sai:**
> **B.** Cú pháp @Extends là chú thích giả, hoàn toàn không tồn tại trong ngôn ngữ Apex.
> **C.** Từ khóa 'extends' chỉ dành riêng cho việc một class kế thừa một class cha khác (kế thừa đơn), dùng cho Interface là sai ngữ pháp.
> **D.** Chú thích @Interface là cú pháp sai lệch, không tồn tại trong Salesforce Apex.

**💡 Từ khóa ghi nhớ:** `Hiện thực hóa Interface -> Bắt buộc dùng từ khóa IMPLEMENTS.`

---

## Câu 255

**🔵 A method is passed a list of generic sObjects as a parameter. What should the developer do to determine which object type (Account, Lead, or Contact, for example) to cast each sObject?**

- **A.** Use the first three characters of the sObject ID to determine the sObject type. ❌
- **B.** Use the getSObjectType method on each generic sObject to retrieve the sObject token. ✅
- **C.** Use the getSObjectName method on the sObject class to get the sObject name. ❌
- **D.** Use a try-catch construct to cast the sObject into one of the three sObject types. ❌

**📝 Dịch tiếng Việt:**
> Một phương thức nhận tham số đầu vào là một danh sách sObject chung chung (List<sObject>). Developer nên làm gì để xác định chính xác kiểu dữ liệu cụ thể (như Account, Lead, hay Contact) của từng bản ghi để thực hiện ép kiểu (cast) dữ liệu an toàn?

**💬 Giải thích gốc (English):**
> To determine the specific object type (e.g., Account, Lead, Contact) of each sObject in a list, the developer can use the getSObjectType method. This method returns the Schema.SObjectType of the sObject, which can then be used to identify the object type.

**✅ Tại sao đáp án đúng:**
> Sử dụng phương thức getSObjectType() trên từng đối tượng sObject thô để lấy về đối tượng Token Schema.SObjectType tương ứng (B). Cách này giúp so khớp chuẩn xác kiểu dữ liệu (ví dụ: obj.getSObjectType() == Account.sObjectType) trước khi tiến hành cast, tránh được lỗi Runtime Exception.

**❌ Tại sao đáp án sai:**
> **A.** Lấy 3 ký tự đầu của ID để phân biệt (ví dụ: 001 là Account, 003 là Contact) tuy chạy được nhưng là bad practice cực kỳ nguy hiểm, không an toàn và không chính thống vì Salesforce cấm hardcode ID prefix.
> **C.** Không tồn tại phương thức getSObjectName() trên lớp sObject chuẩn của Salesforce.
> **D.** Sử dụng try-catch để ép kiểu thử nghiệm mù quáng (blind casting) làm code chạy cực kỳ chậm và gây gánh nặng rất lớn cho CPU.

**💡 Từ khóa ghi nhớ:** `Xác định kiểu đối tượng sObject động trong code Apex -> Luôn dùng hàm getSObjectType()!`

---

## Câu 256

**🔵 What are two use cases for executing Anonymous Apex code? (Choose two.)**

- **A.** To run a batch Apex class to update all Contacts ✅
- **B.** To schedule an Apex class to run periodically ❌
- **C.** To delete 15,000 inactive Accounts in a single transaction after a deployment ✅
- **D.** To add unit test code coverage to an org ❌

**📝 Dịch tiếng Việt:**
> Hai trường hợp nào nên dùng Execute Anonymous Apex? (Chọn 2)

**💬 Giải thích gốc (English):**
> To run a batch Apex class to update all Contacts
> To delete 15,000 inactive Accounts in a single transaction after a deployment
> These use cases are suitable for Anonymous Apex because it allows developers to quickly execute code snippets for tasks such as data manipulation or batch processing without needing to deploy the code to the org.

**✅ Tại sao đáp án đúng:**
> Dùng để kích hoạt các tiến trình chạy một lần hoặc đặt lịch (Schedule) mà không cần viết code lưu vào hệ thống.

**❌ Tại sao đáp án sai:**
> **A.** DML limit là 10,000, xóa 15,000 trong 1 transaction là 'ăn' LimitException ngay.
> **D.** Code chạy trong Anonymous không bao giờ được tính vào Code Coverage.

**💡 Từ khóa ghi nhớ:** `Anonymous Apex: Một đi không trở lại, không tính Coverage.`

---

## Câu 257

**🔵 A Developer wants to get access to the standard price book in the org while writing a test class that covers an OpportunityLineItem trigger. Which method allows access to the price book?**

- **A.** Use Test.getStandardPricebookId() to get the standard price book ID. ✅
- **B.** Use @IsTest(SeeAllData=true) and delete the existing standard price book. ❌
- **C.** Use Test.loadData() and a Static Resource to load a standard price book. ❌
- **D.** Use @TestVisible to allow the test method to see the standard price book. ❌

**📝 Dịch tiếng Việt:**
> Làm thế nào để lấy được ID của Standard Pricebook trong một Unit Test?

**💬 Giải thích gốc (English):**
> To access the standard price book in a test class that covers an OpportunityLineItem trigger, the developer should use the Test.getStandardPricebookId() method. This method retrieves the ID of the standard price book, allowing the test class to reference it.

**✅ Tại sao đáp án đúng:**
> Salesforce cấm query Pricebook thật trong test (trừ SeeAllData). Để lấy ID 'chuẩn' mà không vi phạm, mày dùng method có sẵn: Test.getStandardPricebookId().

**❌ Tại sao đáp án sai:**
> **A.** SeeAllData=true là bad practice, tuyệt đối tránh khi đi thi.
> **B.** @TestVisible chỉ dùng để xem biến private, không giúp mày lấy data từ hệ thống.
> **D.** Standard Pricebook là của hệ thống, mày không thể nạp nó bằng CSV qua Test.loadData().

**💡 Từ khóa ghi nhớ:** `Test + Pricebook -> Test.getStandardPricebookId(). Nhớ nằm lòng!`

---

## Câu 258

**🔵 A development team wants to use a deployment script to automatically deploy to a sandbox during their development cycles. Which two tools can they use to run a script that deploys to a sandbox? (Choose two.)**

- **A.** SFDX CLI ✅
- **B.** Developer Console ❌
- **C.** Change Sets ❌
- **D.** Ant Migration Tool ✅

**📝 Dịch tiếng Việt:**
> Dùng công cụ nào để chạy script tự động deploy lên sandbox? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> A: CLI sinh ra để chạy command line/script. B: VS Code tích hợp cực tốt với CLI để thực thi các lệnh deploy.

**❌ Tại sao đáp án sai:**
> **C.** Change Sets chỉ thao tác bằng tay trên trình duyệt (Point-and-click).
> **D.** Developer Console không có chức năng deploy metadata từ máy local.

**💡 Từ khóa ghi nhớ:** `Keyword: Scripting + Deployment -> CLI / SFDX.`

---

## Câu 259

**🔵 A platform developer at Universal Containers needs to create a custom button for the Account object that, when clicked, will perform a series of calculations and redirect the user to a custom Visualforce page. Which three attributes need to be defined with values in the tag to accomplish this? (Choose three.)**

- **A.** action ✅
- **B.** renderAs ❌
- **C.** standardController ✅
- **D.** readOnly ❌
- **E.** extensions ✅

**📝 Dịch tiếng Việt:**
> Lập trình viên cần tạo một nút bấm tùy chỉnh (custom button) cho đối tượng Account. Khi click, hệ thống thực hiện một loạt các phép tính toán nâng cao rồi redirect user sang một trang Visualforce. Ba thuộc tính nào cần khai báo giá trị trong thẻ <apex:page>? (Chọn 3)

**💬 Giải thích gốc (English):**
> To create a custom button for the Account object that performs calculations and redirects to a custom Visualforce page, the developer needs to define the following three attributes in the <apex:page> tag:
> StandardController: This attribute specifies the standard controller for the Visualforce page, which in this case would be the Account object.
> Action: This attribute defines the action method that performs the calculations before redirecting to the Visualforce page.
> Extensions: This attribute specifies any additional Apex classes that extend the standard controller to include custom logic for the calculations.

**✅ Tại sao đáp án đúng:**
> A: action (chứa phương thức Apex thực hiện tính toán và định hướng chuyển trang). C: standardController (bắt buộc cấu hình là 'Account' để nút bấm hiển thị được trên Page Layout). E: extensions (khai báo lớp Apex Controller Extension chứa logic tính toán).

**❌ Tại sao đáp án sai:**
> **B.** renderAs chỉ dùng để chỉ định xuất trang sang định dạng PDF, không liên quan đến việc tính toán chuyển trang.
> **D.** readOnly dùng để tối ưu hóa trang chế độ đọc dữ liệu (tăng giới hạn SOQL), không hỗ trợ cho thao tác tính toán ghi đè nút bấm nghiệp vụ.

**💡 Từ khóa ghi nhớ:** `Ghi đè action nút bấm chuẩn + tính toán phức tạp -> standardController + extensions + action.`

---

## Câu 260

**🔵 A recursive transaction is initiated by a DML statement creating records for these two objects:     1. Accounts 2. Contacts The Account trigger hits a stack depth of 16. Which statement is true regarding the outcome of the transaction?**

- **A.** The transaction fails and all the changes are rolled back. ❌
- **B.** The transaction succeeds as long as the Contact trigger stack depth is less than 16. ❌
- **C.** The transaction fails only if the Contact trigger stack depth is greater or equal to 16. ✅
- **D.** The transaction succeeds and all changes are committed to the database. ❌

**📝 Dịch tiếng Việt:**
> Một transaction đệ quy được khởi tạo bởi một câu lệnh DML tạo các bản ghi cho hai đối tượng này: Accounts và Contacts. Trigger của Account đạt đến độ sâu stack là 16. Phát biểu nào sau đây là đúng về kết quả của transaction này?

**💬 Giải thích gốc (English):**
> When an Account trigger hits a stack depth of 16, it means that the trigger has recursively called itself 16 times. In Salesforce, the maximum allowed stack depth for recursive triggers is 16. Therefore, the transaction will fail with a “maximum trigger depth exceeded” error.
> To avoid these kind of situation we can use public class static variable. We can solve this issue, you can set a condition on trigger so it will not be called recursively.

**✅ Tại sao đáp án đúng:**
> Giới hạn đệ quy (Stack depth) của Salesforce là 16. Nếu đạt đúng 16 mà không vượt quá, transaction vẫn thành công. Nếu là lần thứ 17, nó mới 'oẳng' (LimitException).

**❌ Tại sao đáp án sai:**
> **A.** Salesforce không bao giờ commit một nửa transaction (Atomic).
> **C.** Chỉ rollback nếu vượt quá 16.
> **D.** Trigger của Contact cũng tính chung vào tổng stack depth của transaction đó.

**💡 Từ khóa ghi nhớ:** `Recursion Limit: 16. Chạm 16 vẫn sống, 17 là 'cook'.`

---

## Câu 261

**🔵 Which exception type cannot be caught?**

- **A.** LimitException ✅
- **B.** NoAccessException ❌
- **C.** A Custom Exception ❌
- **D.** CalloutException ❌

**📝 Dịch tiếng Việt:**
> Loại ngoại lệ (exception) nào KHÔNG THỂ bị bắt (catch) bằng khối try-catch?

**💬 Giải thích gốc (English):**
> LimitException is a type of exception in Salesforce that cannot be caught. Since these limits are enforced to ensure the stability and performance of the Salesforce platform, LimitException cannot be handled using try-catch blocks.

**✅ Tại sao đáp án đúng:**
> LimitException (vượt quá governor limits) là loại lỗi 'chí mạng'. Salesforce không cho phép mày 'catch' nó vì nếu cho phép, mày có thể tiếp tục lách luật dùng thêm tài nguyên, làm hỏng cơ chế đa người dùng (multi-tenant).

**❌ Tại sao đáp án sai:**
> **A.** Lỗi quyền truy cập vẫn có thể bắt được.
> **B.** Custom Exception sinh ra là để được ném và bắt.
> **D.** Callout Exception nổ ra khi web service xịt, bắt được bình thường.

**💡 Từ khóa ghi nhớ:** `Đụng tới 'Limit' là 'Cook', không ai cứu được, kể cả Try-Catch.`

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
> Vì Data Import Wizard hoàn toàn không hỗ trợ import đối tượng Opportunity (C). Đây là giới hạn cứng của Salesforce: Data Import Wizard chỉ hỗ trợ một số đối tượng tiêu chuẩn cơ bản như Accounts, Contacts, Leads, Solutions và Campaign Members, còn các đối tượng khác như Opportunity hay Case bắt buộc phải dùng Data Loader.

**❌ Tại sao đáp án sai:**
> **A.** Data Import Wizard mới là công cụ chạy trực tiếp trên trình duyệt web, còn Data Loader là phần mềm cài đặt độc lập trên máy tính client.
> **B.** Data Import Wizard mới là công cụ hỗ trợ so khớp tự động thông minh hơn khi liên kết Account con-cha.
> **D.** Data Import Wizard hỗ trợ import tối đa lên tới 50,000 bản ghi, thừa sức xử lý con số 500 đơn giản.

**💡 Từ khóa ghi nhớ:** `Giới hạn Data Import Wizard -> Không hỗ trợ Opportunity và Case. Muốn import Opp/Case -> Bắt buộc dùng DATA LOADER.`

---

## Câu 263

**🔵 When importing and exporting data into Salesforce, which two statements are true? (Choose two.)**

- **A.** Bulk API can be used to Import large data volumes in development environments without bypassing the storage limits. ❌
- **B.** Developer and Developer Pro sandboxes have different storage limits. ✅
- **C.** Bulk API can be used to bypass the storage limits when importing large data volumes in development environments. ❌
- **D.** Data import wizard is a client application provided by Salesforce. ✅

**📝 Dịch tiếng Việt:**
> Khi nhập (import) và xuất (export) dữ liệu vào Salesforce, hai phát biểu nào sau đây là đúng? (Chọn 2)

**💬 Giải thích gốc (English):**
> Developer sandboxes have a storage limit of 200 MB for data and 200 MB for files, while Developer Pro sandboxes have a storage limit of 1 GB for data and 1 GB for files.
> The Data Import Wizard is a tool provided by Salesforce that allows users to import data into Salesforce objects through a simple interface.

**✅ Tại sao đáp án đúng:**
> A: Dùng Bulk API giúp xử lý dữ liệu lớn cực nhanh nhưng vẫn phải tuân thủ giới hạn lưu trữ (Storage Limits) của Org. C: Dev Sandbox (200MB) và Dev Pro (1GB) rõ ràng là khác nhau.

**❌ Tại sao đáp án sai:**
> **B.** Không có tool nào giúp bypass được Storage Limits của Org.
> **D.** Import Wizard là web-based tool, Data Loader mới là client application.

**💡 Từ khóa ghi nhớ:** `Data storage: Dev (200MB), Dev Pro (1GB). Nhớ con số này để thi!`

---

## Câu 264

**🔵 Which code should be used to update an existing Visualforce page that uses standard Visualforce components so that the page matches the look and feel of Lightning Experience?**

- **A.** <apex:styleSheet value="({$URLFOR($Resource.slds,’assets/slds.css’)}"> ❌
- **B.** <apex:slds/> ❌
- **C.** <apex:page lightningStyleSheets="true"> ✅
- **D.** <apex:includeLightning/> ❌

**📝 Dịch tiếng Việt:**
> Mã nào giúp trang Visualforce có giao diện giống Lightning Experience một cách nhanh nhất?

**💬 Giải thích gốc (English):**
> To style your Visualforce page to match the Lightning Experience UI when viewed in Lightning Experience or the Salesforce mobile app, set lightningStylesheets="true" in the <apex:page> tag. When the page is viewed in Salesforce Classic, it doesn’t get Lightning Experience styling.
> <apex:page lightningStylesheets="true">

**✅ Tại sao đáp án đúng:**
> Chỉ cần thêm lightningStylesheets='true' vào thẻ <apex:page>. Salesforce sẽ tự động 'đắp' CSS của Lightning vào các thành phần chuẩn của VF cho mày.

**❌ Tại sao đáp án sai:**
> **A.** <apex:slds/> chỉ nạp thư viện CSS, mày phải tự viết class vào từng tag, tốn sức vãi chưởng.
> **B.** Đây là cách thủ công cũ rích để nạp CSS từ Static Resource, không ai làm thế nữa.
> **C.** <apex:includeLightning/> dùng để nhúng LWC/Aura, không liên quan đến việc đổi giao diện cho VF.

**💡 Từ khóa ghi nhớ:** `VF sang Lightning nhanh nhất: lightningStylesheets='true'.`

---

## Câu 265

**🔵 Which three code lines are required to create a Lightning component on a Visualforce page? (Choose three.)**

- **A.** $Lightning.useComponent ❌
- **B.** <apex:slds/> ❌
- **C.** $Lightning.use ✅
- **D.** <apex:includeLightning/> ✅
- **E.** $Lightning.createComponent ✅

**📝 Dịch tiếng Việt:**
> Ba dòng mã nào là cần thiết để tạo một Lightning component trên một trang Visualforce? (Chọn 3)

**✅ Tại sao đáp án đúng:**
> Đây là 'bộ 3 huyền thoại' để nhúng Lightning vào VF: 1. <apex:includeLightning/> để nạp thư viện. 2. $Lightning.use để khai báo app. 3. $Lightning.createComponent để khởi tạo component.

**❌ Tại sao đáp án sai:**
> **C.** slds dùng để nạp CSS của Lightning, không liên quan đến việc khởi tạo component bằng JS.
> **D.** $Lightning.useComponent là cái tên 'pha kè', Salesforce không có phương thức này.

**💡 Từ khóa ghi nhớ:** `Nhúng Lightning vào VF: Include -> Use -> Create. Cứ nhớ thứ tự này là ăn điểm.`

---

## Câu 266

**🔵 A developer is integrating with a legacy on-premise SQL database. What should the developer use to ensure the data being integrated is matched to the right records in Salesforce?**

- **A.** Formula field ❌
- **B.** Lookup field ❌
- **C.** External ID field ✅
- **D.** External Object ❌

**📝 Dịch tiếng Việt:**
> Developer đang thực hiện tích hợp dữ liệu với một hệ thống cơ sở dữ liệu SQL cũ của doanh nghiệp (on-premise). Lập trình viên nên sử dụng cấu hình gì để đảm bảo dữ liệu tích hợp được so khớp và cập nhật chính xác vào các bản ghi tương ứng trong Salesforce?

**💬 Giải thích gốc (English):**
> Use External IDs in Salesforce to match records. External IDs are custom fields that have the “External ID” attribute, which can be used to match records from external systems. This is particularly useful for upsert operations where you need to insert or update records based on an external identifier.

**✅ Tại sao đáp án đúng:**
> Sử dụng trường External ID (Khóa ngoài) (C). Việc cấu hình một trường text trong Salesforce làm External ID giúp lưu trữ mã khóa định danh duy nhất của hệ thống SQL ngoài, cho phép hệ thống tích hợp gọi lệnh Upsert so khớp tự động cực kỳ nhanh chóng.

**❌ Tại sao đáp án sai:**
> **A.** Formula field chỉ hiển thị giá trị dạng đọc tĩnh dựa trên công thức, không thể nhận dữ liệu lưu trữ trực tiếp từ hệ thống ngoài.
> **B.** Lookup field dùng để tạo quan hệ liên kết giữa các bảng dữ liệu trong Salesforce, không hỗ trợ lưu trữ mã đối chiếu ngoài để map.
> **D.** External Object dùng để truy cập xem dữ liệu realtime qua Salesforce Connect, không dùng để map nạp dữ liệu vật lý vào Org.

**💡 Từ khóa ghi nhớ:** `So khớp và đồng bộ dữ liệu với hệ thống ngoài -> Luôn tạo trường EXTERNAL ID!`

---

## Câu 267

**🔵 A developer is asked to create a Visualforce page that displays some Account fields as well as fields configured on the page layout for related Contacts. How should the developer implement this request?**

- **A.** Use the <apex:include> tag. ❌
- **B.** Use the <apex:relatedList> tag. ✅
- **C.** Add a method to the standard controller. ❌
- **D.** Create a controller extension. ❌

**📝 Dịch tiếng Việt:**
> Developer được yêu cầu tạo một trang Visualforce hiển thị một số trường dữ liệu của Account, đồng thời phải hiển thị đầy đủ các trường của danh sách Contact liên quan giống hệt như Page Layout chuẩn. Giải pháp tối ưu nhất là gì?

**💬 Giải thích gốc (English):**
> To create a Visualforce page that displays some Account fields as well as fields configured on the page layout for related Contacts, the developer can follow these steps:
> 1. Use the Standard Controller for Account: This allows the Visualforce page to access the Account data.
> 2. Use <apex:detail> for Account Fields: This component displays the standard detail page for the Account, including fields configured on the page layout.
> 3. Use <apex:relatedList> for Related Contacts: This component displays the related list of Contacts as configured on the Account page layout.

**✅ Tại sao đáp án đúng:**
> Sử dụng thẻ <apex:relatedList list='Contacts' /> (B). Thẻ này là thành phần Visualforce chuẩn cực mạnh, tự động vẽ bảng dữ liệu chứa đầy đủ các trường của danh sách Contact con liên quan theo đúng cấu hình layout mà Admin đã thiết lập trên Account cha mà không cần viết code.

**❌ Tại sao đáp án sai:**
> **A.** <apex:include> dùng để nhúng trực tiếp một trang Visualforce hoàn chỉnh khác vào trang hiện tại, không tự động render được layout related list.
> **C.** Không thể thêm một phương thức vào Standard Controller của hệ thống vì nó là lớp đóng của Salesforce.
> **D.** Viết Controller Extension là giải pháp code cồng kềnh, tốn công query dữ liệu và vẽ bảng HTML thủ công không cần thiết.

**💡 Từ khóa ghi nhớ:** `Hiển thị nhanh danh sách bản ghi con theo đúng Page Layout của Cha -> Dùng thẻ <apex:relatedList>.`

---

## Câu 268

**🔵 While working in a sandbox, an Apex test falls when run in the Test Framework. However, running the Apex test logic in the Execute Anonymous window succeeds with no exceptions or errors. Why did the method fall in the sandbox test framework but succeed in the Developer Console?**

- **A.** The test method is calling an @future method. ❌
- **B.** The test method has a syntax error in the code. ❌
- **C.** The test method does not use System.runAs to execute as a specific user. ❌
- **D.** The test method relies on existing data in the sandbox. ✅

**📝 Dịch tiếng Việt:**
> Trong quá trình chạy kiểm thử, một test class bị báo FAIL trên Test Framework. Tuy nhiên, khi developer copy logic đó và chạy trong cửa sổ Execute Anonymous của Developer Console thì lại SUCCESS không báo lỗi nào. Nguyên nhân tại sao?

**💬 Giải thích gốc (English):**
> In Apex tests, it’s important to create all necessary data within the test itself to ensure it doesn’t depend on existing data in the environment. When you run the code via the Execute Anonymous tool, it can access the existing data in the sandbox, which might not be the case when running the test method

**✅ Tại sao đáp án đúng:**
> Vì phương thức test đang dựa dẫm vào dữ liệu thật có sẵn trong Sandbox (D). Khi chạy qua Test Framework, hệ thống mặc định cô lập hoàn toàn dữ liệu (SeeAllData=false) làm DB trống rỗng dẫn đến crash test. Trong khi Execute Anonymous chạy trên database thật nhìn thấy mọi bản ghi nên chạy qua mượt mà.

**❌ Tại sao đáp án sai:**
> **A.** Lỗi gọi phương thức @future không làm thành công Execute Anonymous nếu logic code bị sai.
> **B.** Nếu có lỗi cú pháp (syntax error), hệ thống sẽ báo lỗi biên dịch ngay lập tức ở cả hai công cụ chứ không cho phép chạy thành công.
> **C.** System.runAs giúp test phân quyền user, không phải lý do chính tạo sự khác biệt dữ liệu giữa hai môi trường.

**💡 Từ khóa ghi nhớ:** `Test FAIL mà Execute Anonymous SUCCESS -> Do test class chưa tự tạo dữ liệu test mà đi dựa dẫm dữ liệu có sẵn trong Org!`

---

## Câu 269

**🔵 A developer has a single custom controller class that works with a Visualforce Wizard to support creating and editing multiple sObjects. The wizard accepts data from user inputs across multiple Visualforce pages and from a parameter on the initial URL. Which three statements are useful inside the unit test to effectively test the custom controller? (Choose three.)**

- **A.** Insert pageRef; ❌
- **B.** String nextPage = controller.save().getUrl(); ✅
- **C.** ApexPages.currentPage().getParameters().put('Input', 'TestValue'); ✅
- **D.** public ExtendedController(ApexPages.StandardController cntrl){} ❌
- **E.** Test.setCurrentPage(pageRef); ✅

**📝 Dịch tiếng Việt:**
> Một trang Visualforce Wizard phức tạp sử dụng duy nhất một custom controller để hỗ trợ tạo và sửa đổi nhiều đối tượng sObjects khác nhau. Wizard nhận dữ liệu từ các input trên nhiều trang độc lập và từ tham số trên URL ban đầu. Ba câu lệnh nào hữu ích khi viết test class cho controller này? (Chọn 3)

**💬 Giải thích gốc (English):**
> Test.setCurrentPage(pageRef);
> This statement sets the current page context to the specified PageReference, which is essential for simulating the Visualforce page environment in your test.
> ApexPages.CurrentPage().getParameters().put(‘input’, ‘TestValue’);
> This statement allows you to set parameters on the current page, which is useful for testing how your controller handles URL parameters.
> String nextPage = controller.save().getUrl();
> This statement captures the URL of the next page after an action method (like save) is called, which helps verify the navigation logic of your controller.

**✅ Tại sao đáp án đúng:**
> B: 'String nextPage = controller.save().getUrl();' để test chuyển trang sau khi lưu. C: 'ApexPages.currentPage().getParameters().put('Input', 'TestValue');' để giả lập truyền tham số URL đầu vào. E: 'Test.setCurrentPage(pageRef);' để thiết lập ngữ cảnh trang chạy test.

**❌ Tại sao đáp án sai:**
> **A.** Cú pháp DML 'Insert pageRef;' là hoàn toàn sai, đối tượng PageReference đại diện URL trang chứ không phải sObject để lưu xuống DB.
> **D.** Khai báo hàm khởi tạo Controller Extension 'public ExtendedController...' là code định nghĩa class, không phải câu lệnh thực thi kiểm thử.

**💡 Từ khóa ghi nhớ:** `Viết test cho Visualforce Controller -> Dùng Test.setCurrentPage() để set trang + getParameters().put() để truyền tham số URL.`

---

## Câu 270

**🔵 Which three Salesforce resources can be accessed from a Lightning web component? (Choose three.)**

- **A.** All external libraries ❌
- **B.** Static resources ✅
- **C.** Third-party web components ❌
- **D.** Content asset files ✅
- **E.** SVG resources ✅

**📝 Dịch tiếng Việt:**
> LWC có thể truy cập trực tiếp 3 loại tài nguyên nào từ Org Salesforce?

**✅ Tại sao đáp án đúng:**
> LWC hỗ trợ import: E: Static Resources (CSS/JS ngoài), C: SVG (biểu tượng) và B: Content Asset files thông qua các module `@salesforce/`.

**❌ Tại sao đáp án sai:**
> **A.** Mày không thể gọi trực tiếp component của bên thứ 3 trừ khi nó đã được nạp dưới dạng LWC hoặc Static Resource.
> **D.** Không phải mọi thư viện ngoài đều truy cập được do chính sách bảo mật CSP của Salesforce.

**💡 Từ khóa ghi nhớ:** `LWC Get Stuff: @salesforce/resourceUrl, @salesforce/contentAssetUrl.`

---

## Câu 271

**🔵 Which two events need to happen when deploying to a production org? (Choose two.)**

- **A.** All Workflow rules must have at least 1% test coverage. ❌
- **B.** All Apex code must have at least 75% test coverage. ✅
- **C.** All triggers must have some test coverage. ✅
- **D.** All Visual Flows must have at least 1% test coverage. ❌

**📝 Dịch tiếng Việt:**
> 2 điều kiện cần khi deploy lên Production?

**💬 Giải thích gốc (English):**
> Code Coverage
> You must have at least 75% of your Apex covered by unit tests to deploy your code to production environments.
> All triggers must have at least one line of test coverage.

**✅ Tại sao đáp án đúng:**
> B: Tổng Org phải đạt 75%. D: Mỗi trigger phải có coverage > 0%.

**❌ Tại sao đáp án sai:**
> **A.** Flow không bắt buộc test coverage.
> **C.** Process Builder cũng không bắt buộc test coverage.

**💡 Từ khóa ghi nhớ:** `Deploy Pro: Toàn Org 75%, Mỗi Trigger > 0%.`

---

## Câu 272

**🔵 Universal Containers recently transitioned from Classic to Lightning Experience. One of its business processes requires certain values from the Opportunity object to be sent via an HTTP REST callout to its external order management system based on a user-initiated action on the Opportunity detail page. Example values are as follows: Name Amount Account. Which two methods should the developer implement to fulfill the business requirement? (Choose two.)**

- **A.** Create a Visualforce page that performs the HTTP REST callout, and use a Visualforce quick action to expose the component on the Opportunity detail page. ❌
- **B.** Create a Process Builder on the Opportunity object that executes an Apex immediate action to perform the HTTP REST callout whenever the Opportunity is updated. ❌
- **C.** Create a Lightning component that performs the HTTP REST callout, and use a Lightning Action to expose the component on the Opportunity detail page. ✅
- **D.** Create an after update trigger on the Opportunity object that calls a helper method using @Future(Callout=true) to perform the HTTP REST callout. ✅

**📝 Dịch tiếng Việt:**
> Universal Containers chuyển đổi sang Lightning Experience. Nghiệp vụ yêu cầu: Khi user bấm nút trên trang chi tiết Opportunity, hệ thống phải lấy thông tin Name, Amount gửi REST Callout sang hệ thống OMS ngoài. Hai giải pháp nào lập trình viên nên chọn? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> C: Tạo một Lightning Component thực hiện Callout và bọc vào một Lightning Action (Quick Action) hiển thị trên page chi tiết. D: Tạo một trigger after update Opportunity gọi helper method có gắn @future(callout=true) để gửi API bất đồng bộ sau khi cập nhật trường đánh dấu của user.

**❌ Tại sao đáp án sai:**
> **A.** Visualforce Quick Action là công nghệ cũ cho Classic, không tối ưu cho giao diện Lightning Experience hiện đại.
> **B.** Process Builder không hỗ trợ thực hiện trực tiếp các cuộc gọi REST HTTP callout, bắt buộc phải viết thêm Apex code trung gian cực kỳ cồng kềnh.

**💡 Từ khóa ghi nhớ:** `Gọi API từ giao diện Lightning -> Tạo Lightning Component kết hợp Lightning Quick Action, hoặc Trigger + @future(callout=true).`

---

## Câu 273

**🔵 Which statement describes the execution order when triggers are associated to the same object and event?**

- **A.** Triggers are executed in the order they are modified. ❌
- **B.** Triggers are executed alphabetically by trigger name. ❌
- **C.** Trigger execution order cannot be guaranteed. ✅
- **D.** Triggers are executed in the order they are created. ❌

**📝 Dịch tiếng Việt:**
> Nếu một object mà có cả đống trigger chạy cùng một sự kiện (ví dụ before insert) thì thằng nào chạy trước?

**💬 Giải thích gốc (English):**
> If more than one trigger is defined on an object for the same event, the order of trigger execution isn't guaranteed. For example, if you have two before insert triggers for Case and a new Case record is inserted. The firing order of these two triggers isn’t guaranteed.

**✅ Tại sao đáp án đúng:**
> A đúng vì Salesforce không hứa hẹn gì về thứ tự chạy của trigger trên cùng một object. Đừng có tin vào mấy cái thứ tự alphabet hay ngày tạo, lừa hết đấy.

**❌ Tại sao đáp án sai:**
> **B.** Sai. Modified date chả liên quan gì đến thứ tự thực thi của Salesforce.
> **C.** Sai. Alphabet chỉ là cách sắp xếp trong danh sách thôi, không phải thứ tự chạy.
> **D.** Sai. Created date cũng không đảm bảo được gì.

**💡 Từ khóa ghi nhớ:** `Để quản lý thứ tự -> Chỉ dùng 1 trigger duy nhất cho 1 object (Trigger Framework).`

---

## Câu 274

**🔵 In the Lightning UI, where should a developer look to find information about a Paused Flow Interview?**

- **A.** On the Paused Flow Interviews related list for a given record ❌
- **B.** In the system debug log by filtering on Paused Flow Interview ❌
- **C.** In the Paused Interviews section of the Apex Flex Queue ❌
- **D.** On the Paused Flow Interviews component on the Home page ✅

**📝 Dịch tiếng Việt:**
> Tìm các Flow đang bị tạm dừng (Paused Flow Interview) ở đâu trên giao diện Lightning?

**💬 Giải thích gốc (English):**
> Lightning Experience—Add the Paused Flow Interviews component to the appropriate Home pages. This component is available only for Home pages in the Lightning App Builder. It displays paused interviews that the user has read access to.
> Experience Builder Site—Add the Paused Flows component to a site page. This component is available for most pages in Experience Builder, except ones like login pages and error pages. The component displays paused interviews that the user has read access to.
> Salesforce mobile app—Add the Paused Flows item to the navigation items of any Lightning app.
> Salesforce Classic—Add the Paused Flow Interviews related list to the appropriate home page layouts. This component displays only interviews that the user paused.

**✅ Tại sao đáp án đúng:**
> Salesforce cung cấp một Standard Component tên là 'Paused Flow Interviews'. Admin có thể kéo nó vào trang Home hoặc bất kỳ trang nào để user thấy và tiếp tục công việc.

**❌ Tại sao đáp án sai:**
> **B.** Apex Flex Queue chỉ dành cho Batch Apex, không dành cho Flow.
> **D.** Không có Related List mặc định nào tên như vậy trên mọi record.

**💡 Từ khóa ghi nhớ:** `Paused Flow = Home Page Component.`

---

## Câu 275

**🔵 An Opportunity needs to have an amount rolled up from a custom object that is not in a master-detail relationship. How can this be achieved?**

- **A.** Write a Process Builder that links the custom object to the Opportunity. ❌
- **B.** Use the Streaming API to create real-time roll-up summaries. ❌
- **C.** Write a trigger on the child object and use a red-black tree sorting to sum the amount for all related child objects under the Opportunity. ❌
- **D.** Write a trigger on the child object and use an aggregate function to sum the amount for all related child objects under the Opportunity. ✅

**📝 Dịch tiếng Việt:**
> Làm sao để tính tổng (Roll-up) lên Opportunity khi quan hệ chỉ là Lookup?

**✅ Tại sao đáp án đúng:**
> Lookup không hỗ trợ field Roll-up Summary. Mày phải viết Trigger trên object con, dùng SOQL Aggregate (SUM) để tính toán rồi update ngược lại Opportunity cha bằng code.

**❌ Tại sao đáp án sai:**
> **A.** Streaming API chỉ để hóng data, không dùng để tính toán và lưu trữ dữ liệu.
> **B.** Giải thuật red-black tree cực kỳ phức tạp và không liên quan gì đến việc SUM dữ liệu bản ghi con.
> **D.** Process Builder không hỗ trợ các hàm Aggregate (SUM, AVG) trên danh sách con.

**💡 Từ khóa ghi nhớ:** `No Master-Detail -> Dùng Trigger + Aggregate Query.`

---

## Câu 276

**🔵 How does the Lightning Component framework help developers implement solutions faster?**

- **A.** By providing an Agile process with default steps ❌
- **B.** By providing code review standards and processes ❌
- **C.** By providing device-awareness for mobile and desktops ✅
- **D.** By providing change history and version control ❌

**📝 Dịch tiếng Việt:**
> Khung làm việc (framework) Lightning component giúp lập trình viên triển khai các giải pháp nhanh hơn như thế nào?

**💬 Giải thích gốc (English):**
> The framework is designed to create responsive applications that work seamlessly across different devices, including mobile and desktop1. This means developers can build components once and have them function well on various platforms without additional adjustments.

**✅ Tại sao đáp án đúng:**
> Lightning framework được thiết kế kiểu 'Responsive' ngay từ đầu, tự động tối ưu giao diện cho cả Mobile và Desktop mà không cần dev phải viết nhiều code CSS/JS riêng biệt.

**❌ Tại sao đáp án sai:**
> **A.** Code review là quy trình con người, không phải do framework.
> **C.** Agile là phương pháp quản lý dự án, framework không cung cấp quy trình này.
> **D.** Version control (Git) nằm ngoài phạm vi framework này.

**💡 Từ khóa ghi nhớ:** `Lightning = Mobile First + Component Based.`

---

## Câu 277

**🔵 Which Salesforce feature allows a developer to see when a user last logged in to Salesforce if real-time notification is not required?**

- **A.** Event Monitoring Log ✅
- **B.** Calendar Events ❌
- **C.** Developer Log ❌
- **D.** Asynchronous Data Capture Events ❌

**📝 Dịch tiếng Việt:**
> Xem lịch sử đăng nhập cuối cùng của user mà không cần thông báo tức thời bằng cách nào?

**💬 Giải thích gốc (English):**
> Event Monitoring: One of the many tools that Salesforce provides to help keep your data secure, allowing you to see the granular details of user activity in your organization. We refer to these user activities as events. Unlike Real-Time Events, Event Monitoring doesn’t send real-time notifications. Instead, it stores user activity in a log that you can query.

**✅ Tại sao đáp án đúng:**
> Event Monitoring ghi lại hầu hết các hành vi của người dùng trong hệ thống (Login, Logout, Download báo cáo...). Dữ liệu này được lưu trữ trong các file log để admin/dev tải về phân tích.

**❌ Tại sao đáp án sai:**
> **A.** CDC (Data Capture) dùng để theo dõi sự thay đổi của dữ liệu bản ghi (Insert/Update), không dùng cho hành vi Login.
> **C.** Developer Log chỉ dùng để debug code thực thi trong thời gian ngắn, không phải nhật ký hệ thống lâu dài.
> **D.** Calendar Events là các sự kiện trên lịch công việc, không liên quan đến log đăng nhập.

**💡 Từ khóa ghi nhớ:** `Audit hành vi user -> Event Monitoring.`

---

## Câu 278

**🔵 Which two are best practices when it comes to component and application event handling? (Choose two.)**

- **A.** Reuse the event logic in a component bundle, by putting the logic in the helper. ❌
- **B.** Use component events to communicate actions that should be handled at the application level. ✅
- **C.** Handle low-level events in the event handler and re-fire them as higher-level events. ✅
- **D.** Try to use application events as opposed to component events. ❌

**📝 Dịch tiếng Việt:**
> Hai thực hành tốt nhất (best practices) nào khi thiết kế và xử lý các sự kiện Component Event và Application Event trong lập trình Aura Components? (Chọn 2)

**✅ Tại sao đáp án đúng:**
> A: Gom toàn bộ logic xử lý phức tạp của sự kiện từ file Controller vào lớp Helper của component để tái sử dụng mã nguồn hiệu quả. C: Xử lý các sự kiện cấp thấp (low-level HTML events) trong trình xử lý và bắn lại chúng thành các sự kiện nghiệp vụ cấp cao (higher-level custom events).

**❌ Tại sao đáp án sai:**
> **B.** Sai vì các hành động ở tầm ứng dụng (Application level) bắt buộc phải dùng Application Events, Component Events bị giới hạn trong ranh giới cha-con không thể bắt được.
> **D.** Ngược lại, Salesforce khuyến nghị tối cao nên ưu tiên sử dụng Component Events thay vì Application Events bất cứ khi nào có thể để tăng hiệu năng và tính đóng gói.

**💡 Từ khóa ghi nhớ:** `Aura Event Best Practice -> Gom logic vào lớp HELPER + Chuyển đổi low-level event thành high-level custom event.`

---

## Câu 279

**🔵 From which two locations can a developer determine the overall code coverage for a sandbox? (Choose two.)**

- **A.** The Apex Test Execution page ❌
- **B.** The Test Suite Run panel of the Developer Console ❌
- **C.** The Apex Classes setup page ✅
- **D.** The Tests tab of the Developer Console ✅

**📝 Dịch tiếng Việt:**
> Hai địa điểm chính thống nào trong Salesforce giúp lập trình viên xác định tỷ lệ phủ code kiểm thử tổng thể (overall code coverage) của môi trường Sandbox? (Chọn 2)

**💬 Giải thích gốc (English):**
> After the completed run, check the overall code coverage for your org by navigating to:
> 1. In the Quick Find Search type 'Apex' and click 'Apex Classes'
> 2. Click 'Estimate your organization's code coverage'

**✅ Tại sao đáp án đúng:**
> C: Trang Apex Classes trong Setup (click vào link 'Estimate your organization's code coverage'). D: Tab Tests của trình biên dịch Developer Console (hiển thị bảng tỷ lệ % chi tiết ở góc dưới bên phải).

**❌ Tại sao đáp án sai:**
> **A.** Trang Apex Test Execution chỉ hiển thị trạng thái Pass/Fail của các lượt chạy test cụ thể, không hiển thị tổng lượng phủ sóng code toàn bộ Org.
> **B.** Bảng điều khiển Test Suite Run chỉ hiển thị kết quả gom nhóm bộ test, không hiển thị số liệu overall coverage.

**💡 Từ khóa ghi nhớ:** `Xem tỷ lệ phủ test (Overall Code Coverage) toàn Org -> Vào Setup gõ APEX CLASSES hoặc vào tab TESTS trong Developer Console.`

---

## Câu 280

**🔵 A SSN__c custom field exists on the Candidate__c custom object. The field is used to store each candidate's social security number and is marked as Unique in the schema definition. As part of a data enrichment process, Universal Containers has a CSV file that contains updated data for all candidates in the system. The file contains each Candidate's social security number as a data point. Universal Containers wants to upload this information into Salesforce, while ensuring all data rows are correctly mapped to a candidate in the system. Which technique should the developer implement to streamline the data upload?**

- **A.** Update the SSN__c field definition to mark it as an External Id. ✅
- **B.** Upload the CSV into a custom object related to Candidate__c. ❌
- **C.** Create a before insert trigger to correctly map the records. ❌
- **D.** Create a Process Builder on the Candidate__c object to map the records. ❌

**📝 Dịch tiếng Việt:**
> Candidate__c có trường SSN__c (Social Security Number) là duy nhất. Công ty muốn nạp dữ liệu cập nhật từ file CSV vào hệ thống sao cho các bản ghi CSV tự động khớp với các Candidate có sẵn. Developer nên áp dụng kỹ thuật gì để tối ưu hóa quá trình upload?

**💬 Giải thích gốc (English):**
> Mark the SSN__c field as an External ID on the Candidate__c object. This ensures that the CSV file's SSN values can be used to match and update existing records accurately.

**✅ Tại sao đáp án đúng:**
> Cập nhật định nghĩa trường SSN__c, đánh dấu chọn thuộc tính 'External ID' cho trường này (A). Khi đó, các công cụ nạp dữ liệu như Data Loader sẽ nhận diện trường này làm khóa đối chiếu để so khớp trực tiếp với CSV để tự động cập nhật bản ghi mà không cần Salesforce ID.

**❌ Tại sao đáp án sai:**
> **B.** Tạo đối tượng trung gian phụ gây phình to cấu trúc cơ sở dữ liệu và nhân đôi công sức tích hợp thừa thãi.
> **C.** Viết trigger map dữ liệu là giải pháp code cồng kềnh, làm lãng phí năng lực tính toán của CPU và tốn công bảo trì.
> **D.** Process Builder không hỗ trợ so khớp và cập nhật hàng loạt bản ghi từ tệp tin CSV đầu vào.

**💡 Từ khóa ghi nhớ:** `So khớp nạp dữ liệu tự động từ CSV không cần ID -> Đánh dấu trường unique đó là EXTERNAL ID.`

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
> Tại sao field Account Type không hiển thị trên trang Visualforce?

**💬 Giải thích gốc (English):**
> By default, properties in Apex are private, meaning they can't be accessed directly by the Visualforce page. You need to make the actType property accessible by using the {get; set;} notation.
> public String actType { get; set; }

**✅ Tại sao đáp án đúng:**
> Biến trong Apex muốn ra được Page thì phải có Getter hoặc khai báo `{get; set;}`.

**❌ Tại sao đáp án sai:**
> **B.** Public biến thôi chưa đủ, Visualforce 'đòi' phải có getter cụ thể.
> **C.** `with sharing` chỉ để lọc bản ghi, không liên quan đến việc hiển thị biến.
> **D.** Account.Type vốn dĩ đã là String rồi, không cần convert gì cả.

**💡 Từ khóa ghi nhớ:** `VF + Apex: Get/Set là điều kiện cần và đủ.`

---

## Câu 282

**🔵 A developer wants to store a description of a product that can be entered on separate lines by a user during product setup and later displayed on a Visualforce page for shoppers. Which field type should the developer choose to ensure that the description will be searchable in the custom Apex SOQL queries that are written?**

- **A.** Text Area ✅
- **B.** Text ❌
- **C.** Text Area (Long) ❌
- **D.** Text Area (Rich) ❌

**📝 Dịch tiếng Việt:**
> Developer muốn tạo một trường mô tả sản phẩm cho phép user nhập xuống dòng hiển thị trên Visualforce, đồng thời trường này bắt buộc phải tìm kiếm lọc được bằng mệnh đề WHERE LIKE trong các câu truy vấn SOQL tùy chỉnh. Chọn kiểu trường nào?

**💬 Giải thích gốc (English):**
> Text Area: Lets users enter up to 255 characters that display on separate lines similar to a Description field.

**✅ Tại sao đáp án đúng:**
> Chọn kiểu trường Text Area (A). Trường Text Area cho phép nhập tối đa 255 ký tự hiển thị trên nhiều dòng độc lập, và đặc biệt là nó HỖ TRỢ tìm kiếm bình thường trong các câu SOQL query.

**❌ Tại sao đáp án sai:**
> **B.** Text thường giới hạn hiển thị trên 1 dòng duy nhất, không đáp ứng yêu cầu xuống dòng của người dùng.
> **C.** Text Area (Long) cho phép nhập dữ liệu cực lớn nhưng Salesforce cấm tiệt sử dụng trường text lớn ở mệnh đề lọc WHERE của câu lệnh SOQL.
> **D.** Text Area (Rich) chứa định dạng HTML phức tạp và tương tự câu C, bị Salesforce chặn hoàn toàn khỏi khả năng so khớp lọc WHERE trong SOQL.

**💡 Từ khóa ghi nhớ:** `Vừa xuống được dòng vừa lọc được trong SOQL WHERE -> Bắt buộc dùng kiểu trường TEXT AREA (không dùng Long/Rich).`

---

## Câu 283

**🔵 How should a developer create a new custom exception class?**

- **A.** public class CustomException extends Exception{} ✅
- **B.** CustomException ex = new (CustomException)Exception(); ❌
- **C.** public class CustomException implements Exception{} ❌
- **D.** (Exception)CustomException ex = new Exception(); ❌

**📝 Dịch tiếng Việt:**
> Làm thế nào để lập trình viên tự định nghĩa một custom exception class (lớp ngoại lệ tùy chỉnh) trong Apex?

**💬 Giải thích gốc (English):**
> To create your custom exception class, extend the built-in Exception class and make sure your class name ends with the word Exception, such as “MyException” or “PurchaseException”. All exception classes extend the system-defined base class Exception, and therefore, inherits all common Exception methods.
> This example defines a custom exception called MyException.
> public class MyException extends Exception {}

**✅ Tại sao đáp án đúng:**
> Định nghĩa class kế thừa Exception chuẩn và tên lớp bắt buộc phải kết thúc bằng từ khóa Exception (A): 'public class CustomException extends Exception{}'.

**❌ Tại sao đáp án sai:**
> **B.** Cú pháp ép kiểu ngược ngạo, hoàn toàn sai ngữ pháp cơ bản của ngôn ngữ Apex.
> **C.** Dùng từ khóa 'implements' là sai lệch nghiêm trọng, Exception là lớp cha (Class) chứ không phải Interface để implements.
> **D.** Cú pháp gán biến sai ngữ pháp, gây lỗi biên dịch compiler ngay lập tức.

**💡 Từ khóa ghi nhớ:** `Tạo Custom Exception -> class bắt buộc có đuôi 'Exception' và dùng từ khóa EXTENDS EXCEPTION.`

---

## Câu 284

**🔵 A developer identifies the following triggers on the Expense__c object: deteleExpense, applyDefaultsToExpense, validateExpenseUpdate; The triggers process before delete, before insert, and before update events respectively. Which two techniques should the developer implement to ensure trigger best practices are followed? (Choose two.)**

- **A.** Unify the before insert and before update triggers and use Process Builder for the delete action. ❌
- **B.** Create helper classes to execute the appropriate logic when a record is saved. ✅
- **C.** Maintain all three triggers on the Expense__c object, but move the Apex logic out of the trigger definition. ❌
- **D.** Unify all three triggers in a single trigger on the Expense__c object that includes all events. ✅

**📝 Dịch tiếng Việt:**
> Sửa 3 trigger trên cùng 1 object theo Best Practice?

**✅ Tại sao đáp án đúng:**
> C: Gom thành 1 Trigger duy nhất. B: Dùng Helper Class.

**❌ Tại sao đáp án sai:**
> **A.** Để 3 trigger là vi phạm Best Practice 'One Trigger per Object'.
> **D.** Process Builder không thay thế tốt được logic phức tạp của Delete trigger.

**💡 Từ khóa ghi nhớ:** `Trigger Thần Chú: One Trigger per Object + Logicless Trigger.`

---

## Câu 285

**🔵 Universal Containers has implemented an order management application. Each Order can have one or more Order Line items. The Order Line object is related to the Order via a master-detail relationship. For each Order Line item, the total price is calculated by multiplying the Order Line item price with the quantity ordered. What is the best practice to get the sum of all Order Line item totals on the Order record?**

- **A.** Roll-up summary field ✅
- **B.** Quick action ❌
- **C.** Apex trigger ❌
- **D.** Formula field ❌

**📝 Dịch tiếng Việt:**
> Ứng dụng Order Management có quan hệ Master-Detail giữa Order (Master) và Order Line (Detail). Yêu cầu tính tổng số tiền của toàn bộ các dòng Order Line con và hiển thị lên Order cha. Thực hành tốt nhất là gì?

**✅ Tại sao đáp án đúng:**
> Tạo một trường Roll-up Summary trên đối tượng cha Order thực hiện tính SUM trường tổng tiền của Order Line con (A). Đây là cách tối ưu hoàn hảo hoàn toàn no-code.

**❌ Tại sao đáp án sai:**
> **B.** Quick Action chỉ dùng để mở giao diện hành động nhanh, không có tính năng tính toán cộng dồn cơ sở dữ liệu.
> **C.** Viết trigger Apex tính toán bằng code là giải pháp cồng kềnh, lãng phí CPU limit và tốn công viết code phủ test.
> **D.** Formula field cấm thực hiện hàm tổng hợp (SUM) đi ngược từ con lên cha trong Salesforce.

**💡 Từ khóa ghi nhớ:** `Tính tổng bản ghi con lên cha ở mối quan hệ Master-Detail -> Luôn luôn dùng ROLL-UP SUMMARY.`

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
> A: Log levels có tính kế thừa (cumulative), cấp thấp hơn sẽ bao gồm cả cấp cao hơn (ví dụ FINE bao gồm cả INFO, ERROR). B: Đây là các permission cần thiết để xem log. D: Log levels (ERROR, WARN, INFO...) giúp lọc lượng thông tin ghi ra log.

**❌ Tại sao đáp án sai:**
> **C.** Modify All Data là quyền quá lớn, View All Data là đủ để xem log.
> **E.** Debug log được hệ thống ghi lại dựa trên cấu hình (Debug Levels), không phải điều khiển trực tiếp bằng code.

**💡 Từ khóa ghi nhớ:** `Log Levels: FINEST > FINER > FINE > DEBUG > INFO > WARN > ERROR.`

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
> Trường tùy chỉnh Rating__c kiểu Percent (phần trăm) trên Account được cấu hình độ dài 2 ký tự, không lấy chữ số thập phân. Bản ghi Account chứa giá trị 50% ở trường Rating__c được query lên và xử lý bằng đoạn code Apex sau: [Code acctScore]. Hỏi giá trị của acctScore sau khi chạy xong là bao nhiêu?

**💬 Giải thích gốc (English):**
> With the Percent field defined with 0 decimal places, the value stored in the Rating field is 50, not 0.50. When the code executes, it multiplies 50 by 100, resulting in an acctScore of 5000.

**✅ Tại sao đáp án đúng:**
> Giá trị của acctScore là 5000 (D). Trong Salesforce, các trường Percent được lưu trữ và truy vấn trong code Apex dưới dạng giá trị thực tế không chia cho 100 (tức là 50% thì Rating__c có giá trị là số thực 50 chứ không phải 0.50). Do đó, phép toán 50 * 100 = 5000.

**❌ Tại sao đáp án sai:**
> **A.** Tính toán sai lệch hoàn toàn.
> **B.** Sai vì nghĩ Percent trong code Apex tự động chia cho 100 thành 0.50 để nhân với 100 ra 50.
> **C.** Sai do nhầm lẫn thứ tự tính toán thập phân.

**💡 Từ khóa ghi nhớ:** `Mẹo thi Percent Salesforce: Trong Apex code, trường % được lấy giá trị thô không chia 100 (ví dụ 50% = 50, 75% = 75).`

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
> Các giới hạn governor limits giúp ngăn chặn việc code Apex của một khách thuê gây ảnh hưởng xấu hoặc làm tê liệt hiệu năng của các khách thuê khác chạy chung trên cùng một máy chủ vật lý (C).

**❌ Tại sao đáp án sai:**
> **A.** Apex Sharing chỉ giúp chia sẻ bản ghi bảo mật trong nội bộ một Org (tenant) cụ thể chứ không thể chia sẻ dữ liệu chéo Org giữa các khách thuê độc lập được.
> **B.** Bảo mật cấp Org kiểm soát quyền truy cập của người dùng trong Org đó, không kiểm soát chéo dữ liệu đa khách thuê vật lý.
> **D.** Từ khóa global trên Apex class chỉ hỗ trợ kết nối chéo namespace nội bộ Org chứ không cho phép Org khác truy cập trực tiếp.

**💡 Từ khóa ghi nhớ:** `Bản chất Multi-tenancy -> Governor Limits sinh ra để bảo vệ tài nguyên dùng chung, tránh các Org ảnh hưởng hiệu năng lẫn nhau.`

---

## Câu 289

**🔵 Universal Containers decides to use exclusively declarative development to build out a new Salesforce application. Which three options should be used to build out the database layer for the application? (Choose three.)**

- **A.** Process Builder ❌
- **B.** Roll-up summaries ✅
- **C.** Triggers ❌
- **D.** Relationships ✅
- **E.** Custom objects and fields ✅

**📝 Dịch tiếng Việt:**
> Universal Containers quyết định sử dụng hoàn toàn phát triển dạng khai báo (declarative) để xây dựng ứng dụng mới. Ba tùy chọn nào nên được sử dụng để thiết lập lớp Cơ sở dữ liệu (Database Layer)? (Chọn 3)

**💬 Giải thích gốc (English):**
> Database Layer
> Declarative: Custom Objects, Fields, Relationships, Rollups
> Coding: Apex Triggers

**✅ Tại sao đáp án đúng:**
> B: Roll-up summaries. D: Relationships. E: Custom objects and fields. Đây là các thành phần cấu tạo nên cấu trúc lớp lưu trữ dữ liệu vật lý hoàn toàn no-code trong Salesforce.

**❌ Tại sao đáp án sai:**
> **A.** Process Builder là công cụ tự động hóa xử lý logic (Logic Layer), không phải cấu trúc lưu trữ cơ sở dữ liệu.
> **C.** Triggers là code Apex dùng để xử lý logic, không thuộc lớp khai báo no-code.

**💡 Từ khóa ghi nhớ:** `Database Layer no-code -> Object/Fields, Relationships, Roll-up Summaries.`

---

## Câu 290

**🔵 A developer must implement a CheckPaymentProcessor class that provides check processing payment capabilities that adhere to what is defined for payments in the PaymentProcessor interface.
public interface PaymentProcessor {
void pay(Decimal amount);
}
Which is the correct implementation to use the PaymentProcessor interface class?
A.
public class CheckPaymentProcessor implements PaymentProcessor{
public void pay(Decimal amount);
}
B.
public class CheckPaymentProcessor implements PaymentProcessor{
public void pay(Decimal amount){}
}
C.
public class CheckPaymentProcessor extends PaymentProcessor{
public void pay(Decimal amount){}
}
D.
public class CheckPaymentProcessor extends PaymentProcessor{
public void pay(Decimal amount);
}**


**📝 Dịch tiếng Việt:**
> Lập trình viên cần tạo class CheckPaymentProcessor để thực hiện xử lý thanh toán tuân thủ đúng các phương thức ký mẫu được định nghĩa trong Interface PaymentProcessor: [Interface Code]. Cách viết nào sau đây là đúng cú pháp Apex?

**💬 Giải thích gốc (English):**
> You need to implement the PaymentProcessor interface and provide the required pay method definition.

**✅ Tại sao đáp án đúng:**
> Cú pháp B: public class CheckPaymentProcessor implements PaymentProcessor { public void pay(Decimal amount){} }. Class con bắt buộc dùng từ khóa 'implements' và phải viết phần thân hàm cụ thể chứa cặp dấu ngoặc nhọn {} để hiện thực hóa phương thức.

**❌ Tại sao đáp án sai:**
> **A.** Hàm pay kết thúc bằng dấu chấm phẩy mà không có ngoặc nhọn chỉ được dùng ở định nghĩa Interface, dùng ở class thường sẽ bị lỗi biên dịch.
> **C.** Sử dụng từ khóa 'extends' đối với Interface là hoàn toàn sai cú pháp lập trình.
> **D.** Sai cú pháp vì vừa dùng từ khóa extends vừa thiếu cặp dấu ngoặc nhọn thân hàm.

**💡 Từ khóa ghi nhớ:** `Hiện thực hóa Interface -> Bắt buộc dùng IMPLEMENTS + Viết đầy đủ thân hàm chứa cặp ngoặc nhọn {}.`

---

## Câu 291

**🔵 Universal Containers has a large number of custom applications that were built using a third-party JavaScript framework and exposed using Visualforce pages. The company wants to update these applications to apply styling that resembles the look and feel of Lightning Experience. What should the developer do to fulfill the business request in the quickest and most effective manner?**

- **A.** Set the attribute enableLightning to true in the definition. ❌
- **B.** Enable Available for Lightning Experience, Lightning Communities, and the mobile app on Visualforce pages used by the custom application. ❌
- **C.** Incorporate the Salesforce Lightning Design System CSS stylesheet into the JavaScript applications. ✅
- **D.** Rewrite all Visualforce pages as Lightning components. ❌

**📝 Dịch tiếng Việt:**
> Universal Containers sở hữu một loạt các ứng dụng tùy chỉnh được xây dựng bằng thư viện JavaScript của bên thứ ba nhúng trong trang Visualforce. Công ty muốn cập nhật nhanh nhất giao diện của các app này theo chuẩn giao diện Lightning Experience. Lập trình viên nên làm gì?

**💬 Giải thích gốc (English):**
> With Lightning stylesheets, it’s easy to tweak your existing Visualforce pages so they’ll display with classic styling in Salesforce Classic and Lightning styling in Lightning Experience.
> 1. From Setup, enter Visualforce in the Quick Find box, then select Visualforce Pages.
> 2. Click Edit next to the Visualforce page.
> 3. Add the lightningStylesheets="true" attribute to the initial <apex:page> component in the Visualforce markup.
> <apex:page standardController="Account" lightningStyleSheets="true">

**✅ Tại sao đáp án đúng:**
> Tích hợp trực tiếp file CSS của Salesforce Lightning Design System (SLDS) vào ứng dụng JavaScript của bên thứ ba đó (C). Vì ứng dụng dùng thư viện JS ngoài (như React/Angular) render HTML tùy chỉnh, việc bật tính năng đổi style tự động của Salesforce sẽ vô tác dụng, bắt buộc phải import SLDS CSS để tự áp dụng các class giao diện chuẩn của Salesforce.

**❌ Tại sao đáp án sai:**
> **A.** Không tồn tại thuộc tính enableLightning trong thẻ khai báo Visualforce page.
> **B.** Tùy chọn Available for Lightning chỉ giúp hiển thị trang Visualforce trên menu Lightning chứ không có khả năng tự động đổi CSS của JS framework ngoài.
> **D.** Viết lại toàn bộ trang Visualforce thành Lightning component là giải pháp cực kỳ tốn công sức và thời gian, không đáp ứng yêu cầu 'nhanh nhất'.

**💡 Từ khóa ghi nhớ:** `Đổi giao diện JS App ngoài sang Lightning chuẩn nhanh nhất -> Nhúng bộ CSS Salesforce Lightning Design System (SLDS) vào ứng dụng.`

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
> C: Record-triggered flow (công cụ no-code hiện đại hỗ trợ query bảng tra cứu động). D: Account trigger (code Apex trigger xử lý hoàn hảo khâu query và map dữ liệu).

**❌ Tại sao đáp án sai:**
> **A.** Quick actions chỉ hiển thị nút bấm hành động nhanh trên giao diện để người dùng nhập liệu, không tự động chạy ngầm cập nhật trường chéo bảng được.
> **B.** Approval Process dùng cho quy trình xét duyệt hồ sơ chứng từ, không dùng để tự động cập nhật trường tra cứu chéo bảng khi sửa Postal Code.

**💡 Từ khóa ghi nhớ:** `Tự động cập nhật trường bằng cách truy vấn (query) bảng đối tượng khác -> Chỉ dùng Record-triggered Flow hoặc Apex Trigger.`

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
> A: Thiết lập nhanh các mối quan hệ liên kết (relationships) giữa các bản ghi con-cha khi import từ hệ thống ngoài. D: Làm khóa đối chiếu giúp ngăn chặn việc tạo mới bản ghi trùng lặp khi chạy lệnh nạp dữ liệu Upsert.

**❌ Tại sao đáp án sai:**
> **B.** Salesforce ID do hệ thống tự sinh ngẫu nhiên khi insert và là duy nhất trên từng Org, cấm và không thể ép bản ghi ở Sandbox có chung ID với Production bằng External ID.
> **C.** External ID không dùng để xác định kiểu sObject (Account, Contact) của bản ghi.

**💡 Từ khóa ghi nhớ:** `External ID: Dùng làm khóa ngoài liên kết dữ liệu khi nạp + Làm bộ lọc so khớp độc nhất cho lệnh DML UPSERT tránh trùng.`

---

## Câu 294

**🔵 An Apex method, getAccounts, that returns a List of Accounts given a searchTerm, is available for Lightning Web components to use. What is the correct definition of a Lightning Web component property that uses the getAccounts method?**

- **A.** @wire(getAccounts, { searchTerm: '$searchTerm'})  accountList; ✅
- **B.** @AuraEnabled(getAccounts, '$searchTerm') accountList; ❌
- **C.** @AuraEnabled(getAccounts, { searchTerm: '$searchTerm'}) accountList; ❌
- **D.** @wire(getAccounts, '$searchTerm') accountList; ❌

**📝 Dịch tiếng Việt:**
> Một phương thức Apex, getAccounts, trả về một List các Account dựa trên một search Term, có sẵn để Lightning Web Components sử dụng. Định nghĩa đúng của một thuộc tính (property) Lightning Web Component sử dụng phương thức getAccounts là gì?

**💬 Giải thích gốc (English):**
> To read Salesforce data, Lightning web components use a reactive wire service. Use @wire in a component’s JavaScript class to specify an Apex method. You can @wire a property or a function to receive the data. To operate on the returned data, @wire a function.

**✅ Tại sao đáp án đúng:**
> Cú pháp chuẩn là @wire(FunctionName, { paramName: '$dynamicValue' }). Dấu '$' làm cho tham số trở thành reactive (tự động gọi lại khi giá trị thay đổi).

**❌ Tại sao đáp án sai:**
> **A.** @AuraEnabled là annotation bên phía Apex, không phải decorator trong JS LWC.
> **B.** Sai cú pháp hoàn toàn cho một decorator trong LWC JS.
> **D.** Thiếu cặp ngoặc nhọn { } để truyền tham số dưới dạng một object.

**💡 Từ khóa ghi nhớ:** `LWC @wire: Phải có ngoặc nhọn { } cho tham số và '$' để reactive.`

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
> A: Trường Number của Salesforce được map sang kiểu Decimal trong Apex (để chứa số thập phân an toàn). D: Trường Date/Time được map sang kiểu DateTime trong Apex. E: Trường Checkbox (chỉ có True/False) được ánh xạ sang kiểu Boolean trong Apex.

**❌ Tại sao đáp án sai:**
> **B.** Trường Number có thể chứa phần thập phân, nếu map cứng sang Integer sẽ bị crash lỗi hoặc mất mát dữ liệu số lẻ.
> **C.** Trường TextArea chỉ đơn giản là một String lớn chứa các ký tự xuống dòng, cấm tự động map thành List<String>.

**💡 Từ khóa ghi nhớ:** `Mẹo Ánh Xạ Apex: Checkbox -> Boolean. Date/Time -> DateTime. Number -> Decimal.`

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
> A: Sử dụng cấu trúc Map để lưu kết quả query theo ID, giúp loại bỏ việc gọi SOQL trùng lặp trong các vòng lặp. C: Sử dụng cấu trúc Set để lưu danh sách ID lọc duy nhất, tối ưu hóa bộ lọc WHERE IN trong các câu lệnh truy vấn SOQL.

**❌ Tại sao đáp án sai:**
> **B.** Không dùng @future bừa bãi chỉ để chạy DML update vì phương thức future chạy bất đồng bộ không kiểm soát được thứ tự lưu và dễ gây khóa bản ghi (record locking).
> **D.** Không thể khai báo callout trực tiếp trong trigger (kể cả dùng callout=true), bắt buộc trigger phải gọi qua helper method bất đồng bộ @future(callout=true) để tránh treo transaction.

**💡 Từ khóa ghi nhớ:** `Tối ưu hóa Trigger (Bulkification) -> Luôn sử dụng bộ đôi SET (để lọc duy nhất) và MAP (để lưu cache đối chiếu SOQL).`

---

## Câu 297

**🔵 A developer wants to mark each Account in a List as either Active or Inactive, based on the value in the LastModifiedDate field of each Account being greater than 90 days in the past. Which Apex technique should the developer use?**

- **A.** A for loop, with a switch statement inside ❌
- **B.** A switch statement, with a for loop inside ❌
- **C.** An if-else statement, with a for loop inside ❌
- **D.** A for loop, with an if-else statement inside ✅

**📝 Dịch tiếng Việt:**
> Developer muốn duyệt qua danh sách Account và đánh dấu trạng thái Active hoặc Inactive cho từng bản ghi dựa trên việc trường LastModifiedDate có lớn hơn 90 ngày trước hay không. Kỹ thuật Apex nào là tối ưu?

**💬 Giải thích gốc (English):**
> To mark each Account as Active or Inactive based on the LastModified field value, the developer should use a for loop, with an if/else statement inside. This technique allows the developer to iterate through each account and apply the conditional logic to determine the status based on the 90-day threshold.

**✅ Tại sao đáp án đúng:**
> Sử dụng một vòng lặp for để duyệt qua danh sách Account, và viết một câu lệnh điều kiện if-else ở bên trong thân vòng lặp để so sánh ngày và gán nhãn trạng thái tương ứng cho từng bản ghi (D).

**❌ Tại sao đáp án sai:**
> **A.** Switch statement chỉ dùng để so khớp các giá trị hằng số rời rạc cụ thể, không hỗ trợ so sánh toán tử điều kiện lớn hơn/nhỏ hơn phức tạp của ngày tháng.
> **B.** Đặt switch ngoài for lặp là hoàn toàn sai trình tự logic xử lý danh sách.
> **C.** Đặt if-else ngoài for lặp không thể can thiệp xử lý điều kiện cho từng bản ghi độc lập bên trong danh sách được.

**💡 Từ khóa ghi nhớ:** `Xử lý điều kiện động cho từng phần tử trong List -> Dùng vòng lặp FOR, bọc khối lệnh điều kiện IF - ELSE bên trong.`

---

## Câu 298

**🔵 A developer has identified a method in an Apex class that performs resource intensive actions in memory by iterating over the result set of a SOQL statement on the account. The method also performs a DML statement to save the changes to the database. Which two techniques should the developer implement as a best practice to ensure transaction control and avoid exceeding governor limits? (Choose two.)**

- **A.** Use the @ReadOnly annotation to bypass the number of rows returned by a SOQL. ❌
- **B.** Use partial DML statements to ensure only valid data is committed. ❌
- **C.** Use the System.Limit class to monitor the current CPU governor limit consumption. ✅
- **D.** Use the Database.Savepoint method to enforce database integrity. ✅

**📝 Dịch tiếng Việt:**
> Hai kỹ thuật nào lập trình viên nên thực hiện để đảm bảo kiểm soát transaction và tránh vượt quá governor limits cho một phương thức tốn tài nguyên? (Chọn 2)

**💬 Giải thích gốc (English):**
> The developer should implement the following best practices to ensure transaction control and avoid exceeding governor limits:
> Use the System.Limit class to monitor the current CPU governor limit consumption: This helps keep track of how close the code is to hitting governor limits and can allow for proactive management.
> Use the Database.Savepoint method to enforce database integrity: Savepoints allow the developer to roll back to a certain point in the transaction if necessary, which is critical for maintaining data integrity during complex operations.

**✅ Tại sao đáp án đúng:**
> B: Savepoint cho phép mày rollback dữ liệu về trạng thái trước đó nếu có lỗi xảy ra giữa chừng (Transaction Control). D: Class System.Limit cung cấp các method (như getCpuTime()) để check xem mày sắp 'chạm trần' limit chưa để còn biết đường xử lý.

**❌ Tại sao đáp án sai:**
> **A.** Partial DML (allOrNone=false) giúp lưu những bản ghi đúng, nhưng nó không giúp kiểm soát tổng thể transaction hay tránh limit.
> **C.** @ReadOnly chỉ dùng cho Web Services hoặc JS Remoting, không dùng để bypass limit trong transaction thông thường.

**💡 Từ khóa ghi nhớ:** `Keywords: Transaction Control -> Savepoint; Monitor Limits -> System.Limit class.`

---

## Câu 299

**🔵 What should a developer use to script the deployment and unit test execution as part of continuous integration?**

- **A.** Developer Console ❌
- **B.** Salesforce CLI ✅
- **C.** VS Code ❌
- **D.** Execute Anonymous ❌

**📝 Dịch tiếng Việt:**
> Nên sử dụng gì để lập trình việc deploy và chạy unit test trong CI (Continuous Integration)?

**💬 Giải thích gốc (English):**
> A developer should use Salesforce DX (SFDX) for scripting the deployment and unit test execution as part of continuous integration. Here's how:
> SFDX CLI: Command-line interface tools enable you to script deployment and automate unit tests.
> Continuous Integration Tools: Combine SFDX with CI tools like Jenkins, GitHub Actions, or CircleCI to automate the deployment process and run your tests seamlessly.

**✅ Tại sao đáp án đúng:**
> Salesforce CLI (SFDX) sinh ra để tự động hóa bằng script qua terminal, cực kỳ phù hợp cho Jenkins, GitHub Actions...

**❌ Tại sao đáp án sai:**
> **A.** VS Code là IDE để gõ code bằng tay, không phải công cụ để chạy script tự động trong server CI.
> **B.** Developer Console chỉ chạy được trong trình duyệt, không hỗ trợ lập trình script từ bên ngoài.
> **D.** Execute Anonymous dùng để chạy code Apex, không dùng để deploy metadata hay quản lý vòng đời CI.

**💡 Từ khóa ghi nhớ:** `CI/CD / Scripting -> Salesforce CLI.`

---

## Câu 300

**🔵 What are two ways for a developer to execute tests in an org? (Choose two.)**

- **A.** Tooling API ✅
- **B.** Developer Console ✅
- **C.** Metadata API ❌
- **D.** Bulk API ❌

**📝 Dịch tiếng Việt:**
> Ba cách nào để thực thi Unit Test trong Salesforce?

**💬 Giải thích gốc (English):**
> Run Unit Test Methods
> To verify the functionality of your Apex code, execute unit tests. You can run Apex test methods in the Developer Console, in Setup, in the Salesforce extensions for Visual Studio Code, or using the API.

**✅ Tại sao đáp án đúng:**
> B: Qua giao diện Setup -> Apex Test Execution. D: Dùng Salesforce CLI (SFDX). E: Tooling API là cái mà các tool như VS Code sử dụng để ra lệnh chạy test.

**❌ Tại sao đáp án sai:**
> **A.** Metadata API dùng để deploy/retrieve cấu hình, không phải để chạy logic test.
> **C.** Bulk API dùng để nạp lượng lớn dữ liệu (Data), không liên quan đến việc chạy test.

**💡 Từ khóa ghi nhớ:** `Run Test: Setup, CLI, Tooling API (VS Code).`

---

## Câu 301

**🔵 Which tool allows a developer to send requests to the Salesforce REST APIs and view the responses?**

- **A.** REST resource path URL ❌
- **B.** Workbench REST Explorer ✅
- **C.** Developer Console REST tab ❌
- **D.** Force.com IDE REST Explorer tab ❌

**📝 Dịch tiếng Việt:**
> Công cụ nào cho phép lập trình viên dễ dàng gửi thử nghiệm các yêu cầu REST API đến Salesforce và xem trực tiếp các phản hồi JSON trả về ngay trên giao diện?

**💬 Giải thích gốc (English):**
> Workbench Rest Explorer allows developers to send requests to the Salesforce REST APIs and view the responses, making it an excellent choice for testing and interacting with RESTful services in Salesforce.

**✅ Tại sao đáp án đúng:**
> Workbench REST Explorer (B). Đây là tính năng cực kỳ mạnh mẽ tích hợp trong Workbench giúp lập trình viên test nhanh các API Endpoint của Salesforce (như /services/data/vXX.X/) rất trực quan.

**❌ Tại sao đáp án sai:**
> **A.** REST resource path URL chỉ là chuỗi địa chỉ endpoint tĩnh, không phải công cụ gửi nhận và hiển thị phản hồi API.
> **C.** Developer Console không có tab nào chuyên biệt để test REST API thủ công giống REST Explorer.
> **D.** Force.com IDE là công cụ viết code cổ điển trên Eclipse đã bị khai tử, không chứa REST Explorer chuyên biệt.

**💡 Từ khóa ghi nhớ:** `Test thử nghiệm REST API Salesforce nhanh chóng -> Sử dụng công cụ WORKBENCH REST EXPLORER.`

---

## Câu 302

**🔵 A developer needs to create a baseline set of data (Accounts, Contacts, Products, Assets) for an entire suite of tests allowing them to test independent requirements various types of Salesforce Cases. Which approach can efficiently generate the required data for each unit test?**

- **A.** Create a mock using the Stub API. ❌
- **B.** Use @TestSetup with a void method. ✅
- **C.** Add @IsTest(seeAllData=true) at the start of the unit test class. ❌
- **D.** Create test data before Test.startTest() in the unit test. ❌

**📝 Dịch tiếng Việt:**
> Cách tạo data test hiệu quả nhất cho toàn bộ test suite?

**✅ Tại sao đáp án đúng:**
> Dùng `@testSetup` để tạo data dùng chung 1 lần cho cả class.

**❌ Tại sao đáp án sai:**
> **A.** Bad practice, phụ thuộc data thật và không đảm bảo tính độc lập.
> **B.** Mỗi method đều phải tự tạo data, làm chậm performance và code bị lặp.
> **D.** Stud API dùng để mock logic, không dùng để tạo baseline data kiểu này.

**💡 Từ khóa ghi nhớ:** `Test Data Chìa khóa: @testSetup.`

---

## Câu 303

**🔵 Which three statements are true regarding custom exceptions in Apex? (Choose three.)**

- **A.** A custom exception class must extend the system Exception class. ✅
- **B.** A custom exception class can implement one or many interfaces. ✅
- **C.** A custom exception class cannot contain member variables or methods. ❌
- **D.** A custom exception class name must end with "Exception" ✅
- **E.** A custom exception class can extend other classes besides the Exception class. ❌

**📝 Dịch tiếng Việt:**
> Ba phát biểu nào đúng về ngoại lệ tùy chỉnh (Custom Exception) trong Apex?

**💬 Giải thích gốc (English):**
> To create your custom exception class, extend the built-in Exception class and make sure your class name ends with the word Exception, such as “MyException” or “PurchaseException”. All exception classes extend the system-defined base class Exception, and therefore, inherits all common Exception methods.

**✅ Tại sao đáp án đúng:**
> A: Phải kế thừa lớp `Exception` của hệ thống. D: Tên phải kết thúc bằng 'Exception' để Salesforce nhận dạng. E: Nó là 1 class nên vẫn implement interface bình thường.

**❌ Tại sao đáp án sai:**
> **B.** Nó hoàn toàn có thể chứa biến/method để lưu thêm thông tin lỗi (ví dụ ErrorCode).
> **C.** Apex chỉ cho kế thừa duy nhất 1 class cha, và để làm exception thì bắt buộc phải là class Exception.

**💡 Từ khóa ghi nhớ:** `Custom Exception = extends Exception + Hậu tố 'Exception'.`

---

## Câu 304

**🔵 A developer writes a trigger on the Account object on the before update event that increments a count field. A workflow rule also increments the count field every time that an Account is created or updated. The field update in the workflow rule is configured to not re-evaluate workflow rules. What is the value of the count field if an Account is inserted with an initial value of zero, assuming no other automation logic is implemented on the Account?**

- **A.** 1 ❌
- **B.** 3 ❌
- **C.** 4 ❌
- **D.** 2 ✅

**📝 Dịch tiếng Việt:**
> Tính giá trị trường đếm khi có cả trigger before update và workflow field update (không re-evaluate).

**💬 Giải thích gốc (English):**
> 1. Initial Value: The Account is initially created with a value of 0.
> 2. Trigger: The trigger fires before the update, incrementing the count to 1.
> 3. Workflow Rule: The workflow rule triggers and increments the count to 2.
> Since the workflow rule is configured to not re-evaluate, it will not trigger again after the trigger's update. Therefore, the final value of the count field will be 2.

**✅ Tại sao đáp án đúng:**
> 1. Before Trigger (0+1=1). 2. Lưu (1). 3. Workflow Update (1+1=2). Vì không re-evaluate nên dừng tại đó.

**❌ Tại sao đáp án sai:**
> **A.** Bằng 3 nếu Workflow có re-evaluate, khiến trigger chạy thêm 1 lần nữa.
> **B.** Con số này quá cao, trừ khi có nhiều automation lặp đi lặp lại.
> **C.** Quên tính bước cộng của Workflow.

**💡 Từ khóa ghi nhớ:** `Order of Execution: Trigger Before -> Workflow -> (Nếu re-evaluate) -> Trigger Before/After lần nữa.`

---

## Câu 305

**🔵 For which three items can a trace flag be configured? (Choose three.)**

- **A.** Apex Trigger ✅
- **B.** Apex Class ✅
- **C.** Process Builder ❌
- **D.** User ✅
- **E.** Visualforce ❌

**📝 Dịch tiếng Việt:**
> Trace Flag có thể được cấu hình cho ba mục nào? (Chọn 3)

**💬 Giải thích gốc (English):**
> Set Up Debug Logging
> To activate debug logging for users, Apex classes, and Apex triggers, configure trace flags and debug levels in the Developer Console or in Setup. Each trace flag includes a debug level, start time, end time, and log type. The trace flag’s log type specifies the entity you’re tracing.

**✅ Tại sao đáp án đúng:**
> Trace Flag giúp mày chỉ định Salesforce ghi log cho các thực thể cụ thể. Ba cái phổ biến nhất là: 1. User cụ thể, 2. Một Apex Class nhất định, 3. Một Trigger nhất định.

**❌ Tại sao đáp án sai:**
> **B.** Visualforce không được cấu hình Trace Flag trực tiếp như một thực thể riêng lẻ.
> **D.** Process Builder cũng không nằm trong danh sách thực thể có thể đặt Trace Flag.

**💡 Từ khóa ghi nhớ:** `Trace Flag = Đặt máy quay lén. Đối tượng: Người (User), Khuôn mẫu (Class), hoặc Hành động (Trigger).`

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
> B: Trả về một danh sách các bản ghi (List<sObject>). C: Trả về một bản ghi đơn duy nhất (Single sObject) khi query giới hạn LIMIT 1. D: Trả về một số nguyên (Integer) khi sử dụng hàm đếm COUNT() trực tiếp (ví dụ: Integer cnt = [SELECT COUNT() FROM Account]).

**❌ Tại sao đáp án sai:**
> **A.** SOQL không bao giờ trả về trực tiếp giá trị Boolean.
> **E.** SOQL cấm và không thể trả về trực tiếp kiểu dữ liệu String thô (muốn lấy string phải lấy qua thuộc tính của sObject).

**💡 Từ khóa ghi nhớ:** `Kiểu trả về của SOQL -> 1. List<sObject>; 2. Single sObject; 3. Integer (khi dùng COUNT()).`

---

## Câu 307

**🔵 In which three areas can a Lightning component be used in the Lightning Experience? (Choose three.)**

- **A.** Lightning Report page ❌
- **B.** Lightning Connect page ❌
- **C.** Lightning Record Page ✅
- **D.** Lightning Community Page ✅
- **E.** Lightning Home page ✅

**📝 Dịch tiếng Việt:**
> Ba khu vực/trang nào lập trình viên có thể trực tiếp nhúng và sử dụng Lightning Components trong giao diện Lightning Experience? (Chọn 3)

**✅ Tại sao đáp án đúng:**
> C: Lightning Record Page (Trang chi tiết bản ghi). D: Lightning Community Page (Trang cộng đồng/Experience Cloud). E: Lightning Home page (Trang chủ hệ thống). Đây là các khu vực hỗ trợ kéo thả component bằng App Builder cực kỳ linh hoạt.

**❌ Tại sao đáp án sai:**
> **A.** Lightning Report page là trang báo cáo tiêu chuẩn của hệ thống, cấm nhúng component tự thiết kế bừa bãi.
> **B.** Không tồn tại khái niệm 'Lightning Connect page' để kéo thả nhúng component trực tiếp trên UI.

**💡 Từ khóa ghi nhớ:** `Nhúng LWC trên Lightning UI -> Nhúng tại Record Page, Home Page, hoặc Community (Experience Cloud) Page.`

---

## Câu 308

**🔵 What are three ways for a developer to execute tests in an org?**

- **A.** Tooling API ✅
- **B.** Salesforce DX ✅
- **C.** Metadata API ❌
- **D.** Bulk API ❌
- **E.** Setup Menu ✅

**📝 Dịch tiếng Việt:**
> Ba phương thức/công cụ nào cho phép lập trình viên trực tiếp kích hoạt chạy toàn bộ các lớp test class (execute tests) trong một Salesforce Org? (Chọn 3)

**💬 Giải thích gốc (English):**
> A developer can execute tests in an org using these three ways:
> Tooling API : Allows for powerful interactions with Salesforce metadata, including running tests.
> Setup Menu : Provides a user-friendly interface to run tests directly within the Salesforce setup area.
> Salesforce DX : Offers robust command-line tools to manage and run tests as part of your development workflow.

**✅ Tại sao đáp án đúng:**
> A: Gọi thông qua Tooling API. B: Thực thi lệnh CLI từ bộ công cụ Salesforce DX (SFDX). E: Click chạy trực tiếp trong trang quản trị Setup Menu (Apex Test Execution).

**❌ Tại sao đáp án sai:**
> **C.** Metadata API dùng để deploy/retrieve cấu trúc code và cấu hình Org, không dùng để kích hoạt tiến trình chạy test độc lập.
> **D.** Bulk API dùng để nạp/xử lý hàng triệu bản ghi dữ liệu cực lớn, hoàn toàn không liên quan đến việc chạy test code.

**💡 Từ khóa ghi nhớ:** `Chạy Apex Test -> 1. Setup Menu (Apex Test Execution); 2. CLI Salesforce DX; 3. Tooling API.`

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
> Tập hợp COUNT, SUM, MIN, MAX (A). Đây là 4 hàm toán học duy nhất được Salesforce hỗ trợ để tính toán dồn dữ liệu từ các bản ghi con lên cha trong mối quan hệ Master-Detail.

**❌ Tại sao đáp án sai:**
> **B.** Hàm tính trung bình AVERAGE hoàn toàn không được hỗ trợ trong Roll-up Summary Field của Salesforce.
> **C.** Tập hợp này bị thiếu mất hàm đếm số lượng COUNT rất quan trọng.
> **D.** Chứa hàm AVERAGE sai lệch cấu hình hệ thống.

**💡 Từ khóa ghi nhớ:** `Bốn hàm Roll-up Summary thần thánh -> Luôn ghi nhớ: COUNT, SUM, MIN, MAX (Tuyệt đối không có AVERAGE!).`

---

## Câu 310

**🔵 Which scenario is valid for execution by unit tests?**

- **A.** Set the created of a record using a system method. ✅
- **B.** Generate a Visualforce Pdf with getContentasPdf(). ❌
- **C.** Load data from a remote site with a callout. ❌
- **D.** Execute anonymous Apex as a different user. ❌

**📝 Dịch tiếng Việt:**
> Kịch bản nào sau đây là hợp lệ để thực thi bởi các unit test?

**💬 Giải thích gốc (English):**
> You can create a test record, set its CreatedDate using a system method, and then assert that the value is correct.
> setCreatedDate(recordId, createdDatetime)

**✅ Tại sao đáp án đúng:**
> Trong Unit Test, mày có thể dùng `Test.setCreatedDate(recordId, dateTime)` để giả lập ngày tạo, dù bình thường nó là field read-only.

**❌ Tại sao đáp án sai:**
> **A.** getContentAsPDF() là phương thức bị cấm (bắn exception) trong context của unit test.
> **C.** Thực hiện Callout thật bị cấm trong test, mày bắt buộc phải dùng Mock.
> **D.** Execute Anonymous là một công cụ riêng trong Dev Console, không phải là một phần hợp lệ bên trong Unit Test code.

**💡 Từ khóa ghi nhớ:** `Test: No Callouts (use Mock), Yes Test.setCreatedDate().`

---

## Câu 311

**🔵 Which two conditions cause workflow rules to fire? (Choose two.)**

- **A.** An Apex Batch process that changes field values. ✅
- **B.** Updating records using the bulk API ✅
- **C.** Converting leads to person accounts ❌
- **D.** Changing the territory assignments of accounts and opportunities ❌

**📝 Dịch tiếng Việt:**
> Hai điều kiện nào sau đây sẽ kích hoạt (fire) các quy tắc Workflow Rules hoạt động bình thường? (Chọn 2)

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
> A: Một tiến trình chạy lô Apex Batch thay đổi các giá trị trường. B: Thực hiện cập nhật các bản ghi sử dụng công cụ Bulk API. Cả hai trường hợp này đều thực thi DML update thông thường nên Salesforce sẽ chạy đầy đủ Save Order of Execution bao gồm kích hoạt Workflow Rules.

**❌ Tại sao đáp án sai:**
> **C.** Chuyển đổi lead sang Person Account nằm trong danh sách cấm tự động hóa, Salesforce chặn không kích hoạt Workflow Rule để tránh xung đột vòng lặp dữ liệu.
> **D.** Thay đổi gán Territory của Accounts và Opportunities cũng bị Salesforce loại trừ hoàn toàn khỏi danh sách hành động kích hoạt Workflow Rule.

**💡 Từ khóa ghi nhớ:** `Mẹo thi Workflow: Batch Apex (DML) và Bulk API (DML) -> Vẫn kích hoạt Workflow bình thường. Convert Lead -> Không kích hoạt!`

---

## Câu 312

**🔵 What are three capabilities of the tag when loading JavaScript resources in Aura components? (Choose three.)**

- **A.** One-time loading for duplicate scripts ✅
- **B.** Specifying loading order ✅
- **C.** Loading externally hosted scripts ❌
- **D.** Loading files from Documents ❌
- **E.** Loading scripts in parallel ✅

**📝 Dịch tiếng Việt:**
> Ba khả năng của thẻ <ltng:require> khi tải tài nguyên JavaScript trong Aura component là gì?

**✅ Tại sao đáp án đúng:**
> Thẻ này cực kỳ linh hoạt: A: Có thể tải nhiều script song song để tăng tốc. D: Tự động nhận diện nếu script đã được tải rồi thì không tải lại (tránh trùng). E: Cho phép xác định thứ tự tải (thông qua thuộc tính scripts) để đảm bảo các thư viện phụ thuộc chạy đúng.

**❌ Tại sao đáp án sai:**
> **B.** Aura chỉ tải được từ Static Resources, không tải trực tiếp từ object 'Documents'.
> **C.** Vì lý do bảo mật (CSP), Salesforce không cho phép tải script trực tiếp từ host bên ngoài trừ khi được cấu hình Trusted Site và thường thẻ này ưu tiên Static Resource.

**💡 Từ khóa ghi nhớ:** `ltng:require = Nạp 'đạn' JS từ Static Resource. Nhớ: Song song - Không trùng - Đúng thứ tự.`

---

## Câu 313

**🔵 Which three resources in an Aura component can contain JavaScript functions? (Choose three.)**

- **A.** Helper ✅
- **B.** Design ❌
- **C.** Renderer ✅
- **D.** Style ❌
- **E.** Controller ✅

**📝 Dịch tiếng Việt:**
> Ba tài nguyên nào trong một Aura Component bundle có thể chứa các hàm JavaScript?

**💬 Giải thích gốc (English):**
> The following resources can define and use JavaScript functions in Salesforce Aura components:
> 1. Controller: The controller is in charge of specifying the JavaScript functions that manage the logic and actions of the component. It includes the methods that the component's events or those of other components call. These procedures are listed and associated with the component in the controller's JavaScript file.
> 2. Helper: The helper is a supplemental resource that may be used to add further JavaScript features to assist the operation of the component. It can have reusable functions that are invoked by the component's controller or other helpers and is defined in a separate JavaScript file.
> 3. Renderer: The renderer is yet another optional resource that enables you to change or improve the way a component renders. It can have functions that alter the component's DOM elements, styles, or other visual components during rendering. It is defined in a distinct JavaScript file.

**✅ Tại sao đáp án đúng:**
> Trong Aura Component bundle: Controller.js xử lý sự kiện, Helper.js chứa logic dùng chung, và Renderer.js dùng để ghi đè cách hiển thị mặc định. Cả 3 đều viết bằng JavaScript.

**❌ Tại sao đáp án sai:**
> **D.** Style là file CSS để định dạng giao diện.
> **E.** Design là file XML dùng để cấu hình thuộc tính cho App Builder.

**💡 Từ khóa ghi nhớ:** `Aura JS Trio: Controller - Helper - Renderer. Cứ thế mà quất!`

---

## Câu 314

**🔵 A developer created a Visualforce page and a custom controller with methods to handle different buttons and events that can occur on the page. What should the developer do to deploy to production?**

- **A.** Create a test class that provides coverage of the Visualforce page. ❌
- **B.** Create a test page that provides coverage of the Visualforce page. ❌
- **C.** Create a test page that provides coverage of the custom controller. ❌
- **D.** Create a test class that provides coverage of the custom controller. ✅

**📝 Dịch tiếng Việt:**
> Developer đã tạo một trang Visualforce và một custom controller chứa các hàm xử lý nút bấm nghiệp vụ. Lập trình viên bắt buộc phải làm gì để có thể deploy (triển khai) thành công các thành phần này lên Production?

**💬 Giải thích gốc (English):**
> To ensure the quality and reliability of your Visualforce page and custom controller before deploying to production, it's crucial to write comprehensive unit tests for the custom controller. This will help identify potential issues and bugs early in the development process.
> To deploy it we need code coverage above 75%.

**✅ Tại sao đáp án đúng:**
> Tạo một Test Class kiểm thử bao phủ toàn bộ các dòng mã logic của lớp Custom Controller (D). Đây là điều kiện bắt buộc của Salesforce: mọi Apex Class (bao gồm custom controller) phải có độ phủ code (code coverage) tối thiểu đạt 75% thì mới được phép deploy lên môi trường Production.

**❌ Tại sao đáp án sai:**
> **A.** Visualforce page chỉ là trang thẻ markup giao diện hiển thị, Salesforce tuyệt đối không yêu cầu viết test class cho bản thân trang Visualforce.
> **B.** Không tồn tại khái niệm 'Test Page' để phủ sóng mã nguồn Visualforce.
> **C.** Không thể viết 'Test Page' để đo đạc và phủ sóng logic code trong Apex Custom Controller.

**💡 Từ khóa ghi nhớ:** `Deploy lên Production -> Bắt buộc viết TEST CLASS kiểm thử bao phủ Apex Class đạt tối thiểu 75% code coverage!`

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
> Định nghĩa trường Order Number kiểu Number (hoặc Text) và chọn thuộc tính 'External ID' (C). Vì dữ liệu được import từ hệ thống bên ngoài vào Salesforce, việc cấu hình External ID giúp Salesforce làm khóa đối chiếu để so khớp nạp dữ liệu và liên kết bản ghi chính xác.

**❌ Tại sao đáp án sai:**
> **A.** Direct Lookup không phải là kiểu trường dữ liệu có sẵn trong Salesforce.
> **B.** Lookup field dùng để tạo liên kết quan hệ cha con giữa 2 bảng, không giúp định danh duy nhất bản ghi từ file import ngoài.
> **D.** Indirect Lookup dùng cho đối tượng ngoài (External Object) của Salesforce Connect, không phù hợp cho trường hợp nạp dữ liệu vật lý vào Sandbox.

**💡 Từ khóa ghi nhớ:** `Định danh duy nhất bản ghi import từ hệ thống ngoài -> Luôn cấu hình trường là EXTERNAL ID.`

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
> LastName (Họ) (A). Ở mức cơ sở dữ liệu hệ thống (Database Layer) của Salesforce, trường LastName là trường bắt buộc (required) duy nhất của đối tượng Contact.

**❌ Tại sao đáp án sai:**
> **B.** Trường Name là trường ghép tự động giữa FirstName và LastName trên UI, bản thân nó không tồn tại độc lập để bắt buộc nhập.
> **C.** AccountId (mã liên kết Account cha) là tùy chọn (optional), người dùng có thể tạo một Contact mồ côi không trực thuộc Account nào.
> **D.** FirstName (Tên) là tùy chọn, người dùng hoàn toàn có thể bỏ trống trường này.

**💡 Từ khóa ghi nhớ:** `Trường bắt buộc duy nhất của Contact -> Bắt buộc là LastName!`

---

## Câu 317

**🔵 A developer wrote a unit test to confirm that a custom exception works properly in a custom controller, but the test failed due to an exception being thrown. Which step should the developer take to resolve the issue and properly test the exception?**

- **A.** Use try/catch within the unit test to catch the exception. ✅
- **B.** Use the finally block within the unit test to populate the exception. ❌
- **C.** Use the database methods with all or none set to FALSE. ❌
- **D.** Use Test.isRunningTest() within the custom controller. ❌

**📝 Dịch tiếng Việt:**
> Developer viết một unit test để xác nhận một custom exception (ngoại lệ tùy chỉnh) hoạt động chính xác trong custom controller, nhưng bài test bị báo FAIL do có lỗi exception thực sự bị ném ra. Lập trình viên nên làm gì để giải quyết vấn đề và test exception đúng cách?

**💬 Giải thích gốc (English):**
> By using a try/catch block, the developer can assert that the correct exception type is thrown and that the exception message contains the expected information. This ensures that the custom exception is working as intended and the unit test is reliable.

**✅ Tại sao đáp án đúng:**
> Bọc khối code test trong khối try-catch để chủ động hứng exception bị ném ra trong test class (A). Việc này giúp ngăn chặn exception làm crash luồng chạy của Test Framework, sau đó dùng System.assert để xác thực loại lỗi ném ra là chính xác.

**❌ Tại sao đáp án sai:**
> **B.** Khối finally chỉ chạy dọn dẹp tài nguyên ở cuối, không có khả năng hứng và triệt tiêu lỗi crash của Exception.
> **C.** Sử dụng allOrNone=false của Database method chỉ áp dụng cho DML chèn bản ghi, không giải quyết được việc hứng ngoại lệ tùy chỉnh ném ra từ logic Apex controller.
> **D.** Test.isRunningTest() giúp bỏ qua code khi chạy test, chứ không giúp kiểm tra tính chính xác của logic ném Exception.

**💡 Từ khóa ghi nhớ:** `Kiểm thử ngoại lệ (Test Exception) -> Bắt buộc dùng khối TRY - CATCH trong Test Class để hứng lỗi!`

---

## Câu 318

**🔵 A developer is asked to create a Visualforce page that lists the contacts owned by the current user. This component will be embedded in a Lightning page. Without writing unnecessary code, which controller should be used for this purpose?**

- **A.** Standard controller ❌
- **B.** Custom controller ❌
- **C.** Standard list controller ✅
- **D.** Lightning controller ❌

**📝 Dịch tiếng Việt:**
> Dùng controller nào để hiện list Contact mà không cần viết code Apex?

**💬 Giải thích gốc (English):**
> Standard list controllers allow you to create Visualforce pages that can display or act on a set of records. Examples of existing Salesforce pages that work with a set of records include list pages, related lists, and mass action pages.

**✅ Tại sao đáp án đúng:**
> Standard List Controller hỗ trợ hiện danh sách cực nhanh không tốn 1 dòng code.

**❌ Tại sao đáp án sai:**
> **A.** Lightning controller không phải là thành phần của Visualforce.
> **C.** Bắt buộc phải viết code Apex, trái với yêu cầu 'without unnecessary code'.
> **D.** Chỉ dùng để hiện 1 bản ghi duy nhất, không hiện được list.

**💡 Từ khóa ghi nhớ:** `Keyword: Lists / Without unnecessary code -> Standard List Controller.`

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
> Đoạn code sau được kích hoạt bởi một LWC trong môi trường chứa hơn 2,000 bản ghi Lead: [Code for update in loop]. Giới hạn governor limit nào của Apex transaction sẽ có nguy cơ cao bị vượt quá (exceeded)?

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
> Tổng số câu lệnh DML được thực thi (Total number of DML statements issued) (B). Salesforce giới hạn nghiêm ngặt mỗi transaction chỉ được thực thi tối đa 150 câu lệnh DML. Do câu lệnh 'update thisLead;' bị đặt bên trong thân vòng lặp for chạy 2000 lần, hệ thống sẽ thực hiện DML 2000 lần dẫn đến crash limit tức thì ở lần chạy thứ 151.

**❌ Tại sao đáp án sai:**
> **A.** Hệ thống chỉ thực thi duy nhất 1 câu lệnh SOQL query Lead ở vòng lặp for, hoàn toàn không chạm giới hạn 100 SOQL queries.
> **C.** Giới hạn tổng số bản ghi DML trong transaction là 10,000 bản ghi, con số 2000 vẫn nằm trong tầm an toàn.
> **D.** Giới hạn số bản ghi retrieve từ SOQL là 50,000 bản ghi, con số 2000 vẫn rất nhỏ.

**💡 Từ khóa ghi nhớ:** `Mẹo governor limits: DML nằm trong vòng lặp FOR -> Luôn vượt quá giới hạn DML STATEMENTS (Limit 150 DML)!`

---

## Câu 320

**🔵 How can a developer warn users of SOQL governor limit violations in a trigger?**

- **A.** Use Messaging.SendEmail() to continue the transaction and send an alert to the user after the number of SOQL queries exceeds the limit. ❌
- **B.** Use PageReference.setRedirect() to redirect the user to a custom Visualforce page before the number of SOQL queries exceeds the limit. ❌
- **C.** Use Limits.getQueries() and display an error message before the number of SOQL queries exceeds the limit. ✅
- **D.** Use ApexMessage.Message() to display an error message after the number of SOQL queries exceeds the limit. ❌

**📝 Dịch tiếng Việt:**
> Làm thế nào để lập trình viên chủ động cảnh báo người dùng về việc vi phạm giới hạn governor limits SOQL ngay trong một Apex Trigger?

**💬 Giải thích gốc (English):**
> By checking the current number of SOQL queries using Limits.getQueries(), the trigger can proactively identify potential issues before they lead to a transaction failure.

**✅ Tại sao đáp án đúng:**
> Sử dụng phương thức Limits.getQueries() để theo dõi lượng SOQL đã nổ và chủ động ném ra thông báo lỗi chặn lại trước khi số lượng SOQL vượt quá giới hạn 100 câu truy vấn (C).

**❌ Tại sao đáp án sai:**
> **A.** Khi số lượng SOQL đã thực sự vượt quá giới hạn 100, Salesforce sẽ lập tức rollback transaction và kill tiến trình ngay tức khắc, cấm và không thể gửi email hay thực thi thêm bất cứ dòng code nào sau đó.
> **B.** PageReference.setRedirect() là hàm điều hướng trang của Visualforce Controller, hoàn toàn cấm sử dụng trong môi trường Apex Trigger.
> **D.** ApexPages.Message chỉ dùng hiển thị trên giao diện Visualforce Page, và tương tự câu A, không thể chạy sau khi lỗi LimitException đã nổ ra.

**💡 Từ khóa ghi nhớ:** `Chủ động kiểm soát và ngăn chặn đụng trần SOQL Limits -> Luôn dùng hàm LIMITS.GETQUERIES() để check!`

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
> A: 'for(Account theAccount : AccountList){ }' (Vòng lặp for nâng cao duyệt trực tiếp phần tử). D: 'for(Integer i=0; i < AccountList.Size(); i++){ }' (Vòng lặp for truyền thống duyệt qua chỉ số index).

**❌ Tại sao đáp án sai:**
> **B.** Thiếu biến khai báo phần tử chạy trong vòng lặp, sai cú pháp biên dịch.
> **C.** Khai báo kiểu biến chạy là List L thay vì đối tượng đơn lẻ Account là hoàn toàn sai cú pháp.

**💡 Từ khóa ghi nhớ:** `Duyệt List trong Apex -> Dùng for(Type var : List) hoặc dùng for(Integer i=0; i < List.size(); i++).`

---

## Câu 322

**🔵 A developer created these three Rollup Summary fields in the custom object, Project__c: - Total_Timesheets__c
- Total_Approved_Timesheets__c - Total_Rejected_Timesheets__c The developer is asked to create a new field that shows the ratio between rejected and approved timesheets for a given project. Which should the developer use to implement the business requirement in order to minimize maintenance overhead?**

- **A.** Apex trigger ❌
- **B.** Record-triggered flow ❌
- **C.** Formula field ✅
- **D.** Field Update actions ❌

**📝 Dịch tiếng Việt:**
> Developer đã tạo 3 trường Rollup Summary trên Project__c. Lập trình viên được yêu cầu tạo một trường mới hiển thị tỷ lệ giữa Timesheets bị từ chối và được phê duyệt nhằm giảm thiểu tối đa công sức bảo trì hệ thống. Giải pháp tối ưu là gì?

**💬 Giải thích gốc (English):**
> Formula fields are calculated automatically whenever the related fields (Total_Approved_Timesheets__c and Total_Rejected_Timesheets__c) change. This ensures that the ratio is always up-to-date.
> Formula:
> (Total_Rejected_Timesheets__c / Total_Approved_Timesheets__c)

**✅ Tại sao đáp án đúng:**
> Tạo một trường công thức (Formula Field) (C). Việc sử dụng trường công thức giúp hoàn toàn no-code, tự động tính toán tức thì khi các trường Rollup thay đổi và không cần viết mã nguồn hay kiểm thử bảo trì.

**❌ Tại sao đáp án sai:**
> **A.** Viết trigger Apex tính toán bằng code là giải pháp cồng kềnh, tốn công bảo trì và tốn tài nguyên CPU.
> **B.** Record-triggered Flow cũng là giải pháp tự động hóa phức tạp hơn so với trường công thức tự tính toán đơn giản.
> **D.** Field Update của Workflow rule đời cũ cồng kềnh và đòi hỏi quy tắc kích hoạt phức tạp hơn nhiều.

**💡 Từ khóa ghi nhớ:** `Tính tỷ lệ dựa trên các trường có sẵn no-code -> Giải pháp tốt nhất luôn là FORMULA FIELD.`

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
> A: Cross-object formulas có khả năng tham chiếu đến các trường thuộc các đối tượng cách xa tối đa lên tới 10 mối quan hệ liên kết (10 relationships away). B: Cross-object formulas hỗ trợ tham chiếu trường chéo qua các mối quan hệ Master-Detail hoặc Lookup. D: Cross-object formulas hiển thị giá trị bình thường trên trang dù người dùng không có quyền truy cập trực tiếp (sharing) vào bản ghi cha hoặc trường gốc.

**❌ Tại sao đáp án sai:**
> **C.** Trường công thức chéo đối tượng chỉ hỗ trợ đi ngược lên cha (parent), tuyệt đối cấm và không thể tham chiếu đi xuống danh sách con để thực hiện hàm trung bình AVERAGE.
> **E.** Salesforce cấm không cho phép tham chiếu trường công thức chéo đối tượng làm bộ lọc hoặc giá trị cộng dồn trong các trường Roll-up Summary.

**💡 Từ khóa ghi nhớ:** `Đặc tính Cross-Object Formula -> Tham chiếu tối đa 10 cấp quan hệ đi lên Cha (Lookup/Master-Detail) + Expose được data bỏ qua Sharing User.`

---

## Câu 324

**🔵 A developer working on a time management application wants to make total hours for each timecard available to application users. A timecard entry has a Master Detail relationship to a timecard. Which approach should the developer use to accomplish this declaratively?**

- **A.** A Visualforce page that calculates the total number of hours for a timecard and displays it on the page ❌
- **B.** A Roll-Up Summary field on the Timecard Object that calculates the total hours from timecard entries for that timecard ✅
- **C.** A Process Builder process that updates a field on the timecard when a timecard entry is created ❌
- **D.** An Apex trigger that uses an Aggregate Query to calculate the hours for a given timecard and stores it in a custom field ❌

**📝 Dịch tiếng Việt:**
> Một ứng dụng quản lý thời gian yêu cầu hiển thị tổng số giờ của tất cả các bản ghi Timecard Entry con lên bản ghi Timecard cha. Timecard Entry liên kết với Timecard bằng quan hệ Master-Detail. Lập trình viên nên làm gì để giải quyết yêu cầu hoàn toàn bằng cấu hình khai báo (declarative)?

**💬 Giải thích gốc (English):**
> Roll-up summary fields are a declarative feature that can be configured directly in the object's field definition. The system automatically calculates the total hours whenever a new timecard entry is created, updated, or deleted, ensuring that the value is always up-to-date.

**✅ Tại sao đáp án đúng:**
> Tạo một trường Roll-Up Summary trên đối tượng cha Timecard thực hiện tính SUM số giờ làm của các bản ghi Timecard Entry con (B). Đây là cách giải quyết no-code chuẩn mực và tối ưu hiệu năng tuyệt đối.

**❌ Tại sao đáp án sai:**
> **A.** Sử dụng trang Visualforce đòi hỏi phải viết code và chỉ hiển thị trên trang đó chứ không lưu trữ giá trị vào database để báo cáo.
> **C.** Process Builder không hỗ trợ trực tiếp hàm cộng dồn SUM các bản ghi con ngược lên cha một cách mượt mà.
> **D.** Apex trigger đòi hỏi phải viết code lập trình và viết test class phủ 75%, đi ngược lại yêu cầu giải quyết bằng cấu hình khai báo (declarative).

**💡 Từ khóa ghi nhớ:** `Tính tổng bản ghi con lên cha ở mối quan hệ Master-Detail -> Luôn dùng ROLL-UP SUMMARY.`

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
> Sử dụng một Lightning Component (Aura Component hoặc LWC được bọc trong Aura) (D). Salesforce cho phép ghi đè các hành động chuẩn của đối tượng bằng Lightning Component để tùy biến giao diện và logic chỉnh sửa dữ liệu của người dùng.

**❌ Tại sao đáp án sai:**
> **A.** Lightning action (Quick Action) chỉ là nút bấm thêm hành động nhanh trên UI, không thể dùng để ghi đè nút Edit tiêu chuẩn của hệ thống.
> **B.** Lightning Flow chỉ dùng để chạy luồng quy trình, không thể gán trực tiếp làm component ghi đè nút Edit trong Lightning chuẩn.
> **C.** Lightning Page đại diện cho trang hoàn chỉnh (Home Page/Record Page) chứ không phải linh kiện con có thể dùng để ghi đè nút Edit.

**💡 Từ khóa ghi nhớ:** `Ghi đè nút chuẩn (Override standard button) trong Lightning Experience -> Chỉ dùng LIGHTNING COMPONENT.`

---

## Câu 326

**🔵 A developer needs to allow user to complete a form on an Account record that will create a record for a custom object, The form needs to display different fields depending on the user’s job role. The functionality should only be available to a small group of users. Which three things should the developer do to satisfy these requirements?**

- **A.** Add a dynamic action to the user’s assigned page layouts. ❌
- **B.** Create a light web component. ❌
- **C.** Create a dynamic form. ✅
- **D.** Add a dynamic action to the Account record page. ✅
- **E.** Create a custom permission for the users. ✅

**📝 Dịch tiếng Việt:**
> Yêu cầu: Cho phép user điền form trên Account để tạo bản ghi mới. Form phải hiển thị các trường khác nhau tùy theo vai trò (job role) của user. Tính năng này chỉ hiển thị cho một nhóm nhỏ người dùng đặc biệt. Lập trình viên nên làm ba việc gì để đáp ứng yêu cầu no-code tối ưu nhất? (Chọn 3)

**✅ Tại sao đáp án đúng:**
> C: Tạo một Dynamic Form (để kiểm soát hiển thị trường theo điều kiện vai trò). D: Thêm một Dynamic Action vào trang chi tiết Account record page (để hiển thị nút bấm gọi form dựa trên điều kiện đặc biệt). E: Tạo một Custom Permission dành riêng cho nhóm người dùng đó (để làm điều kiện phân quyền hiển thị nút).

**❌ Tại sao đáp án sai:**
> **A.** Page Layout truyền thống không hỗ trợ cấu hình động hiển thị trường linh hoạt theo vai trò người dùng mượt mà bằng Dynamic Form.
> **B.** Tạo LWC đòi hỏi phải viết code lập trình phức tạp, đi ngược lại xu hướng sử dụng tính năng no-code hiện đại có sẵn của Salesforce.

**💡 Từ khóa ghi nhớ:** `Ẩn hiện trường/nút động theo vai trò & quyền hạn no-code -> Dùng bộ ba DYNAMIC FORM + DYNAMIC ACTION + CUSTOM PERMISSION.`

---

## Câu 327

**🔵 While writing an Apex class, a developer wants to make sure that all functionality being developed is handled as specified by the requirements. Which approach should the developer use to be sure that the Apex class is working according to specifications?**

- **A.** Include a try/catch block to the Apex class. ❌
- **B.** Run the code in an execute Anonymous block in the developer console. ❌
- **C.** Create a test class to execute the business logic and run the test in the developer console. ✅
- **D.** Include a savepoint and Database.rollback(). ❌

**📝 Dịch tiếng Việt:**
> Trong quá trình viết class Apex, lập trình viên muốn đảm bảo toàn bộ các tính năng được phát triển hoạt động chính xác và trơn tru theo đúng tài liệu đặc tả yêu cầu nghiệp vụ. Lập trình viên nên áp dụng phương pháp kiểm thử nào?

**✅ Tại sao đáp án đúng:**
> Xây dựng một lớp kiểm thử (Test Class) chuyên biệt để chạy kiểm tra toàn bộ logic nghiệp vụ và bấm chạy test trực tiếp trong Developer Console hoặc qua Setup (C). Khối kiểm thử sẽ dùng System.assert để xác thực kết quả chạy thực tế trùng khớp với mong đợi.

**❌ Tại sao đáp án sai:**
> **A.** try/catch chỉ giúp bắt ngoại lệ tại runtime để chương trình không bị crash đột ngột, chứ không có tính năng tự động hóa đo đạc độ chính xác của logic nghiệp vụ.
> **B.** Chạy code trong cửa sổ Execute Anonymous là phương pháp test thủ công một lần, không thể tái sử dụng để làm quy trình kiểm thử tự động của hệ thống.
> **D.** Savepoint và rollback dùng để quản lý giao dịch DB (transaction) rollback khi gặp lỗi, không phải công cụ kiểm thử đặc tả.

**💡 Từ khóa ghi nhớ:** `Đảm bảo code Apex chạy đúng theo đặc tả nghiệp vụ -> Xây dựng hệ thống tự động hóa qua TEST CLASS.`

---

## Câu 328

**🔵 What should a developer use to obtain the Id and Name of all the Leads, Accounts, and Contacts that have the company name 'Universal Containers'?**

- **A.** FIND 'Universal Containers' IN CompanyName Fields RETURNING lead{ld,name), account(Id, name), contact(Id, name) ❌
- **B.** FIND 'Universal Containers' IN Name Fields RETURNING lead(id, name), account(Id, name), contact(Id, name) ✅
- **C.** SELECT lead(id, name), account(Id, name), contact(Id, name) FROM Lead, Account, Contact WHERE Name = "universal Containers' ❌
- **D.** SELECT Lead.id. Lead.Name, Account.Id, AccountName, Contacted, Contact.Name FROM Lead, Account, Contact WHERE CompanvName * Universal Containers' ❌

**📝 Dịch tiếng Việt:**
> Developer muốn tìm kiếm và lấy ra Id và Name của tất cả các bản ghi Leads, Accounts, và Contacts có chứa tên công ty 'Universal Containers'. Cú pháp truy vấn nào là đúng?

**💬 Giải thích gốc (English):**
> IN CompanyName" does not exist.
> This query(B) will search for the string "Universal Containers" within the Name field of Lead, Account, and Contact objects and return the specified fields for matching records.

**✅ Tại sao đáp án đúng:**
> Cú pháp SOSL B: FIND 'Universal Containers' IN Name Fields RETURNING lead(id, name), account(Id, name), contact(Id, name). Đây là truy vấn tìm kiếm toàn văn chuẩn của Salesforce, hỗ trợ quét từ khóa trên trường Name và trả về danh sách đối tượng mong muốn.

**❌ Tại sao đáp án sai:**
> **A.** Mệnh đề 'IN CompanyName Fields' là sai cú pháp nghiêm trọng, Salesforce chỉ hỗ trợ các nhóm tìm kiếm chuẩn như Name Fields, All Fields, Email Fields, Phone Fields.
> **C.** Truy vấn SOQL cấm không cho phép khai báo nhiều bảng độc lập ở mệnh đề FROM (FROM Lead, Account, Contact là sai ngữ pháp SOQL hoàn toàn).
> **D.** Tương tự C, SOQL cấm truy vấn kết hợp nhiều bảng độc lập không cùng mối quan hệ trực hệ.

**💡 Từ khóa ghi nhớ:** `SOSL syntax: FIND 'Từ khóa' IN Name Fields RETURNING object1(fields), object2(fields)... (Không bao giờ dùng SOQL FROM nhiều bảng độc lập!).`

---

## Câu 329

**🔵 In a single record, a user selects multiple values from a multi-select picklist. How are the selected values represented in Apex?**

- **A.** As a List<String> with each value as a element in the list. ❌
- **B.** As a String with each value separated by a comma ❌
- **C.** As a String with each value separated by a semicolon ✅
- **D.** As a Set<String> with each value as a element in the set. ❌

**📝 Dịch tiếng Việt:**
> Khi người dùng chọn nhiều giá trị trong một trường Multi-Select Picklist trên giao diện, các giá trị này được lưu trữ và đại diện dưới dạng kiểu dữ liệu gì trong ngôn ngữ Apex?

**💬 Giải thích gốc (English):**
> When a user selects multiple values from a multi-select picklist, the selected values are stored in the database as a single string, with each value separated by a comma.
> For example, if a user selects "Red", "Green", and "Blue" from a multi-select picklist, the value stored in the database would be "Red,Green,Blue".

**✅ Tại sao đáp án đúng:**
> Được đại diện dưới dạng một chuỗi String duy nhất, trong đó các giá trị được phân tách với nhau bằng dấu chấm phẩy (semicolon ';') (C) (ví dụ: 'Red;Green;Blue').

**❌ Tại sao đáp án sai:**
> **A.** Apex không tự động ánh xạ Multi-Select Picklist thành List<String> ở sObject layer.
> **B.** Dấu phẩy ',' không phải là ký tự phân cách chuẩn của Multi-Select Picklist trong Salesforce.
> **D.** Apex không tự động ánh xạ Multi-Select Picklist thành Set<String>.

**💡 Từ khóa ghi nhớ:** `Mẹo thi Multi-Select Picklist: Trong Apex, giá trị luôn được trả về dạng String phân cách bằng DẤU CHẤM PHẨY (;).`

---

## Câu 330

**🔵 What does the Lightning Component framework provide to developers?**

- **A.** Support for Classic and Lightning UIs ❌
- **B.** Templates to create custom components ❌
- **C.** Extended governor limits for applications ❌
- **D.** Prebuilt components that can be reused ✅

**📝 Dịch tiếng Việt:**
> Khung làm việc Lightning Component cung cấp gì cho lập trình viên?

**💬 Giải thích gốc (English):**
> The Lightning Component framework provides a rich set of pre-built components that developers can reuse to quickly build custom applications. These components handle common UI elements like buttons, input fields, modals, and data tables, saving developers time and effort.

**✅ Tại sao đáp án đúng:**
> Salesforce cung cấp sẵn một thư viện đồ sộ các component (Base Lightning Components) để mày lắp ghép, giúp tăng tốc độ phát triển.

**❌ Tại sao đáp án sai:**
> **A.** Lightning component sinh ra cho Lightning Experience, việc hỗ trợ Classic khá hạn chế và không phải là mục tiêu chính của framework.
> **D.** Framework UI không làm thay đổi các giới hạn Governor Limits của hệ thống Apex/Database.

**💡 Từ khóa ghi nhớ:** `Lightning = Có sẵn đống gạch (Prebuilt components) để xây nhà.`

---

## Câu 331

**🔵 What are two benefits of the Lightning Component framework? (Choose two.)**

- **A.** It simplifies complexity when building pages, but not applications. ❌
- **B.** It provides an event-driven architecture for better decoupling between components. ✅
- **C.** It promotes faster development using out-of-box components that are suitable for desktop and mobile devices. ✅
- **D.** It allows faster PDF generation with Lightning components. ❌

**📝 Dịch tiếng Việt:**
> Hai lợi ích nổi bật nhất của kiến trúc lập trình Lightning Component Framework là gì? (Chọn 2)

**💬 Giải thích gốc (English):**
> It provides an event-driven architecture for better decoupling between components.
> This allows for modularity and reusability of components. Components can communicate with each other through events, making the overall application more maintainable and scalable.
> It promotes faster development using out-of-box components that are suitable for desktop and mobile devices.
> The framework provides a wide range of pre-built components that can be customized and used to create responsive user interfaces that adapt to different screen sizes. This accelerates development time and ensures consistency across devices.

**✅ Tại sao đáp án đúng:**
> B: Cung cấp kiến trúc hướng sự kiện (event-driven architecture) giúp tăng tính độc lập (decoupling) và khả năng tái sử dụng giữa các components. C: Thúc đẩy tiến độ phát triển nhanh nhờ kho component chuẩn có sẵn (out-of-box) tự động tương thích tốt trên cả máy tính để bàn (desktop) và thiết bị di động (mobile).

**❌ Tại sao đáp án sai:**
> **A.** Lightning Component đơn giản hóa độ phức tạp cho việc xây dựng cả các trang đơn lẫn toàn bộ hệ thống ứng dụng quy mô lớn.
> **D.** Không có tính năng nào hỗ trợ tăng tốc độ sinh file PDF trong lõi của Lightning component framework.

**💡 Từ khóa ghi nhớ:** `Lợi ích Lightning Framework -> Kiến trúc hướng sự kiện (Event-driven) + Tương thích đa thiết bị di động và desktop (Out-of-box).`

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
> Cho đoạn code cập nhật Contact trong Custom Controller của Visualforce Page: [Code updateContact]. Lập trình viên nên bọc khối lệnh try/catch bằng những điều kiện nào sau đây để kiểm tra quyền hạn cấp đối tượng (object-level permissions) của người dùng hiện tại trước khi thực thi DML? (Chọn 2)

**💬 Giải thích gốc (English):**
> B. Schema.sObjectType.<objectApiName>.isAccessible() checks if the current user has has read access to the specified object.
> D. Use if(Schema.sObjectType.Contact.isUpdateable()) checks if the current user has permission to update on the object.

**✅ Tại sao đáp án đúng:**
> B: 'Schema.sObjectType.Contact.isAccessible()' để kiểm tra xem người dùng hiện tại có quyền Xem (Read) đối tượng Contact hay không. D: 'Schema.sObjectType.Contact.isUpdateable()' để kiểm tra xem người dùng hiện tại có quyền Sửa (Update) đối tượng Contact hay không.

**❌ Tại sao đáp án sai:**
> **A.** So khớp OwnerId chỉ kiểm tra quyền sở hữu bản ghi cụ thể, không kiểm tra quyền phân quyền hệ thống cấp đối tượng (Object-level) của Profile/Permission Set.
> **C.** Schema...fields.Is_Active__c.isUpdateable() dùng để kiểm tra quyền hạn cấp trường (Field-level security - FLS) chứ không phải cấp đối tượng (Object-level) theo yêu cầu đề bài.

**💡 Từ khóa ghi nhớ:** `Kiểm tra quyền hạn cấp Đối tượng (Object-level permission) -> Dùng isAccessible() (Xem) và isUpdateable() (Sửa) trực tiếp trên sObjectType.`

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
> Thực hiện deploy bằng bộ công cụ Ant Migration Tool (hoặc SFDX CLI) chứa một tệp cấu hình xóa 'destructiveChanges.xml' và một tệp 'package.xml' trống không chứa khai báo deploy mới (C).

**❌ Tại sao đáp án sai:**
> **A.** Bộ công cụ Change Sets tiêu chuẩn trên giao diện web hoàn toàn không hỗ trợ tệp destructiveChanges.xml để xóa metadata.
> **B.** Change Sets không có nút chọn nào tên là 'delete option checked' để xóa các thành phần metadata đã triển khai.
> **D.** Nếu khai báo các thành phần cần xóa vào tệp package.xml, hệ thống sẽ cố gắng deploy/update chúng thay vì thực thi lệnh xóa bỏ.

**💡 Từ khóa ghi nhớ:** `Xóa metadata khỏi Production -> Dùng Ant/SFDX CLI với tệp DESTRUCTIVECHANGES.XML đi kèm tệp PACKAGE.XML TRỐNG!`

---

## Câu 334

**🔵 A developer is debugging the following code to determine why Accounts are not being created. Account a = new Account(Name = 'A'); Database.insert(a, false); How should the code be altered to help debug the issue?**

- **A.** Add a System.debug() statement before the insert method. ❌
- **B.** Collect the insert method return value in a SaveResult record. ✅
- **C.** Set the second insert method parameter to TRUE. ❌
- **D.** Add a try/catch around the insert method. ❌

**📝 Dịch tiếng Việt:**
> Làm thế nào để debug lỗi khi dùng Database.insert với tham số allOrNone = false?

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
> Khi dùng 'false', Salesforce sẽ không bắn Exception nếu lỗi. Mày phải hứng kết quả trả về vào object Database.SaveResult, sau đó check sr.isSuccess() để biết nó oẳng hay không và lỗi gì.

**❌ Tại sao đáp án sai:**
> **A.** Đổi thành TRUE sẽ làm transaction dừng ngay khi gặp lỗi, không giúp mày xử lý logic debug chuyên sâu trong code.
> **B.** Vì tham số là 'false' nên code sẽ không bao giờ nhảy vào khối 'catch', vô dụng.
> **C.** System.debug() trước khi insert không giúp mày biết kết quả của việc insert đó thành bại ra sao.

**💡 Từ khóa ghi nhớ:** `Database.insert + false -> Phải đi kèm với SaveResult. Cặp đôi hoàn hảo!`

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
> Developer Edition (D). Đây là quy định cứng của Salesforce: chỉ có môi trường Developer Edition mới hỗ trợ đăng ký Namespace độc quyền và cho phép đóng gói, phát hành Managed Package lên AppExchange.

**❌ Tại sao đáp án sai:**
> **A.** Developer Sandbox chỉ dùng để dev code nội bộ doanh nghiệp, cấm đóng gói Managed Package.
> **B.** Partial Copy Sandbox tương tự A, không hỗ trợ tạo namespace độc quyền để đóng gói phát hành ngoại sàn.
> **C.** Unlimited Edition là môi trường Production thực tế của doanh nghiệp, không hỗ trợ tính năng đóng gói Managed Package.

**💡 Từ khóa ghi nhớ:** `Nơi duy nhất tạo được Managed Package -> Bắt buộc là DEVELOPER EDITION Org!`

---

## Câu 336

**🔵 A Platform Developer needs to implement a declarative solution that will display the most recent Closed Won date for all Opportunity records associated with an Account. Which field is required to achieve this declaratively?**

- **A.** Roll-up summary field on the Opportunity object ❌
- **B.** Cross-object formula field on the Opportunity object ❌
- **C.** Roll-up summary field on the Account object ✅
- **D.** Cross-object formula field on the Account object ❌

**📝 Dịch tiếng Việt:**
> Developer cần hiển thị ngày thắng cơ hội thành công gần nhất ('Closed Won' date) của toàn bộ các Opportunity liên quan lên bản ghi Account cha bằng công cụ no-code. Trường nào cần cấu hình để đạt được điều này?

**💬 Giải thích gốc (English):**
> An opportunity has a lookup field of account. Even though the relationship is a lookup, Salesforce treats certain standard object relationships in a hybrid model i.e. Relationship is Lookup but behaves like Master-Detail
> Also in the backend, there is a relationship property 'cascade delete' between Contact and Account which is always set to True. You will find the same cascade delete Property between objects in a Master-Detail Relationship.
> So for any relationship where the cascade delete is set to True a child record is deleted when the parent is deleted.

**✅ Tại sao đáp án đúng:**
> Tạo trường Roll-up Summary trên đối tượng Account thực hiện hàm MAX trỏ vào trường CloseDate của Opportunity con với điều kiện lọc Stage = 'Closed Won' (C). Do Salesforce hỗ trợ quan hệ đặc biệt giữa Account và Opportunity, ta có thể dùng Roll-up Summary no-code vô cùng tiện lợi.

**❌ Tại sao đáp án sai:**
> **A.** Đặt trường Roll-up Summary ở phía Opportunity con là sai chiều thiết kế cơ sở dữ liệu.
> **B.** Cross-object formula field chỉ hỗ trợ đi từ con tham chiếu lên cha chứ không thể tính toán tổng hợp dồn từ dưới lên cha được.
> **D.** Tương tự B, trường công thức chéo đối tượng trên Account cấm đi xuống Opportunity con để tính toán tổng hợp.

**💡 Từ khóa ghi nhớ:** `Cộng dồn hoặc lấy ngày lớn nhất/nhỏ nhất của bản ghi con lên cha -> Luôn tạo trường ROLL-UP SUMMARY trên đối tượng CHA.`

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
> B: Sử dụng một Validation Rule để chặn lưu dữ liệu khi Stage đã đóng. D: Sử dụng một Apex Trigger before update gọi hàm addError() để chặn lưu dữ liệu.

**❌ Tại sao đáp án sai:**
> **A.** Visual Workflow (Flow) dùng để hướng dẫn người dùng nhập liệu, không có tính năng khóa cứng database ngăn cản sửa đổi từ các công cụ khác như API/Data Loader.
> **C.** Process Automation Settings chứa các cấu hình chung của hệ thống, không có tùy chọn nào hỗ trợ khóa bản ghi Opportunity thông thường khi đổi Stage.

**💡 Từ khóa ghi nhớ:** `Khóa bản ghi ngăn chặn sửa đổi -> Giải pháp tốt nhất luôn là VALIDATION RULE hoặc APEX TRIGGER dùng addError().`

---

## Câu 338

**🔵 A development team wants to use a deployment script to automatically deploy to a sandbox during their development cycles. Which two tools can they use to run a script that deploys to a sandbox? (Choose two.)**

- **A.** SFDX CLI ✅
- **B.** Developer Console ❌
- **C.** Change Sets ❌
- **D.** VSCode ✅

**📝 Dịch tiếng Việt:**
> Dùng công cụ nào để chạy script tự động deploy lên sandbox? (Chọn 2)

**💬 Giải thích gốc (English):**
> SFDX CLI: A powerful command-line tool for automating Salesforce development tasks, including deployments. It allows you to create scripts to deploy metadata changes to sandboxes.
> VSCode: A popular code editor with extensions that can integrate with SFDX. You can use it to write and run deployment scripts, as well as to automate the deployment process using tasks and workflows.

**✅ Tại sao đáp án đúng:**
> A: CLI sinh ra để chạy command line/script. B: VS Code tích hợp cực tốt với CLI để thực thi các lệnh deploy.

**❌ Tại sao đáp án sai:**
> **C.** Change Sets chỉ thao tác bằng tay trên trình duyệt (Point-and-click).
> **D.** Developer Console không có chức năng deploy metadata từ máy local.

**💡 Từ khóa ghi nhớ:** `Keyword: Scripting + Deployment -> CLI / SFDX.`

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
> API Name của trường sẽ không bị thay đổi và hệ thống chặn đứng hành động này để đảm bảo tính an toàn dữ liệu, không gây ra ảnh hưởng nào khác (A). Salesforce cấm sửa tên API Name của trường/object khi nó đang được tham chiếu trong code metadata để tránh lỗi biên dịch.

**❌ Tại sao đáp án sai:**
> **B.** Salesforce không tự động sửa đổi code trong Apex class khi đổi tên trường trên Schema Builder.
> **C.** Hệ thống cấm sửa đổi trực tiếp chứ không cho phép đổi rồi ném ra cảnh báo cập nhật class sau.
> **D.** Không tự động cập nhật được code tham chiếu.

**💡 Từ khóa ghi nhớ:** `Sửa API Name của trường đang có code tham chiếu -> Salesforce CẤM TUYỆT ĐỐI và chặn đứng hành động!`

---

## Câu 340

**🔵 A Next Best Action strategy uses an Enhance Element that invokes an Apex method to determine a discount level for a Contact, based on a number of factors. What is the correct definition of the Apex method?**

- **A.** @InvocableMethod global static List<List<Recommendation>> getLevel(List<ContactWrapper> input) { /*implementation*/ } ✅
- **B.** @InvocableMethod global List<List<Recommendation>> getLevel(List<ContactWrapper> input){ /*implementation*/ } ❌
- **C.** @InvocableMethod global static ListRecommendation getLevel(List<ContactWrapper> input){ /*implementation*/ } ❌
- **D.** @InvocableMethod global Recommendation getLevel(ContactWrapper input){ /*implementation*/ } ❌

**📝 Dịch tiếng Việt:**
> Một chiến lược Next Best Action sử dụng Enhance Element để gọi một Apex method nhằm xác định mức chiết khấu cho Contact. Khai báo nào sau đây của Apex method là đúng quy chuẩn?

**💬 Giải thích gốc (English):**
> Invocable methods are called natively from Rest, Apex, Flow, or Einstein bot that interacts with the external API source. Invocable methods have dynamic input and output values and support describe calls. The invocable method must be static and public or global, and its class must be an outer class.

**✅ Tại sao đáp án đúng:**
> Cú pháp A: @InvocableMethod global static List<List<Recommendation>> getLevel(List<ContactWrapper> input). Phương thức invocable bắt buộc phải là static, nhận tham số dạng List và kiểu trả về cũng bắt buộc là List of List (ở đây là List<List<Recommendation>>) để hỗ trợ xử lý hàng loạt bulkified.

**❌ Tại sao đáp án sai:**
> **B.** Sai vì thiếu từ khóa 'static', invocable method bắt buộc phải là static.
> **C.** Kiểu trả về ListRecommendation (không có List bao ngoài) là sai định dạng danh sách bulkified.
> **D.** Thiếu static và tham số truyền vào là ContactWrapper thô không bọc trong List là sai quy tắc bulkified.

**💡 Từ khóa ghi nhớ:** `Invocable Method -> Luôn bắt đầu bằng @InvocableMethod, bắt buộc phải là STATIC, nhận vào List và trả về List/List of List!`

---

## Câu 341

**🔵 An Apex transaction inserts 100 Account records and 2,000 Contact records before encountering a DML exception when attempting to insert 500 Opportunity records. The Account records are inserted by calling the database.insert() method with the allOrNone argument set to false. The Contact and Opportunity records are inserted using the standalone insert statement. How many total records will be committed to the database in this transaction?**

- **A.** 2,000 ❌
- **B.** 2,100 ❌
- **C.** 0 ✅
- **D.** 100 ❌

**📝 Dịch tiếng Việt:**
> Một Apex transaction thực hiện: Chèn thành công 100 Accounts (bằng Database.insert(accts, false)). Chèn thành công 2,000 Contacts (bằng lệnh insert standalone). Cuối cùng bị báo lỗi DML Exception khi cố chèn 500 Opportunities (bằng lệnh insert standalone). Hỏi tổng cộng có bao nhiêu bản ghi thực sự được lưu (commit) thành công vào cơ sở dữ liệu sau transaction này?

**💬 Giải thích gốc (English):**
> All operations are in one transaction. If any operation in the transaction fails, all DML operation are rolledback.

**✅ Tại sao đáp án đúng:**
> Tổng số bản ghi committed thành công là 0 (C). Vì toàn bộ các câu lệnh diễn ra trong cùng một Transaction (Giao dịch). Một khi xảy ra lỗi runtime không được xử lý (DML Exception ở bước Opportunity), Salesforce sẽ lập tức hủy bỏ (rollback) toàn bộ giao dịch, xóa sạch mọi dữ liệu đã chèn tạm trước đó để đảm bảo tính toàn vẹn dữ liệu.

**❌ Tại sao đáp án sai:**
> **A.** Sai tính toán do nghĩ Contacts không bị rollback.
> **B.** Sai tính toán.
> **D.** Lầm tưởng 100 Accounts dùng Database.insert(..., false) sẽ được giữ lại. Thực tế, allOrNone=false chỉ bỏ qua lỗi trong chính câu lệnh chèn Account đó, chứ không thể bảo vệ Account khỏi đợt rollback toàn cục của cả Transaction khi có exception nổ ra ở câu lệnh sau.

**💡 Từ khóa ghi nhớ:** `Mẹo Transaction: Có lỗi Exception không được bắt xảy ra ở bất cứ đâu trong Transaction -> TOÀN BỘ BẢN GHI ĐỀU BỊ ROLLBACK VỀ 0!`

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
> Tạo một trường Roll-Up Summary trên đối tượng cha Order thực hiện tính MAX trường availability date của các Line Items con (D). Ngày giao hàng khi tất cả có sẵn bắt buộc phải là ngày có hàng muộn nhất (lớn nhất - MAX) trong số các bản ghi con.

**❌ Tại sao đáp án sai:**
> **A.** Không tồn tại hàm LATEST trong cấu trúc trường công thức của Salesforce.
> **B.** Hàm CEILING chỉ dùng để làm tròn lên một số thực decimal, không liên quan đến việc tính toán ngày tháng.
> **C.** Sử dụng hàm DAYS và đếm số lượng bản ghi con COUNT không giúp xác định được ngày có hàng lớn nhất của các bản ghi con.

**💡 Từ khóa ghi nhớ:** `Tìm ngày muộn nhất của bản ghi con đưa lên cha -> Tạo trường Roll-up Summary sử dụng hàm MAX.`

---

## Câu 343

**🔵 The following Apex method is part of the ContactService class that is called from a trigger:
public static void setBusinessUnitToEMEA(Contact thisContact){
thisContact.Business_Unit__c = 'EMEA';
update thisContact;
}
How should the developer modify the code to ensure best practices are met?
A.
Public void setBusinessUnitToEMEA(List<Contact> contatcs){
contacts[0].Business_Unit__c = 'EMEA' ;
update contacts[0];
}
B.
Public static void setBusinessUnitToEMEA(Contact thisContact){
List<Contact> contacts = new List<Contact>();
contacts.add(thisContact.Business_Unit__c = 'EMEA');
update contacts;
}
C.
Public static void setBusinessUnitToEMEA(List<Contact> contacts){
for(Contact thisContact : contacts){
thisContact.Business_Unit__c = 'EMEA' ;
update contacts[0];
}
}
D.
Public static void setBusinessUnitToEMEA(List<Contact> contacts){
for(Contact thisContact : contacts) {
thisContact.Business_Unit__c = 'EMEA' ;
}
update contacts;
}**


**📝 Dịch tiếng Việt:**
> Cho phương thức Apex sau được gọi từ một Trigger: [Code setBusinessUnitToEMEA]. Developer nên sửa đổi code như thế nào để đảm bảo tuân thủ best practices (thực hành tốt nhất) của Salesforce trigger?

**💬 Giải thích gốc (English):**
> A DML statement should be placed outside of a loop to optimize performance and reduce governor limit usage.

**✅ Tại sao đáp án đúng:**
> Cú pháp D: Public static void setBusinessUnitToEMEA(List<Contact> contacts) { for(Contact thisContact : contacts) { thisContact.Business_Unit__c = 'EMEA' ; } update contacts; }. Phương thức nhận tham số là danh sách List<Contact> để xử lý bulkified và đưa câu lệnh DML update ra NGOÀI vòng lặp for để tránh đụng trần 150 DML limit.

**❌ Tại sao đáp án sai:**
> **A.** Sai vì chỉ xử lý phần tử đầu tiên của danh sách (contacts[0]) và thực hiện DML đơn lẻ, làm mất đi tính xử lý hàng loạt.
> **B.** Cú pháp gán trị chèn vào list sai ngữ pháp nghiêm trọng.
> **C.** Vẫn giữ nguyên câu lệnh DML update bên trong thân vòng lặp for (update contacts[0]), gây nguy cơ crash DML Limit cực cao.

**💡 Từ khóa ghi nhớ:** `Trigger Best Practice thần thánh -> Luôn nhận tham số dạng LIST + Tuyệt đối cấm tiệt đặt câu lệnh DML (insert, update, delete) bên trong vòng lặp FOR!`

---

## Câu 344

**🔵 What is an example of a polymorphic lookup field in Salesforce?**

- **A.** The WhatId field on the standard Event object ✅
- **B.** The ParentId field on the standard Account object ❌
- **C.** A custom field, Link__c, on the standard Contact object that looks up to an Account or a Campaign ❌
- **D.** The LeadId and ContactId fields on the standard Campaign Member object ❌

**📝 Dịch tiếng Việt:**
> Cái field lookup nào dưới đây thuộc loại 'đa hình' (polymorphic) - tức là một mình nó có thể trỏ tới nhiều loại Object khác nhau?

**💬 Giải thích gốc (English):**
> A polymorphic lookup field can reference multiple different object types. The WhatId field on the Event object is a classic example of this. It can reference either a Lead, Contact, Account, or Opportunity.

**✅ Tại sao đáp án đúng:**
> B đúng vì `WhatId` trên Task hoặc Event cực kỳ linh hoạt, nó có thể link tới Account, Opportunity, Campaign... tùy hỉ. Đó chính là sự đa hình.

**❌ Tại sao đáp án sai:**
> **A.** `ParentId` trên Account chỉ trỏ tới duy nhất 1 loại object là Account (cha). Không có đa hình gì ở đây.
> **C.** Đây là 2 field riêng biệt trỏ tới 2 object riêng biệt. Không phải là 1 field trỏ tới nhiều object.
> **D.** Salesforce không cho phép mày tự tạo Polymorphic Lookup field đâu (trừ khi dùng vài trick cực khó hoặc tool xịn), đây chỉ là câu lừa thôi.

**💡 Từ khóa ghi nhớ:** `Mẹo PD1: Polymorphic = WhoId (trỏ tới People: Lead/Contact) hoặc WhatId (trỏ tới Objects: Account/Opp/...). Cứ nhớ Who/What là đa hình.`

---

## Câu 345

**🔵 Which three operations affect the number of times a trigger can fire? (Choose three.)**

- **A.** Lightning Flows ✅
- **B.** Roll-Up Summary fields ✅
- **C.** Criteria-based Sharing calculations ❌
- **D.** Workflow Rules ✅
- **E.** Email messages ❌

**📝 Dịch tiếng Việt:**
> Ba thao tác nào ảnh hưởng đến số lần một trigger có thể được kích hoạt? (Chọn 3)

**💬 Giải thích gốc (English):**
> The three operations that affect the number of times a trigger can fire are:
> 1. Lightning Flows
> 2. Roll-Up Summary fields
> 3. Workflow Rules
> These operations can cause triggers to execute multiple times due to updates they perform on records.

**✅ Tại sao đáp án đúng:**
> B: Roll-up summary trên bản ghi cha sẽ làm trigger của cha nổ khi con thay đổi. C & D: Flow và Workflow Field Update có thể làm bản ghi được cập nhật lại và kích hoạt lại các Before/After Update triggers (re-fire).

**❌ Tại sao đáp án sai:**
> **A.** Sharing calculations chạy ngầm để tính toán quyền truy cập, không làm nổ trigger.
> **E.** Gửi email là một hành động đi kèm, không làm thay đổi bản ghi để kích hoạt lại trigger.

**💡 Từ khóa ghi nhớ:** `Keywords: Trigger re-fire -> Workflow, Flow, Roll-up Summary. 'Bộ ba sát thủ' làm tăng số lần trigger nổ.`

---

## Câu 346

**🔵 A Salesforce Administrator is creating a record-triggered now. When certain criteria are met, the now must call an Apex method to execute a complex validation involving several types of objects. When creating the Apex method, which annotation should a developer use to ensure the method can be used within the flow?**

- **A.** @RemoteAction ❌
- **B.** @future ❌
- **C.** @AuraEnabled ❌
- **D.** @InvocableMethod ✅

**📝 Dịch tiếng Việt:**
> Khi tạo một phương thức Apex để Flow có thể gọi và thực hiện kiểm tra logic phức tạp, developer nên dùng annotation nào?

**💬 Giải thích gốc (English):**
> Invocable methods are called natively from Rest, Apex, Flow, or Einstein bot that interacts with the external API source. Invocable methods have dynamic input and output values and support describe calls.

**✅ Tại sao đáp án đúng:**
> @InvocableMethod cho phép một phương thức Apex được hiển thị dưới dạng một Action trong Flow Builder hoặc Process Builder.

**❌ Tại sao đáp án sai:**
> **A.** @future dùng để chạy các tác vụ không đồng bộ (background), Flow không thể gọi trực tiếp và nhận kết quả ngay được.
> **C.** @AuraEnabled dùng cho giao tiếp giữa Client-side (LWC/Aura) và Server-side (Apex).
> **D.** @RemoteAction dùng riêng cho Visualforce JavaScript Remoting.

**💡 Từ khóa ghi nhớ:** `Flow gọi Apex -> Luôn luôn là @InvocableMethod.`

---

## Câu 347

**🔵 A developer is creating an app that contains multiple Lightning web components. One of the child components is used for navigation purposes. When a user clicks a button called Next in the child component, the parent component must be alerted so it can navigate to the next page. How should this be accomplished?**

- **A.** Create a custom event. ✅
- **B.** Call a method in the Apex controller. ❌
- **C.** Update a property on the parent. ❌
- **D.** Fire a notification. ❌

**📝 Dịch tiếng Việt:**
> Developer đang xây dựng một ứng dụng chứa nhiều Lightning Web Components. Một component con được dùng để định hướng trang. Khi user click nút 'Next' trên component con, component cha phải được thông báo để chuyển trang. Cách giải quyết chuẩn xác nhất là gì?

**💬 Giải thích gốc (English):**
> Custom events are used to communicate between Lightning web components, and can be used to pass data from a parent component to a child component. The parent component can fire a custom event and include the data as a parameter, which the child component can then access.

**✅ Tại sao đáp án đúng:**
> Tạo và bắn ra một sự kiện tùy chỉnh (Custom Event) từ component con (A). Component cha sẽ đăng ký lắng nghe sự kiện này (onnext) để thực thi logic chuyển trang, đảm bảo đúng cơ chế đóng gói và truyền thông tin ngược dòng từ con lên cha trong LWC.

**❌ Tại sao đáp án sai:**
> **B.** Apex controller chạy dưới database server layer, không thể can thiệp điều hướng giao diện trực quan client-side của component cha.
> **C.** Component con cấm và không thể trực tiếp thay đổi thuộc tính (property) của component cha để bảo toàn tính đóng gói dữ liệu.
> **D.** Fire notification chỉ hiển thị thông báo toast nổi trên màn hình, không giúp truyền thông tin điều khiển giữa hai component.

**💡 Từ khóa ghi nhớ:** `Giao tiếp ngược dòng từ Component Con lên Component Cha trong LWC -> Luôn sử dụng CUSTOM EVENT!`

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
> Sử dụng lớp Schema.DescribeSObjectResult của đối tượng Case (A). Lập trình viên gọi hàm Case.SObjectType.getDescribe().getRecordTypeInfos() để lấy danh sách chi tiết các Record Type khả dụng của user một cách động và chính xác nhất.

**❌ Tại sao đáp án sai:**
> **B.** Sử dụng SOQL lấy toàn bộ Case chỉ trả về các bản ghi Case cụ thể, không trả về thông tin cấu hình Record Types khả dụng của Org.
> **C.** DescribeFieldResult của trường RecordType chỉ trả về thông tin metadata mô tả của trường, không trả về danh sách các Record Type Info thực tế của đối tượng.
> **D.** Không tồn tại phương thức getRecordTypes() trực tiếp trên đối tượng Case.

**💡 Từ khóa ghi nhớ:** `Truy xuất danh sách Record Types động khả dụng của user -> Luôn dùng Schema.DescribeSObjectResult (SObjectType.getDescribe()).`

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
> A: Chỉ được khởi tạo duy nhất 1 lần khi class được nạp vào bộ nhớ (class loaded). C: Chỉ được phép định nghĩa và khai báo trong các lớp cha ngoài cùng (outer classes), cấm khai báo trong inner classes. E: Hoàn toàn được loại trừ (excluded) khỏi View State của trang Visualforce, giúp tối ưu hóa dung lượng truyền tải dữ liệu của trang.

**❌ Tại sao đáp án sai:**
> **B.** Biến tĩnh static trong Apex chỉ tồn tại trong phạm vi của 1 single Apex Transaction chứ không thể tồn tại vượt ra ngoài scope của transaction.
> **D.** Ngược lại với câu C, static methods hoàn toàn bị cấm khai báo trong các inner classes.

**💡 Từ khóa ghi nhớ:** `Đặc tính static Apex -> Khởi tạo khi load class + Chỉ có ở Outer class + Không bị truyền vào Visualforce View State!`

---
