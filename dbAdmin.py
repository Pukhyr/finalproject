import psycopg2


def createdb()-> None:
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        user='note',
        password='1234',
        dbname='finalproject'
    )
    with conn.cursor() as cursor:
        cursor.execute("""
CREATE TABLE IF NOT EXISTS question (
	id bigint PRIMARY KEY,
	text varchar(1000) NOT NULL,
	publish_data timestamp) 
        """)
        conn.commit()
    conn.close()


def createdbchoice()-> None:
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        user='note',
        password='1234',
        dbname='finalproject'
    )
    with conn.cursor() as cursor:
        cursor.execute("""
CREATE TABLE IF NOT EXISTS public.choice (
    id bigint NOT NULL,
    choice_text character varying(1000) COLLATE pg_catalog."default" NOT NULL,
    votes bigint,
    qeustion_id bigint NOT NULL,
    CONSTRAINT choice_pkey PRIMARY KEY (id),
    CONSTRAINT question_id FOREIGN KEY (qeustion_id)
        REFERENCES public.question (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.choice
    OWNER to postgres;
	 ) 
        """)
        conn.commit()
    conn.close()

def createstattable()-> None:
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        user='note',
        password='1234',
        dbname='finalproject'
    )
    with conn.cursor() as cursor:
        cursor.execute("""
CREATE TABLE IF NOT EXISTS public.stat (
    id bigint NOT NULL,
    tg_user_id integer NOT NULL,
    question_id bigint NOT NULL,
    choice_id bigint NOT NULL,
    CONSTRAINT stat_pkey PRIMARY KEY (id),
    CONSTRAINT choice_id FOREIGN KEY (choice_id)
        REFERENCES public.choice (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT question_id FOREIGN KEY (question_id)
        REFERENCES public.question (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.stat
    OWNER to postgres;
	 ) 
        """)
        conn.commit()
    conn.close()


if __name__=='__main__':
    createstattable()
    createdbchoice()
    createdb()
