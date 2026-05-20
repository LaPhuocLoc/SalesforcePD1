### Question 1
Which two components are available to deploy using the Metadata API? (Choose two.)
- [x] **A.** Lead Conversion Settings  [CORRECT]
- [ ] **B.** Web-to-Case  [WRONG]
- [ ] **C.** Web-to-Lead  [WRONG]
- [x] **D.** Case Settings  [CORRECT]

**Explanation:**
> Web-to-Case and Web-to-Lead option are not available Metadata API​​​​​​​

---

### Question 2
A developer created a custom order management app that uses an Apex class. The order is represented by an Order object and an OrderItem object that has a master-detail relationship to Order. During order processing, an order may be split into multiple orders. What should a developer do to allow their code to move some existing OrderItem records to a new Order record?
- [x] **A.** Select the Allow reparenting option on the master-detail relationship.  [CORRECT]
- [ ] **B.** Change the master-detail relationship to an external lookup relationship.  [WRONG]
- [ ] **C.** Add without sharing to the Apex class declaration.  [WRONG]
- [ ] **D.** Create a junction object between OrderItem and Order.  [WRONG]

**Explanation:**
> "Allow reparenting" the developer enables the ability to change the parent of a child record (OrderItem) from one master record (Order) to another. This allows the developer to move certain OrderItem records to a new Order record, effectively splitting the order into multiple orders.

**Resources:**
> Considerations for Object Relationships

---

### Question 3
A developer is implementing an Apex class for a financial system. Within the class, the variables 'creditAmount' and 'debitAmount' should not be able to change once a value is assigned. In which two ways can the developer declare the variables to ensure their value can only be assigned one time? (Choose two.)
- [ ] **A.** Use the static keyword and assign its value in a static initializer.  [WRONG]
- [x] **B.** Use the final keyword and assign its value when declaring the variable.  [CORRECT]
- [x] **C.** Use the final keyword and assign its value in the class constructor.  [CORRECT]
- [ ] **D.** Use the static keyword and assign its value in the class constructor.  [WRONG]

**Explanation:**
> The variables 'creditAmount' and 'debitAmount' can only be assigned one time, the developer should use the 'final' keyword and assign their values when declaring the variables. This will make the variables constant and their values cannot be changed after assignment.

---

### Question 4
Which three web technologies can be integrated into a Visualforce page? (Choose three.)
- [x] **A.** JavaScript  [CORRECT]
- [x] **B.** CSS  [CORRECT]
- [ ] **C.** Java  [WRONG]
- [ ] **D.** PHP  [WRONG]
- [x] **E.** HTML  [CORRECT]

**Explanation:**
> You can't write any Java/Php code in VF page.
> https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/pages_intro_what_is_it.htm

---

### Question 5
Which is a valid Apex assignment?
- [ ] **A.** Integer x=5*1.0;  [WRONG]
- [ ] **B.** Integer x =5.0;  [WRONG]
- [x] **C.** Double x =5;  [CORRECT]
- [ ] **D.** Float x =5.0;  [WRONG]

**Explanation:**
> An Integer can be assigned to a Double, but a Double cannot be directly assigned to an Integer.

---

### Question 6
A developer completed modifications to a customized feature that is comprised of two elements: 1. Apex trigger 2. Trigger handler Apex class. What are two factors that the developer must take into account to properly deploy the modification to the production environment? (Choose two.)
- [x] **A.** Apex classes must have at least 75% code coverage org-wide.  [CORRECT]
- [x] **B.** At least one line of code must be executed for the Apex trigger.  [CORRECT]
- [ ] **C.** All methods in the test classes must use @isTest.  [WRONG]
- [ ] **D.** Test methods must be declared with the testMethod keyword.  [WRONG]

**Explanation:**
> To deploy your code to production environments, it is mandatory to achieve a minimum of 75% code coverage for your Apex through unit tests. Additionally, all triggers must have at least one line of test coverage.

**Resources:**
> Instructions to test Apex code

---

### Question 7
How many levels of child records can be returned in a single SOQL query from one parent object?
- [ ] **A.** 1  [WRONG]
- [ ] **B.** 3  [WRONG]
- [x] **C.** 5  [CORRECT]
- [ ] **D.** 7  [WRONG]

**Explanation:**
> Query Five Levels of Parent-to-Child Relationships in SOQL Queries
> https://help.salesforce.com/s/articleView?id=release-notes.rn_api_soql_5level.htm&release=244&type=5

---

### Question 8
When an Account's custom picklist field called Customer Sentiment is changed to a value of 'Confused', a new related Case should automatically be created. Which two methods should a developer use to create this case? (Choose two.)
- [x] **A.** Process Builder  [CORRECT]
- [x] **B.** Apex Trigger  [CORRECT]
- [ ] **C.** Custom Button  [WRONG]
- [ ] **D.** Workflow Rule  [WRONG]

**Explanation:**
> 1. Apex Trigger: The developer can write an Apex trigger on the Account object to detect changes in the Customer Sentiment picklist field. When the picklist field value changes to 'Confused,' the trigger can create a new Case record and establish the necessary relationship between the Account and the Case.
> 2. Process Builder: The developer can use Process Builder, a declarative automation tool in Salesforce, to create the automation flow. The process builder can be configured to monitor changes on the Account object and specifically check for the Customer Sentiment picklist field value change to 'Confused.' When the condition is met, the process builder can take action to create a new related Case record.

---

### Question 9
Which statement results in an Apex compiler error?
- [ ] **A.** Map<Id, Lead> lmap = new Map<Id, Lead>([Select ID from Lead Limit 8]);  [WRONG]
- [ ] **B.** Date d1 = Date.Today(), d2 = Date.ValueOf('2018-01-01');  [WRONG]
- [ ] **C.** Integer a=5, b=6, c, d = 7;  [WRONG]
- [x] **D.** List<string> s = List<string>{'a','b','c'};  [CORRECT]

**Explanation:**
> D is not correct because of the missing new operator
> List<string> s = new List<string>{'a','b','c'};

---

### Question 10
A developer has a Visualforce page and custom controller to save Account records. The developer wants to display any validation rule violations to the user. How can the developer make sure that validation rule violations are displayed?
- [ ] **A.** Add custom controller attributes to display the message.  [WRONG]
- [ ] **B.** Use a try/catch with a custom exception class.  [WRONG]
- [x] **C.** Include<apex:messages>on the Visualforce page.  [CORRECT]
- [ ] **D.** Perform the DML using the Database.upsert() method.  [WRONG]

**Explanation:**
> Display Errors on the Visualforce Page: In the Visualforce page, utilize the Visualforce markup and Apex expressions to iterate over the error messages collection and display them to the user. This can be achieved using components like <apex:pageMessages> or by manually rendering error messages using <apex:outputPanel> and <apex:repeat>.

---

### Question 11
A developer encounters APEX heap limit errors in a trigger. Which two methods should the developer use to avoid this error? (Choose two.)
- [ ] **A.** Use the transient keyword when declaring variables.  [WRONG]
- [ ] **B.** Query and store fields from the related object in a collection when updating related objects.  [WRONG]
- [x] **C.** Remove or set collections to null after use.  [CORRECT]
- [x] **D.** Use SOQL for loops instead of assigning large queries results to a single collection and looping through the collection.  [CORRECT]

**Explanation:**
> Use the transient keyword to declare instance variables that can't be saved, and shouldn't be transmitted as part of the view state for a Visualforce page -> For VF 'heap' limit.
> Reduce heap size during runtime by removing items from the collection as you iterate over it.
> To avoid heap size limits, developers should always use a SOQL "for" loop to process query results that return many records.

**Resources:**
> Build better apex scripts to manage heap limits
> SOQL For Loops

---

### Question 12
Which two are phases in the Salesforce Application Event propagation framework? (Choose two.)
- [x] **A.** Bubble  [CORRECT]
- [x] **B.** Default  [CORRECT]
- [ ] **C.** Control  [WRONG]
- [ ] **D.** Emit  [WRONG]

**Explanation:**
> Here is the sequence of application event propagation.
> 1. Event fired—An application event is fired. The component that fires the event is known as the source component.
> 2. Capture phase—The framework executes the capture phase from the application root to the source component until all components are traversed. Any handling event can stop propagation by calling stopPropagation() on the event.
> 3. Bubble phase—The framework executes the bubble phase from the source component to the application root until all components are traversed or stopPropagation() is called.
> 4. Default phase—The framework executes the default phase from the root node unless preventDefault() was called in the capture or bubble phases. If the event’s propagation wasn’t stopped in a previous phase, the root node defaults to the application root. If the event’s propagation was stopped in a previous phase, the root node is set to the component whose handler invoked event.stopPropagation().

**Resources:**
> Application Event Propagation

---

### Question 13
A custom object Trainer__c has a lookup field to another custom object Gym__c. Which SOQL query will get the record for the Viridian City Gym and all its trainers?
- [ ] **A.** SELECT ID FROM Trainer__c WHERE Gym__r.Name = 'Viridian City Gym'  [WRONG]
- [ ] **B.** SELECT Id, (SELECT Id FROM Trainers__c) FROM Gym__c WHERE Name = 'Viridian City Gym'  [WRONG]
- [ ] **C.** SELECT Id, (SELECT Id FROM Trainer__c) FROM Gym__c WHERE Name = 'Viridian City Gym'  [WRONG]
- [x] **D.** SELECT Id, (SELECT Id FROM Trainers__r) FROM Gym__c WHERE Name = 'Viridian City Gym'  [CORRECT]

---

### Question 14
A developer needs to create an audit trail for records that are sent to the recycle bin. Which type of trigger is most appropriate to create?
- [x] **A.** after delete  [CORRECT]
- [ ] **B.** after undelete  [WRONG]
- [ ] **C.** before undelete  [WRONG]
- [ ] **D.** before delete  [WRONG]

**Resources:**
> Triggers

---

### Question 15
Where are two locations a developer can look to find information about the status of asynchronous or future calls? (Choose two.)
- [ ] **A.** Time-Based Workflow Monitor  [WRONG]
- [x] **B.** Apex Flex Queue  [CORRECT]
- [x] **C.** Apex Jobs  [CORRECT]
- [ ] **D.** Paused Flow Interviews component  [WRONG]

**Explanation:**
> AsyncApexJob Object: The AsyncApexJob object represents the status of asynchronous Apex jobs, which include future calls, batch Apex jobs, and scheduled Apex jobs.
> Apex Flex Queue is where a developer can find information about the status of asynchronous or future calls in Salesforce. The Apex Flex Queue is a mechanism introduced to manage the execution of asynchronous Apex jobs when there is a large backlog.

---

### Question 16
Given the code below:
public class AccountListController {
public List<Account> getAccounts() {
return controller.getRecords();
}
}
which three statements can be used to create the controller variable? (Choose three.)
- [x] **A.** ApexPages.StandardsetController controller = new Apexpages.StandardsetController(Database.query('SELECT Id FROM Account'));  [CORRECT]
- [x] **B.** ApexPages.StandardsetController controller = new Apexpages.StandardsetController(Database.getQueryLocator('SELECT Id FROM Account'));  [CORRECT]
- [ ] **C.** ApexPages.StandardController controller = new Apexpages.StandardController(Database.getQueryLocator('SELECT Id FROM Account'));  [WRONG]
- [ ] **D.** ApexPages.StandardController controller = new Apexpages.StandardController([SELECT Id FROM Account]);  [WRONG]
- [x] **E.** ApexPages.StandardsetController controller = new Apexpages.StandardsetController(Database.getQueryLocator([SELECT Id FROM Account]);  [CORRECT]

**Explanation:**
> The StandardController has getRecord() not getRecords().

**Resources:**
> StandardSetController Class
> StandardController Class

---

### Question 17
Given: Map<ID, Account> accountMap = new Map<ID, Account> ([SELECT Id, Name FROM Account]); What are three valid Apex loop structures for iterating through items in the collection? (Choose three.)
- [ ] **A.** for (ID accountID : accountMap.keySet()) { }  [WRONG]
- [x] **B.** for (Account accountRecord : accountMap.values()) { }  [CORRECT]
- [x] **C.** for (Integer i = 0; i < accountMap.size(); i++) { }  [CORRECT]
- [ ] **D.** for (ID accountID : accountMap) { }  [WRONG]
- [ ] **E.** for (Account accountRecord : accountMap.keySet()) { }  [WRONG]

**Explanation:**
> Problem:
> D: Loop must iterate over collection: Map<Id,Account>
> E: Invalid loop variable type expected Id was Account.

---

### Question 18
What is the order of operations when a record is saved in Salesforce?
- [ ] **A.** workflow, process flows, triggers, commit  [WRONG]
- [ ] **B.** process flows, triggers, workflow, commit  [WRONG]
- [x] **C.** triggers, workflow, process flows, commit  [CORRECT]
- [ ] **D.** workflow, triggers, process flows, commit  [WRONG]

**Explanation:**
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

---

### Question 19
Which three options can be accomplished with formula fields? (Choose three.)
- [x] **A.** Generate a link using the HYPERLINK function to a specific record.  [CORRECT]
- [ ] **B.** Display the previous value for a field using the PRIORVALUE function.  [WRONG]
- [x] **C.** Determine if a datetime field value has passed using the NOW function.  [CORRECT]
- [ ] **D.** Return and display a field value from another object using the VLOOKUP function.  [WRONG]
- [x] **E.** Determine which of three different images to display using the IF function.  [CORRECT]

**Resources:**
> Examples of Advanced Formula Fields

---

### Question 20
A developer is tasked to perform a security review of the ContactSearch Apex class that exists in the system. Within the class, the developer identifies the following method as a security threat:
List<Contact> performSearch(String lastName) {
return Database.query('SELECT Id, FirstName, LastName FROM Contact WHERE Lastname like %'+lastName+'%');
}
What are two ways the developer can update the method to prevent a SOQL injection attack? (Choose two.)
- [ ] **A.** Use the @ReadOnly annotation and the with sharing keyword on the class.  [WRONG]
- [x] **B.** Use the escapeSingleQuotes method to sanitize the parameter before its use.  [CORRECT]
- [ ] **C.** Use a regular expression expression on the parameter to remove special characters.  [WRONG]
- [x] **D.** Use variable binding and replace the dynamic query with a static SOQL.  [CORRECT]

---

### Question 21
A developer writes the following code:
List<Account> acc = [Select Id From Account Limit 10];
Delete acc;
Database.emptyRecyclebin(acc);
System.Debug(Limits.getDMLStatements() +', ' + Limits.getLimitDMLStatements());
What is the result of the debug statement?
- [ ] **A.** 1, 100  [WRONG]
- [ ] **B.** 1, 150  [WRONG]
- [x] **C.** 2, 150  [CORRECT]
- [ ] **D.** 2, 200  [WRONG]

**Explanation:**
> getDMLStatements() Returns the number of DML statements (such as insert, update or the database.EmptyRecycleBin method) that have been called.
> getLimitDMLStatements() Returns the total number of DML statements or the database.EmptyRecycleBin methods that can be called.

**Resources:**
> Limits Class
> Execution Governors and Limits

---

### Question 22
Which approach should a developer take to automatically add a 'Maintenance Plan' to each Opportunity that includes an 'Annual Subscription' when an opportunity is closed?
- [ ] **A.** Build a OpportunityLineItem trigger that adds a PriceBookEntry record.  [WRONG]
- [ ] **B.** Build an OpportunityLineItem trigger to add an OpportunityLineItem record.  [WRONG]
- [ ] **C.** Build an Opportunity trigger that adds a PriceBookEntry record.  [WRONG]
- [x] **D.** Build an Opportunity trigger that adds an OpportunityLineItem record.  [CORRECT]

**Explanation:**
> Write an Apex trigger on the Opportunity object that fires when an Opportunity is closed.

---

### Question 23
Which action may cause triggers to fire?
- [ ] **A.** Renaming or replacing a picklist entry  [WRONG]
- [x] **B.** Updates to Feed Items  [CORRECT]
- [ ] **C.** Cascading delete operations  [WRONG]
- [ ] **D.** Changing a user's default division when the transfer division option is checked  [WRONG]
Explanation
Record Update: When an existing record is updated, triggers associated with the object can fire. This includes both before and after update triggers.

---

### Question 24
Management asked for opportunities to be automatically created for accounts with annual revenue greater than $1,000,000. A developer created the following trigger on the Account object to satisfy this requirement.
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
Which two actions should the developer take to fix the code segment shown above? (Choose two.)
- [ ] **A.** Check if all the required fields for Opportunity are being added on creation.  [WRONG]
- [ ] **B.** Use Database.query to query the opportunities.  [WRONG]
- [x] **C.** Move the DML that saves opportunities outside the for loop.  [CORRECT]
- [x] **D.** Query for existing opportunities outside the for loop.  [CORRECT]

**Explanation:**
> The two actions the developer should take to fix the code segment are:
> 1. Move the DML that saves opportunities outside of the for loop.
> 2. Query for existing opportunities outside of the for loop.

---

### Question 25
An org has a data model with a Buyer__c object that has a lookup relationship to Region__c and a Supplier__c object has a lookup relationship to Region___c. How can a developer display data from the related Supplier__c records on a Visualforce page that has a standard controller for the Buyer__c object?
- [ ] **A.** Use rollup formula fields on the Buyer__c object to reference the related Supplier__c records through the Region__c.  [WRONG]
- [x] **B.** Use SOQL in a controller extension to query for related Supplier__c records.  [CORRECT]
- [ ] **C.** Use a second standard controller for the Region__c object on a page to display the related Supplier__c records.  [WRONG]
- [ ] **D.** Use merge field syntax to retrieve the Supplier__c records related to the Buyer__c record through the Region__c.  [WRONG]

**Explanation:**
> 1. Create a Custom Controller Extension: Create a custom Apex controller extension for the Visualforce page. The controller extension allows you to add custom logic to the standard controller's functionality.
> 2. Query Related Supplier__c Records: In the custom controller extension, use a SOQL query to retrieve the Supplier__c records related to the Buyer__c record being displayed on the Visualforce page. This can be achieved by using the Buyer__c object's lookup relationship field (e.g., Region__c) to traverse to the related Supplier__c records.

---

### Question 26
A developer is asked to create a custom Visualforce page that will be used as a dashboard component. Which three are valid controller options for this page? (Choose three.)
- [ ] **A.** Use a standard controller.  [WRONG]
- [ ] **B.** Use a standard controller with extensions.  [WRONG]
- [x] **C.** Use a custom controller with extensions.  [CORRECT]
- [x] **D.** Do not specify a controller.  [CORRECT]
- [x] **E.** Use a custom controller.  [CORRECT]

**Resources:**
> Create Visualforce Dashboard Components

---

### Question 27
Universal Hiring is using Salesforce to capture job applications. A salesforce administrator created two custom objects: Job__c acting as the master object, Job_Application__c acting as the detail. Within the Job__c object, a custom multi-select picklist, Preferred_Locations__c, contains a list of approved states for the position. Each Job_Application__c record relates to a Contact within the system through a master-detail relationship. 	Recruiters have requested the ability to view whether the Contact's Mailing State value matches a value selected on the Preferred_Locations__c field, within the Job_Application__c record. Recruiters would like this value to be kept in sync, if changes occur to the Contact's Mailing State or if the Job's Preferred_Locations__c field is updated. What is the recommended tool a developer should use to meet the business requirement?
- [ ] **A.** Apex Trigger  [WRONG]
- [ ] **B.** Process Builder  [WRONG]
- [x] **C.** Record-triggered flow  [CORRECT]
- [ ] **D.** Formula field  [WRONG]

---

### Question 28
A developer declared a class as follows.
public class wysiwyg {
//properties and methods including DML
}
Which invocation of a class method will obey the organization-wide defaults and sharing settings for the running user in the Salesforce organization?
- [ ] **A.** An Apex trigger that invokes a helper method in this class  [WRONG]
- [x] **B.** A developer using the Developer Console that invokes a method in this class from the execute anonymous window  [CORRECT]
- [ ] **C.** A Visualforce page with an Apex controller that invokes a method in this class  [WRONG]
- [ ] **D.** A user on an external system that has an API call into Salesforce that invokes a method in this class  [WRONG]

---

### Question 29
Universal Containers uses a simple Order Management app. On the Order Lines, the order line total is calculated by multiplying the item price with the quantity ordered. There is a Master-Detail relationship between the Order and the Order Lines object. What is the best practice to get the sum of all order line totals on the order header?
- [ ] **A.** Declarative Roll-Up Summaries App  [WRONG]
- [x] **B.** Roll-Up Summary field  [CORRECT]
- [ ] **C.** Process Builder  [WRONG]
- [ ] **D.** Apex Trigger  [WRONG]

**Explanation:**
> Roll-Up Summary Fields are a powerful feature in Salesforce that allow you to calculate and display aggregate values (such as sum, count, max, min, etc.) from child records on a parent record. In this case, you can create a Roll-Up Summary Field on the Order object to calculate the total order amount by summing up the order line totals from all related Order Line records.

---

### Question 30
Given the following Apex statement: Account myAccount = [SELECT Id, Name FROM Account]; What occurs when more than one Account is returned by the SOQL query?
- [ ] **A.** The variable, myAccount, is automatically cast to the List data type.  [WRONG]
- [ ] **B.** The first Account returned is assigned to myAccount.  [WRONG]
- [ ] **C.** The query fails and an error is written to the debug log.  [WRONG]
- [x] **D.** An unhandled exception is thrown and the code terminates.  [CORRECT]

**Explanation:**
> When the query returns multiple records (multiple Accounts in this case), Salesforce will raise a QueryException because you cannot assign a list of records to a single record variable.

---

### Question 31
Which two statements are true about Apex code executed in Anonymous Blocks? (Choose two.)
- [ ] **A.** The code runs with the permissions of the user specified in the runAs() statement.  [WRONG]
- [x] **B.** The code runs with the permissions of the logged in user.  [CORRECT]
- [ ] **C.** The code runs in system mode having access to all objects and fields.  [WRONG]
- [ ] **D.** All DML operations are automatically rolled back.  [WRONG]
- [x] **E.** Successful DML operations are automatically committed.  [CORRECT]

**Explanation:**
> Limited Access to Data: Anonymous Blocks have access only to data that the running user has permission to view. They don't have access to data that requires higher permissions, such as records with "View All" or "Modify All" permission.
> Data Changes are Committed: Any data changes made within an Anonymous Block are committed to the database and cannot be rolled back. Unlike unit tests, which perform a full rollback after execution, data changes made in Anonymous Blocks are permanent. This means that if you modify records or data in the Anonymous Block, those changes will be saved to the database.

---

### Question 32
Using DescribeSObjectResult, which Apex method can a developer use to determine if the current user can edit records for an object?
- [ ] **A.** canUpdate()  [WRONG]
- [ ] **B.** canEdit()  [WRONG]
- [x] **C.** isUpdateable()  [CORRECT]
- [ ] **D.** isEditable()  [WRONG]

**Explanation:**
> Developer can use the isUpdateable() method. This method allows you to check if the current user has the necessary permissions to edit records of a specific object.

---

### Question 33
Given the code below:
Public class Mycontroller {
private Integer recordCount;
}
what can be done so that recordCount can be accessed by a test class, but not by a non-test class?
- [ ] **A.** Change recordCount from private to public.  [WRONG]
- [ ] **B.** Add the SeeAllData annotation to the test class.  [WRONG]
- [x] **C.** Add the TestVisible annotation to recordCount.  [CORRECT]
- [ ] **D.** Add the TestVisible annotation to the MyController class.  [WRONG]

**Explanation:**
> The TestVisible annotation allows test classes to access private or protected members of a class.

---

### Question 34
Which two number expressions evaluate correctly? (Choose two.)
- [x] **A.** Double d = 3.14159;  [CORRECT]
- [ ] **B.** Integer I = 3.14159;  [WRONG]
- [x] **C.** Decimal d = 3.14159;  [CORRECT]
- [ ] **D.** Long l = 3.14159;  [WRONG]

**Explanation:**
> A. Double d = 3.14159;: This expression is correct because 3.14159 is a floating-point literal, and it can be assigned to a variable of type Double
> C. Decimal d = 3.14159;: This expression is correct because 3.14159 is a floating-point literal, and it can be assigned to a variable of type Decimal

---

### Question 35
Assuming that name is a String obtained by an a Visualforce page.
which two SOQL Queries performed are safe from SOQL injection? (Choose two.)
- [x] **A.** List<Account> results = [SELECT Id FROM Account WHERE Name LIKE :query];  [CORRECT]
- [ ] **B.** String query = 'SELECT Id FROM Account WHERE Name LIKE \'%' + name.noQuotes()+ '%\''; List<Account> results = Database.query(query);  [WRONG]
- [x] **C.** String query = 'SELECT Id FROM Account WHERE Name LIKE \'%' + string.escapeSingleQuotes(name) + '%\'';  List<Account> results = Database.query(query);  [CORRECT]
- [ ] **D.** String query = 'SELECT Id FROM Account WHERE Name LIKE \'% + name + '%\'';  List<Account> results = Database.query(query);  [WRONG]

**Explanation:**
> A: Uses Apex binding to dynamically insert the value of the 'name' variable into the SOQL query. This approach ensures that the input is properly sanitized and prevents any malicious injection of SOQL queries.
> C: Uses the 'string.escapeSingleQuotes()' method to properly escape any single quotes in the 'name' variable before inserting it into the query. This prevents the injection of malicious queries and ensures the query's integrity.

---

### Question 36
A developer must create a ShippingCalculator class that cannot be instantiated and must include a working default implementation of a calculate method, that sub-classes can override. What is the correct implementation of the ShippingCalculator class?
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
}

**Explanation:**
> To create a ShippingCalculator class that cannot be instantiated and includes a default implementation of a calculate method that sub-classes can override, you can use the abstract keyword for the class and the virtual keyword for the calculate method.

---

### Question 37
Given the following Anonymous block:
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
What should a developer consider for an environment that has over 10,000 Case records?
- [ ] **A.** The try-catch block will handle exceptions thrown by governor limits.  [WRONG]
- [x] **B.** The transaction will fall due to exceeding the governor limit.  [CORRECT]
- [ ] **C.** The transaction will succeed and changes will be committed.  [WRONG]
- [ ] **D.** The try-catch block will handle any DML exceptions thrown.  [WRONG]

**Explanation:**
> If there are more than 10,000 Case records in the environment, the code may hit the DML row limit and result in a "Too many DML rows: 10001" exception.

---

### Question 38
Which process automation should be used to send an outbound message without using Apex code?
- [ ] **A.** Flow Builder  [WRONG]
- [ ] **B.** Process Builder  [WRONG]
- [x] **C.** Workflow Rule  [CORRECT]
- [ ] **D.** Approval Process  [WRONG]

**Explanation:**
> You can use the Workflow Outbound Message process automation in Salesforce to send an outbound message without using Apex code.

---

### Question 39
A developer has an Apex controller for a Visualforce page that takes an ID as a URL parameter. How should the developer prevent a cross site scripting vulnerability?
- [ ] **A.** ApexPages.currentPage().getParameters().get('url_param')  [WRONG]
- [x] **B.** String.escapeSingleQuotes(ApexPages.currentPage().getParameters().get('url_param'))  [CORRECT]
- [ ] **C.** String.ValueOf(ApexPages.currentPage().getParameters().get('url_param'))  [WRONG]
- [ ] **D.** ApexPages.currentPage().getParameters().get('url_param').escapeHtml4()  [WRONG]

