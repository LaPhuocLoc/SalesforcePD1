# Salesforce Certified Platform Developer I — Practice Exam (SET 0)
**EXAM:** Salesforce Certified Platform Developer  
**GRADE:** Pass  

---

## Question 1 of 60
**Choose 1 option.**

A developer is alerted to an issue with a custom Apex trigger that is causing records to be duplicated.

What is the most appropriate debugging approach to troubleshoot the issue?

- A. Disable the trigger in production and test to see if the issue still occurs.
- B. Add system.debug statements to the code to track the execution flow and identify the issue.
- C. Review the Historical Event logs to identify the source of the issue.
- **D. ✅ Use the Apex Interactive Debugger to step through the code and identify the issue.**

---

## Question 2 of 60
**Choose 1 option.**

While writing an Apex class, a developer wants to make sure that all functionality being developed is handled as specified by the requirements.

Which approach should the developer use to be sure that the Apex class is working according to specifications?

- A. Create a test class to execute the business logic and run the test in the Developer Console.
- B. Run the code in an Execute Anonymous block in the Developer Console.
- C. Include a savepoint and `Database.rollback()`.
- **D. ✅ Include a try/catch block to the Apex class.**

---

## Question 3 of 60
**Choose 2 options.**

A developer has identified a method in an Apex class that performs resource intensive actions in memory by iterating over the result set of a SOQL statement on the account. The method also performs a DML statement to save the changes to the database.

Which two techniques should the developer implement as a best practice to ensure transaction control and avoid exceeding governor limits?

- **A. ✅ Use the `Database.Savepoint` method to enforce database integrity.**
- **B. ✅ Use the `System.Limit` class to monitor the current CPU governor limit consumption.**
- C. Use the `@ReadOnly` annotation to bypass the number of rows returned by a SOQL.
- D. Use partial DML statements to ensure only valid data is committed.

---

## Question 4 of 60
**Choose 1 option.**

A developer wants to get access to the standard price book in the org while writing a test class that covers an OpportunityLineItem trigger.

Which method allows access to the price book?

- **A. ✅ Use `Test.getStandardPricebookId()` to get the standard price book ID.**
- B. Use `@TestVisible` to allow the test method to see the standard price book.
- C. Use `Test.loadData()` and a static resource to load a standard price book.
- D. Use `@IsTest(SeeAllData=true)` and delete the existing standard price book.

---

## Question 5 of 60
**Choose 2 options.**

Assuming that `name` is a String obtained by an `<apex:inputText>` tag on a Visualforce page, which two SOQL queries performed are safe from SOQL injection?

- **A. ✅**
  ```apex
  String query = '%' + name + '%';
  List<Account> results = [SELECT Id FROM Account WHERE Name LIKE :query];
  ```
- B.
  ```apex
  String query = 'SELECT Id FROM Account WHERE Name LIKE \'%' + name + '%\'';
  List<Account> results = Database.query(query);
  ```
- C.
  ```apex
  String query = 'SELECT Id FROM Account WHERE Name LIKE \'%' + name.noQuotes() + '%\'';
  List<Account> results = Database.query(query);
  ```
- **D. ✅**
  ```apex
  String query = 'SELECT Id FROM Account WHERE Name LIKE \'%' +
      String.escapeSingleQuotes(name) + '%\'';
  List<Account> results = Database.query(query);
  ```

---

## Question 6 of 60
**Choose 2 options.**

A developer created a Lightning web component called `statusComponent` to be inserted into the Account record page.

Which two things should the developer do to make this component available?

- A. Add `<target>lightning__RecordPage</target>` to the `statusComponent.js` file.
- **B. ✅ Add `<target>lightning__RecordPage</target>` to the `statusComponent.js-meta.xml` file.**
- **C. ✅ Set `isExposed` to true in the `statusComponent.js-meta.xml` file.**
- D. Add `<masterLabel>Account</masterLabel>` to the `statusComponent.js-meta.xml` file.

---

## Question 7 of 60
**Choose 1 option.**

