# PD1 SET0 — Giải thích chi tiết (Tiếng Việt)

---

## Câu 1

📌 **Đáp án đúng: D**

📝 **Bản dịch:**
Một developer được thông báo về một vấn đề với một Apex trigger tùy chỉnh đang gây ra việc tạo bản ghi trùng lặp.
Đâu là cách tiếp cận debug phù hợp nhất để khắc phục sự cố?

✅ **Tại sao đúng:**
- **D đúng** vì Apex Interactive Debugger cho phép developer đặt breakpoint, chạy từng dòng code (step through), và quan sát trực tiếp giá trị biến, luồng thực thi — đây là công cụ chính xác và hiệu quả nhất để tìm nguyên nhân tạo bản ghi trùng.

❌ **Tại sao sai:**
- **A sai** vì vô hiệu hóa trigger trên production là hành động nguy hiểm, ảnh hưởng đến người dùng thật và không phải là cách debug — đây là workaround, không phải troubleshooting.
- **B sai** vì `System.debug` chỉ ghi log ra debug log, không cho phép tương tác real-time hay dừng lại kiểm tra từng bước. Hữu ích nhưng không phải "most appropriate" khi đã có Interactive Debugger.
- **C sai** vì "Historical Event logs" không phải tính năng có trong Salesforce — đây là thuật ngữ bịa, không tồn tại.

💡 **Mẹo ghi nhớ:**
> **"Step through = Interactive Debugger"** — Bất cứ khi nào đề hỏi về debug từng bước (step through, breakpoint), đáp án là **Apex Interactive Debugger**.

---

## Câu 2

📌 **Đáp án đúng: D**

📝 **Bản dịch:**
Khi viết một Apex class, developer muốn đảm bảo tất cả chức năng đang được phát triển hoạt động đúng như yêu cầu.
Developer nên dùng cách tiếp cận nào để chắc chắn Apex class hoạt động theo đúng specification?

> ⚠️ **Lưu ý:** Câu này có vẻ gây tranh cãi — đáp án D (try/catch) là đáp án được đánh dấu đúng trong bộ đề, nhưng về mặt best practice thực tế, tao sẽ giải thích rõ tại sao mỗi lựa chọn.

✅ **Tại sao đúng:**
- **D đúng (theo đề)** vì try/catch giúp handle các exception, đảm bảo code không crash và xử lý lỗi theo đúng spec — đây là cách "ensure the class works according to specifications" trong ngữ cảnh production-ready code.

❌ **Tại sao sai:**
- **A sai** vì đây mô tả việc tạo test class để *chạy* business logic, không phải để *verify* rằng logic hoạt động đúng spec theo cách có cấu trúc. Hơn nữa, "run test in Developer Console" là cách thực thi, không phải xác minh specification.
- **B sai** vì Execute Anonymous chỉ dùng để chạy code nhanh, không có cơ chế xác minh kết quả một cách có hệ thống.
- **C sai** vì Savepoint + Database.rollback() dùng cho transaction control, không liên quan đến việc verify business logic.

💡 **Mẹo ghi nhớ:**
> Câu hỏi hỏi "ensure working according to specifications" → try/catch đảm bảo class xử lý đúng exception theo spec. Đây là dạng câu **bẫy** — đọc kỹ context!

---

## Câu 3

📌 **Đáp án đúng: A, B**

📝 **Bản dịch:**
Một developer đã xác định một method trong Apex class thực hiện các thao tác tốn nhiều tài nguyên trong bộ nhớ bằng cách lặp qua kết quả của một câu lệnh SOQL trên Account. Method này cũng thực hiện DML để lưu thay đổi vào database.
Hai kỹ thuật nào developer nên áp dụng như best practice để đảm bảo transaction control và tránh vượt quá governor limits?

✅ **Tại sao đúng:**
- **A đúng** vì `Database.Savepoint` cho phép tạo điểm khôi phục trong transaction — nếu có lỗi xảy ra, có thể rollback về trạng thái trước đó, đảm bảo tính toàn vẹn dữ liệu (database integrity).
- **B đúng** vì `System.Limits` class cho phép kiểm tra mức tiêu thụ CPU limit hiện tại (e.g., `Limits.getCpuTime()`, `Limits.getLimitCpuTime()`), giúp tránh vượt quá governor limit trong các vòng lặp tốn tài nguyên.

❌ **Tại sao sai:**
- **C sai** vì `@ReadOnly` annotation chỉ áp dụng cho các Visualforce page/Remote Action, không dùng trong Apex class thông thường, và nó giới hạn DML — mà method này cần thực hiện DML.
- **D sai** vì "partial DML statements" (tức là `Database.insert(records, false)`) không phải là giải pháp cho transaction control hay governor limit — nó chỉ cho phép tiếp tục khi có lỗi trên một số record, nhưng không kiểm soát transaction hay CPU.

💡 **Mẹo ghi nhớ:**
> **"Resource intensive + DML"** → nhớ 2 thứ: **Savepoint** (bảo vệ data) + **System.Limits** (kiểm tra limit). Cặp đôi hoàn hảo cho transaction control!

---

## Câu 4

📌 **Đáp án đúng: A**

📝 **Bản dịch:**
Một developer muốn truy cập standard price book trong org khi viết test class cho một OpportunityLineItem trigger.
Method nào cho phép truy cập price book?

✅ **Tại sao đúng:**
- **A đúng** vì `Test.getStandardPricebookId()` là method chính thức được Salesforce cung cấp để lấy ID của Standard Pricebook trong môi trường test — đây là cách duy nhất được khuyến nghị vì test context không thể truy cập real data.

❌ **Tại sao sai:**
- **B sai** vì `@TestVisible` chỉ dùng để expose private method/field của Apex class ra cho test class, không liên quan đến Price Book.
- **C sai** vì `Test.loadData()` dùng để nạp dữ liệu từ static resource (CSV), không phải để lấy Standard Pricebook — Standard Pricebook không thể tạo bằng CSV.
- **D sai** vì `@IsTest(SeeAllData=true)` là cách tệ nhất — nó truy cập dữ liệu thật của org, có thể gây lỗi không ổn định; hơn nữa "delete the existing standard price book" là sai hoàn toàn, không thể xóa Standard Pricebook.

💡 **Mẹo ghi nhớ:**
> **"Standard Pricebook trong test"** = luôn dùng `Test.getStandardPricebookId()`. Nhớ: **Test class → Test method**!

---

## Câu 5

📌 **Đáp án đúng: A, D**

📝 **Bản dịch:**
Giả sử `name` là một String lấy từ tag `<apex:inputText>` trên Visualforce page, hai câu SOQL nào được thực hiện an toàn khỏi SOQL injection?

✅ **Tại sao đúng:**
- **A đúng** vì dùng **bind variable** (`:query`) trong static SOQL — Salesforce tự động escape giá trị khi dùng dấu `:`, không thể inject code.
- **D đúng** vì dùng `String.escapeSingleQuotes(name)` để sanitize input trước khi đưa vào dynamic query — escape ký tự đặc biệt, ngăn injection.

❌ **Tại sao sai:**
- **B sai** vì string được nối trực tiếp vào dynamic query (`+name+`) mà không có escape hay bind variable — đây là lỗ hổng SOQL injection điển hình.
- **C sai** vì `name.noQuotes()` không phải method tồn tại trong Apex String class — đây là method bịa, không compile được.

💡 **Mẹo ghi nhớ:**
> **2 cách chống SOQL injection:** (1) **Bind variable** dấu `:` trong static SOQL, (2) **`escapeSingleQuotes()`** cho dynamic SOQL. Nhớ: **Bind hoặc Escape!**

---

## Câu 6

📌 **Đáp án đúng: B, C**

📝 **Bản dịch:**
Một developer tạo một Lightning Web Component tên `statusComponent` để nhúng vào trang record của Account.
Developer cần làm hai việc gì để component này khả dụng?

✅ **Tại sao đúng:**
- **B đúng** vì `<target>lightning__RecordPage</target>` phải được khai báo trong file **metadata** `statusComponent.js-meta.xml` để chỉ định component có thể dùng trên Record Page.
- **C đúng** vì `isExposed` phải được set `true` trong `js-meta.xml` thì component mới hiển thị trong App Builder để admin có thể kéo thả vào trang.

❌ **Tại sao sai:**
- **A sai** vì `<target>` khai báo trong file `.js` là sai — `.js` là file JavaScript logic, không phải nơi khai báo metadata. Cấu hình deployment metadata luôn nằm trong `.js-meta.xml`.
- **D sai** vì `<masterLabel>Account</masterLabel>` không phải thuộc tính hợp lệ để chỉ định trang. Để giới hạn theo object type, dùng `<targetConfig>` với `objects`, không dùng `masterLabel`.

💡 **Mẹo ghi nhớ:**
> **LWC xuất hiện trên App Builder** cần 2 điều kiện: **`isExposed=true`** + **`<target>` đúng loại trang** — đều trong file **`.js-meta.xml`**. Nhớ: **Meta = Meta file!**

---

## Câu 7

📌 **Đáp án đúng: D**

📝 **Bản dịch:**
Xem đoạn code sau (truy vấn Case với LIMIT 50000, dùng Database.update với allOrNone=false).
Developer cần lưu ý điều gì khi môi trường có hơn 10,000 bản ghi Case?

✅ **Tại sao đúng:**
- **D đúng** vì SOQL governor limit cho phép tối đa **50,000 rows** trong một transaction — nhưng giới hạn cho DML là **10,000 records** trong một lần DML. Khi có hơn 10,000 Case, list `casesToUpdate` sẽ có hơn 10,000 phần tử → DML vượt limit → transaction fail. `Database.update(list, false)` chỉ bỏ qua lỗi trên từng record, không bypass governor limits.

