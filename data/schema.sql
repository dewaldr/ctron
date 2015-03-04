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
  get_method text,
  get_cmd text,
  is_active integer not null
);
INSERT INTO "sensor" VALUES(1, '12v-monitor', '12V battery monitor', 'command', '/usr/local/bin/12vmon', 1);

CREATE TABLE relay (
  relay_id integer primary key autoincrement,
  name integer not null,
  description text not null,
  get_method text,
  get_cmd text,
  is_active integer not null
);
INSERT INTO "relay" VALUES(1, 'gate-open', 'Gate Open Actuator', 'gpio', '', 1);