Given the following Anonymous block:

```apex
List<Case> casesToUpdate = new List<Case>();
for(Case thisCase : [SELECT Id, Status FROM Case LIMIT 50000]){
    thisCase.Status = 'Working';
    casesToUpdate.add(thisCase);
}
try{
    Database.update(casesToUpdate,false);
}catch(Exception e){
    System.debug(e.getMessage());
}
```

What should a developer consider for an environment that has over 10,000 Case records?

- A. The try-catch block will handle exceptions thrown by governor limits.
- B. The try-catch block will handle any DML exceptions thrown.
- C. The transaction will succeed and changes will be committed.
- **D. ✅ The transaction will fail due to exceeding the governor limit.**

---

## Question 8 of 60
**Choose 1 option.**

An Apex method, `getAccounts`, that returns a list of Accounts given a `searchTerm`, is available for Lightning Web Components to use.

What is the correct definition of a Lightning Web Component property that uses the `getAccounts` method?

- A. `@wire(getAccounts, '$searchTerm') accountList;`
- **B. ✅ `@wire(getAccounts, { searchTerm: '$searchTerm' }) accountList;`**
- C. `@AuraEnabled(getAccounts, { searchTerm: '$searchTerm' }) accountList;`
- D. `@AuraEnabled(getAccounts, '$searchTerm') accountList;`

---

## Question 9 of 60
**Choose 1 option.**

When a user edits the Postal Code on an Account, a custom Account text field named "Timezone" must be updated based on the values in another custom object called `PostalCodeToTimezone__c`.

What is the optimal way to implement this feature?

- A. Build an account assignment rule.
- B. Create a formula field.
- **C. ✅ Build a flow with Flow Builder.**
- D. Create an account approval process.

---

## Question 10 of 60
**Choose 2 options.**

As part of new feature development, a developer is asked to build a responsive application capable of responding to touch events, that will be executed on stateful clients.

Which two technologies are built on a framework that fully supports the business requirement?

- A. Visualforce Pages
- **B. ✅ Lightning Web Components**
- C. Visualforce Components
- **D. ✅ Aura Components**

---

## Question 11 of 60
**Choose 1 option.**

A software company is using Salesforce to track the companies they sell their software to in the Account object. They also use Salesforce to track bugs in their software with a custom object, `Bug__c`.

As part of a process improvement initiative, they want to be able to report on which companies have reported which bugs. Each company should be able to report multiple bugs and bugs can also be reported by multiple companies.

What is needed to allow this reporting?

- A. Master-detail field on `Bug__c` to Account
- **B. ✅ Junction object between `Bug__c` and Account**
- C. Roll-up summary field of `Bug__c` on Account
- D. Lookup field on `Bug__c` to Account

---

## Question 12 of 60
**Choose 2 options.**

What are two ways a developer can get the status of an enqueued job for a class that implements the queueable interface?

- **A. ✅ View the Apex Jobs page**
- B. View the Apex Status page
- **C. ✅ View the Apex Flex Queue**
- D. Query the `AsyncApexJob` object

---

## Question 13 of 60
**Choose 1 option.**

A developer is creating a page that allows users to create multiple Opportunities. The developer is asked to verify the current user's default Opportunity record type, and set certain default values based on the record type before inserting the record.

How can the developer find the current user's default record type?

- A. Query the Profile where the ID equals `userInfo.getProfileID()` and then use the `profile.Opportunity.getDefaultRecordType()` method.
- B. Create the opportunity and check the `opportunity.recordType`, which will have the record ID of the current user's default record type, before inserting.
- **C. ✅ Use `Opportunity.SObjectType.getDescribe().getRecordTypeInfos()` to get a list of record types, and iterate through them until `isDefaultRecordTypeMapping()` is true.**
- D. Use the `Schema.userInfo.Opportunity.getDefaultRecordType()` method.

---

## Question 14 of 60
**Choose 1 option.**

Which Lightning Web Component custom event property settings enable the event to bubble up the containment hierarchy and cross the Shadow DOM boundary?