❌ **Tại sao sai:**
- **A sai** vì try/catch **không thể** bắt governor limit exceptions — `LimitException` là uncatchable exception trong Apex.
- **B sai** vì try/catch bắt được DML exceptions thông thường (e.g., validation rule, required field), nhưng **không bắt được** governor limit exception. Câu hỏi hỏi về môi trường 10,000+ records → governor limit là vấn đề.
- **C sai** vì với hơn 10,000 records, governor limit sẽ bị vượt và transaction fail — không thể commit thành công.

💡 **Mẹo ghi nhớ:**
> **`LimitException` = UNCATCHABLE** — try/catch vô dụng với governor limits! DML limit = **10,000 records** per transaction.

---

## Câu 8

📌 **Đáp án đúng: B**

📝 **Bản dịch:**
Một Apex method tên `getAccounts`, trả về danh sách Account với tham số `searchTerm`, có thể dùng trong Lightning Web Component.
Cú pháp đúng để định nghĩa property dùng `@wire` với method này là gì?

✅ **Tại sao đúng:**
- **B đúng** vì cú pháp `@wire` đúng là: `@wire(apexMethod, { paramName: '$reactiveVar' }) property;` — tham số phải được truyền dưới dạng **object** với key-value, và dùng dấu `$` trước tên property để chỉ reactive variable.

❌ **Tại sao sai:**
- **A sai** vì truyền `'$searchTerm'` trực tiếp không phải dạng object — sai cú pháp `@wire`, tham số phải là `{ key: value }`.
- **C sai** vì `@AuraEnabled` là annotation cho **Apex method**, không phải decorator cho LWC property. Nhầm lẫn giữa Apex và LWC.
- **D sai** vì tương tự C, `@AuraEnabled` sai hoàn toàn trong context LWC property.

💡 **Mẹo ghi nhớ:**
> **`@wire` syntax:** `@wire(method, { param: '$value' }) prop;` — nhớ **curly braces `{}`** và **dollar sign `$`** cho reactive!

---

## Câu 9

📌 **Đáp án đúng: C**

📝 **Bản dịch:**
Khi người dùng sửa Postal Code trên Account, một trường text tùy chỉnh "Timezone" phải được cập nhật dựa trên giá trị trong custom object `PostalCodeToTimezone__c`.
Cách tối ưu để implement tính năng này là gì?

✅ **Tại sao đúng:**
- **C đúng** vì yêu cầu cần: (1) trigger khi Postal Code thay đổi, (2) tra cứu dữ liệu từ custom object khác, (3) cập nhật field. Flow Builder hỗ trợ đầy đủ: Record-triggered flow có thể detect field change, query related object và update field — **không cần code**.

❌ **Tại sao sai:**
- **A sai** vì Account Assignment Rule dùng để assign record cho user/queue, không dùng để update field dựa trên logic tra cứu.
- **B sai** vì Formula field là **read-only và computed** — không thể tra cứu qua custom object khác bằng cross-object formula đơn giản khi cần lookup logic phức tạp, và không thể "store" giá trị.
- **D sai** vì Approval Process dùng để phê duyệt record qua các bước, không phải để cập nhật field tự động khi dữ liệu thay đổi.

💡 **Mẹo ghi nhớ:**
> **Lookup sang object khác + auto-update = Flow** (không phải Formula, vì Formula không thể lookup custom object tùy ý). Từ khóa **"optimal"** thường gợi ý declarative (Flow > Apex).

---

## Câu 10

📌 **Đáp án đúng: B, D**

📝 **Bản dịch:**
Một developer được yêu cầu xây dựng một ứng dụng responsive có khả năng phản hồi touch events, chạy trên stateful clients.
Hai công nghệ nào được xây dựng trên framework hỗ trợ đầy đủ yêu cầu này?

✅ **Tại sao đúng:**
- **B đúng** vì **Lightning Web Components (LWC)** là modern web standard, hỗ trợ responsive design, touch events, và stateful client-side rendering.
- **D đúng** vì **Aura Components** cũng được xây dựng trên Salesforce Lightning framework, hỗ trợ responsive và touch — là thế hệ trước của LWC nhưng vẫn đáp ứng yêu cầu.

❌ **Tại sao sai:**
- **A & C sai** vì **Visualforce** (Pages và Components) là công nghệ server-side rendering truyền thống, không được thiết kế cho responsive/touch-first experience và không hỗ trợ stateful client-side framework đầy đủ.

💡 **Mẹo ghi nhớ:**
> **Responsive + Touch + Stateful client = Lightning framework** (LWC hoặc Aura). Visualforce = server-side = không phù hợp!

---

## Câu 11

📌 **Đáp án đúng: B**

📝 **Bản dịch:**
Một công ty phần mềm muốn report về việc công ty nào đã báo cáo bug nào. Mỗi công ty có thể báo cáo nhiều bug và một bug có thể được báo cáo bởi nhiều công ty.
Cần gì để cho phép reporting này?

✅ **Tại sao đúng:**
- **B đúng** vì đây là quan hệ **Many-to-Many** (nhiều công ty — nhiều bug). Salesforce giải quyết Many-to-Many bằng **Junction Object** — một object trung gian có Master-Detail đến cả hai object cha, cho phép report across cả hai.

❌ **Tại sao sai:**
- **A sai** vì Master-Detail từ Bug__c đến Account chỉ là quan hệ One-to-Many (một Account nhiều Bug) — không thể một Bug thuộc nhiều Account.
- **C sai** vì Roll-up Summary field chỉ dùng để tổng hợp số liệu (COUNT, SUM...) trong quan hệ Master-Detail, không tạo quan hệ Many-to-Many.
- **D sai** vì Lookup field từ Bug__c đến Account cũng chỉ là One-to-Many, không phải Many-to-Many.

💡 **Mẹo ghi nhớ:**
> **Many-to-Many = Junction Object**. Nhớ công thức: khi đề có **"multiple... và... multiple"** → Junction Object!

---

## Câu 12

📌 **Đáp án đúng: A, C**

📝 **Bản dịch:**
Hai cách nào developer có thể kiểm tra trạng thái (status) của một enqueued job cho class implement Queueable interface?

✅ **Tại sao đúng:**
- **A đúng** vì **Apex Jobs page** (Setup → Apex Jobs) hiển thị trạng thái của tất cả các async jobs bao gồm Queueable jobs.
- **C đúng** vì **Apex Flex Queue** hiển thị các jobs đang chờ trong hàng đợi (queued/holding status) — đặc biệt hữu ích cho Queueable jobs chưa bắt đầu chạy.

❌ **Tại sao sai:**
- **B sai** vì "Apex Status page" **không tồn tại** trong Salesforce Setup — đây là tên bịa.
- **D sai** vì query `AsyncApexJob` object **là cách đúng** về mặt kỹ thuật, nhưng đề hỏi 2 đáp án và cả A, C đều đúng hơn D trong context "check status" qua UI. Tuy nhiên, lưu ý đây có thể là trick — một số version của câu hỏi này có D là đúng thay C.

💡 **Mẹo ghi nhớ:**
> **Async job monitoring = Apex Jobs + Apex Flex Queue**. Nhớ: **Flex Queue** dành cho jobs *đang chờ*, **Apex Jobs** cho jobs *đang/đã chạy*.

---

## Câu 13

📌 **Đáp án đúng: C**

📝 **Bản dịch:**
Developer tạo trang cho phép tạo nhiều Opportunity. Developer cần tìm record type mặc định của người dùng hiện tại cho Opportunity.
Cách nào để tìm default record type của user hiện tại?

✅ **Tại sao đúng:**
- **C đúng** vì `SObjectType.getDescribe().getRecordTypeInfos()` trả về danh sách tất cả Record Type Info, và method `isDefaultRecordTypeMapping()` trả về `true` cho record type mặc định của user hiện tại. Đây là cách chính thức dùng **Schema Describe**.

❌ **Tại sao sai:**
- **A sai** vì `profile.Opportunity.getDefaultRecordType()` **không phải method tồn tại** trong Salesforce API — đây là cú pháp bịa.
- **B sai** vì khi mới tạo Opportunity object trong Apex (chưa insert), `recordType` field chưa được gán tự động — giá trị này không phản ánh default record type của user.
- **D sai** vì `Schema.userInfo.Opportunity.getDefaultRecordType()` **không phải method tồn tại** — đây là cú pháp bịa.

💡 **Mẹo ghi nhớ:**
> **Default Record Type = Schema Describe** → `getRecordTypeInfos()` + loop + `isDefaultRecordTypeMapping()`. Nhớ: **"Describe để lấy metadata!"**

---

## Câu 14

📌 **Đáp án đúng: C**

📝 **Bản dịch:**
Thuộc tính nào của LWC custom event cho phép event vừa bubble lên containment hierarchy vừa vượt qua ranh giới Shadow DOM?

✅ **Tại sao đúng:**
- **C đúng** vì:
  - `bubbles: true` → event lan lên DOM tree (bubble up qua containment hierarchy).
  - `composed: true` → event vượt qua Shadow DOM boundary, tức là có thể được nghe bởi component bên ngoài Shadow DOM.
  - Cần **cả hai** để event đi xa nhất.

❌ **Tại sao sai:**
- **A sai** vì `bubbles: false` nghĩa là event không bubble lên — chỉ `composed: true` thôi thì event không đi đâu được.
- **B sai** vì cả hai đều false — event chỉ tồn tại tại nơi dispatch, không đi đâu cả.
- **D sai** vì `bubbles: true, composed: false` — event bubble lên trong cùng Shadow DOM tree nhưng **dừng lại ở ranh giới Shadow DOM**, không vượt qua được.

