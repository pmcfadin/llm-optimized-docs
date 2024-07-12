When you create apps using the Data API clients for Python, TypeScript,
and Java, your main entry point is the `DataAPIClient` object.

If you haven’t already, install the client for your preferred language.
See:

-   [Install the Python
    client](databases:python-client.xml#install-the-python-client)

-   [Install the TypeScript
    client](databases:typescript-client.xml#install-the-typescript-client)

-   [Install the Java
    client](databases:java-client.xml#install-the-java-client)

Then proceed with the instructions in this topic.

# Get a client

Instantiate a client object. The client only needs a token, as it is not
specific to a database.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/client.html#astrapy.client.DataAPIClient\[API
Reference\].

    client = DataAPIClient("TOKEN")

Returns:

`DataAPIClient` - An instance of the client class.

    DataAPIClient("AstraCS:aAbB...")

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>token</p></td>
<td style="text-align: left;"><p><code>str</code></p></td>
<td style="text-align: left;"><p>An Access Token to the database.
Example: <code>"AstraCS:aAbB…​"</code>.</p></td>
</tr>
</tbody>
</table>

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database0 = client.get_database("API_ENDPOINT")
    collection0 = database0.create_collection("movies", dimension=5)
    collection0.insert_one({
        "title": "The Title",
        "$vector": [0.1, 0.3, -0.7, 0.9, -0.1],
    })
    database_by_id = client.get_database("01234567-...")
    database_by_id_region = client.get_database("01234567-...", region="us-east1")
    admin = client.get_admin()
    admin1 = client.get_admin(token=more_powerful_token_override)
    database_iterator = admin.list_databases()

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/DataAPIClient.html\[API Reference\].

    const client = new DataAPIClient('TOKEN');

Returns:

`{ts-client-api-ref-url}/classes/DataAPIClient.html[DataAPIClient]` - An
instance of the client class.

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>token?</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>An access token for the database, e.g.
<code>'AstraCS:aAbB…​'</code>.</p>
<p>You can omit this and, instead, pass it with <code>client.db()</code>
or <code>client.admin()</code> through the <code>token</code>
parameter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/DataAPIClientOptions.html[DataAPIClientOptions]</code></p></td>
<td style="text-align: left;"><p>The options to use for the client,
including defaults.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/DataAPIClientOptions.html[DataAPIClientOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DataAPIClientOptions.html#environment[environment?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/DataAPIEnvironment.html[DataAPIEnvironment]</code></p></td>
<td style="text-align: left;"><p>Sets the Data API backend to use (for
example, <code>dse</code>, <code>hcd</code>, <code>astra</code>). The
default is <code>astra</code>.</p>
<p>Most operations are the same between backends. Authentication and
available administration operations can differ. For information, see the
<a
href="https://github.com/datastax/astra-db-ts?tab=readme-ov-file#non-astra-support">astra-db-ts
README</a>.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DataAPIClientOptions.html#httpOptions[httpOptions?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/DataAPIHttpOptions.html[DataAPIHttpOptions]</code></p></td>
<td style="text-align: left;"><p>Options related to the API requests the
client makes.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DataAPIClientOptions.html#dbOptions[dbOptions?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/DbSpawnOptions.html[DbSpawnOptions]</code></p></td>
<td style="text-align: left;"><p>Allows default options for when
spawning a Db instance.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DataAPIClientOptions.html#adminOptions[adminOptions?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/AdminSpawnOptions.html[AdminSpawnOptions]</code></p></td>
<td style="text-align: left;"><p>Allows default options for when
spawning some Admin instance.</p></td>
</tr>
</tbody>
</table>

Http options
(`{ts-client-api-ref-url}/types/DataAPIHttpOptions.html[DataAPIHttpOptions]`):

The
`{ts-client-api-ref-url}/types/DataAPIHttpOptions.html[DataAPIHttpOptions]`
type is a discriminated union on the `client` field. There are four
available behaviors for the `client` field:

-   **`httpOptions` not set**: Use `fetch-h2` if available or fall back
    to `fetch`.

-   **`client: 'default'` or unset**: Use `fetch-h2` if available or
    throw an error.

-   **`client: 'fetch'`**: Only use the native `fetch` API.

-   **`client: 'custom'`**: Pass a custom Fetcher implementation to the
    client.

`fetch-h2` is generally available by default on node runtimes only. On
other runtimes, you might need to use the native `fetch` API or, if your
code is minified, pass in the `fetch-h2` module manually.

For more information on http clients, see the [astra-db-ts
README](https://github.com/datastax/astra-db-ts?tab=readme-ov-file#non-standard-environment-support)
and the {ts-client-api-ref-url}/types/DataAPIHttpOptions.html\[API
reference\].

Monitoring/logging:

For information on setting up commands monitoring, see the [astra-db-ts
README](https://github.com/datastax/astra-db-ts?tab=readme-ov-file#monitoringlogging).

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    const client = new DataAPIClient('TOKEN');

    const db1 = client.db('ENDPOINT');
    const db2 = client.db('DB_ID', 'REGION');

    (async function () {
      const coll = await db1.createCollection('movies');

      const admin1 = client.admin();
      const admin2 = client.admin({ adminToken: 'STRONGER_TOKEN' });

      console.log(await coll.insertOne({ name: 'Airplane!' }));
      console.log(await admin1.listDatabases());
    })();

Java  
    // Default Initialization
    DataAPIClient client = new DataAPIClient("TOKEN");

    // Overriding default settings
    DataAPIClient client = new DataAPIClient("TOKEN", DataAPIOptions.builder()
      .withHttpConnectTimeout(20)
      .withHttpRequestTimeout(20)
      .build());

Returns:

`DataAPIClient` - An instance of the client class.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>token</p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>An Access Token to the database.
Example: <code>"AstraCS:aAbB…​"</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options</p></td>
<td
style="text-align: left;"><p>{javadoc-url}com/datastax/astra/client/DataAPIOptions.html[<code>DataAPIOptions</code>]</p></td>
<td style="text-align: left;"><p>A class wrapping the advanced
configuration of the client such as as <code>HttpClient</code> settings
(timeouts…​).</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/DataApiClient.java[role=include]

# See also

-   [api-reference:overview.xml](api-reference:overview.xml)

-   [api-reference:databases.xml](api-reference:databases.xml)

-   [api-reference:collections.xml](api-reference:collections.xml)

-   [api-reference:documents.xml](api-reference:documents.xml)

-   [api-reference:administration.xml](api-reference:administration.xml)

-   [Data API
    changelog](https://github.com/stargate/data-api/blob/main/CHANGELOG.md)
    = Databases reference :navtitle: Databases :page-toclevels: 2

Databases are used to store collections in {product}.

# Connect to a database

You must connect to a database before you can work with data.

Python  
See the
{py-client-api-ref-url}/client.html#astrapy.client.DataAPIClient.get\_database\[API
Reference\] for more details.

Get a reference to an existing database (using the default namespace).

    database = client.get_database("API_ENDPOINT")

The example above is equivalent to the following shorthand:

    database = client["API_ENDPOINT"]

Get a reference to an existing database, additionally specifying a
working namespace explicitly.

    database = client.get_database(
        "API_ENDPOINT",
        namespace="NAMESPACE",
    )

An instance of the `Database` class always has a notion of working
namespace. This can be passed explicitly, as in the last example below,
or left to its system default of `"default_keyspace"`. Some subsequent
operations with the database will act on the working namespace, unless a
different one is given in the method invocation: this holds for
`get_collection`, `create_collection`, `list_collection_names`,
`list_collections` and `command`.

Most `astrapy` objects have an asynchronous counterpart, for use within
the `asyncio` framework. To get an `AsyncDatabase`, clients expose a
`get_async_database` method; likewise, synchronous Databases have a
`to_async` method as well.

See the
{py-client-api-ref-url}/database.html#astrapy.database.AsyncDatabase\[AsyncDatabase\]
API reference for more details about the async API.

Returns:

`{py-client-api-ref-url}/database.html#astrapy.database.Database[Database]` -
An instance of the Database class.

    Database(api_endpoint="https://01234567-89ab-cdef-0123-456789abcdef-us-east1.apps.astra.datastax.com", token="AstraCS:aAbB...", namespace="default_keyspace")

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>id</p></td>
<td style="text-align: left;"><p><code>str</code></p></td>
<td style="text-align: left;"><p>Either a database ID or an API endpoint
URL for the database, used to reach the Data API (e.g.
<code>https://DATABASE_ID-REGION.apps.astra.datastax.com</code>).
DataStax recommends using an API endpoint. If you use a database ID
instead (e.g. <code>01234567-89ab-cdef-0123-456789abcdef</code>), you
can optionally specify a region.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>token</p></td>
<td style="text-align: left;"><p><code>Optional[str]</code></p></td>
<td style="text-align: left;"><p>If supplied, is passed to the Database
instead of the client token.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>namespace</p></td>
<td style="text-align: left;"><p><code>Optional[str]</code></p></td>
<td style="text-align: left;"><p>If provided, is passed to the Database
(it is left to the default otherwise).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>region</p></td>
<td style="text-align: left;"><p><code>Optional[str]</code></p></td>
<td style="text-align: left;"><p>The region to use for connecting to the
database. The database must be accessible in that region. You cannot set
the region parameter when an API endpoint is used instead of an ID. If
you do not set this parameter and the region cannot be inferred from the
API endpoint, an additional DevOps API request is made to determine the
default region and use it in subsequent operations.</p></td>
</tr>
</tbody>
</table>

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")

    database = my_client.get_database("API_ENDPOINT")
    collection = database.create_collection("movies", dimension=5)
    collection.insert_one({
        "title": "The Title",
        "$vector": [0.1, 0.3, -0.7, 0.9, -0.1],
    })

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Db.html\[API Reference\].

Get a reference to an existing database using the default namespace.

    const db = client.db('API_ENDPOINT');

Get a reference to an existing database using a specific namespace.

    const db = client.db('API_ENDPOINT', { namespace: 'NAMESPACE' });

An instance of the {ts-client-api-ref-url}/classes/Db.html\[`Db`\] class
always has a notion of working namespace. This can be passed explicitly,
as in the second example below, or left to its system default of
`'default_keyspace'`. Some subsequent operations with the database will
act on the working namespace, unless a different one is given in the
method invocation: this holds for
{ts-client-api-ref-url}/classes/Db.html#collection\[`collection`\],
{ts-client-api-ref-url}/classes/Db.html#createCollection\[`createCollection`\],
{ts-client-api-ref-url}/classes/Db.html#dropCollection\[`dropCollection`\],
{ts-client-api-ref-url}/classes/Db.html#listCollections\[`listCollections`\],
and {ts-client-api-ref-url}/classes/Db.html#command\[`command`\].

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>endpoint</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The full "API Endpoint" string used to
reach the Database on the Data API (typically of the format
<code>'https://&lt;database_id&gt;-&lt;region&gt;.apps.astra.datastax.com'</code>)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/DbSpawnOptions.html[DbSpawnOptions]</code></p></td>
<td style="text-align: left;"><p>The options to use for the database
(namespace can be overridden in method calls)</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/DbSpawnOptions.html[DbSpawnOptions]`):

Note that if any of these options were set through the client, they act
as the actual defaults for these options (e.g. setting the namespace in
the client, so it’s automatically used for every spawned db).

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DbSpawnOptions.html#namespace[namespace?]</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The namespace to use for the database.
Defaults to <code>'default_keyspace'</code>. Can be overridden in method
calls.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DbSpawnOptions.html#monitorCommands[monitorCommands?]</p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether to monitor commands through
<code>{ts-client-api-ref-url}/classes/CommandEvent.html[CommandEvents]</code>,
using the client as an event emitter. Defaults to false.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DbSpawnOptions.html#token[token?]</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Access token to use for the database.
Default is the client’s token. Typically, of the form
<code>'AstraCS:…​'</code>.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DbSpawnOptions.html#dataApiPath[dataApiPath?]</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to the Data API. Defaults to
<code>'api/json/v1'</code>.</p></td>
</tr>
</tbody>
</table>

Returns:

`{ts-client-api-ref-url}/classes/Db.html[Db]` - An unverified reference
to the database.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts'

    const client = new DataAPIClient('TOKEN');

    // Connect to a database using a direct endpoint
    const db1 = client.db('API_ENDPOINT');

    // Overrides default options from the DataAPIClient
    const db2 = client.db('API_ENDPOINT', {
      namespace: 'NAMESPACE',
      token: 'WEAKER_TOKEN',
    });

    // Lets you connect using a database ID and region
    const db3 = client.db('DB_ID', 'REGION');

    // Use the database
    (async function () {
      const collection = db1.collection('movies');
      await collection.insertOne({ title: 'The Italian Job', $vector: [...] });
    })();

Java  
Get a reference to an existing database. You can access the database
from its endpoint (url) or a combination of identifier, cloud and
region.

To get details on each signature you can access the [DataAPIClient
JavaDOC](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/DataAPIClient.html#method-summary).

    // Given 'client' an instance of 'DataAPIClient'
    Database db1 = client.getDatabase(String apiEndpoint);
    Database db2 = client.getDatabase(String apiEndpoint, String namespace);
    Database db3 = client.getDatabase(UUID databaseId);
    Database db4 = client.getDatabase(UUID databaseId, String namespace);
    Database db5 = client.getDatabase(UUID databaseId, String namespace, String region);

An instance of the `Database` class always has a notion of working
namespace. This can be passed explicitly, or left to its system default
of `"default_keyspace"`. Some subsequent operations with the database
will act on the working namespace, unless a different one is given in
the method invocation: this holds for the `getCollection`,
`createCollection`, `listCollectionNames`, `listCollections` and
`runCommand`.

Returns:

`Database` - An instance of the Database class.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>apiEndpoint</code></p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The endpoint URL for the
database.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The namespace to use. If not provided,
the default is <code>default_keyspace</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>databaseId</code></p></td>
<td style="text-align: left;"><p><code>UUID</code></p></td>
<td style="text-align: left;"><p>The database identifier, the endpoint
url will be built from it using the default region.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>region</code></p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The region where database is deployed
you want to contact. Useful in multi-regions configurations.</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/Connecting.java[role=include]

cURL  
Connect to a database by using the
**`ASTRA_DB_ENDPOINT`**/api/json/v1/**`ASTRA_DB_KEYSPACE`** endpoint.

Parameters:

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 20%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p><strong><code>ASTRA_DB_APPLICATION_TOKEN</code></strong></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The authentication token for Astra
DB.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><strong><code>ASTRA_DB_ENDPOINT</code></strong></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The endpoint URL for the
database.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><strong><code>ASTRA_DB_KEYSPACE</code></strong></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>(Optional) The keyspace to use. If not
provided, the default is <code>default_keyspace</code>.</p></td>
</tr>
</tbody>
</table>

Example:

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json"

CLI  
The CLI gives you an overview of your database metadata.

    astra db describe <database_name>
    astra db describe <database_uid>

Arguments:

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 20%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Options</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>database_name</p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The desired name for the database (does
not ensure uniqueness).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>database_uid</p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The desired identifier for the
database.</p></td>
</tr>
</tbody>
</table>

    +------------------+-----------------------------------------+
    | Attribute        | Value                                   |
    +------------------+-----------------------------------------+
    | Name             | astra_db_client                         |
    | id               | 4391daae-016c-49e3-8d0a-b4633a86082c    |
    | Cloud            | GCP                                     |
    | Regions          | us-east1                                |
    | Status           | ACTIVE                                  |
    | Vector           | Enabled                                 |
    | Default Keyspace | default_keyspace                        |
    | Creation Time    | 2024-02-24T01:20:03Z                    |
    |                  |                                         |
    | Keyspaces        | [0] default_keyspace                    |
    |                  |                                         |
    |                  |                                         |
    | Regions          | [0] us-east1                            |
    |                  |                                         |
    +------------------+-----------------------------------------+

# Create a database

Create a new {product} database. While you can easily create one in
{astra\_ui}, another option is to create the database programmatically.

This and the following topics are also presented in the [Administration
Reference](api-reference:administration.xml#create-a-database). They are
included here for convenience.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/admin.html#astrapy.admin.AstraDBAdmin.create\_database\[API
Reference\].

The database creation is done through an instance of the
`{py-client-api-ref-url}/admin.html#astrapy.admin.AstraDBAdmin[AstraDBAdmin]`
class.

    new_db_admin = admin.create_database(
        "new_database",
        cloud_provider="aws",
        region="ap-south-1",
    )

Returns:

`{py-client-api-ref-url}/admin.html#astrapy.admin.AstraDBDatabaseAdmin[AstraDBDatabaseAdmin]` -
A Database Admin object representing the newly-created database.

    AstraDBDatabaseAdmin(id="01234567-89ab-cdef-0123-456789abcdef", "AstraCS:aAbB...")

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>name</p></td>
<td style="text-align: left;"><p><code>str</code></p></td>
<td style="text-align: left;"><p>The desired name for the
database.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>wait_until_active</p></td>
<td style="text-align: left;"><p><code>bool</code></p></td>
<td style="text-align: left;"><p>If True (default), the method returns
only after the newly-created database is in ACTIVE state (a few minutes,
usually). If False, it will return right after issuing the creation
request to the DevOps API, and it will be responsibility of the caller
to check the database status before working with it.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>cloud_provider</p></td>
<td style="text-align: left;"><p><code>str</code></p></td>
<td style="text-align: left;"><p>one of 'aws', 'gcp' or
'azure'.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>region</p></td>
<td style="text-align: left;"><p><code>str</code></p></td>
<td style="text-align: left;"><p>any of the available cloud
regions.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>namespace</p></td>
<td style="text-align: left;"><p><code>Optional[str]</code></p></td>
<td style="text-align: left;"><p>name for the one namespace the database
starts with. If omitted, DevOps API will use its default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
whole requested operation to complete. Note that a timeout is no
guarantee that the creation request has not reached the API
server.</p></td>
</tr>
</tbody>
</table>

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    admin = client.get_admin()
    new_db_admin = admin.create_database(
        "new_database",
        cloud_provider="aws",
        region="ap-south-1",
    )
    new_db = new_db_admin.get_database()
    collection = new_db.create_collection("movies", dimension=5)
    collection.insert_one({
        "title": "The Title",
        "$vector": [0.1, 0.3, -0.7, 0.9, -0.1],
    })

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/AstraAdmin.html#createDatabase\[API
Reference\].

The database creation is done through an instance of the
`{ts-client-api-ref-url}/classes/AstraAdmin.html[AstraAdmin]` class.

    const newDbAdmin = await admin.createDatabase({
      name: 'new-database',
      region: 'us-east1',
      cloudProvider: 'GCP',
    });

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>config</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/DatabaseConfig.html[DatabaseConfig]</code></p></td>
<td style="text-align: left;"><p>The properties of the database to
create.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/AdminBlockingOptions.html[AdminBlockingOptions]</code></p></td>
<td style="text-align: left;"><p>Options regarding the creation of the
database.</p></td>
</tr>
</tbody>
</table>

Config
(`{ts-client-api-ref-url}/interfaces/DatabaseConfig.html[DatabaseConfig]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DatabaseConfig.html#name[name]</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name of the database (non-unique
user-friendly identifier)</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DatabaseConfig.html#cloudProvider[cloudProvider]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/DatabaseCloudProvider.html[DatabaseCloudProvider]</code></p></td>
<td style="text-align: left;"><p>Cloud provider where the database
lives</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DatabaseConfig.html#region[region]</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The cloud region where the database is
located.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DatabaseConfig.html#namespace[namespace?]</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Overrides the default namespace
(keyspace)</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<{ts-client-api-ref-url}/classes/AstraDbAdmin.html[AstraDbAdmin]>` -
A promised instance of the AstraDbAdmin class for that database.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts'

    // Obtain an admin instance
    const admin = new DataAPIClient('TOKEN').admin();

    (async function () {
      // Create a new database
      const dbAdmin = await admin.createDatabase({
        name: 'my-database',
        region: 'us-east1',
        cloudProvider: 'GCP',
      });

      // Get and use the database
      const db = dbAdmin.db();
      console.log(await db.listCollections());
    })();

The `createDatabase` method blocks until the database is active, by
default. This entails polling the database status until it is `ACTIVE`.
You can disable this behavior by passing `{ blocking: false }` to the
`options` parameter.

Java  
Creating a database is available in the
{javadoc-url}/com/datastax/astra/client/admin/AstraDBAdmin.html\[`AstraDBAdmin`\]
class.

    // Given 'client' an instance of 'DataAPIClient'
    AstraDBAdmin admin = client.getAdmin();
    DatabaseAdmin dbAdmin1 = admin.createDatabase(String name);
    DatabaseAdmin dbAdmin2 = admin.createDatabase(String name, CloudProviderType cloud, String cloudRegion);
    DatabaseAdmin dbAdmin3 = admin.createDatabase(String name, CloudProviderType cloud, String cloudRegion, boolean waitActive);

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The name of the database to
create.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cloud</code></p></td>
<td style="text-align: left;"><p><code>CloudProviderType</code></p></td>
<td style="text-align: left;"><p>The cloud provider where the database
will be created.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cloudRegion</code></p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The region of the cloud provider where
the database will be created.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>waitActive</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Default behavior is synchronous and
wait for the database to be active; if the parameter is provided, the
operation will be asynchronous.</p></td>
</tr>
</tbody>
</table>

Returned Values:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>DatabaseAdmin</code></p></td>
<td style="text-align: left;"><p>The administration object for the
database to manage namespaces or to access the database.</p></td>
</tr>
</tbody>
</table>

You cannot use the database until it is created and its status is
`ACTIVE`.

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/admin/CreateDatabase.java[role=include]

CLI  
To create a database, use the following command:

    astra db create <db_name> \
       --region <region>
       --cloud <cloud>  \
       -k <keyspace> \
       --if-not-exist
       --async

Arguments:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 40%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Options</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>db_name</p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The desired name for the
database.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>region</p></td>
<td style="text-align: left;"><p><code>String</code> (OPTIONAL)</p></td>
<td style="text-align: left;"><p>The region where to create the
database, it goes with the cloud provider.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>cloud</p></td>
<td style="text-align: left;"><p><code>String</code> (OPTIONAL)</p></td>
<td style="text-align: left;"><p>The cloud provider
(<code>gcp,azure,aws</code>) where to create the database.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>keyspace</p></td>
<td style="text-align: left;"><p><code>String</code> (OPTIONAL)</p></td>
<td style="text-align: left;"><p>The name of the namespace, if not
provided default is <code>default_keyspace</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--if-not-exists</code></p></td>
<td style="text-align: left;"><p><code>flag</code> (OPTIONAL)</p></td>
<td style="text-align: left;"><p>If provided, make the operation
idempotent.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--async</code></p></td>
<td style="text-align: left;"><p><code>flag</code> (OPTIONAL)</p></td>
<td style="text-align: left;"><p>Default behavior is synchronous and
wait for the db to be active; if this parameters is provided, the
operation will be asynchronous.</p></td>
</tr>
</tbody>
</table>

The command will wait until the database is created and ready to use. To
know more use the command `astra help db create`.

# Get database information

Get all information on a database.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/admin.html#astrapy.admin.AstraDBAdmin.database\_info\[API
Reference\].

This operation is done through an instance of the
`{py-client-api-ref-url}/admin.html#astrapy.admin.AstraDBAdmin[AstraDBAdmin]`
class.

    db_info = admin.database_info("01234567-...")

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>id</p></td>
<td style="text-align: left;"><p><code>str</code></p></td>
<td style="text-align: left;"><p>The ID of the target database, e. g.
"01234567-89ab-cdef-0123-456789abcdef".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the API
request.</p></td>
</tr>
</tbody>
</table>

Returns:

`{py-client-api-ref-url}/info.html#astrapy.info.AdminDatabaseInfo[AdminDatabaseInfo]` -
An object containing the requested information.

    # (output below abridged and reformatted in pprint-style for clarity)

    AdminDatabaseInfo(
        info=DatabaseInfo(
            id='01234567-89ab-cdef-0123-456789abcdef',
            region='us-east1',
            namespace='default_keyspace',
            name='my_database',
            environment='prod',
            raw_info={
                'additionalKeyspaces': [
                    'default_keyspace',
                    'my_dreamspace'
                ],
                'capacityUnits': 1,
                'cloudProvider': 'GCP',
                'datacenters': [
                    {
                        'capacityUnits': 1,
                        'cloudProvider': 'GCP',
                        'dateCreated': '2023-06-05T21:29:46Z',
                        'id': '01234567-89ab-cdef-0123-456789abcdef-1',
                        'isPrimary': True,
                        'name': 'dc-1',
                        'region': 'us-east1',
                        'regionClassification': 'standard',
                        'regionZone': 'na',
                        'secureBundleInternalUrl': 'https://...',
                        'secureBundleMigrationProxyInternalUrl': 'https://...',
                        'secureBundleMigrationProxyUrl': 'https://...',
                        'secureBundleUrl': 'https://datastax-cluster...',
                        'status': '',
                        'tier': 'serverless'
                    }
                ],
                'dbType': 'vector',
                'keyspace': 'default_keyspace',
                'keyspaces': [
                    'default_keyspace',
                    'my_dreamspace'
                ],
                'name': 'my_database',
                'region': 'us-east1',
                'tier': 'serverless'
            }
        ),
        available_actions=[
            'getCreds',
            'addDatacenters',
            '...',
            'hibernate'
        ],
        cost={
            'costPerDayCents': 0,
            'costPerDayMRCents': 0,
            '...': 0,
            'costPerReadGbCents': 0.1,
            'costPerWrittenGbCents': 0.1
        },
        cqlsh_url='https://01234567-....datastax.com/cqlsh',
        creation_time='2023-06-05T21:29:46Z',
        data_endpoint_url='https://01234567-....datastax.com/api/rest',
        grafana_url='https://01234567-....datastax.com/d/cloud/...',
        graphql_url='https://01234567-....datastax.com/api/graphql',
        id='01234567-89ab-cdef-0123-456789abcdef',
        last_usage_time='2024-03-22T15:00:14Z',
        metrics={
            'errorsTotalCount': 0,
            'liveDataSizeBytes': 0,
            'readRequestsTotalCount': 0,
            'writeRequestsTotalCount': 0
        },
        observed_status='ACTIVE',
        org_id='aabbccdd-eeff-0011-2233-445566778899',
        owner_id='00112233-4455-6677-8899aabbddeeff',
        status='ACTIVE',
        storage={
            'displayStorage': 10,
            'nodeCount': 3,
            'replicationFactor': 1,
            'totalStorage': 5
        },
        termination_time='0001-01-01T00:00:00Z',
        raw_info={...}
    )

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    admin = client.get_admin()

    db_details = admin.database_info("01234567-...")
    db_details.id
    # '01234567-...'
    db_details.status
    # 'ACTIVE'
    db_details.info.region
    # 'eu-west-1'

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/AstraAdmin.html#dbInfo\[API Reference\].

This operation is done through an instance of the
`{ts-client-api-ref-url}/classes/AstraAdmin.html[AstraAdmin]` class.

    const dbInfo = admin.dbInfo('DB_ID');

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>id</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The ID of the target database.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/WithTimeout.html[WithTimeout]</code></p></td>
<td style="text-align: left;"><p>The options (the timeout) for this
operation.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<{ts-client-api-ref-url}/interfaces/FullDatabaseInfo[FullDatabaseInfo]>` -
A promise that resolves to the complete information for the
corresponding database.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts'

    const admin = new DataAPIClient('TOKEN').admin();

    (async function () {
      const details = await admin.dbInfo('DB_ID');
      console.log(details.id); // '01234567-...'
      console.log(details.status); // 'ACTIVE'
      console.log(details.info.region); // 'eu-west-1'
    })();

Java  
    // Given 'admin' an instance of 'AstraDBAdmin'
    DatabaseInfo info = admin.getDatabaseInfo(UUID id);

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>id</code></p></td>
<td style="text-align: left;"><p><code>UUID</code></p></td>
<td style="text-align: left;"><p>The unique identifier of the database
to find.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The name of the database to
find.</p></td>
</tr>
</tbody>
</table>

Returned values:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{javadoc-url}/latest/com/datastax/astra/client/model/DatabaseInfo.html[<code>DatabaseInfo</code>]</p></td>
<td style="text-align: left;"><p>Database information wrapped as an
object. The UUID ensures that the database is unique; you get one
database or nothing.</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/admin/GetDatabaseInformation.java[role=include]

CLI  
To access details about a database, use the following commands:

    astra db describe <database_name>
    astra db describe <database_id>

# Find all databases

Retrieve the listing of all databases.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/admin.html#astrapy.admin.AstraDBAdmin.list\_databases\[API
Reference\].

This operation is done through an instance of the
`{py-client-api-ref-url}/admin.html#astrapy.admin.AstraDBAdmin[AstraDBAdmin]`
class.

    all_databases = admin.list_databases()

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the API
request.</p></td>
</tr>
</tbody>
</table>

Returns:

`{py-client-api-ref-url}/cursors.html#astrapy.cursors.CommandCursor[CommandCursor][{py-client-api-ref-url}/info.html#astrapy.info.AdminDatabaseInfo[AdminDatabaseInfo]]` -
An iterable of `AdminDatabaseInfo` objects, each carrying detailed
information on a database.

    # (output below abridged and reformatted in pprint-style for clarity)
    # (a single example AdminDatabaseInfo from the cursor is shown)

    [
        ...,
        AdminDatabaseInfo(
            info=DatabaseInfo(
                id='01234567-89ab-cdef-0123-456789abcdef',
                region='us-east1',
                namespace='default_keyspace',
                name='my_database',
                environment='prod',
                raw_info={
                    'additionalKeyspaces': [
                        'default_keyspace',
                        'my_dreamspace'
                    ],
                    'capacityUnits': 1,
                    'cloudProvider': 'GCP',
                    'datacenters': [
                        {
                            'capacityUnits': 1,
                            'cloudProvider': 'GCP',
                            'dateCreated': '2023-06-05T21:29:46Z',
                            'id': '01234567-89ab-cdef-0123-456789abcdef-1',
                            'isPrimary': True,
                            'name': 'dc-1',
                            'region': 'us-east1',
                            'regionClassification': 'standard',
                            'regionZone': 'na',
                            'secureBundleInternalUrl': 'https://...',
                            'secureBundleMigrationProxyInternalUrl': 'https://...',
                            'secureBundleMigrationProxyUrl': 'https://...',
                            'secureBundleUrl': 'https://datastax-cluster...',
                            'status': '',
                            'tier': 'serverless'
                        }
                    ],
                    'dbType': 'vector',
                    'keyspace': 'default_keyspace',
                    'keyspaces': [
                        'default_keyspace',
                        'my_dreamspace'
                    ],
                    'name': 'my_database',
                    'region': 'us-east1',
                    'tier': 'serverless'
                }
            ),
            available_actions=[
                'getCreds',
                'addDatacenters',
                '...',
                'hibernate'
            ],
            cost={
                'costPerDayCents': 0,
                'costPerDayMRCents': 0,
                '...': 0,
                'costPerReadGbCents': 0.1,
                'costPerWrittenGbCents': 0.1
            },
            cqlsh_url='https://01234567-....datastax.com/cqlsh',
            creation_time='2023-06-05T21:29:46Z',
            data_endpoint_url='https://01234567-....datastax.com/api/rest',
            grafana_url='https://01234567-....datastax.com/d/cloud/...',
            graphql_url='https://01234567-....datastax.com/api/graphql',
            id='01234567-89ab-cdef-0123-456789abcdef',
            last_usage_time='2024-03-22T15:00:14Z',
            metrics={
                'errorsTotalCount': 0,
                'liveDataSizeBytes': 0,
                'readRequestsTotalCount': 0,
                'writeRequestsTotalCount': 0
            },
            observed_status='ACTIVE',
            org_id='aabbccdd-eeff-0011-2233-445566778899',
            owner_id='00112233-4455-6677-8899aabbddeeff',
            status='ACTIVE',
            storage={
                'displayStorage': 10,
                'nodeCount': 3,
                'replicationFactor': 1,
                'totalStorage': 5
            },
            termination_time='0001-01-01T00:00:00Z',
            raw_info={...}
        ),
        ...
    ]

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    admin = client.get_admin()

    database_cursor = admin.list_databases()
    database_list = list(database_cursor)
    len(database_list)
    # 3
    database_list[2].id
    # '01234567-...'
    database_list[2].status
    # 'ACTIVE'
    database_list[2].info.region
    # 'eu-west-1'

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/AstraAdmin.html#listDatabases\[API
Reference\].

This operation is done through an instance of the
`{ts-client-api-ref-url}/classes/AstraAdmin.html[AstraAdmin]` class.

    const dbs = await admin.listDatabases();

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>options</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/ListDatabasesOptions.html[ListDatabasesOptions]</code></p></td>
<td style="text-align: left;"><p>The filters to use when listing the
database</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/ListDatabasesOptions.html[ListDatabasesOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/ListDatabasesOptions.html#include[include?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/DatabaseStatus.html[DatabaseStatus]</code></p></td>
<td style="text-align: left;"><p>Allows filtering by database status.
Defaults to <code>NONTERMINATED</code>.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/ListDatabasesOptions.html#provider[provider?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/DatabaseCloudProviderFilter.html[DatabaseCloudProviderFilter]</code></p></td>
<td style="text-align: left;"><p>Allows filtering by cloud provider.
Defaults to <code>ALL</code>.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/ListDatabasesOptions.html#limit[limit?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>Number of databases to return, between
1-100. Defaults to 25.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/ListDatabasesOptions.html#skip[skip?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>Number of databases to skip. Defaults
to 0.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/ListDatabasesOptions.html#maxTimeMs[maxTimeMs?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>Maximum time in milliseconds the client
should wait for the operation to complete.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<{ts-client-api-ref-url}/interfaces/FullDatabaseInfo[FullDatabaseInfo][]>` -
A promised list of the complete information for all the databases
matching the given filter.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts'

    const admin = new DataAPIClient('TOKEN').admin();

    (async function () {
      const activeDbs = await admin.listDatabases({ include: 'ACTIVE' });

      for (const db of activeDbs) {
        console.log(`Database ${db.name} is active`);
      }
    })();

Java  
Listing databased function is available in the
{javadoc-url}/com/datastax/astra/client/admin/AstraDBAdmin.html\[`AstraDBAdmin`\]
class

    // Given 'admin' an instance of 'AstraDBAdmin'
    String<String> nameList = admin.listDatabaseNames();
    String<DatabaseInfo> infoList = admin.listDatabases();

Returned Values:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{javadoc-url}/com/datastax/astra/client/model/DatabaseInfo.html[<code>List&lt;DatabaseInfo&gt;</code>]</p></td>
<td style="text-align: left;"><p>Database information list exposed as a
Stream.</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/admin/ListDatabases.java[role=include]

CLI  
To list all databases, use the following command:

    astra db list

    +---------------------+--------------------------------------+-----------+-------+---+-----------+
    | Name                | id                                   | Regions   | Cloud | V | Status    |
    +---------------------+--------------------------------------+-----------+-------+---+-----------+
    | astra_db_client     | 4391daae-016c-49e3-8d0a-b4633a86082c | us-east1  | gcp   | ■ | ACTIVE    |
    +---------------------+--------------------------------------+-----------+-------+---+-----------+

# Drop a database

Drop (delete) a database, erasing all data stored in it as well.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/admin.html#astrapy.admin.AstraDBAdmin.drop\_database\[API
Reference\].

The database deletion is done through an instance of the
`{py-client-api-ref-url}/admin.html#astrapy.admin.AstraDBAdmin[AstraDBAdmin]`
class.

    admin.drop_database("01234567-...")

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>id</p></td>
<td style="text-align: left;"><p><code>str</code></p></td>
<td style="text-align: left;"><p>The ID of the database to drop, e. g.
"01234567-89ab-cdef-0123-456789abcdef".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>wait_until_active</p></td>
<td style="text-align: left;"><p><code>bool</code></p></td>
<td style="text-align: left;"><p>If True (default), the method returns
only after the database has actually been deleted (generally a few
minutes). If False, it will return right after issuing the drop request
to the DevOps API, and it will be responsibility of the caller to check
the database status/availability after that, if desired.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
whole requested operation to complete. Note that a timeout is no
guarantee that the deletion request has not reached the API
server.</p></td>
</tr>
</tbody>
</table>

Returns:

`Dict` - A dictionary in the form `{"ok": 1}` if the method succeeds.

    {"ok": 1}

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    admin = client.get_admin()

    database_list_pre = list(admin.list_databases())
    len(database_list_pre)
    # 3
    admin.drop_database("01234567-...")
    # {'ok': 1}
    database_list_post = list(admin.list_databases())
    len(database_list_post)
    # 2

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/AstraAdmin.html#dropDatabase\[API
Reference\].

The database termination is done through an instance of the
`{ts-client-api-ref-url}/classes/AstraAdmin.html[AstraAdmin]` class.

    await admin.dropDatabase('DB_ID');

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>db</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/classes/Db.html[Db] | string</code></p></td>
<td style="text-align: left;"><p>The <code>Db</code>, or database ID, to
drop.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/AdminBlockingOptions.html[AdminBlockingOptions]</code></p></td>
<td style="text-align: left;"><p>Options regarding the termination of
the database.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<void>` - A promise that resolves when the database is
terminated.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts'

    const admin = new DataAPIClient('TOKEN').admin();

    (async function () {
      await admin.dropDatabase('DB_ID');
    })();

The `dropDatabase` method blocks until the database is deleted, by
default. This entails polling the database status until it is
`TERMINATED`. You can disable this behavior by passing
`{ blocking: false }` to the `options` parameter.

Java  
Listing databased function is available in the
{javadoc-url}/com/datastax/astra/client/admin/AstraDBAdmin.html\[`AstraDBAdmin`\]
class.

    boolean AstraDBAdmin.deleteDatabase(String name);
    boolean AstraDBAdmin.deleteDatabase(UUID id);

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>id</code></p></td>
<td style="text-align: left;"><p><code>UUID</code></p></td>
<td style="text-align: left;"><p>The identifier of the database to
delete.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The name of the database to
delete.</p></td>
</tr>
</tbody>
</table>

Returned Values:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Flag indicating if the database was
deleted.</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/admin/DropDatabase.java[role=include]

CLI  
To delete a database, use the following command:

    astra db delete <db_name>
    astra db delete <db_id>

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>db_id</code></p></td>
<td style="text-align: left;"><p><code>UUID</code></p></td>
<td style="text-align: left;"><p>The identifier of the database to
delete.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>db_name</code></p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The name of the database to
delete.</p></td>
</tr>
</tbody>
</table>

# See also

-   [api-reference:overview.xml](api-reference:overview.xml)

-   [api-reference:dataapiclient.xml](api-reference:dataapiclient.xml)

-   [api-reference:collections.xml](api-reference:collections.xml)

-   [api-reference:documents.xml](api-reference:documents.xml)

-   [api-reference:administration.xml](api-reference:administration.xml)

-   [Data API
    changelog](https://github.com/stargate/data-api/blob/main/CHANGELOG.md)
    = Collections reference :navtitle: Collections :page-toclevels: 2

Collections are used to store documents in {product}.

Use the `Database` class to manage collections, and the `Collection`
class itself to work with the data in them.

Currently, you can create up to five collections in an {product}
database.

The examples in this topic assume you have already created an {product}
database. The Data API supports vector-enabled {product} databases. If
you haven’t already, sign into [{astra\_ui}](https://astra.datastax.com)
to create a vector-enabled {product} database. See
[databases:create-database.xml](databases:create-database.xml).

In addition, the client app examples (Python, TypeScript, Java) in this
topic and subsequent API Reference topics assume you have already:

1.  Instantiated a `DataAPIClient` object. See
    [api-reference:dataapiclient.xml](api-reference:dataapiclient.xml).

2.  Connected to a database. See
    [api-reference:databases.xml](api-reference:databases.xml).

# Create a collection

Create a new collection in an {product} database.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/database.html#astrapy.database.Database.create\_collection\[API
Reference\].

    collection = database.create_collection("collection")

Create a new collection to store vector data.

    from astrapy.constants import VectorMetric

    collection = database.create_collection(
        "vector_collection",
        dimension=5,
        metric=VectorMetric.COSINE,
    )

Create a new collection that generates vector embeddings automatically.

To automatically generate vector embeddings, you must enable the
corresponding [embedding provider
integration](databases:embedding-generation.xml), add the embedding
provider API key in the Astra KMS, and make sure your database can
access the embedding provider service.

    from astrapy.info import CollectionVectorServiceOptions
    from astrapy.constants import VectorMetric

    collection = database.create_collection(
        "vector_auto_collection",
        metric=VectorMetric.DOT_PRODUCT,
        service=CollectionVectorServiceOptions(
            provider="openai",
            model_name="text-embedding-3-small",
            authentication={
                "providerKey": "API_KEY_NAME",
            },
        ),
    )

Create a new collection with [default document IDs of type
`ObjectID`](#the-defaultid-option).

    from astrapy.constants import DefaultIdType

    collection = database.create_collection(
        "collection_defaulting_to_objectids",
        default_id_type=DefaultIdType.OBJECTID,
    )

Create a new collection with [only some fields
indexed](#the-indexing-option).

    collection = database.create_collection(
        "partial_indexing_collection",
        indexing={"allow": ["city", "country"]},
    )

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>name</p></td>
<td style="text-align: left;"><p><code>str</code></p></td>
<td style="text-align: left;"><p>The name of the collection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>namespace</p></td>
<td style="text-align: left;"><p><code>Optional[str]</code></p></td>
<td style="text-align: left;"><p>The namespace where the collection is
to be created. If not specified, the database’s working namespace is
used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>dimension</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>For vector collections, the dimension
of the vectors; that is, the number of their components. If you’re not
sure what dimension to set, use whatever dimension vector your <a
href="get-started:concepts.xml#popular-embedding-models">embeddings
model</a> produces.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>metric</p></td>
<td style="text-align: left;"><p><code>Optional[str]</code></p></td>
<td style="text-align: left;"><p>The <a
href="get-started:concepts.xml#metrics">similarity metric</a> used for
vector searches. Allowed values are
<code>{py-client-api-ref-url}/constants.html#astrapy.constants.VectorMetric.DOT_PRODUCT[VectorMetric.DOT_PRODUCT]</code>,
<code>{py-client-api-ref-url}/constants.html#astrapy.constants.VectorMetric.EUCLIDEAN[VectorMetric.EUCLIDEAN]</code>
or
<code>{py-client-api-ref-url}/constants.html#astrapy.constants.VectorMetric.COSINE[VectorMetric.COSINE]</code>
(default).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>service</p></td>
<td
style="text-align: left;"><p><code>Optional[CollectionVectorServiceOptions]</code></p></td>
<td style="text-align: left;"><p>The service definition for vector
embeddings. Required for vector collections that generate embeddings
automatically.</p>
<p>This is an instance of
<code>{py-client-api-ref-url}/info.html#astrapy.info.CollectionVectorServiceOptions[CollectionVectorServiceOptions]</code>,
which defines the <code>provider</code> and <code>model_name</code>, and
other optional settings, such as <code>authentication</code>. This
parameter can also be a simple dictionary.</p>
<p><code>authentication</code> is an object defining how to authenticate
with the embeddings provider. For example,
<code>{providerKey: "API_KEY_NAME"}</code>, where
<code>API_KEY_NAME</code> is the name of your embeddings provider key in
the {astra_db} KMS.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>indexing</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>Optional specification of the indexing
options for the collection, in the form of a dictionary such as
<code>{"deny": […​]}</code> or <code>{"allow": […​]}</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>default_id_type</p></td>
<td style="text-align: left;"><p><code>Optional[str]</code></p></td>
<td style="text-align: left;"><p>This sets what type of IDs the API
server will generate when inserting documents that do not specify their
<code>_id</code> field explicitly. Can be set to any of the values
<code>{py-client-api-ref-url}/constants.html#astrapy.constants.DefaultIdType.UUID[DefaultIdType.UUID]</code>,
<code>{py-client-api-ref-url}/constants.html#astrapy.constants.DefaultIdType.OBJECTID[DefaultIdType.OBJECTID]</code>,
<code>{py-client-api-ref-url}/constants.html#astrapy.constants.DefaultIdType.UUIDV6[DefaultIdType.UUIDV6]</code>,
<code>{py-client-api-ref-url}/constants.html#astrapy.constants.DefaultIdType.UUIDV7[DefaultIdType.UUIDV7]</code>,
<code>{py-client-api-ref-url}/constants.html#astrapy.constants.DefaultIdType.DEFAULT[DefaultIdType.DEFAULT]</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>additional_options</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>Any further set of key-value pairs that
will be added to the "options" part of the payload when sending the Data
API command to create a collection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>check_exists</p></td>
<td style="text-align: left;"><p><code>Optional[bool]</code></p></td>
<td style="text-align: left;"><p>Whether to run an existence check for
the collection name before attempting to create the collection: If
<code>check_exists</code> is True, an error is raised when creating an
existing collection. If it is False, the creation is attempted. In this
case, for preexisting collections, the command will succeed or fail
depending on whether the options match or not.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
underlying HTTP request.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>embedding_api_key</p></td>
<td style="text-align: left;"><p><code>Optional[str]</code></p></td>
<td style="text-align: left;"><p>An alternative to
<code>authentication</code> in
<code>CollectionVectorServiceOptions</code>. Provide the API key
directly instead of using an API key in the {astra_db} KMS. The API key
is passed to the Data API with each request in the form of an
<code>x-embedding-api-key</code> HTTP header.</p>
<p>This parameter is not stored on the database, and it is used by the
<code>Collection</code> instance only when issuing reads or writes on
the collection.</p>
<p>This is useful for creating collections with an embedding service
without specifying an <code>authentication</code> in the service
configuration.</p>
<p><code>embedding_api_key</code> overrides the {astra_db} KMS API key
if you set both.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>collection_max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A default timeout, in milliseconds, for
the duration of each operation on the collection. Individual timeouts
can be provided to each collection method call and will take precedence,
with this value being an overall default. Note that for some methods
involving multiple API calls (such as <code>delete_many</code> and
<code>insert_many</code>), you should provide a timeout with sufficient
duration for the operation you’re performing. This parameter is not
stored on the database, it is only used by the <code>Collection</code>
instance when issuing reads or writes on the collection.</p></td>
</tr>
</tbody>
</table>

Returns:

`{py-client-api-ref-url}/collection.html#astrapy.collection.Collection[Collection]` -
The created collection object, ready to be used to work with the
documents in it.

    Collection(name="collection", namespace="default_keyspace", database=Database(api_endpoint="https://01234567-89ab-cdef-0123-456789abcdef-us-east1.apps.astra.datastax.com", token="AstraCS:aAbB...", namespace="default_keyspace"))

Example:

    from astrapy import DataAPIClient
    import astrapy
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")

    # Create a non-vector collection
    collection_simple = database.create_collection("collection")

    # Create a vector collection
    collection_vector = database.create_collection(
        "vector_collection",
        dimension=3,
        metric=astrapy.constants.VectorMetric.COSINE,
    )

    # Create a collection with UUIDv6 as default IDs
    from astrapy.constants import DefaultIdType, SortDocuments

    collection_uuid6 = database.create_collection(
        "uuid6_collection",
        default_id_type=DefaultIdType.UUIDV6,
    )

    collection_uuid6.insert_one({"desc": "a document", "seq": 0})
    collection_uuid6.insert_one({"_id": 123, "desc": "another", "seq": 1})
    doc_ids = [
        doc["_id"]
        for doc in collection_uuid6.find({}, sort={"seq": SortDocuments.ASCENDING})
    ]
    print(doc_ids)
    #  Will print: [UUID('1eef29eb-d587-6779-adef-45b95ef13497'), 123]
    print(doc_ids[0].version)
    #  Will print: 6

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Db.html#createCollection\[API
Reference\].

    const collection = await db.createCollection('COLLECTION');

Create a new collection to store vector data.

    const collection = await db.createCollection<Schema>('COLLECTION', {
      vector: {
        dimension: 5,
        metric: 'cosine',
      },
      checkExists: false,
    });

Create a new collection that generates vector embeddings automatically.

To automatically generate vector embeddings, you must enable the
corresponding [embedding provider
integration](databases:embedding-generation.xml), add the embedding
provider API key in the Astra KMS, and make sure your database can
access the embedding provider service.

    const collection = await db.createCollection<Schema>('COLLECTION', {
      vector: {
        metric: 'dot_product',
        service: {
          provider: 'openai',
          modelName: 'text-embedding-3-small',
          authentication: {
            providerKey: 'API_KEY_NAME',
          },
        },
      },
      checkExists: false,
    });

A `Collection` is typed as `Collection<Schema>` where `Schema` is the
type of the documents in the collection. Operations on the collection
will be strongly typed if a specific schema is provided, otherwise
remained largely weakly typed if no type is provided, which may be
preferred for dynamic data access & operations. It’s up to the user to
ensure that the provided type truly represents the documents in the
collection.

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>collectionName</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The name of the collection to
create.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>vector?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/CreateCollectionOptions.html[CreateCollectionOptions&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>The options for creating the
collection.</p>
<ul>
<li><p><code>dimension</code>: The dimension for the vector in the
collection.</p></li>
<li><p><code>metric</code>: The similarity metric to use for vector
search.</p></li>
<li><p><code>service.provider</code>: The name of the embeddings
provider. Required for vector collections that generate embeddings
automatically.</p></li>
<li><p><code>service.modelName</code>: The model name for vector
embeddings.</p></li>
<li><p><code>service.authentication</code>: An object defining how to
authenticate with the embeddings provider. For example,
<code>{providerKey: 'API_KEY_NAME'}</code>, where
<code>API_KEY_NAME</code> is the name of your embeddings provider key in
the {astra_db} KMS.</p></li>
</ul></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/CreateCollectionOptions.html[CreateCollectionOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/CreateCollectionOptions.html#vector[vector?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/VectorOptions.html[VectorOptions]</code></p></td>
<td style="text-align: left;"><p>The vector configuration for the
collection, e.g. vector dimension &amp; similarity metric. If not set,
collection will not support vector search. If you’re not sure what
dimension to set, use whatever dimension vector your <a
href="get-started:concepts.xml#popular-embedding-models">embeddings
model</a> produces.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/CreateCollectionOptions.html#indexing[indexing?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/IndexingOptions.html[IndexingOptions&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>The indexing configuration for the
collection.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/CreateCollectionOptions.html#defaultId[defaultId?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/DefaultIdOptions.html[DefaultIdOptions]</code></p></td>
<td style="text-align: left;"><p>The defaultId configuration for the
collection, for when a document does not specify an <code>_id</code>
field.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/CreateCollectionOptions.html#namespace[namespace?]</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Overrides the namespace where the
collection is created. If not set, the database’s working namespace is
used.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/CreateCollectionOptions.html#checkExists[checkExists?]</p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether to run an existence check for
the collection name before attempting to create the collection.</p>
<p>If it is <code>true</code> or unset, an error is raised when creating
an existing collection.</p>
<p>Else, if it’s <code>false</code>, the creation is attempted. In this
case, for preexisting collections, the command will succeed or fail
depending on whether the options match or not.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/CreateCollectionOptions.html#embeddingsApiKey[embeddingApiKey?]</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>An alternative to
<code>service.authentication.providerKey</code> for the embeddings
provider. Provide the API key directly instead of using an API key in
the {astra_db} KMS. <code>embeddingApiKey</code> overrides the
{astra_db} KMS API key if you set both.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/CreateCollectionOptions.html#maxTimeMs[maxTimeMs?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>Maximum time in milliseconds the client
should wait for the operation to complete.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<{ts-client-api-ref-url}/classes/Collection.html[Collection<Schema>]>` -
A promise that resolves to the created collection object.

Example:

    import { DataAPIClient, VectorDoc } from '@datastax/astra-db-ts';

    // Get a new Db instance
    const db = new DataAPIClient('TOKEN').db('API_ENDPOINT');

    // Define the schema for the collection
    interface User extends VectorDoc {
      name: string,
      age?: number,
    }

    (async function () {
      // Create a basic untyped non-vector collection
      const users1 = await db.createCollection('users');
      await users1.insertOne({ name: 'John' });

      // Typed collection with custom options in a non-default namespace
      const users2 = await db.createCollection<User>('users', {
        namespace: 'NAMESPACE',
        defaultId: {
          type: 'objectId',
        },
        vector: {
          dimension: 5,
          metric: 'cosine',
        },
      });
      await users2.insertOne({ name: 'John' }, { sort: { $vector: [.12, .62, .87, .16, .72] } });
    })();

See also: {ts-client-api-ref-url}/types/SomeDoc.html\[SomeDoc\],
{ts-client-api-ref-url}/interfaces/VectorDoc.html\[VectorDoc\]

Java  
To access the Javadoc on those methods consult the
{javadoc-url}com/datastax/astra/client/Database.html\[Database
Javadoc\].

    // Given db Database object, create a new collection

    // Create simple collection with given name.
    Collection<Document> simple1 = db
      .createCollection(String collectionName);
    Collection<MyBean> simple2 = db
      .createCollection(String collectionName, Class<MyBean> clazz);

    // Create collections with vector options
    Collection<Document> vector1 = createCollection(
      String collectionName,
      int dimension,
      SimilarityMetric metric);
    Collection<MyBean> vector2 = createCollection(
      String collectionName,
      int dimension,
      SimilarityMetric metric,
      Class<MyBean> clazz);

    // Full-Fledged CollectionOptions with a builder
    Collection<Document> full1 = createCollection(
       String collectionName,
       CollectionOptions collectionOptions);
    Collection<MyBean> full2 = createCollection(
       String collectionName,
       CollectionOptions collectionOptions,
       Class<MyBean> clazz);

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>collectionName</code></p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The name of the collection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dimension</code></p></td>
<td style="text-align: left;"><p><code>int</code></p></td>
<td style="text-align: left;"><p>The dimension for the vector in the
collection. If you’re not sure what dimension to set, use whatever
dimension vector your <a
href="get-started:concepts.xml#popular-embedding-models">embeddings
model</a> produces.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metric</code></p></td>
<td style="text-align: left;"><p><code>SimilarityMetric</code></p></td>
<td style="text-align: left;"><p>The <a
href="get-started:concepts.xml#metrics">similarity metric</a> to use for
vector search: <code>SimilarityMetric.cosine</code> (default),
<code>SimilarityMetric.dot_product</code>, or
<code>SimilarityMetric.euclidean</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collectionOptions</code></p></td>
<td style="text-align: left;"><p><code>CollectionOptions</code></p></td>
<td style="text-align: left;"><p>Fine-grained settings with vector,
embedding provider, model name, authentication, indexing, and
<code>defaultId</code> options.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>clazz</code></p></td>
<td style="text-align: left;"><p><code>Class&lt;T&gt;</code></p></td>
<td style="text-align: left;"><p>Working with specialized beans for the
collection and not the default <code>Document</code> type.</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/database/CreateCollection.java[role=include]

cURL  
    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
        "createCollection": {
            "name": "vector_collection",
            "options": {
                "defaultId": {
                    "type": "objectId"
                },
                "vector": {
                    "dimension": 5,
                    "metric": "cosine"
                },
                "indexing": {
                    "allow": ["*"]
                }
            }
        }
    }' | jq
    # `| jq` is optional.

Properties:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>createCollection</code></p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>The Data API command that specifies a
new collection is to be created. It acts as a container for all the
attributes and settings required to create the new collection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>The name of the new collection. A
string value that uniquely identifies the collection within the
database.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>options</code></p></td>
<td style="text-align: left;"><p>Optional[string]</p></td>
<td style="text-align: left;"><p>Options for the collection, such as
configuration for vector search. Required to create a vector-enabled
collection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>options.defaultId</code></p></td>
<td style="text-align: left;"><p>Optional[string]</p></td>
<td style="text-align: left;"><p>Controls how the Data API will allocate
a new <code>_id</code> for each document that does not specify a value
in the request. For backwards compatibility with Data API releases
before version 1.0.3, if you omit a <code>defaultId</code> option on
<code>createCollection</code>, a document’s <code>_id</code> value is a
plain String version of random-based UUID (version 4).</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>options.defaultId.type</code></p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: left;"><p>Required if <code>defaultId</code>
option is used. Specifies one of <code>objectId</code>,
<code>uuidv7</code>, <code>uuidv6</code>, <code>uuid</code>. Cannot be
changed after the collection is created.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>options.vector.dimension</code></p></td>
<td style="text-align: left;"><p>Optional[int]</p></td>
<td style="text-align: left;"><p>The dimension for vector search in the
collection. If you’re not sure what dimension to set, use whatever
dimension vector your <a
href="get-started:concepts.xml#popular-embedding-models">embeddings
model</a> produces.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>options.vector.metric</code></p></td>
<td style="text-align: left;"><p>Optional[string]</p></td>
<td style="text-align: left;"><p>The <a
href="get-started:concepts.xml#metrics">similarity metric</a> to use for
vector search: <code>cosine</code> (default), <code>dot_product</code>,
or <code>euclidean</code>.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>options.vector.provider</code></p></td>
<td style="text-align: left;"><p>Optional[string]</p></td>
<td style="text-align: left;"><p>The service provider for vector
embeddings. Required for vector collections that generate embeddings
automatically.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>options.vector.modelName</code></p></td>
<td style="text-align: left;"><p>Optional[string]</p></td>
<td style="text-align: left;"><p>The model name for vector
embeddings.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>options.vector.authentication</code></p></td>
<td style="text-align: left;"><p>Optional[string]</p></td>
<td style="text-align: left;"><p>Authenticate with the embeddings
provider using an API key in the {astra_db} KMS. Alternatively, you can
provide the embeddings provider key directly in an
<code>x-embedding-api-key</code> header.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>options.indexing</code></p></td>
<td style="text-align: left;"><p>Optional[string]</p></td>
<td style="text-align: left;"><p>Determine which properties are indexed
during subsequent update operations. If indexing is specified on
<code>createCollection</code>, you must further specify
<code>allow</code> or <code>deny</code> clauses, but not both. They are
mutually exclusive.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>options.indexing.allow</code></p></td>
<td style="text-align: left;"><p>[array]</p></td>
<td style="text-align: left;"><p>The <code>allow</code> or
<code>deny</code> is required if <code>indexing</code> is specified. An
array of one or more properties that are indexed. Or you can enter a
wildcard <code>"allow": ["*""]</code> indicating that all properties
will be indexed during an update operation (functionally the same as the
default if <code>indexing</code> clause is not present.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>options.indexing.deny</code></p></td>
<td style="text-align: left;"><p>[array]</p></td>
<td style="text-align: left;"><p>The <code>allow</code> or
<code>deny</code> is required if <code>indexing</code> is specified. An
array of one or more properties that are not indexed. Or you can enter a
wildcard <code>"deny": ["*""]</code> indicating that no properties will
be indexed during an update operation.</p></td>
</tr>
</tbody>
</table>

    {
        "status": {
            "ok": 1
        }
    }

## The defaultId option

The Data API `defaultId` option controls how the Data API will allocate
a new `_id` for each document that does not specify a value in the
request.

For backwards compatibility with Data API releases before version 1.0.3,
if you omit a `defaultId` option on `createCollection`, a document’s
`_id` value is a plain String version of random-based UUID (version 4).

Once the collection has been created, you cannot change the `defaultId`
option (if entered).

If you include a `defaultId` option with `createCollection`, you
**must** set the `type`. The capitalization is case-sensitive. Specify
one of the following:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>objectId</code></p></td>
<td style="text-align: left;"><p>Each document’s generated
<code>_id</code> will be an <code>objectId</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>uuidv6</code></p></td>
<td style="text-align: left;"><p>Each document’s generated
<code>_id</code> will be a <a
href="https://www.ietf.org/archive/id/draft-ietf-uuidrev-rfc4122bis-14.html#name-uuid-version-6">Version
6 UUID</a>, which is field compatible with a Version 1 time uuid, but
with the ability to be lexicographically sortable.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>uuidv7</code></p></td>
<td style="text-align: left;"><p>Each document’s <code>_id</code> will
be a <a
href="https://www.ietf.org/archive/id/draft-ietf-uuidrev-rfc4122bis-14.html#name-uuid-version-7">Version
7 UUID</a>, which is designed to be a replacement for Version 1 time
uuid, and is recommended for use in new systems.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>uuid</code></p></td>
<td style="text-align: left;"><p>Each document’s generated
<code>_id</code> will be a <a
href="https://www.ietf.org/archive/id/draft-ietf-uuidrev-rfc4122bis-14.html#name-uuid-version-4">Version
4 Random UUID</a>. This type is analogous to the uuid type and functions
in Apache Cassandra®.</p></td>
</tr>
</tbody>
</table>

Example:

    {
        "createCollection": {
            "name": "vector_collection2",
            "options": {
                "defaultId": {
                    "type": "objectId"
                },
                "vector": {
                    "dimension": 1024,
                    "metric": "cosine"
                }
            }
        }
    }

When you add documents to your collection, using Data API commands such
as `insertOne` and `insertMany`, you would **not** specify an explicitly
numbered `_id` value (such as `"_id": "12"`) in the request. The server
allocates a unique value per document based on the `type` you indicated
in the `createCollection` command’s `defaultId` option.

Client apps can detect the use of `$objectId` or `$uuid` in the response
document and return to the caller the objects that represent the types
natively. In this way, client apps can use generated IDs in the methods
that are based on Data API operations such as `findOneAndUpdate`,
`updateOne`, `updateMany`.

For example, in Python, the client can specify the detected value for a
document’s `$objectId` or `$uuid`:

    # API Response with $objectId
    {
        "_id": {"$objectId": "57f00cf47958af95dca29c0c"}
        "summary": "Retrieval-Augmented Generation is the process of optimizing the output of a large language model..."
    }

    # Client returns Dict from collection.find_one()
    my_doc = {
        "_id": astrapy.ObjectId("57f00cf47958af95dca29c0c"),
        "summary": "Retrieval-Augmented Generation is the process of optimizing the output of a large language model..."
    }

    # API Response with $uuid
    {
        "_id": {"$uuid": "ffd1196e-d770-11ee-bc0e-4ec105f276b8"}
        "summary": "Retrieval-Augmented Generation is the process of optimizing the output of a large language model..."
    }

    # Client returns Dict from collection.find_one()
    my_doc = {
        "_id": UUID("ffd1196e-d770-11ee-bc0e-4ec105f276b8"),
        "summary": "Retrieval-Augmented Generation is the process of optimizing the output of a large language model..."
    }

There are many advantages when using generated `_id` values with
documents, versus relying on manually numbered `_id` values. For
example, with generated `_id` values of type `uuidv7`:

-   **Uniqueness across the database**: A generated `_id` value is
    designed to be globally unique across the entire database. This
    uniqueness is achieved through a combination of timestamp, machine
    identifier, process identifier, and a sequence number. Explicitly
    numbering documents might lead to clashes unless carefully managed,
    especially in distributed systems.

-   **Automatic generation**: The `_id` values are automatically
    generated by {product}. This means you won’t have to worry about
    creating and maintaining a unique ID system, reducing the complexity
    of the code and the risk of errors.

-   **Timestamp information**: A generated `_id` value includes a
    timestamp as its first component, representing the document’s
    creation time. This can be useful for tracking when a document was
    created without needing an additional field. In particular, type
    `uuidv7` values provide a high degree of granularity (milliseconds)
    in timestamps.

-   **Avoids manual sequence management**: Managing sequential numeric
    IDs manually can be challenging, especially in environments with
    high concurrency or distributed systems. There’s a risk of ID
    collision or the need to lock tables or sequences to generate a new
    ID, which can affect performance. Generated `_id` values are
    designed to handle these issues automatically.

While numeric `_id` values might be simpler and more human-readable, the
benefits of using generated `_id` values make it a superior choice for
most applications, especially those that have many documents.

## The indexing option

The Data API `createCollection` command includes an optional `indexing`
clause.

If you omit the `indexing` option, by default all properties in the
document are indexed when it is added or modified in the database. The
index is implemented as a [Storage-Attached Index
(SAI)](https://docs.datastax.com/en/cql/astra/docs/developing/indexing/sai/sai-overview.html),
which enables Data API queries that filter and/or sort data based on the
indexed property.

If you specify the `indexing` option when you create a collection, you
must include one (but not both) of the following: an `allow` or a `deny`
array.

### Pros and cons of selective indexing

It’s important to emphasize the pros and cons of allowing only certain
properties to be indexed. While you may want to skip indexing certain
properties to increase write-time performance, you’ll need to think
ahead — when you create the collection — about which properties will be
important to use in subsequent queries that rely on filtering and/or
sort operations. **You can only filter and/or sort the properties that
have been indexed.** Data API returns an error if you attempt to filter
or sort a non-indexed property.

The error would have one of these formats:

    UNINDEXED_FILTER_PATH("Unindexed filter path"), ...

    UNINDEXED_SORT_PATH("Unindexed sort path"), ...

    ID_NOT_INDEXED("_id is not indexed"), ...

Example:

    UNINDEXED_FILTER_PATH("Unindexed filter path: The filter path ('address.city') is not indexed)"

While weighing the pros and cons of indexed or non-indexed properties in
a document, consider the maximum size limits for those properties.
Non-indexed properties allow for a much larger quantity of data, to
accommodate data such as a blog post’s String content. In comparison,
indexed properties are appropriately bound by lower maximum size limits
to ensure efficient and performant read operations via the SAI index.

You’ll want to evaluate the pros and cons for each property in a
document, and make decisions with the `createCollection` command’s
`indexing` clause (if specified), based on the read/write and data
capacity requirements of your apps.

Of course, test your app’s performance with the database including
average and peak loads. If you need to adjust `indexing` options, try
different settings in a newly defined collection and run tests again.

### Indexing allow example

cURL example:

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
        "createCollection": {
            "name": "vector_collection",
            "options": {
                "vector": {
                    "dimension": 5,
                    "metric": "cosine"
                },
                "indexing": {
                    "allow": [
                        "property1",
                        "property2"
                    ]
                }
            }
        }
    }' | jq
    # `| jq` is optional.

In the preceding `allow` example, **only** the values of `property1` and
`property2` are included in the SAI index. No other properties are
indexed.

The net result for subsequent update operations:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><p>Property name</p></td>
<td style="text-align: left;"><p>Indexed?</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property1</code></p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property2</code></p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property3</code></p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property3.prop3a</code></p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property3.prop3b</code></p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property4</code></p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property5</code></p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property5.prop5a</code></p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property5.prop5b</code></p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property5.prop5c</code></p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
</tbody>
</table>

As a result, subsequent {astra-api} queries may perform filtering and/or
sort operations based only on `property1`, `property2`, or both.

### Indexing deny example

Now let’s take an inverse approach with an `indexing` …​ `deny` array
example in cURL:

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
        "createCollection": {
            "name": "vector_collection",
            "options": {
                "vector": {
                    "dimension": 5,
                    "metric": "cosine"
                },
                "indexing": {
                    "deny": [
                        "property1",
                        "property3",
                        "property5.prop5b"
                    ]
                }
            }
        }
    }' | jq
    # `| jq` is optional.

In the preceding example, all the properties in the document are indexed
except the ones listed in the `deny` clause.

Notice how the parent `property3` was specified, which means its
sub-properties `property3.prop3a` and `property3.prop3b` are also
**not** indexed.

However, also notice how the specific sub-property named
`property5.prop5b` was listed on the `deny` clause; which means
`property5.prop5b` is not indexed, but the parent `property5` and the
sub-properties `property5.prop5a` and `property5.prop5c` are included in
the SAI index.

The net result for subsequent update operations:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><p>Property name</p></td>
<td style="text-align: left;"><p>Indexed?</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property1</code></p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property2</code></p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property3</code></p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property3.prop3a</code></p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property3.prop3b</code></p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property4</code></p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property5</code></p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property5.prop5a</code></p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property5.prop5b</code></p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>property5.prop5c</code></p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
</tbody>
</table>

### Indexing wildcard examples

The `createCollection` command’s optional `indexing` clause provides a
convenience wildcard `["*"]` in its syntax. For example, in cURL, the
following clause means that all properties will be indexed:

    {
      "indexing": {
        "allow": ["*"]
      }
    }

The preceding example is the equivalent of omitting the `indexing`
clause. Meaning, all properties in the document will be indexed during
update operations.

You can use the wildcard character with the `deny` clause:

    {
      "indexing": {
        "deny": ["*"]
      }
    }

In the preceding example, no properties are indexed, not even `$vector`.

# List all collections

Retrieve an iterable object over collections. Unless otherwise
specified, this implementation refers to the collections in the working
namespace of the database.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/database.html#astrapy.database.Database.list\_collections\[API
Reference\].

    collection_iterable = database.list_collections()

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>namespace</p></td>
<td style="text-align: left;"><p><code>Optional[str]</code></p></td>
<td style="text-align: left;"><p>the namespace to be inspected. If not
specified, the database’s working namespace is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
underlying HTTP request.</p></td>
</tr>
</tbody>
</table>

Returns:

`{py-client-api-ref-url}/cursors.html#astrapy.cursors.CommandCursor[CommandCursor][{py-client-api-ref-url}/info.html#astrapy.info.CollectionDescriptor[CollectionDescriptor]]` -
An iterable over CollectionDescriptor objects.

    # (output below reformatted with indentation for clarity)
    # (a single example collection descriptor from the cursor is shown)
    [
        ...,
        CollectionDescriptor(
            name='my_collection',
            options=CollectionOptions(
                vector=CollectionVectorOptions(
                    dimension=3,
                    metric='dot_product'
                ),
                indexing={'allow': ['field']}
            )
        ),
        ...
    ]

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")

    coll_cursor = database.list_collections()
    coll_cursor  # this looks like: CommandCursor("https://....astra.datastax.com", alive)
    list(coll_cursor)  # [CollectionDescriptor(name='my_v_col', ...), ...]
    for coll_desc in database.list_collections():
        print(coll_desc)
    # will print:
    #   CollectionDescriptor(name='my_v_col', options=CollectionOptions(vector=CollectionVectorOptions(dimension=3, metric='dot_product', service=None)))
    #   ...

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Db.html#listCollections.listCollections-2\[API
Reference\].

    const collections = await db.listCollections();

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>options</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/ListCollectionsOptions.html[ListCollectionsOptions]</code></p></td>
<td style="text-align: left;"><p>Options regarding listing
collections.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/ListCollectionsOptions.html[ListCollectionsOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/ListCollectionsOptions.html#nameOnly[nameOnly?]</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>If true, only the name of the
collection is returned. Else, the full information for each collection
is returned. Defaults to true.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/ListCollectionsOptions.html#namespace[namespace?]</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The namespace to be inspected. If not
specified, the database’s working namespace is used.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/ListCollectionsOptions.html#maxTimeMs[maxTimeMs?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>Maximum time in milliseconds the client
should wait for the operation to complete.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<{ts-client-api-ref-url}/interfaces/FullCollectionInfo.html[FullCollectionInfo][]>` -
A promise that resolves to an array of full collection information
objects.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Get a new Db instance
    const db = new DataAPIClient('TOKEN').db('API_ENDPOINT');

    (async function () {
      // Gets full info about all collections in db
      const collections = await db.listCollections();

      for (const collection of collections) {
        console.log(`Collection '${collection.name}' has default ID type '${collection.options.defaultId?.type}'`);
      }
    })();

Java  
To access the Javadoc on those methods consult the
{javadoc-url}com/datastax/astra/client/Database.html\[Database
Javadoc\].

    // Given db Database object, list all collections
    Stream<CollectionInfo> collection = listCollections();

Returned Value:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{javadoc-url}/com/datastax/astra/client/model/CollectionInfo.html[<code>Stream&lt;CollectionInfo&gt;</code>]</p></td>
<td style="text-align: left;"><p>The definition elements of
collections.</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/database/ListCollections.java[role=include]

cURL  
    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
      "findCollections": {
        "options": {
          "explain": true
        }
      }
    }' | jq
    # `| jq` is optional.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>findCollections</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>The Data API command to find all
collections in the database. It acts as a container for all the
attributes and settings required to find collections.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options</p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Under this key, an additional setting
for <code>findCollections</code> may be specified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>explain</p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p>When set to <code>true</code>,
indicates that the command should not just retrieve the names of
collections, but also provide a brief explanation of metadata associated
with each collection. Such as whether the collection was created with
the vector option. And for each vector-enabled collection, to further
specify its dimension and metric values, and any indexing
option.</p></td>
</tr>
</tbody>
</table>

    {
        "status": {
            "collections": [
                {
                    "name": "vector_collection",
                    "options": {
                        "defaultId": {
                            "type": "objectId"
                        },
                        "vector": {
                            "dimension": 5,
                            "metric": "cosine"
                        },
                        "indexing": {
                            "allow": [
                                "*"
                            ]
                        }
                    }
                }
            ]
        }
    }

CLI  
To list all collections in a database, use the following command:

    astra db list-collections <db_name>

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>db_name</p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The name of the database</p></td>
</tr>
</tbody>
</table>

Example output:

    +---------------------+-----------+-------------+
    | Name                | Dimension | Metric      |
    +---------------------+-----------+-------------+
    | collection_simple   |           |             |
    | collection_vector   | 14        | cosine      |
    | msp                 | 1536      | dot_product |
    +---------------------+-----------+-------------+

# List collection names

Get the names of the collections as a list of strings. Unless otherwise
specified, this refers to the collections in the namespace the database
is set to use.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/database.html#astrapy.database.Database.list\_collection\_names\[API
Reference\].

    database.list_collection_names()

Get the names of the collections in a specified namespace of the
database.

    database.list_collection_names(namespace="that_other_namespace")

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>namespace</p></td>
<td style="text-align: left;"><p><code>Optional[str]</code></p></td>
<td style="text-align: left;"><p>the namespace to be inspected. If not
specified, the database’s working namespace is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
underlying HTTP request.</p></td>
</tr>
</tbody>
</table>

Returns:

`List[str]` - A list of the collection names, in no particular order.

    ['a_collection', 'another_col']

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")

    database.list_collection_names()
    # ['a_collection', 'another_col']

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Db.html#listCollections.listCollections-1\[API
Reference\].

    const collectionNames = await db.listCollections({ nameOnly: true });

Get the names of the collections in a specified namespace of the
database.

    const collectionNames = await db.listCollections({ nameOnly: true, namespace: 'NAMESPACE' });

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>options</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/ListCollectionsOptions.html[ListCollectionsOptions]</code></p></td>
<td style="text-align: left;"><p>Options regarding listing
collections.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/ListCollectionsOptions.html[ListCollectionsOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/ListCollectionsOptions.html#nameOnly[nameOnly]</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>If true, only the name of the
collection is returned. Else, the full information for each collection
is returned. Defaults to true.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/ListCollectionsOptions.html#namespace[namespace?]</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The namespace to be inspected. If not
specified, the database’s working namespace is used.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/ListCollectionsOptions.html#maxTimeMs[maxTimeMs?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>Maximum time in milliseconds the client
should wait for the operation to complete.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<string[]>` - A promise that resolves to an array of the
collection names.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Get a new Db instance
    const db = new DataAPIClient('TOKEN').db('API_ENDPOINT');

    (async function () {
      // Gets just names of all collections in db
      const collections = await db.listCollections({ nameOnly: true });

      for (const collectionName of collections) {
        console.log(`Collection '${collectionName}' exists`);
      }
    })();

Java  
To access the Javadoc on those methods consult the
{javadoc-url}com/datastax/astra/client/Database.html\[Database
Javadoc\].

    // Given db Database object, list all collections
    Stream<String> collection = listCollectionsNames();

Returned Value:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p><code>Stream&lt;String&gt;</code></p></td>
<td style="text-align: left;"><p>The names of the collections.</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/database/ListCollections.java[role=include]

cURL  
    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
      "findCollections": {
        "options": {
          "explain": true
        }
      }
    }' | jq
    # `| jq` is optional.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>findCollections</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>The Data API command to find all
collections in the database. It acts as a container for all the
attributes and settings required to find collections.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options</p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Under this key, an additional setting
for <code>findCollections</code> may be specified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>explain</p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p>When set to <code>true</code>,
indicates that the command should not just retrieve the names of
collections, but also provide a brief explanation of metadata associated
with each collection. Such as whether the collection was created with
the vector option. And for each vector-enabled collection, to further
specify its dimension and metric values, and any indexing
option.</p></td>
</tr>
</tbody>
</table>

    {
        "status": {
            "collections": [
                {
                    "name": "vector_collection",
                    "options": {
                        "defaultId": {
                            "type": "objectId"
                        },
                        "vector": {
                            "dimension": 5,
                            "metric": "cosine"
                        },
                        "indexing": {
                            "allow": [
                                "*"
                            ]
                        }
                    }
                }
            ]
        }
    }

CLI  
To list all collections in a database, use the following command:

    astra db list-collections <db_name> | cut -b 1-23

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>db_name</p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The name of the database</p></td>
</tr>
</tbody>
</table>

Example output:

    +---------------------+
    | Name                |
    +---------------------+
    | collection_simple   |
    | collection_vector   |
    | msp                 |
    +---------------------+

# Get a collection

Get a reference to an existing collection.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/database.html#astrapy.database.Database.get\_collection\[API
Reference\].

    collection = database.get_collection("vector_collection")

The example above is equivalent to these two alternate notations:

    collection1 = database["vector_collection"]
    collection2 = database.vector_collection

The `get_collection` method will return a `Collection` object even for
collections that don’t exist, so make sure the collection exists first.
Your responsibility is to know which collections exist, because the
`get_collection` method does not check for you.

Most `astrapy` objects have an asynchronous counterpart, for use within
the `asyncio` framework. To get an `AsyncCollection`, use the
`get_collection` method of instances of `AsyncDatabase`, or
alternatively the `to_async` method of the synchronous `Collection`
class.

See the
{py-client-api-ref-url}/collection.html#astrapy.collection.AsyncCollection\[AsyncCollection\]
API reference for details about the async API.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>name</p></td>
<td style="text-align: left;"><p><code>str</code></p></td>
<td style="text-align: left;"><p>The name of the collection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>namespace</p></td>
<td style="text-align: left;"><p><code>Optional[str]</code></p></td>
<td style="text-align: left;"><p>The namespace containing the
collection. If no namespace is specified, the general setting for this
database is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>embedding_api_key</p></td>
<td style="text-align: left;"><p><code>Optional[str]</code></p></td>
<td style="text-align: left;"><p>An optional API key that is passed to
the Data API with each request in the form of an
<code>x-embedding-api-key</code> HTTP header.</p>
<p>If you instantiated the collection with
<code>embedding_api_key</code> or specified <code>authentication</code>
in the service configuration, then the client uses that key. You can use
this optional parameter to pass a different key, if needed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>collection_max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A default timeout, in milliseconds, for
the duration of each operation on the collection. Individual timeouts
can be provided to each collection method call and will take precedence,
with this value being an overall default. Note that for some methods
involving multiple API calls (such as <code>delete_many</code> and
<code>insert_many</code>), you should provide a timeout with sufficient
duration for the operation you’re performing.</p></td>
</tr>
</tbody>
</table>

Returns:

`{py-client-api-ref-url}/collection.html#astrapy.collection.Collection[Collection]` -
An instance of the Collection class corresponding to the specified
collection name.

    Collection(name="vector_collection", namespace="default_keyspace", database=Database(api_endpoint="https://01234567-89ab-cdef-0123-456789abcdef-us-east1.apps.astra.datastax.com", token="AstraCS:aAbB...", namespace="default_keyspace"))

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")

    collection = database.get_collection("my_collection")
    collection.count_documents({}, upper_bound=100)  # will print e.g.: 41

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Db.html#collection\[API Reference\].

    const collection = db.collection('COLLECTION');

The `collection` method will return a `Collection` object even for
collections that don’t exist, so make sure the collection exists first.
Your responsibility is to know which collections exist, because the
`collection` method does not check for you.

A `Collection` is typed as `Collection<Schema>` where `Schema` is the
type of the documents in the collection. Operations on the collection
will be strongly typed if a specific schema is provided, otherwise
remained largely weakly typed if no type is provided, which may be
preferred for dynamic data access & operations. It’s up to the user to
ensure that the provided type truly represents the documents in the
collection.

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>collectionName</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The name of the collection to
create.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/CollectionSpawnOptions.html#embeddingsApiKey[embeddingApiKey?]</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>An alternative to
<code>service.authentication.providerKey</code> for the embeddings
provider. Provide the API key directly instead of using an API key in
the {astra_db} KMS. <code>embeddingApiKey</code> overrides the
{astra_db} KMS API key if you set both.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/WithNamespace.html[WithNamespace]</code></p></td>
<td style="text-align: left;"><p>Allows you to override which namespace
to use for the collection.</p></td>
</tr>
</tbody>
</table>

Returns:

`{ts-client-api-ref-url}/classes/Collection.html[Collection<Schema>]` -
An unverified reference to the collection.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Get a new Db instance
    const db = new DataAPIClient('TOKEN').db('API_ENDPOINT');

    // Define the schema for the collection
    interface User {
      name: string,
      age?: number,
    }

    (async function () {
      // Basic untyped collection
      const users1 = db.collection('users');
      await users1.insertOne({ name: 'John' });

      // Typed collection from different namespace with a specific embedding API key
      const users2 = db.collection<User>('users', {
        namespace: 'NAMESPACE',
        embeddingApiKey: 'EMBEDDINGS_API_KEY',
      });
      await users2.insertOne({ name: 'John' });
    })();

See also: {ts-client-api-ref-url}/types/SomeDoc.html\[SomeDoc\],
{ts-client-api-ref-url}/interfaces/VectorDoc.html\[VectorDoc\]

Java  
To access the Javadoc on those methods consult the
{javadoc-url}com/datastax/astra/client/Database.html\[Database
Javadoc\].

    // Given db Database object, list all collections
    Collection<Document> collection = db.getCollection("collection_name");

    // Gather collection information
    CollectionOptions options = collection.getOptions();

Returned Value:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{javadoc-url}/com/datastax/astra/client/model/CollectionInfo.html[<code>CollectionOptions</code>]</p></td>
<td style="text-align: left;"><p>The Collection with all metadata
(defaultId, vector, indexing) for the collection.</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/database/FindCollection.java[role=include]

# Drop a collection

Drop (delete) a collection from a database, erasing all data stored in
it as well.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/database.html#astrapy.database.Database.drop\_collection\[API
Reference\].

    result = db.drop_collection(name_or_collection="vector_collection")

Calling this method is equivalent to invoking the collection’s own
method `collection.drop()`. In that case, trying to use the object
afterwards would result in an API error, as it will have become a
reference to a non-existent collection.

Parameters:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>name_or_collection</p></td>
<td
style="text-align: left;"><p><code>Union[str, Collection]</code></p></td>
<td style="text-align: left;"><p>either the name of a collection or a
<code>Collection</code> instance.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
underlying HTTP request.</p></td>
</tr>
</tbody>
</table>

Returns:

`Dict` - A dictionary in the form `{"ok": 1}` if the method succeeds.

    {'ok': 1}

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")

    database.list_collection_names()
    # prints: ['a_collection', 'my_v_col', 'another_col']
    database.drop_collection("my_v_col")  # {'ok': 1}
    database.list_collection_names()
    # prints: ['a_collection', 'another_col']

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Db.html#dropCollection\[API Reference\].

    const ok = await db.dropCollection('COLLECTION');

Calling this method is equivalent to invoking the collection’s own
method `collection.drop()`. In that case, trying to use the object
afterward would result in an API error, as it will have become a
reference to a non-existent collection.

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>name</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The name of the collection to
delete.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/DropCollectionOptions.html[DropCollectionOptions]</code></p></td>
<td style="text-align: left;"><p>Allows you to override the namespace
&amp; set a <code>maxTimeMs</code>.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/DropCollectionOptions.html[DropCollectionOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DropCollectionOptions.html#namespace[namespace?]</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The namespace containing the
collection. If not specified, the database’s working namespace is
used.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DropCollectionOptions.html#maxTimeMS[maxTimeMS?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>Maximum time in milliseconds the client
should wait for the operation to complete.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<boolean>` - A promise that resolves to true if the collection
was dropped successfully.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Get a new Db instance
    const db = new DataAPIClient('TOKEN').db('API_ENDPOINT');

    (async function () {
      // Uses db's default namespace
      const success1 = await db.dropCollection('users');
      console.log(success1); // true

      // Overrides db's default namespace
      const success2 = await db.dropCollection('users', {
        namespace: 'NAMESPACE'
      });
      console.log(success2); // true
    })();

Java  
To access the Javadoc on those methods consult the
{javadoc-url}com/datastax/astra/client/Database.html\[Database
Javadoc\].

    // Given db Database object, list all collections
    void db.dropCollection("collectionName");

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>collectionName</code></p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The name of the collection to
delete.</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/database/DropCollection.java[role=include]

cURL  
    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
      "deleteCollection": {
        "name": "vector_collection"
      }
    }' | jq
    # `| jq` is optional.

    {
        "status": {
            "ok": 1
        }
    }

Parameter:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The name of the collection to
delete.</p></td>
</tr>
</tbody>
</table>

# See also

-   [api-reference:overview.xml](api-reference:overview.xml)

-   [api-reference:dataapiclient.xml](api-reference:dataapiclient.xml)

-   [api-reference:databases.xml](api-reference:databases.xml)

-   [api-reference:documents.xml](api-reference:documents.xml)

-   [api-reference:administration.xml](api-reference:administration.xml)

-   [Data API
    changelog](https://github.com/stargate/data-api/blob/main/CHANGELOG.md)
    = Documents reference :navtitle: Documents :page-toclevels: 2

Documents represent a single row or record of data in {product}.

Use the `Collection` class to work with documents.

If you haven’t already, consult the [Collections
reference](api-reference:collections.xml) topic for details on how to
get a `Collection` object.

# Working with dates

Python  
Date and datetime objects, which are instances of the Python standard
library `datetime.datetime` and `datetime.date` classes, can be used
anywhere in documents.

    import datetime

    from astrapy import DataAPIClient
    from astrapy.ids import ObjectId, uuid8, UUID
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    collection.insert_one({"when": datetime.datetime.now()})
    collection.insert_one({"date_of_birth": datetime.date(2000, 1, 1)})

    collection.update_one(
        {"registered_at": datetime.date(1999, 11, 14)},
        {"$set": {"message": "happy Sunday!"}},
    )

    print(
        collection.find_one(
            {"date_of_birth": {"$lt": datetime.date(2001, 1, 1)}},
            projection={"_id": False},
        )
    )
    # will print:
    #    {'date_of_birth': datetime.datetime(2000, 1, 1, 0, 0)}

As shown in the example, read operations from a collection always return
the `datetime` class regardless of whether a `date` or a `datetime` was
provided in the insertion.

TypeScript  
Native JS `Date` objects can be used anywhere in documents to represent
dates and times.

Document fields stored using the `{ $date: number }` will also be
returned as `Date` objects when read.

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });

    (async function () {
      // Create an untyped collection
      const collection = await db.createCollection('dates_test', { checkExists: false });

      // Insert documents with some dates
      await collection.insertOne({ dateOfBirth: new Date(1394104654000) });
      await collection.insertOne({ dateOfBirth: new Date('1863-05-28') });

      // Update a document with a date and setting lastModified to now
      await collection.updateOne(
        {
          dateOfBirth: new Date('1863-05-28'),
        },
        {
          $set: { message: 'Happy Birthday!' },
          $currentDate: { lastModified: true },
        },
      );

      // Will print around new Date()
      const found = await collection.findOne({ dateOfBirth: { $lt: new Date('1900-01-01') } });
      console.log(found?.lastModified);
    })();

Java  
Data API is using the `ejson` standard to represents time-related
objects. The client introducing custom serializers but 3 types of
objects `java.util.Date`, `java.util.Calendar`, `java.util.Instant`.

Those objects can be used naturally both in filter clauses, update
clauses and or in documents.

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/WorkingWithDates.java[role=include]

cURL  
In the JSON payload of the following Data API `insertOne` command,
`$date` is used to specify a car’s purchase date:

    "purchase_date": {"$date": 1690045891}

Example:

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
      "insertOne": {
        "document": {
          "_id": "1",
          "purchase_type": "Online",
          "$vector": [0.25, 0.25, 0.25, 0.25, 0.25],
          "customer": {
            "name": "Jim A.",
            "phone": "123-456-1111",
            "age": 51,
            "credit_score": 782,
            "address": {
              "address_line": "1234 Broadway",
              "city": "New York",
              "state": "NY"
            }
          },
          "purchase_date": {"$date": 1690045891},
          "seller": {
            "name": "Jon B.",
            "location": "Manhattan NYC"
          },
          "items": [
            {
              "car": "BMW 330i Sedan",
              "color": "Silver"
            },
            "Extended warranty - 5 years"
          ],
          "amount": 47601,
          "status": "active",
          "preferred_customer": true
        }
      }
    }' | jq
    # | jq is optional.

    {
        "status": {
            "insertedIds": [
                "1"
            ]
        }
    }

# Working with document IDs

Documents in a collection are always identified by an ID that is unique
within the collection. The ID can be any of several types, such as a
string, integer, or datetime. However, it’s recommended to instead
prefer the `uuid` or the `ObjectId` types.

The Data API supports `uuid` identifiers up to version 8, as well as
`ObjectId` identifiers as provided by the `bson` library. These can
appear anywhere in the document, not only in its `_id` field. Moreover,
different types of identifier can appear in different parts of the same
document. And these identifiers can be part of filtering clauses and
update/replace directives just like any other data type.

One of the optional settings of a collection is the "default ID type":
that is, it is possible to specify what kind of identifiers the server
should supply for documents without an explicit `_id` field. (For
details, see the `create_collection` method and Data API
`createCollection` command in the [Collections
reference](api-reference:collections.xml#create-a-collection).)
Regardless of the `defaultId` setting, however, identifiers of any type
can be explicitly provided for documents at any time and will be honored
by the API, for example when inserting documents.

Python  
    from astrapy.ids import (
        ObjectId,
        uuid1,
        uuid3,
        uuid4,
        uuid5,
        uuid6,
        uuid7,
        uuid8,
        UUID,
    )

AstraPy recognizes `uuid` versions 1 through 8 (with the exception of 2)
as provided by the `uuid` and `uuid6` Python libraries, as well as the
`ObjectId` from the `bson` package. Furthermore, out of convenience,
these same utilities are exposed in AstraPy directly, as shown in the
example above.

You can then generate new identifiers with statements such as
`new_id = uuid8()` or `new_obj_id = ObjectId()`. Keep in mind that all
`uuid` versions are instances of the same class (`UUID`), which exposes
a `version` property, should you need to access it.

Here is a short example:

    from astrapy import DataAPIClient
    from astrapy.ids import ObjectId, uuid8, UUID
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    collection.insert_one({"_id": uuid8(), "tag": "new_id_v_8"})
    collection.insert_one(
        {"_id": UUID("018e77bc-648d-8795-a0e2-1cad0fdd53f5"), "tag": "id_v_8"}
    )
    collection.insert_one({"id": ObjectId(), "tag": "new_obj_id"})
    collection.insert_one(
        {"id": ObjectId("6601fb0f83ffc5f51ba22b88"), "tag": "obj_id"}
    )
    collection.find_one_and_update(
        {"_id": ObjectId("6601fb0f83ffc5f51ba22b88")},
        {"$set": {"item_inventory_id": UUID("1eeeaf80-e333-6613-b42f-f739b95106e6")}},
    )

TypeScript  
    import { UUID, ObjectId } from '@datastax/astra-db-ts';

astra-db-ts provides the `UUID` and `ObjectId` classes for using and
generating new identifiers. Note that these are *not* the same as
exported from the `bson` or `uuid` libraries, but rather are custom
classes that must be imported from the `astra-db-ts` package.

You can generate new identifiers using `UUID.v4()`, `UUID.v7()`, or
`new ObjectId()`. The UUID methods all return an instance of the same
class, but it exposes a `version` property, should you need to access
it. They may also be constructed from a string representation of the IDs
if custom generation is desired.

Here is a short example of the concepts:

    import { DataAPIClient, UUID, ObjectId } from '@datastax/astra-db-ts';

    // Schema for the collection
    interface Person {
      _id: UUID | ObjectId;
      name: string;
      friendId?: UUID;
    }

    // Reference the DB instance
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });

    (async function () {
      // Create the collection
      const collection = await db.createCollection<Person>('people', { checkExists: false });

      // Insert documents w/ various IDs
      await collection.insertOne({ name: 'John', _id: UUID.v4() });
      await collection.insertOne({ name: 'Jane', _id: new UUID('016b1cac-14ce-660e-8974-026c927b9b91') });

      await collection.insertOne({ name: 'Dan', _id: new ObjectId()});
      await collection.insertOne({ name: 'Tim', _id: new ObjectId('65fd9b52d7fabba03349d013') });

      // Update a document with a UUID in a non-_id field
      await collection.updateOne(
        { name: 'John' },
        { $set: { friendId: new UUID('016b1cac-14ce-660e-8974-026c927b9b91') } },
      );

      // Find a document by a UUID in a non-_id field
      const john = await collection.findOne({ name: 'John' });
      const jane = await collection.findOne({ _id: john!.friendId });

      // Prints 'Jane 016b1cac-14ce-660e-8974-026c927b9b91 6'
      console.log(jane?.name, jane?._id.toString(), (<UUID>jane?._id).version);
    })();

Java  
-   To cope with different implementations of `UUID` (v6 and v7
    especially) dedicated classes have been defined.

-   When an unique identifier is retrieved from the server, it is
    returned as a `uuid` and will be converted to the appropriate `UUID`
    class leveraging the class definition in the `defaultId` option.

-   The `ObjectId` classes is extracted from the Bson package and is
    used to represent the `ObjectId` type.

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/WorkingWithDocumentIds.java[role=include]

Java natural `UUID` are implemented the UUID v4 standard.

cURL  
The same underlying ID functionality as noted for the clients applies
when using `_id` types with Data API commands.

The following example creates a collection with a `defaultId` type. For
more information about the `defaultId` option on the `createCollection`
command, see [The defaultId
option](api-reference:collections.xml#the-defaultid-option).

    {
        "createCollection": {
            "name": "vector_collection2",
            "options": {
                "defaultId": {
                    "type": "objectId"
                },
                "vector": {
                    "dimension": 1024,
                    "metric": "cosine"
                }
            }
        }
    }

    {
        "status": {
            "ok": 1
        }
    }

You can also insert documents with different ID types specified.

Insert document with `$objectId`:

    {
        "insertOne": {
            "document": {
                "_id": {
                    "$objectId": "6672e1cbd7fabb4e5493916f"
                },
                "key": "value"
            }
        }
    }

    {
        "status": {
            "insertedIds": [
                {
                    "$objectId": "6672e1cbd7fabb4e5493916f"
                }
            ]
        }
    }

Insert one document with `$uuid`:

    {
        "insertOne": {
            "document": {
                "_id": {
                    "$uuid": "1ef2e42c-1fdb-6ad6-aae4-e84679831739"
                },
                "key": "value"
            }
        }
    }

    {
        "status": {
            "insertedIds": [
                {
                    "$uuid": "1ef2e42c-1fdb-6ad6-aae4-e84679831739"
                }
            ]
        }
    }

# Insert a single document

Insert a single document into a collection.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.insert\_one\[API
Reference\].

    insert_result = collection.insert_one({"name": "Jane Doe"})

Insert a document with an associated vector.

    insert_result = collection.insert_one(
        {
          "name": "Jane Doe",
          "$vector": [.08, .68, .30],
        },
    )

Insert a document and generate a vector automatically.

    insert_result = collection.insert_one(
        {
          "name": "Jane Doe",
          "$vectorize": "Text to vectorize",
        },
    )

Returns:

`{py-client-api-ref-url}/results.html#astrapy.results.InsertOneResult[InsertOneResult]` -
An object representing the response from the database after the insert
operation. It includes information about the success of the operation
and details of the inserted documents.

    InsertOneResult(raw_results=[{'status': {'insertedIds': ['92b4c4f4-db44-4440-b4c4-f4db44e440b8']}}], inserted_id='92b4c4f4-db44-4440-b4c4-f4db44e440b8')

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>document</p></td>
<td style="text-align: left;"><p><code>Dict</code></p></td>
<td style="text-align: left;"><p>The dictionary expressing the document
to insert. The <code>_id</code> field of the document can be left out,
in which case it will be created automatically. The document may contain
the <code>$vector</code> or the <code>$vectorize</code> fields, but not
both.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
underlying HTTP request. If not passed, the collection-level setting is
used instead.</p></td>
</tr>
</tbody>
</table>

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    # Insert a document with a specific ID
    response1 = collection.insert_one(
        {
            "_id": 101,
            "name": "John Doe",
            "$vector": [.12, .52, .32],
        },
    )

    # Insert a document without specifying an ID
    # so that _id is generated automatically
    response2 = collection.insert_one(
        {
            "name": "Jane Doe",
            "$vector": [.08, .68, .30],
        },
    )

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#insertOne\[API
Reference\].

    const result = await collection.insertOne({ name: 'Jane Doe' });

Insert a document with an associated vector.

    const result = await collection.insertOne({
      name: 'Jane Doe',
      $vector: [.08, .68, .30],
    });

Insert a document and generate a vector automatically.

    const result = await collection.insertOne({
      name: 'Jane Doe',
      $vectorize: 'Text to vectorize',
    });

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>document</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/MaybeId.html[MaybeId&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>The document to insert. If the document
does not have an <code>_id</code> field, the server generates one. It
may contain a <code>$vector</code> or <code>$vectorize</code> field to
enable semantic searching.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/InsertOneOptions.html[InsertOneOptions]</code></p></td>
<td style="text-align: left;"><p>The options for this
operation.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/InsertOneOptions.html[InsertOneOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/InsertOneOptions.html#maxTimeMS[maxTimeMS?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>The maximum time in milliseconds that
the client should wait for the operation to complete.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<{ts-client-api-ref-url}/interfaces/InsertOneResult.html[InsertOneResult<Schema>]>` -
A promise that resolves to the inserted ID.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      // Insert a document with a specific ID
      await collection.insertOne({ _id: '1', name: 'John Doe' });

      // Insert a document with an autogenerated ID
      await collection.insertOne({ name: 'Jane Doe' });

      // Insert a document with a vector
      await collection.insertOne({ name: 'Jane Doe', $vector: [.12, .52, .32] });
    })();

Java  
-   Operations on documents are performed at `Collection` level, to get
    details on each signature you can access the [Collection
    JavaDOC](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/Collection.html).

-   Collection is a generic class, default type is `Document` but you
    can specify your own type and the object will be serialized by
    Jackson.

-   Most methods come with synchronous and asynchronous flavors where
    the asynchronous version will be suffixed by `Async` and return a
    `CompletableFuture`.

    InsertOneResult insertOne(DOC document);
    InsertOneResult insertOne(DOC document, float[] embeddings);

    // Equivalent in asynchronous
    CompletableFuture<InsertOneResult> insertOneAsync(DOC document);
    CompletableFuture<InsertOneResult> insertOneAsync(DOC document, float[] embeddings);

Returns:

[`InsertOneResult`](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/InsertOneResult.html) -
Wrapper with the inserted document Id.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>document</code></p></td>
<td style="text-align: left;"><p><code>DOC</code></p></td>
<td style="text-align: left;"><p>Object representing the document to
insert. The <code>_id</code> field of the document can be left out, in
which case it will be created automatically. If the collection is
associated with an embedding service, it will generate a vector
automatically from the <code>$vectorize</code> field.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>embeddings</code></p></td>
<td style="text-align: left;"><p><code>float[]</code></p></td>
<td style="text-align: left;"><p>A vector of embeddings (a list of
numbers appropriate for the collection) for the document. Passing this
parameter is equivalent to providing the vector in the
<code>$vector</code> field of the document itself.</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/InsertOne.java[role=include]

cURL  
    cURL -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
      "insertOne": {
        "document": {
          "_id": "1",
          "purchase_type": "Online",
          "$vector": [0.25, 0.25, 0.25, 0.25, 0.25],
          "customer": {
            "name": "Jim A.",
            "phone": "123-456-1111",
            "age": 51,
            "credit_score": 782,
            "address": {
              "address_line": "1234 Broadway",
              "city": "New York",
              "state": "NY"
            }
          },
          "purchase_date": {"$date": 1690045891},
          "seller": {
            "name": "Jon B.",
            "location": "Manhattan NYC"
          },
          "items": [
            {
              "car": "BMW 330i Sedan",
              "color": "Silver"
            },
            "Extended warranty - 5 years"
          ],
          "amount": 47601,
          "status": "active",
          "preferred_customer": true
        }
      }
    }' | jq
    # `| jq` is optional.

Properties:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>insertOne</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>Data API designation that a single
document is inserted.</p>
<p><a
href="api-reference:partial$insert-command-payload.adoc">api-reference:partial$insert-command-payload.adoc</a></p></td>
</tr>
</tbody>
</table>

    {
        "status": {
            "insertedIds": [
                "1"
            ]
        }
    }

# Insert many documents

Insert multiple documents into a collection.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.insert\_many\[API
Reference\].

    response = collection.insert_many(
        [
            {
                "_id": 101,
                "name": "John Doe",
                "$vector": [.12, .52, .32],
            },
            {
                # ID is generated automatically
                "name": "Jane Doe",
                "$vector": [.08, .68, .30],
            },
        ],
    )

Insert multiple documents and generate vectors automatically.

    response = collection.insert_many(
        [
            {
                "name": "John Doe",
                "$vectorize": "Text to vectorize for John Doe",
            },
            {
                "name": "Jane Doe",
                "$vectorize": "Text to vectorize for Jane Doe",
            },
        ],
    )

Returns:

`{py-client-api-ref-url}/results.html#astrapy.results.InsertManyResult[InsertManyResult]` -
An object representing the response from the database after the insert
operation. It includes information about the success of the operation
and details of the inserted documents.

    InsertManyResult(raw_results=[{'status': {'insertedIds': [101, '81077d86-05dc-43ca-877d-8605dce3ca4d']}}], inserted_ids=[101, '81077d86-05dc-43ca-877d-8605dce3ca4d'])

Parameters:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 40%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>documents</p></td>
<td
style="text-align: left;"><p><code>Iterable[Dict[str, Any]],</code></p></td>
<td style="text-align: left;"><p>An iterable of dictionaries, each a
document to insert. Documents may specify their <code>_id</code> field
or leave it out, in which case it will be added automatically. Each
document may contain the <code>$vector</code> or the
<code>$vectorize</code> fields, but not both.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>ordered</p></td>
<td style="text-align: left;"><p><code>bool</code></p></td>
<td style="text-align: left;"><p>If False (default), the insertions can
occur in arbitrary order and possibly concurrently. If True, they are
processed sequentially. If you don’t need ordered inserts, DataStax
recommends setting this parameter to False for faster
performance.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>chunk_size</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>How many documents to include in a
single API request. The default is 50, and the maximum is 100.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>concurrency</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>Maximum number of concurrent requests
to the API at a given time. It cannot be more than one for ordered
insertions.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
operation. If not passed, the collection-level setting is used instead:
If you are inserting many documents, this method will require multiple
HTTP requests. You may need to increase the timeout duration for the
method to complete successfully.</p></td>
</tr>
</tbody>
</table>

Unless there are specific reasons not to, it is recommended to prefer
`ordered = False` as it will result in a much higher insert throughput
than an equivalent ordered insertion.

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    collection.insert_many([{"a": 10}, {"a": 5}, {"b": [True, False, False]}])

    collection.insert_many(
        [{"seq": i} for i in range(50)],
        concurrency=5,
    )

    collection.insert_many(
        [
            {"tag": "a", "$vector": [1, 2]},
            {"tag": "b", "$vector": [3, 4]},
        ]
    )

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#insertMany\[API
Reference\].

    const result = await collection.insertMany([
      {
        _id: '1',
        name: 'John Doe',
        $vector: [.12, .52, .32],
      },
      {
        name: 'Jane Doe',
        $vector: [.08, .68, .30],
      },
    ], {
      ordered: true,
    });

Insert multiple documents and generate vectors automatically.

    const result = await collection.insertMany([
      {
        name: 'John Doe',
        $vectorize: 'Text to vectorize for John Doe',
      },
      {
        name: 'Jane Doe',
        $vectorize: 'Text to vectorize for Jane Doe',
      },
    ], {
      ordered: true,
    });

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>documents</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/MaybeId.html[MaybeId&lt;Schema&gt;][]</code></p></td>
<td style="text-align: left;"><p>The documents to insert. If any
document does not have an <code>_id</code> field, the server generates
one. They may each contain a <code>$vector</code> or
<code>$vectorize</code> field to enable semantic searching.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/InsertManyOptions.html[InsertManyOptions]</code></p></td>
<td style="text-align: left;"><p>The options for this
operation.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/types/InsertManyOptions.html[InsertManyOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/InsertManyUnorderedOptions.html#ordered[ordered?]</p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>You may set the <code>ordered</code>
option to <code>true</code> to stop the operation after the first error;
otherwise all documents may be parallelized and processed in arbitrary
order, improving, perhaps vastly, performance.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/InsertManyUnorderedOptions.html#concurrency[concurrency?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>You can set the
<code>concurrency</code> option to control how many network requests are
made in parallel on unordered insertions. Defaults to
<code>8</code>.</p>
<p>Not available for ordered insertions.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/InsertManyUnorderedOptions.html#chunkSize[chunkSize?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>Control how many documents are sent
with each network request. The default is 50, and the maximum is
100.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/InsertManyUnorderedOptions.html#maxTimeMS[maxTimeMS?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>The maximum time in milliseconds that
the client should wait for the operation to complete.</p></td>
</tr>
</tbody>
</table>

Unless there are specific reasons not to, it is recommended to prefer to
leave ordered `false` as it will result in a much higher insert
throughput than an equivalent ordered insertion.

Returns:

`Promise<{ts-client-api-ref-url}/interfaces/InsertManyResult.html[InsertManyResult<Schema>]>` -
A promise that resolves to the inserted IDs.

Example:

    import { DataAPIClient, InsertManyError } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      try {
        // Insert many documents
        await collection.insertMany([
          { _id: '1', name: 'John Doe' },
          { name: 'Jane Doe' }, // Will autogen ID
        ], { ordered: true });

        // Insert many with vectors
        await collection.insertMany([
          { name: 'John Doe', $vector: [.12, .52, .32] },
          { name: 'Jane Doe', $vector: [.32, .52, .12] },
        ]);
      } catch (e) {
        if (e instanceof InsertManyError) {
          console.log(e.partialResult);
        }
      }
    })();

Java  
-   Operations on documents are performed at `Collection` level, to get
    details on each signature you can access the [Collection
    JavaDOC](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/Collection.html).

-   Collection is a generic class, default type is `Document` but you
    can specify your own type and the object will be serialized by
    Jackson.

-   Most methods come with synchronous and asynchronous flavors where
    the asynchronous version will be suffixed by `Async` and return a
    `CompletableFuture`.

    // Synchronous
    InsertManyResult insertMany(List<? extends DOC> documents);
    InsertManyResult insertMany(List<? extends DOC> documents, InsertManyOptions options);

    // Asynchronous
    CompletableFuture<InsertManyResult> insertManyAsync(List<? extends DOC> docList);
    CompletableFuture<InsertManyResult> insertManyAsync(List<? extends DOC> docList, InsertManyOptions options);

Returns:

[`InsertManyResult`](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/InsertManyResult.html) -
Wrapper with the list of inserted document ids.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>docList</code></p></td>
<td
style="text-align: left;"><p><code>List&lt;? extends DOC&gt;</code></p></td>
<td style="text-align: left;"><p>A list of documents to insert.
Documents may specify their <code>_id</code> field or leave it out, in
which case it will be added automatically. If the collection is
associated with an embedding service, it will generate vectors
automatically from the <code>$vectorize</code> field in each document.
You can also set the <code>$vector</code> field directly.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>options</code>
(optional)</p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/InsertManyOptions.html"><code>InsertManyOptions</code></a></p></td>
<td style="text-align: left;"><p>Set the different options for the
insert operation. The options are <code>ordered</code>,
<code>concurrency</code>, <code>chunkSize</code>.</p></td>
</tr>
</tbody>
</table>

The java operation `insertMany` can take as many documents as you want
as long as it fits in your JVM memory. It will split the documents in
chunks of `chunkSize` and send them to the server in a distributed way
through an `ExecutorService`. The default value of `chunkSize` is 50,
and the maximum value is 100. To set the size of the executor use
`concurrency.`

    InsertManyOptions.Builder
      .chunkSize(20)  // batch size, 100 is max
      .concurrency(8) // concurrent insertions
      .ordered(false) // unordered insertions
      .build();

If not provided the default values are `chunkSize=20`, `concurrency=1`
and `ordered=false`.

-   It is recommended to work with `ordered=false` for performance
    reasons. It would then insert chunks in parallels.

-   Try to always provide the `InsertManyOptions` even when using
    default, it brings visibility to the readers.

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/InsertMany.java[role=include]

cURL  
The API accepts up to 100 documents per request.

The following Data API `insertMany` command adds 20 documents to a
collection.

    cURL -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
      "insertMany": {
        "documents": [
          {
            "_id": "2",
            "purchase_type": "Online",
            "$vector": [0.1, 0.15, 0.3, 0.12, 0.05],
            "customer": {
              "name": "Jack B.",
              "phone": "123-456-2222",
            "age": 34,
            "credit_score": 700,
              "address": {
                "address_line": "888 Broadway",
                "city": "New York",
                "state": "NY"
              }
            },
            "purchase_date": {"$date": 1690391491},
            "seller": {
              "name": "Tammy S.",
              "location": "Staten Island NYC"
            },
            "items": [
                {
              "car": "Tesla Model 3",
              "color": "White"
                },
                "Extended warranty - 10 years",
                "Service - 5 years"
            ],
            "amount": 53990,
          "status": "active"
          },
          {
            "_id": "3",
            "purchase_type": "Online",
            "$vector": [0.15, 0.1, 0.1, 0.35, 0.55],
            "customer": {
              "name": "Jill D.",
              "phone": "123-456-3333",
            "age": 30,
            "credit_score": 742,
              "address": {
                "address_line": "12345 Broadway",
                "city": "New York",
                "state": "NY"
              }
            },
            "purchase_date": {"$date": 1690564291},
            "seller": {
              "name": "Jasmine S.",
              "location": "Brooklyn NYC"
            },
            "items": "Extended warranty - 10 years",
            "amount": 4600,
          "status": "active"
          },
    // Example truncated for brevity
          {
            "_id": "21",
            "purchase_type": "In Person",
            "$vector": [0.21, 0.22, 0.33, 0.44, 0.53],
            "customer": {
              "name": "Rachel I.",
              "phone": null,
            "age": 62,
            "credit_score": 786,
              "address": {
                "address_line": "1234 Park Ave",
                "city": "New York",
                "state": "NY"
              }
            },
            "purchase_date": {"$date": 1706202691},
            "seller": {
              "name": "Jon B.",
              "location": "Manhattan NYC"
            },
            "items": [{
              "car": "BMW M440i Gran Coupe",
              "color": "Silver"
                },
                "Extended warranty - 5 years",
                "Gap Insurance - 5 years"
            ],
            "amount": 65250,
          "status": "active"
          }
        ],
        "options": {
            "ordered": false
        }
      }
    }' | jq
    # `| jq` is optional.

    {
       "status": {
          "insertedIds": [
             "4",
             "7",
             "10",
             "13",
             "16",
             "19",
             "21",
             "18",
             "6",
             "12",
             "15",
             "9",
             "3",
             "11",
             "2",
             "17",
             "14",
             "8",
             "20",
             "5"
          ]
       }
    }

Properties:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>insertMany</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>Data API designation that many
documents are being inserted. You can insert up to 100 documents at a
time.</p>
<p><a
href="api-reference:partial$insert-command-payload.adoc">api-reference:partial$insert-command-payload.adoc</a></p></td>
</tr>
</tbody>
</table>

# Find a document

Retrieve a single document from a collection using various options.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.find\_one\[API
Reference\].

Retrieve a single document from a collection by its `_id`.

    document = collection.find_one({"_id": 101})

Retrieve a single document from a collection by any attribute, as long
as it is covered by the collection’s indexing configuration.

As noted in [The Indexing
option](api-reference:collections.xml#the-indexing-option) in the
Collections reference topic, any field that is part of a subsequent
filter or sort operation must be an indexed field. If you elected to not
index certain or all fields when you created the collection, you cannot
reference that field in a filter/sort query.

    document = collection.find_one({"location": "warehouse_C"})

Retrieve a single document from a collection by an arbitrary filtering
clause.

    document = collection.find_one({"tag": {"$exists": True}})

Retrieve the most similar document to a given vector.

    result = collection.find_one({}, sort={"$vector": [.12, .52, .32]})

Generate a vector and retrieve the most similar document.

    result = collection.find_one({}, sort={"$vectorize": "Text to vectorize"})

Retrieve only specific fields from a document.

    result = collection.find_one({"_id": 101}, projection={"name": True})

Returns:

`Union[Dict[str, Any], None]` - Either the found document as a
dictionary or None if no matching document is found.

    {'_id': 101, 'name': 'John Doe', '$vector': [0.12, 0.52, 0.32]}

Parameters:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>projection</p></td>
<td
style="text-align: left;"><p><code>Optional[Union[Iterable[str], Dict[str, bool]]]</code></p></td>
<td style="text-align: left;"><p>Used to select a subset of fields in
the documents being returned. The projection can be: an iterable over
the included field names; a dictionary {field_name: True} to positively
select certain fields; or a dictionary {field_name: False} if one wants
to exclude specific fields from the response. Special document fields
(e.g. <code>_id</code>, <code>$vector</code>) are controlled
individually. The default projection does not necessarily include all
fields of the document. See the <a
href="api-reference:documents.xml#example-values-for-projection-operations"><code>projection</code>
examples</a> for more on this parameter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>include_similarity</p></td>
<td style="text-align: left;"><p><code>Optional[bool]</code></p></td>
<td style="text-align: left;"><p>A boolean to request the numeric value
of the similarity to be returned as an added "$similarity" key in the
returned document. Can only be used for vector ANN search, i.e. when
either <code>vector</code> is supplied or the <code>sort</code>
parameter has the shape {"$vector": …​}.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>sort</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>With this dictionary parameter one can
control the order the documents are returned. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations">discussion
about sorting</a> for details. This parameter can express
<code>$vector</code> or <code>$vectorize</code> sort clauses, but not
both at the same time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
underlying HTTP request. This method uses the collection-level timeout
by default.</p></td>
</tr>
</tbody>
</table>

Example:

    from astrapy import DataAPIClient
    import astrapy
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    collection.find_one()
    # prints: {'_id': '68d1e515-...', 'seq': 37}
    collection.find_one({"seq": 10})
    # prints: {'_id': 'd560e217-...', 'seq': 10}
    collection.find_one({"seq": 1011})
    # (returns None for no matches)
    collection.find_one(projection={"seq": False})
    # prints: {'_id': '68d1e515-...'}
    collection.find_one(
        {},
        sort={"seq": astrapy.constants.SortDocuments.DESCENDING},
    )
    # prints: {'_id': '97e85f81-...', 'seq': 69}
    collection.find_one(sort={"$vector": [1, 0]}, projection={"*": True})
    # prints: {'_id': '...', 'tag': 'D', '$vector': [4.0, 1.0]}

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#findOne\[API
Reference\].

Retrieve a single document from a collection by its `_id`.

    const doc = await collection.findOne({ _id: '101' });

Retrieve a single document from a collection by any attribute, as long
as it is covered by the collection’s indexing configuration.

As noted in [The Indexing
option](api-reference:collections.xml#the-indexing-option) in the
Collections reference topic, any field that is part of a subsequent
filter or sort operation must be an indexed field. If you elected to not
index certain or all fields when you created the collection, you cannot
reference that field in a filter/sort query.

    const doc = await collection.findOne({ location: 'warehouse_C' });

Retrieve a single document from a collection by an arbitrary filtering
clause.

    const doc = await collection.findOne({ tag: { $exists: true } });

Retrieve the most similar document to a given vector.

    const doc = await collection.findOne({}, { sort: { $vector: [.12, .52, .32] } });

Generate a vector and retrieve the most similar document.

    const doc = await collection.findOne({}, { sort: { $vectorize: 'Text to vectorize' } });

Retrieve only specific fields from a document.

    const doc = await collection.findOne({ _id: '101' }, { projection: { name: 1 } });

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Filter.html[Filter&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>A filter to select the document to
find.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/FindOneOptions.html[FindOneOptions]</code></p></td>
<td style="text-align: left;"><p>The options for this
operation.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/FindOneOptions.html[FindOneOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneOptions.html#projection[projection?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Projection.html[Projection]</code></p></td>
<td style="text-align: left;"><p>Specifies which fields should be
included/excluded in the returned documents. Defaults to including all
fields.</p>
<p>When specifying a projection, it’s the user’s responsibility to
handle the return type carefully. Consider type-casting.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneOptions.html#includeSimilarity[includeSimilarity?]</p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Requests the numeric value of the
similarity to be returned as an added <code>$similarity</code> key in
the returned document.</p>
<p>Can only be used when performing a vector search.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneOptions.html#sort[sort?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Sort.html[Sort]</code></p></td>
<td style="text-align: left;"><p>Specifies the order in which the
documents are returned. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations">section
on sorting</a> for further detail. The sort may contain
<code>$vector</code> or <code>$vectorize</code> clauses, but not both at
once.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneOptions.html#maxTimeMS[maxTimeMS?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>The maximum time in milliseconds that
the client should wait for the operation to complete.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<{ts-client-api-ref-url}/types/FoundDoc.html[FoundDoc<Schema>] | null>` -
A promise that resolves to the found document (inc. `$similarity` if
applicable), or `null` if no matching document is found.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      // Insert some documents
      await collection.insertMany([
        { name: 'John', age: 30, $vector: [1, 1, 1, 1, 1] },
        { name: 'Jane', age: 25, },
        { name: 'Dave', age: 40, },
      ]);

      // Unpredictably prints one of their names
      const unpredictable = await collection.findOne({});
      console.log(unpredictable?.name);

      // Failed find by name (null)
      const failed = await collection.findOne({ name: 'Carrie' });
      console.log(failed);

      // Find by $gt age (Dave)
      const dave = await collection.findOne({ age: { $gt: 30 } });
      console.log(dave?.name);

      // Find by sorting by age (Jane)
      const jane = await collection.findOne({}, { sort: { age: 1 } });
      console.log(jane?.name);

      // Find by vector similarity (John, 1)
      const john = await collection.findOne({}, { sort: { $vector: [1, 1, 1, 1, 1] }, includeSimilarity: true });
      console.log(john?.name, john?.$similarity);
    })();

Java  
-   Operations on documents are performed at `Collection` level, to get
    details on each signature you can access the [Collection
    JavaDOC](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/Collection.html).

-   Collection is a generic class, default type is `Document` but you
    can specify your own type and the object will be serialized by
    Jackson.

-   Most methods come with synchronous and asynchronous flavors where
    the asynchronous version will be suffixed by `Async` and return a
    `CompletableFuture`.

    // Synchronous
    Optional<T> findOne(Filter filter);
    Optional<T> findOne(Filter filter, FindOneOptions options);
    Optional<T> findById(Object id); // build the filter for you

    // Asynchronous
    CompletableFuture<Optional<DOC>> findOneAsync(Filter filter);
    CompletableFuture<Optional<DOC>> findOneAsync(Filter filter, FindOneOptions options);
    CompletableFuture<Optional<DOC>> findByIdAsync(Filter filter);

Returns:

\[`Optional<T>`\] - Return the working document matching the filter or
`Optional.empty()` if no document is found.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>filter</code></p></td>
<td style="text-align: left;"><p><code>Filter</code></p></td>
<td style="text-align: left;"><p>Criteria list to filter the document.
The filter is a JSON object that can contain any valid Data API filter
expression.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>options</code>
(optional)</p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/FindOneOptions.html"><code>FindOneOptions</code></a></p></td>
<td style="text-align: left;"><p>Set the different options for the
<code>findOne</code> operation. The options are a <code>sort</code>
clause, some <code>projection</code> to retrieve sub parts of the
documents and a flag to include the similarity in case of a vector
search.</p></td>
</tr>
</tbody>
</table>

Things you must know about Data API requests:

-   A `Filter` is a Json expression that accept different operators
    listed on the Data API command page.

-   A `Projection` is list of flags that indicate if you want to
    retrieve a field or not

-   The `sort` clause is used either for similarity search or order
    results

-   In `options` you will reveal if you want to include the similarity
    in the result

    {
      "findOne": {
        "filter": {
         "$and": [
            {"field2": {"$gt": 10}},
            {"field3": {"$lt": 20}},
            {"field4": {"$eq": "value"}}
         ]
        },
        "projection": {
          "_id": 0,
          "field": 1,
          "field2": 1,
          "field3": 1
        },
        "sort": {
          "$vector": [ 0.25, 0.25, 0.25,0.25, 0.25]
        },
        "options": {
          "includeSimilarity": true
        }
      }
    }

To execute this exact query with Java here is the snippet

    collection.findOne(
      Filters.and(
       Filters.gt("field2", 10),
       Filters.lt("field3", 20),
       Filters.eq("field4", "value")
      ),
      new FindOneOptions()
       .projection(Projections.include("field", "field2", "field3"))
       .projection(Projections.exclude("_id"))
       .vector(new float[] {0.25f, 0.25f, 0.25f,0.25f, 0.25f})
       .includeSimilarity()
      )
    );

    // with the import Static Magic
    collection.findOne(
      and(
       gt("field2", 10),
       lt("field3", 20),
       eq("field4", "value")
      ),
      vector(new float[] {0.25f, 0.25f, 0.25f,0.25f, 0.25f})
       .projection(Projections.include("field", "field2", "field3"))
       .projection(Projections.exclude("_id"))
       .includeSimilarity()
    );

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/FindOne.java[role=include]

cURL  
This Data API `findOne` command retrieves a document based on a filter
using a specific `_id` value.

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
      "findOne": {
        "filter": {"_id": "14"}
      }
    }' | jq
    # `| jq` is optional.

Result:

    {
       "data": {
          "document": {
             "$vector": [
                0.11,
                0.02,
                0.78,
                0.21,
                0.27
             ],
             "_id": "14",
             "amount": 110400,
             "customer": {
                "address": {
                   "address_line": "1414 14th Pl",
                   "city": "Brooklyn",
                   "state": "NY"
                },
                "age": 44,
                "credit_score": 702,
                "name": "Kris S.",
                "phone": "123-456-1144"
             },
             "items": [
                {
                   "car": "Tesla Model X",
                   "color": "White"
                }
             ],
             "purchase_date": {
                "$date": 1698513091
             },
             "purchase_type": "In Person",
             "seller": {
                "location": "Brooklyn NYC",
                "name": "Jasmine S."
             },
             "status": "active"
          }
       }
    }

# Find documents using filtering options

Iterate over documents in a collection matching a given filter.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.find\[API
Reference\].

    doc_iterator = collection.find({"category": "house_appliance"}, limit=10)

Iterate over the documents most similar to a given query vector.

    doc_iterator = collection.find(
        {},
        sort={"$vector": [0.55, -0.40, 0.08]},
        limit=5,
    )

Generate a vector and iterate over the documents most similar to it.

    doc_iterator = collection.find(
        {},
        sort={"$vectorize": "Text to vectorize"},
        limit=5,
    )

Returns:

`{py-client-api-ref-url}/cursors.html#astrapy.cursors.Cursor[Cursor]` -
A cursor for iterating over documents. An AstraPy cursor can be used in
a for loop, and provides a few additional features.

    Cursor("vector_collection", new, retrieved so far: 0)

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>projection</p></td>
<td
style="text-align: left;"><p><code>Optional[Union[Iterable[str], Dict[str, bool]]]</code></p></td>
<td style="text-align: left;"><p>Used to select a subset of fields in
the documents being returned. The projection can be: an iterable over
the included field names; a dictionary {field_name: True} to positively
select certain fields; or a dictionary {field_name: False} if one wants
to exclude specific fields from the response. Special document fields
(e.g. <code>_id</code>, <code>$vector</code>) are controlled
individually. The default projection does not necessarily include all
fields of the document. See the <a
href="api-reference:documents.xml#example-values-for-projection-operations"><code>projection</code>
examples</a> for more on this parameter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>skip</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>With this integer parameter, what would
be the first <code>skip</code> documents returned by the query are
discarded, and the results start from the (skip+1)-th document. This
parameter can be used only in conjunction with an explicit
<code>sort</code> criterion of the ascending/descending type (i.e. it
cannot be used when not sorting, nor with vector-based ANN
search).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>limit</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>This (integer) parameter sets a limit
over how many documents are returned. Once <code>limit</code> is reached
(or the cursor is exhausted for lack of matching documents), nothing
more is returned.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>include_similarity</p></td>
<td style="text-align: left;"><p><code>Optional[bool]</code></p></td>
<td style="text-align: left;"><p>A boolean to request the numeric value
of the similarity to be returned as an added "$similarity" key in each
returned document. Can only be used for vector ANN search, i.e. when
either <code>vector</code> is supplied or the <code>sort</code>
parameter has the shape {"$vector": …​}.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>include_sort_vector</p></td>
<td style="text-align: left;"><p><code>Optional[bool]</code></p></td>
<td style="text-align: left;"><p>A boolean to request the vector used
when querying the database. Only meaningful if <code>sort</code>
includes either <code>$vector</code> or <code>$vectorize</code>.</p>
<p>You can’t use <code>include_sort_vector</code> with
<code>find_one()</code>. However, you can use
<code>include_sort_vector</code> and <code>limit=1</code> with
<code>find()</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>sort</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>With this dictionary parameter one can
control the order the documents are returned. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations">discussion
about sorting</a>, including the note on upper bounds on the number of
visited documents, for details. This parameter can express
<code>$vector</code> or <code>$vectorize</code> sort clauses, but not
both at the same time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for each
underlying HTTP request used to fetch documents as you iterate over the
cursor. This method uses the collection-level timeout by
default.</p></td>
</tr>
</tbody>
</table>

Example:

    from astrapy import DataAPIClient
    import astrapy

    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.COLLECTION

    # Find all documents in the collection
    # Not advisable if a very high number of matches is anticipated
    for document in collection.find({}):
        print(document)

    # Find all documents in the collection with a specific field value
    for document in collection.find({"a": 123}):
        print(document)

    # Find all documents in the collection matching a compound filter expression
    matches = list(collection.find({
        "$and": [
          {"f1": 1},
          {"f2": 2},
        ]
    }))

    # Same as the preceeding example, but using the implicit AND operator
    matches = list(collection.find({
        "f1": 1,
        "f2": 2,
    }))

    # Use the "less than" operator in the filter expression
    matches2 = list(collection.find({
        "$and": [
          {"name": "John"},
          {"price": {"$lt": 100}},
        ]
    }))

    # Run a $vectorize search, get back the query vector along with the documents
    results_ite = collection.find(
        {},
        projection={"*": 1},
        limit=3,
        include_sort_vector=True,
        sort={"$vectorize": "Query text"},
    )
    query = results_ite.get_sort_vector()
    for doc in results_ite:
        print(f"{doc['$vectorize']}: {doc['$vector'][:2]}... VS. {query[:2]}...")

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#find\[API Reference\].

    const cursor = collection.find({ category: 'house_appliance' }, { limit: 10 });

Iterate over the documents most similar to a given query vector.

    const cursor = collection.find({}, { sort: { $vector: [0.55, -0.40, 0.08] }, limit: 5 });

Generate a vector and iterate over the documents most similar to it.

    const cursor = collection.find({}, { sort: { $vectorize: 'Text to vectorize' }, limit: 5 });

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Filter.html[Filter&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>A filter to select the document to
find.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/FindOptions.html[FindOptions]</code></p></td>
<td style="text-align: left;"><p>The options for this
operation.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/FindOptions.html[FindOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOptions.html#projection[projection?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Projection.html[Projection]</code></p></td>
<td style="text-align: left;"><p>Specifies which fields should be
included/excluded in the returned documents. Defaults to including all
fields.</p>
<p>When specifying a projection, it’s the user’s responsibility to
handle the return type carefully. Consider type-casting.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOptions.html#includeSimilarity[includeSimilarity?]</p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Requests the numeric value of the
similarity to be returned as an added <code>$similarity</code> key in
the returned document.</p>
<p>Can only be used when performing a vector search.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOptions.html#includeSortVector[includeSortVector?]</p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Include the vector used when querying
the database in the response. Only meaningful if <code>sort</code>
includes either <code>$vector</code> or <code>$vectorize</code>.</p>
<p>You can also access this through
<code>await cursor.getSortVector()</code>.</p>
<p>You can’t use <code>includeSortVector</code> with
<code>findOne()</code>. However, you can use
<code>includeSortVector</code> and <code>limit: 1</code> with
<code>find()</code>.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOptions.html#sort[sort?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Sort.html[Sort]</code></p></td>
<td style="text-align: left;"><p>Specifies the order in which the
documents are returned. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations">section
on sorting</a> for further detail. The <code>sort</code> may contain
<code>$vector</code> or <code>$vectorize</code> clauses, but not both at
once.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOptions.html#skip[skip?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>The number of documents to skip before
returning the first document.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOptions.html#limit[limit?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>The maximum number of documents to
return in the lifetime of the cursor.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOptions.html#maxTimeMS[maxTimeMS?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>The maximum time in milliseconds that
the client should wait for the operation to complete for each single one
of the underlying HTTP requests.</p></td>
</tr>
</tbody>
</table>

Returns:

`{ts-client-api-ref-url}/classes/FindCursor.html[FindCursor<FoundDoc<Schema>>]` -
A cursor for iterating over the matching documents.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      // Insert some documents
      await collection.insertMany([
        { name: 'John', age: 30, $vector: [1, 1, 1, 1, 1] },
        { name: 'Jane', age: 25, },
        { name: 'Dave', age: 40, },
      ]);

      // Gets all 3 in some order
      const unpredictable = await collection.find({}).toArray();
      console.log(unpredictable);

      // Failed find by name ([])
      const matchless = await collection.find({ name: 'Carrie' }).toArray();
      console.log(matchless);

      // Find by $gt age (John, Dave)
      const gtAgeCursor = collection.find({ age: { $gt: 25 } });
      for await (const doc of gtAgeCursor) {
        console.log(doc.name);
      }

      // Find by sorting by age (Jane, John, Dave)
      const sortedAgeCursor = collection.find({}, { sort: { age: 1 } });
      await sortedAgeCursor.forEach(console.log);

      // Find first by vector similarity (John, 1)
      const john = await collection.find({}, { sort: { $vector: [1, 1, 1, 1, 1] }, includeSimilarity: true }).next();
      console.log(john?.name, john?.$similarity);
    })();

Java  
-   Operations on documents are performed at `Collection` level. To get
    details on each signature you can access the [Collection
    JavaDOC](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/Collection.html).

-   Collection is a generic class, default type is `Document` but you
    can specify your own type and the object will be serialized by
    Jackson.

-   Most methods come with synchronous and asynchronous flavors where
    the asynchronous version will be suffixed by `Async` and return a
    `CompletableFuture`.

    // Synchronous
    FindIterable<T> find(Filter filter, FindOptions options);
    // Helper to build filter and options above ^
    FindIterable<T> find(FindOptions options); // no filter
    FindIterable<T> find(Filter filter); // default options
    FindIterable<T> find(); // default options + no filters
    FindIterable<T> find(float[] vector, int limit); // semantic search
    FindIterable<T> find(Filter filter, float[] vector, int limit);

Returns:

[`FindIterable<T>`](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/FindIterable.html) -
A cursor where the first up to 20 documents are fetched and the rest are
fetched as needed. As the same stated it is an `Iterable`.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>filter</code></p></td>
<td style="text-align: left;"><p><code>Filter</code></p></td>
<td style="text-align: left;"><p>Criteria list to filter the document.
The filter is a JSON object that can contain any valid Data API filter
expression.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>options</code>
(optional)</p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/FindOptions.html"><code>FindOptions</code></a></p></td>
<td style="text-align: left;"><p>Set the different options for the
<code>find</code> operation. The options are a <code>sort</code> clause,
some <code>projection</code> to retrieve sub parts of the documents, the
<code>includeSimilarity</code> flag to include the similarity in case of
a vector search, and the <code>includeSortVector</code> flag to return
the vector used when querying the database with vector search.</p></td>
</tr>
</tbody>
</table>

The `FindIterable` is an `Iterable` that can be used in a `for` loop to
iterate over the documents.

The `FindIterable` fetches chunks of documents and fetches more as
needed. The `FindIterable` is a lazy iterator, meaning that it only
fetches the next chunk of documents when needed.

You can use the `.all()` method to exhaust it, but use this with
caution.

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/Find.java[role=include]

cURL  
There are two examples with Data API `find` filters in this cURL
section.

The first example uses a filter specifying two properties,
`customer.address.city` and `customer.address.state`, to look for car
sales by customers in Hoboken, NJ.

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
      "find": {
        "filter": {
          "customer.address.city": "Hoboken",
          "customer.address.state": "NJ"
        }
      }
    }' | jq
    # | jq is optional.

Result:

    {
       "data": {
          "documents": [
             {
                "$vector": [
                   0.1,
                   0.15,
                   0.3,
                   0.12,
                   0.09
                ],
                "_id": "17",
                "amount": 54900,
                "customer": {
                   "address": {
                      "address_line": "1234 Main St",
                      "city": "Hoboken",
                      "state": "NJ"
                   },
                   "age": 61,
                   "credit_score": 694,
                   "name": "Yolanda Z.",
                   "phone": "123-456-1177"
                },
                "items": [
                   {
                      "car": "Tesla Model 3",
                      "color": "Blue"
                   },
                   "Extended warranty - 5 years"
                ],
                "purchase_date": {
                   "$date": 1702660291
                },
                "purchase_type": "Online",
                "seller": {
                   "location": "Jersey City NJ",
                   "name": "Jim A."
                },
                "status": "active"
             }
          ],
          "nextPageState": null
       }
    }

Parameters:

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 20%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>find</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>Selects and returns documents from a
collection based on a specified criteria.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td style="text-align: left;"><p>object</p></td>
<td style="text-align: left;"><p>Contains the criteria that the
<code>find</code> command uses to fetch documents from the
database.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>customer.address.city</code> and
<code>customer.address.state</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>Query values in this example that find
customers from Hoboken, NJ.</p></td>
</tr>
</tbody>
</table>

This next Data API `find` example uses the `$and` and `$or` logical
operators in a filter. The goal is to find documents where the
customer’s city is "Jersey City" or "Orange" **AND** the seller’s name
is "Jim A." or "Tammy S.". For a document to be returned, both these
primary conditions (customer’s city and seller’s name) must be met.

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
        "find": {
            "filter": {
                "$and": [
                    {
                        "$or": [
                            {
                                "customer.address.city": "Jersey City"
                            },
                            {
                                "customer.address.city": "Orange"
                            }
                        ]
                    },
                    {
                        "$or": [
                            {
                                "seller.name": "Jim A."
                            },
                            {
                                "seller.name": "Tammy S."
                            }
                        ]
                    }
                ]
            }
        }
    }' | jq
    # | jq is optional.

Result:

    {
       "data": {
          "documents": [
             {
                "$vector": [
                   0.3,
                   0.23,
                   0.15,
                   0.17,
                   0.4
                ],
                "_id": "8",
                "amount": 46900,
                "customer": {
                   "address": {
                      "address_line": "1234 Main St",
                      "city": "Orange",
                      "state": "NJ"
                   },
                   "age": 29,
                   "credit_score": 710,
                   "name": "Harold S.",
                   "phone": "123-456-8888"
                },
                "items": [
                   {
                      "car": "BMW X3 SUV",
                      "color": "Black"
                   },
                   "Extended warranty - 5 years"
                ],
                "purchase_date": {
                   "$date": 1693329091
                },
                "purchase_type": "In Person",
                "seller": {
                   "location": "Staten Island NYC",
                   "name": "Tammy S."
                },
                "status": "active"
             },
             {
                "$vector": [
                   0.25,
                   0.045,
                   0.38,
                   0.31,
                   0.67
                ],
                "_id": "5",
                "amount": 94990,
                "customer": {
                   "address": {
                      "address_line": "32345 Main Ave",
                      "city": "Jersey City",
                      "state": "NJ"
                   },
                   "age": 50,
                   "credit_score": 800,
                   "name": "David C.",
                   "phone": "123-456-5555"
                },
                "items": [
                   {
                      "car": "Tesla Model S",
                      "color": "Red"
                   },
                   "Extended warranty - 5 years"
                ],
                "purchase_date": {
                   "$date": 1690996291
                },
                "purchase_type": "Online",
                "seller": {
                   "location": "Jersey City NJ",
                   "name": "Jim A."
                },
                "status": "active"
             }
          ],
          "nextPageState": null
       }
    }

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>find</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>Selects and returns documents from
collections based on a specified criteria.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td style="text-align: left;"><p>object</p></td>
<td style="text-align: left;"><p>Contains the criteria that the
<code>find</code> command uses to fetch documents from the
database.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>$and</p></td>
<td style="text-align: left;"><p>logical operator</p></td>
<td style="text-align: left;"><p>Ensures all nested conditions must be
met for a record to be returned.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>$or</p></td>
<td style="text-align: left;"><p>logical operator</p></td>
<td style="text-align: left;"><p>A logical operator where any one of the
nested conditions must be met. In this example, the first
<code>$or</code> nested condition checks whether the
<code>customer.address.city</code> property is equal to "Jersey City" or
to "Orange". The next <code>$or</code> nested condition check whether
the <code>seller.name</code> property is equal to "Jim A." or to "Tammy
S.".</p></td>
</tr>
</tbody>
</table>

# Example values for sort operations

Python  
When no particular order is required:

    sort={}  # (default when parameter not provided)

When sorting by a certain value in
{py-client-api-ref-url}/constants.html#astrapy.constants.SortDocuments\[ascending/descending
order\]:

    from astrapy.constants import SortDocuments
    sort={"field": SortDocuments.ASCENDING}
    sort={"field": SortDocuments.DESCENDING}

When sorting first by "field" and then by "subfield" (while modern
Python versions preserve the order of dictionaries, it is suggested for
clarity to employ a `collections.OrderedDict` in these cases):

    sort={
        "field": SortDocuments.ASCENDING,
        "subfield": SortDocuments.ASCENDING,
    }

Run a vector similarity (ANN) search based on a query vector:

    sort={"$vector": [0.4, 0.15, -0.5]}

Generate a vector to perform a vector similarity search. The collection
must be associated with an embedding service.

    sort={"$vectorize": "Text to vectorize"}

-   You can’t use the `$vector` and `$vectorize` sort clauses together.

-   Some combinations of arguments impose an implicit upper bound on the
    number of documents that are returned by the Data API:

    -   Vector ANN searches can’t return more than 1000 documents per
        search operation.

    -   When using an ascending or descending sort criterion, the Data
        API returns a smaller number of documents (20) and then stops.
        The returned documents are the top results across the whole
        collection based on the requested criterion.

        These provision can also apply when running subsequent commands
        on cursors, such as
        `{py-client-api-ref-url}/cursors.html#astrapy.cursors.Cursor.distinct[.distinct()]`.

-   When you don’t specify sorting criteria (by vector or otherwise),
    the cursor can scroll through an arbitrary number of documents
    because the Data API and the client periodically exchange new chunks
    of documents.

    If documents are added or removed after starting a `find` operation,
    the cursor behavior depends on database internals. There is no
    guarantee as to whether or not the cursor will pick up such
    "real-time" changes in the data.

Example:

    from astrapy import DataAPIClient
    import astrapy
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    filter = {"seq": {"$exists": True}}
    for doc in collection.find(filter, projection={"seq": True}, limit=5):
        print(doc["seq"])
    ...
    # will print e.g.:
    #   37
    #   35
    #   10
    #   36
    #   27
    cursor1 = collection.find(
        {},
        limit=4,
        sort={"seq": astrapy.constants.SortDocuments.DESCENDING},
    )
    [doc["_id"] for doc in cursor1]
    # prints: ['97e85f81-...', '1581efe4-...', '...', '...']
    cursor2 = collection.find({}, limit=3)
    cursor2.distinct("seq")
    # prints: [37, 35, 10]
    collection.insert_many([
        {"tag": "A", "$vector": [4, 5]},
        {"tag": "B", "$vector": [3, 4]},
        {"tag": "C", "$vector": [3, 2]},
        {"tag": "D", "$vector": [4, 1]},
        {"tag": "E", "$vector": [2, 5]},
    ])
    ann_tags = [
        document["tag"]
        for document in collection.find(
            {},
            sort={"$vector": [3, 3]},
            limit=3,
        )
    ]
    ann_tags
    # prints: ['A', 'B', 'C']
    # (assuming the collection has metric VectorMetric.COSINE)

TypeScript  

`{ts-client-api-ref-url}/types/Sort.html[Sort]` is very weakly typed by
default—see
`{ts-client-api-ref-url}/types/StrictSort.html[StrictSort<Schema>]` for
a stronger typed alternative that provides full autocomplete as well.

When no particular order is required:

    { sort: {} }  // (default when parameter not provided)

When sorting by a certain value in ascending/descending order:

    { sort: { field: +1 } }  // ascending
    { sort: { field: -1 } }  // descending

When sorting first by "field" and then by "subfield" (order matters!
ES2015+ guarantees string keys in order of insertion):

    { sort: { field: 1, subfield: 1 } }

Run a vector similarity (ANN) search based on a query vector:

    { sort: { $vector: [0.4, 0.15, -0.5] } }

Generate a vector to perform a vector similarity search. The collection
must be associated with an embedding service.

    { sort: { $vectorize: "Text to vectorize" } }

-   You can’t use the `$vector` and `$vectorize` sort clauses together.

-   Some combinations of arguments impose an implicit upper bound on the
    number of documents that are returned by the Data API:

    -   Vector ANN searches can’t return more than 1000 documents per
        search operation.

    -   When using an ascending or descending sort criterion, the Data
        API returns a smaller number of documents (20) and then stops.
        The returned documents are the top results across the whole
        collection based on the requested criterion.

        These provision can also apply when running subsequent commands,
        such as `.distinct()`, which relies on a cursor.

-   When you don’t specify sorting criteria (by vector or otherwise),
    the cursor can scroll through an arbitrary number of documents
    because the Data API and the client periodically exchange new chunks
    of documents.

    If documents are added or removed after starting a `find` operation,
    the cursor behavior depends on database internals. There is no
    guarantee as to whether or not the cursor will pick up such
    "real-time" changes in the data.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      // Insert some documents
      await collection.insertMany([
        { name: 'Jane', age: 25, $vector: [1.0, 1.0, 1.0, 1.0, 1.0] },
        { name: 'Dave', age: 40, $vector: [0.4, 0.5, 0.6, 0.7, 0.8] },
        { name: 'Jack', age: 40, $vector: [0.1, 0.9, 0.0, 0.5, 0.7] },
      ]);

      // Sort by age ascending, then by name descending (Jane, Jack, Dave)
      const sorted1 = await collection.find({}, { sort: { age: 1, name: -1 } }).toArray();
      console.log(sorted1.map(d => d.name));

      // Sort by vector distance (Jane, Dave, Jack)
      const sorted2 = await collection.find({}, { sort: { $vector: [1, 1, 1, 1, 1] } }).toArray();
      console.log(sorted2.map(d => d.name));
    })();