- A. bubbles: false, composed: true
- B. bubbles: false, composed: false
- **C. ✅ bubbles: true, composed: true**
- D. bubbles: true, composed: false

---

## Question 15 of 60
**Choose 1 option.**

A developer is asked to prevent anyone other than a user with Sales Manager profile from changing the Opportunity Status to Closed Lost if the lost reason is blank.

Which automation allows the developer to satisfy this requirement in the most efficient manner?

- A. A record trigger flow on the Opportunity object
- B. An approval process on the Opportunity object
- C. An Apex trigger on the Opportunity object
- **D. ✅ An error condition formula on a validation rule on Opportunity**

---

## Question 16 of 60
**Choose 1 option.**

The values 'High', 'Medium', and 'Low' are identified as common values for multiple picklists across different objects.

What is an approach a developer can take to streamline maintenance of the picklists and their values, while also restricting the values to the ones mentioned above?

- A. Create the Picklist on each object as a required field and select "Display values alphabetically, not in the order entered".
- B. Create the Picklist on each object and add a validation rule to ensure data integrity.
- C. Create the Picklist on each object and select "Restrict picklist to the values defined in the value set".
- **D. ✅ Create the Picklist on each object and use a Global Picklist Value Set containing the values.**

---

## Question 17 of 60
**Choose 1 option.**

A software company uses the following objects and relationships:
- **Case**: to handle customer support issues
- **Defect__c**: a custom object to represent known issues with the company's software
- **Case_Defect__c**: a junction object between Case and Defect__c to represent that a defect is a cause of a customer issue

Case and `Defect__c` have Private organization-wide defaults.

What should be done to share a specific `Case_Defect__c` record with a user?

- A. Share the `Case_Defect__c` record.
- **B. ✅ Share the parent Case and `Defect__c` records.**
- C. Share the parent Case record.
- D. Share the parent `Defect__c` record.

---

## Question 18 of 60
**Choose 1 option.**

A developer has the following requirements:
- Calculate the total amount on an Order.
- Calculate the line amount for each Line Item based on quantity selected and price.
- Move Line Items to a different Order if a Line Item is not in stock.

Which relationship implementation supports these requirements on its own?

- **A. ✅ Line Item has a re-parentable master-detail field to Order.**
- B. Line Item has a re-parentable lookup field to Order.
- C. Order has a re-parentable master-detail field to Line Item.
- D. Order has a re-parentable lookup field to Line Item.

---

## Question 19 of 60
**Choose 1 option.**

Considering the following code snippet:

```apex
public static void insertAccounts(List<Account> theseAccounts){
    for(Account thisAccount : theseAccounts){
        if(thisAccount.website == null){
            thisAccount.website = 'https://www.demo.com';
        }
    }
    update theseAccounts;
}
```

When the code executes, a DML exception is thrown.

How should a developer modify the code to ensure exceptions are handled gracefully?

- A. Implement the `upsert` DML statement.
- B. Remove null items from the list of Accounts.
- **C. ✅ Implement a try/catch block for the DML.**
- D. Implement Change Data Capture.

---

## Question 20 of 60
**Choose 2 options.**

Which two statements are true about using the `@testSetup` annotation in an Apex test class?

- **A. ✅ The @testSetup annotation is not supported when the @isTest(SeeAllData=True) annotation is used.**
- **B. ✅ A method defined with the @testSetup annotation executes once for each test method in the test class and counts towards system limits.**
- C. Records created in the test setup method cannot be updated in individual test methods.
- D. In a test setup method, test data is inserted once and made available for all test methods in the test class.

---

## Question 21 of 60
**Choose 1 option.**

Flow Builder uses an Apex action to provide additional information about multiple Contacts, stored in a custom class, `ContactInfo`.

Which is the correct definition of the Apex method that gets the additional information?

- A.
  ```apex
  @InvocableMethod(label='Additional Info')
  public List<ContactInfo> getInfo(List<Id> contactIds)
  { /*implementation*/ }
  ```