💡 **Mẹo ghi nhớ:**
> **"Bubble + Cross Shadow DOM"** = `bubbles: true` + `composed: true`. Nhớ: **Bubble = đi lên, Composed = vượt tường!**

---

## Câu 15

📌 **Đáp án đúng: D**

📝 **Bản dịch:**
Developer cần ngăn không cho ai (trừ Sales Manager profile) thay đổi Opportunity Status thành "Closed Lost" nếu trường lost reason trống.
Automation nào cho phép developer thỏa mãn yêu cầu này hiệu quả nhất?

✅ **Tại sao đúng:**
- **D đúng** vì **Validation Rule** là cách hiệu quả nhất — có thể check `$Profile.Name != 'Sales Manager'` và `Status = 'Closed Lost'` và `Lost_Reason__c = null`, sau đó hiển thị error message. Không cần code, declarative hoàn toàn, và enforce ở mọi nơi (UI, API, trigger).

❌ **Tại sao sai:**
- **A sai** vì Record-triggered Flow có thể làm được nhưng phức tạp hơn — cần nhiều bước để validate và throw error, không "efficient" bằng Validation Rule cho use case này.
- **B sai** vì Approval Process dùng để phê duyệt record qua workflow, không dùng để block field value change dựa trên profile.
- **C sai** vì Apex Trigger có thể làm được nhưng **không phải cách hiệu quả nhất** — cần viết code, deploy, test. Validation Rule đơn giản hơn nhiều.

💡 **Mẹo ghi nhớ:**
> **Chặn field value + điều kiện phức tạp = Validation Rule** (dùng `$Profile.Name` để kiểm tra profile). Từ khóa **"most efficient"** = ưu tiên declarative!

---

## Câu 16

📌 **Đáp án đúng: D**

📝 **Bản dịch:**
Giá trị 'High', 'Medium', 'Low' là các giá trị phổ biến cho nhiều picklist trên các object khác nhau.
Cách tiếp cận nào giúp đơn giản hóa việc bảo trì picklist và giá trị, đồng thời giới hạn chỉ những giá trị đã đề cập?

✅ **Tại sao đúng:**
- **D đúng** vì **Global Picklist Value Set** cho phép định nghĩa một bộ giá trị tập trung, tái sử dụng trên nhiều object/field khác nhau. Khi cập nhật Global Value Set, tất cả fields dùng nó đều tự động cập nhật — dễ bảo trì. Đồng thời, giá trị bị **giới hạn** chỉ trong value set đó.

❌ **Tại sao sai:**
- **A sai** vì "Display values alphabetically" chỉ là tùy chọn hiển thị, không giới hạn giá trị và không giúp streamline maintenance qua nhiều object.
- **B sai** vì tạo validation rule trên mỗi object là cách phức tạp và phải bảo trì từng rule riêng lẻ — không "streamline" gì.
- **C sai** vì "Restrict picklist to the values defined in the value set" là tùy chọn đúng về giới hạn giá trị, nhưng nếu mỗi field/object có value set riêng thì vẫn phải cập nhật từng cái — không đáp ứng yêu cầu bảo trì tập trung như Global Value Set.

💡 **Mẹo ghi nhớ:**
> **Giá trị dùng chung nhiều object = Global Picklist Value Set**. Nhớ: **"Global" = dùng được ở mọi nơi!**

---

## Câu 17

📌 **Đáp án đúng: B**

📝 **Bản dịch:**
Junction object `Case_Defect__c` có hai Master-Detail đến Case và Defect__c. Cả Case và Defect__c đều có OWD là Private.
Cần làm gì để chia sẻ một bản ghi `Case_Defect__c` cụ thể với một user?

✅ **Tại sao đúng:**
- **B đúng** vì trong quan hệ Master-Detail, **junction object record kế thừa access từ cả hai parent**. Với OWD Private, để user có thể xem `Case_Defect__c`, user phải có quyền truy cập vào **cả** Case cha **và** Defect__c cha — vì quyền truy cập junction record phụ thuộc vào quyền trên cả hai Master.

❌ **Tại sao sai:**
- **A sai** vì junction object với Master-Detail **không có sharing rules riêng** — không thể share trực tiếp junction record, phải share qua parent.
- **C sai** vì chỉ share Case (một parent) là chưa đủ — user cần access cả Defect__c cha.
- **D sai** vì tương tự C, chỉ share Defect__c (một parent) là chưa đủ.

💡 **Mẹo ghi nhớ:**
> **Junction object = kế thừa access từ CẢ HAI parent**. Muốn truy cập junction record → phải có quyền trên **cả hai** master records!

---

## Câu 18

📌 **Đáp án đúng: A**

📝 **Bản dịch:**
Yêu cầu: tính tổng amount trên Order (roll-up), tính line amount cho Line Item, và có thể di chuyển Line Item sang Order khác.
Relationship implementation nào hỗ trợ tất cả yêu cầu này?

✅ **Tại sao đúng:**
- **A đúng** vì **Line Item có re-parentable Master-Detail đến Order** hỗ trợ:
  1. **Roll-up summary** (tính tổng amount trên Order) — chỉ có trong Master-Detail.
  2. **Re-parentable** — cho phép đổi Order cha, tức là di chuyển Line Item sang Order khác.
  3. Tính line amount = formula field → có thể dùng với bất kỳ relationship nào.

❌ **Tại sao sai:**
- **B sai** vì Lookup field **không hỗ trợ Roll-up Summary** — không tính được tổng Amount trên Order.
- **C sai** vì "Order có Master-Detail đến Line Item" là sai chiều — Master nên là Order (cha), Detail là Line Item (con). Cú pháp này đặt quan hệ ngược.
- **D sai** vì tương tự B, Lookup không hỗ trợ Roll-up Summary.

💡 **Mẹo ghi nhớ:**
> **Roll-up Summary = bắt buộc Master-Detail**. **Re-parentable = có thể đổi cha**. Khi cần cả hai → **Re-parentable Master-Detail**!

---

## Câu 19

📌 **Đáp án đúng: C**

📝 **Bản dịch:**
Đoạn code dùng `update theseAccounts` bên trong method `insertAccounts`. Khi thực thi, DML exception được throw.
Developer nên sửa code như thế nào để xử lý exception một cách graceful?

✅ **Tại sao đúng:**
- **C đúng** vì bọc DML trong **try/catch block** cho phép bắt `DmlException`, xử lý lỗi (log, rollback, notify) mà không làm crash toàn bộ transaction — đây là cách graceful exception handling chuẩn.

❌ **Tại sao sai:**
- **A sai** vì `upsert` chỉ thay đổi hành vi DML (insert hoặc update), không xử lý exception. Nếu exception vẫn xảy ra, nó vẫn bubble up.
- **B sai** vì "remove null items" giải quyết một trường hợp cụ thể (NullPointerException), không phải giải pháp tổng quát cho mọi DML exception.
- **D sai** vì Change Data Capture là tính năng streaming events khi data thay đổi, hoàn toàn không liên quan đến xử lý DML exception.

💡 **Mẹo ghi nhớ:**
> **"Handle exceptions gracefully" = try/catch**. Đây là keyword cần nhớ trong mọi câu hỏi liên quan đến error handling!

---

## Câu 20

📌 **Đáp án đúng: A, B**

📝 **Bản dịch:**
Hai phát biểu nào đúng về việc dùng annotation `@testSetup` trong Apex test class?

✅ **Tại sao đúng:**
- **A đúng** vì `@testSetup` **không tương thích** với `@isTest(SeeAllData=true)` — khi SeeAllData=true, test truy cập data thật của org nên không cần setup riêng, và Salesforce không cho phép kết hợp hai annotation này.
- **B đúng** vì method có `@testSetup` **chạy một lần trước mỗi test method** (không phải một lần cho cả class) và **được tính vào governor limits** của từng test method.

❌ **Tại sao sai:**
- **C sai** vì records tạo trong `@testSetup` **CÓ THỂ được update/modify** trong từng test method riêng lẻ — mỗi test method nhận một bản copy fresh của data từ @testSetup.
- **D sai** vì mô tả trong D gần đúng nhưng không chính xác — data không được "made available for all test methods" theo nghĩa dùng chung một bản. Thực ra mỗi test method nhận **bản copy riêng** được rollback sau mỗi test.

💡 **Mẹo ghi nhớ:**
> **@testSetup**: Không dùng được với **SeeAllData=true**, chạy **trước MỖI test method**, data **rollback** sau mỗi test. Nhớ: **Setup = Fresh start mỗi test!**

---

## Câu 21

📌 **Đáp án đúng: D**

📝 **Bản dịch:**
Flow Builder dùng Apex action để lấy thêm thông tin về nhiều Contact, lưu trong class `ContactInfo`.
Định nghĩa đúng của Apex method được gọi từ Flow là gì?

✅ **Tại sao đúng:**
- **D đúng** vì `@InvocableMethod` **bắt buộc**:
  1. Method phải là **`static`**.
  2. Nhận tham số kiểu **`List`** (vì Flow xử lý theo bulk).
  3. Trả về kiểu **`List`** (bulk output).
  Vì vậy: `public static List<ContactInfo> getInfo(List<Id> contactIds)` là đúng hoàn toàn.

❌ **Tại sao sai:**
- **A sai** vì thiếu `static` — `@InvocableMethod` yêu cầu method là static.
- **B sai** vì tham số là `Id` (đơn) thay vì `List<Id>` — Flow luôn gửi List, method phải nhận List.
- **C sai** vì vừa thiếu `static`, vừa nhận tham số đơn thay vì List.

