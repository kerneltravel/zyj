create table books(id int primary key ,partids text,tags text, name text, author text, dynasty text, year text);
create virtual table books_vt using fts4(content="books",tokenize=icu zh_CN, partids, tags, name,author,dynasty,year);

create table bkparts(id integer primary key, name text, tags text, articleids text);
create virtual table bkparts_vt using fts4(content="bkparts",tokenize=icu zh_CN,,name,tags,articleids);

create table articles (id integer primary key, title text, tags text, content text);
create virtual table articles_vt using fts4(content="articles",tokenize=icu zh_CN,title,content,tags);

CREATE TRIGGER books_bu BEFORE UPDATE ON books BEGIN
  DELETE FROM books_vt WHERE docid=old.rowid;
END;
CREATE TRIGGER books_bd BEFORE DELETE ON books BEGIN
  DELETE FROM books_vt WHERE docid=old.rowid;
END;

CREATE TRIGGER books_au AFTER UPDATE ON books BEGIN
  INSERT INTO books_vt(docid, partids, tags, name) VALUES(new.rowid, new.partids, new.tags, new.name);
END;
CREATE TRIGGER books_ai AFTER INSERT ON books BEGIN
  INSERT INTO books_vt(docid, partids, tags, name) VALUES(new.rowid, new.partids, new.tags, new.name);
END;


CREATE TRIGGER bkparts_bu BEFORE UPDATE ON bkparts BEGIN
  DELETE FROM bkparts_vt WHERE docid=old.rowid;
END;
CREATE TRIGGER bkparts_bd BEFORE DELETE ON bkparts BEGIN
  DELETE FROM bkparts_vt WHERE docid=old.rowid;
END;

CREATE TRIGGER bkparts_au AFTER UPDATE ON bkparts BEGIN
  INSERT INTO bkparts_vt(docid, name, tags, articleids) VALUES(new.rowid, new.name, new.tags, new.articleids);
END;
CREATE TRIGGER bkparts_ai AFTER INSERT ON bkparts BEGIN
  INSERT INTO bkparts_vt(docid, name, tags, articleids) VALUES(new.rowid, new.name, new.tags, new.articleids);
END;


CREATE TRIGGER articles_bu BEFORE UPDATE ON articles BEGIN
  DELETE FROM articles_vt WHERE docid=old.rowid;
END;
CREATE TRIGGER articles_bd BEFORE DELETE ON articles BEGIN
  DELETE FROM articles_vt WHERE docid=old.rowid;
END;

CREATE TRIGGER articles_au AFTER UPDATE ON articles BEGIN
  INSERT INTO articles_vt(docid, title, tags, content) VALUES(new.rowid, new.title, new.tags, new.content);
END;
CREATE TRIGGER articles_ai AFTER INSERT ON articles BEGIN
  INSERT INTO articles_vt(docid, title, tags, content) VALUES(new.rowid, new.title, new.tags, new.content);
END;

create table bookmarks(id int primary key ,showname text,comments text,artids text,modifiedate text);