**Explanation:**
> This option is the correct approach to prevent XSS vulnerabilities. The String.escapeSingleQuotes() method escapes any single quotes (') in the parameter value, making it safe for further use in Apex code and preventing potential script injection.

---

### Question 40
A Visual Flow uses an Apex Action to provide additional information about multiple Contacts, stored in a custom class, ContactInfo. Which is the correct definition of the Apex method that gets the additional information?
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
public static List<ContactInfo> getInfo(List<Contact> contactIds) { /*implementation*/ }

**Explanation:**
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

---

### Question 41
Which aspect of Apex programming is limited due to multitenancy?
- [ ] **A.** The number of methods in an Apex class  [WRONG]
- [x] **B.** The number of records returned from database queries  [CORRECT]
- [ ] **C.** The number of active Apex classes  [WRONG]
- [ ] **D.** The number of records processed in a loop  [WRONG]

**Explanation:**
> The number of records returned from database queries is limited due to multitenancy in Salesforce. Salesforce enforces governor limits to prevent queries from returning an excessive number of records, which could impact the performance and stability of the platform for other users.

---

### Question 42
A developer is migrating a Visualforce page into a Lightning web component. The Visualforce page shows information about a single record. The developer decides to use Lightning Data Service to access record data. Which security consideration should the developer be aware of?
- [ ] **A.** The with sharing keyword must be used to enforce sharing rules.  [WRONG]
- [x] **B.** Lightning Data Service handles sharing rules and field-level security.  [CORRECT]
- [ ] **C.** The isAccessible() method must be used for field-level access checks.  [WRONG]
- [ ] **D.** Lightning Data Service ignores field-level security.  [WRONG]

**Explanation:**
> Check CRUD and FLS: Before accessing the record data through LDS, check whether the current user has the necessary CRUD permissions for the object and whether they have FLS permissions for the specific fields you are accessing. You can use Apex's Schema classes to check FLS for fields.

---

### Question 43
Which approach should a developer use to add pagination to a Visualforce page?
- [ ] **A.** A StandardController  [WRONG]
- [ ] **B.** The Action attribute for a page  [WRONG]
- [ ] **C.** The extensions attribute for a page  [WRONG]
- [x] **D.** A StandardSetController  [CORRECT]

**Explanation:**
> Use StandardSetController: The StandardSetController is a built-in Apex class that provides pagination functionality for displaying sets of records in Visualforce pages. It allows developers to easily implement pagination with minimal code.

---

### Question 44
Which message is logged by the code below?
- [ ] **A.** Generic Exception  [WRONG]
- [ ] **B.** List Exception  [WRONG]
- [x] **C.** NullPointer Exception  [CORRECT]
- [ ] **D.** No message is logged.  [WRONG]

---

### Question 45
Universal Containers implemented a private sharing model for the Account object. A custom Account search tool was developed with Apex to help sales representatives find accounts that match multiple criteria they specify. Since its release, users of the tool report they can see Accounts they do not own. What should the developer use to enforce sharing permissions for the currently logged-in user while using the custom search tool?
- [ ] **A.** Use the schema describe calls to determine if the logged-in user has access to the Account object.  [WRONG]
- [ ] **B.** Use the UserInfo Apex class to filter all SOQL queries to returned records owned by the logged-in user.  [WRONG]
- [x] **C.** Use the with sharing keyword on the class declaration.  [CORRECT]
- [ ] **D.** Use the without sharing keyword on the class declaration.  [WRONG]

**Explanation:**
> To enforce sharing permissions for the currently logged-in user while using the custom search tool, the developer should use the with sharing keyword in the Apex class that backs the search tool.

---

### Question 46
What are two ways that a controller and extension can be specified for a custom object named “Notice” on a Visualforce page? (Choose two.)
- [x] **A.** apex:page standardController=”Notice__c” extensions=”myControllerExtension”  [CORRECT]
- [ ] **B.** apex:page=Notice extends=”myControllerExtension”  [WRONG]
- [x] **C.** apex:page controller=”Notice__c” extensions=”myControllerExtension”  [CORRECT]
- [ ] **D.** apex:page controllers=”Notice__c, myControllerExtension”  [WRONG]

**Explanation:**
> Controller Attribute: You can specify the controller for the Visualforce page using the controller attribute in the <apex:page> tag.
> Extension Attribute: You can specify an extension for the Visualforce page using the extensions attribute in the <apex:page> tag.

---

### Question 47
A developer creates a custom controller and custom Visualforce page by using the code block below.
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
What can the user expect to see when accessing the custom page?
- [ ] **A.** a, b, b  [WRONG]
- [ ] **B.** a, b, getMyString  [WRONG]
- [x] **C.** a, a, a  [CORRECT]
- [ ] **D.** b, a, getMyString  [WRONG]

**Explanation:**
> The code block initializes myString as 'a' if it is null, so all three occurrences of {!myString} will display 'a' when accessed on the custom page.

---

### Question 48
Given the following trigger implementation:
trigger leadTrigger on Lead (before update) {
final ID BUSINESS_RECORDTYPEID = '012500000009Qad';
for (Lead thisLead : Trigger.new) {
if (thisLead.Company != null thisLead.RecordTypeld != BUSINESS_RECORDTYPEID) {
thisLead.RecordTypeld = BUSINESS_RECORDTYPEID;
}
}
}
The developer receives deployment errors every time a deployment is attempted from a sandbox to Production.
What should the developer do to ensure a successful deployment?
- [x] **A.** Ensure a record type with an ID of BUSINESS_RECORDTYPEID exists on Production prior to deployment.  [CORRECT]
- [ ] **B.** Ensure BUSINESS_RECORDTYPEID is pushed as part of the deployment components.  [WRONG]
- [ ] **C.** Ensure BUSINESS_RECORDTYPEID is retrieved using Schema.Describe calls.  [WRONG]
- [ ] **D.** Ensure the deployment is validated by a System Admin user on Production.  [WRONG]

**Explanation:**
> The ID of a record type can vary between different environments (e.g., sandbox and production).
> -> Ensure a record type with an ID of BUSINESS_RECORDTYPEID exists on Production prior to deployment.

---

### Question 49
Which two settings must be defined in order to update a record of a junction object? (Choose two.)
- [ ] **A.** Read/Write access on the junction object  [WRONG]
- [ ] **B.** Read access on the primary relationship  [WRONG]
- [x] **C.** Read/Write access on the primary relationship  [CORRECT]
- [x] **D.** Read/Write access on the secondary relationship  [CORRECT]

**Explanation:**
> Junction Object is child and will get access settings from Primary Object.

---

### Question 50
Which tag should a developer include when styling from external CSS is required in a Visualforce page?
- [ ] **A.** apex:includeStyles  [WRONG]
- [ ] **B.** apex:includeScript  [WRONG]
- [ ] **C.** apex:require  [WRONG]
- [x] **D.** apex:stylesheet  [CORRECT]

**Explanation:**
> To include external CSS styling in a Visualforce page, a developer should use the <apex:stylesheet> tag. The <apex:stylesheet> tag is used to reference an external CSS file and apply the specified styles to the Visualforce page.

---

### Question 51
Which declarative process automation feature supports iterating over multiple records?
- [ ] **A.** Workflow rules  [WRONG]
- [x] **B.** Flows  [CORRECT]
- [ ] **C.** Validation rules  [WRONG]
- [ ] **D.** Approval processes  [WRONG]

**Explanation:**
> Flows is a powerful tool in Salesforce that allows administrators and developers to create automated processes with a point-and-click interface. One of its key functionalities is the ability to define actions that iterate over multiple records at once.

---

### Question 52
The Account object in an organization has a master detail relationship to a child object called Branch. The following automations exist: Rollup summary fields Custom validation rules Duplicate rules A developer created a trigger on the Account object. What two things should the developer consider while testing the trigger code? (Choose two.)
- [x] **A.** The trigger may fire multiple times during a transaction.  [CORRECT]
- [x] **B.** Rollup summary fields can cause the parent record to go through Save.  [CORRECT]
- [ ] **C.** Duplicate rules are executed once all DML operations commit to the database.  [WRONG]
- [ ] **D.** The validation rules will cause the trigger to fire again.  [WRONG]

**Explanation:**
> The trigger may fire multiple times during a transaction: Triggers in Salesforce can fire multiple times during a single transaction. This can happen due to workflow updates, record updates in triggers, or any other recursive actions.
> Rollup summary fields can cause the parent record to go through Save: Rollup summary fields on the Account object can trigger a recalculation of the parent record when child records (Branches) are inserted, updated, or deleted. This recalculation of the parent record may cause the trigger to fire again if the trigger logic is dependent on specific field changes or data conditions.

---

### Question 53
How can a developer set up a debug log on a specific user?
- [ ] **A.** It is not possible to setup debug logs for users other than yourself.  [WRONG]
- [ ] **B.** Ask the user for access to their account credentials, log in as the user and debug the issue.  [WRONG]
- [ ] **C.** Create Apex code that logs code actions into a custom object.  [WRONG]
- [x] **D.** Set up a trace flag for the user, and define a logging level and time period for the trace.  [CORRECT]

**Explanation:**
> To set up a debug log on a specific user in Salesforce, a developer needs to set up a TraceFlag for that user. A TraceFlag defines the logging level and time period for the trace.

---

### Question 54
A developer has an integer variable called maxAttempts. The developer needs to ensure that once maxAttempts is initialized, it preserves its value for the length of the Apex transaction; while being able to share the variable's state between trigger executions. How should the developer declare maxAttempts to meet these requirements?
- [ ] **A.** Declare maxAttempts as a private static variable on a helper class.  [WRONG]
- [ ] **B.** Declare maxAttempts as a variable on a helper class.  [WRONG]
- [ ] **C.** Declare maxAttempts as a member variable on the trigger definition.  [WRONG]
- [x] **D.** Declare maxAttempts as a constant using the static and final keywords.  [CORRECT]

**Explanation:**
> Apex constants are variables whose values don’t change after being initialized once. Constants can be defined using the final keyword.
> The final keyword means that the variable can be assigned at most once, either in the declaration itself, or with a static initializer method if the constant is defined in a class. This example declares two constants. The first is initialized in the declaration statement. The second is assigned a value in a static block by calling a static method.

**Resources:**
> Constants

---

### Question 55
Universal Containers (UC) decided it will not send emails to support personnel directly from Salesforce in the event that an unhandled exception occurs. Instead, UC wants an external system be notified of the error. What is the appropriate publish/subscribe logic to meet these requirements?
- [ ] **A.** Publish the error event using the addError() method and write a trigger to subscribe to the event and notify the external system.  [WRONG]
- [x] **B.** Publish the error event using the Eventbus.publish() method and have the external system subscribe to the event using CometD.  [CORRECT]
- [ ] **C.** Have the external system subscribe to the BatchApexError event, no publishing is necessary.  [WRONG]
- [ ] **D.** Publish the error event using the addError() method and have the external system subscribe to the event using CometD.  [WRONG]

**Explanation:**
> By using the Eventbus.publish() method in the trigger to publish the Platform Event and having the external system subscribe to the event using CometD, UC can achieve the goal of notifying the external system of unhandled exceptions without directly sending emails from Salesforce. This approach provides real-time, scalable, and robust communication between Salesforce and the external system for exception notifications.

---

### Question 56
A developer has JavaScript code that needs to be called by controller functions in multiple Aura components by extending a new abstract component. Which resource in the abstract Aura component bundle allows the developer to achieve this?
- [x] **A.** helper.js  [CORRECT]
- [ ] **B.** controller.js  [WRONG]
- [ ] **C.** superRender.js  [WRONG]
- [ ] **D.** renderer.js  [WRONG]

**Explanation:**
> To achieve the goal of calling JavaScript code by controller functions in multiple Aura components by extending a new abstract component, the developer can use the Helper resource in the abstract Aura component bundle.

---

### Question 57
A developer must create a Lightning component that allows users to input Contact record information to create a Contact record, including a Salary__c custom field. What should the developer use, along with a lightning-record-edit-form, so that Salary__c field functions as a currency input and is only viewable and editable by users that have the correct field level permissions on Salary__c?
- [ ] **A.** <lightning-input type="number" value="Salary__c" formatter="currency"></lightning-input>  [WRONG]
- [ ] **B.** <lightning-formatted-number value="Salary__c" format-style="currency"></lightning-formatted-number>  [WRONG]
- [x] **C.** <ligthning-input-field field-name="Salary__c"></lightning-input-field>  [CORRECT]
- [ ] **D.** <lightning-input-currency value="Salary__c"></lightning-input-currency>  [WRONG]

**Explanation:**
> Using the lightning-record-edit-form along with lightning-input-field and setting the disabled attribute appropriately based on field-level permissions, the developer can ensure that the Salary__c field functions as a currency input and is only viewable and editable by users with the correct permissions.

---

### Question 58
Which two statements are acceptable for a developer to use inside procedural loops? (Choose two.)
- [ ] **A.** delete contactList;  [WRONG]
- [x] **B.** contactList.remove(i);  [CORRECT]
- [x] **C.** Contact con = new Contact();  [CORRECT]
- [ ] **D.** Account a = [SELECT Id, Name FROM Account WHERE Id = :con.AccountId LIMIT 1];  [WRONG]

**Explanation:**
> Options B and C are acceptable inside procedural loops, while options A and D are not recommended due to potential issues and governor limit concerns.

---

### Question 59
A developer needs to display all of the available fields for an object. In which two ways can the developer retrieve the available fields if the variable myObject represents the name of the object? (Choose two.)
- [ ] **A.** Use myObject.sObjectType.getDescribe().fieldSet() to return a set of fields.  [WRONG]
- [ ] **B.** Use mySObject.myObject.fields.getMap() to return a map of fields.  [WRONG]
- [x] **C.** Use Schema.describeSObjects(new String[]{myObject})[0].fields.getMap() to return a map of fields.  [CORRECT]
- [x] **D.** Use getGlobalDescribe().get(myObject).getDescribe().fields.getMap() to return a map of fields.  [CORRECT]

**Explanation:**
> Options C and D are the correct ways to retrieve the available fields for an object using the variable myObject.

---

### Question 60
A newly hired developer discovers that there are multiple triggers on the case object. What should the developer consider when working with triggers?
- [ ] **A.** Developers must dictate the order of trigger execution.  [WRONG]
- [ ] **B.** Trigger execution order is based on creation date and time.  [WRONG]
- [ ] **C.** Unit tests must specify the trigger being tested.  [WRONG]
- [x] **D.** Trigger execution order is not guaranteed for the same sObject.  [CORRECT]

**Explanation:**
> When working with triggers, it's essential to be aware that the order of execution of multiple triggers on the same sObject is not guaranteed. Salesforce executes triggers for the same sObject in an undetermined order. This means that if there are multiple triggers on the Case object, the developer cannot rely on a specific sequence of trigger execution.

---

### Question 1
Universal Containers has a support process that allows users to request support from its engineering team using a custom object, Engineering_Support__c. Users should be able to associate multiple Engineering_Support__c records to a single Opportunity record. Additionally, aggregate information about the Engineering_Support__c records should be shown on the Opportunity record. What should a developer implement to support these requirements?
- [ ] **A.** Master-detail field from Opportunity to Engineering_Support__c  [WRONG]
- [ ] **B.** Lookup field from Engineering_Support__c to Opportunity  [WRONG]
- [ ] **C.** Lookup field from Opportunity to Engineering_Support__c  [WRONG]
- [x] **D.** Master-detail field from Engineering_Support__c to Opportunity  [CORRECT]

**Explanation:**
> Implementing a Master-detail relationship from the Engineering_Support__c custom object to the Opportunity standard object ensures that the support records are tightly associated with specific Opportunities. This relationship allows for automatic aggregation of information and cascading behavior, which is essential for displaying aggregate data on the Opportunity record.

---

### Question 2
When a user edits the Postal Code on an Account, a custom Account text field named 'Timezone' must be updated based on the values in another custom object called PostalCodeToTimezone__c. What is the optimal way to implement this feature?
- [ ] **A.** Build an account assignment rule.  [WRONG]
- [x] **B.** Build a flow with Flow Builder.  [CORRECT]
- [ ] **C.** Create an account approval process.  [WRONG]
- [ ] **D.** Create a formula field.  [WRONG]

**Explanation:**
> The flow can then perform actions such as querying the PostalCodeToTimezone__c custom object, retrieving the relevant timezone value, and updating the ‘Timezone’ field on the Account.
> Formula fields are used to calculate values based on other fields on the same object or related objects, but they cannot perform lookups to other custom objects.

---

### Question 3
A team of many developers work in their own individual orgs that have the same configuration as the production org. Which type of org is best suited for this scenario?
- [x] **A.** Developer Sandbox  [CORRECT]
- [ ] **B.** Developer Edition  [WRONG]
- [ ] **C.** Full Sandbox  [WRONG]
- [ ] **D.** Partner Developer Edition  [WRONG]

**Explanation:**
> A Developer Sandbox is a copy of the production org with the same configuration and data. Each developer can have their own Developer Sandbox, which allows them to work independently without interfering with each other's work.

---

### Question 4
Universal Containers uses Service Cloud with a custom field, Stage__c, on the Case object. Management wants to send a follow-up email reminder 6 hours after the Stage__c field is set to 'Waiting on Customer'. The Salesforce Administrator wants to ensure the solution used is bulk safe. Which automation tool should a developer recommend to meet these business requirements? (Choose two)
- [x] **A.** Record-Triggered Flow  [CORRECT]
- [ ] **B.** Entitlement Process  [WRONG]
- [ ] **C.** Einstein Next Best Action  [WRONG]
- [x] **D.** Scheduled Flow  [CORRECT]

**Explanation:**
> A Record-Triggered Flow can be used to detect when the Stage__c field is updated to ‘Waiting on Customer’. Then, a Scheduled Flow can be set to execute 6 hours later to send the follow-up email.

---

### Question 5
A developer observes that an Apex test method fails in the Sandbox. To identify the issue, the developer copies the code inside the test method and executes it via the Execute Anonymous tool in the Developer Console. The code then executes with no exceptions or errors. Why did the test method fail in the sandbox and pass in the Developer Console?
- [ ] **A.** The test method has a syntax error in the code.  [WRONG]
- [ ] **B.** The test method does not use System.runAs to execute as a specific user.  [WRONG]
- [ ] **C.** The test method is calling an @future method.  [WRONG]
- [x] **D.** The test method relies on existing data in the sandbox.  [CORRECT]

**Explanation:**
> When running the same code in the Execute Anonymous tool in the Developer Console, it executes within the current user's context and can access the existing data, which might result in successful execution.

---

### Question 6
A developer is writing tests for a class and needs to insert records to validate functionality. Which annotation method should be used to create records for every method in the test class?
- [ ] **A.** @StartTest  [WRONG]
- [ ] **B.** @PreTest  [WRONG]
- [x] **C.** @TestSetup  [CORRECT]
- [ ] **D.** @isTest(SeeAllData=true)  [WRONG]

**Explanation:**
> @TestSetup annotation
> Can create common test data once, which will be available for all test methods in the test class. This helps reduce duplicate code and ensures that the test data is consistent across all test methods.

---

### Question 7
In the following example, which sharing context myMethod execute when it is invoked?
public Class myClass {
public void myMethod() { /* implementation */ }
}
- [x] **A.** Sharing rules will not be enforced for the running user.  [CORRECT]
- [ ] **B.** Sharing rules will be inherited from the calling context.  [WRONG]
- [ ] **C.** Sharing rules will be enforced for the running user.  [WRONG]
- [ ] **D.** Sharing rules will be enforced by the instantiating class.  [WRONG]

**Explanation:**
> Since the class myClass does not explicitly specify a sharing context (using with sharing or without sharing), it defaults to “without sharing”. This means that the method myMethod will execute without enforcing the sharing rules of the running user.

**Resources:**
> Using the with sharing, without sharing, and inherited sharing Keywords

---

### Question 8
A developer created a new after insert trigger on the Lead object that creates Task records for each Lead. After deploying to production, an existing outside integration that inserts Lead records in batches to Salesforce is occasionally reporting total batch failures being caused by the Task insert statement. This causes the integration process in the outside system to stop, requiring a manual restart. 	Which change should the developer make to allow the integration to continue when some records in a batch cause failures due to the Task insert statement, so that manual restarts are not needed?
- [ ] **A.** Deactivate the trigger before the integration runs.  [WRONG]
- [ ] **B.** Use a try-catch block after the insert statement.  [WRONG]
- [x] **C.** Use the Database method with allOrNone set to false.  [CORRECT]
- [ ] **D.** Remove the Apex class from the integration user’s profile.  [WRONG]

**Explanation:**
> When using the Database.insert() method with allOrNone set to false, if there are any errors during the insert operation (such as validation rule failures or triggers that cause an exception), the successful records will be committed, and the failed records will generate errors but won't cause the entire batch to fail. This way, the integration process will continue without requiring a manual restart.

---

### Question 9
A developer needs to join data received from an integration with an external system with parent records in Salesforce. The data set does not contain the Salesforce IDs of the parent records, but it does have a foreign key attribute that can be used to identify the parent. Which action will allow the developer to relate records in the data model without knowing the Salesforce ID?
- [ ] **A.** Create and populate a custom field on the parent object marked as Unique.  [WRONG]
- [ ] **B.** Create a custom field on the child object of type External Relationship.  [WRONG]
- [x] **C.** Create and populate a custom field on the parent object marked as an External ID.  [CORRECT]
- [ ] **D.** Create a custom field on the child object of type Foreign Key.  [WRONG]

**Explanation:**
> An External ID field is used to store unique identifiers from an external system and allows the developer to use this external identifier to match records in Salesforce with records in the external system.

---

### Question 10
A developer creates a new Apex trigger with a helper class, and writes a test class that only exercises 95% coverage of the new Apex helper class. Change Set deployment to production fails with the test coverage warning: Test coverage of selected Apex Trigger is 0%, at least 1% test coverage is required. What should the developer do to successfully deploy the new Apex trigger and helper class?
- [ ] **A.** Increase the test class coverage on the helper class.  [WRONG]
- [ ] **B.** Remove the failing test methods from the test class.  [WRONG]
- [ ] **C.** Run the tests using the 'Run All Tests' method.  [WRONG]
- [x] **D.** Create a test class and methods to cover the Apex trigger.  [CORRECT]

**Explanation:**
> To successfully deploy the new Apex trigger and helper class, the developer needs to create a test class that provides test coverage for both the trigger and the helper class.

---

### Question 11
How many Accounts will be inserted by the following block of code?
for(Integer i = 0; i 500; i++){
Account a = new Account(Name = 'New Account ' + i);
insert a;
}
- [ ] **A.** 100  [WRONG]
- [ ] **B.** 150  [WRONG]
- [x] **C.** 0  [CORRECT]
- [ ] **D.** 500  [WRONG]

**Explanation:**
> DML Exception

---

### Question 12
A developer needs to implement a custom SOAP Web Service that is used by an external Web Application. The developer chooses to Include helper methods that are not used by the Web Application in the implementation of the Web Service Class. Which code segment shows the correct declaration of the class and methods?
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
}

**Explanation:**
> The class must be declared as global to be accessible by external applications.
> The method that is exposed as a web service must be declared with the webservice keyword.

**Resources:**
> Webservice Methods

---

### Question 13
A developer is asked to prevent anyone other than a user with Sales Manager profile from changing the Opportunity Status to Closed Lost if the lost reason is blank. Which automation allows the developer to satisfy this requirement in the most efficient manner?
- [x] **A.** An error condition formula on a validation rule on Opportunity  [CORRECT]
- [ ] **B.** An Apex trigger on the Opportunity object  [WRONG]
- [ ] **C.** A record trigger flow on the Opportunity object  [WRONG]
- [ ] **D.** An approval process on the Opportunity object  [WRONG]

**Explanation:**
> Using a validation rule is the most efficient way to enforce this requirement. The validation rule can be set up to check if the Opportunity Status is being changed to “Closed Lost” and if the “Lost Reason” field is blank.
> Here’s an example of how the validation rule might look:
> AND(
> ISPICKVAL(StageName, "Closed Lost"),
> ISBLANK(Lost_Reason__c),
> $Profile.Name <> "Sales Manager"
> )

---

### Question 14
A developer needs to prevent the creation of Request records when certain conditions exist in the system. A RequestLogic class exists that checks the conditions. What is the correct implementation?
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
}

**Explanation:**
> This implementation ensures that the validation logic is applied before the records are inserted into the database, allowing the trigger to prevent the creation of invalid records.

---

### Question 15
Which annotation exposes an Apex class as a RESTful web service?
- [ ] **A.** @RemoteAction  [WRONG]
- [x] **B.** @RestResource  [CORRECT]
- [ ] **C.** @HttpInvocable  [WRONG]
- [ ] **D.** @AuraEnabled  [WRONG]

---

### Question 16
A developer must troubleshoot to pinpoint the causes of performance issues when a custom page loads in their org. Which tool should the developer use to troubleshoot?
- [ ] **A.** Visual Studio Code IDE  [WRONG]
- [ ] **B.** AppExchange  [WRONG]
- [x] **C.** Developer Console  [CORRECT]
- [ ] **D.** Setup Menu  [WRONG]

**Explanation:**
> The Developer Console allows developers to set up debug logs for specific users or classes. These logs capture detailed information about the execution of Apex code, including any SOQL queries, DML operations, and method calls.

---

### Question 17
What should a developer use to implement an automatic Approval Process submission for Cases?
- [ ] **A.** An Assignment Rule  [WRONG]
- [ ] **B.** Scheduled Apex  [WRONG]
- [x] **C.** Process Builder  [CORRECT]
- [ ] **D.** A Workflow Rule  [WRONG]

**Explanation:**
> Process Builder is a declarative automation tool that allows you to create automated processes by defining a set of criteria and actions to be executed when those criteria are met.

---

### Question 18
What are two ways a developer can get the status of an enqueued job for a class that implements the queueable interface? (Choose two.)
- [x] **A.** View the Apex Jobs Page  [CORRECT]
- [ ] **B.** View the Apex Status Page  [WRONG]
- [x] **C.** Query the AsyncApexJob object  [CORRECT]
- [ ] **D.** View the Apex Flex Queue  [WRONG]

**Explanation:**
> The two correct ways for a developer to get the status of an enqueued job for a class that implements the Queueable interface are:
> A. View the Apex Jobs Page
> This page provides a list of all queued, in-progress, and completed jobs, including those that implement the Queueable interface.
> C. Query the AsyncApexJob object
> Developers can query the AsyncApexJob object to retrieve detailed information about the status of queued jobs. For example:
> AsyncApexJob job = [SELECT Id, Status, NumberOfErrors, JobItemsProcessed, TotalJobItems, CreatedBy.Email
> FROM AsyncApexJob
> WHERE Id = :jobId];

---

### Question 19
The Review_c object has a lookup relationship up to the Job_Application_c object. The Job_Application_c object has a master-detail relationship up to the Position_c object. The relationship field names are based on the auto-populated defaults. What is the recommended way to display field data from the related Position_c record on a Visualforce page for a single Review_c record?
- [ ] **A.** Use the Standard Controller for Review_c and cross-object Formula Fields on the Position_c object to display Position_c data.  [WRONG]
- [x] **B.** Use the Standard Controller for Job_Application_c and a Controller Extension to query for Position_c data.  [CORRECT]
- [ ] **C.** Use the Standard Controller for Job_Application_c and cross-object Formula Fields on the Review_c object to display Position_c data.  [WRONG]
- [ ] **D.** Use the Standard Controller for Review_c and expression syntax in the Page to display related Position_c data through the Job_Application_c object.  [WRONG]

---

### Question 20
Refer to the following code snippet for an environment has more than 200 Accounts belonging to the ‘Technology’ industry:
for(Account thisAccount : [SELECT Id, Industry FROM Account LIMIT 150]){
if(thisAccount.Industry == 'Technology'){
thisAccount.Is_Tech__c = true;
}
update thisAccount;
}
When the code executes, what happens as a result of the Apex transaction?
- [x] **A.** The Apex transaction succeeds regardless of any uncaught exception and all processed accounts are updated.  [CORRECT]
- [ ] **B.** If executed in a synchronous context, the Apex transaction is likely to fail by exceeding the DML governor limit.  [WRONG]
- [ ] **C.** The Apex transaction fails with the following message: SObject row was retrieved via SOQL without querying the requested field: Account.Is_Tech__c.  [WRONG]
- [ ] **D.** If executed in an asynchronous context, the Apex transaction is likely to fail by exceeding the DML governor limit.  [WRONG]

**Resources:**
> Apex Governor Limits

---

### Question 21
What is the data type returned by the following SOSL search?
[FIND 'Acme*' IN NAME FIELDS RETURNING Account, Opportunity];
- [ ] **A.** List<List<Account>, List<Opportunity>>  [WRONG]
- [ ] **B.** Map<sObject, sObject>  [WRONG]
- [x] **C.** List<List<sObject>>  [CORRECT]
- [ ] **D.** Map<Id, sObject>  [WRONG]

**Explanation:**
> The data type List<List<sObject>> is correct because SOSL searches return a List of Lists of sObjects. In this case, the search query is returning a List of sObjects that include both Account and Opportunity records.

**Resources:**
> Write SOSL Queries

---

### Question 22
A change set deployment from a sandbox to production fails due to a failure in a managed package unit test. The developer spoke with the managed package owner and they determined it is a false positive and can be ignored. What should the developer do to successfully deploy?
- [x] **A.** Select "Run local tests" to run all tests in the org that are not in the managed package.  [CORRECT]
- [ ] **B.** Select "Fast Deploy" to run only the tests that are in the change set.  [WRONG]
- [ ] **C.** Select "Run local tests" to run only the tests that are in the change set.  [WRONG]
- [ ] **D.** Edit the managed package's unit test.  [WRONG]

**Explanation:**
> By running only local tests, the deployment will bypass the managed package unit test that caused the failure and proceed with deploying the rest of the changes in the change set.

---

### Question 23
Which code displays the contents of a Visualforce page as a PDF?
- [ ] **A.** <apex:page contentType="application/pdf">  [WRONG]
- [x] **B.** <apex:page renderAs="pdf">  [CORRECT]
- [ ] **C.** <apex:page renderAs="application/pdf">  [WRONG]
- [ ] **D.** <apex:page contentType="pdf">  [WRONG]

**Explanation:**
> <apex:page renderAs="pdf">
> <!-- Contents of your Visualforce page -->
> </apex:page>

**Resources:**
> Render a Visualforce Page as a PDF File

---

### Question 24
What is a fundamental difference between a Master-Detail relationship and a Lookup relationship?
- [ ] **A.** In a Master-Detail relationship, when a record of a master object is deleted, the detail records are not deleted.  [WRONG]
- [ ] **B.** In a Lookup relationship when the parent record is deleted, the child records are always deleted.  [WRONG]
- [x] **C.** A Master-Detail relationship detail record inherits the sharing and security of its master record.  [CORRECT]
- [ ] **D.** In a Lookup relationship, the field value is mandatory.  [WRONG]

**Explanation:**
> In a Master-Detail relationship, the detail record (child) is considered to be a subordinate of the master record (parent). The detail record inherits the sharing and security settings of its master record. This means that the detail record's access is determined by the access level of the master record.

---

### Question 25
A developer wants multiple test classes to use the same set of test data. How should the developer create the test data?
- [x] **A.** Reference a test utility class in each test class.  [CORRECT]
- [ ] **B.** Define variables for test records in each test class.  [WRONG]
- [ ] **C.** Create a Test Setup method for each test class.  [WRONG]
- [ ] **D.** Use the SeeAllData=true annotation in each test class.  [WRONG]

**Explanation:**
> Create a test utility class that contains methods to create and insert the common test data.
> Each test class can then reference this test utility class and call its methods to set up the required test data.

---

### Question 26
Which two statements are true about using the @testSetup annotation in an Apex test class? (Choose two.)
- [x] **A.** The @testSetup annotation cannot be used when the @isTest(SeeAllData=True) annotation is used.  [CORRECT]
- [x] **B.** Test data is inserted once for all test methods in a class.  [CORRECT]
- [ ] **C.** Records created in the @testSetup method cannot be updates in individual test methods.  [WRONG]
- [ ] **D.** The @testSetup method is automatically executed before each test method in the test class is executed.  [WRONG]

**Explanation:**
> The @testSetup annotation is used to set up test data that will be used by all test methods within a class. This helps to avoid redundant data creation and improves test efficiency.
> Test setup methods are supported only with the default data isolation mode for a test class. If the test class or a test method has access to organization data by using the @isTest(SeeAllData=true) annotation, test setup methods aren’t supported in this class.

---

### Question 27
Which two platform features align to the Controller portion of MVC architecture? (Choose two.)
- [x] **A.** Process Builder actions  [CORRECT]
- [x] **B.** Workflow rules  [CORRECT]
- [ ] **C.** Standard objects  [WRONG]
- [ ] **D.** Date fields  [WRONG]

**Explanation:**
> In the Model-View-Controller (MVC) architecture, the Controller is responsible for handling user input and processing data. In Salesforce, both Process Builder actions and Workflow rules can be considered as part of the Controller layer because they automate and process data based on certain criteria and user input.

---

### Question 28
A developer wrote the following two classes:
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
The StatusFetcher class successfully compiled and saved. However, the Calculator class has a compile time error. How should the developer fix this code?
- [ ] **A.** Change the class declaration for the StatusFetcher class to public with inherited sharing.  [WRONG]
- [x] **B.** Make the isActive method in the StatusFetcher class public.  [CORRECT]
- [ ] **C.** Make the doCalculations method in the Calculator class private.  [WRONG]
- [ ] **D.** Change the class declaration for the Calculator class to public with inherited sharing.  [WRONG]

**Explanation:**
> Make the isActive method public, it can now be accessed from other classes, and the Calculator class will be able to call the isActive method on the StatusFetcher instance without any compilation errors.

---

### Question 29
Which statement generates a list of Leads and Contacts that have a field with the phrase 'ACME'?
- [ ] **A.** List <sObject> searchList = [FIND "*ACME*" IN ALL FIELDS RETURNING Contact, Lead];  [WRONG]
- [x] **B.** List<List <sObject>> searchList = [FIND "*ACME*" IN ALL FIELDS RETURNING Contact, Lead];  [CORRECT]
- [ ] **C.** List<List <sObject>> searchList = [SELECT Name, ID FROM Contact, Lead WHERE Name like ‘%ACME%’];  [WRONG]
- [ ] **D.** Map <sObject> searchList = [FIND "*ACME*" IN ALL FIELDS RETURNING Contact, Lead];  [WRONG]

**Explanation:**
> SOSL searches return a List of Lists of sObjects List<List<sObject>>.

**Resources:**
> Write SOSL Queries

---

### Question 30
A custom picklist field, Food_Preference__c, exists on a custom object. The picklist contains the following options: 'Vegan', 'Kosher', 'No Preference'. The developer must ensure a value is populated every time a record is created or updated. What is the most efficient way to ensure a value is selected every time a record is saved?
- [x] **A.** Mark the field as Required on the field definition.  [CORRECT]
- [ ] **B.** Set Use the first value in the list as the default value as True.  [WRONG]
- [ ] **C.** Mark the field as Required on the object's page layout.  [WRONG]
- [ ] **D.** Set a validation rule to enforce a value is selected.  [WRONG]

**Explanation:**
> Change the access modifier of the isActive method in the StatusFetcher class to public.

---

### Question 31
As part of a data cleanup strategy, AW Computing wants to proactively delete associated opportunity records when the related Account is deleted. Which automation tool should be used to meet this business requirement?
- [ ] **A.** Scheduled job  [WRONG]
- [x] **B.** Record-triggered flow  [CORRECT]
- [ ] **C.** Workflow rules  [WRONG]
- [ ] **D.** Outbound messaging  [WRONG]