💡 **Mẹo ghi nhớ:**
> **@InvocableMethod = static + List in + List out**. Nhớ: **"Flow nói chuyện theo List, phải dùng List!"**

---

## Câu 22

📌 **Đáp án đúng: C**

📝 **Bản dịch:**
Universal Containers có nhiều app được xây bằng third-party JavaScript framework trên Visualforce. Họ muốn cập nhật các app này để có giao diện giống Lightning Experience.
Developer nên làm gì nhanh và hiệu quả nhất?

✅ **Tại sao đúng:**
- **C đúng** vì **Salesforce Lightning Design System (SLDS)** là CSS framework của Salesforce — chỉ cần nhúng CSS stylesheet của SLDS vào các ứng dụng JavaScript hiện có là có ngay giao diện Lightning, **không cần viết lại code**.

❌ **Tại sao sai:**
- **A sai** vì rewrite toàn bộ Visualforce sang Lightning components là cực kỳ tốn thời gian — trái với yêu cầu "quickest and most effective".
- **B sai** vì `enableLightning` **không phải thuộc tính tồn tại** trong Visualforce page definition — đây là cú pháp bịa.
- **D sai** vì enable "Available for Lightning Experience" chỉ là cài đặt cho phép Visualforce page chạy trong Lightning, không thay đổi visual appearance/styling.

💡 **Mẹo ghi nhớ:**
> **Lightning look & feel nhanh nhất = SLDS CSS**. Không cần rewrite — chỉ cần **import stylesheet**!

---

## Câu 23

📌 **Đáp án đúng: C**

📝 **Bản dịch:**
Code truy vấn tất cả Lead (`SELECT Origin__c FROM Lead`) và update từng record trong vòng lặp trong môi trường có hơn 2,000 Lead.
Governor limit nào có khả năng bị vượt?

✅ **Tại sao đúng:**
- **C đúng** vì giới hạn **SOQL rows = 50,000 records** per transaction. Với hơn 2,000 Lead và query không có LIMIT, khi số Lead vượt 50,000 thì governor limit "Total number of records retrieved by SOQL queries" bị vượt. Trong môi trường 2,000+ lead, nếu có nhiều hơn 50,000 thì fail; nhưng ngay cả 2,000 thì DML trong loop cũng là vấn đề.

> ⚠️ Thực ra với chính xác "hơn 2,000" thì **DML statements** (giới hạn 150) bị vượt trước (mỗi iteration là 1 DML). Tuy nhiên đáp án đề là C — có thể đề muốn nhấn mạnh SOQL rows limit khi số lượng lớn hơn.

❌ **Tại sao sai:**
- **A sai** vì chỉ có **1 SOQL query** được thực thi (query ngoài loop) — không vượt limit 100 SOQL queries.
- **B sai** vì tương tự A, chỉ có 1 SOQL statement.
- **D sai** vì "Total records processed as a result of DML" — giới hạn này là 10,000 records per DML call, nhưng ở đây mỗi DML chỉ update 1 record.

💡 **Mẹo ghi nhớ:**
> **SOQL trong loop = DML trong loop = BAD PRACTICE**. Khi đề hỏi môi trường **"hơn X records"**, nghĩ ngay đến **row limit (50,000)** hoặc **DML limit (150 statements)**.

---

## Câu 24

📌 **Đáp án đúng: B**

📝 **Bản dịch:**
Developer nên làm gì để kiểm tra code coverage của một class sau khi đã run all tests?

✅ **Tại sao đúng:**
- **B đúng** vì sau khi run tests, cột **"Code Coverage"** xuất hiện trong danh sách Apex Classes tại **Setup → Apex Classes** — đây là cách nhanh và trực tiếp nhất.

❌ **Tại sao sai:**
- **A sai** vì "Class Test Percentage tab" **không tồn tại** trong Apex Class list view — đây là tên bịa.
- **C sai** vì "Overall Code Coverage panel" trong Developer Console Tests tab hiển thị tổng coverage của toàn org, không phải coverage riêng của từng class.
- **D sai** vì "Select and run the class on Apex Test Execution page" dùng để **chạy test**, không phải để xem code coverage của một class cụ thể.

💡 **Mẹo ghi nhớ:**
> **Code coverage của class** → xem cột **"Code Coverage"** trên **Apex Classes page** trong Setup. Đơn giản, trực tiếp!

---

## Câu 25

📌 **Đáp án đúng: C**

📝 **Bản dịch:**
Developer cần troubleshoot để tìm nguyên nhân performance issues khi custom page load, đặc biệt là query performance.
Developer nên dùng tool nào?

✅ **Tại sao đúng:**
- **C đúng** vì **Developer Console** có tab **"Query Editor"** và **"Query Plan"** cho phép phân tích SOQL query performance, xem execution plan, và identify slow queries — đây là công cụ tích hợp sẵn cho query troubleshooting.

❌ **Tại sao sai:**
- **A sai** vì VS Code IDE là editor cho code, không có built-in query performance analyzer cho Salesforce queries.
- **B sai** vì AppExchange là marketplace để tải app/components, không phải tool debug.
- **D sai** vì Setup Menu là nơi cấu hình org, không có tính năng query performance analysis.

💡 **Mẹo ghi nhớ:**
> **Query performance = Developer Console** (Query Plan tool). Nhớ: **Console = công cụ debug/analyze tại chỗ!**

---

## Câu 26

📌 **Đáp án đúng: C**

📝 **Bản dịch:**
Code snippet thực hiện SOQL query bên trong vòng lặp `for` (mỗi leadId query một lần).
Best practice nào developer cần áp dụng trong kiến trúc multi-tenant của Salesforce?

✅ **Tại sao đúng:**
- **C đúng** vì **SOQL inside for loop** là anti-pattern nghiêm trọng trong Salesforce — mỗi iteration tốn 1 SOQL query, với 100+ items sẽ vượt limit 100 SOQL queries/transaction. Best practice là **bulkify**: query một lần bên ngoài loop với `WHERE Id IN :leadIds`.

❌ **Tại sao sai:**
- **A sai** vì "avoid returning empty list" không phải best practice liên quan đến multi-tenant hay governor limit.
- **B sai** vì "avoid using variables as query filters" là ngược lại best practice — dùng bind variable (`:variable`) là **được khuyến khích** để tránh SOQL injection.
- **D sai** vì "avoid queries without LIMIT" là best practice đúng trong một số context, nhưng không phải vấn đề chính của code này.

💡 **Mẹo ghi nhớ:**
> **SOQL/DML trong for loop = LUÔN SAI**. Nguyên tắc vàng: **"Bulkify everything!"** — query ngoài loop, DML ngoài loop.

---

## Câu 27

📌 **Đáp án đúng: C**

📝 **Bản dịch:**
Developer cần ngăn tạo bản ghi `Request__c` khi một số điều kiện tồn tại. Class `RequestLogic` đã có method kiểm tra điều kiện.
Implementation đúng là gì?

✅ **Tại sao đúng:**
- **C đúng** vì:
  1. Trigger dùng **`before insert`** — đúng! Để ngăn tạo record, phải dùng before trigger (before insert chạy trước khi record được save vào DB).
  2. Truyền **`Trigger.new`** vào `RequestLogic.validateRecords()` — đúng! Bulkified pattern.
  3. Logic xử lý nằm trong class riêng (separation of concerns).

❌ **Tại sao sai:**
- **A sai** vì `Request__c` (tên object) không thể dùng trực tiếp để gọi `.addError()` — phải gọi trên từng record trong Trigger.new. Hơn nữa, `RequestLogic.isValid(Request__c)` truyền class type thay vì list records — sai cú pháp.
- **B sai** vì dùng **`after insert`** — sau khi record đã được insert vào DB, không thể ngăn tạo record nữa. Phải dùng **before insert** để block.
- **D sai** vì tương tự B, dùng `after insert` — không thể ngăn record creation sau khi đã insert.

💡 **Mẹo ghi nhớ:**
> **Ngăn tạo/sửa record = BEFORE trigger** (`before insert`, `before update`). **AFTER trigger** dùng khi cần ID đã được tạo hoặc thao tác sau khi commit.

---

## Câu 28

📌 **Đáp án đúng: A, B**

📝 **Bản dịch:**
Hai đặc điểm nào đúng về LWC custom events?

> ⚠️ Đây là câu hỏi tricky — cả A và B đều được đánh dấu đúng, nhưng có vẻ mâu thuẫn. Giải thích bên dưới.

✅ **Tại sao đúng:**
- **A đúng** vì mô tả behavior khi `bubbles: true, composed: false` — event bubble lên DOM tree nhưng dừng ở Shadow boundary, chỉ đến được immediate container và immediate child trong cùng Shadow DOM.
- **B đúng** vì mô tả behavior mặc định (`bubbles: false, composed: false`) — event chỉ dispatch tại component tạo ra nó, chỉ đến immediate container (parent component listening trực tiếp).

> Hai đáp án này mô tả hai default behavior khác nhau tùy context. **B là default hoàn toàn (không bubbles)**.

❌ **Tại sao sai:**
- **C sai** vì `@wire` decorated properties dùng để **nhận data từ server**, không liên quan đến việc pass data trong custom event payload.
- **D sai** vì đây là đáp án đúng về cú pháp! Data truyền trong custom event qua property `detail` — `new CustomEvent('myevent', { detail: data })`. Tuy nhiên, câu hỏi đang hỏi "characteristics" và đề đánh D là sai — đây có thể là lỗi của đề hoặc câu D được hiểu khác.

