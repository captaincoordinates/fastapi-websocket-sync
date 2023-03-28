/* tslint:disable */
/* eslint-disable */
/**
/* This file was automatically generated from pydantic models by running pydantic2ts.
/* Do not modify it by hand - just update the pydantic models and then re-run the script
*/

export type PushType = "connected_to" | "notified_by";
export type SentMessageType = "user-initiated" | "connect-initiated";

export interface PushReport {
  push_type: PushType;
  host: string;
  pid: number;
  initiated_by: SentMessageType;
  report_time?: number;
}