**Explanation:**
> With Record-Triggered Flows, you can automate actions based on changes to record data, including deleting related records.

---

### Question 32
Given the following Anonymous Block:
List<Case> casesToUpdate = new List<Case>();
for(Case thisCase : [Select Id, Status FROM Case LIMIT 50000]){
thisCase.Status = 'Working';
casesToUpdate.add(thisCase);
}try{
Database.update(casesToUpdate, false);
}catch(Exception e) {
System.debug(e.getMessage());
}
What should a developer consider for an environment that has over 10,000 Case records?
- [ ] **A.** The transaction will succeed and changes will be committed.  [WRONG]
- [x] **B.** The transaction will fail due to exceeding the governor limit.  [CORRECT]
- [ ] **C.** The try/catch block will handle any DML exceptions thrown.  [WRONG]
- [ ] **D.** The try/catch block will handle exceptions thrown by governor limits.  [WRONG]

**Explanation:**
> Total number of records processed as a result of DML statements, Approval.process, or database.emptyRecycleBin: 10,000
> If there are more than 10,000 Case records in the environment, the code may hit the DML row limit and result in a "Too many DML rows: 10001" exception.
> Reference:
> 1. Execution Governors and Limits
> https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apexgov.htm
> 2. Exceptions that Can’t be Caught(LimitException)
> https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_exception_statements.htm

---

### Question 33
Which two statements are true about Getter and Setter methods? (Choose two.)
- [ ] **A.** Setter methods always have to be declared global.  [WRONG]
- [x] **B.** Setter methods are required to pass a value from a page to a controller.  [CORRECT]
- [x] **C.** There is no guarantee for the order in which Getter or Setter methods are executed.  [CORRECT]
- [ ] **D.** Getter methods can pass a value from a controller to a page.  [WRONG]

**Explanation:**
> Setter Methods: While a getter method is always required to access values from a controller, it’s not always necessary to include a setter method to pass values into a controller. If a Visualforce component is bound to an sObject that is stored in a controller, the sObject's fields are automatically set if changed by the user, as long as the sObject is saved or updated by a corresponding action method.
> There is no guaranteed order in which Apex methods and variables are processed by a controller extension or custom controller. Therefore, do not allow controller and extension classes to rely on another method being run, call that method directly. This applies specifically to setting variables and accessing data from the database.

**Resources:**
> Controller Methods

---

### Question 34
A Platform Developer needs to write an Apex method that will only perform an action if a record is assigned to a specific Record Type. Which two options allow the developer to dynamically determine the ID of the required Record Type by its name? (Choose two.)
- [ ] **A.** Make an outbound web services call to the SOAP API.  [WRONG]
- [ ] **B.** Hardcode the ID as a constant in an Apex class.  [WRONG]
- [x] **C.** Use the getRecordTypeInfosByName() method in the DescribeSObjectResult class.  [CORRECT]
- [x] **D.** Execute a SOQL query on the RecordType object.  [CORRECT]

**Explanation:**
> Using the getRecordTypeInfosByName() method allows you to dynamically retrieve the Record Type ID by its name without hardcoding.
> Executing a SOQL query on the RecordType object is another way to dynamically determine the Record Type ID.

**Resources:**
> DescribeSObjectResult Class

---

### Question 35
Which situation prevents a developer from setting sharing rules for a custom object?
- [ ] **A.** The object's Sharing Settings is set to Public Read/Write.  [WRONG]
- [x] **B.** The object is on the detail side of a Master-Detail relationship.  [CORRECT]
- [ ] **C.** The developer is not a System Administrator.  [WRONG]
- [ ] **D.** The object is referenced in an Owner field of a Master-Detail relationship.  [WRONG]

**Explanation:**
> Cannot set explicit sharing rules for custom objects that are on the detail side of a Master-Detail relationship.

---

### Question 36
What will be the output in the debug log in the event of a QueryException during a call to the aQuery method in the following example?
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
}
- [ ] **A.** Querying Accounts. Query Exception.  [WRONG]
- [ ] **B.** Querying Accounts. Custom Exception.  [WRONG]
- [ ] **C.** Querying Accounts. Custom Exception. Done.  [WRONG]
- [x] **D.** Querying Accounts. Query Exception. Done.  [CORRECT]

**Explanation:**
> 1. Try Block: The code attempts to execute the SOQL query inside the try block and logs “Querying Accounts.”.
> 2. Catch Blocks: If a QueryException occurs, it will be caught by the catch(QueryException eX) block, logging “Query Exception.”.
> 3. Finally Block: The finally block will always execute, logging “Done.”.

**Resources:**
> Exception Handling

---

### Question 37
Universal Containers wants Opportunities to no longer be editable when reaching the Closed/Won stage. Which two strategies can a developer use to accomplish this? (Choose two.)
- [ ] **A.** Use an after-save flow.  [WRONG]
- [x] **B.** Use a validation rule.  [CORRECT]
- [ ] **C.** Use the Process Automation Settings.  [WRONG]
- [x] **D.** Use a trigger.  [CORRECT]

**Explanation:**
> Create a validation rule on the Opportunity object that checks the stage value. If the stage is Closed/Won, the validation rule should prevent any updates or changes to the Opportunity.
> Using a trigger can be an option.

---

### Question 38
Which action causes a before trigger to fire by default for Accounts?
- [ ] **A.** Renaming or replacing picklists  [WRONG]
- [x] **B.** Importing data using the Data Loader and the Bulk API  [CORRECT]
- [ ] **C.** Updating addresses using the Mass Address update tool  [WRONG]
- [ ] **D.** Converting Leads to Contacts  [WRONG]

**Explanation:**
> When importing data using the Data Loader or Bulk API, Salesforce triggers are executed by default. This includes before triggers for Accounts, which would fire before the imported data is inserted or updated.

**Resources:**
> Operations That Don't Invoke Triggers
> Workflow Considerations

---

### Question 39
The values 'High', 'Medium', and 'Low' are identified as common values for multiple picklists across different objects. What is an approach a developer can take to streamline maintenance of the picklists and their values, while also restricting the values to the ones mentioned above?
- [x] **A.** Create the Picklist on each object and use a Global Picklist Value Set containing the values.  [CORRECT]
- [ ] **B.** Create the Picklist on each object as a required field and select "Display values alphabetically, not in the order entered".  [WRONG]
- [ ] **C.** Create the Picklist on each object and add a validation rule to ensure data integrity.  [WRONG]
- [ ] **D.** Create the Picklist on each object and select "Restrict picklist to the values defined in the value set".  [WRONG]

**Explanation:**
> By creating a Global Picklist Value Set with the common values 'High', 'Medium', and 'Low', you can then use this value set to populate the picklist fields on different objects.

---

### Question 40
Which option should a developer use to create 500 Accounts and make sure that duplicates are not created for existing Account Sites?
- [ ] **A.** Sandbox template  [WRONG]
- [ ] **B.** Data Loader  [WRONG]
- [x] **C.** Data Import Wizard  [CORRECT]
- [ ] **D.** Salesforce-to-Salesforce  [WRONG]

**Explanation:**
> The Data Import Wizard in Salesforce provides an easy-to-use interface for importing data, and it has a built-in duplicate management feature that allows you to prevent the creation of duplicate records during the import process.

**Resources:**
> What Is Imported for Business Accounts and Contacts?

---

### Question 41
How should a developer write unit tests for a private method in an Apex class?
- [ ] **A.** Add a test method in the Apex class.  [WRONG]
- [ ] **B.** Mark the Apex class as global.  [WRONG]
- [ ] **C.** Use the SeeAllData annotation.  [WRONG]
- [x] **D.** Use the TestVisible annotation.  [CORRECT]

**Explanation:**
> The TestVisible annotation allows you to expose private methods and variables to be accessed in test classes.

---

### Question 42
A company has a custom object named Region. Each Account in Salesforce can only be related to one Region at a time, but this relationship is optional. Which type of relationship should a developer use to relate an Account to a Region?
- [ ] **A.** Parent-Child  [WRONG]
- [ ] **B.** Hierarchical  [WRONG]
- [x] **C.** Lookup  [CORRECT]
- [ ] **D.** Master-Detail  [WRONG]

**Explanation:**
> A Lookup relationship allows each Account to be optionally related to one Region at a time without enforcing strict dependency rules, which fits the requirement of an optional relationship.

---

### Question 43
An Account trigger updates all related Contacts and Cases each time an Account is saved using the following two DML statements: update allContacts; update allCases; What is the result if the Case update exceeds the governor limit for maximum number of DML records?
- [x] **A.** The Account save fails and no Contacts or Cases are updated.  [CORRECT]
- [ ] **B.** The Account save succeeds and no Contacts or Cases are updated.  [WRONG]
- [ ] **C.** The Account save succeeds, Contacts are updated, but Cases are not.  [WRONG]
- [ ] **D.** The Account save is retried using a smaller trigger batch size.  [WRONG]

**Explanation:**
> If the Case update exceeds the governor limit for the maximum number of DML records, the entire transaction is rolled back, causing the Account save to fail and preventing any updates to Contacts or Cases.

---

### Question 44
A developer wants to invoke an outbound message when a record meets a specific criteria. Which three features satisfy this use case? (Choose three.)
- [x] **A.** Process builder can be used to check the record criteria and send an outbound message with Apex Code.  [CORRECT]
- [ ] **B.** Process builder can be used to check the record criteria and send an outbound message without Apex Code.  [WRONG]
- [x] **C.** Approval Process has the capability to check the record criteria and send an outbound message without Apex Code.  [CORRECT]
- [x] **D.** Workflows can be used to check the record criteria and send an outbound message.  [CORRECT]
- [ ] **E.** Visual Workflow can be used to check the record criteria and send an outbound message without Apex Code.  [WRONG]

**Explanation:**
> Outbound messaging allows you to specify that changes to fields within Salesforce can cause messages with field values to be sent to designated external servers.
> Outbound messaging is part of the workflow rule functionality in Salesforce. Workflow rules watch for specific kinds of field changes and trigger automatic Salesforce actions, such as sending email alerts, creating task records, or sending an outbound message. You can associate outbound messages with flows, workflow rules, approval processes, or entitlement processes.

**Resources:**
> Outbound Messaging

---

### Question 45
What is the result of the following code snippet?
public void doWork(Account acct){
for(Integer i = 0; i <= 200; i++){
insert acct;
}
}
- [ ] **A.** 200 Accounts are inserted.  [WRONG]
- [ ] **B.** 1 Account is inserted.  [WRONG]
- [ ] **C.** 201 Accounts are inserted.  [WRONG]
- [x] **D.** 0 Accounts are inserted.  [CORRECT]

**Explanation:**
> The exception prevents any accounts from being inserted, and the final outcome is that 0 Accounts are inserted.
> To avoid hitting the governor limit, a better approach would be to collect the accounts in a collection (such as a List<Account>) during the loop and then perform a single bulk insert after the loop completes.

---

### Question 46
A developer writes a single trigger on the Account object on the after insert and after update events. A workflow rule modifies a field every time an Account is created or updated. How many times will the trigger fire if a new Account is inserted, assuming no other automation logic is implemented on the Account?
- [ ] **A.** 8  [WRONG]
- [ ] **B.** 1  [WRONG]
- [ ] **C.** 4  [WRONG]
- [x] **D.** 2  [CORRECT]

**Explanation:**
> When a new Account is inserted, the following sequence of events occurs:
> 1. The Account is inserted, triggering the after insert event.
> 2. The workflow rule modifies a field on the Account, which triggers an after update event.
> So, the trigger will fire twice:
> 1. Once for the after insert event.
> 2. Once for the after update event caused by the workflow rule.

---

### Question 47
A developer must provide custom user interfaces when users edit a Contact in either Salesforce Classic or Lightning Experience. What should the developer use to override the Contact's Edit button and provide this functionality?
- [ ] **A.** A Lightning page in Salesforce Classic and a Visualforce page in Lightning Experience  [WRONG]
- [ ] **B.** A Visualforce page in Salesforce Classic and a Lightning page in Lightning Experience  [WRONG]
- [x] **C.** A Visualforce page in Salesforce Classic and a Lightning component in Lightning Experience  [CORRECT]
- [ ] **D.** A Lightning component in Salesforce Classic and a Lightning component in Lightning Experience  [WRONG]

**Explanation:**
> Visualforce pages are used to create custom user interfaces in Salesforce Classic, and Lightning components are used to create custom user interfaces in Lightning Experience.

---

### Question 48
What is the result of the debug statements in testMethod3 when you create test data using testSetup in below code?
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
}
- [ ] **A.** Account0.Phone=333-8781, Account1.Phone=333-8780  [WRONG]
- [ ] **B.** Account0.Phone=888-1515, Account1.Phone=999-2525  [WRONG]
- [x] **C.** Account0.Phone=333-8780, Account1.Phone=333-8781  [CORRECT]
- [ ] **D.** Account0.Phone=888-1515, Account1.Phone=999-1515  [WRONG]

**Explanation:**
> The debug statements in testMethod3 will display the phone numbers of the accounts created in the test setup method. Since the accounts are created in a loop where the phone numbers are incremented, the expected result is Account0.Phone=333-8780, Account1.Phone=333-8781, making this choice correct.

---

### Question 49
Which type of code represents the Model in the MVC architecture when using Apex and Visualforce pages?
- [ ] **A.** A Controller Extension method that saves a list of Account records  [WRONG]
- [ ] **B.** Custom JavaScript that processes a list of Account records  [WRONG]
- [x] **C.** A list of Account records returned from a Controller Extension method  [CORRECT]
- [ ] **D.** A Controller Extension method that uses SOQL to query for a list of Account records  [WRONG]

**Explanation:**
> The Model is responsible for handling the data and business logic. A list of Account records returned from a Controller Extension method would be an example of the Model.

---

### Question 50
An org has a single account named 'NoContacts' that has no related contacts. Given the query: List<Account> accounts = [Select ID, (Select ID, Name from Contacts) from Account where Name = 'NoContacts']; What is the result of running this Apex?
- [ ] **A.** accounts[0].contacts is invalid Apex.  [WRONG]
- [x] **B.** accounts[0].contacts is an empty list.  [CORRECT]
- [ ] **C.** accounts[0].contacts is Null.  [WRONG]
- [ ] **D.** A QueryException is thrown.  [WRONG]

**Explanation:**
> When you run the given query, it retrieves the account with the name ‘NoContacts’. Since this account has no related contacts, the contacts relationship will be an empty list, not null. Therefore, accounts[0].contacts will be an empty list.

---

### Question 51
Which SOQL query successfully returns the Accounts grouped by name?
- [ ] **A.** SELECT Type, Max(CreatedDate) FROM Account GROUP BY Name  [WRONG]
- [x] **B.** SELECT Name, Max(CreatedDate) FROM Account GROUP BY Name  [CORRECT]
- [ ] **C.** SELECT Id, Type, Max(CreatedDate) FROM Account GROUP BY Name  [WRONG]
- [ ] **D.** SELECT Type, Name, Max(CreatedDate) FROM Account GROUP BY Name LIMIT 5  [WRONG]

**Explanation:**
> This query selects the Name and maximum CreatedDate from the Account object and groups the results by the Name field. This is the correct query to successfully return the Accounts grouped by name.

---

### Question 52
For which example task should a developer use a trigger rather than a workflow rule?
- [ ] **A.** To set the Name field of an expense report record to Expense and the Date when it is saved  [WRONG]
- [ ] **B.** To send an email to a hiring manager when a candidate accepts a job offer  [WRONG]
- [ ] **C.** To notify an external system that a record has been modified  [WRONG]
- [x] **D.** To set the primary Contact on an Account record when it is saved  [CORRECT]

**Explanation:**
> Workflow rules in Salesforce cannot update records of other objects. They are limited to actions like field updates, sending emails, creating tasks, and sending outbound messages within the same object.

---

### Question 53
A developer must build an application that tracks which Accounts have purchased specific pieces of equipment that are represented as Products. Each Account could purchase many pieces of equipment. How should the developer track that an Account has purchased a piece of equipment?
- [x] **A.** Use the Asset object  [CORRECT]
- [ ] **B.** Use a Master-Detail on Product to Account  [WRONG]
- [ ] **C.** Use a Custom object  [WRONG]
- [ ] **D.** Use a Lookup on Account to Product  [WRONG]

**Explanation:**
> The Asset object in Salesforce is designed to represent specific products that customers have purchased. By using the Asset object, you can easily track each piece of equipment purchased by an Account, including details like purchase date, maintenance history, and more. This approach leverages Salesforce’s built-in functionality for managing customer assets, making it a robust and scalable solution.

**Resources:**
> Track Customer Assets
> Asset Management

---

### Question 54
A developer is creating a page that allows users to create multiple Opportunities. The developer is asked to verify the current user’s default Opportunity record type, and set certain default values based on the record type before inserting the record. How can the developer find the current user’s default record type?
- [ ] **A.** Use the Schema.userInfo.Opportunity.getDefaultRecordType() method.  [WRONG]
- [ ] **B.** Query the Profile where the ID equals userInfo.getProfileID() and then use the profile.Opportunity.getDefaultRecordType() method.  [WRONG]
- [ ] **C.** Create the opportunity and check the opportunity.recordType, which will have the record ID of the current user’s default record type, before inserting.  [WRONG]
- [x] **D.** Use Opportunity.SObjectType.getDescribe().getRecordTypeInfos() to get a list of record types, and iterate through them until isDefaultRecordTypeMapping() is true.  [CORRECT]

**Explanation:**
> This method allows the developer to programmatically access the record type information and identify the default record type for the current user.

---

### Question 55
Requirements state that a child record is deleted when its parent is deleted, and a child can be moved to a different parent when necessary. Which type of relationship should be built between the parent and child objects in Schema builder to support these requirements?
- [x] **A.** Master-Detail relationship  [CORRECT]
- [ ] **B.** Child relationship  [WRONG]
- [ ] **C.** Lookup relationship from the parent to the child  [WRONG]
- [ ] **D.** Lookup relationship from the child to the parent  [WRONG]

**Explanation:**
> A Master-Detail relationship provides the following features that align with the given requirements:
> Automatic deletion of child records: When the parent record is deleted, all related child records are automatically deleted.
> Relocation of child records: By default, records can’t be reparented in master-detail relationships. Administrators can, however, allow child records in master-detail relationships on custom objects to be reparented to different parent records by selecting the Allow reparenting option in the master-detail relationship definition.

**Resources:**
> Considerations for Object Relationships

---

### Question 56
A developer must modify the following code snippet to prevent the number of SOQL queries issued from exceeding the platform governor limit.
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
Which technique should be implemented to avoid reaching the governor limit?
- [ ] **A.** Refactor the code above to perform the SOQL query only if the Set of opportunityIds contains less 100 Ids.  [WRONG]
- [ ] **B.** Use the System.Limits.getLimitQueries() method to ensure the number of queries is less than 100.  [WRONG]
- [x] **C.** Refactor the code above to perform only one SOQL query, filtering by the Set of opportunityIds.  [CORRECT]
- [ ] **D.** Use the System.Limits.getQueries() method to ensure the number of queries is less than 100.  [WRONG]

**Explanation:**
> Refactor the code above to perform only one SOQL query, filtering by the Set of opportunityIds.
> This technique will significantly reduce the number of SOQL queries issued, as it combines all the individual queries into a single query, filtering by the entire Set of opportunityIds. This is much more efficient and helps to avoid reaching the governor limit.

---

### Question 57
A developer must write an Apex method that will be called from a Lightning component. The method may delete an Account stored in the accountRec variable. Which method should a developer use to ensure only users that should be able to delete Accounts can successfully perform deletions?
- [x] **A.** Schema.sObjectType.Account.isDeletable()  [CORRECT]
- [ ] **B.** Account.isDeletable()  [WRONG]
- [ ] **C.** accountRec.isDeletable()  [WRONG]
- [ ] **D.** accountRec.sObjectType.isDeletable()  [WRONG]

**Explanation:**
> Schema.sObjectType.Account.isDeletable()
> This method checks if the current user has the necessary permissions to delete the Account object.

**Resources:**
> DescribeSObjectResult Class

---

### Question 58
Which two statements are valid regarding Apex classes and interfaces? (Choose two.)
- [x] **A.** Classes are final by default.  [CORRECT]
- [ ] **B.** Interface methods are public by default.  [WRONG]
- [x] **C.** Inner classes are private by default.  [CORRECT]
- [ ] **D.** A class can only have one inner class level.  [WRONG]

**Explanation:**
> Methods and classes are final by default. You can’t use the final keyword in the declaration of a class or method. This means they can’t be overridden. Use the virtual keyword if you need to override a method or class.

**Resources:**
> Using the final Keyword

---

### Question 59
What is a benefit of using an after insert trigger over using a before insert trigger?
- [ ] **A.** An after insert trigger allows a developer to bypass validation rules when updating fields on the new record.  [WRONG]
- [x] **B.** An after insert trigger allows a developer to insert other objects that reference the new record.  [CORRECT]
- [ ] **C.** An after insert trigger allows a developer to make a callout to an external service.  [WRONG]
- [ ] **D.** An after insert trigger allows a developer to modify fields in the new record without a query.  [WRONG]

**Explanation:**
> In an after insert trigger, the record has already been committed to the database, so you can safely reference its ID and use it to create or update other related objects.

---

### Question 60
An org has an existing Visual Flow that creates an Opportunity with an Update Records element. A developer must update the Visual Flow to also create a Contact and store the created Contact's ID on the Opportunity. Which update should the developer make in the Visual Flow?
- [x] **A.** Add a new Create Records element.  [CORRECT]
- [ ] **B.** Add a new Quick Action (of type Create) element.  [WRONG]
- [ ] **C.** Add a new Update Records element.  [WRONG]
- [ ] **D.** Add a new Get Records element.  [WRONG]

**Explanation:**
> A. Add a new Create Records element.
> This element will allow the flow to create a new Contact record. After creating the Contact, the flow can then store the Contact’s ID in a variable. This variable can be used in an Update Records element to update the Opportunity with the Contact’s ID

---

### Question 1
Universal Containers wants Opportunities to be locked from editing when reaching the Closed/Won stage. Which two strategies should a developer use to accomplish this? (Choose two.)
- [ ] **A.** Use a Flow Builder.  [WRONG]
- [x] **B.** Use a validation rule.  [CORRECT]
- [ ] **C.** Use the Process Automation Settings.  [WRONG]
- [x] **D.** Mark fields as read-only on the page layout.  [CORRECT]

**Explanation:**
> B. Use a validation rule: This can prevent users from making changes to Opportunities once they reach the Closed/Won stage by setting up a rule that triggers an error message if any edits are attempted.
> D. Mark fields as read-only on the page layout: By marking the Opportunity fields as read-only on the page layout, users will be unable to edit them directly. This can be combined with the Flow Builder approach to provide a more comprehensive solution.

**Resources:**
> Validation Rules

---

### Question 2
Which action can a developer take to reduce the execution time of the following code?
List<Account> allAccounts = [SELECT Id FROM Account];
List<Contact> allContacts = [SELECT Id, AccountId FROM Contact];
for(Account a : allAccounts){
for(Contact c: allContacts){
if(c.AccountId = a.Id){
//do work
}
}
}
- [ ] **A.** Put the Account loop inside the Contact loop.  [WRONG]
- [ ] **B.** Create an Apex helper class for SOQL.  [WRONG]
- [ ] **C.** Add a GROUP BY clause to the Contact SOQL.  [WRONG]
- [x] **D.** Use a Map<Id List<Contact> for allContacts.  [CORRECT]

**Explanation:**
> By using a Map<Id, List<Contact>>, you can efficiently group the contacts by their AccountId. This allows you to avoid the nested loops and directly access the contacts related to each account, significantly reducing the number of iterations and improving performance.

---

### Question 3
Which three tools can deploy metadata to production? (Choose three.)
- [ ] **A.** Change Set from Developer Org  [WRONG]
- [x] **B.** Force.com IDE  [CORRECT]
- [ ] **C.** Data Loader  [WRONG]
- [x] **D.** Change Set from Sandbox  [CORRECT]
- [x] **E.** Metadata API  [CORRECT]

**Explanation:**
> Change Set from Sandbox: This is a common method for deploying metadata changes from a sandbox environment to a production environment1.
> Force.com IDE: This integrated development environment allows developers to manage and deploy metadata changes.
> Metadata API: This API is designed for deploying metadata changes programmatically, making it a powerful tool for managing customizations.

**Resources:**
> Choose Your Tools for Developing and Deploying Changes
> Deploy Metadata to Production

---

### Question 4
Universal Containers is building a recruiting app with an Applicant object that stores information about an individual person and a Job object that represents a job. Each applicant may apply for more than one job. What should a developer implement to represent that an applicant has applied for a job?
- [ ] **A.** Lookup field from Applicant to Job  [WRONG]
- [x] **B.** Junction object between Applicant and Job  [CORRECT]
- [ ] **C.** Master-detail field from Applicant to Job  [WRONG]
- [ ] **D.** Formula field on Applicant that references Job  [WRONG]

**Explanation:**
> A junction object is used to create a many-to-many relationship between two objects. In this case, since each applicant can apply for multiple jobs and each job can have multiple applicants, a junction object is the most appropriate solution. This junction object would have two master-detail relationships: one to the Applicant object and one to the Job object.

**Resources:**
> Create a Custom Junction Object

---

### Question 5
The sales team at Universal Containers would like to see a visual indicator appear on both Account and Opportunity page layouts to alert sales people when an Account is late making payments or has entered the collections process. What can a developer implement to achieve this requirement without having to write custom code?
- [x] **A.** Formula Field  [CORRECT]
- [ ] **B.** Workflow Rule  [WRONG]
- [ ] **C.** Quick Action  [WRONG]
- [ ] **D.** Roll-up Summary Field  [WRONG]

**Explanation:**
> A formula field can be used to create a visual indicator on both the Account and Opportunity page layouts. This field can be configured to display a specific value or image based on the criteria you set, such as when an account is late making payments or has entered the collections process.

---

### Question 6
Which governor limit applies to all the code in an Apex transaction?
- [ ] **A.** Elapsed SOQL query time  [WRONG]
- [ ] **B.** Number of classes called  [WRONG]
- [ ] **C.** Number of new records created  [WRONG]
- [x] **D.** Elapsed CPU time  [CORRECT]

**Explanation:**
> The elapsed CPU time is the governor limit that applies to all the code in an Apex transaction. This means that the total amount of time the CPU spends executing your Apex code must be within the specified limit.
> The other options are also governor limits, but they apply to specific aspects of Apex code
> A. Elapsed SOQL query time: This limit restricts the amount of time spent executing SOQL queries.
> B. Number of classes called: This limit restricts the number of different classes that can be called within a transaction.
> C. Number of new records created: This limit restricts the number of new records that can be created in a transaction.

---

### Question 7
Which two sfdx commands can be used to add testing data to a Developer sandbox? (Choose two.)
- [ ] **A.** force:data:async:upsert  [WRONG]
- [x] **B.** force:data:tree:import  [CORRECT]
- [x] **C.** force:data:bulk:upsert  [CORRECT]
- [ ] **D.** force:data:object:create  [WRONG]

**Explanation:**
> force:data:tree:import - This command is used to import data from a JSON file into Salesforce, which is useful for hierarchical data.
> force:data:bulk:upsert - This command allows you to upsert (update or insert) large volumes of data in bulk.

**Resources:**
> data Commands

---

### Question 8
A developer wants to override a button using Visualforce on an object. What is the requirement?
- [ ] **A.** The controller or extension must have a PageReference method.  [WRONG]
- [x] **B.** The standardController attribute must be set to the object.  [CORRECT]
- [ ] **C.** The action attribute must be set to a controller method.  [WRONG]
- [ ] **D.** The object record must be instantiated in a controller or extension.  [WRONG]

**Explanation:**
> In Visualforce, if a developer wants to override a standard button with a custom Visualforce page on an object, they need to specify the standardController attribute in the apex:page component.

---

### Question 9
A Visualforce page is required for displaying and editing Case records that includes both standard and custom functionality defined in an Apex class called myControllerExtension. The Visualforce page should include which attribute(s) to correctly implement controller functionality?
- [ ] **A.** controller="Case" and extensions="myControllerExtension"  [WRONG]
- [ ] **B.** extensions="myControllerExtension"  [WRONG]
- [ ] **C.** controller="myControllerExtension"  [WRONG]
- [x] **D.** standardController="Case" and extensions="myControllerExtension"  [CORRECT]

**Explanation:**
> standardController="Case": This attribute specifies that the Visualforce page is associated with the standard Case object. This means that the page will have access to standard Case fields and methods.
> extensions="myControllerExtension": This attribute specifies that the page will use the custom controller class myControllerExtension. This allows you to add custom functionality to the page, such as custom buttons, actions, or validation rules.

**Resources:**
> Building a Controller Extension

---

### Question 10
A lead object has a custom field Prior_Email__c.
The following trigger is intended to copy the current Email into the Prior_Email__c field any time the Email field is changed:
trigger test on Lead (before update) {
for(Lead Id: trigger.new){
if(Id.Email != trigger.oldMap.get(Id.id).email){
Id.Prior_Email__c = trigger.oldMap.get(Id.id).email;
Update Id;
}
}
}
Which type of exception will this trigger cause?
- [ ] **A.** A null reference exception  [WRONG]
- [ ] **B.** A compile time exception  [WRONG]
- [x] **C.** A DML exception  [CORRECT]
- [ ] **D.** A limit exception when doing a bulk update  [WRONG]

**Explanation:**
> The update statement inside the for loop attempts to perform a DML operation on the same record that is currently being processed in a before update trigger. Salesforce does not allow DML operations on records that are already in the process of being updated, leading to a DML exception.
> Exception:
> System.SObjectException: DML statement cannot operate on trigger.new or trigger.old

---

### Question 11
What is the result of the following code?
Account a = new Account();
Database.insert(a, false);
- [ ] **A.** The record will be created and no error will be reported.  [WRONG]
- [x] **B.** The record will not be created and no error will be reported.  [CORRECT]
- [ ] **C.** The record will be created and a message will be in the debug log.  [WRONG]
- [ ] **D.** The record will not be created and an exception will be thrown.  [WRONG]

**Explanation:**
> The allOrNone parameter specifies whether the operation allows partial success.
> If allOrNone is set to false and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify which records succeeded or failed.
> If allOrNone is set to true and the method isn’t successful, an exception is thrown. The default for the parameter is true.

**Resources:**
> Database Class

---

### Question 12
An after trigger on the Account object performs a DML update operation on all of the child Opportunities of an Account. There are no active triggers on the Opportunity object, yet a 'maximum trigger depth exceeded' error occurs in certain situations. Which two reasons possibly explain the Account trigger firing recursively? (Choose two.)
- [x] **A.** Changes to Opportunities are causing cross-object workflow field updates to be made on the Account.  [CORRECT]
- [x] **B.** Changes to Opportunities are causing roll-up summary fields to update on the Account.  [CORRECT]
- [ ] **C.** Changes are being made to the Account during an unrelated parallel save operation.  [WRONG]
- [ ] **D.** Changes are being made to the Account during Criteria Based Sharing evaluation.  [WRONG]

**Explanation:**
> The two reasons that could possibly explain the Account trigger firing recursively are:
> Cross-object workflow field updates can trigger the Account trigger again if the workflow rule updates a field on the Account.
> Roll-up summary fields on the Account that aggregate data from child Opportunities can cause the Account trigger to fire again when these fields are recalculated.

---

