-- Table: public.books

-- DROP TABLE public.books;

CREATE TABLE public.books
(
    id integer NOT NULL DEFAULT nextval('books_id_seq'::regclass),
    code character varying(100) COLLATE pg_catalog."default" NOT NULL,
    title character varying(100) COLLATE pg_catalog."default" NOT NULL,
    author character varying(100) COLLATE pg_catalog."default",
    status character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT books_pkey PRIMARY KEY (id),
    CONSTRAINT code_unique UNIQUE (code)
)

TABLESPACE pg_default;

ALTER TABLE public.books
    OWNER to postgres;


-- Table: public.book_issue

-- DROP TABLE public.book_issue;

CREATE TABLE public.book_issue
(
    id integer NOT NULL DEFAULT nextval('book_issue_id_seq'::regclass),
    code text COLLATE pg_catalog."default" NOT NULL,
    member_id text COLLATE pg_catalog."default",
    issue_date date,
    issue_return date,
    CONSTRAINT book_issue_pkey PRIMARY KEY (id),
    CONSTRAINT book_code_fk FOREIGN KEY (code)
        REFERENCES public.books (code) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.book_issue
    OWNER to postgres;