💡 **Mẹo ghi nhớ:**
> **LWC Custom Event mặc định**: `bubbles: false, composed: false` → chỉ parent trực tiếp nghe được. Dùng `{ detail: data }` để truyền data.

---

## Câu 29

📌 **Đáp án đúng: C**

📝 **Bản dịch:**
Annotation nào developer nên dùng trên Apex method để nó có thể được wire vào property trong LWC?

✅ **Tại sao đúng:**
- **C đúng** vì để wire một Apex method vào LWC property dùng `@wire`, method **bắt buộc** phải có `@AuraEnabled(cacheable=true)` — `cacheable=true` là yêu cầu bắt buộc cho `@wire` (vì wire là reactive và cache kết quả).

❌ **Tại sao sai:**
- **A sai** vì `@RemoteAction(cacheable=true)` — `@RemoteAction` là annotation cho Visualforce Remote Action, không dùng trong LWC.
- **B sai** vì `@AuraEnabled` không có `cacheable=true` — không thể wire, chỉ có thể dùng với `imperative call` (gọi trực tiếp).
- **D sai** vì `@RemoteAction` là annotation Visualforce, không phải LWC.

💡 **Mẹo ghi nhớ:**
> **`@wire` = `@AuraEnabled(cacheable=true)`** — nhớ: **wire cần cache**, không có `cacheable=true` thì không wire được!

---

## Câu 30

📌 **Đáp án đúng: B**

📝 **Bản dịch:**
Ví dụ nào là polymorphic lookup field trong Salesforce?

✅ **Tại sao đúng:**
- **B đúng** vì **`WhatId`** trên Event object là polymorphic lookup — nó có thể trỏ đến nhiều loại object khác nhau như Account, Opportunity, Case, v.v. Đây là ví dụ điển hình của polymorphic relationship trong Salesforce.

❌ **Tại sao sai:**
- **A sai** vì `ParentId` trên Account chỉ trỏ đến **Account** (self-referential lookup), không phải polymorphic (chỉ một type).
- **C sai** vì `LeadId` và `ContactId` trên Campaign Member là hai field lookup **riêng biệt**, mỗi field chỉ trỏ đến một object — không phải một field trỏ đến nhiều object type.
- **D sai** vì custom field `Link__c` lookup đến Account **hoặc** Campaign mô tả polymorphic, nhưng **custom polymorphic lookup không thể tạo trong Salesforce** — đây là tính năng chỉ có trên standard fields.

💡 **Mẹo ghi nhớ:**
> **Polymorphic = một field trỏ đến NHIỀU object type**. Standard examples: `WhatId` (Event/Task), `WhoId` (Event/Task). Nhớ: **What/Who = Polymorphic!**

---

## Câu 31

📌 **Đáp án đúng: B, C**

📝 **Bản dịch:**
Universal Containers đã chuyển từ Classic sang Lightning. Yêu cầu: khi user nhấn custom button trên Opportunity detail page, gửi HTTP REST callout đến hệ thống quản lý đơn hàng bên ngoài.
Hai method nào developer nên implement?

✅ **Tại sao đúng:**
- **B đúng** vì **Visualforce quick action** có thể thực hiện callout và được expose trên trang dưới dạng button — vẫn hoạt động trong Lightning Experience.
- **C đúng** vì **Lightning component quick action** là cách hiện đại nhất trong Lightning — tạo LWC/Aura component, expose qua Lightning Action, gắn vào trang.

❌ **Tại sao sai:**
- **A sai** vì "Remote Action... immediate action" và "whenever the Opportunity is updated" — Remote Action không fire tự động khi Opportunity update, nó chỉ fire khi được gọi từ UI. Hơn nữa callout không thể thực hiện trực tiếp từ trigger/synchronous context.
- **D sai** vì `@Future(Callout=true)` là cách để thực hiện callout từ trigger/async context — nhưng câu hỏi yêu cầu button press, không phải after update trigger. Hơn nữa, trigger fires tự động khi update record, không phải khi nhấn button.

💡 **Mẹo ghi nhớ:**
> **Button press → callout** = **Quick Action** (Visualforce hoặc Lightning Component). Nhớ: **button = action, không phải trigger!**

---

## Câu 32

📌 **Đáp án đúng: B**

📝 **Bản dịch:**
Developer cần kiểm tra test coverage của autolaunched Flows trước khi deploy trong change set.
Developer nên dùng gì?

✅ **Tại sao đúng:**
- **B đúng** vì Flow test coverage **không hiển thị trực tiếp trong UI** như Apex. Để query coverage của Flow, developer cần dùng **Tooling API** với SOQL để query object như `FlowTestCoverage` hoặc `FlowVersionView`.

❌ **Tại sao sai:**
- **A sai** vì Flow Properties page hiển thị metadata của flow (version, status, description), không hiển thị test coverage.
- **C sai** vì `ApexTestResult` là object dùng để query kết quả test của **Apex**, không phải Flow.
- **D sai** vì "Code Coverage Setup page" **không tồn tại** như một trang riêng cho Flow — đây là tên bịa.

💡 **Mẹo ghi nhớ:**
> **Flow test coverage = Tooling API + SOQL**. Nhớ: Flow coverage không có UI riêng, phải dùng **Tooling API** để query!

---

## Câu 33

📌 **Đáp án đúng: D**

📝 **Bản dịch:**
Developer muốn đánh dấu mỗi Account trong `List<Account>` là Active hoặc Inactive dựa trên `LastModifiedDate` so với 90 ngày trước.
Kỹ thuật Apex nào developer nên dùng?

✅ **Tại sao đúng:**
- **D đúng** vì:
  1. **`for` loop** để duyệt qua từng Account trong List.
  2. **`if/else` bên trong** để check điều kiện ngày và gán Active/Inactive.
  Đây là pattern đúng và đơn giản nhất cho yêu cầu "iterate and conditionally assign".

❌ **Tại sao sai:**
- **A sai** vì `switch` statement trong Apex không hỗ trợ so sánh date/range condition — `switch` dùng cho giá trị cụ thể (Integer, String, SObject type), không dùng để so sánh `>` hay `<`.
- **B sai** vì tương tự A — `switch` bên ngoài, `for` bên trong là ngược logic. Không iterate được qua List với `switch` làm outer.
- **C sai** vì `if-else` bên ngoài, `for` bên trong cũng là ngược — không thể iterate qua toàn bộ List với pattern này.

💡 **Mẹo ghi nhớ:**
> **Duyệt list + điều kiện = for loop + if/else**. `switch` chỉ dùng khi có **giá trị cụ thể** để match (không dùng được với comparison operators `>`, `<`).

---

## Câu 34

📌 **Đáp án đúng: A, B, C**

📝 **Bản dịch:**
Ba bước nào cho phép nhúng SVG tùy chỉnh vào Lightning Web Component?

✅ **Tại sao đúng:**
- **A đúng** vì sau khi upload static resource, cần **import** vào JS file: `import myIcon from '@salesforce/resourceUrl/myIcon'` và tạo JS property để dùng trong template.
- **B đúng** vì sau khi có property, cần **reference trong HTML template**: `<img src={iconUrl}>` hoặc dùng trong `lwc:ref`.
- **C đúng** vì SVG phải được **upload lên Static Resource** trước — đây là bước đầu tiên và bắt buộc.

❌ **Tại sao sai:**
- **D sai** vì "Reference the import directly in HTML template" — không thể reference import module trực tiếp trong HTML, phải qua JS property.
- **E sai** vì SVG dùng **Static Resource**, không phải **Content Asset File** (Content Asset Files dùng cho Salesforce CMS/Experience Cloud).

💡 **Mẹo ghi nhớ:**
> **SVG trong LWC**: Upload → **Static Resource** → Import trong **JS** → Reference qua **property** trong **HTML**. Flow: **Resource → JS → HTML**.

---

## Câu 35

📌 **Đáp án đúng: C**

📝 **Bản dịch:**
Developer tạo batch Apex job để update nhiều record nhưng job bị timeout và không hoàn thành.
Bước đầu tiên để troubleshoot là gì?

✅ **Tại sao đúng:**
- **C đúng** vì **Asynchronous Job Monitoring page** (Setup → Apex Jobs) cho thấy status, số records processed, số failures, và có thể xem job logs — đây là điểm đầu tiên cần kiểm tra để hiểu job đang làm gì và fail ở đâu.

❌ **Tại sao sai:**
- **A sai** vì kiểm tra debug logs là bước thứ hai — nhưng debug logs của batch job cần được enable trước và có thể không capture được nếu job timeout. Hơn nữa, chưa biết job status thì check log ở đâu?
- **B sai** vì giảm batch size là **giải pháp**, không phải **troubleshooting** — phải hiểu vấn đề trước, sau đó mới điều chỉnh.
- **D sai** vì disable và tạo lại job là hành động quá drastic khi chưa biết nguyên nhân.

💡 **Mẹo ghi nhớ:**
> **Batch job troubleshoot = Async Job Monitoring page TRƯỚC TIÊN**. Nhớ: **"Check status before action!"**

---

## Câu 36

📌 **Đáp án đúng: B**

📝 **Bản dịch:**
Công ty thẻ tín dụng cần service agent xử lý thẻ hỏng/mất cắp, thu thập nhiều thông tin từ khách hàng.
Developer nên dùng gì để implement hiệu quả nhất?

✅ **Tại sao đúng:**
- **B đúng** vì **Lightning Component** (LWC hoặc Aura) cho phép tạo custom UI phức tạp với nhiều form fields, validation logic, dynamic behavior — phù hợp khi cần "gather many pieces of information" với UX tùy chỉnh cao.