### Question 13
A developer has the following class and trigger code.
public class InsuranceRates{
public static final Decimal smokerCharge = 0.01;
}
trigger ContactTrigger on Contact(before insert){
InsuranceRates rates = new InsuranceRates();
Decimal baseCost = XXX;
}
Which code segment should a developer insert at the XXX to set the baseCost variable to the value of the class variable smokerCharge?
- [x] **A.** InsuranceRates.smokerCharge  [CORRECT]
- [ ] **B.** rates.getSmokerCharge()  [WRONG]
- [ ] **C.** ContactTrigger.InsuranceRates.smokerCharge  [WRONG]
- [ ] **D.** rates.smokerCharge  [WRONG]

**Explanation:**
> The smokerCharge variable is declared as a static variable in the InsuranceRates class. Static variables belong to the class itself rather than any instance of the class, so you access it using the class name InsuranceRates

---

### Question 14
How should a developer prevent a recursive trigger?
- [ ] **A.** Use a one trigger per object pattern.  [WRONG]
- [x] **B.** Use a static Boolean variable.  [CORRECT]
- [ ] **C.** Use a trigger handler.  [WRONG]
- [ ] **D.** Use a private Boolean variable.  [WRONG]

**Explanation:**
> What is a Recursive Trigger: A recursive trigger is one that performs an action, such as an update or insert, which causes the trigger to invoke itself, often due to an update it performs.
> How to Avoid Recursive Triggers: To prevent recursive triggers, you can create a class with a static Boolean variable initialized to true. In the trigger, before executing your code, check if the variable is true. If it is, proceed with your code and then set the variable to false.

---

### Question 15
What is a capability of the tag that is used for loading external Javascript libraries in Lightning Component? (Choose three.)
- [ ] **A.** Loading files from Documents.  [WRONG]
- [x] **B.** One-time loading for duplicate scripts.  [CORRECT]
- [x] **C.** Specifying loading order.  [CORRECT]
- [x] **D.** Loading scripts in parallel.  [CORRECT]
- [ ] **E.** Loading externally hosted scripts.  [WRONG]

**Explanation:**
> Loading Order
> The scripts are loaded in the order that they are listed.
> One-Time Loading
> Scripts load only once, even if they’re specified in multiple <ltng:require> tags in the same component or across different components.
> Parallel Loading
> Use separate <ltng:require> tags for parallel loading if you have multiple sets of scripts that are not dependent on each other.

**Resources:**
> Using External JavaScript Libraries

---

### Question 16
Universal Containers (UC) wants to lower its shipping cost while making the shipping process more efficient. The Distribution Officer advises UC to implement global addresses to allow multiple Accounts to share a default pickup address. The developer is tasked to create the supporting object and relationship for this business requirement and uses the Setup Menu to create a custom object called 'Global Address'. Which field should the developer add to create the most efficient model that supports the business need?
- [ ] **A.** Add a Master-Detail field on the Global Address object to the Account object.  [WRONG]
- [ ] **B.** Add a Master-Detail field on the Account object to the Global Address object.  [WRONG]
- [ ] **C.** Add a Lookup field on the Global Address object to the Account object.  [WRONG]
- [x] **D.** Add a Lookup field on the Account object to the Global Address object.  [CORRECT]

**Explanation:**
> Since a standard object like Account cannot be a detail in a Master-Detail Relationship, we should use a Lookup Relationship instead. To allow multiple Accounts to share a default pickup address, add a Lookup field on the Account object that points to the Global Address object. This setup enables each Account to reference a Global Address, supporting the business need by enhancing shipping efficiency and reducing costs.

---

### Question 17
A developer is creating a Lightning web component to show a list of sales records. The Sales Representative user should be able to see the commission field on each record. The Sales Assistant user should be able to see all fields on the record except the commission field. How should this be enforced so that the component works for both users without showing any errors?
- [ ] **A.** Use Lightning Data Service to get the collection of sales records.  [WRONG]
- [ ] **B.** Use WITH SECURITY_ENFORCED in the SOQL that fetches the data for the component.  [WRONG]
- [ ] **C.** Use Lightning Locker Service to enforce sharing rules and field-level security.  [WRONG]
- [x] **D.** Use Security.stripInaccessible to remove fields inaccessible to the current user.  [CORRECT]

**Explanation:**
> Use the stripInaccessible method to enforce field-level and object-level data protection. This method can be used to strip the fields and relationship fields from query and subquery results that the user can’t access. The method can also be used to remove inaccessible sObject fields before DML operations to avoid exceptions and to sanitize sObjects that have been deserialized from an untrusted source.

**Resources:**
> Enforce Security with the stripInaccessible Method

---

### Question 18
The sales management team at Universal Containers requires that the Lead Source field of the Lead record be populated when a Lead is converted. What should be done to ensure that a user populates the Lead Source field prior to converting a Lead?
- [ ] **A.** Create an after trigger on Lead  [WRONG]
- [x] **B.** Use a Validation Rule  [CORRECT]
- [ ] **C.** Use a Formula Field  [WRONG]
- [ ] **D.** Use Lead Conversion field mapping  [WRONG]

**Explanation:**
> A validation rule can enforce that the Lead Source field is populated by preventing the Lead from being saved or converted if the field is empty. This ensures that users must fill in the Lead Source field before proceeding with the conversion.

---

### Question 19
A PrimaryId__c custom field exists on the Candidate__c custom object. The field is used to store each candidate's id number and is marked as Unique in the schema definition. As part of a data enrichment process, Universal Containers has a CSV file that contains updated data for all candidates in the system. The file contains each Candidate's social security number as a data point. Universal Containers wants to upload this information into Salesforce, while ensuring all data rows are correctly mapped to a candidate in the system. Which technique should the developer implement to streamline the data upload?
- [x] **A.** Update the PrimaryId__c field definition to mark it as an External Id.  [CORRECT]
- [ ] **B.** Upload the CSV into a custom object related to Candidate__c.  [WRONG]
- [ ] **C.** Create a before save flow to correctly map the records.  [WRONG]
- [ ] **D.** Create a before insert trigger to correctly map the records.  [WRONG]

**Explanation:**
> Marking the PrimaryId__c field as an External Id allows Salesforce to use this field as a unique identifier for matching records during data import. This ensures that the data from the CSV file is correctly mapped to the existing candidate records based on their unique IDs.

---

### Question 20
When a Task is created for a Contact, how can a developer prevent the task from being included on the Activity Timeline of the Contact's Account record?
- [x] **A.** In Activity Setting, uncheck Roll up activities to a contact's primary account.  [CORRECT]
- [ ] **B.** Create a Task trigger to set the Account field to NULL.  [WRONG]
- [ ] **C.** Use Process Builder to create a process to set the Task Account field to blank.  [WRONG]
- [ ] **D.** By default, tasks do not display on the Account Activity Timeline.  [WRONG]

**Explanation:**
> This setting ensures that tasks created for a Contact are not rolled up to the Activity Timeline of the Contact’s associated Account.

**Resources:**
> Considerations for Disabling Roll Up of Activities to a Contact’s Primary Account

---

### Question 21
What is the requirement for a class to be used as a custom Visualforce controller?
- [ ] **A.** Any top-level Apex class that has a constructor that returns a PageReference  [WRONG]
- [ ] **B.** Any top-level Apex class that extends a PageReference  [WRONG]
- [x] **C.** Any top-level Apex class that has a default, no-argument constructor  [CORRECT]
- [ ] **D.** Any top-level Apex class that implements the controller interface  [WRONG]

**Explanation:**
> A custom controller is an Apex class that uses the default, no-argument constructor for the outer, top-level class.

**Resources:**
> Build a Custom Controller

---

### Question 22
In order to override a standard action with a Visualforce page, which attribute must be defined in the <apex:page> tag?
- [ ] **A.** pageReference  [WRONG]
- [ ] **B.** override  [WRONG]
- [ ] **C.** controller  [WRONG]
- [x] **D.** standardController  [CORRECT]

**Explanation:**
> When overriding buttons with a Visualforce page, you must use the standard controller for the object on which the button appears. For example, to use a page to override the Edit button on accounts, the page markup must include the standardController="Account" attribute on the <apex:page> tag.

**Resources:**
> Overriding Buttons, Links, and Tabs with Visualforce

---

### Question 23
A developer needs to provide a way to mass edit, update, and delete records from a list view. In which two ways can this be accomplished? (Choose two.)
- [x] **A.** Create a new Visualforce page and Apex Controller for the list view that provides mass edit, update, and delete functionality.  [CORRECT]
- [x] **B.** Download a managed package from the AppExchange that provides customizable Enhanced List Views and buttons.  [CORRECT]
- [ ] **C.** Download an unmanaged package from the AppExchange that provides customizable mass edit, update, and delete functionality.  [WRONG]
- [ ] **D.** Configure the user interface and enable both inline editing and enhanced lists.  [WRONG]

---

### Question 24
What is a benefit of using a trigger framework?
- [ ] **A.** Reduces trigger execution time  [WRONG]
- [ ] **B.** Allows functional code to be tested by a test class  [WRONG]
- [ ] **C.** Increases trigger governor limits  [WRONG]
- [x] **D.** Simplifies addition of context-specific logic  [CORRECT]

**Explanation:**
> The primary benefit of using a trigger framework in Salesforce is that it simplifies the addition of context-specific logic. A trigger framework helps organize and manage complex trigger logic, making it easier to add, modify, and maintain code. This approach promotes best practices and ensures that triggers are scalable and maintainable.

**Resources:**
> Implement Frameworks

---

### Question 25
The sales management team at Universal Containers requires that the Lead Source field of the Lead record be populated when a Lead is converted. What should be used to ensure that a user populates the Lead Source field prior to converting a Lead?
- [ ] **A.** Workflow Rule  [WRONG]
- [x] **B.** Validation Rule  [CORRECT]
- [ ] **C.** Formula Field  [WRONG]
- [ ] **D.** Process Builder  [WRONG]

**Explanation:**
> To ensure that the Lead Source field is populated before a Lead is converted, you should use a Validation Rule. A validation rule can enforce that the Lead Source field is not left blank by preventing the conversion process until the field is populated.

**Resources:**
> Considerations for Converting Leads

---

### Question 26
A company has been adding data to Salesforce and has not done a good job of limiting the creation of duplicate Lead records. The developer is considering writing an Apex process to identify duplicates and merge the records together. Which two statements are valid considerations when using merge? (Choose two.)
- [x] **A.** The merge method allows up to three records, including the master and two additional records with the same sObject type, to be merged into the master record.  [CORRECT]
- [x] **B.** Merge is supported with accounts, contacts, cases, and leads.  [CORRECT]
- [ ] **C.** External ID fields can be used with the merge method.  [WRONG]
- [ ] **D.** The field values on the master record are overwritten by the records being merged.  [WRONG]

**Explanation:**
> The two valid considerations when using the merge method in Salesforce are:
> The merge method allows up to three records, including the master and two additional records with the same sObject type, to be merged into the master record. This is a key feature of the merge operation, allowing consolidation of up to three records.
> Merge is supported with accounts, contacts, cases, and leads. These are the standard objects that support the merge operation in Salesforce.

---

### Question 27
A developer created this Apex trigger that calls MyClass.myStaticMethod:
trigger myTrigger on Contact(before insert){
MyClass.myStaticMethod(trigger.new, trigger.oldMap);
}
The developer creates a test class with a test method that calls MyClass.myStaticMethod, resulting in 81% overall code coverage.
What happens when the developer tries to deploy the trigger and two classes to production, assuming no other code exists?
- [ ] **A.** The deployment fails because no assertions were made in the test method.  [WRONG]
- [ ] **B.** The deployment passes because both classes and the trigger were included in the deployment.  [WRONG]
- [ ] **C.** The deployment passes because the Apex code has required (>75%) code coverage.  [WRONG]
- [x] **D.** The deployment fails because the Apex trigger has no code coverage.  [CORRECT]

**Explanation:**
> Even though the overall code coverage is 81%, the specific Apex trigger itself must have code coverage. In Salesforce, each trigger must be covered by tests, and the deployment will fail if any trigger has 0% coverage.

**Resources:**
> Testing and Code Coverage

---

### Question 28
What are three considerations when using the @InvocableMethod annotation in Apex? (Choose three.)
- [x] **A.** A method using the @InvocableMethod annotation must be declared as static.  [CORRECT]
- [x] **B.** A method using the @InvocableMethod annotation can be declared as Public or Global.  [CORRECT]
- [ ] **C.** A method using the @InvocableMethod annotation can have multiple input parameters.  [WRONG]
- [ ] **D.** A method using the @InvocableMethod annotation must define a return value.  [WRONG]
- [x] **E.** Only one method using the @InvocableMethod annotation can be defined per Apex class.  [CORRECT]

**Explanation:**
> InvocableMethod Considerations
> The invocable method must be static and public or global, and its class must be an outer class.
> Only one method in a class can have the InvocableMethod annotation.
> Other annotations can’t be used with the InvocableMethod annotation.

**Resources:**
> InvocableMethod Annotation

---

### Question 29
A team of developers is working on a source-driven project that allows them to work independently, with many different org configurations. Which type of Salesforce orgs should they use for their development?
- [ ] **A.** Developer orgs  [WRONG]
- [ ] **B.** Developer sandboxes  [WRONG]
- [ ] **C.** Full Copy sandboxes  [WRONG]
- [x] **D.** Scratch orgs  [CORRECT]

**Explanation:**
> The scratch org is a source-driven and disposable deployment of Salesforce code and metadata. A scratch org is fully configurable, allowing developers to emulate different Salesforce editions with different features and settings. You can share the scratch org configuration file with other team members, so you all have the same basic org in which to do your development. In addition to code and metadata, developers can install packages and deploy synthetic or dummy data for testing. Don’t add personal data to scratch orgs.

**Resources:**
> Scratch Orgs

---

### Question 30
A developer executes the following query in Apex to retrieve a list of contacts for each account: List<account> accounts = [Select ID, Name, (Select ID, Name from Contacts) from Account]; Which two exceptions may occur when it executes? (Choose two.)
- [ ] **A.** CPU limit exception due to the complexity of the query.  [WRONG]
- [x] **B.** SOQL query row limit exception due to the number of contacts.  [CORRECT]
- [ ] **C.** SOQL query limit exception due to the number of contacts.  [WRONG]
- [x] **D.** SOQL query row limit exception due to the number of accounts.  [CORRECT]

**Explanation:**
> SOQL query row limit exception due to the number of contacts (B): Salesforce imposes a limit on the total number of rows that can be retrieved by a single SOQL query. If the number of contacts retrieved exceeds this limit, a row limit exception will occur.
> SOQL query row limit exception due to the number of accounts: Similarly, if the number of accounts retrieved exceeds the row limit, this will also trigger a row limit exception.

**Resources:**
> SOQL and SOSL Queries

---

### Question 31
Universal Containers wants to assess the advantages of declarative development versus programmatic customization for specific use cases in its Salesforce implementation. What are two advantages of declarative development over programmatic customization? (Choose two.)
- [ ] **A.** Declarative development has higher design limits and query limits.  [WRONG]
- [x] **B.** Declarative development does not require Apex test classes.  [CORRECT]
- [ ] **C.** Declarative development does not require maintenance.  [WRONG]
- [x] **D.** Declarative development can be updated in production using the Setup UI.  [CORRECT]

**Explanation:**
> Declarative development does not require Apex test classes: Declarative tools like workflows, process builders, and flows do not require the creation of test classes, which simplifies the development and deployment process.
> Declarative development can be updated in production using the Setup UI: Declarative changes can be made directly in the production environment through the Salesforce Setup UI, allowing for quicker and easier updates without the need for a deployment process.

---

### Question 32
A developer is asked to create a PDF quote document formatted using the company's branding guidelines, and automatically save it to the Opportunity record. Which two ways should a developer create this functionality? (Choose two.)
- [x] **A.** Install an application from the AppExchange to generate documents.  [CORRECT]
- [x] **B.** Create a Visualforce page with custom styling.  [CORRECT]
- [ ] **C.** Create an email template and use it in Process Builder.  [WRONG]
- [ ] **D.** Create a visual flow that implements the company's formatting.  [WRONG]

**Explanation:**
> The two ways a developer can create this functionality are:
> Install an application from the AppExchange to generate documents: There are several applications available on the AppExchange that can help generate PDF documents with custom branding and save them to records automatically. These apps often come with pre-built templates and functionalities that simplify the process.
> Create a Visualforce page with custom styling: By creating a Visualforce page, a developer can have full control over the styling and formatting of the PDF document. This approach allows for the customization needed to adhere to the company’s branding guidelines

---

### Question 33
What should be used to create scratch orgs?
- [ ] **A.** Developer Console  [WRONG]
- [x] **B.** Salesforce CLI  [CORRECT]
- [ ] **C.** Workbench  [WRONG]
- [ ] **D.** Sandbox refresh  [WRONG]

**Explanation:**
> Salesforce CLI (Command Line Interface) is the tool used to create and manage scratch orgs. It allows developers to easily spin up scratch orgs, configure them, and manage their lifecycle through command-line commands.

**Resources:**
> Create Scratch Orgs

---

### Question 34
Which Apex class contains methods to return the amount of resources that have been used for a particular governor, such as the number of DML statements?
- [ ] **A.** Exception  [WRONG]
- [ ] **B.** Messaging  [WRONG]
- [ ] **C.** OrgLimits  [WRONG]
- [x] **D.** Limits  [CORRECT]

**Explanation:**
> The Limits methods return the specific limit for the particular governor, such as the number of calls of a method or the amount of heap size remaining.
> Because Apex runs in a multitenant environment, the Apex runtime engine strictly enforces a number of limits to ensure that runaway Apex doesn’t monopolize shared resources.

**Resources:**
> Limits Class

---

### Question 35
If Apex code executes inside the execute() method of an Apex class when implementing the Batchable interface, which two statements are true regarding governor limits? (Choose two.)
- [x] **A.** The Apex governor limits are reset for each iteration of the execute() method.  [CORRECT]
- [ ] **B.** The Apex governor limits cannot be exceeded due to the asynchronous nature of the transaction.  [WRONG]
- [x] **C.** The Apex governor limits might be higher due to the asynchronous nature of the transaction.  [CORRECT]
- [ ] **D.** The Apex governor limits are relaxed while calling the constructor of the Apex class.  [WRONG]

**Explanation:**
> Each execution of a batch Apex job is considered a discrete transaction, and the governor limits are reset for each transaction.
> Batch Apex operates asynchronously, which can allow for higher governor limits compared to synchronous transactions.

**Resources:**
> Using Batch Apex

---

### Question 36
What are three characteristics of change set deployments? (Choose three.)
- [x] **A.** They require a deployment connection.  [CORRECT]
- [ ] **B.** They can be used to transfer records.  [WRONG]
- [x] **C.** They can be used only between related organizations.  [CORRECT]
- [ ] **D.** They can be used to deploy custom settings data.  [WRONG]
- [x] **E.** They use an all or none deployment model.  [CORRECT]

**Explanation:**
> Change sets can only be sent between Salesforce orgs that have an established deployment connection.
> Change sets can be used only between related organizations, such as a production org and its sandbox, or two sandboxes created from the same production org.
> Change sets are deployed as a single transaction, meaning if any part of the deployment fails, the entire change set is rolled back.

**Resources:**
> Change Sets

---

### Question 37
Consider the following code snippet:
public static List<Lead> obtainAllFields(Set<Id> leadIds){
List<Lead> result = new List<Lead>();
for(Id leadId : leadIds){
result.add([SELECT FIELDS(ALL) FROM Lead WHERE Id =:leadId]);
}
return result;
}
Given the multi-tenant architecture of the Salesforce platform, what is a best practice a developer should implement and ensure successful execution of the method?
- [x] **A.** Avoid performing queries Inside for loops.  [CORRECT]
- [ ] **B.** Avoid executing queries without a limit clause.  [WRONG]
- [ ] **C.** Avoid using variables as query filters.  [WRONG]
- [ ] **D.** Avoid returning an empty List of records.  [WRONG]

**Explanation:**
> Performing queries inside for loops can lead to hitting governor limits, as it results in a separate query for each iteration of the loop. This can quickly exceed the allowed number of SOQL queries per transaction.

---

### Question 38
Refer to the following Apex code:
Integer x = 0;
do{
x = 1;
x++;
}
while(x < 1);
System.debug(x);
What is the value of x when it is written to the debug log?
- [ ] **A.** 0  [WRONG]
- [ ] **B.** 1  [WRONG]
- [x] **C.** 2  [CORRECT]
- [ ] **D.** 3  [WRONG]

**Explanation:**
> The loop executes once, setting x to 1 and then incrementing it to 2. After the loop finishes, x has the value 2, which is then written to the debug log.

---

### Question 39
A developer needs to test an Invoicing system integration. After reviewing the number of transactions required for the test, the developer estimates that the test data will total about 2 GB of data storage. Production data is not required for the integration testing. Which two environments meet the requirements for testing? (Choose two)
- [ ] **A.** Developer Sandbox  [WRONG]
- [x] **B.** Full Sandbox  [CORRECT]
- [ ] **C.** Developer Edition  [WRONG]
- [x] **D.** Partial Sandbox  [CORRECT]
- [ ] **E.** Developer Pro Sandbox  [WRONG]

**Explanation:**
> Full Sandbox(Data storage: Same as your production org): Full sandboxes are a complete copy of your production org, including all data, metadata, and customizations. This means they can handle large amounts of data and provide a realistic environment for testing integrations.
> Partial Sandbox(Data storage: 5 GB): Partial sandboxes are smaller copies of your production org, but they can still handle a significant amount of data. The exact size limit depends on your organization's specific settings, but partial sandboxes are generally sufficient for testing integrations with moderate amounts of data.

**Resources:**
> Sandbox Licenses and Storage Limits by Type

---

### Question 40
Universal Containers hires a developer to build a custom search page to help users find the Accounts they want. Users will be able to search on Name, Description, and a custom comments field. Which consideration should the developer be aware of when deciding between SOQL and SOSL? (Choose two.)
- [x] **A.** SOSL is faster for text searches.  [CORRECT]
- [x] **B.** SOQL is able to return more records.  [CORRECT]
- [ ] **C.** SOQL is faster for text searches.  [WRONG]
- [ ] **D.** SOSL is able to return more records.  [WRONG]

**Explanation:**
> SOQL vs. SOSL Queries
> Search can be accessed with SOQL or SOSL queries. SOQL is Force.com's database query language, similar to SQL. You can use SOQL to query child-to-parent relationships, which are often many-to-one, and to query parent-to-child relationships, which are almost always one-to-many.
> SOSL is Force.com's full-text search language. SOSL can tokenize multiple terms within a field, and can build a search index off of this. If you’re searching for a specific distinct term that you know exists within a field, you might find SOSL faster than SOQL. However, for each Apex transaction, the governor limit for multiple SOSL searches in a single transaction is 2,000 (Note: It is common to only need a single search, in which case the limit is 40,000); for SOQL queries it’s 50,000. So if you need to retrieve more than 2,000 records, SOQL is the better choice.

**Resources:**
> Introduction to SOQL and SOSL

---

### Question 41
Considering the following code snippet:
public static void insertAccounts(ListAccount theseAccounts){
for(Account thisAccount : theseAccounts){
if(thisAccount.website == null){
thisAccount.website = 'https://www.test.com';
}
}
update theseAccounts;
}
When the code executes, a DML exception is thrown.
How should the developer modify the code to ensure exceptions are handled gracefully?
- [ ] **A.** Implement Change Data Capture.  [WRONG]
- [ ] **B.** Implement the upsert DML statement.  [WRONG]
- [ ] **C.** Remove null items from the list of Accounts.  [WRONG]
- [x] **D.** Implement a try/catch block for the DML.  [CORRECT]

**Explanation:**
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

---

### Question 42
When using SalesforceDX, what does a developer need to enable to create and manage scratch orgs?
- [ ] **A.** Production  [WRONG]
- [ ] **B.** Environment Hub  [WRONG]
- [x] **C.** Dev Hub  [CORRECT]
- [ ] **D.** Sandbox  [WRONG]

**Explanation:**
> To create and manage scratch orgs using SalesforceDX, a developer needs to enable the Dev Hub. The Dev Hub is the central place for managing your scratch orgs and is essential for using SalesforceDX tools.

**Resources:**
> Scratch Orgs

---

### Question 43
Where are two locations a developer can look to find information about the status of batch or future calls? (Choose two.)
- [ ] **A.** Developer Console  [WRONG]
- [x] **B.** Apex Flex Queue  [CORRECT]
- [x] **C.** Apex Jobs  [CORRECT]
- [ ] **D.** Paused Flow Interviews component  [WRONG]

**Explanation:**
> The Apex Jobs page shows all asynchronous Apex jobs with information about each job’s execution. You can also monitor the status of Apex jobs in the Apex Flex Queue, and reorder them to control which jobs are processed first.

**Resources:**
> Monitor Asynchronous Apex

---

### Question 44
A Salesforce Administrator used Flow Builder to create a flow named 'accountOnboarding'. The flow must be used inside an Aura component. Which tag should a developer use to display the flow in the component?
- [ ] **A.** lightning-flow  [WRONG]
- [ ] **B.** aura-flow  [WRONG]
- [x] **C.** lightning:flow  [CORRECT]
- [ ] **D.** aura:flow  [WRONG]

**Explanation:**
> To display a flow inside an Aura component, the developer should use the <lightning:flow> tag. This tag is specifically designed to embed flows within Aura components.

**Resources:**
> Embed a Flow in a Custom Aura Component

---

### Question 45
A developer must create a CreditCardPayment class that provides an implementation of an existing Payment class.
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
}

**Explanation:**
> The CreditCardPayment class should extend the Payment class and override the makePayment method to provide its specific implementation.

---

### Question 46
How should a developer make sure that a child record on a custom object, with a lookup to the Account object, has the same sharing access as its associated account?
- [ ] **A.** Create a Sharing Rule comparing the custom object owner to the account owner.  [WRONG]
- [ ] **B.** Create a validation rule on the custom object comparing the record owners on both records.  [WRONG]
- [ ] **C.** Include the sharing related list on the custom object page layout.  [WRONG]
- [x] **D.** Ensure that the relationship between the objects is Master-Detail.  [CORRECT]

**Explanation:**
> When you set up a Master-Detail relationship, the child record inherits the sharing and security settings of the parent record. This means that if a user has access to the parent record (in this case, the Account), they will automatically have the same level of access to the child records (the custom object records).

---

### Question 47
Universal Containers wants a list button to display a Visualforce page that allows users to edit multiple records. Which Visualforce feature supports this requirement?
- [ ] **A.** <apex:listButton> tag  [WRONG]
- [x] **B.** recordSetVar page attribute  [CORRECT]
- [ ] **C.** custom controller  [WRONG]
- [ ] **D.** controller extension  [WRONG]

**Explanation:**
> The recordSetVar attribute in Visualforce allows you to work with a collection of records. This is particularly useful for creating pages that enable users to edit multiple records at once. By using recordSetVar, you can pass a set of records to your Visualforce page and then iterate over them to display and edit each record.

**Resources:**
> Associating a Standard List Controller with a Visualforce Page

---

### Question 48
Which code in a Visualforce page and/or controller might present a security vulnerability?
A . <apex:outputField value="{!ctrl.userInput}" />
B . <apex:outputText escape="false" value=" {!$CurrentPage.parameters.userInput}" />
C . <apex:outputText value="{!£CurrentPage.parameters.userInput}" />
D . <apex:outputField escape="false" value="{!ctrl.userInput}" />

**Explanation:**
> Disabling Escape on Visualforce Tags
> By default, nearly all Visualforce tags escape the XSS-vulnerable characters. You can disable this behavior by setting the optional attribute escape="false". For example, this output is vulnerable to XSS attacks. When escape="false" is used, the input is not escaped, meaning any HTML or JavaScript code included in the user input will be rendered as-is, potentially allowing malicious scripts to be executed.

**Resources:**
> Security Guidelines for Apex and Visualforce Development

---

### Question 49
What should a developer do to check the code coverage of a class after running all tests?
- [ ] **A.** Select and run the class on the Apex Test Execution page in the Developer Console.  [WRONG]
- [x] **B.** View the code coverage percentage for the class using the Overall Code Coverage panel in the Developer Console Tests tab.  [CORRECT]
- [ ] **C.** View the Code Coverage column in the list view on the Apex Classes page.  [WRONG]
- [ ] **D.** View the Class Test Percentage tab on the Apex Class list view in Salesforce Setup.  [WRONG]

**Explanation:**
> After running tests, the Developer Console provides a comprehensive view of code coverage. The Overall Code Coverage panel in the Tests tab displays the code coverage percentage for each Apex class that has been included in a test run.

**Resources:**
> Testing and Code Coverage

---

### Question 50
Universal Containers decides to use exclusively declarative development to build out a new Salesforce application. Which three options should be used to build out the database layer for the application? (Choose three.)
- [ ] **A.** Flows  [WRONG]
- [x] **B.** Roll-up summaries  [CORRECT]
- [ ] **C.** Triggers  [WRONG]
- [x] **D.** Relationships  [CORRECT]
- [x] **E.** Custom objects and fields  [CORRECT]

**Explanation:**
> Database Layer
> Declarative: Custom Objects, Fields, Relationships, Rollups
> Coding: Apex Triggers

**Resources:**
> Understand Separation of Concerns

---

### Question 51
Which three statements are true regarding the @isTest annotation? (Choose three.)
- [x] **A.** A method annotated @isTest(SeeAllData=true) in a class annotated @isTest(SeeAllData=false) has access to all org data.  [CORRECT]
- [ ] **B.** A method annotated @isTest(SeeAllData=false) in a class annotated @isTest(SeeAllData=true) has access to all org data.  [WRONG]
- [ ] **C.** A class containing test methods counts toward the Apex code limit regardless of any @isTest annotation.  [WRONG]
- [ ] **D.** Products and Pricebooks are visible in a test even if a class is annotated @isTest(SeeAllData=false).  [WRONG]
- [x] **E.** Profiles are visible in a test even if a class is annotated @isTest(SeeAllData=false).  [CORRECT]

**Explanation:**
> Considerations for the @IsTest(SeeAllData=true) Annotation
> If a test class is defined with the @IsTest(SeeAllData=true) annotation, the SeeAllData=true applies to all test methods that don’t explicitly set the SeeAllData keyword.
> The @IsTest(SeeAllData=true) annotation is used to open up data access when applied at the class or method level. However, if the containing class has been annotated with @IsTest(SeeAllData=true), annotating a method with @IsTest(SeeAllData=false) is ignored for that method. In this case, that method still has access to all the data in the organization. Annotating a method with @IsTest(SeeAllData=true) overrides, for that method, an @IsTest(SeeAllData=false) annotation on the class.
> @IsTest(SeeAllData=true) and @IsTest(IsParallel=true) annotations can’t be used together on the same Apex method.

**Resources:**
> IsTest Annotation
> Using the isTest(SeeAllData=True) Annotation

---

### Question 52
The Job_Application__c custom object has a field that is a Master-Detail relationship to the Contact object, where the Contact object is the Master. As part of a feature implementation, a developer needs to retrieve a list containing all Contact records where the related Account Industry is 'Technology' while also retrieving the contact's Job_Application__c records. Based on the object's relationships, what is the most efficient statement to retrieve the list of contacts?
- [x] **A.** [SELECT Id, (SELECT Id FROM Job_Applications_r) FROM Contact WHERE Account.Industry = 'Technology'];  [CORRECT]
- [ ] **B.** [SELECT Id, (SELECT Id FROM Job_Applications_r) FROM Contact WHERE Accounts.Industry = 'Technology'];  [WRONG]
- [ ] **C.** [SELECT Id, (SELECT Id FROM Job_Applications_c) FROM Contact WHERE Accounts.Industry = 'Technology'];  [WRONG]
- [ ] **D.** [SELECT Id, (SELECT Id FROM Job_Application_c) FROM Contact WHERE Account.Industry = 'Technology'];  [WRONG]

