This is the most critical part of the "Senior" curriculum. A Junior Engineer reads tutorials; a Senior Engineer **conducts experiments**.

Below is the complete list of 100 "Senior-Level" exercises. These are designed to be **destructive, investigative, or architectural**. You aren't just building pipelines; you are crashing them to see how they break.

---

### 🟢 Phase 1: The Metal (Days 1–20)

**Focus:** Breaking the OS and Database constraints.

| Day | Topic | Senior Exercise (The "Lab") |
| --- | --- | --- |
| **1** | Linux Kernel | **The Inode Explosion:** Write a script to create 1 million 0-byte files. Observe `df -i` vs `df -h`. Try to write a new file when Inodes are 100% full but disk is 90% empty. |
| **2** | Streams | **The 10GB Race:** Generate a 10GB CSV. Write a Python script to count rows (measure RAM). Write a bash pipeline (`awk |
| **3** | Oracle Arch | **The Memory Map:** Use `pmap -x` on a running DB process to identify which memory segment corresponds to the SGA (Shared) vs PGA (Private). |
| **4** | Storage Physics | **The Block Padding:** Create a table. Insert 100 rows. Check storage used. Now Update every row to expand a VARCHAR column. Measure the "Table Scan" I/O increase due to **Row Migration**. |
| **5** | ACID & WAL | **The Power Plug:** Write a script that writes to a file but *never* calls `fsync`. Kill the power (or VM). Reboot and verify data loss. Fix it by adding `fsync`. |
| **6** | Concurrency | ** The Deadlock Script:** Open two terminals. Manually start transactions in each that update the same two rows in opposite order. Trigger a classic ORA-00060 (Deadlock). |
| **7** | OLTP vs OLAP | **The Columnar Crush:** Store 1M rows in a Row Store (Postgres/Oracle). Store same in a Column Store (Parquet/ClickHouse). Run `SELECT AVG(col)`. Measure I/O throughput differences. |
| **8** | Indexing | **The Cardinality Trap:** Create a B-Tree index on a "Gender" column (Low Cardinality). Run a query. Prove via `EXPLAIN PLAN` that the DB ignores your index and does a Full Table Scan. |
| **9** | CAP Theorem | **The Split Brain:** Setup a 3-node DB cluster. Use `iptables` to block network traffic to the Leader. Observe if the system chooses Availability (accepts writes) or Consistency (rejects writes). |
| **10** | **Project 1** | **Build the LSM Engine:** Code a Python script that accepts writes to RAM, sorts them, and flushes to an SSTable on disk when RAM > 10MB. |
| **11** | Analytical SQL | **The Gaps & Islands:** Given a table of login dates, write a single SQL query to find the longest "Streak" of consecutive daily logins without using a loop/cursor. |
| **12** | Join Physics | **The Hash Spill:** Force a Hash Join on two massive datasets with small memory. Watch the "Temp/Disk" usage spike as the Hash Table spills to disk. |
| **13** | Aggregation | **The Cube:** Generate a report using `GROUP BY CUBE (Region, Product, Date)`. Calculate how many rows are generated compared to the source data. |
| **14** | Modeling | **The Kimball whiteboard:** Reverse engineer a receipt from a grocery store into a Star Schema (Fact_Sales, Dim_Product, Dim_Date, Dim_Store). |
| **15** | Schema Design | **The SCD Type 2:** Write a merge statement that handles a user changing their address, preserving history by expiring the old row and inserting a new one. |
| **16** | Views | **The Materialized Lag:** Create a Materialized View. Update the base table. Measure the "Staleness" window before the view refreshes. |
| **17** | JSON/XML | **The Parsing Cost:** Store JSON as a Blob vs. Shredded into columns. Run an aggregation. Benchmark the CPU cost of parsing JSON on-the-fly vs reading columns. |
| **18** | Optimization | **The Predicate Pushdown:** Write a query with a function on an indexed column (e.g., `WHERE YEAR(date_col) = 2023`). Show how this kills the index usage. Fix it. |
| **19** | Constraints | **The Bad Data Injection:** Disable constraints. Load dirty data. Re-enable constraints with `NOVALIDATE`. Explain why Big Data systems default to this. |
| **20** | **Project Review** | **The Benchmark:** Run your custom LSM DB (Day 10) against SQLite. Measure write throughput. |

---

### 🔵 Phase 2: Distributed Foundation (Days 21–40)

**Focus:** Understanding the network and "The Shuffle."

| Day | Topic | Senior Exercise (The "Lab") |
| --- | --- | --- |
| **21** | Big Data | **The Latency math:** Calculate the time to send 1TB over 1Gbps network vs Reading from HDD. Prove why "Data Locality" exists. |
| **22** | HDFS Arch | **The Metadata Fill:** Calculate how much RAM a NameNode needs for 100 Million files. Prove why HDFS fails with small files. |
| **23** | Replication | **The Block Hunt:** Upload a file to HDFS. Use `hdfs fsck` to find exactly which physical Linux servers store the blocks. Kill one server. Watch replication heal. |
| **24** | MapReduce Shuffle | **The Network Saturation:** Run a TeraSort. Monitor network bandwidth across the cluster. Identify the "Shuffle Phase" spike. |
| **25** | Skew | **The Straggler:** Create a dataset where "Key=A" has 90% of the data. Run a job. Watch one reducer run for hours while others finish in seconds. |
| **26** | YARN Arch | **The Container Kill:** Identify the ApplicationMaster container ID. Kill it manually. Watch YARN restart the whole job (or just the AM). |
| **27** | Schedulers | **The Queue War:** Submit a massive job to the "Default" queue. Submit a tiny job to the same queue. Watch the tiny job get stuck (FIFO). Switch to "Fair" and retry. |
| **28** | File Formats | **The Splittability Test:** Store data as GZIP CSV vs BZIP2 CSV. Run a MapReduce job. Show that GZIP uses only 1 Mapper (non-splittable) vs BZIP2 uses many. |
| **29** | Compression | **The CPU Trade-off:** Compress 1GB data with Snappy vs GZIP. Measure Compression Time vs Size reduction. |
| **30** | **Project 2** | **ProtoBuf Registry:** Define a `.proto` schema. Serialize data to binary. Write a reader that fails if the schema is incompatible. |
| **31** | Hive Arch | **The Metastore Hack:** Query the backend MySQL of Hive. Find the table definition directly in the `TBLS` and `SDS` tables. |
| **32** | Partitioning | **The Dynamic Partition Bomb:** Run a query that inserts dynamic partitions on a high-cardinality column (e.g., Timestamp). Watch it create 10k tiny files and crash the NameNode. |
| **33** | Optimization | **The CBO Check:** Run a Join without stats. Run `ANALYZE TABLE`. Run Join again. Compare the execution plans. |
| **34** | HBase Arch | **The MemStore Flush:** Write continuously to HBase. Watch the logs for "MemStore Flush." Correlate it with minor compactions. |
| **35** | HBase Design | **The Hotspot:** Create a table with sequential RowKeys. Insert fast. Watch only 1 RegionServer taking all the load. Salt the keys to fix it. |
| **36** | Kafka Arch | **The Topic Surgery:** Inspect the physical folder of a Kafka topic on disk. Identify the `.log` and `.index` files. |
| **37** | Kafka Internals | **The ISR Drop:** Kill a Kafka Broker. Watch the "In-Sync Replica" count drop. Produce with `acks=all` and see if it blocks. |
| **38** | Consumers | **The Lag Spike:** Stop your consumer. Produce 1M messages. Start consumer. Measure how long it takes to catch up. |
| **39** | Semantics | **The Duplication:** Produce a message. Crash the producer *after* send but *before* ack. Restart producer. Observe duplicate message in topic. |
| **40** | **Project Review** | **Schema Evolution:** Try to read old binary data with a new ProtoBuf schema (Day 30). Fix the backward compatibility. |

---

### 🟠 Phase 3: Spark Mastery (Days 41–60)

**Focus:** Memory management and bypassing the JVM.

| Day | Topic | Senior Exercise (The "Lab") |
| --- | --- | --- |
| **41** | Architecture | **The WordCount DAG:** Draw the exact DAG (Stages) for a `reduceByKey` vs `groupByKey` word count. |
| **42** | RDD Internals | **The Lineage Trace:** Use `toDebugString` on an RDD to see the lineage graph grows with every transformation. |
| **43** | Lazy Eval | **The No-Op:** Write a complex Spark job with 50 transformations but NO Action (e.g., no `count()`). Run it. Prove it takes 0 seconds. |
| **44** | Transformations | **The Stage Boundary:** Write code that triggers a Shuffle. Look at the Spark UI to verify a new "Stage" was created. |
| **45** | Shuffle & Sort | **The Spill Monitor:** Reduce Executor memory to 512MB. Run a large sort. Look for "Disk Spill" in Spark UI metrics. |
| **46** | Variables | **The Closure Bug:** Try to update a standard Python counter variable inside a `map()` function. Print it at the end (It will be 0). Fix with Accumulator. |
| **47** | Memory | **The Cache Crash:** `cache()` a dataframe larger than RAM. Observe the storage tab to see what % is cached vs dropped. |
| **48** | Caching | **The Persistence Format:** Compare `MEMORY_ONLY` vs `MEMORY_ONLY_SER` (Serialized). Measure RAM savings vs CPU cost. |
| **49** | Tuning | **The Core Sizing:** Run the same job with `--executor-cores 1` vs `--executor-cores 5`. Benchmark performance. |
| **50** | **Project 3** | **Time Machine:** Ingest "Late" data. Use Spark Streaming watermarks to drop it, then log it to a side-table. |
| **51** | Catalyst | **The Plan Inspector:** Run `df.explain(True)`. Identify the "Logical Plan" vs "Physical Plan". Find where filters were pushed down. |
| **52** | Tungsten | **The JVM Bypass:** Compare a UDF (Python) vs a Built-in Function (Scala/Tungsten). Measure the 10x speed difference. |
| **53** | Joins | **The BHJ Force:** Force a `BroadcastHashJoin` on a large table using hints. Watch it crash with OOM (Out Of Memory). |
| **54** | Skew | **The Salting Fix:** Take the skewed dataset from Day 25. Add a "Salt" key. Join again. Verify even distribution of tasks. |
| **55** | Streaming | **The Netcat Stream:** Open a generic socket (`nc -lk 9999`). Connect Spark Streaming to it. Type words and see counts in real-time. |
| **56** | Watermarking | **The Window Drop:** Send a timestamped event 1 hour old. Set watermark to 30 mins. Verify the event is dropped from the aggregation. |
| **57** | Delta Lake | **The Log Check:** Look inside the `_delta_log` folder. Read the JSON commit files to see how ACID is implemented on S3. |
| **58** | Delta Ops | **The Time Travel:** Update a Delta table. Select from the table `VERSION AS OF 0`. Verify you see the old data. |
| **59** | K8s | **The Pod Watch:** Submit Spark to K8s. Watch `kubectl get pods`. See executors spin up and die dynamically. |
| **60** | **Project Review** | **The Late Data Replay:** Take the side-output from Day 50 and trigger a batch job to merge it into history. |

---

### 🟣 Phase 4: Multi-Cloud (Days 61–80)

**Focus:** Cost, Architecture, and "The Wars".

| Day | Topic | Senior Exercise (The "Lab") |
| --- | --- | --- |
| **61** | Storage Wars | **The Consistency Check:** Write to S3. Immediately read it back from a different thread. (Verify S3's strong consistency vs Eventual consistency of older object stores). |
| **62** | Compute Wars | **The Spin-up Time:** Time how long it takes to get a usable Spark shell on EMR (AWS) vs Dataproc (GCP) vs Synapse (Azure). |
| **63** | Redshift | **The Vacuum:** Delete 50% of rows in Redshift. Check disk usage (It won't change). Run `VACUUM`. Check disk usage again. |
| **64** | BigQuery | **The Slot Exhaustion:** Run a massive query. Check the "Slot Usage". See if you hit the 2000 slot limit for on-demand pricing. |
| **65** | Snowflake | **The Micro-partition:** Run a query filtering on a non-clustered column. Note the "Partitions Scanned". Re-cluster. Run again. |
| **66** | Showdown | **The JSON Off:** Load complex JSON into BigQuery (Native) vs Snowflake (Variant). Run a nested query. Benchmark speed. |
| **67** | Serverless | **The Cold Start:** Trigger a Glue Job. Measure the time until it actually starts processing data. |
| **68** | Dataflow | **The Backpressure:** Intentionally slow down a Beam worker. Watch Dataflow autoscaling trigger to add more workers. |
| **69** | Networking | **The Egress Bill:** Calculate the cost of moving 1PB from AWS S3 to Google Cloud. (Realize why we don't move data). |
| **70** | **Project 4** | **Cloud Arbitrage:** Write a script that checks Spot Prices for AWS vs GCP and prints the cheapest region for a 100-node cluster. |
| **71** | Orchestration | **The Trigger:** Setup a Storage Event Trigger in ADF/AWS Pipeline. Drop a file to start the pipeline automatically. |
| **72** | Databricks | **The Mount:** Mount an S3 bucket to DBFS. Access it like a local file system. |
| **73** | Security | **The IAM Deny:** Create an IAM role that allows reading S3 but explicitly denies writing. Try to write. Verify. |
| **74** | Encryption | **The CMK Rotation:** Encrypt a bucket with a Customer Managed Key. Disable the key. Verify data is unreadable. |
| **75** | Migration | **The Data Type Mapping:** Map a Teradata `PERIOD` data type to the closest equivalent in Snowflake. |
| **76** | Hybrid | **The Latency Ping:** Ping from an AWS EC2 instance to your local machine (simulating on-prem). Compare to pinging another EC2. |
| **77** | Governance | **The PII Tag:** Manually tag a column as "PII" in a Data Catalog. Write a policy that hides it from "Analyst" role. |
| **78** | FinOps | **The Tagging Script:** Write a script to find all untagged EC2 instances and terminate them (Simulation). |
| **79** | Serverless Fn | **The S3 Hook:** Write a Lambda that triggers on S3 Put. It should parse the filename and insert metadata to DynamoDB. |
| **80** | **Project Review** | **The Spot Loss:** Simulate a Spot Instance revocation in your Arbitrage script (Day 70). Ensure it retries on On-Demand. |

---

### ⚫ Phase 5: Production (Days 81–100)

**Focus:** Reliability, Automation, and System Design.

| Day | Topic | Senior Exercise (The "Lab") |
| --- | --- | --- |
| **81** | Airflow Core | **The Cyclic DAG:** Create a DAG where Task A depends on Task B, and Task B depends on Task A. Watch the Scheduler panic. |
| **82** | Scheduling | **The Catchup Trap:** Deploy a DAG with `start_date` 1 year ago and `catchup=True`. Watch Airflow try to schedule 365 runs instantly. Kill it. |
| **83** | Operators | **The Custom Sensor:** Write a Python sensor that waits for a specific row to appear in a Postgres table before proceeding. |
| **84** | Docker | **The Volume Persist:** Run a container, write a file inside, kill container. Start new one. File is gone. Fix with `-v` (Volumes). |
| **85** | K8s Arch | **The Service Discovery:** Run two pods. Make Pod A ping Pod B by Service Name (DNS), not IP. |
| **86** | Helm | **The Rollback:** Deploy an app with Helm. Break it. Use `helm rollback` to restore the previous version instantly. |
| **87** | Terraform Basics | **The State Drift:** Create an S3 bucket with Terraform. Manually delete it in AWS Console. Run `terraform plan`. Watch it detect the drift. |
| **88** | Terraform Adv | **The Lock:** Try to run `terraform apply` from two terminals at the exact same time. Verify DynamoDB locking stops one. |
| **89** | CI/CD | **The Pipeline Block:** Write a GitHub Action that fails if Python code is not formatted (Black/Flake8). |
| **90** | **Project 5** | **Chaos Monkey:** Write a script that randomly kills a random Airflow worker process. Ensure tasks retry on a new worker. |
| **91** | FastAPI | **The Async Test:** Hammer your API with 1000 requests. Compare `def path` (Sync) vs `async def path` (Async) performance. |
| **92** | Data Quality | **The Circuit Breaker:** Implement a check: If `NULL` count in column > 5%, exit script with Error 1. |
| **93** | Observability | **The Lineage Graph:** Draw the lineage from Source -> Kafka -> Spark -> Snowflake -> Tableau. Identify the single point of failure. |
| **94** | System Design | **The Backfill Calc:** You have 5 years of data. Processing 1 day takes 1 hour. How many nodes do you need to backfill in 24 hours? |
| **95** | Data Mesh | **The Domain Boundary:** Define the "Interface" (Data Contract) between a "Sales Domain" and "Marketing Domain". |
| **96** | **Capstone Infra** | **The One-Click Deploy:** Run `terraform apply`. Watch Network, Cluster, and Storage spin up from zero. |
| **97** | **Capstone Ingest** | **The Jitter:** Feed data into Kafka with deliberate random delays. Verify your streaming job handles it. |
| **98** | **Capstone Process** | **The Poison Pill:** Send a malformed JSON event that causes the parser to crash. Implement a "Dead Letter Queue" to catch it without stopping the stream. |
| **99** | **Capstone Orch** | **The Dependency:** Ensure the "Daily Report" DAG waits for the "Ingestion" DAG to finish using an `ExternalTaskSensor`. |
| **100** | **Final Review** | **The Mock Interview:** Explain your 100-day architecture to a rubber duck (or friend) as if you are selling it for $1M. |