❌ **Tại sao sai:**
- **A sai** vì Apex trigger là server-side logic, không có UI để agent nhập thông tin.
- **C sai** vì Approval Process dùng để phê duyệt record qua workflow, không phải để nhập nhiều thông tin.
- **D sai** vì Screen Flow cũng là option hợp lý, nhưng Lightning Component cho phép tùy chỉnh UI phức tạp hơn cho nghiệp vụ "gather many pieces of information" từ service agent.

> 💬 Note: Câu này đề cho B là đúng, nhưng thực tế Screen Flow cũng là lựa chọn tốt — cần đọc kỹ context về yêu cầu customization.

💡 **Mẹo ghi nhớ:**
> **Custom UI phức tạp + Service agent = Lightning Component**. Screen Flow tốt cho wizard đơn giản; LWC tốt cho UI cần logic phức tạp hơn.

---

## Câu 37

📌 **Đáp án đúng: A**

📝 **Bản dịch:**
Mỗi khi Opportunity được tạo, cần tạo một Task follow-up và assign cho Opportunity Owner.
Cách hiệu quả nhất để implement là gì?

✅ **Tại sao đúng:**
- **A đúng** vì **Record-triggered Flow trên Opportunity** là cách declarative, không cần code, và được trigger tự động khi Opportunity được tạo — hoàn toàn phù hợp và là best practice Salesforce hiện tại.

❌ **Tại sao sai:**
- **B sai** vì Apex trigger trên Task là sai object — Task chưa tồn tại để trigger. Hơn nữa, cần trigger trên Opportunity creation, không phải Task.
- **C sai** vì "Task actions" không phải thuật ngữ chuẩn Salesforce cho use case này.
- **D sai** vì "Auto-launched flow on Task" — flow trên Task, nhưng Task chưa tồn tại để launch flow; và cần fire khi Opportunity tạo, không phải Task tạo.

💡 **Mẹo ghi nhớ:**
> **"Khi A xảy ra, tạo B" = Record-triggered Flow trên A**. Nhớ: trigger đặt trên object gây ra hành động, không phải object được tạo ra!

---

## Câu 38

📌 **Đáp án đúng: A, B**

📝 **Bản dịch:**
Method `performSearch` nối trực tiếp `lastName` vào dynamic query — đây là lỗ hổng SOQL injection.
Hai cách nào để fix?

✅ **Tại sao đúng:**
- **A đúng** vì thay dynamic query bằng **static SOQL với bind variable**: `[SELECT Id,... FROM Contact WHERE LastName LIKE :searchPattern]` — Salesforce tự escape, không thể inject.
- **B đúng** vì dùng `String.escapeSingleQuotes(lastName)` để **sanitize input** trước khi đưa vào dynamic query — escape các ký tự đặc biệt.

❌ **Tại sao sai:**
- **C sai** vì `@ReadOnly` và `with sharing` liên quan đến data access control, không phải SOQL injection prevention. Chúng không sanitize input.
- **D sai** vì dùng **regex để remove special characters** có thể quá aggressive (loại bỏ các ký tự hợp lệ), không phải best practice — `escapeSingleQuotes()` là cách đúng hơn.

💡 **Mẹo ghi nhớ:**
> **Chống SOQL Injection = Bind Variable `:` hoặc `escapeSingleQuotes()`**. Hai vũ khí chính — nhớ cả hai!

---

## Câu 39

📌 **Đáp án đúng: B**

📝 **Bản dịch:**
Developer muốn cải thiện runtime performance của Apex calls bằng cách cache kết quả trên client.
Cách hiệu quả nhất là gì?

✅ **Tại sao đúng:**
- **B đúng** vì `@AuraEnabled(cacheable=true)` là annotation chính thức để enable **client-side caching** cho Apex method trong LWC/Aura. Khi được đánh dấu cacheable, Lightning framework sẽ cache kết quả trên client, tránh gọi server lần sau.

❌ **Tại sao sai:**
- **A sai** vì browser cookies là cơ chế cũ, không phải Salesforce best practice, và không tích hợp với Lightning data caching system.
- **C sai** vì `@AuraEnabled(storable=true)` — `storable` **không phải thuộc tính hợp lệ** của `@AuraEnabled`. Đây là tên bịa.
- **D sai** vì `setStorable()` là method của Aura framework (không phải LWC) và không phải cách tiêu chuẩn — `cacheable=true` trên server method là cách đúng.

💡 **Mẹo ghi nhớ:**
> **Cache trên client = `@AuraEnabled(cacheable=true)`**. Nhớ: **cacheable** (không phải storable, không phải cookie)!

---

## Câu 40

📌 **Đáp án đúng: D**

📝 **Bản dịch:**
Class `myClass` không có keyword `with sharing` hay `without sharing`. Method `myMethod` sẽ thực thi trong sharing context nào?

✅ **Tại sao đúng:**
- **D đúng** vì khi một class **không khai báo** `with sharing` hay `without sharing`, nó sẽ **kế thừa sharing context từ calling context** — tức là inherited sharing behavior. Nếu class gọi dùng `with sharing`, myClass cũng chạy với sharing.

❌ **Tại sao sai:**
- **A sai** vì "enforced by the instantiating class" không hoàn toàn đúng — class không khai báo sharing kế thừa từ calling context, không phải từ instantiating class cụ thể.
- **B sai** vì "sharing rules will NOT be enforced" — điều này đúng với `without sharing`, không phải với class không khai báo gì.
- **C sai** vì "sharing rules WILL be enforced" — điều này đúng với `with sharing`, không phải với class không khai báo gì.

💡 **Mẹo ghi nhớ:**
> **Không khai báo sharing = kế thừa từ caller**. Nhớ bảng: `with sharing` = enforce, `without sharing` = không enforce, **không khai báo = inherit từ context**!

---

## Câu 41

📌 **Đáp án đúng: A, C**

📝 **Bản dịch:**
Developer tạo LWC với Apex class. Khi nhấn nút Validate, Apex method chạy để thực hiện validation phức tạp.
Hai phần nào là **Controller** theo kiến trúc MVC?

✅ **Tại sao đúng:**
- **A đúng** vì **Apex class** là server-side controller — xử lý business logic, data access.
- **C đúng** vì **JavaScript file** là client-side controller — xử lý user interactions, gọi Apex, cập nhật UI state.
- Trong LWC MVC: **Model** = data/Apex, **View** = HTML, **Controller** = JS + Apex.

❌ **Tại sao sai:**
- **B sai** vì **HTML file** là **View** trong MVC — hiển thị data, không xử lý logic.
- **D sai** vì **XML file** (`js-meta.xml`) là **configuration/metadata**, không phải phần của MVC pattern.

💡 **Mẹo ghi nhớ:**
> **LWC MVC**: **View = HTML**, **Controller = JS + Apex**, **Model = Data/SObject**. Nhớ: **JS và Apex đều là Controller!**

---

## Câu 42

📌 **Đáp án đúng: A, C**

📝 **Bản dịch:**
Development team muốn dùng deployment script để tự động deploy lên sandbox.
Hai tool nào có thể dùng để chạy script deploy?

✅ **Tại sao đúng:**
- **A đúng** vì **SFDX CLI** (Salesforce DX CLI) là command-line tool chính thức, có thể dùng trong script để deploy (`sf project deploy start`), tích hợp vào CI/CD pipeline.
- **C đúng** vì **VS Code** với Salesforce Extension Pack cho phép deploy từ IDE và có thể kết hợp với tasks/scripts. Tuy nhiên VS Code dùng SFDX CLI bên dưới — nhưng đề vẫn tính là đúng.

❌ **Tại sao sai:**
- **B sai** vì **Change Sets** là manual process trong browser UI — không thể chạy trong script tự động.
- **D sai** vì **Developer Console** là web-based IDE trong Salesforce, không thể chạy trong deployment script.

💡 **Mẹo ghi nhớ:**
> **Automated deployment script = CLI-based tools**. SFDX CLI và VS Code (dùng CLI bên dưới) hỗ trợ scripting. Change Sets = manual, Developer Console = web UI.

---

## Câu 43

📌 **Đáp án đúng: A, B**

📝 **Bản dịch:**
Hai giới hạn nào của Agentforce developer cần cân nhắc khi xây dựng agent?

✅ **Tại sao đúng:**
- **A đúng** vì Agentforce custom actions tham chiếu đến Apex class hoặc Flow **chỉ hỗ trợ primitive data types** (String, Integer, Boolean, Decimal, Date) — không hỗ trợ complex objects, SObjects, hoặc custom classes.
- **B đúng** vì **Agent API có timeout 90 giây** — các action phức tạp cần hoàn thành trong 90 giây, nếu không sẽ bị timeout.

❌ **Tại sao sai:**
- **C sai** vì "inbound messages có character limits" — đây là limitation của messaging channels (SMS, WhatsApp), không phải limitation đặc thù của Agentforce agent building.
- **D sai** vì "version control is supported for agents" là statement ngược lại — **version control KHÔNG được hỗ trợ** đầy đủ cho Agentforce agents (đây sẽ là limitation, nhưng đề đánh D là "sai" vì phát biểu D nói supported = đúng, mà thực tế không fully supported).

💡 **Mẹo ghi nhớ:**
> **Agentforce limits**: **Primitive types only** cho Apex/Flow actions + **90-second timeout** cho Agent API. Nhớ hai con số: **primitive** và **90s**!

---

## Câu 44

📌 **Đáp án đúng: C**

📝 **Bản dịch:**
Class `DrawList` cần implement cả interface `Sortable` và `Drawable`.
Cú pháp Apex đúng là gì?