- B.
  ```apex
  @InvocableMethod(label='Additional Info')
  public static ContactInfo getInfo(Id contactId)
  { /*implementation*/ }
  ```
- C.
  ```apex
  @InvocableMethod(label='Additional Info')
  public ContactInfo getInfo(Id contactId)
  { /*implementation*/ }
  ```
- **D. ✅**
  ```apex
  @InvocableMethod(label='Additional Info')
  public static List<ContactInfo> getInfo(List<Id> contactIds)
  { /*implementation*/ }
  ```

---

## Question 22 of 60
**Choose 1 option.**

Universal Containers has a large number of custom applications that were built using a third-party JavaScript framework and exposed using Visualforce pages. The company wants to update these applications to apply styling that resembles the look and feel of Lightning Experience.

What should the developer do to fulfill the business request in the quickest and most effective manner?

- A. Rewrite all Visualforce pages as Lightning components.
- B. Set the attribute `enableLightning` to true in the definition.
- **C. ✅ Incorporate the Salesforce Lightning Design System CSS stylesheet into the JavaScript applications.**
- D. Enable Available for Lightning Experience, Lightning Communities, and the mobile app on Visualforce pages used by the custom application.

---

## Question 23 of 60
**Choose 1 option.**

The following code snippet is executed by a Lightning web component in an environment with more than 2,000 lead records:

```apex
@AuraEnabled
public void static updateLeads(){
    for(Lead thisLead : [SELECT Origin__c FROM Lead]){
        thisLead.LeadSource = thisLead.Origin__c;
        update thisLead;
    }
}
```

Which governor limit will likely be exceeded within the Apex transaction?

- A. Total number of DML statements issued
- B. Total number of SOQL queries issued
- **C. ✅ Total number of records retrieved by SOQL queries**
- D. Total number of records processed as a result of DML statements

---

## Question 24 of 60
**Choose 1 option.**

What should a developer do to check the code coverage of a class after running all tests?

- A. View the Class Test Percentage tab on the Apex Class list view in Salesforce Setup.
- **B. ✅ View the Code Coverage column in the list view on the Apex Classes page.**
- C. View the code coverage percentage for the class using the Overall Code Coverage panel in the Developer Console Tests tab.
- D. Select and run the class on the Apex Test Execution page in the Developer Console.

---

## Question 25 of 60
**Choose 1 option.**

A developer must troubleshoot to pinpoint the causes of performance issues when a custom page loads in their org.

Which tool should the developer use to troubleshoot query performance?

- A. Visual Studio Code IDE
- B. AppExchange
- **C. ✅ Developer Console**
- D. Setup Menu

---

## Question 26 of 60
**Choose 1 option.**

Consider the following code snippet:

```apex
public static List<Lead> obtainAllFields(Set<Id> leadIds){
    List<Lead> result = new List<Lead>();
    for(Id leadId : leadIds){
        result.add([SELECT FIELDS(STANDARD) FROM Lead WHERE Id = :leadId]);
    }
    return result;
}
```

Given the multi-tenant architecture of the Salesforce platform, what is a best practice a developer should implement and ensure successful execution of the method?

- A. Avoid returning an empty List of records.
- B. Avoid using variables as query filters.
- **C. ✅ Avoid performing queries inside for loops.**
- D. Avoid executing queries without a limit clause.

---

## Question 27 of 60
**Choose 1 option.**

A developer needs to prevent the creation of `Request__c` records when certain conditions exist in the system. A `RequestLogic` class exists that checks the conditions.

What is the correct implementation?

- A.
  ```apex
  trigger RequestTrigger on Request__c (before insert) {
      if (RequestLogic.isValid(Request__c))
          Request.addError('Your request cannot be created at this time.');
  }
  ```
- B.
  ```apex
  trigger RequestTrigger on Request__c (after insert) {
      if (RequestLogic.isValid(Request__c))
          Request.addError('Your request cannot be created at this time.');
  }
  ```
