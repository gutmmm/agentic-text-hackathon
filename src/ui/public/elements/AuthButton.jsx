import { useEffect } from "react";
import { useChatInteract } from "@chainlit/react-client";

export default function AuthButton() {
  const { sendMessage, replyMessage, clear } = useChatInteract();

  useEffect(() => {
    const handleMessage = (event) => {
      console.log("Received message:", event.data);

      if (event.data.action === "handle_auth_result") {
        const { status } = event.data.payload;
        const isSuccess = status === 'USER_AUTHORIZED';

        sendMessage({
          output:
            isSuccess ? "[AUTHORIZATION_SYSTEM_MESSAGE_SUCCESS] User authentication successful. Proceed" : "[AUTHORIZATION_SYSTEM_MESSAGE_FAILED] User authenticatio unssuccesful. Access denied",
          type: "assistant_message",
        });
      }
    };

    window.addEventListener("message", handleMessage);
    return () => window.removeEventListener("message", handleMessage);
  }, []);

  const handleAuth = async () => {
    const width = 500;
    const height = 600;
    const left = window.screen.width / 2 - width / 2;
    const top = window.screen.height / 2 - height / 2;

    window.open(
      "http://0.0.0.0:8001/authorize",
      "auth_window",
      `width=${width},height=${height},left=${left},top=${top}`
    );
  };

  return (
    <div>
      <button onClick={handleAuth}>Authorize</button>
    </div>
  );
}