**Explanation:**
> A: This query correctly references the relationship and filters based on the Account’s Industry
> B: This option is incorrect because the correct relationship name for the Account object is Account, not Accounts.
> C: This option is incorrect for two reasons: it uses Accounts instead of Account, and it incorrectly references Job_Applications_c instead of Job_Applications_r.
> D: This option is incorrect because it uses Job_Application_c instead of Job_Applications_r.

---

### Question 53
Which two SOSL searches will return records matching search criteria contained in any of the searchable text fields on an object? (Choose two.)
- [ ] **A.** [FIND 'Acme*' IN ANY FIELDS RETURNING Account, Opportunity];  [WRONG]
- [x] **B.** [FIND 'Acme*' RETURNING Account, Opportunity];  [CORRECT]
- [x] **C.** [FIND 'Acme*' IN ALL FIELDS RETURNING Account, Opportunity];  [CORRECT]
- [ ] **D.** [FIND 'Acme*' IN TEXT FIELDS RETURNING Account, Opportunity];  [WRONG]

**Resources:**
> Salesforce Object Search Language (SOSL)

---

### Question 54
A developer needs to save a List of existing Account records named myAccounts to the database, but the records do not contain Salesforce Id values. Only the value of a custom text field configured as an External ID with an API name of Foreign_Key__c is known. Which two statements enable the developer to save the records to the database without an Id? (Choose two.)
- [x] **A.** Upsert myAccounts Foreign_Key__c;  [CORRECT]
- [ ] **B.** Upsert myAccounts(Foreign_Key__c);  [WRONG]
- [x] **C.** Database.upsert (myAccounts, Foreign_Key__c);  [CORRECT]
- [ ] **D.** Database.upsert(myAccounts).Foreign_Key__c;  [WRONG]

**Resources:**
> Upserting Records
> Database Class

---

### Question 55
How should a developer avoid hitting the governor limits in test methods?
- [ ] **A.** Use @TestVisible on methods that create records.  [WRONG]
- [ ] **B.** Use Test.loadData() to load data from a static resource.  [WRONG]
- [ ] **C.** Use @IsTest (SeeAllData=true) to use existing data.  [WRONG]
- [x] **D.** Use Test.startTest() to reset governor limits.  [CORRECT]

**Explanation:**
> The Test.startTest() and Test.stopTest() methods are used to reset governor limits within test methods. This allows the developer to perform setup operations before Test.startTest() and then execute the actual test code within the new set of governor limits.

**Resources:**
> Using Limits, startTest, and stopTest

---

### Question 56
Universal Containers wants Opportunities to be locked from editing when reaching the Closed/Won stage. Which two strategies should a developer use to accomplish this? (Choose two.)
- [ ] **A.** Use a Flow Builder.  [WRONG]
- [x] **B.** Use a validation rule.  [CORRECT]
- [ ] **C.** Use the Process Automation Settings.  [WRONG]
- [x] **D.** Mark fields as read-only on the page layout.  [CORRECT]

**Explanation:**
> Using a validation rule  and marking fields as read-only on the page layout are indeed effective strategies to lock Opportunities from editing when they reach the Closed/Won stage.

---

### Question 57
A developer wants to display all of the picklist entries for the Opportunity StageName field and all of the available record types for the Opportunity object on a Visualforce page. Which two actions should the developer perform to get the available picklist values and record types in the controller? (Choose two.)
- [x] **A.** Use Schema.RecordTypeInfo returned by Opportunity.SObjectType.getDescribe().getRecordTypeInfos().  [CORRECT]
- [ ] **B.** Use Schema.PicklistEntry returned by Opportunity.SObjectType.getDescribe().getPicklistValues ().  [WRONG]
- [ ] **C.** Use Schema.RecordTypeInfo returned by RecordType.SObjectType.getDescribe().getRecordTypeInfos().  [WRONG]
- [x] **D.** Use Schema.PicklistEntry returned by Opportunity.StageName.getDescribe().getPicklistValues ().  [CORRECT]

**Explanation:**
> Use Schema.RecordTypeInfo returned by Opportunity.SObjectType.getDescribe().getRecordTypeInfos(): This will retrieve the available record types for the Opportunity object.
> Use Schema.PicklistEntry returned by Opportunity.StageName.getDescribe().getPicklistValues(): This will retrieve the picklist entries for the Opportunity StageName field.

**Resources:**
> RecordTypeInfo Class
> PicklistEntry Class

---

### Question 58
An org has two custom objects: Plan__c, that has a master-detail relationship to the Account object Plan_Item__c, that has a master-detail relationship to the Plan__c object. What should a developer use to create a Visualforce section on the Account page layout that displays all of the Plan__c records related to the Account and all of the Plan_Item__c records related to those Plan__c records?
- [ ] **A.** A standard controller with a custom controller  [WRONG]
- [x] **B.** A standard controller with a controller extension  [CORRECT]
- [ ] **C.** A controller extension with a custom controller  [WRONG]
- [ ] **D.** A custom controller by itself  [WRONG]

**Explanation:**
> Using a standard controller for the Account object allows you to leverage built-in functionality, while a controller extension can be used to add custom logic to retrieve and display the related Plan__c and Plan_Item__c records.

---

### Question 59
A developer uses a loop to check each Contact in a list. When a Contact with the Title of 'Boss' is found, the Apex method should jump to the first line of code outside of the for loop. Which Apex solution will let the developer implement this requirement?
- [ ] **A.** return;  [WRONG]
- [ ] **B.** continue;  [WRONG]
- [x] **C.** break;  [CORRECT]
- [ ] **D.** System.assert(false);  [WRONG]

**Explanation:**
> The break statement exits the loop immediately, allowing the code execution to continue from the first line outside the loop.

---

### Question 60
A business has a proprietary Order Management System (OMS) that creates orders from their website and fulfills the orders. When the order is created in the OMS, an integration also creates an order record in Salesforce and relates it to the contact as identified by the email on the order. As the order goes through different stages in the OMS, the integration also updates it in Salesforce. It is noticed that each update from the OMS creates a new order record in Salesforce. Which two actions will prevent the duplicate order records from being created in Salesforce? (Choose two.)
- [x] **A.** Use the order number from the OMS as an external ID.  [CORRECT]
- [ ] **B.** Write a before trigger on the order object to delete any duplicates.  [WRONG]
- [x] **C.** Ensure that the order number in the OMS is unique.  [CORRECT]
- [ ] **D.** Use the email on the contact record as an external ID.  [WRONG]

**Explanation:**
> Use the order number from the OMS as an external ID.
> By setting the order number as an external ID, Salesforce can recognize and update existing records instead of creating new ones.
> Ensure that the order number in the OMS is unique.
> Ensuring the uniqueness of the order number in the OMS helps maintain data integrity and prevents the creation of duplicate records.

---

### Question 1
What is the impact of declaring an Apex class using the `without sharing` keywords?
- [ ] **A.** Only records owned by the current user can be updated.  [WRONG]
- [x] **B.** Sharing restrictions for the current user are bypassed.  [CORRECT]
- [ ] **C.** Records created by the class cannot have sharing rules.  [WRONG]
- [ ] **D.** The class can only be used by users with developer rights.  [WRONG]

**Explanation:**
> Declaring an Apex class using the without sharing keywords means that the class runs in system mode, bypassing the sharing rules of the current user.

**Resources:**
> Using the with sharing, without sharing, and inherited sharing Keywords

---

### Question 2
A developer needs to find information about @future methods that were invoked. From which system monitoring feature can the developer see this information?
- [ ] **A.** Scheduled Jobs  [WRONG]
- [x] **B.** Apex Jobs  [CORRECT]
- [ ] **C.** Background Jobs  [WRONG]
- [ ] **D.** Asynchronous Jobs  [WRONG]

**Explanation:**
> Apex Jobs allows developers to monitor the status of @future methods, along with other asynchronous processes like batch jobs and scheduled jobs.

---

### Question 3
A developer has a requirement to create an Order when an Opportunity reaches a 'Closed-Won' status. Which tool should be used to implement this requirement?
- [ ] **A.** Lightning Component  [WRONG]
- [x] **B.** Apex Trigger  [CORRECT]
- [ ] **C.** Flow Builder  [WRONG]
- [ ] **D.** Process Builder  [WRONG]

**Explanation:**
> Process Builder is a powerful tool in Salesforce that allows you to automate business processes. It can be used to create an Order automatically when an Opportunity reaches the ‘Closed-Won’ status without writing any code.

---

### Question 4
Universal Containers has a Visualforce page that displays a table of every Container__c being rented by a given Account. Recently this page is failing with a view state limit because some of the customers rent over 10,000 containers. What should a developer change about the Visualforce page to help with the page load errors?
- [ ] **A.** Use lazy loading and a transient List variable.  [WRONG]
- [ ] **B.** Use JavaScript remoting with SOQL Offset.  [WRONG]
- [x] **C.** Implement pagination with a StandardSetController.  [CORRECT]
- [ ] **D.** Implement pagination with an OffsetController.  [WRONG]

**Explanation:**
> Implement pagination with a StandardSetController. This approach helps manage large datasets by loading only a subset of records at a time, significantly reducing the view state size and improving page performance.

**Resources:**
> StandardSetController Class

---

### Question 5
What are three techniques that a developer can use to invoke an anonymous block of code? (Choose three.)
- [x] **A.** Use the SOAP API to make a call to execute anonymous code.  [CORRECT]
- [ ] **B.** Create a Visualforce page that uses a controller class that is declared without sharing.  [WRONG]
- [x] **C.** Run code using the Anonymous Apex feature of the Developer's IDE.  [CORRECT]
- [x] **D.** Type code into the Developer Console and execute it directly.  [CORRECT]
- [ ] **E.** Create and execute a test method that does not specify a runAs() call.  [WRONG]

**Resources:**
> Anonymous Blocks

---

### Question 6
A developer has two custom controller extensions where each has a save() method.
<Apex:page standardController="Account", extensions="ExtensionA, ExtensionB">
<apex:commandButton action="{!save}" value="Save"/>
</apex:page>
Which save() method will be called for the following Visualforce page?
- [x] **A.** ExtensionA save()  [CORRECT]
- [ ] **B.** ExtensionB save()  [WRONG]
- [ ] **C.** standard controller save()  [WRONG]
- [ ] **D.** Runtime error will be generated  [WRONG]

**Explanation:**
> When multiple controller extensions are specified, the methods in the first extension listed (in this case, ExtensionA) take precedence and will be called.

**Resources:**
> Building a Controller Extension

---

### Question 7
A developer needs to create a Visualforce page that displays Case data. The page will be used by both support reps and support managers. The Support Rep profile does not allow visibility of the Customer_Satisfaction__c field, but the Support Manager profile does. How can the developer create the page to enforce Field Level Security and keep future maintenance to a minimum?
- [x] **A.** Create one Visualforce Page for use by both profiles.  [CORRECT]
- [ ] **B.** Use a new Support Manager permission set.  [WRONG]
- [ ] **C.** Create a separate Visualforce Page for each profile.  [WRONG]
- [ ] **D.** Use a custom controller that has the with sharing keywords.  [WRONG]

**Explanation:**
> The best approach to enforce Field Level Security (FLS) and minimize future maintenance is to create one Visualforce Page for use by both profiles . When using Visualforce pages, the platform indeed enforces CRUD and FLS automatically when SObjects and SObject fields are referenced directly. This means that creating a single Visualforce page will handle field visibility based on the user’s profile permissions.
> Note: Using a custom controller with the with sharing keyword ensures record-level security, but for field-level security.

---

### Question 8
Which three steps allow a custom SVG to be included in a Lightning web component? (Choose three.)
- [x] **A.** Upload the SVG as a static resource.  [CORRECT]
- [x] **B.** Reference the getter in the HTML template.  [CORRECT]
- [ ] **C.** Import the SVG as a content asset file.  [WRONG]
- [x] **D.** Import the static resource and provide a getter for it in JavaScript.  [CORRECT]
- [ ] **E.** Reference the import in the HTML template.  [WRONG]

**Resources:**
> Use SVG Resources

---

### Question 9
A custom Visualforce controller calls the ApexPages.addMessage() method, but no messages are rendering on the page. Which component should be added to the Visualforce page to display the message?
- [ ] **A.** <apex:message for="info"/>  [WRONG]
- [ ] **B.** <apex:facet name="messages" />  [WRONG]
- [ ] **C.** <apex:pageMessage severity="info" />  [WRONG]
- [x] **D.** <apex:pageMessages />  [CORRECT]

**Explanation:**
> To display messages added by the ApexPages.addMessage() method, you should use the <apex:pageMessages /> component. This component displays all messages that were generated for all components on the current page, using Salesforce’s standard styling.

**Resources:**
> apex:pageMessages

---

### Question 10
A Licensed_Professional__c custom object exists in the system with two Master-Detail fields for the following objects: Certification__c and Contact.
Users with the 'Certification Representative' role can access the Certification records they own and view the related Licensed Professionals records, however users with the 'Sales Representative' role report they cannot view any Licensed Professional records even though they own the associated Contact record. What are two likely causes of users in the 'Sales Representative' role not being able to access the Licensed Professional records? (Choose two.)
- [x] **A.** The organization has a private sharing model for Certification__c and Certification__c is the primary relationship in the Licensed_Professional__c object.  [CORRECT]
- [x] **B.** The organization's sharing rules for Licensed_Professional__c have not finished their recalculation process.  [CORRECT]
- [ ] **C.** The organization recently modified the Sales Representative role to restrict Read/Write access to Licensed_Professional__c.  [WRONG]
- [ ] **D.** The organization has a private sharing model for Certification__c, and Contact is the primary relationship in the Licensed_Professional__c object.  [WRONG]

**Resources:**
> Recalculate Sharing Rules Manually
> Considerations for Object Relationships

---

### Question 11
A developer considers the following snippet of code:
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
Based on this code, what is the value of x?
- [ ] **A.** 1  [WRONG]
- [ ] **B.** 2  [WRONG]
- [ ] **C.** 3  [WRONG]
- [x] **D.** 4  [CORRECT]

**Explanation:**
> In the given code snippet, the variable isOK is declared but not initialized, so its value is null by default. Let’s analyze the conditions:
> 1. if(isOK == false && theString == 'Hello'): This condition is false because isOK is null.
> 2. else if(isOK == true && theString == 'Hello'): This condition is also false because isOK is null.
> 3. else if(isOK != null && theString == 'Hello'): This condition is false because isOK is null.
> 4. else: This block will execute because none of the previous conditions are true.
> Therefore, the value of x will be set to 4.

---

### Question 12
A developer needs to include a Visualforce page in the detail section of a page layout for the Account object, but does not see the page as an available option in the Page Layout Editor. Which attribute must the developer include in the tag to ensure the Visualforce page can be embedded in a page layout?
- [x] **A.** standardController= "Account"  [CORRECT]
- [ ] **B.** extensions= "AccountController"  [WRONG]
- [ ] **C.** controller= "Account"  [WRONG]
- [ ] **D.** action= "AccountId"  [WRONG]

**Explanation:**
> To ensure the Visualforce page can be embedded in a page layout for the Account object, the developer must include the attribute standardController="Account" in the <apex:page> tag.

---

### Question 13
Which two operations can be performed using a formula field? (Choose two.)
- [ ] **A.** Displaying the last four digits of an encrypted Social Security number  [WRONG]
- [ ] **B.** Triggering a Process Builder  [WRONG]
- [x] **C.** Displaying an Image based on the Opportunity Amount  [CORRECT]
- [x] **D.** Calculating a score on a Lead based on the information from another field  [CORRECT]

**Explanation:**
> Displaying an Image based on the Opportunity Amount: Formula fields can display different images based on certain criteria.
> Calculating a score on a Lead based on the information from another field: Formula fields can perform calculations using data from other fields.

**Resources:**
> Formula Operators and Functions by Context

---

### Question 14
Application Events follow the traditional publish-subscribe model. Which method is used to fire an event?
- [ ] **A.** registerEvent()  [WRONG]
- [ ] **B.** fireEvent()  [WRONG]
- [ ] **C.** emit()  [WRONG]
- [x] **D.** fire()  [CORRECT]

**Explanation:**
> To fire an application event in Salesforce, you use the fire() method.

**Resources:**
> Fire Application Events

---

### Question 15
A developer needs to implement the functionality for a service agent to gather multiple pieces of information from a customer in order to send a replacement credit card. Which automation tool meets these requirements?
- [ ] **A.** Lightning Component  [WRONG]
- [x] **B.** Flow Builder  [CORRECT]
- [ ] **C.** Process Builder  [WRONG]
- [ ] **D.** Approval Process  [WRONG]

**Explanation:**
> To gather multiple pieces of information from a customer and send a replacement credit card, the best automation tool to use is Flow Builder. Flow Builder allows you to create guided, interactive processes for users, making it ideal for collecting information through a series of steps.

---

### Question 16
Einstein Next Best Action is configured at Universal Containers to display recommendations to internal users on the Account detail page. If the recommendation is approved, a new opportunity record and task should be generated. If the recommendation is rejected, an Apex method must be executed to perform a callout to an external system. Which three factors should a developer keep in mind when implementing the Apex method? (Choose three.)
- [ ] **A.** The method must use the @AuraEnabled annotation.  [WRONG]
- [x] **B.** The method must use the @InvokableMethod annotation.  [CORRECT]
- [x] **C.** The method must be defined as static.  [CORRECT]
- [x] **D.** The method must be defined as public.  [CORRECT]
- [ ] **E.** The method must use the @Future annotation  [WRONG]

**Explanation:**
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

---

### Question 17
An Opportunity needs to have an amount rolled up from a custom object that is not in a master-detail relationship. How can this be achieved?
- [ ] **A.** Use the Metadata API to create real-time roll-up summaries.  [WRONG]
- [ ] **B.** Use the Streaming API to create real-time roll-up summaries.  [WRONG]
- [ ] **C.** Write a trigger on the Opportunity object and use tree sorting to sum the amount for all related child objects under the Opportunity.  [WRONG]
- [x] **D.** Write a trigger on the child object and use an aggregate function to sum the amount for all related child objects under the Opportunity.  [CORRECT]

**Explanation:**
> The correct approach to roll up an amount from a custom object that is not in a master-detail relationship is: Write a trigger on the child object and use an aggregate function to sum the amount for all related child objects under the Opportunity. This trigger will ensure that whenever a child object is inserted, updated, deleted, or undeleted, the corresponding Opportunity’s amount is updated accordingly.

---

### Question 18
A developer at Universal Containers is tasked with implementing a new Salesforce application that must be able to be maintained completely by their company's Salesforce administrator. Which three options should be considered for building out the business logic layer of the application? (Choose three.)
- [x] **A.** Process Builder  [CORRECT]
- [ ] **B.** Scheduled Jobs  [WRONG]
- [x] **C.** Invocable Actions  [CORRECT]
- [ ] **D.** Workflows  [WRONG]
- [x] **E.** Validation Rules  [CORRECT]

---

### Question 19
Universal Containers (UC) uses a custom object called Vendor. The Vendor custom object has a Master-Detail relationship with the standard Account object. Based on some internal discussions, the UC administrator tried to change the Master-Detail relationship to a Lookup relationship but was not able to do so. What is a possible reason that this change was not permitted?
- [ ] **A.** The Vendor records have existing values in the Account object.  [WRONG]
- [ ] **B.** The Account object is included on a workflow on the Vendor object.  [WRONG]
- [x] **C.** The Account records contain Vendor roll-up summary fields.  [CORRECT]
- [ ] **D.** The Vendor object must use a Master-Detail field for reporting.  [WRONG]

**Explanation:**
> You cannot change a Master-Detail relationship to a Lookup relationship if there are roll-up summary fields on the parent object that summarize data from the child object. These roll-up summary fields must be deleted before the relationship type can be changed.

---

### Question 20
When is an Apex Trigger required instead of a Process Builder Process?
- [ ] **A.** When a record needs to be created  [WRONG]
- [ ] **B.** When multiple records related to the triggering record need to be updated  [WRONG]
- [ ] **C.** When a post to Chatter needs to be created  [WRONG]
- [x] **D.** When an action needs to be taken on a delete or undelete, or before a DML operation is executed.  [CORRECT]

**Explanation:**
> Process Builder cannot handle delete or undelete events, nor can it execute actions before a DML operation. Triggers are necessary for these scenarios as they provide more granular control over the timing and conditions of the actions.

---

### Question 21
A company wants to create an employee rating program that allows employees to rate each other. An employee's average rating must be displayed on the employee record. Employees must be able to create rating records, but are not allowed to create employee records. Which two actions should a developer take to accomplish this task? (Choose two.)
- [x] **A.** Create a trigger on the Rating object that updates a fields on the Employee object.  [CORRECT]
- [x] **B.** Create a lookup relationship between the Rating and Employee object.  [CORRECT]
- [ ] **C.** Create a roll-up summary field on the Employee and use AVG to calculate the average rating score.  [WRONG]
- [ ] **D.** Create a master-detail relationship between the Rating and Employee objects.  [WRONG]

**Explanation:**
> Roll-Up summary doesn't have AVG.

---

### Question 22
What is a benefit of developing applications in a multi-tenant environment?
- [ ] **A.** Access to predefined computing resources  [WRONG]
- [x] **B.** Enforced best practices for development  [CORRECT]
- [ ] **C.** Unlimited processing power and memory  [WRONG]
- [ ] **D.** Default out-of-the-box configuration  [WRONG]

---

### Question 23
When viewing a Quote, the sales representative wants to easily see how many discounted items are included in the Quote Line Items. What should a developer do to meet this requirement?
- [ ] **A.** Create a trigger on the Quote object that queries the Quantity field on discounted Quote Line Items.  [WRONG]
- [ ] **B.** Create a Workflow Rule on the Quote Line Item object that updates a field on the parent Quote when the item is discounted.  [WRONG]
- [x] **C.** Create a roll-up summary field on the Quote object that performs a SUM on the quote Line Item Quantity field, filtered for only discounted Quote Line Items.  [CORRECT]
- [ ] **D.** Create a formula field on the Quote object that performs a SUM on the Quote Line Item Quantity field, filtered for only discounted Quote Line Items.  [WRONG]

**Explanation:**
> To meet the requirement of showing how many discounted items are included in the Quote Line Items, the best approach is to use a roll-up summary field. This field can perform a SUM on the Quote Line Item Quantity field, filtered specifically for discounted items.

---

### Question 24
In terms of the MVC paradigm, what are two advantages of implementing the view layer of a Salesforce application using Lightning Web Component-based development over Visualforce? (Choose two.)
- [x] **A.** Self-contained and reusable units of an application  [CORRECT]
- [x] **B.** Rich component ecosystem  [CORRECT]
- [ ] **C.** Server-side run-time debugging  [WRONG]
- [ ] **D.** Automatic code generation  [WRONG]

**Explanation:**
> Self-contained and reusable units of an application: LWCs are designed as modular components that can be reused across different parts of the application, promoting better code organization and maintainability.
> Rich component ecosystem: LWC benefits from a modern, rich ecosystem of components that can be easily integrated and customized, enhancing the development experience and enabling the creation of more dynamic and responsive user interfaces.

---

### Question 25
Cloud Kicks Fitness, an ISV Salesforce partner, is developing a managed package application. One of the application modules allows the user to calculate body fat using the Apex class, BodyFat, and its method, calculateBodyFat(). The product owner wants to ensure this method is accessible by the consumer of the application when developing customizations outside the ISV's package namespace. Which approach should a developer take to ensure calculateBodyFat() is accessible outside the package namespace?
- [ ] **A.** Declare the class and method using the public access modifier.  [WRONG]
- [ ] **B.** Declare the class as global and use the public access modifier on the method.  [WRONG]
- [ ] **C.** Declare the class as public and use the global access modifier on the method.  [WRONG]
- [x] **D.** Declare the class and method using the global access modifier.  [CORRECT]

**Explanation:**
> To ensure that the calculateBodyFat() method is accessible outside the package namespace, the developer should use the global access modifier. This is because the global access modifier allows the class and its methods to be accessible across different namespaces, which is essential for managed packages.

**Resources:**
> Apex Class Considerations for Packages

---

### Question 26
A software company uses the following objects and relationships:
Case: to handle customer support issues
Defect__c: a custom object to represent known issues with the company's software
Case_Defect__c: a junction object between Case and Defect__c to represent that a defect is a cause of a customer issue Case and Defect__c have Private organization-wide defaults.
What should be done to share a specific Case_Defect__c: record with a user?
- [ ] **A.** Share the parent Defect__c record.  [WRONG]
- [x] **B.** Share the parent Case and Defect__c records.  [CORRECT]
- [ ] **C.** Share the Case_Defect__c record.  [WRONG]
- [ ] **D.** Share the parent Case record.  [WRONG]

**Explanation:**
> A junction object Case_Defect__c typically has two master-detail relationships, one to Case and another to Defect__c. This means that the sharing settings for Case_Defect__c are inherited from its parent records.
> To share a specific Case_Defect__c record with a user, you would indeed need to ensure that the user has access to both the Case and Defect__c records. This is because the visibility of the junction object record is controlled by the sharing settings of its parent objects.

**Resources:**
> Object Relationships Overview

---

### Question 27
What is the debug output of the following Apex code?
Decimal theValue;
System.debug(theValue);
- [ ] **A.** 0.0  [WRONG]
- [x] **B.** null  [CORRECT]
- [ ] **C.** Undefined  [WRONG]
- [ ] **D.** 0  [WRONG]

**Explanation:**
> In Apex, when a Decimal variable is declared but not initialized, its default value is 'null'.

---

### Question 28
Candidates are reviewed by four separate reviewers and their comments and scores which range from 1 (lowest) to 5 (highest) are stored on a review record that is a detail record for a candidate. What is the best way to indicate that a combined review score of 15 or better is required to recommend that the candidate come in for an interview?
- [ ] **A.** Use a Validation Rule on a total score field on the candidate record that prevents a recommended field from being true if the total score is less than 15.  [WRONG]
- [x] **B.** Use a Rollup Summary field to calculate the sum of the review scores, and store this in a total score field on the candidate.  [CORRECT]
- [ ] **C.** Use Visual Workflow to set a recommended field on the candidate whenever the cumulative review score is 15 or better.  [WRONG]
- [ ] **D.** Use a Workflow Rule to calculate the sum of the review scores and send an email to the hiring manager when the total is 15 or better.  [WRONG]

**Explanation:**
> Rollup Summary Field: This field type allows you to perform calculations on related records, such as summing up the review scores. By creating a rollup summary field on the candidate record, you can automatically calculate the total score from the related review records.

---

### Question 29
A developer needs an Apex method that can process Account or Contact records. Which method signature should the developer use?
- [ ] **A.** public void doWork(Account | | Contact)  [WRONG]
- [ ] **B.** public void doWork(Record theRecord)  [WRONG]
- [ ] **C.** public void doWork(Account Contact)  [WRONG]
- [x] **D.** public void doWork(sObject theRecord)  [CORRECT]

**Explanation:**
> In Apex, sObject is the generic base class for all objects in Salesforce. This allows the method to accept any standard or custom object, including Account and Contact.

**Resources:**
> SObject Class

---

### Question 30
Which Salesforce org has a complete duplicate copy of the production org including data and configuration?
- [ ] **A.** Developer Pro Sandbox  [WRONG]
- [ ] **B.** Partial Copy Sandbox  [WRONG]
- [ ] **C.** Production  [WRONG]
- [x] **D.** Full Sandbox  [CORRECT]

**Explanation:**
> Sandbox Types
> Developer Sandbox – A Developer sandbox is intended for development and testing in an isolated environment. A Developer Sandbox includes a copy of your production org’s configuration (metadata).
> Developer Pro Sandbox – A Developer Pro sandbox is intended for development and testing in an isolated environment and can host larger data sets than a Developer sandbox. A Developer Pro sandbox includes a copy of your production org’s configuration (metadata). Use a Developer Pro sandbox to handle more development and quality assurance tasks and for integration testing or user training.
> Partial Copy Sandbox – A Partial Copy sandbox is intended to be used as a testing environment. This environment includes a copy of your production org’s configuration (metadata) and a sample of your production org’s data as defined by a sandbox template. Use a Partial Copy sandbox for quality assurance tasks such as user acceptance testing, integration testing, and training.
> Full Sandbox – A Full sandbox is intended to be used as a testing environment. Only Full sandboxes support performance testing, load testing, and staging. Full sandboxes are a replica of your production org, including all data, such as object records and attachments, and metadata. The length of the refresh interval makes it difficult to use Full sandboxes for development.
> We recommend that you apply a sandbox template so that your sandbox contains only the records that you need for testing or other tasks.

**Resources:**
> Sandbox Types and Templates

---

### Question 31
Universal Containers stores Orders and Line Items in Salesforce. For security reasons, financial representatives are allowed to see information on the Order such as order amount, but they are not allowed to see the Line Items on the Order. Which type of relationship should be used?
- [ ] **A.** Direct Lookup  [WRONG]
- [ ] **B.** Indirect Lookup  [WRONG]
- [ ] **C.** Master-Detail  [WRONG]
- [x] **D.** Lookup  [CORRECT]

**Explanation:**
> Using a Lookup relationship allows you to control access to the related records independently. This means financial representatives can see the Order information without having access to the Line Items.

**Resources:**
> Object Relationships Overview

---

### Question 32
Which two events need to happen when deploying to a production org? (Choose two.)
- [ ] **A.** All Process Builder Processes must have at least 1% test coverage.  [WRONG]
- [x] **B.** All Apex code must have at least 75% test coverage.  [CORRECT]
- [x] **C.** All triggers must have at least 1% test coverage.  [CORRECT]
- [ ] **D.** All Visual Flows must have at least 1% test coverage.  [WRONG]

**Explanation:**
> You must have at least 75% of your Apex covered by unit tests to deploy your code to production environments.
> Ensure all tests pass and at least 1% of coverage is applied to all triggers

**Resources:**
> Code coverage steps before deployment
> Instructions to test Apex code

---

### Question 33
An Approval Process is defined in the Expense_Item__c object. A business rule dictates that whenever a user changes the Status to 'Submitted' on an Expense_Report__c record, all the Expense_Item__c records related to the expense report must enter the approval process individually. Which approach should be used to ensure the business requirement is met?
- [ ] **A.** Create a Process Builder on Expense_Report__c with an 'Apex' action type to submit all related Expense_Item__c records when the criteria is met.  [WRONG]
- [ ] **B.** Create a Process Builder on Expense_Report__c to mark the related Expense_Item__c as submittable and a trigger on Expense_Item__c to submit the records for approval.  [WRONG]
- [x] **C.** Create two Process Builders, one on Expense_Report__c to mark the related Expense_Item__c as submittable and the second on Expense_Item__c to submit the records for approval.  [CORRECT]
- [ ] **D.** Create a Process Builder on Expense_Report__c with a 'Submit for Approval' action type to submit all related Expense_Item__c records when the criteria are met.  [WRONG]

---

### Question 34
A developer is asked to set a picklist field to 'Monitor' on any new Leads owned by a subnet of Users. How should the developer implement this request?
- [ ] **A.** Create an after insert Lead trigger.  [WRONG]
- [ ] **B.** Create a before insert Lead trigger.  [WRONG]
- [x] **C.** Create a record-triggered Flow.  [CORRECT]
- [ ] **D.** Create a Lead formula field.  [WRONG]

