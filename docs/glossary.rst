
Glossary
========

.. glossary::
   :sorted:
   
   Grammar
      An ontology is a set of statements in the logical form: :class:`subject` :class:`predicate` :class:`object` where :class:`subject` and :class:`object` are facet terms.

   baseline 
       An approved revision of a file from which subsequent changes can be made. 

   branch 
       A set of files under version control may be branched (forked) at a point 
       in time. From that time forward, the two copies of the files may develop 
       in different ways, independently of each other.

   change 
       A change (or diff, or delta) represents a specific modification to a 
       file under version control.

   changeset
       A collection of files that have changes.

   checkout 
       See 'clone'.

   clone
       To clone is to create a local working copy from the repository. 
       A user may specify a revision or obtain the latest. 
       In centralised version control systems (with a single central repository),
       the term 'checkout' is also used.
       The term 'checkout' can be used as a noun to describe the working copy.

   commit 
       To commit is to write or merge the changes made in the working copy back 
       to the repository. The terms 'commit' and 'checkin' can also be used as 
       nouns to describe the revision that is created as a result of committing.

   conflict 
       A conflict occurs when different parties make changes to the same file, 
       and the system is unable to reconcile the changes. 
       
       A user must resolve the conflict by combining the changes, 
       or by selecting one change in favour of the other.

   fork
       See 'branch'.

   head
       The most recent revision, either to the trunk or to a branch.
       
       The trunk and each branch have their own head. 
       HEAD is sometimes used to refer to the head of the trunk.

   merge 
       A merge is an operation in which two sets of changes are applied 
       to a file or set of files under version control. 
       
       A user updates their working copy with changes made to the repository
       by other users.
       
       A user tries to update a repository with changes made to a working copy.

   repository 
       The repository is where the files' current and historical data are stored,
       often on a server.

   resolve 
       The act of user intervention to address a conflict between different 
       changes to the same file.

   revision 
       A revision (version) is any registered "snapshot" in time of the repository.

   sync
       See 'update'.

   trunk
       The trunk is the "main" line of development to the collection of 
       information under version control, consisting only of 'baseline' (approved) 
       files.

   update 
       An update (or sync) merges changes made in the original repository 
       (by other users, for example) into the local working copy.
     
   version
       See 'revision'.

   working copy
       A working copy is a local copy of files from a repository, made
       at a specific time (revision).
    