- **C. ✅**
  ```apex
  trigger RequestTrigger on Request__c (before insert) {
      RequestLogic.validateRecords(trigger.new);
  }
  ```
- D.
  ```apex
  trigger RequestTrigger on Request__c (after insert) {
      RequestLogic.validateRecords(trigger.new);
  }
  ```

---

## Question 28 of 60
**Choose 2 options.**

Which two characteristics are true for Lightning Web Component custom events?

- **A. ✅ By default a custom event only propagates to its immediate container and to its immediate child component.**
- **B. ✅ By default a custom event only propagates to its immediate container.**
- C. Data may be passed in the payload of a custom event using @wire decorated properties.
- D. Data may be passed in the payload of a custom event using a property called detail.

---

## Question 29 of 60
**Choose 1 option.**

Which annotation should a developer use on an Apex method to make it available to be wired to a property in a Lightning web component?

- A. `@RemoteAction(cacheable=true)`
- B. `@AuraEnabled`
- **C. ✅ `@AuraEnabled(cacheable=true)`**
- D. `@RemoteAction`

---

## Question 30 of 60
**Choose 1 option.**

What is an example of a polymorphic lookup field in Salesforce?

- A. The ParentId field on the standard Account object
- **B. ✅ The WhatId field on the standard Event object**
- C. The LeadId and ContactId fields on the standard Campaign Member object
- D. A custom field, `Link__c`, on the standard Contact object that looks up to an Account or a Campaign

---

## Question 31 of 60
**Choose 2 options.**

Universal Containers recently transitioned from Classic to Lightning Experience.

One of its business processes requires certain values from the Opportunity object to be sent via an HTTP REST callout to its external order management system when the user presses a custom button on the Opportunity detail page. Example values are: Name, Amount, Account.

Which two methods should the developer implement to fulfill the business requirement?

- A. Create a Remote Action on the Opportunity object that executes an Apex immediate action to perform the HTTP REST callout whenever the Opportunity is updated.
- **B. ✅ Create a custom Visualforce quick action that performs the HTTP REST callout, and use a Visualforce quick action to expose the component on the Opportunity detail page.**
- **C. ✅ Create a Lightning component quick action that performs the HTTP REST callout, and use a Lightning Action to expose the component on the Opportunity detail page.**
- D. Create an after update trigger on the Opportunity object that calls a helper method using `@Future(Callout=true)` to perform the HTTP REST callout.

---

## Question 32 of 60
**Choose 1 option.**

How can a developer check the test coverage of autolaunched Flows before deploying them in a change set?

- A. Use the Flow Properties page.
- **B. ✅ Use SOQL and the Tooling API.**
- C. Use the `ApexTestResult` class.
- D. Use the Code Coverage Setup page.

---

## Question 33 of 60
**Choose 1 option.**

A developer wants to mark each Account in a `List<Account>` as either Active or Inactive, based on the value in the `LastModifiedDate` field of each Account being greater than 90 days in the past.

Which Apex technique should the developer use?

- A. A `for` loop, with a `switch` statement inside
- B. A `switch` statement, with a `for` loop inside
- C. An if-else statement, with a `for` loop inside
- **D. ✅ A `for` loop, with an if or if/else statement inside**

---

## Question 34 of 60
**Choose 3 options.**

Which three steps allow a custom Scalable Vector Graphic (SVG) to be included in a Lightning web component?

- **A. ✅ Import the static resource and provide a JavaScript property for it.**
- **B. ✅ Reference the property in the HTML template.**
- **C. ✅ Upload the SVG as a static resource.**
- D. Reference the import in the HTML template.
- E. Import the SVG as a content asset file.

---

## Question 35 of 60
**Choose 1 option.**

A developer creates a batch Apex job to update a large number of records, and receives reports of the job timing out and not completing.

What is the first step towards troubleshooting the issue?

- A. Check the debug logs for the batch job.
- B. Decrease the batch size to reduce the load on the system.
- **C. ✅ Check the asynchronous job monitoring page to view the job status and logs.**
- D. Disable the batch job and recreate it with a smaller number of records.

