CREATE TABLE IF NOT EXISTS public.service_revisions
(
	id bigint NOT NULL,
	entity_uuid character varying(255) NOT NULL,
	revision_uuid character varying(255) NOT NULL,
	entity_type VARCHAR NOT NULL,
	service_name VARCHAR NOT NULL,
	status int NOT NULL,
	created_at timestamp without time zone,
    updated_at timestamp without time zone,
	
	CONSTRAINT service_revisions_pkey PRIMARY KEY (id)
);

CREATE INDEX IF NOT EXISTS service_revisions_entity_uuid
    ON public.service_revisions USING btree
    (revision_uuid ASC NULLS LAST)
    TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.service_revisions
    OWNER to ordering_user;