Java  
-   Use the `sort()` operations in different options only is you need
    them, it is optional

-   It is important to keep the order when chaining multiple sorts.

    Sort s1 = Sorts.ascending("field1");
    Sort s2 = Sorts.descending("field2");
    FindOptions.Builder.sort(s1, s2);

-   When running a vector similarity (ANN) search:

    FindOptions.Builder
     .sort(new float[] {0.4f, 0.15f, -0.5f});

-   Generate a vector to perform a vector similarity search.

    FindOptions.Builder
     .sort("Text to vectorize");

-   Some combinations of arguments impose an implicit upper bound on the
    number of documents that are returned by the Data API:

    -   Vector ANN searches can’t return more than 1000 documents per
        search operation.

    -   When using an ascending or descending sort criterion, the Data
        API returns a smaller number of documents (20) and then stops.
        The returned documents are the top results across the whole
        collection based on the requested criterion.

        These provision can also apply when running subsequent commands
        on a cursor, such as `.distinct()`.

-   When you don’t specify sorting criteria (by vector or otherwise),
    the cursor can scroll through an arbitrary number of documents
    because the Data API and the client periodically exchange new chunks
    of documents.

    If documents are added or removed after starting a `find` operation,
    the cursor behavior depends on database internals. There is no
    guarantee as to whether or not the cursor will pick up such
    "real-time" changes in the data.

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/WorkingWithSorts.java[role=include]