**Explanation:**
> Creating a record-triggered Flow is indeed a powerful and flexible way to handle this requirement. With a Flow, you can easily set the picklist field to ‘Monitor’ for new Leads owned by a specific subset of Users without writing any code.

---

### Question 35
Which three process automations can immediately send an email notification to the owner of an Opportunity when its Amount is changed to be greater than $10,000? (Choose three.)
- [x] **A.** Process Builder  [CORRECT]
- [ ] **B.** Escalation Rule  [WRONG]
- [x] **C.** Flow Builder  [CORRECT]
- [ ] **D.** Approval Process  [WRONG]
- [x] **E.** Workflow Rule  [CORRECT]

**Explanation:**
> The three process automations that can immediately send an email notification to the owner of an Opportunity when its Amount is changed to be greater than $10,000 are:
> Process Builder
> Flow Builder
> Workflow Rule
> Escalation Rules are primarily used for cases, not opportunities. They are designed to escalate cases to a higher level of support if they are not resolved within a certain time frame. They do not support sending email notifications based on changes to Opportunity fields.
> Approval Processes are used to automate the approval of records. While they can send email notifications, they are triggered by the submission of records for approval, not by changes to field values like the Opportunity Amount. Therefore, they are not suitable for this specific requirement.

---

### Question 36
A developer needs to confirm that a Contact trigger works correctly without changing the organization's data. What should the developer do to test the Contact trigger?
- [ ] **A.** Use Deploy from the VSCode IDE to deploy an 'Insert Contact' Apex class.  [WRONG]
- [ ] **B.** Use the New button on the Salesforce Contacts Tab to create a new Contact record.  [WRONG]
- [ ] **C.** Use the Open Execute Anonymous feature on the Developer Console to run an 'Insert Contact' DML statement.  [WRONG]
- [x] **D.** Use the Test menu on the Developer Console to run all test classes for the Contact trigger.  [CORRECT]

**Explanation:**
> Running test classes is the best practice for testing triggers in Salesforce. Test classes allow you to verify that your code works as expected without affecting the actual data in your organization. By using the Test menu in the Developer Console, you can run all test classes that include tests for the Contact trigger. This ensures that the trigger logic is executed and validated in a controlled environment.
> Deploying an ‘Insert Contact’ Apex class from VSCode IDE does not test the trigger directly. It only deploys the class to the organization.
> Creating a new Contact record directly in the Salesforce UI will change the organization’s data.
> Running an ‘Insert Contact’ DML statement using Execute Anonymous will also change the organization’s data.

---

### Question 37
Which control statement should a developer use to ensure that a loop body executes at least once?
- [ ] **A.** for (init_stmt; exit_condition; increment_stmt) {...}  [WRONG]
- [x] **B.** do {...} while (condition)  [CORRECT]
- [ ] **C.** while (condition) {...}  [WRONG]
- [ ] **D.** for (variable : list_or_set) {...}  [WRONG]

**Explanation:**
> do {…} while (condition): This control statement ensures that the loop body executes at least once because the condition is checked after the loop body has executed.

---

### Question 38
Which two declarative process automation features can be directly invoked when a field value changes on a record? (Choose two.)
- [ ] **A.** Cloud Flow Designer  [WRONG]
- [x] **B.** Process Builder processes  [CORRECT]
- [ ] **C.** Validation rules  [WRONG]
- [x] **D.** Workflow rules  [CORRECT]

**Explanation:**
> Salesforce retired Cloud Flow Designer in Winter '20. Users were encouraged to transition to the newer Flow Builder, which offers a more modern and user-friendly interface for creating flows. Since now Salesforce is retiring the Workflow rules.

---

### Question 39
Which two strategies should a developer use to avoid hitting governor limits when developing in a multi-tenant environment? (Choose two.)
- [ ] **A.** Use collections to store all fields from a related object and not just minimally required fields.  [WRONG]
- [x] **B.** Use methods from the "Limits" class to monitor governor limits.  [CORRECT]
- [x] **C.** Use SOQL for loops to iterate data retrieved from queries that return a high number of rows.  [CORRECT]
- [ ] **D.** Use variables within Apex classes to store large amounts of data.  [WRONG]

---

### Question 40
Which feature should a developer use to update an inventory count on related Product records when the status of an Order is modified to indicate it is fulfilled?
- [x] **A.** Process Builder process  [CORRECT]
- [ ] **B.** Lightning component  [WRONG]
- [ ] **C.** Visualforce page  [WRONG]
- [ ] **D.** Workflow rule  [WRONG]

---

### Question 41
The operation manager at a construction company uses a custom object called Machinery to manage the usage and maintenance of its cranes and other machinery. The manager wants to be able to assign machinery to different constructions jobs, and track the dates and costs associated with each job. More than one piece of machinery can be assigned to one construction job. What should a developer do to meet these requirements?
- [ ] **A.** Create a lookup field on the Construction Job object to the Machinery object.  [WRONG]
- [ ] **B.** Create a lookup field on the Machinery object to the Construction Job object.  [WRONG]
- [x] **C.** Create a junction object with Master-Detail Relationship to both the Machinery object and the Construction Job object.  [CORRECT]
- [ ] **D.** Create a Master-Detail Lookup on the Machinery object to the Construction Job object.  [WRONG]

---

### Question 42
A developer needs to have records with specific field values in order to test a new Apex class. What should the developer do to ensure the data is available to the test?
- [ ] **A.** Use SOQL to query the org for the required data.  [WRONG]
- [ ] **B.** Use Anonymous Apex to create the required data.  [WRONG]
- [ ] **C.** Use Test.loadData() and reference a CSV file.  [WRONG]
- [x] **D.** Use Test.loadData() and reference a static resource.  [CORRECT]

**Explanation:**
> Using the Test.loadData method, you can populate data in your test methods without having to write many lines of code.
> Follow these steps:
> 1. Add the data in a .csv file.
> 2. Create a static resource for this file.
> 3. Call Test.loadData within your test method and passing it the sObject type token and the static resource name.

**Resources:**
> Loading Test Data

---

### Question 43
A developer created a Lightning component to display a short text summary for an object and wants to use it with multiple Apex classes. How should the developer design the Apex classes?
- [ ] **A.** Have each class define method getObject() that returns the sObject that is controlled by the Apex class.  [WRONG]
- [ ] **B.** Extend each class from the same base class that has a method getTextSummary() that returns the summary.  [WRONG]
- [x] **C.** Have each class implement an interface that defines method getTextSummary() that returns the summary.  [CORRECT]
- [ ] **D.** Have each class define method getTextSummary() that returns the summary.  [WRONG]

---

### Question 44
A developer wrote Apex code that calls out to an external system. How should a developer write the test to provide test coverage?
- [x] **A.** Write a class that implements the HTTPCalloutMock interface.  [CORRECT]
- [ ] **B.** Write a class that extends HTTPCalloutMock.  [WRONG]
- [ ] **C.** Write a class that extends WebserviceMock.  [WRONG]
- [ ] **D.** Write a class that implements the WebserviceMock interface.  [WRONG]

**Explanation:**
> To provide test coverage for Apex code that calls out to an external system, the developer should use the HTTPCalloutMock interface. This allows the developer to mock the HTTP response and test the callout logic without actually making a real HTTP request.

**Resources:**
> Testing HTTP Callouts by Implementing the HttpCalloutMock Interface

---

### Question 45
What is the maximum number of SOQL queries used by the following code?
List<Account> aList = [SELECT Id FROM Account LIMIT 5];
for(Account a : aList){
List<Contact> cList = [SELECT Id FROM Contact Where AccountId = : a.Id];
}
- [ ] **A.** 1  [WRONG]
- [ ] **B.** 5  [WRONG]
- [x] **C.** 6  [CORRECT]
- [ ] **D.** 2  [WRONG]

**Explanation:**
> Initial Query: 1
> Queries Inside Loop: Up to 5 (one for each Account)

---

### Question 46
Which process automation can be used to calculate the shipping cost for an Order when the Order is placed and apply a percentage of the shipping cost to some of the related Order Products?
- [ ] **A.** Lightning Component  [WRONG]
- [x] **B.** Flow Builder  [CORRECT]
- [ ] **C.** Entitlement Rules  [WRONG]
- [ ] **D.** Approval Process  [WRONG]

---

### Question 47
A developer created a child Lightning web component nested inside a parent Lightning web component. The parent component needs to pass a string value to the child component. In which two ways can this be accomplished? (Choose two.)
- [x] **A.** The parent component can use a custom event to pass the data to the child component.  [CORRECT]
- [ ] **B.** The parent component can invoke a method in the child component.  [WRONG]
- [x] **C.** The parent component can use a public property to pass the data to the child component.  [CORRECT]
- [ ] **D.** The parent component can use the Apex controller class to send data to the child component.  [WRONG]

---

### Question 48
What are two best practices when it comes to Lightning Web Component events? (Choose two.)
- [ ] **A.** Use event.detail to communicate data to elements in the same shadow tree.  [WRONG]
- [x] **B.** Use CustomEvent to pass data from a child to a parent component.  [CORRECT]
- [x] **C.** Use event.target to communicate data to elements that aren't in the same shadow tree.  [CORRECT]
- [ ] **D.** Use events configured with bubbles: false and composed: false.  [WRONG]

**Resources:**
> Events Best Practices

---

### Question 49
A developer migrated functionality from JavaScript Remoting to a Lightning web component and wants to use the existing getOpportunities() method to provide data. Which modification to the method is necessary?
- [ ] **A.** The method must return a String of a serialized JSON Array.  [WRONG]
- [ ] **B.** The method must be decorated with (cacheable=true).  [WRONG]
- [x] **C.** The method must be decorated with @AuraEnabled.  [CORRECT]
- [ ] **D.** The method must return a JSON Object.  [WRONG]

---

### Question 50
A developer must provide a custom user interface when users edit a Contact. Users must be able to use the interface in Salesforce Classic and Lightning Experience. What should the developer do to provide the custom user interface?
- [x] **A.** Override the Contact's Edit button with a Visualforce page in Salesforce Classic and a Lightning component in Lightning Experience.  [CORRECT]
- [ ] **B.** Override the Contact's Edit button with a Visualforce page in Salesforce Classic and a Lightning page in Lightning Experience.  [WRONG]
- [ ] **C.** Override the Contact's Edit button with a Lightning component in Salesforce Classic and a Lightning component in Lightning Experience.  [WRONG]
- [ ] **D.** Override the Contact's Edit button with a Lightning page in Salesforce Classic and a Visualforce page in Lightning Experience.  [WRONG]

**Resources:**
> Override Standard Actions with Aura Components
> Override Buttons, Links, and Tabs with Visualforce
> Considerations for Overriding Standard Buttons

---

### Question 51
Which Lightning code segment should be written to declare dependencies on a Lightning component, c:accountList, that is used in a Visualforce page?
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
</aura:component>

**Explanation:**
> To describe the components that you want to deploy outside of Salesforce, create a Lightning Out app. A Lightning Out app is a special standalone Aura app defined with the <aura:application> tag. Add components to the app with the <aura:dependency> tag

**Resources:**
> Lightning Out Dependencies

---

### Question 52
A developer can use the debug log to see which three types of information? (Choose three.)
- [x] **A.** HTTP callouts to external systems  [CORRECT]
- [x] **B.** Database changes  [CORRECT]
- [x] **C.** Resource usage and limits  [CORRECT]
- [ ] **D.** User login events  [WRONG]
- [ ] **E.** Actions triggered by time-based workflow  [WRONG]

**Explanation:**
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

**Resources:**
> Debug Log

---

### Question 53
A developer created a trigger on the Account object and wants to test if the trigger is properly bulkified. The developer team decided that the trigger should be tested with 200 account records with unique names. What two things should be done to create the test data within the unit test with the least amount of code? (Choose two.)
- [ ] **A.** Use the @isTest(seeAllData=true) annotation in the test class.  [WRONG]
- [x] **B.** Create a static resource containing test data.  [CORRECT]
- [ ] **C.** Use the @isTest(isParallel=true) annotation in the test class.  [WRONG]
- [x] **D.** Use Test.loadData to populate data in your test methods.  [CORRECT]

**Explanation:**
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

---

### Question 54
What can be developed using the Lightning Component framework?
- [ ] **A.** Salesforce integrations  [WRONG]
- [ ] **B.** Salesforce Classic and Lightning user interface pages  [WRONG]
- [ ] **C.** Hosted web applications  [WRONG]
- [x] **D.** Single-page web apps  [CORRECT]

**Explanation:**
> Lightning Component Framework
> The Lightning Component framework is a UI framework for developing single-page web apps for mobile and desktop devices.

**Resources:**
> Lightning Component Framework

---

### Question 55
A developer must create an Apex class, ContactController, that a Lightning component can use to search for Contact records. Users of the Lightning component should only be able to search for Contact records to which they have access. Which two will restrict the records correctly? (Choose two.)
- [ ] **A.** public class ContactController  [WRONG]
- [x] **B.** public with sharing class ContactController  [CORRECT]
- [ ] **C.** public without sharing class ContactController  [WRONG]
- [x] **D.** public inherited sharing class ContactController  [CORRECT]

**Explanation:**
> With Sharing
> Use the with sharing keyword when declaring a class to enforce sharing rules of the current user. Explicitly setting this keyword ensures that Apex code runs in the current user context. Apex code that is executed with the executeAnonymous call and Connect in Apex always execute using the sharing rules of the current user.
> Without Sharing
> Use the without sharing keyword when declaring a class to ensure that the sharing rules for the current user are not enforced. For example, you can explicitly turn off sharing rule enforcement when a class is called from another class that is declared using with sharing.
> Inherited Sharing
> Use the inherited sharing keyword when declaring a class to enforce the sharing rules of the class that calls it. Using inherited sharing is an advanced technique to determine the sharing mode at runtime and design Apex classes that can run in either with sharing or without sharing mode.

**Resources:**
> Using the with sharing, without sharing, and inherited sharing Keywords

---

### Question 56
A developer must create a DrawList class that provides capabilities defined in the Sortable and Drawable interfaces.
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
}

**Explanation:**
> Option A: Incorrect because you cannot use implements twice.
> Option C, D: Incorrect because you cannot use extends with interfaces; extends is used for classes.

---

### Question 57
Which three options allow a developer to use custom styling in a Visualforce page? (Choose three.)
- [x] **A.** <apex:stylesheet> tag  [CORRECT]
- [x] **B.** Inline CSS  [CORRECT]
- [ ] **C.** <apex:style>tag  [WRONG]
- [ ] **D.** <apex:stylesheets>tag  [WRONG]
- [x] **E.** A static resource  [CORRECT]

**Explanation:**
> <apex:stylesheet> tag: This tag is used to include external CSS stylesheets in your Visualforce page1.
> Inline CSS: You can directly include CSS styles within the <style> tags in your Visualforce page1.
> A static resource: You can upload CSS files as static resources and reference them in your Visualforce page using the <apex:stylesheet> tag.

**Resources:**
> Styling Visualforce Pages

---

### Question 58
When a user edits the Postal Code on an Account, a custom Account text field named 'Timezone' must be updated based on the values in a PostalCodeToTimezone__c custom object. How should a developer implement this feature?
- [ ] **A.** Build an Account Workflow Rule.  [WRONG]
- [ ] **B.** Build an Account Assignment Rule.  [WRONG]
- [x] **C.** Build an Account custom Trigger.  [CORRECT]
- [ ] **D.** Build an Account Approval Process.  [WRONG]

**Explanation:**
> A trigger can handle the logic required to update the ‘Timezone’ field based on the Postal Code changes and the corresponding values in the PostalCodeToTimezone__c custom object.
> Build an Account Workflow Rule: Workflow rules are great for simple field updates, but they don’t support complex logic like querying another object (PostalCodeToTimezone__c) to determine the value of the ‘Timezone’ field.
> Build an Account Assignment Rule: Assignment rules are used to assign records to users or queues based on criteria. They don’t support updating fields based on related object data.
> Build an Account Approval Process: Approval processes are designed for managing record approvals and don’t support the kind of field update logic you’re looking for.

---

### Question 1
Where can a developer identify the time taken by each process in a transaction using Developer Console log inspector?
- [ ] **A.** Performance Tree tab under Stack Tree panel  [WRONG]
- [ ] **B.** Execution Tree tab under Stack Tree panel  [WRONG]
- [x] **C.** Timeline tab under Execution Overview panel  [CORRECT]
- [ ] **D.** Save Order tab under Execution Overview panel  [WRONG]

**Explanation:**
> The Timeline tab provides a visual representation of the time taken by each process. Select the Scale option that results in the most useful view.

**Resources:**
> Log Inspector

---

### Question 2
A developer has the controller class below.
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
System.assert(m.prop == 1);

**Explanation:**
> The value of prop variable is never defined in the constructor, so its default value is null.

**Resources:**
> Anonymous Blocks

---

### Question 3
Which three statements are true regarding trace flags? (Choose three.)
- [ ] **A.** Setting trace flags automatically cause debug logs to be generated.  [WRONG]
- [ ] **B.** Logging levels override trace flags.  [WRONG]
- [x] **C.** Trace flags override logging levels.  [CORRECT]
- [x] **D.** If active trace flags are not set, Apex tests execute with default logging levels.  [CORRECT]
- [x] **E.** Trace flags can be set in the Developer Console, Setup, or using the Tooling API.  [CORRECT]

**Resources:**
> Set Up Debug Logging

---

### Question 4
How can a developer check the test coverage of Autolaunched Flows before deploying them in a change set?
- [ ] **A.** Use the Flow Properties page.  [WRONG]
- [ ] **B.** Use the ApexTestResult class.  [WRONG]
- [x] **C.** Use SOQL and the Tooling API.  [CORRECT]
- [ ] **D.** Use the Code Coverage Setup page.  [WRONG]

**Explanation:**
> Developers can use SOQL queries along with the Tooling API to check the test coverage of autolaunched Flows. The FlowTestCoverage object in the Tooling API provides information about the test coverage for flows.

**Resources:**
> FlowTestCoverage

---

### Question 5
A developer has the following requirements: Calculate the total amount on an Order. Calculate the line amount for each Line Item based on quantity selected and price. Move Line Items to a different Order if a Line Item is not in stock. Which relationship implementation supports these requirements on its own?
- [ ] **A.** Order has a re-parentable master-detail field to Line Item.  [WRONG]
- [ ] **B.** Order has a re-parentable lookup field to Line Item.  [WRONG]
- [ ] **C.** Line Item has a re-parentable lookup field to Order.  [WRONG]
- [x] **D.** Line Item has a re-parentable master-detail field to Order.  [CORRECT]

**Explanation:**
> By default, records can’t be reparented in master-detail relationships. Administrators can, however, allow child records in master-detail relationships on custom objects to be reparented to different parent records by selecting the Allow reparenting option in the master-detail relationship definition.

---

### Question 6
AW Computing tracks order information in custom objects called Order__c and Order_Line__c. Currently, all shipping information is stored in the Order__c object. The company wants to expand its order application to support split shipments so that any number of Order_Line__c records on a single Order__c can be shipped to different locations. What should a developer add to fulfill this requirement?
- [ ] **A.** Order_Shipment_Group__c object and master-detail field on Order__c  [WRONG]
- [x] **B.** Order_Shipment_Group__c object and master-detail fields to Order__c and Order_Line__c  [CORRECT]
- [ ] **C.** Order_Shipment_Group__c object and master-detail field on Order_Line__c  [WRONG]
- [ ] **D.** Order_Shipment_Group__c object and master-detail field on Order_Shipment_Group__c  [WRONG]

---

### Question 7
Which two Apex data types can be used to reference a Salesforce record ID dynamically? (Choose two.)
- [ ] **A.** ENUM  [WRONG]
- [x] **B.** sObject  [CORRECT]
- [ ] **C.** External ID  [WRONG]
- [x] **D.** String  [CORRECT]

---

### Question 8
A developer is debugging the following code to determine why Accounts are not being created. List<Account> accts = getAccounts(); //getAccounts implemented else where Database.insert(accts, false); How should the code be altered to help debug the issue?
- [ ] **A.** Change the DML statement to insert method.  [WRONG]
- [x] **B.** Collect the insert method return value in a SaveResult record.  [CORRECT]
- [ ] **C.** Set the second insert method parameter to TRUE.  [WRONG]
- [ ] **D.** Add a try/catch around the insert method.  [WRONG]

**Explanation:**
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

---

### Question 9
Why would a developer consider using a custom controller over a controller extension?
- [ ] **A.** To increase the SOQL query governor limits.  [WRONG]
- [ ] **B.** To implement all of the logic for a page and bypass default Salesforce functionality  [WRONG]
- [x] **C.** To leverage built-in functionality of a standard controller  [CORRECT]
- [ ] **D.** To enforce user sharing settings and permissions  [WRONG]

**Resources:**
> What are Custom Controllers and Controller Extensions?

---

### Question 10
Which approach should be used to provide test data for a test class?
- [ ] **A.** Query for existing records in the database.  [WRONG]
- [ ] **B.** Execute anonymous code blocks that create data.  [WRONG]
- [x] **C.** Use a test data factory class to create test data.  [CORRECT]
- [ ] **D.** Access data in @TestVisible class variables.  [WRONG]

**Explanation:**
> Using a Test Data Factory or @TestSetup method is generally considered best practice as it ensures tests are isolated, repeatable, and maintainable.

---

### Question 11
A developer created these three roll-up summary fields on the custom object Project__c: - Total_Timesheets__c - Total_Approved_Timesheets__c - Total_Rejected_Timesheet__c The developer is asked to create a new field that shows the ratio between rejected and approved timesheets for a given project. The developer is asked to create a new field that shows the ratio between rejected and approved timesheets for a given project.
What are two benefits of choosing a formula field instead of an Apex trigger to fulfill the request? (Choose two.)
- [ ] **A.** A test class will validate the formula field during deployment.  [WRONG]
- [ ] **B.** A formula field will trigger existing automation when deployed.  [WRONG]
- [x] **C.** Using a formula field reduces maintenance overhead.  [CORRECT]
- [x] **D.** A formula field will calculate the value retroactively for existing records.  [CORRECT]

---

### Question 12
A developer needs to update an unrelated object when a record gets saved. Which two trigger types should the developer create? (Choose two.)
- [x] **A.** after insert  [CORRECT]
- [ ] **B.** before update  [WRONG]
- [ ] **C.** before insert  [WRONG]
- [x] **D.** after update  [CORRECT]

**Explanation:**
> To update an unrelated object when a record gets saved, the developer should create the following two trigger types:
> After Insert Trigger: This trigger runs after a new record is inserted into the database. It allows the developer to perform actions on unrelated objects based on the newly inserted record.
> After Update Trigger: This trigger runs after an existing record is updated. It enables the developer to update unrelated objects based on changes to the original record.

---

### Question 13
Which feature allows a developer to create test records for use in test classes?
- [ ] **A.** Documents  [WRONG]
- [ ] **B.** WebServiceTests  [WRONG]
- [ ] **C.** HttpCalloutMocks  [WRONG]
- [x] **D.** Static Resources  [CORRECT]

---

### Question 14
An org tracks customer orders on an Order object and the line items of an Order on the Line Item object. The Line Item object has a Master/Detail relationship to the Order object. A developer has a requirement to calculate the order amount on an Order and the line amount on each Line Item based on quantity and price. What is the correct implementation?
- [ ] **A.** Write a single before trigger on the Line Item that calculates the item amount and updates the order amount on the Order.  [WRONG]
- [ ] **B.** Write a process on the Line Item that calculates the item amount and order amount and updates the fields on the Line Item and the Order.  [WRONG]
- [ ] **C.** Implement the line amount as a numeric formula field and the order amount as a roll-up summary field.  [WRONG]
- [x] **D.** Implement the line amount as a currency field and the order amount as a SUM formula field.  [CORRECT]

---

### Question 15
A Lightning component has a wired property, searchResults, that stores a list of Opportunities. Which definition of the Apex method, to which the searchResults property is wired, should be used?
- [ ] **A.** @AuraEnabled(cacheable = false) public static List<Opportunity> search(String term) { /*implementation*/ }  [WRONG]
- [ ] **B.** @AuraEnabled(cacheable = false) public List<Opportunity> search(String term) { /*implementation*/ }  [WRONG]
- [x] **C.** @AuraEnabled(cacheable = true) public static List<Opportunity> search(String term) { /*implementation*/ }  [CORRECT]
- [ ] **D.** @AuraEnabled(cacheable = true) public List<Opportunity> search(String term) { /*implementation*/ }  [WRONG]

**Explanation:**
> To improve runtime performance, annotate the Apex method with @AuraEnabled(cacheable=true), which caches the method results on the client. To set cacheable=true, a method must only get data, it can’t mutate (change) data.
> To use @wire to call an Apex method, you must set cacheable=true.

**Resources:**
> Client-Side Caching of Apex Method Results

---

