/* tslint:disable */
/* eslint-disable */
/**
/* This file was automatically generated from pydantic models by running pydantic2ts.
/* Do not modify it by hand - just update the pydantic models and then re-run the script
*/

export type SentMessageType = "user-initiated" | "connect-initiated";

export interface SentMessage {
  sent_message_type: SentMessageType;
}
