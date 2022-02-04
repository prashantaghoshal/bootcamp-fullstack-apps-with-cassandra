// THIS FILE WILL BE OVERWRITTEN. DO NOT MAKE ANY CHANGES
const cassandra = require("cassandra-driver");

// This is the Zip file you downloaded
const SECURE_CONNECT_BUNDLE =
  "/workspace/bootcamp-fullstack-apps-with-cassandra/secure-connect-workshops.zip";
// This is the "Client Id" value you obtained earlier
const USERNAME = "lRcMWccXybYmellPvXhKrrTF";
// This is the "Client Secret" value you obtained earlier
const PASSWORD = "B93npiGZaLMpXUqPOol3,j9UWJ--D+g8p2CcRMqHWX9q4SKlo1vB3Gv+PdQ7lSc-sA.KY7g5HD,0mjPgBf7AsZZXJm,m14EDchDHsiLwJnn,WNDro1bDyrFKF.nvN+Gt";
// This is the keyspace name
const KEYSPACE = "todos";

const client = new cassandra.Client({
  cloud: { secureConnectBundle: SECURE_CONNECT_BUNDLE },
  keyspace: KEYSPACE,
  credentials: { username: USERNAME, password: PASSWORD },
});

process.on("exit", () => client.shutdown());

module.exports = {
  client,
};