### Question 16
A lead developer creates an Apex interface called Laptop. Consider the following code snippet: public class SilverLaptop{//code implementation} How can a developer use the Laptop interface within the SilverLaptop class?
- [x] **A.** public class SilverLaptop implements Laptop{}  [CORRECT]
- [ ] **B.** @Extends(class=Laptop) public class SilverLaptop{}  [WRONG]
- [ ] **C.** public class SilverLaptop extends Laptop{}  [WRONG]
- [ ] **D.** @Interface(class=Laptop) public class SilverLaptop{}  [WRONG]

**Explanation:**
> In Apex (similar to Java), the implements keyword is used to indicate that a class will implement an interface.
> public class SilverLaptop implements Laptop {
> // code implementation
> }

---

### Question 17
A method is passed a list of generic sObjects as a parameter. What should the developer do to determine which object type (Account, Lead, or Contact, for example) to cast each sObject?
- [ ] **A.** Use the first three characters of the sObject ID to determine the sObject type.  [WRONG]
- [x] **B.** Use the getSObjectType method on each generic sObject to retrieve the sObject token.  [CORRECT]
- [ ] **C.** Use the getSObjectName method on the sObject class to get the sObject name.  [WRONG]
- [ ] **D.** Use a try-catch construct to cast the sObject into one of the three sObject types.  [WRONG]

**Explanation:**
> To determine the specific object type (e.g., Account, Lead, Contact) of each sObject in a list, the developer can use the getSObjectType method. This method returns the Schema.SObjectType of the sObject, which can then be used to identify the object type.

**Resources:**
> SObjectType Class

---

### Question 18
What are two use cases for executing Anonymous Apex code? (Choose two.)
- [x] **A.** To run a batch Apex class to update all Contacts  [CORRECT]
- [ ] **B.** To schedule an Apex class to run periodically  [WRONG]
- [x] **C.** To delete 15,000 inactive Accounts in a single transaction after a deployment  [CORRECT]
- [ ] **D.** To add unit test code coverage to an org  [WRONG]

**Explanation:**
> To run a batch Apex class to update all Contacts
> To delete 15,000 inactive Accounts in a single transaction after a deployment
> These use cases are suitable for Anonymous Apex because it allows developers to quickly execute code snippets for tasks such as data manipulation or batch processing without needing to deploy the code to the org.

**Resources:**
> Executing Anonymous Apex Code

---

### Question 19
A Developer wants to get access to the standard price book in the org while writing a test class that covers an OpportunityLineItem trigger. Which method allows access to the price book?
- [x] **A.** Use Test.getStandardPricebookId() to get the standard price book ID.  [CORRECT]
- [ ] **B.** Use @IsTest(SeeAllData=true) and delete the existing standard price book.  [WRONG]
- [ ] **C.** Use Test.loadData() and a Static Resource to load a standard price book.  [WRONG]
- [ ] **D.** Use @TestVisible to allow the test method to see the standard price book.  [WRONG]

**Explanation:**
> To access the standard price book in a test class that covers an OpportunityLineItem trigger, the developer should use the Test.getStandardPricebookId() method. This method retrieves the ID of the standard price book, allowing the test class to reference it.

**Resources:**
> Test Class

---

### Question 20
A development team wants to use a deployment script to automatically deploy to a sandbox during their development cycles. Which two tools can they use to run a script that deploys to a sandbox? (Choose two.)
- [x] **A.** SFDX CLI  [CORRECT]
- [ ] **B.** Developer Console  [WRONG]
- [ ] **C.** Change Sets  [WRONG]
- [x] **D.** Ant Migration Tool  [CORRECT]

**Resources:**
> Choose Your Tools for Developing and Deploying Changes

---

### Question 21
A platform developer at Universal Containers needs to create a custom button for the Account object that, when clicked, will perform a series of calculations and redirect the user to a custom Visualforce page. Which three attributes need to be defined with values in the tag to accomplish this? (Choose three.)
- [x] **A.** action  [CORRECT]
- [ ] **B.** renderAs  [WRONG]
- [x] **C.** standardController  [CORRECT]
- [ ] **D.** readOnly  [WRONG]
- [x] **E.** extensions  [CORRECT]

**Explanation:**
> To create a custom button for the Account object that performs calculations and redirects to a custom Visualforce page, the developer needs to define the following three attributes in the <apex:page> tag:
> StandardController: This attribute specifies the standard controller for the Visualforce page, which in this case would be the Account object.
> Action: This attribute defines the action method that performs the calculations before redirecting to the Visualforce page.
> Extensions: This attribute specifies any additional Apex classes that extend the standard controller to include custom logic for the calculations.

**Resources:**
> What is Visualforce?

---

### Question 22
A recursive transaction is initiated by a DML statement creating records for these two objects:     1. Accounts 2. Contacts The Account trigger hits a stack depth of 16. Which statement is true regarding the outcome of the transaction?
- [ ] **A.** The transaction fails and all the changes are rolled back.  [WRONG]
- [ ] **B.** The transaction succeeds as long as the Contact trigger stack depth is less than 16.  [WRONG]
- [x] **C.** The transaction fails only if the Contact trigger stack depth is greater or equal to 16.  [CORRECT]
- [ ] **D.** The transaction succeeds and all changes are committed to the database.  [WRONG]

**Explanation:**
> When an Account trigger hits a stack depth of 16, it means that the trigger has recursively called itself 16 times. In Salesforce, the maximum allowed stack depth for recursive triggers is 16. Therefore, the transaction will fail with a “maximum trigger depth exceeded” error.
> To avoid these kind of situation we can use public class static variable. We can solve this issue, you can set a condition on trigger so it will not be called recursively.

---

### Question 23
Which exception type cannot be caught?
- [x] **A.** LimitException  [CORRECT]
- [ ] **B.** NoAccessException  [WRONG]
- [ ] **C.** A Custom Exception  [WRONG]
- [ ] **D.** CalloutException  [WRONG]

**Explanation:**
> LimitException is a type of exception in Salesforce that cannot be caught. Since these limits are enforced to ensure the stability and performance of the Salesforce platform, LimitException cannot be handled using try-catch blocks.

---

### Question 24
A developer wants to import 500 Opportunity records into a sandbox. Why should the developer choose to use Data Loader instead of Data Import Wizard?
- [ ] **A.** Data Loader runs from the developer's browser.  [WRONG]
- [ ] **B.** Data Loader automatically relates Opportunities to Accounts.  [WRONG]
- [x] **C.** Data Import Wizard does not support Opportunities.  [CORRECT]
- [ ] **D.** Data Import Wizard can not import all 500 records.  [WRONG]

**Explanation:**
> The Data Import Wizard does not support the import of Opportunity records. It is limited to certain standard objects like Contacts, Leads, and Accounts.

**Resources:**
> Import Data with the Data Import Wizard

---

### Question 25
When importing and exporting data into Salesforce, which two statements are true? (Choose two.)
- [ ] **A.** Bulk API can be used to Import large data volumes in development environments without bypassing the storage limits.  [WRONG]
- [x] **B.** Developer and Developer Pro sandboxes have different storage limits.  [CORRECT]
- [ ] **C.** Bulk API can be used to bypass the storage limits when importing large data volumes in development environments.  [WRONG]
- [x] **D.** Data import wizard is a client application provided by Salesforce.  [CORRECT]

**Explanation:**
> Developer sandboxes have a storage limit of 200 MB for data and 200 MB for files, while Developer Pro sandboxes have a storage limit of 1 GB for data and 1 GB for files.
> The Data Import Wizard is a tool provided by Salesforce that allows users to import data into Salesforce objects through a simple interface.

---

### Question 26
Which code should be used to update an existing Visualforce page that uses standard Visualforce components so that the page matches the look and feel of Lightning Experience?
- [ ] **A.** <apex:styleSheet value="({$URLFOR($Resource.slds,’assets/slds.css’)}">  [WRONG]
- [ ] **B.** <apex:slds/>  [WRONG]
- [x] **C.** <apex:page lightningStyleSheets="true">  [CORRECT]
- [ ] **D.** <apex:includeLightning/>  [WRONG]

**Explanation:**
> To style your Visualforce page to match the Lightning Experience UI when viewed in Lightning Experience or the Salesforce mobile app, set lightningStylesheets="true" in the <apex:page> tag. When the page is viewed in Salesforce Classic, it doesn’t get Lightning Experience styling.
> <apex:page lightningStylesheets="true">

**Resources:**
> Style Existing Visualforce Pages with Lightning Experience Stylesheets

---

### Question 27
Which three code lines are required to create a Lightning component on a Visualforce page? (Choose three.)
- [ ] **A.** $Lightning.useComponent  [WRONG]
- [ ] **B.** <apex:slds/>  [WRONG]
- [x] **C.** $Lightning.use  [CORRECT]
- [x] **D.** <apex:includeLightning/>  [CORRECT]
- [x] **E.** $Lightning.createComponent  [CORRECT]

**Resources:**
> Use Components in Visualforce Pages

---

### Question 28
A developer is integrating with a legacy on-premise SQL database. What should the developer use to ensure the data being integrated is matched to the right records in Salesforce?
- [ ] **A.** Formula field  [WRONG]
- [ ] **B.** Lookup field  [WRONG]
- [x] **C.** External ID field  [CORRECT]
- [ ] **D.** External Object  [WRONG]

**Explanation:**
> Use External IDs in Salesforce to match records. External IDs are custom fields that have the “External ID” attribute, which can be used to match records from external systems. This is particularly useful for upsert operations where you need to insert or update records based on an external identifier.

**Resources:**
> Insert or Update (Upsert) a Record Using an External ID

---

### Question 29
A developer is asked to create a Visualforce page that displays some Account fields as well as fields configured on the page layout for related Contacts. How should the developer implement this request?
- [ ] **A.** Use the <apex:include> tag.  [WRONG]
- [x] **B.** Use the <apex:relatedList> tag.  [CORRECT]
- [ ] **C.** Add a method to the standard controller.  [WRONG]
- [ ] **D.** Create a controller extension.  [WRONG]

**Explanation:**
> To create a Visualforce page that displays some Account fields as well as fields configured on the page layout for related Contacts, the developer can follow these steps:
> 1. Use the Standard Controller for Account: This allows the Visualforce page to access the Account data.
> 2. Use <apex:detail> for Account Fields: This component displays the standard detail page for the Account, including fields configured on the page layout.
> 3. Use <apex:relatedList> for Related Contacts: This component displays the related list of Contacts as configured on the Account page layout.

**Resources:**
> Display Records, Fields, and Tables

---

### Question 30
While working in a sandbox, an Apex test falls when run in the Test Framework. However, running the Apex test logic in the Execute Anonymous window succeeds with no exceptions or errors. Why did the method fall in the sandbox test framework but succeed in the Developer Console?
- [ ] **A.** The test method is calling an @future method.  [WRONG]
- [ ] **B.** The test method has a syntax error in the code.  [WRONG]
- [ ] **C.** The test method does not use System.runAs to execute as a specific user.  [WRONG]
- [x] **D.** The test method relies on existing data in the sandbox.  [CORRECT]

**Explanation:**
> In Apex tests, it’s important to create all necessary data within the test itself to ensure it doesn’t depend on existing data in the environment. When you run the code via the Execute Anonymous tool, it can access the existing data in the sandbox, which might not be the case when running the test method

**Resources:**
> Resolve Apex Test Failures
> Debugging, Testing, and Deploying Apex

---

### Question 31
A developer has a single custom controller class that works with a Visualforce Wizard to support creating and editing multiple sObjects. The wizard accepts data from user inputs across multiple Visualforce pages and from a parameter on the initial URL. Which three statements are useful inside the unit test to effectively test the custom controller? (Choose three.)
- [ ] **A.** Insert pageRef;  [WRONG]
- [x] **B.** String nextPage = controller.save().getUrl();  [CORRECT]
- [x] **C.** ApexPages.currentPage().getParameters().put('Input', 'TestValue');  [CORRECT]
- [ ] **D.** public ExtendedController(ApexPages.StandardController cntrl){}  [WRONG]
- [x] **E.** Test.setCurrentPage(pageRef);  [CORRECT]

**Explanation:**
> Test.setCurrentPage(pageRef);
> This statement sets the current page context to the specified PageReference, which is essential for simulating the Visualforce page environment in your test.
> ApexPages.CurrentPage().getParameters().put(‘input’, ‘TestValue’);
> This statement allows you to set parameters on the current page, which is useful for testing how your controller handles URL parameters.
> String nextPage = controller.save().getUrl();
> This statement captures the URL of the next page after an action method (like save) is called, which helps verify the navigation logic of your controller.

**Resources:**
> Test a Custom Controller

---

### Question 32
Which three Salesforce resources can be accessed from a Lightning web component? (Choose three.)
- [ ] **A.** All external libraries  [WRONG]
- [x] **B.** Static resources  [CORRECT]
- [ ] **C.** Third-party web components  [WRONG]
- [x] **D.** Content asset files  [CORRECT]
- [x] **E.** SVG resources  [CORRECT]

**Resources:**
> Access Static Resources, Labels, Internationalization Properties, User IDs, and Form Factors

---

### Question 33
Which two events need to happen when deploying to a production org? (Choose two.)
- [ ] **A.** All Workflow rules must have at least 1% test coverage.  [WRONG]
- [x] **B.** All Apex code must have at least 75% test coverage.  [CORRECT]
- [x] **C.** All triggers must have some test coverage.  [CORRECT]
- [ ] **D.** All Visual Flows must have at least 1% test coverage.  [WRONG]

**Explanation:**
> Code Coverage
> You must have at least 75% of your Apex covered by unit tests to deploy your code to production environments.
> All triggers must have at least one line of test coverage.

**Resources:**
> Instructions to test Apex code

---

### Question 34
Universal Containers recently transitioned from Classic to Lightning Experience. One of its business processes requires certain values from the Opportunity object to be sent via an HTTP REST callout to its external order management system based on a user-initiated action on the Opportunity detail page. Example values are as follows: Name Amount Account. Which two methods should the developer implement to fulfill the business requirement? (Choose two.)
- [ ] **A.** Create a Visualforce page that performs the HTTP REST callout, and use a Visualforce quick action to expose the component on the Opportunity detail page.  [WRONG]
- [ ] **B.** Create a Process Builder on the Opportunity object that executes an Apex immediate action to perform the HTTP REST callout whenever the Opportunity is updated.  [WRONG]
- [x] **C.** Create a Lightning component that performs the HTTP REST callout, and use a Lightning Action to expose the component on the Opportunity detail page.  [CORRECT]
- [x] **D.** Create an after update trigger on the Opportunity object that calls a helper method using @Future(Callout=true) to perform the HTTP REST callout.  [CORRECT]

---

### Question 35
Which statement describes the execution order when triggers are associated to the same object and event?
- [ ] **A.** Triggers are executed in the order they are modified.  [WRONG]
- [ ] **B.** Triggers are executed alphabetically by trigger name.  [WRONG]
- [x] **C.** Trigger execution order cannot be guaranteed.  [CORRECT]
- [ ] **D.** Triggers are executed in the order they are created.  [WRONG]

**Explanation:**
> If more than one trigger is defined on an object for the same event, the order of trigger execution isn't guaranteed. For example, if you have two before insert triggers for Case and a new Case record is inserted. The firing order of these two triggers isn’t guaranteed.

**Resources:**
> Triggers and Order of Execution

---

### Question 36
In the Lightning UI, where should a developer look to find information about a Paused Flow Interview?
- [ ] **A.** On the Paused Flow Interviews related list for a given record  [WRONG]
- [ ] **B.** In the system debug log by filtering on Paused Flow Interview  [WRONG]
- [ ] **C.** In the Paused Interviews section of the Apex Flex Queue  [WRONG]
- [x] **D.** On the Paused Flow Interviews component on the Home page  [CORRECT]

**Explanation:**
> Lightning Experience—Add the Paused Flow Interviews component to the appropriate Home pages. This component is available only for Home pages in the Lightning App Builder. It displays paused interviews that the user has read access to.
> Experience Builder Site—Add the Paused Flows component to a site page. This component is available for most pages in Experience Builder, except ones like login pages and error pages. The component displays paused interviews that the user has read access to.
> Salesforce mobile app—Add the Paused Flows item to the navigation items of any Lightning app.
> Salesforce Classic—Add the Paused Flow Interviews related list to the appropriate home page layouts. This component displays only interviews that the user paused.

**Resources:**
> Make It Easy for Users to Find Their Paused Flow Interviews

---

### Question 37
An Opportunity needs to have an amount rolled up from a custom object that is not in a master-detail relationship. How can this be achieved?
- [ ] **A.** Write a Process Builder that links the custom object to the Opportunity.  [WRONG]
- [ ] **B.** Use the Streaming API to create real-time roll-up summaries.  [WRONG]
- [ ] **C.** Write a trigger on the child object and use a red-black tree sorting to sum the amount for all related child objects under the Opportunity.  [WRONG]
- [x] **D.** Write a trigger on the child object and use an aggregate function to sum the amount for all related child objects under the Opportunity.  [CORRECT]

---

### Question 38
How does the Lightning Component framework help developers implement solutions faster?
- [ ] **A.** By providing an Agile process with default steps  [WRONG]
- [ ] **B.** By providing code review standards and processes  [WRONG]
- [x] **C.** By providing device-awareness for mobile and desktops  [CORRECT]
- [ ] **D.** By providing change history and version control  [WRONG]

**Explanation:**
> The framework is designed to create responsive applications that work seamlessly across different devices, including mobile and desktop1. This means developers can build components once and have them function well on various platforms without additional adjustments.

**Resources:**
> Lightning Component Framework

---

### Question 39
Which Salesforce feature allows a developer to see when a user last logged in to Salesforce if real-time notification is not required?
- [x] **A.** Event Monitoring Log  [CORRECT]
- [ ] **B.** Calendar Events  [WRONG]
- [ ] **C.** Developer Log  [WRONG]
- [ ] **D.** Asynchronous Data Capture Events  [WRONG]

**Explanation:**
> Event Monitoring: One of the many tools that Salesforce provides to help keep your data secure, allowing you to see the granular details of user activity in your organization. We refer to these user activities as events. Unlike Real-Time Events, Event Monitoring doesn’t send real-time notifications. Instead, it stores user activity in a log that you can query.

**Resources:**
> Get to Know Real-Time Events and Transaction Security
> LoginEvent

---

### Question 40
Which two are best practices when it comes to component and application event handling? (Choose two.)
- [ ] **A.** Reuse the event logic in a component bundle, by putting the logic in the helper.  [WRONG]
- [x] **B.** Use component events to communicate actions that should be handled at the application level.  [CORRECT]
- [x] **C.** Handle low-level events in the event handler and re-fire them as higher-level events.  [CORRECT]
- [ ] **D.** Try to use application events as opposed to component events.  [WRONG]

**Resources:**
> Events Best Practices

---

### Question 41
From which two locations can a developer determine the overall code coverage for a sandbox? (Choose two.)
- [ ] **A.** The Apex Test Execution page  [WRONG]
- [ ] **B.** The Test Suite Run panel of the Developer Console  [WRONG]
- [x] **C.** The Apex Classes setup page  [CORRECT]
- [x] **D.** The Tests tab of the Developer Console  [CORRECT]

**Explanation:**
> After the completed run, check the overall code coverage for your org by navigating to:
> 1. In the Quick Find Search type 'Apex' and click 'Apex Classes'
> 2. Click 'Estimate your organization's code coverage'

**Resources:**
> Calculate overall code coverage in Salesforce

---

### Question 42
A SSN__c custom field exists on the Candidate__c custom object. The field is used to store each candidate's social security number and is marked as Unique in the schema definition. As part of a data enrichment process, Universal Containers has a CSV file that contains updated data for all candidates in the system. The file contains each Candidate's social security number as a data point. Universal Containers wants to upload this information into Salesforce, while ensuring all data rows are correctly mapped to a candidate in the system. Which technique should the developer implement to streamline the data upload?
- [x] **A.** Update the SSN__c field definition to mark it as an External Id.  [CORRECT]
- [ ] **B.** Upload the CSV into a custom object related to Candidate__c.  [WRONG]
- [ ] **C.** Create a before insert trigger to correctly map the records.  [WRONG]
- [ ] **D.** Create a Process Builder on the Candidate__c object to map the records.  [WRONG]

**Explanation:**
> Mark the SSN__c field as an External ID on the Candidate__c object. This ensures that the CSV file's SSN values can be used to match and update existing records accurately.

---

### Question 43
A developer created a Visualforce page and custom controller to display the account type field as shown below.
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
The value of the account type field is not being displayed correctly on the page. Assuming the custom controller is properly referenced on the Visualforce page, what should the developer do to correct the problem?
- [ ] **A.** Convert theAccount.Type to a String.  [WRONG]
- [x] **B.** Add a getter method for the actType attribute.  [CORRECT]
- [ ] **C.** Add with sharing to the custom controller.  [WRONG]
- [ ] **D.** Change theAccount attribute to public.  [WRONG]

**Explanation:**
> By default, properties in Apex are private, meaning they can't be accessed directly by the Visualforce page. You need to make the actType property accessible by using the {get; set;} notation.
> public String actType { get; set; }

---

### Question 44
A developer wants to store a description of a product that can be entered on separate lines by a user during product setup and later displayed on a Visualforce page for shoppers. Which field type should the developer choose to ensure that the description will be searchable in the custom Apex SOQL queries that are written?
- [x] **A.** Text Area  [CORRECT]
- [ ] **B.** Text  [WRONG]
- [ ] **C.** Text Area (Long)  [WRONG]
- [ ] **D.** Text Area (Rich)  [WRONG]

**Explanation:**
> Text Area: Lets users enter up to 255 characters that display on separate lines similar to a Description field.

**Resources:**
> Custom Field Types

---

### Question 45
How should a developer create a new custom exception class?
- [x] **A.** public class CustomException extends Exception{}  [CORRECT]
- [ ] **B.** CustomException ex = new (CustomException)Exception();  [WRONG]
- [ ] **C.** public class CustomException implements Exception{}  [WRONG]
- [ ] **D.** (Exception)CustomException ex = new Exception();  [WRONG]

**Explanation:**
> To create your custom exception class, extend the built-in Exception class and make sure your class name ends with the word Exception, such as “MyException” or “PurchaseException”. All exception classes extend the system-defined base class Exception, and therefore, inherits all common Exception methods.
> This example defines a custom exception called MyException.
> public class MyException extends Exception {}

**Resources:**
> Create Custom Exceptions

---

### Question 46
A developer identifies the following triggers on the Expense__c object: deteleExpense, applyDefaultsToExpense, validateExpenseUpdate; The triggers process before delete, before insert, and before update events respectively. Which two techniques should the developer implement to ensure trigger best practices are followed? (Choose two.)
- [ ] **A.** Unify the before insert and before update triggers and use Process Builder for the delete action.  [WRONG]
- [x] **B.** Create helper classes to execute the appropriate logic when a record is saved.  [CORRECT]
- [ ] **C.** Maintain all three triggers on the Expense__c object, but move the Apex logic out of the trigger definition.  [WRONG]
- [x] **D.** Unify all three triggers in a single trigger on the Expense__c object that includes all events.  [CORRECT]

---

### Question 47
Universal Containers has implemented an order management application. Each Order can have one or more Order Line items. The Order Line object is related to the Order via a master-detail relationship. For each Order Line item, the total price is calculated by multiplying the Order Line item price with the quantity ordered. What is the best practice to get the sum of all Order Line item totals on the Order record?
- [x] **A.** Roll-up summary field  [CORRECT]
- [ ] **B.** Quick action  [WRONG]
- [ ] **C.** Apex trigger  [WRONG]
- [ ] **D.** Formula field  [WRONG]

---

### Question 48
Which three statements are accurate about debug logs? (Choose three.)
- [ ] **A.** Only the 20 most recent debug loos for a user are kept.  [WRONG]
- [x] **B.** System debug logs are retained for 24 hours.  [CORRECT]
- [x] **C.** Debug log levels are cumulative, where FINE log level includes all events logged at the DEBUG, INFO, WARN, and ERROR levels.  [CORRECT]
- [ ] **D.** The maximum size of a debug log is 5 MB.  [WRONG]
- [x] **E.** Debug logs can be set for specific users, classes, and triggers.  [CORRECT]

**Explanation:**
> System debug logs are retained for 24 hours. Monitoring debug logs are retained for seven days.
> Each debug level includes one of the following log levels for each log category. The levels are listed from lowest to highest. Specific events are logged based on the combination of category and levels. Most events start being logged at the INFO level. The level is cumulative, that is, if you select FINE, the log also includes all events logged at the DEBUG, INFO, WARN, and ERROR levels.
> To activate debug logging for users, Apex classes, and Apex triggers, configure trace flags and debug levels in the Salesforce Developer Console or in Salesforce Setup.

**Resources:**
> Debug Log
> Debug Log Levels

---

### Question 49
The Account object has a custom Percent field, Rating, defined with a length of 2 with 0 decimal places. An Account record has the value of 50% in its Rating field and is processed in the Apex code below after being retrieved from the database with SOQL.
public void processAccount(){
Decimal acctScore = acct.Rating__c * 100;
}
What is the value of acctScore after this code executes?
- [ ] **A.** 5  [WRONG]
- [ ] **B.** 50  [WRONG]
- [ ] **C.** 500  [WRONG]
- [x] **D.** 5000  [CORRECT]

**Explanation:**
> With the Percent field defined with 0 decimal places, the value stored in the Rating field is 50, not 0.50. When the code executes, it multiplies 50 by 100, resulting in an acctScore of 5000.

---

### Question 50
Which statement is true about developing in a multi-tenant environment?
- [ ] **A.** Apex Sharing controls access to records from multiple tenants on the same instance.  [WRONG]
- [ ] **B.** Org-level data security controls which users can see data from multiple tenants on the same instance.  [WRONG]
- [x] **C.** Governor limits prevent Apex from impacting the performance of multiple tenants on the same instance.  [CORRECT]
- [ ] **D.** Global Apex classes can be referenced from multiple tenants on the same instance.  [WRONG]

**Explanation:**
> Governor limits prevent Apex from impacting the performance of multiple tenants on the same instance. These limits ensure that no single tenant's code can monopolize shared resources, maintaining performance and stability across the environment.

---

### Question 51
Universal Containers decides to use exclusively declarative development to build out a new Salesforce application. Which three options should be used to build out the database layer for the application? (Choose three.)
- [ ] **A.** Process Builder  [WRONG]
- [x] **B.** Roll-up summaries  [CORRECT]
- [ ] **C.** Triggers  [WRONG]
- [x] **D.** Relationships  [CORRECT]
- [x] **E.** Custom objects and fields  [CORRECT]

**Explanation:**
> Database Layer
> Declarative: Custom Objects, Fields, Relationships, Rollups
> Coding: Apex Triggers

**Resources:**
> Understand Separation of Concerns

---

### Question 52
A developer must implement a CheckPaymentProcessor class that provides check processing payment capabilities that adhere to what is defined for payments in the PaymentProcessor interface.
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
}

**Explanation:**
> You need to implement the PaymentProcessor interface and provide the required pay method definition.

---

### Question 53
Universal Containers has a large number of custom applications that were built using a third-party JavaScript framework and exposed using Visualforce pages. The company wants to update these applications to apply styling that resembles the look and feel of Lightning Experience. What should the developer do to fulfill the business request in the quickest and most effective manner?
- [ ] **A.** Set the attribute enableLightning to true in the definition.  [WRONG]
- [ ] **B.** Enable Available for Lightning Experience, Lightning Communities, and the mobile app on Visualforce pages used by the custom application.  [WRONG]
- [x] **C.** Incorporate the Salesforce Lightning Design System CSS stylesheet into the JavaScript applications.  [CORRECT]
- [ ] **D.** Rewrite all Visualforce pages as Lightning components.  [WRONG]

**Explanation:**
> With Lightning stylesheets, it’s easy to tweak your existing Visualforce pages so they’ll display with classic styling in Salesforce Classic and Lightning styling in Lightning Experience.
> 1. From Setup, enter Visualforce in the Quick Find box, then select Visualforce Pages.
> 2. Click Edit next to the Visualforce page.
> 3. Add the lightningStylesheets="true" attribute to the initial <apex:page> component in the Visualforce markup.
> <apex:page standardController="Account" lightningStyleSheets="true">

**Resources:**
> Apply Lightning Stylesheets to Visualforce Pages Manually

---

### Question 54
When a user edits the Postal Code on an Account, a custom Account text field named "Timezone" must be updated based on the values in a PostalCodeToTimezone__c custom object. Which two automation tools can be used to implement this feature? (Choose two.)
- [ ] **A.** Quick actions  [WRONG]
- [ ] **B.** Approval Process  [WRONG]
- [x] **C.** Record-triggered flow  [CORRECT]
- [x] **D.** Account trigger  [CORRECT]

**Explanation:**
> To update the "Timezone" field based on the Postal Code changes, you can use:
> 1. Record-triggered flow: This can be set up to run when the Postal Code is edited, updating the Timezone field accordingly.
> 2. Account trigger: This can be written to handle changes in the Postal Code and update the Timezone field.
> Both methods will effectively handle the automation you need.

---

### Question 55
What are two uses for External IDs? (Choose two.)
- [x] **A.** To create relationships between records imported from an external system.  [CORRECT]
- [ ] **B.** To create a record in a development environment with the same Salesforce ID as in another environment  [WRONG]
- [ ] **C.** To identify the sObject type in Salesforce  [WRONG]
- [x] **D.** To prevent an import from creating duplicate records using Upsert  [CORRECT]

**Explanation:**
> External IDs are commonly used to establish relationships between records imported from an external system. By using an External ID field, you can link records in Salesforce to corresponding records in an external system, facilitating data integration and synchronization.
> One of the key uses of External IDs is to prevent duplicate records during data imports by using the Upsert operation. By specifying an External ID field as the matching criteria, Salesforce can identify existing records based on that field and update them instead of creating duplicates.

---

### Question 56
An Apex method, getAccounts, that returns a List of Accounts given a searchTerm, is available for Lightning Web components to use. What is the correct definition of a Lightning Web component property that uses the getAccounts method?
- [x] **A.** @wire(getAccounts, { searchTerm: '$searchTerm'})  accountList;  [CORRECT]
- [ ] **B.** @AuraEnabled(getAccounts, '$searchTerm') accountList;  [WRONG]
- [ ] **C.** @AuraEnabled(getAccounts, { searchTerm: '$searchTerm'}) accountList;  [WRONG]
- [ ] **D.** @wire(getAccounts, '$searchTerm') accountList;  [WRONG]

**Explanation:**
> To read Salesforce data, Lightning web components use a reactive wire service. Use @wire in a component’s JavaScript class to specify an Apex method. You can @wire a property or a function to receive the data. To operate on the returned data, @wire a function.

**Resources:**
> Wire Apex Methods to Lightning Web Components

---

### Question 57
Which three declarative fields are correctly mapped to variable types in Apex? (Choose three.)
- [x] **A.** Number maps to Decimal.  [CORRECT]
- [ ] **B.** Number maps to Integer.  [WRONG]
- [ ] **C.** TextArea maps to List of type String.  [WRONG]
- [x] **D.** Date/Time maps to Dateline.  [CORRECT]
- [x] **E.** Checkbox maps to Boolean.  [CORRECT]

---

### Question 58
Which two practices should be used for processing records in a trigger? (Choose two.)
- [x] **A.** Use a Map to reduce the number of SOQL calls.  [CORRECT]
- [ ] **B.** Use @future methods to handle DML operations.  [WRONG]
- [x] **C.** Use a Set to ensure unique values in a query filter.  [CORRECT]
- [ ] **D.** Use (callout=true) to update an external system.  [WRONG]

**Explanation:**
> Using Maps and Sets in Bulk Triggers
> Set and map data structures are critical for successful coding of bulk triggers. Sets can be used to isolate distinct records, while maps can be used to hold query results organized by record ID.

---

### Question 1
A developer wants to mark each Account in a List as either Active or Inactive, based on the value in the LastModifiedDate field of each Account being greater than 90 days in the past. Which Apex technique should the developer use?
- [ ] **A.** A for loop, with a switch statement inside  [WRONG]
- [ ] **B.** A switch statement, with a for loop inside  [WRONG]
- [ ] **C.** An if-else statement, with a for loop inside  [WRONG]
- [x] **D.** A for loop, with an if-else statement inside  [CORRECT]

**Explanation:**
> To mark each Account as Active or Inactive based on the LastModified field value, the developer should use a for loop, with an if/else statement inside. This technique allows the developer to iterate through each account and apply the conditional logic to determine the status based on the 90-day threshold.

---

### Question 2
A developer has identified a method in an Apex class that performs resource intensive actions in memory by iterating over the result set of a SOQL statement on the account. The method also performs a DML statement to save the changes to the database. Which two techniques should the developer implement as a best practice to ensure transaction control and avoid exceeding governor limits? (Choose two.)
- [ ] **A.** Use the @ReadOnly annotation to bypass the number of rows returned by a SOQL.  [WRONG]
- [ ] **B.** Use partial DML statements to ensure only valid data is committed.  [WRONG]
- [x] **C.** Use the System.Limit class to monitor the current CPU governor limit consumption.  [CORRECT]
- [x] **D.** Use the Database.Savepoint method to enforce database integrity.  [CORRECT]

**Explanation:**
> The developer should implement the following best practices to ensure transaction control and avoid exceeding governor limits:
> Use the System.Limit class to monitor the current CPU governor limit consumption: This helps keep track of how close the code is to hitting governor limits and can allow for proactive management.
> Use the Database.Savepoint method to enforce database integrity: Savepoints allow the developer to roll back to a certain point in the transaction if necessary, which is critical for maintaining data integrity during complex operations.

---

### Question 3
What should a developer use to script the deployment and unit test execution as part of continuous integration?
- [ ] **A.** Developer Console  [WRONG]
- [x] **B.** Salesforce CLI  [CORRECT]
- [ ] **C.** VS Code  [WRONG]
- [ ] **D.** Execute Anonymous  [WRONG]

**Explanation:**
> A developer should use Salesforce DX (SFDX) for scripting the deployment and unit test execution as part of continuous integration. Here's how:
> SFDX CLI: Command-line interface tools enable you to script deployment and automate unit tests.
> Continuous Integration Tools: Combine SFDX with CI tools like Jenkins, GitHub Actions, or CircleCI to automate the deployment process and run your tests seamlessly.

---

### Question 4
What are two ways for a developer to execute tests in an org? (Choose two.)
- [x] **A.** Tooling API  [CORRECT]
- [x] **B.** Developer Console  [CORRECT]
- [ ] **C.** Metadata API  [WRONG]
- [ ] **D.** Bulk API  [WRONG]

**Explanation:**
> Run Unit Test Methods
> To verify the functionality of your Apex code, execute unit tests. You can run Apex test methods in the Developer Console, in Setup, in the Salesforce extensions for Visual Studio Code, or using the API.

**Resources:**
> Run Unit Test Methods

---

### Question 5
Which tool allows a developer to send requests to the Salesforce REST APIs and view the responses?
- [ ] **A.** REST resource path URL  [WRONG]
- [x] **B.** Workbench REST Explorer  [CORRECT]
- [ ] **C.** Developer Console REST tab  [WRONG]
- [ ] **D.** Force.com IDE REST Explorer tab  [WRONG]

**Explanation:**
> Workbench Rest Explorer allows developers to send requests to the Salesforce REST APIs and view the responses, making it an excellent choice for testing and interacting with RESTful services in Salesforce.

---

### Question 6
A developer needs to create a baseline set of data (Accounts, Contacts, Products, Assets) for an entire suite of tests allowing them to test independent requirements various types of Salesforce Cases. Which approach can efficiently generate the required data for each unit test?
- [ ] **A.** Create a mock using the Stub API.  [WRONG]
- [x] **B.** Use @TestSetup with a void method.  [CORRECT]
- [ ] **C.** Add @IsTest(seeAllData=true) at the start of the unit test class.  [WRONG]
- [ ] **D.** Create test data before Test.startTest() in the unit test.  [WRONG]

---

### Question 7
Which three statements are true regarding custom exceptions in Apex? (Choose three.)
- [x] **A.** A custom exception class must extend the system Exception class.  [CORRECT]
- [x] **B.** A custom exception class can implement one or many interfaces.  [CORRECT]
- [ ] **C.** A custom exception class cannot contain member variables or methods.  [WRONG]
- [x] **D.** A custom exception class name must end with "Exception"  [CORRECT]
- [ ] **E.** A custom exception class can extend other classes besides the Exception class.  [WRONG]

**Explanation:**
> To create your custom exception class, extend the built-in Exception class and make sure your class name ends with the word Exception, such as “MyException” or “PurchaseException”. All exception classes extend the system-defined base class Exception, and therefore, inherits all common Exception methods.

**Resources:**
> Create Custom Exceptions

---

### Question 8
A developer writes a trigger on the Account object on the before update event that increments a count field. A workflow rule also increments the count field every time that an Account is created or updated. The field update in the workflow rule is configured to not re-evaluate workflow rules. What is the value of the count field if an Account is inserted with an initial value of zero, assuming no other automation logic is implemented on the Account?
- [ ] **A.** 1  [WRONG]
- [ ] **B.** 3  [WRONG]
- [ ] **C.** 4  [WRONG]
- [x] **D.** 2  [CORRECT]

**Explanation:**
> 1. Initial Value: The Account is initially created with a value of 0.
> 2. Trigger: The trigger fires before the update, incrementing the count to 1.
> 3. Workflow Rule: The workflow rule triggers and increments the count to 2.
> Since the workflow rule is configured to not re-evaluate, it will not trigger again after the trigger's update. Therefore, the final value of the count field will be 2.

---

### Question 9
For which three items can a trace flag be configured? (Choose three.)
- [x] **A.** Apex Trigger  [CORRECT]
- [x] **B.** Apex Class  [CORRECT]
- [ ] **C.** Process Builder  [WRONG]
- [x] **D.** User  [CORRECT]
- [ ] **E.** Visualforce  [WRONG]

