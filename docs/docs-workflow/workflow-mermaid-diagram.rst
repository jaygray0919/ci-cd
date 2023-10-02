
Mermaid code for workflow
-------------------------

.. code-block:: mermaid

   %%{
    init: {
      'logLevel': 'debug',
      'theme': 'base',
      'gitGraph': {
        'showBranches': true,
        'showCommitLabel':false,
        'mainBranchName': 'master'
      }
    }
   }%%
    
   gitGraph
    #Development
    commit
    branch develop
    commit
    branch featureA
    branch featureB
    
    checkout featureA
    commit
    checkout featureB
    commit
    checkout featureA
    commit
    checkout develop
    merge featureA tag: "dev-1.1"
    
    commit
    checkout develop
    branch featureC
    commit
    
    checkout featureB
    commit
    commit
    
    checkout develop
    commit
    checkout featureB
    merge develop
    
    checkout develop
    merge featureB tag: "dev-1.2"
    
    checkout featureC
    commit
    commit
    
    checkout develop
    commit
    checkout featureC
    merge develop
    
    checkout develop
    merge featureC tag: "dev-1.3"
    
    checkout develop
    commit tag: "RC-1.0"
    
    #Staging
    checkout develop
    branch staging
    commit tag: "QA-1.0"
    
    branch bugfixA
    commit
    commit
    
    checkout staging
    branch bugfixB
    commit
    
    checkout bugfixA
    commit
    checkout staging
    merge bugfixA tag: "QA-1.1"
    
    checkout bugfixB
    commit
    commit
    
    checkout staging
    commit
    checkout bugfixB
    merge staging
    
    checkout staging
    merge bugfixB tag: "QA-1.2"
    #commit tag: "QA-1.2-final"
    
    checkout develop
    merge staging tag: "RC-1.0-final"
    commit
    
    checkout master
    merge staging tag: "1.0"
    commit
   