---

## Question 36 of 60
**Choose 1 option.**

A credit card company needs to implement the functionality for a service agent to process damaged or stolen credit cards. When the customers call in, the service agent must gather many pieces of information. A developer is tasked to implement this functionality.

What should the developer use to satisfy this requirement in the most efficient manner?

- A. Apex trigger
- **B. ✅ Lightning Component**
- C. Approval process
- D. Screen-based flow

---

## Question 37 of 60
**Choose 1 option.**

A company decides to implement a new process where every time an Opportunity is created, a follow up Task should be created and assigned to the Opportunity Owner.

What is the most efficient way for a developer to implement this?

- **A. ✅ Record-triggered flow on Opportunity**
- B. Apex trigger on Task
- C. Task actions
- D. Auto-launched flow on Task

---

## Question 38 of 60
**Choose 2 options.**

A developer is tasked to perform a security review of the `ContactSearch` Apex class that exists in the system. Within the class, the developer identifies the following method as a security threat:

```apex
List<Contact> performSearch(String lastName){
    return Database.query('SELECT Id, FirstName, LastName FROM Contact WHERE LastName Like
    %'+lastName+'%');
}
```

What are two ways the developer can update the method to prevent a SOQL injection attack?

- **A. ✅ Use variable binding and replace the dynamic query with a static SOQL.**
- **B. ✅ Use the `escapeSingleQuotes` method to sanitize the parameter before its use.**
- C. Use the `@ReadOnly` annotation and the `with sharing` keyword on the class.
- D. Use a regular expression on the parameter to remove special characters.

---

## Question 39 of 60
**Choose 1 option.**

A developer wants to improve runtime performance of Apex calls by caching results on the client.

What is the most efficient way to implement this and follow best practices?

- A. Set a cookie in the browser for use upon return to the page.
- **B. ✅ Decorate the server-side method with `@AuraEnabled(cacheable=true)`.**
- C. Decorate the server-side method with `@AuraEnabled(storable=true)`.
- D. Call the `setStorable()` method on the action in the JavaScript client-side code.

---

## Question 40 of 60
**Choose 1 option.**

In the following example, which sharing context will `myMethod` execute when it is invoked?

```apex
public Class myClass {
    public void myMethod() { /* implementation */ }
}
```

- A. Sharing rules will be enforced by the instantiating class.
- B. Sharing rules will not be enforced for the running user.
- C. Sharing rules will be enforced for the running user.
- **D. ✅ Sharing rules will be inherited from the calling context.**

---

## Question 41 of 60
**Choose 2 options.**

A developer creates a Lightning web component that imports a method within an Apex class. When a Validate button is pressed, the method runs to execute complex validations.

In this implementation scenario, which two options are part of the Controller according to the MVC architecture?

- **A. ✅ Apex class**
- B. HTML file
- **C. ✅ JavaScript file**
- D. XML file

---

## Question 42 of 60
**Choose 2 options.**

A development team wants to use a deployment script to automatically deploy to a sandbox during their development cycles.

Which two tools can they use to run a script that deploys to a sandbox?

- **A. ✅ SFDX CLI**
- B. Change Sets
- **C. ✅ VSCode**
- D. Developer Console

---

## Question 43 of 60
**Choose 2 options.**

Which two Agentforce limitations should a developer consider when building an agent?

- **A. ✅ Custom actions that reference an Apex class or flow support only primitive data types.**
- **B. ✅ The Agent API has a 90-second timeout.**
- C. Inbound messages sent via messaging channels have character limits.
- D. Version control is supported for agents.

---

## Question 44 of 60
**Choose 1 option.**

A developer must create a `DrawList` class that provides capabilities defined in the `Sortable` and `Drawable` interfaces.

```apex
public interface Sortable {
    void sort();
}
public interface Drawable {
    void draw();
}
```

Which is the correct implementation?

- A.
  ```apex
  public class DrawList implements Sortable, implements Drawable {
      public void sort() { /*implementation*/}
      public void draw() { /*implementation*/}
  }
  ```