**Explanation:**
> Set Up Debug Logging
> To activate debug logging for users, Apex classes, and Apex triggers, configure trace flags and debug levels in the Developer Console or in Setup. Each trace flag includes a debug level, start time, end time, and log type. The trace flag’s log type specifies the entity you’re tracing.

**Resources:**
> Set Up Debug Logging

---

### Question 10
Which three data types can be returned from an SOQL statement? (Choose three.)
- [ ] **A.** Boolean  [WRONG]
- [x] **B.** List of sObjects  [CORRECT]
- [x] **C.** Single sObject  [CORRECT]
- [x] **D.** Integer  [CORRECT]
- [ ] **E.** String  [WRONG]

**Explanation:**
> SOQL can return several data types:
> List<sObject>: This is used to retrieve multiple records.
> Single sObject: When you're querying for just one record.
> AggregateResult: Useful for aggregate queries, like those with GROUP BY.
> Integer: Useful for Useful for count records.

---

### Question 11
In which three areas can a Lightning component be used in the Lightning Experience? (Choose three.)
- [ ] **A.** Lightning Report page  [WRONG]
- [ ] **B.** Lightning Connect page  [WRONG]
- [x] **C.** Lightning Record Page  [CORRECT]
- [x] **D.** Lightning Community Page  [CORRECT]
- [x] **E.** Lightning Home page  [CORRECT]

**Resources:**
> Adding an LWC Card to a Lightning or Community Page
> Lightning Web Components in Lightning Communities

---

### Question 12
What are three ways for a developer to execute tests in an org?
- [x] **A.** Tooling API  [CORRECT]
- [x] **B.** Salesforce DX  [CORRECT]
- [ ] **C.** Metadata API  [WRONG]
- [ ] **D.** Bulk API  [WRONG]
- [x] **E.** Setup Menu  [CORRECT]

**Explanation:**
> A developer can execute tests in an org using these three ways:
> Tooling API : Allows for powerful interactions with Salesforce metadata, including running tests.
> Setup Menu : Provides a user-friendly interface to run tests directly within the Salesforce setup area.
> Salesforce DX : Offers robust command-line tools to manage and run tests as part of your development workflow.

**Resources:**
> Run Apex Tests
> Introducing Tooling API

---

### Question 13
Which set of roll-up types are available when creating a roll-up summary field?
- [x] **A.** COUNT, SUM, MIN, MAX  [CORRECT]
- [ ] **B.** AVERAGE, SUM, MIN, MAX  [WRONG]
- [ ] **C.** SUM, MIN, MAX  [WRONG]
- [ ] **D.** AVRAGE, COUNT, SUM, MIN, MAX  [WRONG]

**Explanation:**
> Roll-Up Summary Field
> A roll-up summary field calculates values from related records, such as those in a related list. You can create a roll-up summary field to display a value in a master record based on the values of fields in a detail record. The detail record must be related to the master through a master-detail relationship.
> You can perform different types of calculations with a roll-up summary field. You can count the number of detail records related to a master record. Or, you can calculate the sum, minimum value, or maximum value of a field in the detail records.

**Resources:**
> Roll-Up Summary Field

---

### Question 14
Which scenario is valid for execution by unit tests?
- [x] **A.** Set the created of a record using a system method.  [CORRECT]
- [ ] **B.** Generate a Visualforce Pdf with getContentasPdf().  [WRONG]
- [ ] **C.** Load data from a remote site with a callout.  [WRONG]
- [ ] **D.** Execute anonymous Apex as a different user.  [WRONG]

**Explanation:**
> You can create a test record, set its CreatedDate using a system method, and then assert that the value is correct.
> setCreatedDate(recordId, createdDatetime)

**Resources:**
> Test Class

---

### Question 15
Which two conditions cause workflow rules to fire? (Choose two.)
- [x] **A.** An Apex Batch process that changes field values.  [CORRECT]
- [x] **B.** Updating records using the bulk API  [CORRECT]
- [ ] **C.** Converting leads to person accounts  [WRONG]
- [ ] **D.** Changing the territory assignments of accounts and opportunities  [WRONG]

**Explanation:**
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

**Resources:**
> Workflow Considerations

---

### Question 16
What are three capabilities of the tag when loading JavaScript resources in Aura components? (Choose three.)
- [x] **A.** One-time loading for duplicate scripts  [CORRECT]
- [x] **B.** Specifying loading order  [CORRECT]
- [ ] **C.** Loading externally hosted scripts  [WRONG]
- [ ] **D.** Loading files from Documents  [WRONG]
- [x] **E.** Loading scripts in parallel  [CORRECT]

**Resources:**
> Using External JavaScript Libraries

---

### Question 17
Which three resources in an Aura component can contain JavaScript functions? (Choose three.)
- [x] **A.** Helper  [CORRECT]
- [ ] **B.** Design  [WRONG]
- [x] **C.** Renderer  [CORRECT]
- [ ] **D.** Style  [WRONG]
- [x] **E.** Controller  [CORRECT]

**Explanation:**
> The following resources can define and use JavaScript functions in Salesforce Aura components:
> 1. Controller: The controller is in charge of specifying the JavaScript functions that manage the logic and actions of the component. It includes the methods that the component's events or those of other components call. These procedures are listed and associated with the component in the controller's JavaScript file.
> 2. Helper: The helper is a supplemental resource that may be used to add further JavaScript features to assist the operation of the component. It can have reusable functions that are invoked by the component's controller or other helpers and is defined in a separate JavaScript file.
> 3. Renderer: The renderer is yet another optional resource that enables you to change or improve the way a component renders. It can have functions that alter the component's DOM elements, styles, or other visual components during rendering. It is defined in a distinct JavaScript file.

**Resources:**
> Component Bundles

---

### Question 18
A developer created a Visualforce page and a custom controller with methods to handle different buttons and events that can occur on the page. What should the developer do to deploy to production?
- [ ] **A.** Create a test class that provides coverage of the Visualforce page.  [WRONG]
- [ ] **B.** Create a test page that provides coverage of the Visualforce page.  [WRONG]
- [ ] **C.** Create a test page that provides coverage of the custom controller.  [WRONG]
- [x] **D.** Create a test class that provides coverage of the custom controller.  [CORRECT]

**Explanation:**
> To ensure the quality and reliability of your Visualforce page and custom controller before deploying to production, it's crucial to write comprehensive unit tests for the custom controller. This will help identify potential issues and bugs early in the development process.
> To deploy it we need code coverage above 75%.

---

### Question 19
Universal Containers has an order system that uses an Order Number to identify an order for customers and service agents. Order records will be imported into Salesforce. How should the Order Number field be defined in Salesforce?
- [ ] **A.** Direct Lookup  [WRONG]
- [ ] **B.** Lookup  [WRONG]
- [x] **C.** Number with External ID  [CORRECT]
- [ ] **D.** Indirect Lookup  [WRONG]

**Explanation:**
> Using External ID and Unique would ensure each order has a unique identification in Salesforce.

---

### Question 20
Which standard field is required when creating a new Contact record?
- [x] **A.** LastName  [CORRECT]
- [ ] **B.** Name  [WRONG]
- [ ] **C.** AccountId  [WRONG]
- [ ] **D.** FirstName  [WRONG]

**Explanation:**
> The only required standard field when creating a new Contact record in Salesforce is the Last Name field.

**Resources:**
> Contact

---

### Question 21
A developer wrote a unit test to confirm that a custom exception works properly in a custom controller, but the test failed due to an exception being thrown. Which step should the developer take to resolve the issue and properly test the exception?
- [x] **A.** Use try/catch within the unit test to catch the exception.  [CORRECT]
- [ ] **B.** Use the finally block within the unit test to populate the exception.  [WRONG]
- [ ] **C.** Use the database methods with all or none set to FALSE.  [WRONG]
- [ ] **D.** Use Test.isRunningTest() within the custom controller.  [WRONG]

**Explanation:**
> By using a try/catch block, the developer can assert that the correct exception type is thrown and that the exception message contains the expected information. This ensures that the custom exception is working as intended and the unit test is reliable.

---

### Question 22
A developer is asked to create a Visualforce page that lists the contacts owned by the current user. This component will be embedded in a Lightning page. Without writing unnecessary code, which controller should be used for this purpose?
- [ ] **A.** Standard controller  [WRONG]
- [ ] **B.** Custom controller  [WRONG]
- [x] **C.** Standard list controller  [CORRECT]
- [ ] **D.** Lightning controller  [WRONG]

**Explanation:**
> Standard list controllers allow you to create Visualforce pages that can display or act on a set of records. Examples of existing Salesforce pages that work with a set of records include list pages, related lists, and mass action pages.

**Resources:**
> Standard List Controllers

---

### Question 23
The following code snippet is executed by a Lightning web component in an environment with more than 2,000 lead records:
@AuraEnabled
public void static updateLeads(){
for(Lead thisLead : [SELECT Origin__c FROM Lead]){
thisLead.LeadSource = thisLead.Origin__c;
update thisLead;
}
}
Which governor limit will likely be exceeded within the Apex transaction?
- [ ] **A.** Total number of SOQL queries issued  [WRONG]
- [x] **B.** Total number of DML statements issued  [CORRECT]
- [ ] **C.** Total number of records processed as a result of DML statements  [WRONG]
- [ ] **D.** Total number of records retrieved by SOQL queries  [WRONG]

**Explanation:**
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

---

### Question 24
How can a developer warn users of SOQL governor limit violations in a trigger?
- [ ] **A.** Use Messaging.SendEmail() to continue the transaction and send an alert to the user after the number of SOQL queries exceeds the limit.  [WRONG]
- [ ] **B.** Use PageReference.setRedirect() to redirect the user to a custom Visualforce page before the number of SOQL queries exceeds the limit.  [WRONG]
- [x] **C.** Use Limits.getQueries() and display an error message before the number of SOQL queries exceeds the limit.  [CORRECT]
- [ ] **D.** Use ApexMessage.Message() to display an error message after the number of SOQL queries exceeds the limit.  [WRONG]

**Explanation:**
> By checking the current number of SOQL queries using Limits.getQueries(), the trigger can proactively identify potential issues before they lead to a transaction failure.

**Resources:**
> Limits Class

---

### Question 25
What are two valid options for iterating through each Account in the collection List named AccountList? (Choose two.)
- [x] **A.** for(Account theAccount : AccountList){ }  [CORRECT]
- [ ] **B.** for(AccountList){ }  [WRONG]
- [ ] **C.** for(List L : AccountList){ }  [WRONG]
- [x] **D.** for(Integer i=0; i < AccountList.Size(); i++){ }  [CORRECT]

**Explanation:**
> The two valid options for iterating through each Account in the collection List named AccountList are:
> A. for(Account theAccount : AccountList){ }
> This is the most common and efficient way to iterate over a list in Apex. It directly iterates over each Account object in the AccountList, assigning it to the theAccount variable for processing.
> D. for(Integer i=0; i < AccountList.Size(); i++){ }
> This is a traditional for loop that iterates over the indices of the list. Inside the loop, you can access each Account using AccountList[i]. While this approach works, it's generally less efficient than the enhanced for loop in option A.

---

### Question 26
A developer created these three Rollup Summary fields in the custom object, Project__c: - Total_Timesheets__c
- Total_Approved_Timesheets__c - Total_Rejected_Timesheets__c The developer is asked to create a new field that shows the ratio between rejected and approved timesheets for a given project. Which should the developer use to implement the business requirement in order to minimize maintenance overhead?
- [ ] **A.** Apex trigger  [WRONG]
- [ ] **B.** Record-triggered flow  [WRONG]
- [x] **C.** Formula field  [CORRECT]
- [ ] **D.** Field Update actions  [WRONG]

**Explanation:**
> Formula fields are calculated automatically whenever the related fields (Total_Approved_Timesheets__c and Total_Rejected_Timesheets__c) change. This ensures that the ratio is always up-to-date.
> Formula:
> (Total_Rejected_Timesheets__c / Total_Approved_Timesheets__c)

---

### Question 27
Which three statements are true regarding cross-object formulas? (Choose three.)
- [x] **A.** Cross-object formulas can reference fields from objects that are up to 10 relationships away.  [CORRECT]
- [x] **B.** Cross-object formulas can reference fields from master-detail or lookup relationships.  [CORRECT]
- [ ] **C.** Cross-object formulas can reference child fields to perform an average.  [WRONG]
- [x] **D.** Cross-object formulas can expose data the user does not have access to in a record.  [CORRECT]
- [ ] **E.** Cross-object formulas can be referenced in roll-up summary fields.  [WRONG]

**Explanation:**
> A Cross-object formula is a formula that spans two related objects and references merge fields on those objects. A cross-object formula can reference merge fields from a master (“parent”) object if an object is on the detail side of a master-detail relationship. A cross-object formula also works with lookup relationships.
> You can reference fields from objects that are up to 10 relationships away. A cross-object formula is available anywhere formulas are used except when creating default values.
> If you create a formula that references a field on another object and display that formula in your page layout, users can see the field on the object even if they don’t have access to that object record.

**Resources:**
> What Is a Cross-Object Formula?

---

### Question 28
A developer working on a time management application wants to make total hours for each timecard available to application users. A timecard entry has a Master Detail relationship to a timecard. Which approach should the developer use to accomplish this declaratively?
- [ ] **A.** A Visualforce page that calculates the total number of hours for a timecard and displays it on the page  [WRONG]
- [x] **B.** A Roll-Up Summary field on the Timecard Object that calculates the total hours from timecard entries for that timecard  [CORRECT]
- [ ] **C.** A Process Builder process that updates a field on the timecard when a timecard entry is created  [WRONG]
- [ ] **D.** An Apex trigger that uses an Aggregate Query to calculate the hours for a given timecard and stores it in a custom field  [WRONG]

**Explanation:**
> Roll-up summary fields are a declarative feature that can be configured directly in the object's field definition. The system automatically calculates the total hours whenever a new timecard entry is created, updated, or deleted, ensuring that the value is always up-to-date.

---

### Question 29
What can be used to override the Account's standard Edit button for Lightning Experience?
- [ ] **A.** Lightning action  [WRONG]
- [ ] **B.** Lightning flow  [WRONG]
- [ ] **C.** Lightning page  [WRONG]
- [x] **D.** Lightning component  [CORRECT]

**Explanation:**
> Lightning components are the ideal way to override standard buttons in Lightning Experience. They provide the flexibility to create custom user interfaces and behaviors, allowing you to customize the editing experience for Account records.

**Resources:**
> Override Standard Actions with Aura Components

---

### Question 30
A developer needs to allow user to complete a form on an Account record that will create a record for a custom object, The form needs to display different fields depending on the user’s job role. The functionality should only be available to a small group of users. Which three things should the developer do to satisfy these requirements?
- [ ] **A.** Add a dynamic action to the user’s assigned page layouts.  [WRONG]
- [ ] **B.** Create a light web component.  [WRONG]
- [x] **C.** Create a dynamic form.  [CORRECT]
- [x] **D.** Add a dynamic action to the Account record page.  [CORRECT]
- [x] **E.** Create a custom permission for the users.  [CORRECT]

---

### Question 31
While writing an Apex class, a developer wants to make sure that all functionality being developed is handled as specified by the requirements. Which approach should the developer use to be sure that the Apex class is working according to specifications?
- [ ] **A.** Include a try/catch block to the Apex class.  [WRONG]
- [ ] **B.** Run the code in an execute Anonymous block in the developer console.  [WRONG]
- [x] **C.** Create a test class to execute the business logic and run the test in the developer console.  [CORRECT]
- [ ] **D.** Include a savepoint and Database.rollback().  [WRONG]

---

### Question 32
What should a developer use to obtain the Id and Name of all the Leads, Accounts, and Contacts that have the company name 'Universal Containers'?
- [ ] **A.** FIND 'Universal Containers' IN CompanyName Fields RETURNING lead{ld,name), account(Id, name), contact(Id, name)  [WRONG]
- [x] **B.** FIND 'Universal Containers' IN Name Fields RETURNING lead(id, name), account(Id, name), contact(Id, name)  [CORRECT]
- [ ] **C.** SELECT lead(id, name), account(Id, name), contact(Id, name) FROM Lead, Account, Contact WHERE Name = "universal Containers'  [WRONG]
- [ ] **D.** SELECT Lead.id. Lead.Name, Account.Id, AccountName, Contacted, Contact.Name FROM Lead, Account, Contact WHERE CompanvName * Universal Containers'  [WRONG]

**Explanation:**
> IN CompanyName" does not exist.
> This query(B) will search for the string "Universal Containers" within the Name field of Lead, Account, and Contact objects and return the specified fields for matching records.

**Resources:**
> SOSL Syntax

---

### Question 33
In a single record, a user selects multiple values from a multi-select picklist. How are the selected values represented in Apex?
- [ ] **A.** As a List<String> with each value as a element in the list.  [WRONG]
- [ ] **B.** As a String with each value separated by a comma  [WRONG]
- [x] **C.** As a String with each value separated by a semicolon  [CORRECT]
- [ ] **D.** As a Set<String> with each value as a element in the set.  [WRONG]

**Explanation:**
> When a user selects multiple values from a multi-select picklist, the selected values are stored in the database as a single string, with each value separated by a comma.
> For example, if a user selects "Red", "Green", and "Blue" from a multi-select picklist, the value stored in the database would be "Red,Green,Blue".

---

### Question 34
What does the Lightning Component framework provide to developers?
- [ ] **A.** Support for Classic and Lightning UIs  [WRONG]
- [ ] **B.** Templates to create custom components  [WRONG]
- [ ] **C.** Extended governor limits for applications  [WRONG]
- [x] **D.** Prebuilt components that can be reused  [CORRECT]

**Explanation:**
> The Lightning Component framework provides a rich set of pre-built components that developers can reuse to quickly build custom applications. These components handle common UI elements like buttons, input fields, modals, and data tables, saving developers time and effort.

---

### Question 35
What are two benefits of the Lightning Component framework? (Choose two.)
- [ ] **A.** It simplifies complexity when building pages, but not applications.  [WRONG]
- [x] **B.** It provides an event-driven architecture for better decoupling between components.  [CORRECT]
- [x] **C.** It promotes faster development using out-of-box components that are suitable for desktop and mobile devices.  [CORRECT]
- [ ] **D.** It allows faster PDF generation with Lightning components.  [WRONG]

**Explanation:**
> It provides an event-driven architecture for better decoupling between components.
> This allows for modularity and reusability of components. Components can communicate with each other through events, making the overall application more maintainable and scalable.
> It promotes faster development using out-of-box components that are suitable for desktop and mobile devices.
> The framework provides a wide range of pre-built components that can be customized and used to create responsive user interfaces that adapt to different screen sizes. This accelerates development time and ensures consistency across devices.

---

### Question 36
Given the following code snippet, that is part of a custom controller for a Visualforce page:
public void updateContact(Contact thisContact){
thisContact.Is_Active__c = false;
try{
update thisContact;
}catch(Exception e){
String errorMessage = 'An error occurred while updating the Contact. '+e.getMessage());
ApexPages.addmessage (new ApexPages.message (ApexPages.severity.FATAL,errorMessage));
}
}
In which two ways can the try/catch be enclosed to enforce object-level permissions and prevent the DML statement from being executed if the current logged- in user does not have the appropriate level of access to the object? (Choose two.)
- [ ] **A.** Use if(thisContact.OwnerId == User.Info.getUserId())  [WRONG]
- [x] **B.** Use if(Schema.sObjectType.Contact.isAccessible())  [CORRECT]
- [ ] **C.** Use if(Schema.sObjectType.Contact.fields.Is_Active__c.isUpdateable())  [WRONG]
- [x] **D.** Use if(Schema.sObjectType.Contact.isUpdateable())  [CORRECT]

**Explanation:**
> B. Schema.sObjectType.<objectApiName>.isAccessible() checks if the current user has has read access to the specified object.
> D. Use if(Schema.sObjectType.Contact.isUpdateable()) checks if the current user has permission to update on the object.

---

### Question 37
What can be used to delete components from production?
- [ ] **A.** A change set deployment with a destructiveChanges XML file  [WRONG]
- [ ] **B.** A change set deployment with the delete option checked  [WRONG]
- [x] **C.** An ant migration tool deployment with a destructiveChanges XML file and an empty package.xml file  [CORRECT]
- [ ] **D.** An ant migration tool deployment with a desctuctiveChanges XML file and the components to delete in the package.xml file  [WRONG]

**Explanation:**
> Destructive Changes XML File: This file specifically lists the components you want to delete.
> Empty package.xml File: An empty package.xml file indicates that you're not deploying any new or modified components, only deleting the ones specified in the destructiveChanges.xml file.

**Resources:**
> Deleting Files from an Organization

---

### Question 38
A developer is debugging the following code to determine why Accounts are not being created. Account a = new Account(Name = 'A'); Database.insert(a, false); How should the code be altered to help debug the issue?
- [ ] **A.** Add a System.debug() statement before the insert method.  [WRONG]
- [x] **B.** Collect the insert method return value in a SaveResult record.  [CORRECT]
- [ ] **C.** Set the second insert method parameter to TRUE.  [WRONG]
- [ ] **D.** Add a try/catch around the insert method.  [WRONG]

**Explanation:**
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

---

### Question 39
Managed Packages can be created in which type of org?
- [ ] **A.** Developer Sandbox  [WRONG]
- [ ] **B.** Partial Copy Sandbox  [WRONG]
- [ ] **C.** Unlimited Edition  [WRONG]
- [x] **D.** Developer Edition  [CORRECT]

**Explanation:**
> You must use a Developer Edition organization to create and work with a managed package. A Developer Edition organization can contain a single managed package and many unmanaged packages.

**Resources:**
> Before you create a managed package

---

### Question 40
A Platform Developer needs to implement a declarative solution that will display the most recent Closed Won date for all Opportunity records associated with an Account. Which field is required to achieve this declaratively?
- [ ] **A.** Roll-up summary field on the Opportunity object  [WRONG]
- [ ] **B.** Cross-object formula field on the Opportunity object  [WRONG]
- [x] **C.** Roll-up summary field on the Account object  [CORRECT]
- [ ] **D.** Cross-object formula field on the Account object  [WRONG]

**Explanation:**
> An opportunity has a lookup field of account. Even though the relationship is a lookup, Salesforce treats certain standard object relationships in a hybrid model i.e. Relationship is Lookup but behaves like Master-Detail
> Also in the backend, there is a relationship property 'cascade delete' between Contact and Account which is always set to True. You will find the same cascade delete Property between objects in a Master-Detail Relationship.
> So for any relationship where the cascade delete is set to True a child record is deleted when the parent is deleted.

---

### Question 41
Universal Containers wants Opportunities to be locked from editing when reaching the Closed/Won stage. Which two strategies should a developer use to accomplish this? (Choose two.)
- [ ] **A.** Use a Visual Workflow.  [WRONG]
- [x] **B.** Use a validation rule.  [CORRECT]
- [ ] **C.** Use the Process Automation Settings.  [WRONG]
- [x] **D.** Use a Trigger.  [CORRECT]

**Explanation:**
> Use a validation rule: Create a validation rule that fires when the Opportunity Stage is changed to "Closed Won". The rule can check if the Opportunity is already closed won and throw an error message if the user attempts to edit any fields.
> Using a trigger and addError() is a powerful and flexible approach to validate data and prevent invalid records from being created or updated in Salesforce.

---

### Question 42
A development team wants to use a deployment script to automatically deploy to a sandbox during their development cycles. Which two tools can they use to run a script that deploys to a sandbox? (Choose two.)
- [x] **A.** SFDX CLI  [CORRECT]
- [ ] **B.** Developer Console  [WRONG]
- [ ] **C.** Change Sets  [WRONG]
- [x] **D.** VSCode  [CORRECT]

**Explanation:**
> SFDX CLI: A powerful command-line tool for automating Salesforce development tasks, including deployments. It allows you to create scripts to deploy metadata changes to sandboxes.
> VSCode: A popular code editor with extensions that can integrate with SFDX. You can use it to write and run deployment scripts, as well as to automate the deployment process using tasks and workflows.

---

### Question 43
Using the Schema Builder, a developer tries to change the API name of a field that is referenced in an Apex test class. What is the end result?
- [x] **A.** The API name is not changed and there are no other impacts.  [CORRECT]
- [ ] **B.** The API name of the field and the reference in the test class is changed.  [WRONG]
- [ ] **C.** The API name of the field is changed, and a warning is issued to update the class.  [WRONG]
- [ ] **D.** The API name of the field and the reference in the test class is updated.  [WRONG]

**Explanation:**
> Change the API name of a field
> The API name of a Field or Object is necessary, as this will be referenced in the metadata ( i.e Apex Classes, Triggers, Visualforce Pages, Visualforce Components etc). It is not allowed for Users to change the API name of the Objects/Fields, if it is referenced in any of the metadata. The changing of API Name without removing references can result in errors being thrown as the operation will be unsupported.

---

### Question 44
A Next Best Action strategy uses an Enhance Element that invokes an Apex method to determine a discount level for a Contact, based on a number of factors. What is the correct definition of the Apex method?
- [x] **A.** @InvocableMethod global static List<List<Recommendation>> getLevel(List<ContactWrapper> input) { /*implementation*/ }  [CORRECT]
- [ ] **B.** @InvocableMethod global List<List<Recommendation>> getLevel(List<ContactWrapper> input){ /*implementation*/ }  [WRONG]
- [ ] **C.** @InvocableMethod global static ListRecommendation getLevel(List<ContactWrapper> input){ /*implementation*/ }  [WRONG]
- [ ] **D.** @InvocableMethod global Recommendation getLevel(ContactWrapper input){ /*implementation*/ }  [WRONG]

**Explanation:**
> Invocable methods are called natively from Rest, Apex, Flow, or Einstein bot that interacts with the external API source. Invocable methods have dynamic input and output values and support describe calls. The invocable method must be static and public or global, and its class must be an outer class.

**Resources:**
> InvocableMethod Annotation

---

### Question 45
An Apex transaction inserts 100 Account records and 2,000 Contact records before encountering a DML exception when attempting to insert 500 Opportunity records. The Account records are inserted by calling the database.insert() method with the allOrNone argument set to false. The Contact and Opportunity records are inserted using the standalone insert statement. How many total records will be committed to the database in this transaction?
- [ ] **A.** 2,000  [WRONG]
- [ ] **B.** 2,100  [WRONG]
- [x] **C.** 0  [CORRECT]
- [ ] **D.** 100  [WRONG]

**Explanation:**
> All operations are in one transaction. If any operation in the transaction fails, all DML operation are rolledback.

**Resources:**
> Bulk DML Exception Handling

---

### Question 46
Universal Containers stores the availability date on each Line Item of an Order and Orders are only shipped when all of the Line Items are available. Which method should be used to calculate the estimated ship date for an Order?
- [ ] **A.** Use a LATEST formula on each of the latest availability date fields.  [WRONG]
- [ ] **B.** Use a CEILING formula on each of the latest availability date fields.  [WRONG]
- [ ] **C.** Use a DAYS formula on each of the availability date fields and a COUNT Roll-Up Summary field on the Order.  [WRONG]
- [x] **D.** Use a MAX Roll-Up Summary field on the latest availability date fields.  [CORRECT]

**Explanation:**
> A MAX Roll-Up Summary field is the most suitable option for this scenario. It will calculate the maximum availability date among all line items associated with an order. This maximum date will represent the latest availability date for any item in the order, which, in turn, will be the estimated ship date.

---

### Question 47
The following Apex method is part of the ContactService class that is called from a trigger:
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
}

**Explanation:**
> A DML statement should be placed outside of a loop to optimize performance and reduce governor limit usage.

---

### Question 48
What is an example of a polymorphic lookup field in Salesforce?
- [x] **A.** The WhatId field on the standard Event object  [CORRECT]
- [ ] **B.** The ParentId field on the standard Account object  [WRONG]
- [ ] **C.** A custom field, Link__c, on the standard Contact object that looks up to an Account or a Campaign  [WRONG]
- [ ] **D.** The LeadId and ContactId fields on the standard Campaign Member object  [WRONG]

**Explanation:**
> A polymorphic lookup field can reference multiple different object types. The WhatId field on the Event object is a classic example of this. It can reference either a Lead, Contact, Account, or Opportunity.

**Resources:**
> Understanding Relationship Fields and Polymorphic Fields

---

### Question 49
Which three operations affect the number of times a trigger can fire? (Choose three.)
- [x] **A.** Lightning Flows  [CORRECT]
- [x] **B.** Roll-Up Summary fields  [CORRECT]
- [ ] **C.** Criteria-based Sharing calculations  [WRONG]
- [x] **D.** Workflow Rules  [CORRECT]
- [ ] **E.** Email messages  [WRONG]

**Explanation:**
> The three operations that affect the number of times a trigger can fire are:
> 1. Lightning Flows
> 2. Roll-Up Summary fields
> 3. Workflow Rules
> These operations can cause triggers to execute multiple times due to updates they perform on records.

---

### Question 50
A Salesforce Administrator is creating a record-triggered now. When certain criteria are met, the now must call an Apex method to execute a complex validation involving several types of objects. When creating the Apex method, which annotation should a developer use to ensure the method can be used within the flow?
- [ ] **A.** @RemoteAction  [WRONG]
- [ ] **B.** @future  [WRONG]
- [ ] **C.** @AuraEnabled  [WRONG]
- [x] **D.** @InvocableMethod  [CORRECT]

**Explanation:**
> Invocable methods are called natively from Rest, Apex, Flow, or Einstein bot that interacts with the external API source. Invocable methods have dynamic input and output values and support describe calls.

**Resources:**
> InvocableMethod Annotation

---

### Question 51
A developer is creating an app that contains multiple Lightning web components. One of the child components is used for navigation purposes. When a user clicks a button called Next in the child component, the parent component must be alerted so it can navigate to the next page. How should this be accomplished?
- [x] **A.** Create a custom event.  [CORRECT]
- [ ] **B.** Call a method in the Apex controller.  [WRONG]
- [ ] **C.** Update a property on the parent.  [WRONG]
- [ ] **D.** Fire a notification.  [WRONG]

**Explanation:**
> Custom events are used to communicate between Lightning web components, and can be used to pass data from a parent component to a child component. The parent component can fire a custom event and include the data as a parameter, which the child component can then access.

**Resources:**
> Communicate Between Lightning Web Components

---

### Question 52
How can a developer get all of the available record types for the current user on the Case object?
- [x] **A.** Use DescribeSObjectResult of the Case object.  [CORRECT]
- [ ] **B.** Use SOQL to get all Cases.  [WRONG]
- [ ] **C.** Use DescribeFieldResult of the Case.RecordType field.  [WRONG]
- [ ] **D.** Use Case.getRecordTypes().  [WRONG]

**Explanation:**
> Here's the example code:
> Schema.DescribeSObjectResult rt = case.SObjectType.getDescribe();
> List<Schema.RecordTypeInfo> rti = R.getRecordTypeInfos();

**Resources:**
> DescribeSObjectResult Class

---

### Question 53
What are three characteristics of static methods? (Choose three.)
- [x] **A.** Initialized only when a class is loaded  [CORRECT]
- [ ] **B.** A static variable outside of the scope of an Apex transaction  [WRONG]
- [x] **C.** Allowed only in outer classes  [CORRECT]
- [ ] **D.** Allowed only in inner classes  [WRONG]
- [x] **E.** Excluded from the view state for a Visualforce page  [CORRECT]

**Explanation:**
> Static methods, variables, and initialization code have these characteristics.
> They’re associated with a class.
> They’re allowed only in outer classes.
> They’re initialized only when a class is loaded.
> They aren’t transmitted as part of the view state for a Visualforce page.

**Resources:**
> Static and Instance Methods, Variables, and Initialization Code