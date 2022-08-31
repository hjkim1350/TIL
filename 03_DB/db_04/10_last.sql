-- SQLite

-- AC/DC의 모든 앨범 조회
-- 1) 테이블이 무엇이 있는지 조회
.tables

-- albums          employees       invoices        playlists
-- artists         genres          media_types     tracks
-- customers       invoice_items   playlist_track

-- 2) 앨범 조회가 궁극적인 목적이므로 앨범 테이블 부터 확인
.schema albums

-- CREATE TABLE IF NOT EXISTS "albums"
-- (
--     [AlbumId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
--     [Title] NVARCHAR(160)  NOT NULL,
--     [ArtistId] INTEGER  NOT NULL,
--     FOREIGN KEY ([ArtistId]) REFERENCES "artists" ([ArtistId])
--                 ON DELETE NO ACTION ON UPDATE NO ACTION
-- );
-- CREATE INDEX [IFK_AlbumArtistId] ON "albums" ([ArtistId]);

-- 3) ArtistId를 가져와야 할 것으로 보이는데, 일단 해당 테이블의 실 데이터를 확인
SELECT * FROM albums LIMIT 1;

-- AlbumId  Title                                  ArtistId
-- -------  -------------------------------------  --------
-- 1        For Those About To Rock We Salute You  1

-- 4) ArtistId가 담겼을 것 같은 artists 테이블 스키마 및 실 데이터 조회
.schema artists

-- CREATE TABLE IF NOT EXISTS "artists"
-- (
--     [ArtistId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
--     [Name] NVARCHAR(120)
-- );

SELECT * FROM artists LIMIT 1;
-- ArtistId  Name
-- --------  -----
-- 1         AC/DC

-- 5) AC/DC의 ArtistId 조회
SELECT ArtistId FROM artists WHERE Name ='AC/DC';

-- ArtistId
-- --------
-- 1       

-- 6) 앨범 정보가 담겼을 것 같은 테이블 스키마 및 실 데이터 조회
.schema albums
-- CREATE TABLE IF NOT EXISTS "albums"
-- (
--     [AlbumId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
--     [Title] NVARCHAR(160)  NOT NULL,
--     [ArtistId] INTEGER  NOT NULL,
--     FOREIGN KEY ([ArtistId]) REFERENCES "artists" ([ArtistId])
--                 ON DELETE NO ACTION ON UPDATE NO ACTION
-- );
-- CREATE INDEX [IFK_AlbumArtistId] ON "albums" ([ArtistId]);

SELECT * FROM albums LIMIT 1;

-- AlbumId  Title                                  ArtistId
-- -------  -------------------------------------  --------
-- 1        For Those About To Rock We Salute You  1

-- 7) 이제까지 얻은 정보로 AC/DC의 모든 앨범 조회
SELECT Title FROM albums WHERE AlbumId = (SELECT ArtistId FROM artists WHERE Name = 'AC/DC');
Title
-------------------------------------
For Those About To Rock We Salute You