- B.
  ```apex
  public class DrawList extends Sortable, Drawable {
      public void sort() { /*implementation*/}
      public void draw() { /*implementation*/}
  }
  ```
- **C. ✅**
  ```apex
  public class DrawList implements Sortable, Drawable {
      public void sort() { /*implementation*/}
      public void draw() { /*implementation*/}
  }
  ```

---

## Question 45 of 60
**Choose 1 option.**

A Salesforce administrator used Flow Builder to create a flow named "accountOnboarding". The flow must be used inside an Aura component.

Which tag should a developer use to display the flow in the component?

- A. `lightning-flow`
- B. `aura-flow`
- **C. ✅ `lightning:flow`**
- D. `aura:flow`

---

## Question 46 of 60
**Choose 1 option.**

Which statement describes the execution order when triggers are associated to the same object and event?

- **A. ✅ Trigger execution order cannot be guaranteed.**
- B. Triggers are executed in the order they are modified.
- C. Triggers are executed alphabetically by trigger name.
- D. Triggers are executed in the order they are created.

---

## Question 47 of 60
**Choose 1 option.**

A Lightning component has a wired property, `searchResults`, that stores a list of Opportunities.

Which definition of the Apex method, to which the `searchResults` property is wired, should be used?

- A.
  ```apex
  @AuraEnabled(cacheable=false)
  public List<Opportunity> search(String term) { /*implementation*/ }
  ```
- **B. ✅**
  ```apex
  @AuraEnabled(cacheable=true)
  public static List<Opportunity> search(String term) { /*implementation*/ }
  ```
- C.
  ```apex
  @AuraEnabled(cacheable=false)
  public static List<Opportunity> search(String term) { /*implementation*/ }
  ```
- D.
  ```apex
  @AuraEnabled(cacheable=true)
  public List<Opportunity> search(String term) { /*implementation*/ }
  ```

---

## Question 48 of 60
**Choose 1 option.**

Developers at Universal Containers (UC) use version control to share their code changes, but they notice that when they deploy their code to different environments they often have failures. They decide to set up Continuous Integration (CI).

What should the UC development team use to automatically run tests as part of their CI process?

- A. Visual Studio Code
- **B. ✅ Salesforce CLI**
- C. Developer Console
- D. Force.com Toolkit

---

## Question 49 of 60
**Choose 1 option.**

A custom object `Trainer__c` has a lookup field to another custom object `Gym__c`.

Which SOQL query will get the record for the Viridian City Gym and all its trainers?

- A. `SELECT ID FROM Trainer__c WHERE Gym__r.Name = 'Viridian City Gym'`
- **B. ✅ `SELECT Id, (SELECT Id FROM Trainers__r) FROM Gym__c WHERE Name = 'Viridian City Gym'`**
- C. `SELECT Id, (SELECT Id FROM Trainer__c) FROM Gym__c WHERE Name = 'Viridian City Gym'`
- D. `SELECT Id, (SELECT Id FROM Trainers__c) FROM Gym__c WHERE Name = 'Viridian City Gym'`

---

## Question 50 of 60
**Choose 1 option.**

What should a developer use to fix a Lightning web component bug in a sandbox?

- **A. ✅ VS Code**
- B. Execute Anonymous
- C. Developer Console
- D. Force.com IDE

---

## Question 51 of 60
**Choose 2 options.**

A developer creates a custom exception as shown below:

```apex
public class ParityException extends Exception {}
```

What are two ways the developer can fire the exception in Apex?

- **A. ✅ `throw new ParityException('parity does not match');`**
- **B. ✅ `throw new ParityException();`**
- C. `new ParityException('parity does not match');`
- D. `new ParityException();`

---

## Question 52 of 60
**Choose 2 options.**

What are two characteristics related to formulas?

- A. Formulas can reference themselves.
- **B. ✅ Formulas can reference values in related objects.**
- C. Fields that are used in a formula field can be deleted or edited without editing the formula.
- **D. ✅ Formulas are calculated at runtime and are not stored in the database.**

