from typing import Dict

from titan.resource import Resource, Namespace
from titan.parseable_enum import ParseableEnum
from titan.props import Props, FlagProp, EnumProp, StringProp, BoolProp, AtBeforeProp


# class StreamType(ParseableEnum):
#     TABLE = "TABLE"
#     EXTERNAL_TABLE = "EXTERNAL TABLE"
#     STAGE = "STAGE"
#     VIEW = "VIEW"


class TableStream(Resource):
    """
    -- table
    CREATE [ OR REPLACE ] STREAM [IF NOT EXISTS]
      <name>
      [ COPY GRANTS ]
      ON TABLE <table_name>
      [ { AT | BEFORE } ( { TIMESTAMP => <timestamp> | OFFSET => <time_difference> | STATEMENT => <id> | STREAM => '<name>' } ) ]
      [ APPEND_ONLY = TRUE | FALSE ]
      [ SHOW_INITIAL_ROWS = TRUE | FALSE ]
      [ COMMENT = '<string_literal>' ]

    """

    resource_type = "STREAM"
    props = Props(
        copy_grants=FlagProp("copy grants"),
        on_table=StringProp("on table"),
        at_before=AtBeforeProp(),
        append_only=BoolProp("append_only"),
        show_initial_rows=BoolProp("show_initial_rows"),
        comment=StringProp("comment"),
    )

    name: str
    owner: str = None
    copy_grants: bool = None
    at_before: Dict[str, str] = None
    on_table: str
    append_only: bool = None
    show_initial_rows: bool = None
    comment: str = None


class ExternalTableStream(Resource):
    """
    -- External table
    CREATE [ OR REPLACE ] STREAM [IF NOT EXISTS]
      <name>
      [ COPY GRANTS ]
      ON EXTERNAL TABLE <external_table_name>
      [ { AT | BEFORE } ( { TIMESTAMP => <timestamp> | OFFSET => <time_difference> | STATEMENT => <id> | STREAM => '<name>' } ) ]
      [ INSERT_ONLY = TRUE ]
      [ COMMENT = '<string_literal>' ]
    """

    resource_type = "STREAM"
    props = Props(
        copy_grants=FlagProp("copy grants"),
        on_external_table=StringProp("on external table"),
        insert_only=BoolProp("insert_only"),
        comment=StringProp("comment"),
    )

    name: str
    owner: str = None
    copy_grants: bool = None
    on_external_table: str
    insert_only: bool = None
    comment: str = None


class StageStream(Resource):
    """
    -- Directory table
    CREATE [ OR REPLACE ] STREAM [IF NOT EXISTS]
      <name>
      [ COPY GRANTS ]
      ON STAGE <stage_name>
      [ COMMENT = '<string_literal>' ]
    """

    resource_type = "STREAM"
    props = Props(
        copy_grants=FlagProp("copy grants"),
        on_stage=StringProp("on stage"),
        comment=StringProp("comment"),
    )

    name: str
    owner: str = None
    copy_grants: bool = None
    on_stage: str
    comment: str = None


class ViewStream(Resource):
    """
    -- View
    CREATE [ OR REPLACE ] STREAM [IF NOT EXISTS]
      <name>
      [ COPY GRANTS ]
      ON VIEW <view_name>
      [ { AT | BEFORE } ( { TIMESTAMP => <timestamp> | OFFSET => <time_difference> | STATEMENT => <id> | STREAM => '<name>' } ) ]
      [ APPEND_ONLY = TRUE | FALSE ]
      [ SHOW_INITIAL_ROWS = TRUE | FALSE ]
      [ COMMENT = '<string_literal>' ]
    """

    resource_type = "STREAM"
    props = Props(
        copy_grants=FlagProp("copy grants"),
        on_view=StringProp("on view"),
        append_only=BoolProp("append_only"),
        show_initial_rows=BoolProp("show_initial_rows"),
        comment=StringProp("comment"),
    )

    name: str
    owner: str = None
    copy_grants: bool = None
    on_view: str
    append_only: bool = None
    show_initial_rows: bool = None
    comment: str = None


# StreamTypeMap = {
#     StreamType.TABLE: TableStream,
#     StreamType.EXTERNAL_TABLE: ExternalTableStream,
#     StreamType.STAGE: StageStream,
#     StreamType.VIEW: ViewStream,
# }