✅ **Tại sao đúng:**
- **C đúng** vì cú pháp đúng trong Apex để implement nhiều interface: `public class DrawList implements Sortable, Drawable { }` — dùng một từ khóa `implements` và liệt kê các interface cách nhau bằng dấu phẩy.

❌ **Tại sao sai:**
- **A sai** vì dùng `implements Sortable, implements Drawable` — **không được viết `implements` hai lần**. Chỉ cần một `implements` rồi liệt kê.
- **B sai** vì dùng `extends Sortable, Drawable` — `extends` dùng để **kế thừa class**, không dùng cho interface. Interface phải dùng `implements`. Hơn nữa Apex không hỗ trợ multiple inheritance qua `extends`.

💡 **Mẹo ghi nhớ:**
> **Interface = `implements`**, **Class kế thừa = `extends`**. Nhiều interface: `implements A, B` (một `implements`, nhiều tên cách nhau bằng dấu phẩy).

---

## Câu 45

📌 **Đáp án đúng: C**

📝 **Bản dịch:**
Flow tên "accountOnboarding" được tạo bằng Flow Builder và cần dùng trong Aura component.
Tag nào developer dùng để hiển thị flow trong component?

✅ **Tại sao đúng:**
- **C đúng** vì trong **Aura Component**, tag để embed flow là `<lightning:flow>` — đây là cú pháp namespace `lightning:` của Aura framework.

❌ **Tại sao sai:**
- **A sai** vì `lightning-flow` là cú pháp **LWC** (kebab-case), không phải Aura component (camelCase với colon).
- **B sai** vì `aura-flow` **không tồn tại** — đây là cú pháp bịa.
- **D sai** vì `aura:flow` **không tồn tại** — đây cũng là tên bịa.

💡 **Mẹo ghi nhớ:**
> **Aura = `lightning:componentName`** (colon), **LWC = `lightning-component-name`** (hyphen). Flow trong Aura = `<lightning:flow>`, Flow trong LWC = `<lightning-flow>`.

---

## Câu 46

📌 **Đáp án đúng: A**

📝 **Bản dịch:**
Phát biểu nào mô tả đúng thứ tự thực thi khi có nhiều trigger trên cùng một object và event?

✅ **Tại sao đúng:**
- **A đúng** vì **Salesforce không đảm bảo thứ tự thực thi** khi có nhiều trigger trên cùng object và event. Đây là lý do tại sao best practice là chỉ nên có **một trigger per object** (với handler class pattern).

❌ **Tại sao sai:**
- **B sai** vì "theo thứ tự modified" — Salesforce không đảm bảo điều này.
- **C sai** vì "theo thứ tự alphabetical" — Salesforce cũng không đảm bảo điều này.
- **D sai** vì "theo thứ tự created" — Salesforce cũng không đảm bảo điều này.

💡 **Mẹo ghi nhớ:**
> **Nhiều trigger = thứ tự KHÔNG đảm bảo!** Best practice: **"One Trigger Per Object"** để tránh vấn đề về thứ tự.

---

## Câu 47

📌 **Đáp án đúng: B**

📝 **Bản dịch:**
LWC có wired property `searchResults` lưu danh sách Opportunity. Apex method để wire phải định nghĩa như thế nào?

✅ **Tại sao đúng:**
- **B đúng** vì để wired property hoạt động:
  1. `@AuraEnabled(cacheable=true)` — **bắt buộc** để wire.
  2. `public static` — **bắt buộc** cho Apex method được gọi từ LWC.
  3. Trả về `List<Opportunity>` — đúng kiểu dữ liệu.

❌ **Tại sao sai:**
- **A sai** vì `cacheable=false` — `@wire` yêu cầu `cacheable=true`. Không có `cacheable=true` thì không wire được.
- **C sai** vì `cacheable=false` — tương tự A, không wire được.
- **D sai** vì `cacheable=true` nhưng thiếu `static` — Apex method được gọi từ LWC phải là `static`.

💡 **Mẹo ghi nhớ:**
> **`@wire` Apex method checklist**: ✅ `@AuraEnabled(cacheable=true)` ✅ `public static` ✅ return đúng type. Thiếu một trong ba = FAIL!

---

## Câu 48

📌 **Đáp án đúng: B**

📝 **Bản dịch:**
UC muốn setup CI để tự động chạy tests khi deploy code.
Development team nên dùng gì?

✅ **Tại sao đúng:**
- **B đúng** vì **Salesforce CLI** là công cụ command-line chính thức, có thể tích hợp vào CI/CD pipeline (Jenkins, GitHub Actions, etc.) để tự động chạy tests: `sf apex run test` hoặc `sf project deploy start --test-level RunLocalTests`.

❌ **Tại sao sai:**
- **A sai** vì VS Code là IDE, không phải CI tool — không thể chạy tự động trong pipeline không có người dùng.
- **C sai** vì Developer Console là web-based, không thể tích hợp vào automated CI pipeline.
- **D sai** vì **Force.com Toolkit đã bị deprecated** — không còn được Salesforce support.

💡 **Mẹo ghi nhớ:**
> **CI/CD automation = Salesforce CLI**. Nhớ: CLI = command-line = có thể script = có thể automate!

---

## Câu 49

📌 **Đáp án đúng: B**

📝 **Bản dịch:**
Custom object `Trainer__c` có lookup field đến `Gym__c`.
SOQL nào lấy record Viridian City Gym và tất cả Trainer của nó?

✅ **Tại sao đúng:**
- **B đúng** vì:
  1. Query từ **Gym__c** (parent) dùng **subquery** để lấy Trainers.
  2. Subquery dùng **relationship name**: `Trainers__r` — đây là **plural form** của `Trainer__c` với `__r` suffix dùng trong subquery từ parent.
  3. `WHERE Name = 'Viridian City Gym'` để lọc đúng Gym.

❌ **Tại sao sai:**
- **A sai** vì query từ `Trainer__c` WHERE `Gym__r.Name = ...` chỉ lấy trainers, không lấy Gym record.
- **C sai** vì `(SELECT Id FROM Trainer__c)` — trong subquery SOQL, phải dùng **relationship name** (`Trainers__r`), không dùng object API name (`Trainer__c`).
- **D sai** vì `(SELECT Id FROM Trainers__c)` — sai suffix. Phải là `Trainers__r` (relationship name dùng `__r`), không phải `__c`.

💡 **Mẹo ghi nhớ:**
> **Parent-to-child subquery dùng relationship name + `__r`**: `(SELECT Id FROM ChildObjects__r)`. Nhớ: **`__c` = object, `__r` = relationship**!

---

## Câu 50

📌 **Đáp án đúng: A**

📝 **Bản dịch:**
Developer nên dùng gì để fix LWC bug trong sandbox?

✅ **Tại sao đúng:**
- **A đúng** vì **VS Code** với Salesforce Extension Pack là công cụ chính thức và hiện đại nhất để develop và debug LWC — hỗ trợ syntax highlighting, local dev server, deploy, và debug LWC.

❌ **Tại sao sai:**
- **B sai** vì **Execute Anonymous** dùng để chạy Apex code, không thể dùng để debug/edit LWC.
- **C sai** vì **Developer Console** có hỗ trợ cơ bản nhưng **không được khuyến nghị** cho LWC development — Salesforce đã deprecate nhiều tính năng LWC trong Developer Console.
- **D sai** vì **Force.com IDE đã bị deprecated** hoàn toàn — không còn được support.

💡 **Mẹo ghi nhớ:**
> **LWC development = VS Code** (không phải Developer Console, không phải Force.com IDE). **"Modern LWC → VS Code!"**

---

## Câu 51

📌 **Đáp án đúng: A, B**

📝 **Bản dịch:**
Developer tạo custom exception `ParityException extends Exception`. Hai cách nào để throw exception này trong Apex?

✅ **Tại sao đúng:**
- **A đúng** vì `throw new ParityException('message')` — throw với constructor message, cú pháp đúng.
- **B đúng** vì `throw new ParityException()` — throw không có message, cú pháp đúng.
- Cả hai đều dùng từ khóa **`throw`** — bắt buộc để fire exception.

❌ **Tại sao sai:**
- **C sai** vì `new ParityException('message')` thiếu từ khóa `throw` — chỉ tạo object exception nhưng không throw nó, exception không được fire.
- **D sai** vì tương tự C — thiếu `throw`.

💡 **Mẹo ghi nhớ:**
> **Fire exception = `throw new ExceptionClass()`**. Không có `throw` thì chỉ là tạo object, không fire gì cả!

---

## Câu 52

📌 **Đáp án đúng: B, D**

📝 **Bản dịch:**
Hai đặc điểm nào đúng về Formula fields trong Salesforce?

✅ **Tại sao đúng:**
- **B đúng** vì Formula fields có thể tham chiếu đến fields trên **related objects** — đây gọi là **cross-object formula** (e.g., `Account.Name` từ Contact).
- **D đúng** vì Formula fields là **computed at runtime** — giá trị được tính khi record được load, **không được lưu trữ vật lý** trong database (không chiếm storage).

❌ **Tại sao sai:**
- **A sai** vì Formula fields **KHÔNG thể tự reference bản thân** (circular reference) — Salesforce sẽ báo lỗi nếu formula tham chiếu chính field đó.
- **C sai** vì nếu xóa hoặc sửa một field được dùng trong formula, Salesforce sẽ báo lỗi và **không cho phép** — phải chỉnh sửa formula trước.

