from typing import Any
from uuid import UUID

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import BaseMessage


class BaseCallback(BaseCallbackHandler):
    def on_chain_start(
        self,
        serialized: dict[str, Any],
        inputs: dict[str, Any],
        run_id: UUID,
        **kwargs: Any,
    ):

        parent_run_id = kwargs["parent_run_id"]

        if parent_run_id is None:
            print(f"Начало корневой цепочки: {run_id}")
        else:
            print(f"start: {parent_run_id} -> {run_id}")
            print(inputs)
        print()
        print(serialized)


    def on_chain_end(
        self,
        outputs: dict[str, Any],
        run_id: UUID,
        parent_run_id: UUID | None = None,
        **kwargs: Any,
    ):

        parent_run_id = kwargs["parent_run_id"]

        if parent_run_id is None:
            print(f"Начало корневой цепочки: {run_id}")
        else:
            print(f"end: {parent_run_id} -> {run_id}")
            print(outputs)
        print()

    def on_chat_model_start(
        self,
        serialized: dict[str, Any],
        messages: list[list[BaseMessage]],
        **kwargs: Any
    ):
        print(f"start LLM")
        print(messages)
        print()


class ErrorHandler(BaseCallbackHandler):
    def on_chain_error(
        self,
        error: BaseException,
        *,
        run_id: UUID,
        parent_run_id: UUID | None = None,
        **kwargs: Any,
    ):
        print(f"Error: {error} / {kwargs['tags']}")