cURL  
This Data API command aims to `find` and `sort` documents that are most
similar to the specified vector, based on a similarity metric, and uses
a `projection` clause to project specific properties from those
documents in the response. The `$similarity` score (such as
`0.99444735`) is useful for understanding how close each result is to
the queried vector.

-   A value of 0 indicates that the vectors are diametrically opposed.

-   A value of 0.5 suggests the vectors are orthogonal (or
    perpendicular) and have no match.

-   A value of 1 indicates that the vectors are identical in direction.

In this example response, only the `$vector` and `$similarity`
properties are returned for each document, making the output more
focused and potentially reducing the amount of data transferred.

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
      "find": {
        "sort": {"$vector": [0.15, 0.1, 0.1, 0.35, 0.55]},
        "projection": {"$vector": 1},
        "options": {
            "includeSimilarity": true,
            "includeSortVector": false,
            "limit": 100
        }
      }
    }' | jq
    # | jq is optional.

Response:

    {
       "data": {
          "documents": [
             {
                "$similarity": 1,
                "$vector": [
                   0.15,
                   0.1,
                   0.1,
                   0.35,
                   0.55
                ],
                "_id": "3"
             },
             {
                "$similarity": 0.9953563,
                "$vector": [
                   0.15,
                   0.17,
                   0.15,
                   0.43,
                   0.55
                ],
                "_id": "18"
             },
             {
                "$similarity": 0.9732053,
                "$vector": [
                   0.21,
                   0.22,
                   0.33,
                   0.44,
                   0.53
                ],
                "_id": "21"
             },
             {
                "$similarity": 0.9732053,
                "$vector": [
                   0.21,
                   0.22,
                   0.33,
                   0.44,
                   0.53
                ],
                "_id": "7"
             },
             {
                "$similarity": 0.96955204,
                "$vector": [
                   0.25,
                   0.045,
                   0.38,
                   0.31,
                   0.68
                ],
                "_id": "10"
             },
             {
                "$similarity": 0.9691053,
                "$vector": [
                   0.25,
                   0.045,
                   0.38,
                   0.31,
                   0.67
                ],
                "_id": "5"
             },
             {
                "$similarity": 0.9600924,
                "$vector": [
                   0.44,
                   0.11,
                   0.33,
                   0.22,
                   0.88
                ],
                "_id": "11"
             },
             {
                "$similarity": 0.9600924,
                "$vector": [
                   0.44,
                   0.11,
                   0.33,
                   0.22,
                   0.88
                ],
                "_id": "20"
             },
             {
                "$similarity": 0.9600924,
                "$vector": [
                   0.44,
                   0.11,
                   0.33,
                   0.22,
                   0.88
                ],
                "_id": "16"
             },
             {
                "$similarity": 0.9468591,
                "$vector": [
                   0.33,
                   0.44,
                   0.55,
                   0.77,
                   0.66
                ],
                "_id": "12"
             },
             {
                "$similarity": 0.94535017,
                "$vector": [
                   0.3,
                   0.23,
                   0.15,
                   0.17,
                   0.4
                ],
                "_id": "8"
             },
             {
                "$similarity": 0.9163125,
                "$vector": [
                   0.25,
                   0.25,
                   0.25,
                   0.25,
                   0.27
                ],
                "_id": "19"
             },
             {
                "$similarity": 0.91263497,
                "$vector": [
                   0.25,
                   0.25,
                   0.25,
                   0.25,
                   0.26
                ],
                "_id": "4"
             },
             {
                "$similarity": 0.9087937,
                "$vector": [
                   0.25,
                   0.25,
                   0.25,
                   0.25,
                   0.25
                ],
                "_id": "1"
             },
             {
                "$similarity": 0.7909429,
                "$vector": [
                   0.1,
                   0.15,
                   0.3,
                   0.12,
                   0.09
                ],
                "_id": "17"
             },
             {
                "$similarity": 0.7820388,
                "$vector": [
                   0.1,
                   0.15,
                   0.3,
                   0.12,
                   0.08
                ],
                "_id": "15"
             },
             {
                "$similarity": 0.77284586,
                "$vector": [
                   0.1,
                   0.15,
                   0.3,
                   0.12,
                   0.07
                ],
                "_id": "13"
             },
             {
                "$similarity": 0.7711377,
                "$vector": [
                   0.11,
                   0.02,
                   0.78,
                   0.21,
                   0.27
                ],
                "_id": "14"
             },
             {
                "$similarity": 0.76337516,
                "$vector": [
                   0.1,
                   0.15,
                   0.3,
                   0.12,
                   0.06
                ],
                "_id": "9"
             },
             {
                "$similarity": 0.75363994,
                "$vector": [
                   0.1,
                   0.15,
                   0.3,
                   0.12,
                   0.05
                ],
                "_id": "2"
             },
             {
                "$similarity": 0.74406904,
                "$vector": [
                   0.11,
                   0.02,
                   0.78,
                   0.1,
                   0.27
                ],
                "_id": "6"
             }
          ],
          "nextPageState": null
       }
    }

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>find</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>A "find" or search command is to be
executed. It contains nested JSON objects that define the search
criteria, projection, and other options.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>sort</p></td>
<td style="text-align: left;"><p>clause</p></td>
<td style="text-align: left;"><p>Specifies the vector against which
other vectors in the vector-enabled {product} database are to be
compared. The <code>$vector</code> key is a reserved property name for
storing vector data. The vector in this example is set to
<code>[0.15, 0.1, 0.1, 0.35, 0.55]</code>. Documents in the database are
sorted based on their similarity to this vector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>projection</p></td>
<td style="text-align: left;"><p>clause</p></td>
<td style="text-align: left;"><p>Specify which properties should be
included in the returned documents.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>includeSimilarity</p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p>Setting this boolean to
<code>true</code> means that the response includes a
<strong><code>$similarity</code> score</strong>, representing the
similarity metric between the sorted vector and the vectors in the
database. The returned scores (such as <code>0.99444735</code>) are
useful for understanding how close each result is to the queried
vector.</p>
<ul>
<li><p>A value of 0 indicates that the vectors are diametrically
opposed.</p></li>
<li><p>A value of 0.5 suggests the vectors are orthogonal (or
perpendicular) and have no match.</p></li>
<li><p>A value of 1 indicates that the vectors are identical in
direction.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>includeSortVector</p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p>Set this boolean to <code>true</code>
to return the vector used when querying the database. Only meaningful if
<code>sort</code> includes either <code>$vector</code> or
<code>$vectorize</code>.</p>
<p>A successful response includes the <code>sortVector</code> in the
<code>status</code> object after the <code>data</code> object:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="er">&quot;status&quot;:</span> <span class="fu">{</span><span class="dt">&quot;sortVector&quot;</span><span class="fu">:</span> <span class="ot">[</span><span class="dv">0</span><span class="er">.</span><span class="dv">4</span><span class="ot">,</span> <span class="dv">0</span><span class="er">.</span><span class="dv">1</span><span class="ot">,</span> <span class="er">...</span><span class="ot">]</span><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p>limit</p></td>
<td style="text-align: left;"><p>number</p></td>
<td style="text-align: left;"><p>Specifies the maximum number of
documents to be returned. It’s set to <code>100</code>, meaning the
search returns up to the top 100 most similar documents. Pagination can
occur if more than 20 documents are returned in the current set of
matching documents.</p></td>
</tr>
</tbody>
</table>

# Example values for projection operations

Certain document operations — such as finding one or multiple documents,
find-and-update, find-and-replace, and find-and-delete — allow the use
of a `projection` option to control which part of the document(s) is
returned. The projection can generally take one of two forms: either
specifying which fields to include or which fields to exclude.

If no projection, or an empty projection, is specified, a default
projection is applied by the Data API. This default projection includes
at least the identifier (`_id`) of the document and all its "regular"
fields, which are those not starting with a dollar sign. However, future
versions of the Data API might exclude other fields (such as `$vector`)
from the documents by default.

When a projection is provided, specific, individually overridable
inclusion and exclusion defaults apply for "special" fields, such as
`_id`, `$vector`, and `$vectorize`. Conversely, for the regular fields
the projection must either list included fields or excluded ones and
cannot be a mixture of the two types of specifications.

In order to optimize the response size, a recommended performance
improvement is to always provide, when reading, an explicit projection
tailored to the needs of the application.

If an application relies on the presence of `$vector` (or other special
fields) in the returned document(s), the projection must explicitly
define inclusion of that field.

A quick, if possibly suboptimal, way to ensure the presence of fields is
to use the `{"*": true}` star-projection described below.

A projection is expressed as a mapping of field names to boolean values.
To return the document ID, `field1`, and `field2`:

    {"_id": true, "field1": true, "field2": true}

Specific fields can be excluded, keeping any other field found in the
document:

    {"field1": false, "field2": false}

Fields specified in the projection but not encountered in the document
are simply ignored for that document.

The projection *cannot mix include and exclude clauses for regular
fields*. In other words, it must either have all true or all false
values. If a projection has false values, all non-mentioned fields found
in the document are included; conversely, if it has true values, all
non-mentioned fields in the document are excluded.

Special fields (`_id`, `$vector`, and `$vectorize`) behave differently,
in that they have their own default and their presence can be controlled
in any way within the projection. For example, the `_id` field is
included by default and can be excluded even in an include-clause
projection (`{"_id": talse, "field1": true}`); conversely. the `$vector`
field is excluded by default and can be included even in an exclude
projection (`{"field1": false, "$vector": true}`).

So, the following are all valid projections:

    {"_id": true, "field1": true, "field2": true}
    {"_id": false, "field1": true, "field2": true}
    {"_id": false, "field1": false, "field2": false}
    {"_id": true, "field1": false, "field2": false}
    {"_id": true, "field1": true, "field2": true, "$vector": true}
    {"_id": true, "field1": true, "field2": true, "$vector": false}
    {"_id": false, "field1": true, "field2": true, "$vector": true}
    {"_id": false, "field1": true, "field2": true, "$vector": false}
    {"_id": false, "field1": false, "field2": false, "$vector": true}
    {"_id": false, "field1": false, "field2": false, "$vector": false}
    {"_id": true, "field1": false, "field2": false, "$vector": true}
    {"_id": true, "field1": false, "field2": false, "$vector": false}

However, the following projection is invalid and will result in an API
error:

    // Invalid:
    {"field1": true, "field2": false}

The special projection path `"*"` ("star-projection"), which must be the
only key in the projection, represents the whole of the document. With
the following projection all of the document is returned:

    {"*": true}

Conversely, with the following any document would return as `{}`:

    {"*": false}

The values in a projection map can be objects, booleans or number
(decimal or integer), but are then treated as booleans by the API. The
following two examples include and exclude the four fields respectively:

    {"field1": true, "field2": 1, "field3": 90.0, "field4": {"keep": "yes!"}}
    {"field1": false, "field2": 0, "field3": 0.0, "field4": {}}

Passing null-like things (such as `{}`, `null` or `0`) for the whole
`projection` has the same effect as not passing it altogether.

The projection cannot include the special `$similarity` key — which is
not part of the document but is rather computed during vector ANN
queries and is controlled through a specific `includeSimilarity`
parameter in the search payload.

However, for array fields, a `$slice` can be provided to specify which
elements of the array to return. It can be in one of the following
formats:

    // Return the first two elements
    {"arr": {"$slice": 2}}

    // Return the last two elements
    {"arr": {"$slice": -2}}

    // Skip 4 elements (from 0th index), return the next 2
    {"arr": {"$slice": [4, 2]}}

    // Skip backward 4 elements (from the end), return next 2 elements (forward)
    {"arr": {"$slice": [-4, 2]}}

The projection can also refer to nested fields: in that case, keys in a
subdocument will be included/excluded as requested. If all keys of an
existing subdocument are excluded, the document will be returned with
the subdocument still present, but consisting of an empty object:

Given the following document:

    {
      "_id": "z",
      "a": {
        "a1": 10,
        "a2": 20
      }
    }

Here the result of different projections can be seen:

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Projection</th>
<th style="text-align: left;">Result</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>{"a": true}</code></p></td>
<td
style="text-align: left;"><p><code>{"_id": "z", "a": {"a1": 10, "a2": 20}}</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>{"a.a1": false}</code></p></td>
<td
style="text-align: left;"><p><code>{"_id": "z", "a": {"a2": 20}}</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>{"a.a1": true}</code></p></td>
<td
style="text-align: left;"><p><code>{"_id": "z", "a": {"a1": 10}}</code></p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>{"a.a1": false, "a.a2": false}</code></p></td>
<td
style="text-align: left;"><p><code>{"_id": "z", "a": {}}</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>{"*": false}</code></p></td>
<td style="text-align: left;"><p><code>{}</code></p></td>
</tr>
</tbody>
</table>

Referencing overlapping (sub/)paths in the projection may lead to
(possibly) conflicting clauses. These are rejected, so for instance this
would yield an API error:

    // Invalid:
    {"a.a1": true, "a": true}

Python  
For the Python client, the type of the `projection` argument can be not
only a `Dict[str, Any]` in compliance with the general provisions above,
but it can also be a list — or other iterable — over key names. In this
case it is implied that there are all *included* in the projection. So,
the two following statements are equivalent:

    document = collection.find_one(
       {"_id": 101},
       projection={"name": True, "city": True},
    )

    document = collection.find_one(
       {"_id": 101},
       projection={"name": True, "city": True},
    )

TypeScript  
The Typescript client simply takes in an untyped *Plain Old JavaScript
Object* (POJO) for the `projection` parameter.

However, it offers a
`{ts-client-api-ref-url}/types/StrictProjection.html[StrictProjection<Schema>]`
type that provides full autocomplete and type checking for your document
schema.

    import { StrictProjection } from '@datastax/astra-db-ts';

    const doc = await collection.findOne({}, {
      projection: {
        'name': true,
        'address.city': true,
      },
    });

    interface MySchema {
      name: string,
      address: {
        city: string,
        state: string,
      },
    }

    const doc = await collection.findOne({}, {
      projection: {
        'name': 1,
        'address.city': 1,
        // @ts-expect-error - 'address.car' does not exist in type StrictProjection<MySchema>
        'address.car': 0,
        // @ts-expect-error - Type { $slice: number } is not assignable to type boolean | 0 | 1 | undefined
        'address.state': { $slice: 3 }
      } satisfies StrictProjection<MySchema>,
    });

Java  
To support the projection mechanism, the different `Options` classes
provide the `projection` method in the helpers. This method takes an
array of `Projection` classes providing the field name and a boolean
flag to choose between inclusion and exclusion.

    Projection p1 = new Projection("field1", true);
    Projection p2 = new Projection("field2", true);
    FindOptions options1 = FindOptions.Builder.projection(p1, p2);

This syntax can be simplified by leveraging the syntactic sugar called
`Projections`:

    FindOptions options2 = FindOptions.Builder
      .projection(Projections.include("field1", "field2"));

    FindOptions options3 = FindOptions.Builder
      .projection(Projections.exclude("field1", "field2"));

When it comes to support of `$slice` for array fields, the `Projection`
class provides a method as well:

    // {"arr": {"$slice": 2}}
    Projection sliceOnlyStart = Projections.slice("arr", 2, null);

    // {"arr": {"$slice": [-4, 2]}}
    Projection sliceOnlyRange =Projections.slice("arr", -4, 2);

    // An you can use then freely in the different builders
    FindOptions options4 = FindOptions.Builder
      .projection(sliceOnlyStart);

# Find and update a document

Locate a document matching a filter condition and apply changes to it,
returning the document itself.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.find\_one\_and\_update\[API
Reference\].

    collection.find_one_and_update(
        {"Marco": {"$exists": True}},
        {"$set": {"title": "Mr."}},
    )

Locate and update a document, returning the document itself, creating a
new one if nothing is found.

    collection.find_one_and_update(
        {"Marco": {"$exists": True}},
        {"$set": {"title": "Mr."}},
        upsert=True,
    )

Locate and update the document most similar to a provided query vector.

    collection.find_one_and_update(
        {},
        {"$set": {"best_match": True}},
        sort={"$vector": [0.1, 0.2, 0.3]},
    )

Returns:

`Dict[str, Any]` - The document that was found, either before or after
the update (or a projection thereof, as requested). If no matches are
found, `None` is returned.

    {'_id': 999, 'Marco': 'Polo'}

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td style="text-align: left;"><p><code>Dict[str, Any]</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>update</p></td>
<td style="text-align: left;"><p><code>Dict[str, Any]</code></p></td>
<td style="text-align: left;"><p>The update prescription to apply to the
document, expressed as a dictionary as per Data API syntax. Examples
are: <code>{"$set": {"field": "value}}</code>,
<code>{"$inc": {"counter": 10}}</code> and
<code>{"$unset": {"field": ""}}</code>. See <a
href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full syntax.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>projection</p></td>
<td
style="text-align: left;"><p><code>Optional[Union[Iterable[str], Dict[str, bool]]]</code></p></td>
<td style="text-align: left;"><p>Used to select a subset of fields in
the document being returned. The projection can be: an iterable over the
included field names; a dictionary {field_name: True} to positively
select certain fields; or a dictionary {field_name: False} if one wants
to exclude specific fields from the response. Special document fields
(e.g. <code>_id</code>, <code>$vector</code>) are controlled
individually. The default projection does not necessarily include all
fields of the document. See the <a
href="api-reference:documents.xml#example-values-for-projection-operations"><code>projection</code>
examples</a> for more on this parameter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>sort</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>With this dictionary parameter one can
control the sorting order of the documents matching the filter,
effectively determining what document will come first and hence be the
updated one. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations"><code>sort</code>
examples</a> for more on sorting. This parameter can express
<code>$vector</code> or <code>$vectorize</code> sort clauses, but not
both at the same time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>upsert</p></td>
<td style="text-align: left;"><p><code>bool = False</code></p></td>
<td style="text-align: left;"><p>This parameter controls the behavior in
absence of matches. If True, a new document (resulting from applying the
<code>update</code> to an empty document) is inserted if no matches are
found on the collection. If False, the operation silently does nothing
in case of no matches.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>return_document</p></td>
<td style="text-align: left;"><p><code>str</code></p></td>
<td style="text-align: left;"><p>A flag controlling what document is
returned: if set to
<code>{py-client-api-ref-url}/constants.html#astrapy.constants.ReturnDocument.BEFORE[ReturnDocument.BEFORE]</code>,
or the string "before", the document found on database is returned; if
set to
<code>{py-client-api-ref-url}/constants.html#astrapy.constants.ReturnDocument.AFTER[ReturnDocument.AFTER]</code>,
or the string "after", the new document is returned. The default is
"before".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
underlying HTTP request. This method uses the collection-level timeout
by default.</p></td>
</tr>
</tbody>
</table>

Example:

    from astrapy import DataAPIClient
    import astrapy
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    collection.insert_one({"Marco": "Polo"})

    collection.find_one_and_update(
        {"Marco": {"$exists": True}},
        {"$set": {"title": "Mr."}},
    )
    # prints: {'_id': 'a80106f2-...', 'Marco': 'Polo'}
    collection.find_one_and_update(
        {"title": "Mr."},
        {"$inc": {"rank": 3}},
        projection={"title": True, "rank": True},
        return_document=astrapy.constants.ReturnDocument.AFTER,
    )
    # prints: {'_id': 'a80106f2-...', 'title': 'Mr.', 'rank': 3}
    collection.find_one_and_update(
        {"name": "Johnny"},
        {"$set": {"rank": 0}},
        return_document=astrapy.constants.ReturnDocument.AFTER,
    )
    # (returns None for no matches)
    collection.find_one_and_update(
        {"name": "Johnny"},
        {"$set": {"rank": 0}},
        upsert=True,
        return_document=astrapy.constants.ReturnDocument.AFTER,
    )
    # prints: {'_id': 'cb4ef2ab-...', 'name': 'Johnny', 'rank': 0}

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#findOneAndUpdate.findOneAndUpdate-2\[API
Reference\].

    const docBefore = await collection.findOneAndUpdate(
      { $and: [{ name: 'Jesse' }, { gender: 'M' }] },
      { $set: { title: 'Mr.' } },
    );

Locate and update a document, returning the updated, creating a new one
if nothing is found.

    const docAfter = await collection.findOneAndUpdate(
      { $and: [{ name: 'Jesse' }, { gender: 'M' }] },
      { $set: { title: 'Mr.' } },
      { upsert: true, returnDocument: 'after' },
    );

Locate and update the document most similar to a provided query vector.

    const docBefore = await collection.findOneAndUpdate(
      {},
      { $set: { bestMatch: true } },
      { sort: { $vector: [0.1, 0.2, 0.3] } },
    );

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Filter.html[Filter&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>A filter to select the document to
update.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>update</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/UpdateFilter.html[UpdateFilter&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>The update to apply to the selected
document.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/FindOneAndUpdateOptions.html[FindOneAndUpdateOptions]</code></p></td>
<td style="text-align: left;"><p>The options for this
operation.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/FindOneAndUpdateOptions.html[FindOneAndUpdateOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndUpdateOptions.html#returnDocument[returnDocument]</p></td>
<td
style="text-align: left;"><p><code>'before' | 'after'</code></p></td>
<td style="text-align: left;"><p>Specifies whether to return the
original or updated document.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndUpdateOptions.html#upsert[upsert?]</p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>If true, creates a new document if no
document matches the filter.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndUpdateOptions.html#projection[projection?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Projection.html[Projection]</code></p></td>
<td style="text-align: left;"><p>Specifies which fields should be
included/excluded in the returned documents. Defaults to including all
fields.</p>
<p>When specifying a projection, it’s the user’s responsibility to
handle the return type carefully. Consider type-casting.</p>
<p>Can only be used when performing a vector search.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndUpdateOptions.html#sort[sort?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Sort.html[Sort]</code></p></td>
<td style="text-align: left;"><p>Specifies the order in which the
documents are returned. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations">section
on sorting</a> for further detail. The sort may contain
<code>$vector</code> or <code>$vectorize</code> clauses, but not both at
once.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndUpdateOptions.html#maxTimeMS[maxTimeMS?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>The maximum time in milliseconds that
the client should wait for the operation to complete for each single one
of the underlying HTTP requests.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndUpdateOptions.html#includeResultMetadata[includeResultMetadata?]</p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>When true, returns alongside the
document, an ok field with a value of 1 if the command executed
successfully.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<{ts-client-api-ref-url}/types/WithId.html[WithId<Schema>] | null>` -
The document before/after the update, depending on the type of
`returnDocument`, or `null` if no matches are found.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      // Insert a document
      await collection.insertOne({ 'Marco': 'Polo' });

      // Prints 'Mr.'
      const updated1 = await collection.findOneAndUpdate(
        { 'Marco': 'Polo' },
        { $set: { title: 'Mr.' } },
        { returnDocument: 'after' },
      );
      console.log(updated1?.title);

      // Prints { _id: ..., title: 'Mr.', rank: 3 }
      const updated2 = await collection.findOneAndUpdate(
        { title: 'Mr.' },
        { $inc: { rank: 3 } },
        { projection: { title: 1, rank: 1 }, returnDocument: 'after' },
      );
      console.log(updated2);

      // Prints null
      const updated3 = await collection.findOneAndUpdate(
        { name: 'Johnny' },
        { $set: { rank: 0 } },
        { returnDocument: 'after' },
      );
      console.log(updated3);

      // Prints { _id: ..., name: 'Johnny', rank: 0 }
      const updated4 = await collection.findOneAndUpdate(
        { name: 'Johnny' },
        { $set: { rank: 0 } },
        { upsert: true, returnDocument: 'after' },
      );
      console.log(updated4);
    })();

Java  
-   Operations on documents are performed at `Collection` level, to get
    details on each signature you can access the [Collection
    JavaDOC](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/Collection.html).

-   Collection is a generic class, default type is `Document` but you
    can specify your own type and the object will be serialized by
    Jackson.

-   Most methods come with synchronous and asynchronous flavors where
    the asynchronous version will be suffixed by `Async` and return a
    `CompletableFuture`.

    // Synchronous
    Optional<T> findOneAndUpdate(Filter filter, Update update);

    // Synchronous
    CompletableFuture<Optional<T>> findOneAndUpdateAsync(Filter filter, Update update);

Returns:

\[`Optional<T>`\] - Return the working document matching the filter or
`Optional.empty()` if no document is found.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>filter</code></p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/Filter.html"><code>Filter</code></a></p></td>
<td style="text-align: left;"><p>Criteria list to filter the document.
The filter is a JSON object that can contain any valid Data API filter
expression.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>update</code></p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/Update.html"><code>Update</code></a></p></td>
<td style="text-align: left;"><p>Set the different options for the
<code>find</code> operation. The options are a <code>sort</code> clause,
some <code>projection</code> to retrieve sub parts of the documents and
a flag to include the similarity in case of a vector search.</p></td>
</tr>
</tbody>
</table>

What you need to know:

To build the different parts of the requests a set of helper classes are
provided suffixed by a `s` like `Filters` for `Filter`.

Update is no different and you can leverage the class `Updates`.

    Update update = Updates
     .set("field1", "value1")
     .inc("field2", 1d)
     .unset("field3");

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/FindOneAndUpdate.java[role=include]

cURL  
The following Data API `findOneAndUpdate` command uses the `$sort` and
`$set` operators to update the `status` of one matching document (per
`$vector`) as `active`.

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
        "findOneAndUpdate": {
            "sort": {
                "$vector": [
                    0.25,
                    0.045,
                    0.38,
                    0.31,
                    0.67
                ]
            },
            "update": {
                "$set": {
                    "status": "active"
                }
            },
            "options": {
                "returnDocument": "after"
            }
        }
    }' | jq
    # | jq is optional.

Response:

In this case, notice that the response returns a `modifiedCount` of `0`
because the matching document’s status was already `active`.

    {
        "data": {
            "document": {
                "_id": "5",
                "purchase_type": "Online",
                "$vector": [
                    0.25,
                    0.045,
                    0.38,
                    0.31,
                    0.67
                ],
                "customer": {
                    "name": "David C.",
                    "phone": "123-456-5555",
                    "age": 50,
                    "credit_score": 800,
                    "address": {
                        "address_line": "32345 Main Ave",
                        "city": "Jersey City",
                        "state": "NJ"
                    }
                },
                "purchase_date": {
                    "$date": 1690996291
                },
                "seller": {
                    "name": "Jim A.",
                    "location": "Jersey City NJ"
                },
                "items": [
                    {
                        "car": "Tesla Model S",
                        "color": "Red"
                    },
                    "Extended warranty - 5 years"
                ],
                "amount": 94990,
                "status": "active"
            }
        },
        "status": {
            "matchedCount": 1,
            "modifiedCount": 0
        }
    }

Parameters:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 16%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>findOneAndUpdate</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>Find one document based on certain
criteria and determine if the document should be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>sort</p></td>
<td style="text-align: left;"><p>clause</p></td>
<td style="text-align: left;"><p>Contains an object specifying the sort
criteria for selecting the document.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>$vector</p></td>
<td style="text-align: left;"><p>array</p></td>
<td style="text-align: left;"><p>Indicates a vector-based sort
operation, where the documents are sorted based on the provided vector
values. In this example,
<code>[0.15, 0.1, 0.1, 0.35, 0.55]</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>$vectorize</p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>A string to be vectorized and used as
the sorting criterion in a vector search.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>update</p></td>
<td style="text-align: left;"><p>clause</p></td>
<td style="text-align: left;"><p>Contains the changes to be applied to
the selected document.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>$set</p></td>
<td style="text-align: left;"><p>Update operator</p></td>
<td style="text-align: left;"><p>Used to set the value of a field. Here,
it is used to set the <code>status</code> property of the document to
<code>active</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options</p></td>
<td style="text-align: left;"><p>clause</p></td>
<td style="text-align: left;"><p>Provides additional settings for the
<code>findOneAndUpdate</code> command.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>returnDocument</p></td>
<td style="text-align: left;"><p>clause</p></td>
<td style="text-align: left;"><p>In this example, the
<code>returnDocument</code>: after` option specifies that the modified
document should be returned in the response after the update is applied.
This allows the client to see the updated state of the document
immediately. In this case, though, notice that the response returns a
<code>modifiedCount</code> of <code>0</code> because the matching
document’s status was already <code>active</code>.</p></td>
</tr>
</tbody>
</table>

# Update a document

Update a single document on the collection as requested.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.update\_one\[API
Reference\].

    update_result = collection.update_one(
        {"_id": 456},
        {"$set": {"name": "John Smith"}},
    )

Update a single document on the collection, inserting a new one if no
match is found.

    update_result = collection.update_one(
        {"_id": 456},
        {"$set": {"name": "John Smith"}},
        upsert=True,
    )

Update the document most similar to a provided query vector.

    update_result = collection.update_one(
        {},
        {"$set": {"best_match": True}},
        sort={"$vector": [0.1, 0.2, 0.3]},
    )

Returns:

`{py-client-api-ref-url}/results.html#astrapy.results.UpdateResult[UpdateResult]` -
An object representing the response from the database after the update
operation. It includes information about the operation.

    UpdateResult(raw_results=[{'data': {'document': {'_id': '1', 'name': 'John Doe'}}, 'status': {'matchedCount': 1, 'modifiedCount': 1}}], update_info={'n': 1, 'updatedExisting': True, 'ok': 1.0, 'nModified': 1})

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td style="text-align: left;"><p><code>Dict[str, Any]</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>update</p></td>
<td style="text-align: left;"><p><code>Dict[str, Any]</code></p></td>
<td style="text-align: left;"><p>The update prescription to apply to the
document, expressed as a dictionary as per Data API syntax. Examples
are: <code>{"$set": {"field": "value}}</code>,
<code>{"$inc": {"counter": 10}}</code> and
<code>{"$unset": {"field": ""}}</code>. See <a
href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full syntax.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>sort</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>With this dictionary parameter one can
control the sorting order of the documents matching the filter,
effectively determining what document will come first and hence be the
updated one. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations"><code>sort</code>
examples</a> for more on sorting. This parameter can express
<code>$vector</code> or <code>$vectorize</code> sort clauses, but not
both at the same time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>upsert</p></td>
<td style="text-align: left;"><p><code>bool = False</code></p></td>
<td style="text-align: left;"><p>This parameter controls the behavior in
absence of matches. If True, a new document (resulting from applying the
<code>update</code> to an empty document) is inserted if no matches are
found on the collection. If False, the operation silently does nothing
in case of no matches.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
underlying HTTP request. This method uses the collection-level timeout
by default.</p></td>
</tr>
</tbody>
</table>

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    collection.insert_one({"Marco": "Polo"})

    collection.update_one({"Marco": {"$exists": True}}, {"$inc": {"rank": 3}})
    # prints: UpdateResult(raw_results=..., update_info={'n': 1, 'updatedExisting': True, 'ok': 1.0, 'nModified': 1})
    collection.update_one({"Mirko": {"$exists": True}}, {"$inc": {"rank": 3}})
    # prints: UpdateResult(raw_results=..., update_info={'n': 0, 'updatedExisting': False, 'ok': 1.0, 'nModified': 0})
    collection.update_one(
        {"Mirko": {"$exists": True}},
        {"$inc": {"rank": 3}},
        upsert=True,
    )
    # prints: UpdateResult(raw_results=..., update_info={'n': 1, 'updatedExisting': False, 'ok': 1.0, 'nModified': 0, 'upserted': '2a45ff60-...'})

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#updateOne\[API
Reference\].

    const result = await collection.updateOne(
      { $and: [{ name: 'Jesse' }, { gender: 'M' }] },
      { $set: { title: 'Mr.' } },
    );

Update a single document on the collection, inserting a new one if no
match is found.

    const result = await collection.updateOne(
      { $and: [{ name: 'Jesse' }, { gender: 'M' }] },
      { $set: { title: 'Mr.' } },
      { upsert: true },
    );

Update the document most similar to a provided query vector.

    const result = await collection.updateOne(
      {},
      { $set: { bestMatch: true } },
      { sort: { $vector: [0.1, 0.2, 0.3] } },
    );

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Filter.html[Filter&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>A filter to select the document to
update.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>update</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/UpdateFilter.html[UpdateFilter&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>The update to apply to the selected
document.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/UpdateOneOptions.html[UpdateOneOptions]</code></p></td>
<td style="text-align: left;"><p>The options for this
operation.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/UpdateOneOptions.html[UpdateOneOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndUpdateOptions.html#upsert[upsert?]</p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>If true, creates a new document if no
document matches the filter.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndUpdateOptions.html#sort[sort?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Sort.html[Sort]</code></p></td>
<td style="text-align: left;"><p>Specifies the order in which the
documents are returned. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations">section
on sorting</a> for further detail. The sort may contain
<code>$vector</code> or <code>$vectorize</code> clauses, but not both at
once.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndUpdateOptions.html#maxTimeMS[maxTimeMS?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>The maximum time in milliseconds that
the client should wait for the operation to complete for each single one
of the underlying HTTP requests.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<{ts-client-api-ref-url}/types/UpdateOneResult.html[UpdateOneResult<Schema>]>` -
The result of the update operation.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      // Insert a document
      await collection.insertOne({ 'Marco': 'Polo' });

      // Prints 1
      const updated1 = await collection.updateOne(
        { 'Marco': 'Polo' },
        { $set: { title: 'Mr.' } },
      );
      console.log(updated1?.modifiedCount);

      // Prints 0 0
      const updated2 = await collection.updateOne(
        { name: 'Johnny' },
        { $set: { rank: 0 } },
      );
      console.log(updated2.matchedCount, updated2?.upsertedCount);

      // Prints 0 1
      const updated3 = await collection.updateOne(
        { name: 'Johnny' },
        { $set: { rank: 0 } },
        { upsert: true },
      );
      console.log(updated3.matchedCount, updated3?.upsertedCount);
    })();

Java  
-   Operations on documents are performed at `Collection` level, to get
    details on each signature you can access the [Collection
    JavaDOC](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/Collection.html).

-   Collection is a generic class, default type is `Document` but you
    can specify your own type and the object will be serialized by
    Jackson.

-   Most methods come with synchronous and asynchronous flavors where
    the asynchronous version will be suffixed by `Async` and return a
    `CompletableFuture`.

    // Synchronous
    UpdateResult updateOne(Filter filter, Update update);

    // Asynchronous
    CompletableFuture<UpdateResult<T>> updateOneAsync(Filter filter, Update update);

Returns:

[`UpdateResults<T>`](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/UpdateResult.html) -
Result of the operation with the number of documents matched
(`matchedCount`) and updated (`modifiedCount`)

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>filter</code></p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/Filter.html"><code>Filter</code></a></p></td>
<td style="text-align: left;"><p>Criteria list to filter the document.
The filter is a JSON object that can contain any valid Data API filter
expression.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>update</code></p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/Update.html"><code>Update</code></a></p></td>
<td style="text-align: left;"><p>Set the different options for the
<code>find</code> operation. The options are a <code>sort</code> clause,
some <code>projection</code> to retrieve sub parts of the documents and
a flag to include the similarity in case of a vector search.</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/UpdateOne.java[role=include]

cURL  
The following Data API `updateOne` command uses the `$set` update
operator to set the value of a property (which uses the dot notation
`customer.name`) to a new value.

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
      "updateOne": {
        "filter": {
          "_id": "upsert-id"
        },
        "update": {"$set": { "customer.name": "CUSTOMER 22"}}
      }
    }' | jq
    # | jq is optional.

Response:

    {
       "status": {
          "matchedCount": 1,
          "modifiedCount": 1
       }
    }

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>updateOne</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>Updates a single document that matches
the given criteria within a database collection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td style="text-align: left;"><p>clause</p></td>
<td style="text-align: left;"><p>Used to select the document to be
updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>_id</p></td>
<td style="text-align: left;"><p>key</p></td>
<td style="text-align: left;"><p>This key within the <code>filter</code>
object targets a unique identifier property in the database’s documents.
The accompanying value <code>upsert-id</code> is the specific ID the API
looks for when determining which document to update.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>update</p></td>
<td style="text-align: left;"><p>object</p></td>
<td style="text-align: left;"><p>Specifies what updates are applied to
the document that meets the filter criteria. It’s an object that
contains database update operators and the modifications they
perform.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>$set</p></td>
<td style="text-align: left;"><p>Update operator</p></td>
<td style="text-align: left;"><p>Sets the value of a property in a
document. In this example, <code>customer</code> is a nested document or
a property within the main document, and <code>name</code> is a property
within <code>customer</code>. The operation targets this nested field.
The <code>CUSTOMER 22</code> value is what the
<code>customer.name</code> property is updated to during the
operation.</p></td>
</tr>
</tbody>
</table>

# Update multiple documents

Update multiple documents in a collection.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.update\_many\[API
Reference\].

    results = collection.update_many(
        {"name": {"$exists": False}},
        {"$set": {"name": "unknown"}},
    )

Update multiple documents in a collection, inserting a new one if no
matches are found.

    results = collection.update_many(
        {"name": {"$exists": False}},
        {"$set": {"name": "unknown"}},
        upsert=True,
    )

Returns:

`{py-client-api-ref-url}/results.html#astrapy.results.UpdateResult[UpdateResult]` -
An object representing the response from the database after the update
operation. It includes information about the operation.

    UpdateResult(raw_results=[{'status': {'matchedCount': 2, 'modifiedCount': 2}}], update_info={'n': 2, 'updatedExisting': True, 'ok': 1.0, 'nModified': 2})

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td style="text-align: left;"><p><code>Dict[str, Any]</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>update</p></td>
<td style="text-align: left;"><p><code>Dict[str, Any]</code></p></td>
<td style="text-align: left;"><p>The update prescription to apply to the
document, expressed as a dictionary as per Data API syntax. Examples
are: <code>{"$set": {"field": "value}}</code>,
<code>{"$inc": {"counter": 10}}</code> and
<code>{"$unset": {"field": ""}}</code>. See <a
href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full syntax.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>upsert</p></td>
<td style="text-align: left;"><p><code>bool</code></p></td>
<td style="text-align: left;"><p>This parameter controls the behavior in
absence of matches. If True, a single new document (resulting from
applying <code>update</code> to an empty document) is inserted if no
matches are found on the collection. If False, the operation silently
does nothing in case of no matches.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
operation. This method uses the collection-level timeout by default. You
may need to increase the timeout duration when updating a large number
of documents, as the update will require multiple HTTP requests in
sequence.</p></td>
</tr>
</tbody>
</table>

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    collection.insert_many([{"c": "red"}, {"c": "green"}, {"c": "blue"}])

    collection.update_many({"c": {"$ne": "green"}}, {"$set": {"nongreen": True}})
    # prints: UpdateResult(raw_results=..., update_info={'n': 2, 'updatedExisting': True, 'ok': 1.0, 'nModified': 2})
    collection.update_many({"c": "orange"}, {"$set": {"is_also_fruit": True}})
    # prints: UpdateResult(raw_results=..., update_info={'n': 0, 'updatedExisting': False, 'ok': 1.0, 'nModified': 0})
    collection.update_many(
        {"c": "orange"},
        {"$set": {"is_also_fruit": True}},
        upsert=True,
    )
    # prints: UpdateResult(raw_results=..., update_info={'n': 1, 'updatedExisting': False, 'ok': 1.0, 'nModified': 0, 'upserted': '46643050-...'})

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#updateMany\[API
Reference\].

    const result = await collection.updateMany(
      { name: { $exists: false } },
      { $set: { title: 'unknown' } },
    );

Update multiple documents in a collection, inserting a new one if no
matches are found.

    const result = await collection.updateMany(
      { name: { $exists: false } },
      { $set: { title: 'unknown' } },
      { upsert: true },
    );

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Filter.html[Filter&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>A filter to select the documents to
update.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>update</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/UpdateFilter.html[UpdateFilter&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>The update to apply to the selected
documents.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/UpdateManyOptions.html[UpdateManyOptions]</code></p></td>
<td style="text-align: left;"><p>The options for this
operation.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/UpdateManyOptions.html[UpdateManyOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndUpdateOptions.html#upsert[upsert?]</p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>If true, creates a new document if no
document matches the filter.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndUpdateOptions.html#maxTimeMS[maxTimeMS?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>The maximum time in milliseconds that
the client should wait for the operation to complete for each single one
of the underlying HTTP requests.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<{ts-client-api-ref-url}/types/UpdateManyResult.html[UpdateManyResult<Schema>]>` -
The result of the update operation.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      // Insert some documents
      await collection.insertMany([{ c: 'red' }, { c: 'green' }, { c: 'blue' }]);

      // { modifiedCount: 2, matchedCount: 2, upsertedCount: 0 }
      await collection.updateMany({ c: { $ne: 'green' } }, { $set: { nongreen: true } });

      // { modifiedCount: 0, matchedCount: 0, upsertedCount: 0 }
      await collection.updateMany({ c: 'orange' }, { $set: { is_also_fruit: true } });

      // { modifiedCount: 0, matchedCount: 0, upsertedCount: 1, upsertedId: '...' }
      await collection.updateMany({ c: 'orange' }, { $set: { is_also_fruit: true } }, { upsert: true });
    })();

Java  
-   Operations on documents are performed at `Collection` level, to get
    details on each signature you can access the [Collection
    JavaDOC](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/Collection.html).

-   Collection is a generic class, default type is `Document` but you
    can specify your own type and the object will be serialized by
    Jackson.

-   Most methods come with synchronous and asynchronous flavors where
    the asynchronous version will be suffixed by `Async` and return a
    `CompletableFuture`.

    // Synchronous
    UpdateResult updateMany(Filter filter, Update update);
    UpdateResult updateMany(Filter filter, Update update, UpdateManyOptions);

    // Synchronous
    CompletableFuture<UpdateResult<T>> updateManyAsync(Filter filter, Update update);
    CompletableFuture<UpdateResult<T>> updateManyAsync(Filter filter, Update update, UpdateManyOptions);

Returns:

[`UpdateResults<T>`](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/UpdateResult.html) -
Result of the operation with the number of documents matched
(`matchedCount`) and updated (`modifiedCount`)

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>filter</code></p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/Filter.html"><code>Filter</code></a></p></td>
<td style="text-align: left;"><p>Criteria list to filter the document.
The filter is a JSON object that can contain any valid Data API filter
expression.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>update</code></p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/Update.html"><code>Update</code></a></p></td>
<td style="text-align: left;"><p>Set the different options for the
<code>find</code> operation. The options are a <code>sort</code> clause,
some <code>projection</code> to retrieve sub parts of the documents and
a flag to include the similarity in case of a vector search.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>options</code></p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/UpdateManyOptions.html"><code>UpdateManyOptions</code></a></p></td>
<td style="text-align: left;"><p>Contains the options for update many
here you can set the <code>upsert</code> flag.</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/UpdateMany.java[role=include]

cURL  
Use the Data API `updateMany` command to update multiple documents in a
collection.

In this example, the JSON payload uses the `$set` update operator to
change a status to "inactive" for those documents that have an "active"
status.

The `updateMany` command includes pagination support in the event more
documents that matched the filter are on a subsequent page. For more,
see the [pagination note](#pagination-note) after the cURL example.

[api-reference:partial$json-structure-http-post.adoc](api-reference:partial$json-structure-http-post.adoc)

Example:

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
      "updateMany": {
        "filter": {"status": "active" },
        "update": {"$set": { "status": "inactive"}}
      }
    }' | jq
    # `| jq` is optional.

Result:

    {
       "status": {
          "matchedCount": 20,
          "modifiedCount": 20,
          "moreData": true
       }
    }

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>updateMany</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>Updates multiple documents in the
database’s collection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td style="text-align: left;"><p>object</p></td>
<td style="text-align: left;"><p>Defines the criteria for selecting
documents to which the command applies. The filter looks for documents
where: * <code>status</code>: The key being evaluated in each document;
a property within the documents in the database. * <code>active</code>:
The value that the <code>status</code> property must match for the
document to be selected. In this case, it’s targeting documents that
currently have a status of <code>active.</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>update</p></td>
<td style="text-align: left;"><p>object</p></td>
<td style="text-align: left;"><p>Specifies the modifications to be
applied to all documents that match the criteria set by the
filter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>$set</p></td>
<td style="text-align: left;"><p>operator</p></td>
<td style="text-align: left;"><p>An update operator indicating that the
operation should overwrite the value of a property (or properties) in
the selected documents.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>status</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: left;"><p>Specifies the property in the document
to update. In this example, active or inactive will be set for all
selected documents. In this context, it’s changing the
<code>status</code> from <code>active</code> to
<code>inactive.</code></p></td>
</tr>
</tbody>
</table>

In the `updateMany` response, check whether a `nextPageState` ID was
returned. The `updateMany` command includes pagination support. You can
update one page of matching documents at a time. If there is a
subsequent page with matching documents to update, the transaction
returns a `nextPageState` ID. You would then submit the `insertMany`
command again and include the `pageState` ID in the new request to
update the next page of documents that matched the filter:

    {
        "updateMany": {
            "filter": {
                "active_user": true
            },
            "update": {
                "$set": {
                    "new_data": "new_data_value"
                }
            },
            "options": {
                "pageState": "<id-value-from-prior-response>"
            }
        }
    }

During the pagination process, you would then follow the sequence of one
or more `insertMany` commands until all pages with documents matching
the filter have the update applied.

# Find distinct values across documents

Get a list of the distinct values of a certain key in a collection.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.distinct\[API
Reference\].

    collection.distinct("category")

Get the distinct values in a subset of documents, with a key defined by
a dot-syntax path.

    collection.distinct(
        "food.allergies",
        filter={"registered_for_dinner": True},
    )

Returns:

`List[Any]` - A list of the distinct values encountered. Documents that
lack the requested key are ignored.

    ['home_appliance', None, 'sports_equipment', {'cat_id': 54, 'cat_name': 'gardening_gear'}]

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>key</p></td>
<td style="text-align: left;"><p><code>str</code></p></td>
<td style="text-align: left;"><p>The name of the field whose value is
inspected across documents. Keys can use dot-notation to descend to
deeper document levels. Example of acceptable <code>key</code> values:
<code>"field"</code>, <code>"field.subfield"</code>,
<code>"field.3"</code>, and <code>"field.3.subfield"</code>. If lists
are encountered and no numeric index is specified, all items in the list
are visited.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
operation. This method uses the collection-level timeout by
default.</p></td>
</tr>
</tbody>
</table>

Keep in mind that `distinct` is a client-side operation, which
effectively browses all required documents using the logic of the `find`
method and collects the unique values found for `key`. As such, there
may be performance, latency and ultimately billing implications if the
amount of matching documents is large.

For details on the behavior of "distinct" in conjunction with real-time
changes in the collection contents, see the discussion in the [Sort
examples
values](api-reference:documents.xml#example-values-for-sort-operations)
section.

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    collection.insert_many(
        [
            {"name": "Marco", "food": ["apple", "orange"], "city": "Helsinki"},
            {"name": "Emma", "food": {"likes_fruit": True, "allergies": []}},
        ]
    )

    collection.distinct("name")
    # prints: ['Marco', 'Emma']
    collection.distinct("city")
    # prints: ['Helsinki']
    collection.distinct("food")
    # prints: ['apple', 'orange', {'likes_fruit': True, 'allergies': []}]
    collection.distinct("food.1")
    # prints: ['orange']
    collection.distinct("food.allergies")
    # prints: []
    collection.distinct("food.likes_fruit")
    # prints: [True]

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#distinct\[API
Reference\].

    const unique = await collection.distinct('category');

Get the distinct values in a subset of documents, with a key defined by
a dot-syntax path.

    const unique = await collection.distinct(
      'food.allergies',
      { registeredForDinner: true },
    );

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>key</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The name of the field whose value is
inspected across documents. Keys can use dot-notation to descend to
deeper document levels. Example of acceptable key values:
<code>'field'</code>, <code>'field.subfield'</code>,
<code>'field.3'</code>, and <code>'field.3.subfield'</code>. If lists
are encountered and no numeric index is specified, all items in the list
are visited.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>filter?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Filter.html[Filter&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>A filter to select the documents to
use. If not provided, all documents will be used.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<Flatten<(SomeDoc & ToDotNotation<FoundDoc<Schema>>)[Key]>[]>` -
A promise which resolves to the unique distinct values.

The return type is mostly accurate, but with complex keys, it may be
required to manually cast the return type to the expected type.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      // Insert some documents
      await collection.insertOne({ name: 'Marco', food: ['apple', 'orange'], city: 'Helsinki' });
      await collection.insertOne({ name: 'Emma', food: { likes_fruit: true, allergies: [] } });

      // ['Marco', 'Emma']
      await collection.distinct('name')

      // ['Helsinki']
      await collection.distinct('city')

      // ['apple', 'orange', { likes_fruit: true, allergies: [] }]
      await collection.distinct('food')

      // ['orange']
      await collection.distinct('food.1')

      // []
      await collection.distinct('food.allergies')

      // [true]
      await collection.distinct('food.likes_fruit')
    })();

Java  
Gets the distinct values of the specified field name.

    // Synchronous
    DistinctIterable<T,F> distinct(String fieldName, Filter filter, Class<F> resultClass);
    DistinctIterable<T,F> distinct(String fieldName, Class<F> resultClass);

    // Asynchronous
    CompletableFuture<DistinctIterable<T,F>> distinctAsync(String fieldName, Filter filter, Class<F> resultClass);
    CompletableFuture<DistinctIterable<T,F>> distinctAsync(String fieldName, Class<F> resultClass);

Returns:

[`DistinctIterable<F>`](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/DistinctIterable.html) -
List of distinct values of the specified field name.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>fieldName</code></p></td>
<td style="text-align: left;"><p><code>String</code></p></td>
<td style="text-align: left;"><p>The name of the field on which project
the value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>filter</code></p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/Filter.html"><code>Filter</code></a></p></td>
<td style="text-align: left;"><p>Criteria list to filter the document.
The filter is a JSON object that can contain any valid Data API filter
expression.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resultClass</code></p></td>
<td style="text-align: left;"><p><code>Class</code></p></td>
<td style="text-align: left;"><p>The type of the field we are working
on</p></td>
</tr>
</tbody>
</table>

Keep in mind that `distinct` is a client-side operation, which
effectively browses all required documents using the logic of the `find`
method and collects the unique values found for `key`. As such, there
may be performance, latency and ultimately billing implications if the
amount of matching documents is large.

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/Distinct.java[role=include]

# Count documents in a collection

Get the count of documents in a collection. Count all documents or apply
filtering to count a subset of documents.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.count\_documents\[API
Reference\].

    collection.count_documents({}, upper_bound=500)

Get the count of the documents in a collection matching a condition.

    collection.count_documents({"seq":{"$gt": 15}}, upper_bound=50)

Returns:

`int` - The exact count of the documents counted as requested, unless it
exceeds the caller-provided or API-set upper bound. In case of overflow,
an exception is raised.

    320

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>upper_bound</p></td>
<td style="text-align: left;"><p><code>int</code></p></td>
<td style="text-align: left;"><p>A required ceiling on the result of the
count operation. If the actual number of documents exceeds this value,
an exception is raised. An exception is also raised if the actual number
of documents exceeds the maximum count that the Data API can reach,
regardless of <code>upper_bound</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
underlying HTTP request. This method uses the collection-level timeout
by default.</p></td>
</tr>
</tbody>
</table>

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    collection.insert_many([{"seq": i} for i in range(20)])

    collection.count_documents({}, upper_bound=100)
    # prints: 20
    collection.count_documents({"seq":{"$gt": 15}}, upper_bound=100)
    # prints: 4
    collection.count_documents({}, upper_bound=10)
    # Raises: astrapy.exceptions.TooManyDocumentsToCountException

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#countDocuments\[API
Reference\].

    const numDocs = await collection.countDocuments({}, 500);

Get the count of the documents in a collection matching a filter.

    const numDocs = await collection.countDocuments({ seq: { $gt: 15 } }, 50);

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Filter.html[Filter&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>A filter to select the documents to
count. If not provided, all documents will be counted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>upperBound</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>A required ceiling on the result of the
count operation. If the actual number of documents exceeds this value,
an exception is raised. An exception is also raised if the actual number
of documents exceeds the maximum count that the Data API can reach,
regardless of <code>upperBound</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/WithTimeout.html[WithTimeout]</code></p></td>
<td style="text-align: left;"><p>The options (the timeout) for this
operation.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<number>` - A promise that resolves to the exact count of the
documents counted as requested, unless it exceeds the caller-provided or
API-set upper bound, in which case an exception is raised.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      // Insert some documents
      await collection.insertMany(Array.from({ length: 20 }, (_, i) => ({ seq: i })));

      // Prints 20
      await collection.countDocuments({}, 100);

      // Prints 4
      await collection.countDocuments({ seq: { $gt: 15 } }, 100);

      // Throws TooManyDocumentsToCountError
      await collection.countDocuments({}, 10);
    })();

Java  
    // Synchronous
    int countDocuments(int upperBound)
    throws TooManyDocumentsToCountException;

    int countDocuments(Filter filter, int upperBound)
    throws TooManyDocumentsToCountException;

Get the count of the documents in a collection matching a condition.

Returns:

`int` - The exact count of the documents counted as requested, unless it
exceeds the caller-provided or API-set upper bound. In case of overflow,
an exception is raised.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter (optional)</p></td>
<td style="text-align: left;"><p><code>Filter</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>upperBound</p></td>
<td style="text-align: left;"><p><code>int</code></p></td>
<td style="text-align: left;"><p>A required ceiling on the result of the
count operation. If the actual number of documents exceeds this value,
an exception will be raised. Furthermore, if the actual number of
documents exceeds the maximum count that the Data API can reach
(regardless of upper_bound), an exception will be raised.</p></td>
</tr>
</tbody>
</table>

The checked exception `TooManyDocumentsToCountException` is raised when
the actual number of documents exceeds the upper bound set by the caller
or the API. This exception indicates that there are more matching
documents beyond the count threshold.

Consider modifying your conditions to count fewer documents at once. If
you need to count large numbers of documents, consider using the Data
API
[`estimatedDocumentCount`](api-reference:documents.xml#estimate-document-count-in-a-collection)
command.

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/CountDocuments.java[role=include]

cURL  
Use the Data API `countDocuments` command to obtain the exact count of
documents in a collection:

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
                "countDocuments": {
                }
    }' | jq
    # `| jq` is optional.

You can provide an optional filter condition:

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
                "countDocuments": {
                    "filter": {
                        "year": {"$gt": 2000}
                    }
                }
    }' | jq
    # `| jq` is optional.

Returns:

`count` - The exact count of the documents counted as requested, unless
it exceeds the API-set upper bound, in which case the overflow is
reported in the response by the `moreData` flag.

    {
        "status": {
            "count": 105
        }
    }

Properties:

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 20%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>countDocuments</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>Returns an exact count of documents in
a collection. By default, all documents are counted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td style="text-align: left;"><p>JSON object</p></td>
<td style="text-align: left;"><p>Optional filtering clause for
<code>countDocuments</code>. If included, <code>countDocuments</code>
counts the subset of documents matching the filter.</p></td>
</tr>
</tbody>
</table>

This operation is suited to use cases where the number of documents to
count is moderate. Exact counting of an arbitrary number of documents is
a slow, expensive operation that is not supported by the Data API. If
the count total exceeds the server-side threshold, the response includes
`"moreData": true` to indicate that there are more matching documents
beyond the count threshold.

    {
        "status": {
            "moreData": true,
            "count": 1000
        }
    }

If you need to count large numbers of documents, consider using the Data
API
[`estimatedDocumentCount`](api-reference:documents.xml#estimate-document-count-in-a-collection)
command.

# Estimate document count in a collection

Get an approximate document count for an entire collection. Filtering
isn’t supported.

In the `estimatedDocumentCount` command’s response, the document count
is based on current system statistics at the time the request is
received by the database server. Due to potential in-progress updates
(document additions and deletions), the actual number of documents in
the collection can be lower or higher in the database.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.estimated\_document\_count\[API
Reference\].

    collection.estimated_document_count()

Returns:

`int` - A server-side estimate of the total number of documents in the
collection.

    37500

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
underlying HTTP request.</p></td>
</tr>
</tbody>
</table>

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database = my_client.get_database_by_api_endpoint("01234567-...")
    collection = database.my_collection

    collection.estimated_document_count()
    # prints: 37500

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#countDocuments\[API
Reference\].

    const estNumDocs = await collection.estimatedDocumentCount();

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/WithTimeout.html[WithTimeout]</code></p></td>
<td style="text-align: left;"><p>The options (the timeout) for this
operation.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<number>` - A promise that resolves to a server-side estimate of
the total number of documents in the collection.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      console.log(await collection.estimatedDocumentCount());
    })();

Java  
View this topic in more detail on the [API
Reference](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/Collection.html#estimatedDocumentCount()).

    long estimatedDocumentCount();
    long estimatedDocumentCount(EstimatedCountDocumentsOptions options);

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/EstimatedCountDocumentsOptions.html"><code>options</code></a></p></td>
<td style="text-align: left;"><p>Set different options for the
<code>estimatedDocumentCount</code> operation, such as
<code>timeout</code> and <code>httpSettings</code>.</p></td>
</tr>
</tbody>
</table>

Returns:

`long` - A server-side estimate of the total number of documents in the
collection. This estimate is built from the SSTable files.

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/EstimateCountDocuments.java[role=include]

cURL  
Use the Data API `estimatedDocumentCount` command to return the
approximate number of documents in the collection.

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
                "estimatedDocumentCount": {
                }
    }' | jq
    # `| jq` is optional.

Returns:

`count` - An estimate of the total number of documents in the
collection.

    {
        "status": {
            "count": 37500
        }
    }

Properties:

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 20%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>estimatedDocumentCount</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>Returns an estimated count of documents
within the context of the specified collection.</p></td>
</tr>
</tbody>
</table>

The `estimatedDocumentCount` object is empty (`{}`) because there are no
filters or options for this command.

# Find and replace a document

Locate a document matching a filter condition and replace it with a new
document, returning the document itself.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.find\_one\_and\_replace\[API
Reference\].

    collection.find_one_and_replace(
        {"_id": "rule1"},
        {"text": "some animals are more equal!"},
    )

Locate and replace a document, returning the document itself,
additionally creating it if nothing is found.

    collection.find_one_and_replace(
        {"_id": "rule1"},
        {"text": "some animals are more equal!"},
        upsert=True,
    )

Locate and replace the document most similar to a provided query vector.

    collection.find_one_and_replace(
        {},
        {"name": "Zoo", "desc": "the new best match"},
        sort={"$vector": [0.1, 0.2, 0.3]},
    )

Returns:

`Dict[str, Any]` - The document that was found, either before or after
the replacement (or a projection thereof, as requested). If no matches
are found, `None` is returned.

    {'_id': 'rule1', 'text': 'all animals are equal'}

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td style="text-align: left;"><p><code>Dict[str, Any]</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>replacement</p></td>
<td style="text-align: left;"><p><code>Dict[str, Any]</code></p></td>
<td style="text-align: left;"><p>the new document to write into the
collection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>projection</p></td>
<td
style="text-align: left;"><p><code>Optional[Union[Iterable[str], Dict[str, bool]]]</code></p></td>
<td style="text-align: left;"><p>Used to select a subset of fields in
the document being returned. The projection can be: an iterable over the
included field names; a dictionary {field_name: True} to positively
select certain fields; or a dictionary {field_name: False} if one wants
to exclude specific fields from the response. Special document fields
(e.g. <code>_id</code>, <code>$vector</code>) are controlled
individually. The default projection does not necessarily include all
fields of the document. See the <a
href="api-reference:documents.xml#example-values-for-projection-operations"><code>projection</code>
examples</a> for more on this parameter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>sort</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>With this dictionary parameter one can
control the sorting order of the documents matching the filter,
effectively determining what document will come first and hence be the
replaced one. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations"><code>sort</code>
examples</a> for more on sorting. This parameter can express
<code>$vector</code> or <code>$vectorize</code> sort clauses, but not
both at the same time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>upsert</p></td>
<td style="text-align: left;"><p><code>bool = False</code></p></td>
<td style="text-align: left;"><p>This parameter controls the behavior in
absence of matches. If True, <code>replacement</code> is inserted as a
new document if no matches are found on the collection. If False, the
operation silently does nothing in case of no matches.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>return_document</p></td>
<td style="text-align: left;"><p><code>str</code></p></td>
<td style="text-align: left;"><p>A flag controlling what document is
returned: if set to
<code>{py-client-api-ref-url}/constants.html#astrapy.constants.ReturnDocument.BEFORE[ReturnDocument.BEFORE]</code>,
or the string "before", the document found on database is returned; if
set to
<code>{py-client-api-ref-url}/constants.html#astrapy.constants.ReturnDocument.AFTER[ReturnDocument.AFTER]</code>,
or the string "after", the new document is returned. The default is
"before".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
underlying HTTP request. This method uses the collection-level timeout
by default.</p></td>
</tr>
</tbody>
</table>

An error occurs if the provided replacement has a different ID because
the ID can’t be changed. In most cases, it is best to omit the `_id`
field from the replacement.

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection
    import astrapy

    collection.insert_one({"_id": "rule1", "text": "all animals are equal"})

    collection.find_one_and_replace(
        {"_id": "rule1"},
        {"text": "some animals are more equal!"},
    )
    # prints: {'_id': 'rule1', 'text': 'all animals are equal'}
    collection.find_one_and_replace(
        {"text": "some animals are more equal!"},
        {"text": "and the pigs are the rulers"},
        return_document=astrapy.constants.ReturnDocument.AFTER,
    )
    # prints: {'_id': 'rule1', 'text': 'and the pigs are the rulers'}
    collection.find_one_and_replace(
        {"_id": "rule2"},
        {"text": "F=ma^2"},
        return_document=astrapy.constants.ReturnDocument.AFTER,
    )
    # (returns None for no matches)
    collection.find_one_and_replace(
        {"_id": "rule2"},
        {"text": "F=ma"},
        upsert=True,
        return_document=astrapy.constants.ReturnDocument.AFTER,
        projection={"_id": False},
    )
    # prints: {'text': 'F=ma'}

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#findOneAndReplace.findOneAndReplace-2\[API
Reference\].

    const docBefore = await collection.findOneAndReplace(
      { _id: 123 },
      { text: 'some animals are more equal!' },
    );

Locate and replace a document, returning the replaced document,
additionally creating it if nothing is found.

    const docBefore = await collection.findOneAndReplace(
      { _id: 123 },
      { text: 'some animals are more equal!' },
      { upsert: true  },
    );

Locate and replace the document most similar to a provided query vector.

    const docBefore = await collection.findOneAndReplace(
      {},
      { name: 'Zoe', desc: 'The new best match' },
      { sort: { $vector: [0.1, 0.2, 0.3] } },
    );

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Filter.html[Filter&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>A filter to select the document to
replace.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>replacement</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/NoId.html[NoId&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>The replacement document, which
contains no _id field.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/FindOneAndReplaceOptions.html[FindOneAndReplaceOptions]</code></p></td>
<td style="text-align: left;"><p>The options for this
operation.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/FindOneAndReplaceOptions.html[FindOneAndReplaceOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndReplaceOptions.html#returnDocument[returnDocument]</p></td>
<td
style="text-align: left;"><p><code>'before' | 'after'</code></p></td>
<td style="text-align: left;"><p>Specifies whether to return the
original or replaced document.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndReplaceOptions.html#upsert[upsert?]</p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>If true, creates a new document if no
document matches the filter.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndReplaceOptions.html#projection[projection?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Projection.html[Projection]</code></p></td>
<td style="text-align: left;"><p>Specifies which fields should be
included/excluded in the returned documents. Defaults to including all
fields.</p>
<p>When specifying a projection, it’s the user’s responsibility to
handle the return type carefully. Consider type-casting.</p>
<p>Can only be used when performing a vector search.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndReplaceOptions.html#sort[sort?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Sort.html[Sort]</code></p></td>
<td style="text-align: left;"><p>Specifies the order in which the
documents are returned. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations">section
on sorting</a> for further detail. The sort may contain
<code>$vector</code> or <code>$vectorize</code> clauses, but not both at
once.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndReplaceOptions.html#maxTimeMS[maxTimeMS?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>The maximum time in milliseconds that
the client should wait for the operation to complete for each single one
of the underlying HTTP requests.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndReplaceOptions.html#includeResultMetadata[includeResultMetadata?]</p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>When true, returns alongside the
document, an ok field with a value of 1 if the command executed
successfully.</p></td>
</tr>
</tbody>
</table>

An error occurs if the provided replacement has a different ID because
the ID can’t be changed. In most cases, it is best to omit the `_id`
field from the replacement.

Returns:

`Promise<{ts-client-api-ref-url}/types/WithId.html[WithId<Schema>] | null>` -
The document before/after the update, depending on the type of
`returnDocument`, or `null` if no matches are found.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      // Insert some document
      await collection.insertOne({ _id: 'rule1', text: 'all animals are equal' });

      // { _id: 'rule1', text: 'all animals are equal' }
      await collection.findOneAndReplace(
        { _id: 'rule1' },
        { text: 'some animals are more equal!' },
        { returnDocument: 'before' }
      );

      // { _id: 'rule1', text: 'and the pigs are the rulers' }
      await collection.findOneAndReplace(
        { text: 'some animals are more equal!' },
        { text: 'and the pigs are the rulers' },
        { returnDocument: 'after' }
      );

      // null
      await collection.findOneAndReplace(
        { _id: 'rule2' },
        { text: 'F=ma^2' },
        { returnDocument: 'after' }
      );

      // { text: 'F=ma' }
      await collection.findOneAndReplace(
        { _id: 'rule2' },
        { text: 'F=ma' },
        { upsert: true, returnDocument: 'after', projection: { _id: false } }
      );
    })();

Java  
    // Synchronous
    Optional<T> findOneAndReplace(Filter filter, T replacement);
    Optional<T> findOneAndReplace(Filter filter, T replacement, FindOneAndReplaceOptions options);

    // Asynchronous
    CompletableFuture<Optional<T>> findOneAndReplaceAsync(Filter filter, T replacement);
    CompletableFuture<Optional<T>> findOneAndReplaceAsync(Filter filter, T replacement, FindOneAndReplaceOptions options);

Returns:

`Optional<T>` - Return the a document that matches the filter. Whether
`returnDocument` is set to before or after it will return the document
before or after update accordingly.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter (optional)</p></td>
<td style="text-align: left;"><p><code>Filter</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>replacement</p></td>
<td style="text-align: left;"><p><code>T</code></p></td>
<td style="text-align: left;"><p>This is the document that will replace
the existing one if exist. It flag <code>upsert</code> is set to true
and no document is found, this document will be inserted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options(optional)</p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/FindOneAndReplaceOptions.html"><code>FindOneAndReplaceOptions</code></a></p></td>
<td style="text-align: left;"><p>Provide list of options for
findOneAndReplace operation as a <code>Sort</code> clause (sort on
vector or any other field) or a <code>Projection</code> clause, upsert
flag and <code>returnDocument</code> flag.</p></td>
</tr>
</tbody>
</table>

Sample definition of
[`FindOneAndReplaceOptions`](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/FindOneAndReplaceOptions.html):

     FindOneAndReplaceOptions options = FindOneAndReplaceOptions.Builder
      .projection(Projections.include("field1"))
      .sort(Sorts.ascending("field1"))
      .upsert(true)
      .returnDocumentAfter();

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/FindOneAndReplace.java[role=include]

cURL  
Use the Data API `fineOneAndReplace` command to find an existing
document that matches the filter criteria and replace the document with
a new one.

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
        "findOneAndReplace": {
          "filter": {
            "_id": "14"
            },
            "replacement": { "customer.name": "Ann Jones", "status": "inactive" }
        }
    }' | jq
    # | jq is optional.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>findOneAndReplace</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>Finds a single document that matches a
specified filter and replaces it with the provided replacement document.
This operation is atomic within a single document.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td style="text-align: left;"><p>clause</p></td>
<td style="text-align: left;"><p>Specifies the criteria for selecting
the document to replace. In this example, it’s a document with an
<code>_id</code> value of 14.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>replacement</p></td>
<td style="text-align: left;"><p>clause</p></td>
<td style="text-align: left;"><p>Specifies the new content of the
document that will replace the existing document found using the filter
criteria. The replacement content provided is a document with two
fields:</p>
<ul>
<li><p><code>customer.name</code>: Set to "Ann Jones" in this
examples.</p></li>
<li><p><code>status</code>: Set to "inactive" in this example.</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Replace a document

Replace a document in the collection with a new one.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.replace\_one\[API
Reference\].

    replace_result = collection.replace_one(
        {"Marco": {"$exists": True}},
        {"Buda": "Pest"},
    )

Replace a document in the collection with a new one, creating a new one
if no match is found.

    replace_result = collection.replace_one(
        {"Marco": {"$exists": True}},
        {"Buda": "Pest"},
        upsert=True,
    )

Replace the document most similar to a provided query vector.

    collection.replace_one(
        {},
        {"name": "Zoo", "desc": "the new best match"},
        sort={"$vector": [0.1, 0.2, 0.3]},
    )

Returns:

`{py-client-api-ref-url}/results.html#astrapy.results.UpdateResult[UpdateResult]` -
An object representing the response from the database after the replace
operation. It includes information about the operation.

    UpdateResult(raw_results=[{'data': {'document': {'_id': '1', 'Marco': 'Polo'}}, 'status': {'matchedCount': 1, 'modifiedCount': 1}}], update_info={'n': 1, 'updatedExisting': True, 'ok': 1.0, 'nModified': 1})

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td style="text-align: left;"><p><code>Dict[str, Any]</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>replacement</p></td>
<td style="text-align: left;"><p><code>Dict[str, Any]</code></p></td>
<td style="text-align: left;"><p>the new document to write into the
collection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>sort</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>With this dictionary parameter one can
control the sorting order of the documents matching the filter,
effectively determining what document will come first and hence be the
replaced one. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations"><code>sort</code>
examples</a> for more on sorting. This parameter can express
<code>$vector</code> or <code>$vectorize</code> sort clauses, but not
both at the same time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>upsert</p></td>
<td style="text-align: left;"><p><code>bool = False</code></p></td>
<td style="text-align: left;"><p>This parameter controls the behavior in
absence of matches. If True, <code>replacement</code> is inserted as a
new document if no matches are found on the collection. If False, the
operation silently does nothing in case of no matches.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
underlying HTTP request. This method uses the collection-level timeout
by default.</p></td>
</tr>
</tbody>
</table>

An error occurs if the provided replacement has a different ID because
the ID can’t be changed. In most cases, it is best to omit the `_id`
field from the replacement.

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    collection.insert_one({"Marco": "Polo"})
    collection.replace_one({"Marco": {"$exists": True}}, {"Buda": "Pest"})
     prints: UpdateResult(raw_results=..., update_info={'n': 1, 'updatedExisting': True, 'ok': 1.0, 'nModified': 1})
    collection.find_one({"Buda": "Pest"})
     prints: {'_id': '8424905a-...', 'Buda': 'Pest'}
    collection.replace_one({"Mirco": {"$exists": True}}, {"Oh": "yeah?"})
     prints: UpdateResult(raw_results=..., update_info={'n': 0, 'updatedExisting': False, 'ok': 1.0, 'nModified': 0})
    collection.replace_one({"Mirco": {"$exists": True}}, {"Oh": "yeah?"}, upsert=True)
     prints: UpdateResult(raw_results=..., update_info={'n': 1, 'updatedExisting': False, 'ok': 1.0, 'nModified': 0, 'upserted': '931b47d6-...'})

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#replaceOne\[API
Reference\].

    const result = await collection.replaceOne(
      { 'Marco': 'Polo' },
      { 'Buda': 'Pest' },
    );

Replace a document in the collection with a new one, creating a new one
if no match is found.

    const result = await collection.replaceOne(
      { 'Marco': 'Polo' },
      { 'Buda': 'Pest' },
      { upsert: true },
    );

Replace the document most similar to a provided query vector.

    const result = await collection.replaceOne(
      {},
      { name: "Zoe", desc: "The new best match" },
      { sort: { $vector: [0.1, 0.2, 0.3] } },
    );

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Filter.html[Filter&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>A filter to select the document to
replace.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>replacement</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/NoId.html[NoId&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>The replacement document, which
contains no _id field.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/ReplaceOneOptions.html[ReplaceOneOptions]</code></p></td>
<td style="text-align: left;"><p>The options for this
operation.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/ReplaceOneOptions.html[ReplaceOneOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/ReplaceOneOptions.html#upsert[upsert?]</p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>If true, creates a new document if no
document matches the filter.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/ReplaceOneOptions.html#sort[sort?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Sort.html[Sort]</code></p></td>
<td style="text-align: left;"><p>Specifies the order in which the
documents are returned. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations">section
on sorting</a> for further detail. The sort may contain
<code>$vector</code> or <code>$vectorize</code> clauses, but not both at
once.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/ReplaceOneOptions.html#maxTimeMS[maxTimeMS?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>The maximum time in milliseconds that
the client should wait for the operation to complete for each single one
of the underlying HTTP requests.</p></td>
</tr>
</tbody>
</table>

An error occurs if the provided replacement has a different ID because
the ID can’t be changed. In most cases, it is best to omit the `_id`
field from the replacement.

Returns:

`Promise<{ts-client-api-ref-url}/types/ReplaceOneResult.html[ReplaceOneResult<Schema>]>` -
The result of the replacement operation.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      // Insert some document
      await collection.insertOne({ 'Marco': 'Polo' });

      // { modifiedCount: 1, matchedCount: 1, upsertedCount: 0 }
      await collection.replaceOne(
        { 'Marco': { '$exists': true } },
        { 'Buda': 'Pest' }
      );

      // { _id: '3756ce75-aaf1-430d-96ce-75aaf1730dd3', Buda: 'Pest' }
      await collection.findOne({ 'Buda': 'Pest' });

      // { modifiedCount: 0, matchedCount: 0, upsertedCount: 0 }
      await collection.replaceOne(
        { 'Mirco': { '$exists': true } },
        { 'Oh': 'yeah?' }
      );

      // { modifiedCount: 0, matchedCount: 0, upsertedId: '...', upsertedCount: 1 }
      await collection.replaceOne(
        { 'Mirco': { '$exists': true } },
        { 'Oh': 'yeah?' },
        { upsert: true }
      );
    })();

Java  
    // Synchronous
    UpdateResult replaceOne(Filter filter, T replacement);
    UpdateResult replaceOne(Filter filter, T replacement, ReplaceOneOptions options);

    // Asynchronous
    CompletableFuture<UpdateResult> replaceOneAsync(Filter filter, T replacement);
    CompletableFuture<UpdateResult> replaceOneAsync(Filter filter, T replacement, ReplaceOneOptions options);

Returns:

UpdateResult - Return a wrapper object with the result of the operation.
The object contains the number of documents matched (`matchedCount`) and
updated (`modifiedCount`)

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter (optional)</p></td>
<td style="text-align: left;"><p><code>Filter</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>replacement</p></td>
<td style="text-align: left;"><p><code>T</code></p></td>
<td style="text-align: left;"><p>This is the document that will replace
the existing one if exist. It flag <code>upsert</code> is set to true
and no document is found, this document will be inserted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options(optional)</p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/ReplaceOneOptions.html"><code>ReplaceOneOptions</code></a></p></td>
<td style="text-align: left;"><p>Provide list of options for
<code>replaceOne()</code> operation and especially the
<code>upsert</code> flag.</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/FindOneAndReplace.java[role=include]

cURL  
See [Find and replace a
document](api-reference:documents.xml#find-and-replace-a-document).

# Find and delete a document

Locate a document matching a filter condition and delete it, returning
the document itself.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.find\_one\_and\_delete\[API
Reference\].

    deleted_document = collection.find_one_and_delete({"status": "stale_entry"})

Delete the document most similar to a provided query vector, returning
it.

    deleted_document = collection.find_one_and_delete(
        {},
        sort={"$vector": [0.1, 0.2, 0.3]},
    )

Returns:

`Dict[str, Any]` - The document that was just deleted (or a projection
thereof, as requested). If no matches are found, `None` is returned.

    {'_id': 199, 'status': 'stale_entry', 'request_id': 'A4431'}

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>projection</p></td>
<td
style="text-align: left;"><p><code>Optional[Union[Iterable[str], Dict[str, bool]]]</code></p></td>
<td style="text-align: left;"><p>Used to select a subset of fields in
the documents being returned. The projection can be: an iterable over
the included field names; a dictionary {field_name: True} to positively
select certain fields; or a dictionary {field_name: False} if one wants
to exclude specific fields from the response. Special document fields
(e.g. <code>_id</code>, <code>$vector</code>) are controlled
individually. The default projection does not necessarily include all
fields of the document. See the <a
href="api-reference:documents.xml#example-values-for-projection-operations"><code>projection</code>
examples</a> for more on this parameter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>sort</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>With this dictionary parameter one can
control the sorting order of the documents matching the filter,
effectively determining what document will come first and hence be the
deleted one. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations"><code>sort</code>
examples</a> for more on sorting. This parameter can express
<code>$vector</code> or <code>$vectorize</code> sort clauses, but not
both at the same time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
underlying HTTP request. This method uses the collection-level timeout
by default.</p></td>
</tr>
</tbody>
</table>

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    collection.insert_many(
        [
            {"species": "swan", "class": "Aves"},
            {"species": "frog", "class": "Amphibia"},
        ],
    )
    collection.find_one_and_delete(
        {"species": {"$ne": "frog"}},
        projection={"species": True},
    )
    # prints: {'_id': '5997fb48-...', 'species': 'swan'}
    collection.find_one_and_delete({"species": {"$ne": "frog"}})
    # (returns None for no matches)

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#findOneAndDelete.findOneAndDelete-2\[API
Reference\].

    const deletedDoc = await collection.findOneAndDelete({ status: 'stale_entry' });

Delete the document most similar to a provided query vector, returning
it.

    const deletedDoc = await collection.findOneAndDelete(
      {},
      { sort: { $vector: [0.1, 0.2, 0.3] } },
    );

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Filter.html[Filter&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>A filter to select the document to
delete.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/FindOneAndDeleteOptions.html[FindOneAndDeleteOptions]</code></p></td>
<td style="text-align: left;"><p>The options for this
operation.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/FindOneAndDeleteOptions.html[FindOneAndDeleteOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndDeleteOptions.html#projection[projection?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Projection.html[Projection]</code></p></td>
<td style="text-align: left;"><p>Specifies which fields should be
included/excluded in the returned documents. Defaults to including all
fields.</p>
<p>When specifying a projection, it’s the user’s responsibility to
handle the return type carefully. Consider type-casting.</p>
<p>Can only be used when performing a vector search.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndDeleteOptions.html#sort[sort?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Sort.html[Sort]</code></p></td>
<td style="text-align: left;"><p>Specifies the order in which the
documents are returned. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations">section
on sorting</a> for further detail. The sort may contain
<code>$vector</code> or <code>$vectorize</code> clauses, but not both at
once.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndDeleteOptions.html#maxTimeMS[maxTimeMS?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>The maximum time in milliseconds that
the client should wait for the operation to complete for each single one
of the underlying HTTP requests.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/FindOneAndDeleteOptions.html#includeResultMetadata[includeResultMetadata?]</p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>When true, returns alongside the
document, an ok field with a value of 1 if the command executed
successfully.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<{ts-client-api-ref-url}/types/WithId.html[WithId<Schema>] | null>` -
The document that was deleted, or `null` if no matches are found.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      // Insert some document
      await collection.insertMany([
        { species: 'swan', class: 'Aves' },
        { species: 'frog', class: 'Amphibia' },
      ]);

      // { _id: '...', species: 'swan' }
      await collection.findOneAndDelete(
        { species: { $ne: 'frog' } },
        { projection: { species: 1 } },
      );

      // null
      await collection.findOneAndDelete(
        { species: { $ne: 'frog' } },
      );
    })();

Java  
    // Synchronous
    Optional<T> findOneAndDelete(Filter filter);
    Optional<T> findOneAndDelete(Filter filter, FindOneAndDeleteOptions options);

    // Asynchronous
    CompletableFuture<Optional<T>> findOneAndDeleteAsync(Filter filter);
    CompletableFuture<Optional<T>> findOneAndDeleteAsync(Filter filter, FindOneAndDeleteOptions options);

Returns:

[`DeleteResult`](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/DeleteResult.html) -
Wrapper that contains the deleted count.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter (optional)</p></td>
<td style="text-align: left;"><p><code>Filter</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options(optional)</p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/FindOneAndDeleteOptions.html"><code>FindOneAndDeleteOptions</code></a></p></td>
<td style="text-align: left;"><p>Provide list of options a delete one
such as a <code>Sort</code> clause (sort on vector or any other field)
or a <code>Projection</code> clause</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/FindOneAndDelete.java[role=include]

cURL  
Use the Data API `findOneAndDelete` command to find and delete a single
document.

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
        "findOneAndDelete": {
            "filter": {
                "customer.name": "Fred Smith",
                "_id": "13"
            }
        }
    }' | jq
    # | jq is optional.

Response:

    {
       "status": {
          "deletedCount": 1
       }
    }

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>findOneAndDelete</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>Deletes the first document that matches
the given criteria. If no matching document is found, no action is
taken.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td style="text-align: left;"><p>clause</p></td>
<td style="text-align: left;"><p>Used to identify the document meant for
deletion. In this example, the filter is comprised of
<code>customer.name</code> and document <code>_id</code>
values.</p></td>
</tr>
</tbody>
</table>

# Delete a document

Locate and delete a single document from a collection.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.delete\_one\[API
Reference\].

    response = collection.delete_one({ "_id": "1" })

Locate and delete a single document from a collection by any attribute
(as long as it is covered by the collection’s indexing configuration).

    document = collection.delete_one({"location": "warehouse_C"})

Locate and delete a single document from a collection by an arbitrary
filtering clause.

    document = collection.delete_one({"tag": {"$exists": True}})

Delete the most similar document to a given vector.

    result = collection.delete_one({}, sort={"$vector": [.12, .52, .32]})

Generate a vector from a string and delete the most similar document.

    result = collection.delete_one({}, sort={"$vectorize": "Text to vectorize"})

Returns:

`{py-client-api-ref-url}/results.html#astrapy.results.DeleteResult[DeleteResult]` -
An object representing the response from the database after the delete
operation. It includes information about the success of the operation.

    DeleteResult(raw_results=[{'status': {'deletedCount': 1}}], deleted_count=1)

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>sort</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>With this dictionary parameter one can
control the sorting order of the documents matching the filter,
effectively determining what document will come first and hence be the
deleted one. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations"><code>sort</code>
examples</a> for more on sorting. This parameter can express
<code>$vector</code> or <code>$vectorize</code> sort clauses, but not
both at the same time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
underlying HTTP request. This method uses the collection-level timeout
by default.</p></td>
</tr>
</tbody>
</table>

Example:

    from astrapy import DataAPIClient
    import astrapy
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    collection.insert_many([{"seq": 1}, {"seq": 0}, {"seq": 2}])

    collection.delete_one({"seq": 1})
    # prints: DeleteResult(raw_results=..., deleted_count=1)
    collection.distinct("seq")
    # prints: [0, 2]
    collection.delete_one(
        {"seq": {"$exists": True}},
        sort={"seq": astrapy.constants.SortDocuments.DESCENDING},
    )
    # prints: DeleteResult(raw_results=..., deleted_count=1)
    collection.distinct("seq")
    # prints: [0]
    collection.delete_one({"seq": 2})
    # prints: DeleteResult(raw_results=..., deleted_count=0)

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#deleteOne\[API
Reference\].

    const result = await collection.deleteOne({ _id: '1' });

Locate and delete a single document from a collection.

    const result = await collection.deleteOne({ location: 'warehouse_C' });

Locate and delete a single document from a collection by an arbitrary
filtering clause.

    const result = await collection.deleteOne({ tag: { $exists: true } });

Delete the most similar document to a given vector.

    const result = await collection.deleteOne({}, { sort: { $vector: [.12, .52, .32] } });

Generate a vector from a string and delete the most similar document.

    const result = await collection.deleteOne({}, { sort: { $vectorize: 'Text to vectorize' } });

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Filter.html[Filter&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>A filter to select the document to
delete.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/DeleteOneOptions.html[DeleteOneOptions]</code></p></td>
<td style="text-align: left;"><p>The options for this
operation.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/interfaces/DeleteOneOptions.html[DeleteOneOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DeleteOneOptions.html#sort[sort?]</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Sort.html[Sort]</code></p></td>
<td style="text-align: left;"><p>Specifies the order in which the
documents are returned. See the <a
href="api-reference:documents.xml#example-values-for-sort-operations">section
on sorting</a> for further detail. The sort may contain
<code>$vector</code> or <code>$vectorize</code> clauses, but not both at
once.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/DeleteOneOptions.html#maxTimeMS[maxTimeMS?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>The maximum time in milliseconds that
the client should wait for the operation to complete for each single one
of the underlying HTTP requests.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<{ts-client-api-ref-url}/interfaces/DeleteOneResult.html[DeleteOneResult]>` -
The result of the deletion operation.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      // Insert some document
      await collection.insertMany([{ seq: 1 }, { seq: 0 }, { seq: 2 }]);

      // { deletedCount: 1 }
      await collection.deleteOne({ seq: 1 });

      // [0, 2]
      await collection.distinct('seq');

      // { deletedCount: 1 }
      await collection.deleteOne({ seq: { $exists: true } }, { sort: { seq: -1 } });

      // [0]
      await collection.distinct('seq');

      // { deletedCount: 0 }
      await collection.deleteOne({ seq: 2 });
    })();

Java  
    // Synchronous
    DeleteResult deleteOne(Filter filter);
    DeleteResult deleteOne(Filter filter, DeleteOneOptions options);

    // Asynchronous
    CompletableFuture<DeleteResult> deleteOneAsync(Filter filter);
    CompletableFuture<DeleteResult> deleteOneAsync(Filter filter, DeleteOneOptions options);

Returns:

[`DeleteResult`](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/DeleteResult.html) -
Wrapper that contains the deleted count.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter (optional)</p></td>
<td style="text-align: left;"><p><code>Filter</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. See
<a href="api-reference:overview.xml#operators">{astra-api} operators</a>
for the full list of operators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options(optional)</p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/DeleteOneOptions.html"><code>DeleteOneOptions</code></a></p></td>
<td style="text-align: left;"><p>Provide list of options a delete one
such as a <code>Sort</code> clause (sort on vector or any other
field)</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/DeleteOne.java[role=include]

cURL  
The Data API `deleteOne` command deletes a single document. In this
example, the deletion would occur where the `tags` value is `first`.

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
      "deleteOne": {
        "filter": {
          "tags": "first"
        }
      }
    }' | jq
    # `| jq` is optional.

Response:

    {
       "status": {
          "deletedCount": 1
       }
    }

Properties:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>deleteOne</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>Delete a matching document from a
collection based on the provided filter criteria.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td style="text-align: left;"><p>clause</p></td>
<td style="text-align: left;"><p>Provides the conditions that the
database uses to identify one or more document(s) meant for
deletion.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>tags</p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>A filtering key that targets a specific
property in the database’s documents.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>first</p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>A value iassociated with the
<code>tags</code> key, which in this example must contain the string
"first" to meet the deletion criteria.</p></td>
</tr>
</tbody>
</table>

# Delete documents

Delete multiple documents from a collection.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.delete\_many\[API
Reference\].

    delete_result = collection.delete_many({"status": "processed"})

Returns:

`{py-client-api-ref-url}/results.html#astrapy.results.DeleteResult[DeleteResult]` -
An object representing the response from the database after the delete
operation. It includes information about the success of the operation.

    DeleteResult(raw_results=[{'status': {'deletedCount': 2}}], deleted_count=2)

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>Optional[Dict[str, Any]]</code></p></td>
<td style="text-align: left;"><p>A predicate expressed as a dictionary
according to the Data API filter syntax. Examples are <code>{}</code>,
<code>{"name": "John"}</code>, <code>{"price": {"$lt": 100}}</code>,
<code>{"$and": [{"name": "John"}, {"price": {"$lt": 100}}]}</code>. For
the full list of operators <a
href="api-reference:overview.xml#operators">{astra-api} operators</a> .
If you provide an empty filter (<code>{}</code>), then the command
<strong>deletes all documents (completely emptying the
collection)</strong> and returns the special value of
<code>deleted_count=-1</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
operation. This method uses the collection-level timeout by default. You
may need to increase the timeout duration when deleting a large number
of documents, as the operation will require multiple HTTP requests in
sequence.</p></td>
</tr>
</tbody>
</table>

Example:

    from astrapy import DataAPIClient
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    collection.insert_many([{"seq": 1}, {"seq": 0}, {"seq": 2}])

    collection.delete_many({"seq": {"$lte": 1}})
    # prints: DeleteResult(raw_results=..., deleted_count=2)
    collection.distinct("seq")
    # prints: [2]
    collection.delete_many({"seq": {"$lte": 1}})
    # prints: DeleteResult(raw_results=..., deleted_count=0)

    # An empty filter deletes all documents and completely empties the collection:
    collection.delete_many({})
    # prints: DeleteResult(raw_results=..., deleted_count=-1)

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#deleteMany\[API
Reference\].

Delete all documents matching a filter.

    const result = await collection.deleteMany({ status: 'processed' });

Delete all documents. Proceed with caution.

    const result = await collection.deleteMany({});

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/Filter.html[Filter&lt;Schema&gt;]</code></p></td>
<td style="text-align: left;"><p>A filter to select the document to
delete.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/interfaces/WithTimeout.html[WithTimeout]</code></p></td>
<td style="text-align: left;"><p>The options (the timeout) for this
operation.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<{ts-client-api-ref-url}/interfaces/DeleteManyResult.html[DeleteManyResult]>` -
The result of the deletion operation.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      // Insert some document
      await collection.insertMany([{ seq: 1 }, { seq: 0 }, { seq: 2 }]);

      // { deletedCount: 1 }
      await collection.deleteMany({ seq: { $lte: 1 } });

      // [2]
      await collection.distinct('seq');

      // { deletedCount: 0 }
      await collection.deleteMany({ seq: { $lte: 1 } });

      // { deletedCount: -1 }
      await collection.deleteMany({});
    })();

Java  
    // Synchronous
    DeleteResult deleteMany(Filter filter);

    // Asynchronous
    CompletableFuture<DeleteResult> deleteManyAsync(Filter filter);

    // Delete all - Proceed with caution
    DeleteResult deleteMany();

Returns:

[`DeleteResult`](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/DeleteResult.html) -
Wrapper that contains the deleted count.

Same as a few other methods the delete operation can delete only 20
documents at a time. `deleteMany()` can takes time while it iterates
until it confirms that there are no more documents matching the filter.

To delete all documents, run a `deleteMany()` without any filter (an
empty filter). This can take time while the operation iterates until it
confirms that there are no more documents to delete.

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/DeleteMany.java[role=include]

cURL  
The following JSON payload is designed to delete documents where the
status is inactive.

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
      "deleteMany": {
        "filter": {
          "status": "inactive"
        }
      }
    }' | jq
    # | jq is optional.

Response:

    {
       "status": {
          "deletedCount": 20
       }
    }

Properties:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>deleteMany</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>Deletes all matching documents from a
collection based on the provided filter criteria.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>filter</p></td>
<td style="text-align: left;"><p>option</p></td>
<td style="text-align: left;"><p>Provides the conditions that the
database uses to identify one or more document(s) meant for
deletion.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>status</p></td>
<td style="text-align: left;"><p>option</p></td>
<td style="text-align: left;"><p>Used for filtering to decide which
documents may be deleted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>inactive</p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>The <code>inactive</code> value is
associated with the <code>status</code> key. In this example, it must
contain the string "inactive" to meet the deletion criteria.</p></td>
</tr>
</tbody>
</table>

The following JSON payload is designed to delete all documents in a
collection.

If used with an empty `{ }` filter or an empty body, the Data API
`deleteMany` command deletes all the data in your connected database’s
collection. This command, with an empty filter or body, bypasses the
guardrail of up to 20 rows deleted per transaction. Recall that the auth
token is associated with the privileged Database Administrator role. If
all data is removed in a collection, the response contains
`deletedCount: -1` (meaning all rows).

    curl -s --location \
    --request POST ${ASTRA_DB_API_ENDPOINT}/api/json/v1/${ASTRA_DB_KEYSPACE}/${ASTRA_DB_COLLECTION} \
    --header "Token: ${ASTRA_DB_APPLICATION_TOKEN}" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data '{
      "deleteMany": {
      }
    }' | jq
    # | jq is optional.

Response:

    {
       "status": {
          "deletedCount": -1
       }
    }

Properties:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>deleteMany</p></td>
<td style="text-align: left;"><p>command</p></td>
<td style="text-align: left;"><p>Deletes all matching documents from a
collection based on the provided filter criteria.</p></td>
</tr>
</tbody>
</table>

# Execute multiple write operations

Execute a (reusable) list of write operations on a collection with a
single command.

Python  
View this topic in more detail on the
{py-client-api-ref-url}/collection.html#astrapy.collection.Collection.bulk\_write\[API
Reference\].

    bw_results = collection.bulk_write(
        [
            InsertMany([{"a": 1}, {"a": 2}]),
            ReplaceOne(
                {"z": 9},
                replacement={"z": 9, "replaced": True},
                upsert=True,
            ),
        ],
    )

Returns:

`{py-client-api-ref-url}/results.html#astrapy.results.BulkWriteResult[BulkWriteResult]` -
A single object summarizing the whole list of requested operations. The
keys in the map attributes of the result (when present) are the integer
indices of the corresponding operation in the `requests` iterable.

    BulkWriteResult(bulk_api_results={0: ..., 1: ...}, deleted_count=0, inserted_count=3, matched_count=0, modified_count=0, upserted_count=1, upserted_ids={1: '2addd676-...'})

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>requests</p></td>
<td
style="text-align: left;"><p><code>Iterable[{py-client-api-ref-url}/operations.html#astrapy.operations.BaseOperation[BaseOperation]]</code></p></td>
<td style="text-align: left;"><p>An iterable over concrete subclasses of
<code>{py-client-api-ref-url}/operations.html#astrapy.operations.BaseOperation[BaseOperation]</code>,
such as
<code>{py-client-api-ref-url}/operations.html#astrapy.operations.InsertMany[InsertMany]</code>
or
<code>{py-client-api-ref-url}/operations.html#astrapy.operations.ReplaceOne[ReplaceOne]</code>.
Each such object represents an operation ready to be executed on a
collection, and is instantiated by passing the same parameters as one
would the corresponding collection method.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>ordered</p></td>
<td style="text-align: left;"><p><code>bool</code></p></td>
<td style="text-align: left;"><p>Whether to launch the
<code>requests</code> one after the other or in arbitrary order,
possibly in a concurrent fashion. DataStax suggests False (default) when
possible for faster performance.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>concurrency</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>Maximum number of concurrent operations
executing at a given time. It cannot be more than one for ordered bulk
writes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max_time_ms</p></td>
<td style="text-align: left;"><p><code>Optional[int]</code></p></td>
<td style="text-align: left;"><p>A timeout, in milliseconds, for the
whole bulk write. This method uses the collection-level timeout by
default. You may need to increase the timeout duration depending on the
number of operations. If the method call times out, there’s no guarantee
about how much of the bulk write was completed.</p></td>
</tr>
</tbody>
</table>

Example:

    from astrapy import DataAPIClient
    from astrapy.operations import (
        InsertOne,
        InsertMany,
        UpdateOne,
        UpdateMany,
        ReplaceOne,
        DeleteOne,
        DeleteMany,
    )
    client = DataAPIClient("TOKEN")
    database = my_client.get_database("API_ENDPOINT")
    collection = database.my_collection

    op1 = InsertMany([{"a": 1}, {"a": 2}])
    op2 = ReplaceOne({"z": 9}, replacement={"z": 9, "replaced": True}, upsert=True)
    collection.bulk_write([op1, op2])
    # prints: BulkWriteResult(bulk_api_results={0: ..., 1: ...}, deleted_count=0, inserted_count=3, matched_count=0, modified_count=0, upserted_count=1, upserted_ids={1: '2addd676-...'})
    collection.count_documents({}, upper_bound=100)
    # prints: 3
    collection.distinct("replaced")
    # prints: [True]

TypeScript  
View this topic in more detail on the
{ts-client-api-ref-url}/classes/Collection.html#bulkWrite\[API
Reference\].

    const results = await collection.bulkWrite([
      { insertOne: { a: '1' } },
      { insertOne: { a: '2' } },
      { replaceOne: { z: '9' }, replacement: { z: '9', replaced: true }, upsert: true },
    ]);

Parameters:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>operations</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/AnyBulkWriteOperation.html[AnyBulkWriteOperation&lt;Schema&gt;][]</code></p></td>
<td style="text-align: left;"><p>The operations to perform.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options?</p></td>
<td
style="text-align: left;"><p><code>{ts-client-api-ref-url}/types/BulkWriteOptions.html[BulkWriteOptions]</code></p></td>
<td style="text-align: left;"><p>The options for this
operation.</p></td>
</tr>
</tbody>
</table>

Options
(`{ts-client-api-ref-url}/types/BulkWriteOptions.html[BulkWriteOptions]`):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/BulkWriteUnorderedOptions.html#ordered[ordered?]</p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>You may set the <code>ordered</code>
option to <code>true</code> to stop the operation after the first error;
otherwise all operations may be parallelized and processed in arbitrary
order, improving, perhaps vastly, performance.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/BulkWriteUnorderedOptions.html#concurrency[concurrency?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>You can set the
<code>concurrency</code> option to control how many network requests are
made in parallel on unordered operations. Defaults to
<code>8</code>.</p>
<p>Not available for ordered operations.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>{ts-client-api-ref-url}/interfaces/BulkWriteUnorderedOptions.html#maxTimeMS[maxTimeMS?]</p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"><p>The maximum time in milliseconds that
the client should wait for the operation to complete.</p></td>
</tr>
</tbody>
</table>

Returns:

`Promise<{ts-client-api-ref-url}/classes/BulkWriteResult.html[BulkWriteResult<Schema>]>` -
A promise that resolves to a summary of the performed operations.

Example:

    import { DataAPIClient } from '@datastax/astra-db-ts';

    // Reference an untyped collection
    const client = new DataAPIClient('TOKEN');
    const db = client.db('ENDPOINT', { namespace: 'NAMESPACE' });
    const collection = db.collection('COLLECTION');

    (async function () {
      // Insert some document
      await collection.bulkWrite([
        { insertOne: { document: { a: 1 } } },
        { insertOne: { document: { a: 2 } } },
        { replaceOne: { filter: { z: 9 }, replacement: { z: 9, replaced: true }, upsert: true } },
      ]);

      // 3
      await collection.countDocuments({}, 100);

      // [true]
      await collection.distinct('replaced');
    })();

Java  
    // Synchronous
    BulkWriteResult bulkWrite(List<Command> commands);
    BulkWriteResult bulkWrite(List<Command> commands, BulkWriteOptions options);

    // Asynchronous
    CompletableFuture<BulkWriteResult> bulkWriteAsync(List<Command> commands);
    CompletableFuture<BulkWriteResult> bulkWriteAsync(List<Command> commands, BulkWriteOptions options);

Returns:

[`BulkWriteResult`](https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/BulkWriteResult.html) -
Wrapper with the list of responses for each command.

Parameters:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>commands</p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/Command.html"><code>List&lt;Command&gt;</code></a></p></td>
<td style="text-align: left;"><p>List of the generic
<code>Command</code> to execute.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>options(optional)</p></td>
<td style="text-align: left;"><p><a
href="https://datastaxdevs.github.io/astra-db-java/latest/com/datastax/astra/client/model/BulkWriteOptions.html"><code>BulkWriteOptions</code></a></p></td>
<td style="text-align: left;"><p>Provide list of options for those
commands like <code>ordered</code> or <code>concurrency</code>.</p></td>
</tr>
</tbody>
</table>

Example:

    link:https://raw.githubusercontent.com/datastax/astra-db-java/main/examples/src/main/java/com/datastax/astra/client/collection/BulkWrite.java[role=include]

# See also

-   [api-reference:overview.xml](api-reference:overview.xml)

-   [api-reference:dataapiclient.xml](api-reference:dataapiclient.xml)

-   [api-reference:databases.xml](api-reference:databases.xml)

-   [api-reference:collections.xml](api-reference:collections.xml)

-   [api-reference:administration.xml](api-reference:administration.xml)

-   [Data API
    changelog](https://github.com/stargate/data-api/blob/main/CHANGELOG.md)
