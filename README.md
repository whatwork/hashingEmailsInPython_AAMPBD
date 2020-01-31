# Hashing Emails in Python

Super basic example of how to hash emails for ingestion into AAM for PBD.

The hash of the emails needs to occur before they are sent into AAM for syncing with the UUID. [What the AAM documentation omits](https://docs.adobe.com/content/help/en/audience-manager/user-guide/features/destinations/people-based/implementation-guide/people-based-destinations-workflow-combined.html) is _how_ to hash an email.

Incoming file – tab delimited, existing DPUUID and customer email address.

| DPUUID | Email |
| --- | --- |
|12341762 | xxx@adobe.com|
|81273891 | yyy@adobe.com|
|17298371 | johndoe@example.com |

```sh
python3 hashme.py
```

The result of running the data through that script will now be a file that contains the below -- the first column is the existing DPUUID, and the second is the hashed email.

| DPUUID | Hashed Email |
| --- | --- |
|12341762|c25d1997f56d087451c5d8b4b6d1f5c7332b78cf66f255ad16a460f346561470|
|81273891|d06afecaee96aac79de5c3ade35a1362df64f39cba88fad40e0b9c99efa6b47d|
|17298371|55e79200c1635b37ad31a378c39feb12f120f116625093a19bc32fff15041149|

This new file should then be named accordingly c2c_id_<DPUUID_DATA_SOURCE_ID>_<HASHED_EMAIL_DATA_SOURCE_ID>_TIMESTAMP.sync , [per the instructions here](https://docs.adobe.com/content/help/en/audience-manager/user-guide/implementation-integration-guides/sending-audience-data/batch-data-transfer-process/id-sync-file-based.html), and then uploaded to S3 to sync with AAM.
