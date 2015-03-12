CREATE TABLE user (
  user_id integer primary key autoincrement,
  username text not null,
  email text not null,
  pw_hash text not null
);
INSERT INTO "user" VALUES(1,'sysop','sysop@robot7.net','pbkdf2:sha1:1000$5GichJyN$9ff3f0f129256c02e388d8645ede34f65d87dc11');


CREATE TABLE sensor (
  sensor_id integer primary key autoincrement,
  name integer not null,
  description text not null,
  read_method text,
  read_cmd text,
  is_active integer not null
);
INSERT INTO "sensor" VALUES(1, '12v-monitor', '12V battery monitor', 'command', '/usr/local/bin/12vmon', 1);
INSERT INTO "sensor" VALUES(NULL, 'temp-monitor', 'In-enclosure temperature monitor', 'command', '/usr/local/bin/tempmon', 1);
INSERT INTO "sensor" VALUES(NULL, 'light-monitor', 'Ambient light intensity monitor', 'command', '/usr/local/bin/lightmon', 1);

CREATE TABLE relay (
  relay_id integer primary key autoincrement,
  name integer not null,
  description text not null,
  actuate_method text,
  actuate_cmd text,
  is_active integer not null
);
INSERT INTO "relay" VALUES(1, 'gate-open', 'Gate open actuator', 'function', 'pulse-gpio(0,3)', 1);
INSERT INTO "relay" VALUES(NULL, 'gate-close', 'Gate close actuator', 'function', 'pulse-gpio(1,3)', 1);
INSERT INTO "relay" VALUES(NULL, 'gate-unlock', 'Gate unlock actuator', 'function', 'pulse-gpio(2,3)', 1);
INSERT INTO "relay" VALUES(NULL, 'gate-lock', 'Gate lock actuator', 'function', 'pulse-gpio(3,3)', 1);