---

## Question 53 of 60
**Choose 1 option.**

The sales management team at Universal Containers requires that the Lead Source field of the Lead record be populated when a Lead is converted.

What should be done to ensure that a user populates the Lead Source field prior to converting a Lead?

- A. Create an after trigger on Lead.
- B. Use a formula field.
- C. Use Lead Conversion field mapping.
- **D. ✅ Use a validation rule.**

---

## Question 54 of 60
**Choose 1 option.**

Cloud Kicks Fitness, an ISV Salesforce partner, is developing a managed package application. One of the application modules allows the user to calculate body fat using the Apex class, `BodyFat`, and its method, `calculateBodyFat()`. The product owner wants to ensure this method is accessible by the consumer of the application when developing customizations outside the ISV's package namespace.

Which approach should a developer take to ensure `calculateBodyFat()` is accessible outside the package namespace?

- A. Declare the class and method using the public access modifier.
- B. Declare the class as public and use the global access modifier on the method.
- C. Declare the class as global and use the public access modifier on the method.
- **D. ✅ Declare the class and method using the global access modifier.**

---

## Question 55 of 60
**Choose 1 option.**

Given the following Apex statement:

```apex
Account myAccount = [SELECT Id, Name FROM Account];
```

What occurs when more than one Account is returned by the SOQL query?

- A. The variable, `myAccount`, is automatically cast to the List data type.
- B. The first Account returned is assigned to `myAccount`.
- C. The query fails and an error is written to the debug log.
- **D. ✅ An unhandled exception is thrown and the code terminates.**

---

## Question 56 of 60
**Choose 1 option.**

While developing an Apex class with custom search functionality that will be launched from a Lightning Web Component, how can the developer ensure only records accessible to the currently logged in user are displayed?

- **A. ✅ Use the `with sharing` keyword.**
- B. Use the `inherited sharing` keyword.
- C. Use the `without sharing` keyword.
- D. Use the `WITH SECURITY_ENFORCED` clause within the SOQL.

---

## Question 57 of 60
**Choose 2 options.**

Which two actions may cause triggers to fire?

- **A. ✅ Updates to FeedItem**
- B. Renaming or replacing a picklist entry
- C. Cascading delete operations
- **D. ✅ Changing a user's default division when the transfer division option is checked**

---

## Question 58 of 60
**Choose 1 option.**

A developer is using Agentforce Dev Assistant and noticed that the output from their prompt resembles proprietary code.

Which model training considerations should the developer be aware of when utilizing the extension?

- A. Dev Assistant can reference the developer's prior prompts to generate output in near real time.
- B. Dev Assistant can reference other developers' code and train the model in near real time.
- **C. ✅ Dev Assistant generated output that resembles the code that was used to train the model.**
- D. Dev Assistant anonymized PII data in customer code that was used to train the model.

---

## Question 59 of 60
**Choose 2 options.**

Universal Containers decides to use purely declarative development to build out a new Salesforce application.

Which two options can be used to build out the business logic layer for this application?

- A. Remote Actions
- **B. ✅ Validation Rules**
- **C. ✅ Record-Triggered Flow**
- D. Batch Jobs

---

## Question 60 of 60
**Choose 1 option.**

A developer receives an error when compiling the following code.

```apex
switch on sobject {
    when Account a, Contact c {
        System.debug('account ' + a);
        System.debug('contact ' + c);
    }
    when null {
        System.debug('null');
    }
    when else {
        System.debug('default');
    }
}
```

What is the error?

- **A. ✅ Only one sObject type per when block can be used.**
- B. There is incompatible variable binding.
- C. Switch statements cannot contain multiple when values.

---

## Exam Result Summary

**EXAM:** Salesforce Certified Platform Developer  
**GRADE:** Pass

| Section Name                        |
|-------------------------------------|
| Developer Fundamentals              |
| Process Automation and Logic        |
| User Interface                      |
| Testing, Debugging, and Deployment  |