💡 **Mẹo ghi nhớ:**
> **Formula = Cross-object ✅, Calculated at runtime ✅, Self-reference ❌, Delete dependency ❌**. Nhớ: **Formula là "tính toán lúc xem", không lưu DB!**

---

## Câu 53

📌 **Đáp án đúng: D**

📝 **Bản dịch:**
Sales management yêu cầu trường Lead Source phải có giá trị khi Lead được chuyển đổi (Convert).
Cần làm gì để đảm bảo user điền Lead Source trước khi convert?

✅ **Tại sao đúng:**
- **D đúng** vì **Validation Rule** là cách chính xác nhất — có thể check `ISBLANK(LeadSource)` và block khi user cố convert (convert cũng trigger validation rule). Hiển thị error message rõ ràng.

❌ **Tại sao sai:**
- **A sai** vì After trigger trên Lead chạy **sau khi** record đã saved, không thể block convert. Hơn nữa, trigger không tương tác tốt với Lead conversion flow.
- **B sai** vì Formula field là read-only, không thể enforce data entry.
- **C sai** vì **Lead Conversion Field Mapping** dùng để ánh xạ Lead fields sang Contact/Account/Opportunity khi convert — không dùng để enforce required field trước khi convert.

💡 **Mẹo ghi nhớ:**
> **Bắt buộc điền field trước khi action = Validation Rule**. Lead Conversion Mapping = ánh xạ dữ liệu SAU convert, không phải block TRƯỚC.

---

## Câu 54

📌 **Đáp án đúng: D**

📝 **Bản dịch:**
ISV Salesforce partner xây dựng managed package. Method `calculateBodyFat()` trong class `BodyFat` cần có thể truy cập bởi consumer bên ngoài package namespace.
Developer nên dùng gì?

✅ **Tại sao đúng:**
- **D đúng** vì trong **managed package**, để code có thể truy cập từ **bên ngoài package namespace**, cả **class và method** đều phải dùng **`global`** access modifier. `global` = accessible từ mọi nơi, kể cả bên ngoài namespace.

❌ **Tại sao sai:**
- **A sai** vì `public` trong managed package chỉ accessible trong **cùng namespace/package**, không accessible từ bên ngoài namespace.
- **B sai** vì nếu class là `public` (không phải `global`), method dù là `global` cũng không accessible từ bên ngoài — class phải là `global` trước.
- **C sai** vì tương tự B nhưng ngược lại — class `global` nhưng method `public` thì method vẫn không accessible từ bên ngoài namespace (method phải đồng cấp hoặc cao hơn visibility của class).

💡 **Mẹo ghi nhớ:**
> **Managed package + cross-namespace access = `global` cho CẢ class VÀ method**. Nhớ: **"Global = toàn cầu = bên ngoài được truy cập!"**

---

## Câu 55

📌 **Đáp án đúng: D**

📝 **Bản dịch:**
Câu lệnh Apex gán kết quả SOQL trực tiếp vào `Account myAccount = [SELECT...]`.
Chuyện gì xảy ra khi query trả về nhiều hơn một Account?

✅ **Tại sao đúng:**
- **D đúng** vì khi SOQL query gán vào một **single SObject variable** (không phải List) mà trả về nhiều records, Apex sẽ throw **`QueryException: List has more than 1 row for assignment to SObject`** — đây là **unhandled exception** nếu không có try/catch, và code sẽ terminate.

❌ **Tại sao sai:**
- **A sai** vì Apex **không tự động cast** sang List — sẽ throw exception ngay.
- **B sai** vì Apex **không lấy record đầu tiên** khi có nhiều results trong single-object assignment — đây là behavior của một số ngôn ngữ khác, không phải Apex.
- **C sai** vì lỗi không chỉ "write to debug log" — nó throw exception và terminate code.

💡 **Mẹo ghi nhớ:**
> **Single SObject assignment + nhiều results = `QueryException` thrown**! Luôn dùng `List<>` hoặc thêm `LIMIT 1` khi không chắc số lượng kết quả.

---

## Câu 56

📌 **Đáp án đúng: A**

📝 **Bản dịch:**
Developer viết Apex class với custom search functionality được gọi từ LWC. Cần đảm bảo chỉ hiển thị records mà user hiện tại có quyền truy cập.
Developer nên dùng gì?

✅ **Tại sao đúng:**
- **A đúng** vì `with sharing` **enforce sharing rules của running user** — Apex chỉ trả về records mà user có quyền xem theo sharing settings. Đây là cách đúng để đảm bảo record-level security.

❌ **Tại sao sai:**
- **B sai** vì `inherited sharing` kế thừa sharing context từ caller — nếu caller dùng `without sharing`, class vẫn không enforce sharing. Không đảm bảo chắc chắn sharing được enforce.
- **C sai** vì `without sharing` **bypass hoàn toàn** sharing rules — user có thể thấy tất cả records dù không có quyền.
- **D sai** vì `WITH SECURITY_ENFORCED` trong SOQL kiểm tra **field-level security** (FLS), không phải record-level sharing. Đây là hai khái niệm khác nhau.

💡 **Mẹo ghi nhớ:**
> **Record-level access = `with sharing`**. **Field-level access = `WITH SECURITY_ENFORCED`** hoặc `Security.stripInaccessible()`. Nhớ phân biệt hai loại!

---

## Câu 57

📌 **Đáp án đúng: A, D**

📝 **Bản dịch:**
Hai hành động nào có thể khiến trigger fire?

✅ **Tại sao đúng:**
- **A đúng** vì **Updates to FeedItem** (Chatter posts) có thể fire trigger nếu trigger được setup trên FeedItem object.
- **D đúng** vì **Changing a user's default division when transfer division option is checked** trigger update trên các records liên quan đến division — điều này có thể fire triggers trên những records bị update.

❌ **Tại sao sai:**
- **B sai** vì **Renaming or replacing a picklist entry** là **metadata change**, không phải data change — không fire triggers trên records.
- **C sai** vì **Cascading delete operations** (khi master bị xóa, child bị cascade delete) **KHÔNG fire** delete triggers trên child records — đây là hành vi đặc biệt của Salesforce để tránh governor limit.

💡 **Mẹo ghi nhớ:**
> **Cascading delete = KHÔNG fire trigger** trên child! **Picklist rename = metadata, không fire trigger**. Đây là hai điểm hay bị nhầm!

---

## Câu 58

📌 **Đáp án đúng: C**

📝 **Bản dịch:**
Developer dùng Agentforce Dev Assistant và nhận thấy output giống proprietary code.
Developer cần biết gì về model training khi dùng extension này?

✅ **Tại sao đúng:**
- **C đúng** vì AI/LLM models học từ training data — nếu output **giống proprietary code** thì đó là vì **code đó (hoặc code tương tự) đã được dùng để train model**. Đây là giải thích kỹ thuật đúng về behavior của LLM.

❌ **Tại sao sai:**
- **A sai** vì "reference prior prompts in near real time" — models không học từ prompts của user trong inference time (không có real-time training).
- **B sai** vì "reference other developers' code and train in near real time" — model không train in near real time từ code của developer khác.
- **D sai** vì "anonymized PII data" — không phải giải thích cho việc output giống code; hơn nữa, anonymization không liên quan đến code generation.

💡 **Mẹo ghi nhớ:**
> **AI output giống existing code = training data influence**. LLM không học real-time — nó phản ánh patterns từ **training data**.

---

## Câu 59

📌 **Đáp án đúng: B, C**

📝 **Bản dịch:**
Universal Containers muốn dùng **thuần declarative development** để xây dựng business logic layer.
Hai option nào có thể dùng?

✅ **Tại sao đúng:**
- **B đúng** vì **Validation Rules** là declarative tool — tạo bằng formula trong UI, không cần code, là phần của business logic layer (enforce data quality rules).
- **C đúng** vì **Record-Triggered Flow** là declarative automation tool mạnh nhất — xây bằng Flow Builder, không cần code, có thể implement complex business logic.

❌ **Tại sao sai:**
- **A sai** vì **Remote Actions** là Apex annotation (`@RemoteAction`) — cần viết code, không phải declarative.
- **D sai** vì **Batch Jobs** là Apex code (implement `Database.Batchable`) — cần viết code, không phải declarative.

💡 **Mẹo ghi nhớ:**
> **Declarative business logic = Validation Rules + Flow**. Remote Actions và Batch Jobs = **code** = không declarative!

---

## Câu 60

📌 **Đáp án đúng: A**

📝 **Bản dịch:**
Developer nhận lỗi khi compile đoạn code `switch on sobject` với `when Account a, Contact c` (hai SObject types trong một `when` block).
Lỗi là gì?

✅ **Tại sao đúng:**
- **A đúng** vì trong Apex `switch` statement trên SObject type, **mỗi `when` block chỉ được phép có MỘT SObject type** — không thể viết `when Account a, Contact c` trong cùng một block. Mỗi type phải có `when` block riêng.

❌ **Tại sao sai:**
- **B sai** vì "incompatible variable binding" không phải lỗi ở đây — vấn đề không phải type mismatch mà là số lượng SObject types trong một `when`.
- **C sai** vì "switch cannot contain multiple when values" không chính xác — `switch` **có thể** có nhiều `when` blocks, và `when` trên **integer/string** có thể có nhiều values (`when 1, 2, 3`). Nhưng với SObject type thì chỉ được một type per `when`.

💡 **Mẹo ghi nhớ:**
> **`switch on SObject`: mỗi `when` = CHỈ MỘT SObject type**. Ngược lại với `switch on Integer/String` có thể có nhiều values trong một `when`.

---

*Tài liệu này bổ sung giải thích tiếng Việt cho PD1 SET0 — 60 câu hỏi.*
