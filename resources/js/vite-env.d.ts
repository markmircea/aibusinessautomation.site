/// <reference types="vite/client" />

interface Window {
    gtag: (
      type: string,
      action: string,
      params?: {
        send_to?: string;
        value?: number;
        currency?: string;
        transaction_id?: string;
        event_callback?: () => void;
      }
    ) => void;
  }
